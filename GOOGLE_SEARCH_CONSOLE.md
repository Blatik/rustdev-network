# Google Search Console Setup Guide

## Step 1: Add Your Site to Google Search Console

1. **Go to Google Search Console:**
   https://search.google.com/search-console

2. **Click "Add Property"**

3. **Choose "URL prefix"** and enter:
   ```
   https://blatik.github.io/rustdev-network/
   ```

4. **Verify Ownership** - Choose one method:

### Method A: HTML File Upload (Recommended)

1. Google will give you an HTML file (e.g., `google1234567890abcdef.html`)
2. Download the file
3. Copy it to your `output/` directory:
   ```bash
   cp ~/Downloads/google1234567890abcdef.html /Users/blatik/Downloads/rust_apps/lead_gen_0ae77895/output/
   ```
4. Push to GitHub:
   ```bash
   cd /Users/blatik/Downloads/rust_apps/lead_gen_0ae77895/output
   git add google*.html
   git commit -m "Add Google Search Console verification"
   git push
   ```
5. Wait 1 minute, then click "Verify" in Google Search Console

### Method B: HTML Tag (Alternative)

1. Google will give you a meta tag like:
   ```html
   <meta name="google-site-verification" content="YOUR_CODE_HERE" />
   ```
2. I can add this to all your pages - just give me the code!

## Step 2: Submit Your Sitemap

After verification:

1. **In Google Search Console**, go to **Sitemaps** (left sidebar)

2. **Add new sitemap:**
   ```
   https://blatik.github.io/rustdev-network/sitemap.xml
   ```

3. Click **Submit**

4. Google will start indexing your 50+ pages!

## Step 3: Monitor Your SEO Performance

### What to Check:

**Performance Tab:**
- Total clicks
- Total impressions
- Average CTR (Click-Through Rate)
- Average position in search results

**Coverage Tab:**
- How many pages are indexed
- Any errors or warnings

**Enhancements Tab:**
- Mobile usability
- Core Web Vitals

## Step 4: Request Indexing for Important Pages

For faster indexing of key pages:

1. Go to **URL Inspection** (top bar)
2. Enter a URL, e.g.:
   ```
   https://blatik.github.io/rustdev-network/high-performance-rest-api-development/
   ```
3. Click **Request Indexing**
4. Repeat for your top 10-20 pages

## Expected Timeline

- **Verification**: Instant
- **Sitemap processing**: 1-2 days
- **First pages indexed**: 2-7 days
- **Full site indexed**: 1-4 weeks
- **Ranking improvements**: 4-12 weeks

## Your Sitemap Contains

✅ 50 landing pages (all services)  
✅ About page  
✅ Thank you page  
✅ Home page  

**Total**: 53 pages for Google to index

## Pro Tips

1. **Submit to Bing too**: https://www.bing.com/webmasters
   - Use the same sitemap URL
   - Bing powers DuckDuckGo and other search engines

2. **Check mobile-friendliness**:
   - All your pages are already mobile-responsive ✅

3. **Monitor Core Web Vitals**:
   - Your static HTML loads super fast ✅

4. **Create backlinks**:
   - Share your services on Reddit, LinkedIn, Twitter
   - List on directories like Product Hunt, Indie Hackers

## Next Steps After Setup

1. ✅ Verify site ownership
2. ✅ Submit sitemap
3. ✅ Request indexing for top pages
4. 📊 Wait 7 days
5. 📈 Check Performance report
6. 🔄 Optimize based on data

## Need Help?

If you get stuck, let me know:
- Which verification method you chose
- Any error messages
- Screenshots of issues

I can help troubleshoot!
