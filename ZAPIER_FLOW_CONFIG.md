# 🔄 Perfecte Zapier Flow Configuratie voor Pipedrive

## 📋 Complete Zap Setup - Copy/Paste Ready

### ZAP NAAM
```
Pipedrive JobDigger Deals → Google Sheets (Daily Sync)
```

---

## ⚙️ STAP 1: TRIGGER - Schedule

**App:** Schedule by Zapier
**Event:** Every Day
**Configuratie:**
```yaml
Trigger Type: Every Day
Time of Day: 09:00 AM
Timezone: Europe/Amsterdam
```

---

## ⚙️ STAP 2: ACTION - Pipedrive (Find Deals)

**App:** Pipedrive
**Event:** Find Many Deals
**Account:** recruitinbv.pipedrive.com

### Search Configuration:
```yaml
Status: all
Limit: 500
Sort: update_time DESC
```

### Filter (Optional - voor alleen JobDigger deals):
```yaml
# Als je een custom field hebt voor JobDigger:
Custom Field: [JobDigger] = Yes

# Of filter op pipeline:
Pipeline: [Your Pipeline Name]

# Of laat leeg voor alle deals
```

### Fields to Return:
```yaml
- id
- title
- value
- currency
- status
- stage_id
- person_id
- person_name
- org_id
- org_name
- add_time
- update_time
- won_time
- lost_time
- expected_close_date
- owner_id
- owner_name
```

---

## ⚙️ STAP 3: ACTION - Google Sheets (Create/Update Row)

**App:** Google Sheets
**Event:** Create Spreadsheet Row(s)
**Spreadsheet:** Pipedrive JobDigger Deals
**Worksheet:** Sheet1

### Column Mapping (Exact veld namen):

```yaml
Column A - Deal ID:
  Value: {{Pipedrive: ID}}
  Format: Number

Column B - Title:
  Value: {{Pipedrive: Title}}
  Format: Text

Column C - Status:
  Value: {{Pipedrive: Status}}
  Format: Text

Column D - Value:
  Value: {{Pipedrive: Value}}
  Format: Number

Column E - Currency:
  Value: {{Pipedrive: Currency}}
  Format: Text
  Default: EUR

Column F - Stage:
  Value: {{Pipedrive: Stage ID}}
  Format: Text

Column G - Person:
  Value: {{Pipedrive: Person Name}}
  Format: Text

Column H - Organization:
  Value: {{Pipedrive: Organization Name}}
  Format: Text

Column I - Owner:
  Value: {{Pipedrive: Owner Name}}
  Format: Text

Column J - Created Date:
  Value: {{Pipedrive: Add Time}}
  Format: Date/Time

Column K - Updated Date:
  Value: {{Pipedrive: Update Time}}
  Format: Date/Time

Column L - Expected Close:
  Value: {{Pipedrive: Expected Close Date}}
  Format: Date

Column M - Won Time:
  Value: {{Pipedrive: Won Time}}
  Format: Date/Time

Column N - Lost Time:
  Value: {{Pipedrive: Lost Time}}
  Format: Date/Time
```

---

## 📊 GOOGLE SHEETS SETUP

### Sheet Headers (Rij 1):
Kopieer deze headers exact naar rij 1 van je Google Sheet:

```
Deal ID | Title | Status | Value | Currency | Stage | Person | Organization | Owner | Created Date | Updated Date | Expected Close | Won Time | Lost Time
```

### Formatting Tips:
- **Column D (Value):** Format als Currency → €
- **Columns J, K, L, M, N:** Format als Date/Time
- **Freeze row 1:** View → Freeze → 1 row

---

## 🎯 ALTERNATIEVE CONFIGURATIE - Met Looping (Voor Multiple Deals)

Als "Find Many Deals" meerdere resultaten geeft, voeg deze stap toe tussen Step 2 en 3:

### EXTRA STAP: Looping by Zapier

**App:** Looping by Zapier
**Event:** Create Loop From Line Items

**Configuration:**
```yaml
Loop Source: {{Pipedrive: All Deals}}
Loop Iterations: Up to 500
```

Dan wordt elke deal individueel naar Google Sheets gestuurd.

---

## 📝 ZAPIER PSEUDO-CODE (Voor AI Assistant)

Als Zapier een AI setup tool heeft, gebruik deze prompt:

