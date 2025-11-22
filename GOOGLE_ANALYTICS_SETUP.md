# Google Analytics Setup Guide

## Step 1: Create Google Analytics Account

1. Go to https://analytics.google.com/
2. Click "Start measuring"
3. Enter account name: "Lead Gen Sites"
4. Click "Next"

## Step 2: Create Property

1. Property name: "Lead Gen Network"
2. Time zone: Your timezone
3. Currency: Your currency
4. Click "Next"

## Step 3: Set Up Data Stream

1. Select "Web"
2. Website URL: `https://blatik.github.io`
3. Stream name: "Lead Gen Sites"
4. Click "Create stream"

## Step 4: Get Measurement ID

You'll see a **Measurement ID** like: `G-XXXXXXXXXX`

**Copy this ID!**

## Step 5: Add to Your Sites

### Option A: Manual (Quick Test)

Add this code to each landing page's `<head>` section:

```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

Replace `G-XXXXXXXXXX` with your actual Measurement ID.

### Option B: Automated (Recommended)

1. Open `templates/landing.html`
2. Add the Google Analytics code in the `<head>` section
3. Run `cargo run --bin generator` to regenerate all sites
4. Commit and push to GitHub

## Step 6: Verify Tracking

1. Visit one of your sites: https://blatik.github.io/lead-gen-sites/site_1/
2. Go to Google Analytics → Reports → Realtime
3. You should see yourself as an active user!

## What You'll Track

✅ **Page views** - Which landing pages get the most traffic  
✅ **User behavior** - How long visitors stay  
✅ **Traffic sources** - Where visitors come from (Google, social media, etc.)  
✅ **Conversions** - Track form submissions (requires event setup)  
✅ **Demographics** - Age, location, interests  

## Advanced: Track Form Submissions

Add this to your form's submit event:

```javascript
gtag('event', 'generate_lead', {
  'event_category': 'engagement',
  'event_label': 'email_form',
  'niche': document.getElementById('niche').value
});
```

## Next Steps

1. Get your Measurement ID from Google Analytics
2. Let me know the ID and I'll update the templates
3. Regenerate sites with `cargo run --bin generator`
4. Push to GitHub
5. Start tracking!

## Cost

**Free** - Google Analytics is completely free for up to 10 million events per month.
