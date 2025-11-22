# 🔧 Google Apps Script Troubleshooting

## ❌ Current Error

The Google Apps Script webhook is returning:
```
TypeError: "" is not a function (rad: 1, fil: Code)
```

This error means there's a syntax issue in the Google Apps Script code.

## 🛠️ How to Fix

### Step 1: Open Your Google Apps Script

1. Go to your Google Sheet: **"Lead Gen Database"**
2. Click **Extensions → Apps Script**

### Step 2: Replace the Code

Delete ALL existing code and paste this EXACT code:

```javascript
function doPost(e) {
  try {
    // Get data from POST request
    var data = JSON.parse(e.postData.contents);
    
    // Open the active spreadsheet
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    
    // Add new row with data
    sheet.appendRow([
      data.id,
      data.email,
      data.niche,
      data.created_at,
      data.niche_name || ''
    ]);
    
    // Return success response
    return ContentService.createTextOutput(JSON.stringify({
      'status': 'success',
      'message': 'Lead added to Google Sheets'
    })).setMimeType(ContentService.MimeType.JSON);
    
  } catch(error) {
    // Return error response
    return ContentService.createTextOutput(JSON.stringify({
      'status': 'error',
      'message': error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}
```

### Step 3: Save and Redeploy

1. Click **Save** (💾 icon)
2. Click **Deploy → Manage deployments**
3. Click the **Edit** (✏️) icon next to your existing deployment
4. Click **Version → New version**
5. Click **Deploy**
6. Copy the new Web app URL (it might be the same)

### Step 4: Test the Script

Before deploying, you can test it:

1. In Apps Script, click **Run → testDoPost** (if you added the test function)
2. Or just save and redeploy

## ⚠️ Common Issues

### Issue 1: Wrong Function Name
- Make sure the function is called `doPost` (case-sensitive)
- It must be exactly `doPost`, not `DoPost` or `dopost`

### Issue 2: Deployment Settings
- **Execute as**: Me (your email)
- **Who has access**: **Anyone** ← This is critical!

### Issue 3: Sheet Headers
Make sure your Google Sheet has these headers in row 1:
- A1: `ID`
- B1: `Email`
- C1: `Niche`
- D1: `Date`
- E1: `Niche Name`

## 🧪 Test After Fixing

Once you've fixed the script, let me know and I'll test it again!

Or you can test it yourself with this curl command:

```bash
curl -X POST "YOUR_WEBHOOK_URL_HERE" \
  -H "Content-Type: application/json" \
  -d '{"id":1,"email":"test@example.com","niche":"1","created_at":"2025-11-21T19:00:00Z","niche_name":"REST API Development"}'
```

You should see:
```json
{"status":"success","message":"Lead added to Google Sheets"}
```

And a new row should appear in your Google Sheet!
