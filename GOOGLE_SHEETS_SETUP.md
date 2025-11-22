# Google Sheets Auto-Export Setup

## 📋 Інструкція по налаштуванню автоматичного експорту лідів

### Крок 1: Створити Google Sheet

1. Відкрийте [Google Sheets](https://sheets.google.com)
2. Натисніть **"+ Blank"** (створити нову таблицю)
3. Назвіть таблицю: **"Lead Gen Database"**
4. У перший рядок додайте заголовки:
   - A1: `ID`
   - B1: `Email`
   - C1: `Niche`
   - D1: `Date`
   - E1: `Niche Name`

### Крок 2: Додати Apps Script

1. У Google Sheets натисніть **Extensions → Apps Script**
2. Видаліть весь код, що там є
3. Вставте цей код:

```javascript
function doPost(e) {
  try {
    // Отримуємо дані з POST запиту
    var data = JSON.parse(e.postData.contents);
    
    // Відкриваємо активну таблицю
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    
    // Додаємо новий рядок з даними
    sheet.appendRow([
      data.id,
      data.email,
      data.niche,
      data.created_at,
      data.niche_name || ''
    ]);
    
    // Повертаємо успішну відповідь
    return ContentService.createTextOutput(JSON.stringify({
      'status': 'success',
      'message': 'Lead added to Google Sheets'
    })).setMimeType(ContentService.MimeType.JSON);
    
  } catch(error) {
    // Повертаємо помилку
    return ContentService.createTextOutput(JSON.stringify({
      'status': 'error',
      'message': error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

// Тестова функція (опціонально)
function testDoPost() {
  var testData = {
    postData: {
      contents: JSON.stringify({
        id: 1,
        email: "test@example.com",
        niche: "1",
        created_at: new Date().toISOString(),
        niche_name: "REST API Development"
      })
    }
  };
  
  var result = doPost(testData);
  Logger.log(result.getContent());
}
```

4. Натисніть **Save** (💾 іконка)
5. Назвіть проєкт: **"Lead Gen Webhook"**

### Крок 3: Деплой як Web App

1. Натисніть **Deploy → New deployment**
2. Натисніть на іконку ⚙️ (шестерня) → виберіть **"Web app"**
3. Налаштування:
   - **Description:** "Lead Gen Webhook v1"
   - **Execute as:** Me (ваш email)
   - **Who has access:** Anyone
4. Натисніть **Deploy**
5. **ВАЖЛИВО:** Скопіюйте **Web app URL** (виглядає як `https://script.google.com/macros/s/AKfycby.../exec`)
6. Збережіть цей URL - він вам знадобиться!

### Крок 4: Дозволити доступ

1. При першому деплої Google попросить дозвіл
2. Натисніть **Review permissions**
3. Виберіть ваш Google акаунт
4. Натисніть **Advanced → Go to "Lead Gen Webhook" (unsafe)**
5. Натисніть **Allow**

### Крок 5: Скопіювати Webhook URL

Після деплою ви отримаєте URL типу:
```
https://script.google.com/macros/s/AKfycby...RANDOM_ID.../exec
```

**Збережіть цей URL!** Він вам знадобиться для наступного кроку.

---

## ✅ Готово!

Тепер скажіть мені ваш Webhook URL, і я оновлю Rust API, щоб він автоматично відправляв кожен новий лід в Google Sheets!

## 🧪 Тестування

Після того як я оновлю код, кожен новий лід буде автоматично з'являтися в Google Sheets в реальному часі!
