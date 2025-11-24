# Quick Start Guide

## 🚀 Deploy in 5 Minutes

### 1. Install Wrangler
```bash
npm install -g wrangler
wrangler login
```

### 2. Create Database
```bash
cd /Users/blatik/Documents/rust_apps/lead_gen_0ae77895
wrangler d1 create rustdev-leads
```

**Copy the `database_id` and paste it in `wrangler.toml` line 9**

### 3. Initialize Database
```bash
wrangler d1 execute rustdev-leads --file=schema.sql
```

### 4. Set Telegram Token
```bash
wrangler secret put TELEGRAM_BOT_TOKEN
```
Paste: `8574716516:AAEzjpntgYn3vtrmg0TNK-lV1MuE7pLY7gM`

### 5. Test Locally
```bash
wrangler dev
```

Open another terminal and test:
```bash
curl -X POST http://localhost:8787/api/leads \
  -d "email=test@example.com&niche=1&niche_name=Test"
```

Check your Telegram! 📱

### 6. Deploy
```bash
wrangler deploy
```

### 7. Deploy to Cloudflare Pages

**Option A - Via CLI:**
```bash
wrangler pages deploy . --project-name=rustdev-network
```

**Option B - Via Dashboard:**
1. Go to https://dash.cloudflare.com
2. Pages → Create project
3. Connect GitHub: `Blatik/rustdev-network`
4. Deploy

---

## ✅ Done!

Your site will be live at:
- `https://rustdev-network.pages.dev`
- Or your custom domain

All forms now send to Cloudflare Worker → D1 Database → Telegram! 🎉
