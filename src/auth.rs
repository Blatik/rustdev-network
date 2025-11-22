use axum::{
    extract::Request,
    http::{StatusCode, header},
    middleware::Next,
    response::Response,
    extract::State,
};
use sqlx::SqlitePool;
use crate::db;

#[derive(Clone)]
pub struct AppState {
    pub pool: SqlitePool,
}

pub async fn auth_middleware(
    State(state): State<AppState>,
    req: Request,
    next: Next,
) -> Result<Response, StatusCode> {
    // Skip auth for health check or public routes if any
    if req.uri().path() == "/" {
        return Ok(next.run(req).await);
    }

    let auth_header = req.headers()
        .get(header::AUTHORIZATION)
        .and_then(|header| header.to_str().ok());

    let auth_header = if let Some(auth_header) = auth_header {
        auth_header
    } else {
        return Err(StatusCode::UNAUTHORIZED);
    };

    if !auth_header.starts_with("Bearer ") {
        return Err(StatusCode::UNAUTHORIZED);
    }

    let key = &auth_header[7..];

    match db::validate_key(&state.pool, key).await {
        Ok(true) => Ok(next.run(req).await),
        Ok(false) => Err(StatusCode::UNAUTHORIZED),
        Err(_) => Err(StatusCode::INTERNAL_SERVER_ERROR),
    }
}
