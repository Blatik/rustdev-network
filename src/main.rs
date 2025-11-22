use axum::{
    extract::State,
    http::{Method, StatusCode},
    response::Html,
    routing::{get, post},
    Router,
    Json,
};
use lettre::message::header::ContentType;
use lettre::transport::smtp::authentication::Credentials;
use lettre::{Message, SmtpTransport, Transport};
use serde::{Deserialize, Serialize};
use shuttle_runtime::SecretStore;
use sqlx::PgPool;
use tower_http::cors::{Any, CorsLayer};

#[derive(Debug, Deserialize)]
struct LeadForm {
    email: String,
    niche: String,
    niche_name: Option<String>,
}

#[derive(Debug, Serialize, sqlx::FromRow)]
struct Lead {
    id: i32,
    email: String,
    niche: String,
    niche_name: Option<String>,
    created_at: chrono::NaiveDateTime,
}

#[derive(Clone)]
struct AppState {
    pool: PgPool,
    secret_store: SecretStore,
}

#[shuttle_runtime::main]
async fn main(
    #[shuttle_shared_db::Postgres] pool: PgPool,
    #[shuttle_runtime::Secrets] secret_store: SecretStore,
) -> shuttle_axum::ShuttleAxum {
    // Initialize database table
    sqlx::query(
        "CREATE TABLE IF NOT EXISTS leads (
            id SERIAL PRIMARY KEY,
            email TEXT NOT NULL,
            niche TEXT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT NOW()
        )",
    )
    .execute(&pool)
    .await
    .expect("Failed to create table");

    // Add niche_name column if it doesn't exist
    let _ = sqlx::query("ALTER TABLE leads ADD COLUMN IF NOT EXISTS niche_name TEXT")
        .execute(&pool)
        .await;

    // Setup CORS - Allow All (Simplest for debugging)
    let cors = CorsLayer::new()
        .allow_origin(Any)
        .allow_methods(Any)
        .allow_headers(Any);

    // Build router
    let state = AppState { pool, secret_store };
    let app = Router::new()
        .route("/", get(root))
        .route("/leads", post(submit_lead))
        .route("/leads/list", get(list_leads))
        .route("/admin", get(admin_page))
        .route("/about", get(about_page))
        .layer(cors)
        .with_state(state);

    Ok(app.into())
}

async fn root() -> Html<&'static str> {
    Html("<h1>Lead Generation API</h1><p>POST to /leads to submit a lead</p>")
}

async fn submit_lead(
    State(state): State<AppState>,
    axum::Form(form): axum::Form<LeadForm>,
) -> Result<Html<String>, StatusCode> {
    println!("Received lead: {:?}", form);
    
    let niche_name = form.niche_name.clone().unwrap_or_else(|| "Unknown".to_string());
    
    let _result = sqlx::query("INSERT INTO leads (email, niche, niche_name) VALUES ($1, $2, $3)")
        .bind(&form.email)
        .bind(&form.niche)
        .bind(&niche_name)
        .execute(&state.pool)
        .await
        .map_err(|_| StatusCode::INTERNAL_SERVER_ERROR)?;

    // Send Email Notification
    if let Some(gmail_password) = state.secret_store.get("GMAIL_PASSWORD") {
        if let Some(gmail_user) = state.secret_store.get("GMAIL_USER") {
            let email = Message::builder()
                .from(format!("RustDev Network <{}>", gmail_user).parse().unwrap())
                .to(gmail_user.parse().unwrap()) // Send to yourself
                .subject(format!("New Lead: {}", niche_name))
                .header(ContentType::TEXT_PLAIN)
                .body(format!("New lead received!\n\nEmail: {}\nNiche: {}\nSource: {}", form.email, form.niche, niche_name))
                .unwrap();

            let creds = Credentials::new(gmail_user.clone(), gmail_password);

            // Open a remote connection to gmail
            let mailer = SmtpTransport::relay("smtp.gmail.com")
                .unwrap()
                .credentials(creds)
                .build();

            match mailer.send(&email) {
                Ok(_) => println!("Email sent successfully!"),
                Err(e) => println!("Could not send email: {:?}", e),
            }
        }
    } else {
        println!("GMAIL_PASSWORD not set, skipping email notification");
    }

    // Redirect to thank-you page
    Ok(Html(r#"
        <!DOCTYPE html>
        <html>
            <head>
                <meta http-equiv="refresh" content="0; url=https://blatik.github.io/rustdev-network/thank-you.html" />
            </head>
            <body>
                <p>Redirecting to thank you page...</p>
            </body>
        </html>
    "#.to_string()))
}

async fn about_page() -> Result<Html<String>, StatusCode> {
    Ok(Html("<h1>About Us</h1><p>We are a team of Rust developers.</p>".to_string()))
}

async fn list_leads(
    State(state): State<AppState>,
) -> Result<Json<Vec<Lead>>, StatusCode> {
    let leads = sqlx::query_as::<_, Lead>("SELECT id, email, niche, niche_name, created_at FROM leads ORDER BY created_at DESC")
        .fetch_all(&state.pool)
        .await
        .map_err(|_| StatusCode::INTERNAL_SERVER_ERROR)?;

    Ok(Json(leads))
}

async fn admin_page(
    State(state): State<AppState>,
) -> Result<Html<String>, StatusCode> {
    let leads = sqlx::query_as::<_, Lead>("SELECT id, email, niche, niche_name, created_at FROM leads ORDER BY created_at DESC")
        .fetch_all(&state.pool)
        .await
        .map_err(|_| StatusCode::INTERNAL_SERVER_ERROR)?;

    let mut rows = String::new();
    for lead in leads {
        let niche_display = lead.niche_name.unwrap_or_else(|| lead.niche.clone());
        rows.push_str(&format!(
            "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>",
            lead.id, lead.email, niche_display, lead.created_at
        ));
    }

    let html = format!(r#"
<!DOCTYPE html>
<html>
<head>
    <title>Admin - Leads</title>
    <style>
        body {{ font-family: sans-serif; padding: 20px; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        tr:nth-child(even) {{ background-color: #f9f9f9; }}
    </style>
</head>
<body>
    <h1>Collected Leads</h1>
    <table>
        <tr>
            <th>ID</th>
            <th>Email</th>
            <th>Niche / Source</th>
            <th>Date</th>
        </tr>
        {}
    </table>
</body>
</html>
    "#, rows);

    Ok(Html(html))
}