```
Create a Zap that:

1. TRIGGER: Runs daily at 9:00 AM (Europe/Amsterdam timezone)

2. ACTION: Finds all deals from Pipedrive account "recruitinbv.pipedrive.com"
   - Use "Find Many Deals" action
   - Return up to 500 deals
   - Sort by update_time descending
   - Include fields: id, title, value, currency, status, stage_id,
     person_name, org_name, add_time, update_time, owner_name

3. ACTION: For each deal found, create a row in Google Sheets
   - Spreadsheet: "Pipedrive JobDigger Deals"
   - Worksheet: "Sheet1"
   - Map the following fields:
     * Column A: Deal ID
     * Column B: Title
     * Column C: Status
     * Column D: Value (as number)
     * Column E: Currency
     * Column F: Stage ID
     * Column G: Person Name
     * Column H: Organization Name
     * Column I: Owner Name
     * Column J: Created Date (add_time)
     * Column K: Updated Date (update_time)
     * Column L: Expected Close Date
     * Column M: Won Time
     * Column N: Lost Time

4. SETTINGS:
   - Zap Name: "Pipedrive JobDigger Deals → Google Sheets (Daily Sync)"
   - Status: Active
   - Run daily automatically
```

---

## 🔧 ZAPIER WEBHOOK ALTERNATIVE (Advanced)

Als je real-time updates wilt in plaats van dagelijks:

### Setup met Webhooks:

**TRIGGER:** Webhooks by Zapier
**Event:** Catch Hook

**In Pipedrive:**
1. Settings → Webhooks
2. Create new webhook
3. URL: [Zapier webhook URL]
4. Events: deal.updated, deal.added
5. Save

**Then same Google Sheets action as above**

---

## 🧪 TEST CONFIGURATIE

### Test Checklist:

```
☐ Step 1: Test trigger → Should show current date/time
☐ Step 2: Test Pipedrive → Should return at least 1 deal
☐ Step 3: Test Google Sheets → Should create 1 row in sheet
☐ Full test → Run entire Zap
☐ Check Google Sheet → Verify data is correct
☐ Turn Zap ON
☐ Wait 24 hours → Check if it ran automatically
```

---

## 📦 FIELD MAPPING REFERENCE

Voor copy/paste in Zapier (gebruik deze exact):

| Google Sheet Column | Pipedrive Field | Zapier Variable |
|---------------------|-----------------|-----------------|
| Deal ID | ID | `{{step_2__id}}` |
| Title | Title | `{{step_2__title}}` |
| Status | Status | `{{step_2__status}}` |
| Value | Value | `{{step_2__value}}` |
| Currency | Currency | `{{step_2__currency}}` |
| Stage | Stage ID | `{{step_2__stage_id}}` |
| Person | Person Name | `{{step_2__person_name}}` |
| Organization | Organization Name | `{{step_2__org_name}}` |
| Owner | Owner Name | `{{step_2__owner_name}}` |
| Created Date | Add Time | `{{step_2__add_time}}` |
| Updated Date | Update Time | `{{step_2__update_time}}` |
| Expected Close | Expected Close Date | `{{step_2__expected_close_date}}` |
| Won Time | Won Time | `{{step_2__won_time}}` |
| Lost Time | Lost Time | `{{step_2__lost_time}}` |

*(step_2 = Pipedrive action step number, adjust if different)*

---

## 🎨 BONUS: FORMATTED GOOGLE SHEETS

Om je Google Sheet er professioneel uit te laten zien:

### Apply Formatting:

```javascript
// Google Sheets Script (Tools → Script Editor)
function formatPipedriveSheet() {
  var sheet = SpreadsheetApp.getActiveSheet();

  // Header row formatting
  sheet.getRange("1:1").setFontWeight("bold");
  sheet.getRange("1:1").setBackground("#4285f4");
  sheet.getRange("1:1").setFontColor("#ffffff");

  // Currency formatting
  sheet.getRange("D:D").setNumberFormat("€#,##0.00");

  // Date formatting
  sheet.getRange("J:N").setNumberFormat("dd-mm-yyyy hh:mm");

  // Freeze header row
  sheet.setFrozenRows(1);

  // Auto-resize columns
  sheet.autoResizeColumns(1, 14);

  // Status conditional formatting
  var statusRange = sheet.getRange("C:C");
  var openRule = SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("open")
    .setBackground("#fff3cd")
    .setRanges([statusRange])
    .build();
  var wonRule = SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("won")
    .setBackground("#d4edda")
    .setRanges([statusRange])
    .build();
  var lostRule = SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("lost")
    .setBackground("#f8d7da")
    .setRanges([statusRange])
    .build();

  var rules = sheet.getConditionalFormatRules();
  rules.push(openRule, wonRule, lostRule);
  sheet.setConditionalFormatRules(rules);
}
```

Run deze functie 1x om je sheet te formatteren!

---

## ✅ FINAL CHECKLIST

Voordat je de Zap activeert:

```
☐ Pipedrive account connected in Zapier (recruitinbv)
☐ Google Sheets account connected in Zapier
☐ Google Sheet "Pipedrive JobDigger Deals" created
☐ Headers in row 1 added
☐ All field mappings configured
☐ Test successful - saw data in Google Sheets
☐ Zap named correctly
☐ Zap turned ON
☐ Set reminder to check tomorrow
```

---

**© 2025 WouterArts Recruitin - Labour Market Intelligence**
