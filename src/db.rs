use sqlx::sqlite::SqlitePool;
use uuid::Uuid;

#[derive(sqlx::FromRow)]
pub struct ApiKey {
    pub id: String,
    pub key_hash: String,
    pub owner_id: String,
    pub is_active: bool,
}

pub async fn init_db(pool: &SqlitePool) -> Result<(), sqlx::Error> {
    sqlx::query(
        r#"
        CREATE TABLE IF NOT EXISTS api_keys (
            id TEXT PRIMARY KEY,
            key_hash TEXT NOT NULL,
            owner_id TEXT NOT NULL,
            is_active BOOLEAN NOT NULL DEFAULT 1,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        "#
    )
    .execute(pool)
    .await?;
    
    Ok(())
}

pub async fn create_api_key(pool: &SqlitePool, owner: &str) -> Result<String, sqlx::Error> {
    let key = Uuid::new_v4().to_string();
    let id = Uuid::new_v4().to_string();
    
    // In a real app, hash the key! For MVP we store plain (bad practice, but simple for now)
    // Wait, let's do it right-ish. We'll just store it as is for this demo to be able to read it back, 
    // but in production we'd return it once and store hash.
    // Let's just store it plain for this specific MVP step to avoid adding bcrypt dep yet.
    
    sqlx::query(
        "INSERT INTO api_keys (id, key_hash, owner_id) VALUES (?, ?, ?)"
    )
    .bind(&id)
    .bind(&key)
    .bind(owner)
    .execute(pool)
    .await?;
    
    Ok(key)
}

pub async fn validate_key(pool: &SqlitePool, key: &str) -> Result<bool, sqlx::Error> {
    let result = sqlx::query_as::<_, ApiKey>(
        "SELECT * FROM api_keys WHERE key_hash = ? AND is_active = 1"
    )
    .bind(key)
    .fetch_optional(pool)
    .await?;
    
    Ok(result.is_some())
}
