# Deployment Guide - Lead Generation API

## Overview
This guide explains how to deploy the Lead Generation API to Shuttle.rs with PostgreSQL database.

## Prerequisites
- Shuttle CLI installed: `cargo install cargo-shuttle`
- Shuttle account (free): https://www.shuttle.rs/

## Local Development

### 1. Install Shuttle CLI
```bash
cargo install cargo-shuttle
```

### 2. Login to Shuttle
```bash
cargo shuttle login
```

### 3. Run Locally with Shuttle
```bash
cargo shuttle run
```

This will:
- Start a local PostgreSQL database
- Run the API on `http://localhost:8000`
- Automatically create the `leads` table

### 4. Test the API
```bash
# Submit a test lead
curl -X POST http://localhost:8000/leads \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "email=test@example.com&niche=1"

# View all leads (JSON)
curl http://localhost:8000/leads/list

# View admin page (HTML)
open http://localhost:8000/admin
```

## Deployment to Shuttle

### 1. Initialize Shuttle Project
```bash
cargo shuttle project start
```

### 2. Deploy
```bash
cargo shuttle deploy
```

This will:
- Build your application
- Provision a PostgreSQL database
- Deploy to Shuttle's infrastructure
- Provide you with a public URL (e.g., `https://your-app.shuttleapp.rs`)

### 3. Update Generated Sites
After deployment, update the API URL in `src/generator.rs`:

```rust
const API_URL: &str = "https://your-app.shuttleapp.rs/leads";
```

Then regenerate the sites:
```bash
cargo run --bin generator
```

### 4. Deploy Static Sites
Upload the `output/` directory to:
- **GitHub Pages** (free, recommended)
- **Netlify** (free)
- **Vercel** (free)
- **Cloudflare Pages** (free)

## Environment Variables
No environment variables needed! Shuttle handles the database connection automatically.

## Database Access

### View Logs
```bash
cargo shuttle logs
```

### Access Database
Shuttle provides a PostgreSQL connection string in your project dashboard.

## Endpoints

- `GET /` - API info
- `POST /leads` - Submit a lead (returns thank you page)
- `GET /leads/list` - List all leads (JSON)
- `GET /admin` - Admin dashboard (HTML table)
- `GET /about` - About page

## Monitoring

Check your deployment status:
```bash
cargo shuttle status
```

View recent logs:
```bash
cargo shuttle logs --latest
```

## Cost
- **Shuttle**: Free tier includes PostgreSQL database
- **Static hosting**: Free on GitHub Pages, Netlify, Vercel, or Cloudflare Pages

## Troubleshooting

### Build fails
```bash
# Clean and rebuild
cargo clean
rm Cargo.lock
cargo shuttle deploy
```

### Database issues
Shuttle automatically provisions and manages the PostgreSQL database. If you need to reset it, you can delete and recreate the project.

### CORS issues
The API allows all origins by default. If you need to restrict this, modify the CORS configuration in `src/main.rs`.

## Next Steps
1. Deploy the API to Shuttle
2. Update the API URL in the site generator
3. Regenerate all 50 landing pages
4. Deploy static sites to GitHub Pages
5. Monitor leads via `/admin` endpoint
