# Cloudflare Pages + Workers Deployment Guide

## 📋 Prerequisites

- Cloudflare account
- Node.js installed
- Wrangler CLI installed (`npm install -g wrangler`)

---

## 🚀 Step 1: Install Wrangler

```bash
npm install -g wrangler
```

Login to Cloudflare:
```bash
wrangler login
```

---

## 🗄️ Step 2: Create D1 Database

```bash
cd /Users/blatik/Documents/rust_apps/lead_gen_0ae77895
wrangler d1 create rustdev-leads
```

**Copy the `database_id` from the output and update `wrangler.toml`:**

```toml
[[d1_databases]]
binding = "DB"
database_name = "rustdev-leads"
database_id = "YOUR_DATABASE_ID_HERE"  # ← Paste here
```

---

## 📊 Step 3: Initialize Database Schema

```bash
wrangler d1 execute rustdev-leads --file=schema.sql
```

---

## 🔐 Step 4: Set Telegram Bot Token (Secret)

```bash
wrangler secret put TELEGRAM_BOT_TOKEN
```

When prompted, paste:
```
8574716516:AAEzjpntgYn3vtrmg0TNK-lV1MuE7pLY7gM
```

---

## 🧪 Step 5: Test Locally

```bash
wrangler dev
```

Test the API:
```bash
curl -X POST http://localhost:8787/api/leads \
  -d "email=test@example.com&niche=1&niche_name=Test Service"
```

Check your Telegram for notification! 📱

---

## 🌐 Step 6: Deploy Worker

```bash
wrangler deploy
```

**Copy the Worker URL** (e.g., `https://rustdev-network-worker.YOUR_SUBDOMAIN.workers.dev`)

---

## 📄 Step 7: Deploy to Cloudflare Pages

### Option A: Via Wrangler

```bash
wrangler pages deploy . --project-name=rustdev-network
```

### Option B: Via Cloudflare Dashboard

1. Go to [Cloudflare Dashboard](https://dash.cloudflare.com)
2. Click **Pages** → **Create a project**
3. Connect your GitHub repo: `Blatik/rustdev-network`
4. Build settings:
   - **Build command**: (leave empty - static site)
   - **Build output directory**: `/`
5. Click **Save and Deploy**

---

## 🔗 Step 8: Update Forms (Automated)

I'll create a script to update all HTML forms automatically.

---

## ✅ Verification

1. Visit your Cloudflare Pages URL
2. Submit a test lead
3. Check Telegram for notification
4. Verify lead in database:
   ```bash
   wrangler d1 execute rustdev-leads --command="SELECT * FROM leads"
   ```

---

## 🎯 Next Steps

After deployment, you'll have:
- ✅ Static site on Cloudflare Pages
- ✅ API on Cloudflare Workers
- ✅ Database on Cloudflare D1
- ✅ Telegram notifications
- ✅ Free hosting (Cloudflare Free Tier)

**Estimated time**: 10-15 minutes
