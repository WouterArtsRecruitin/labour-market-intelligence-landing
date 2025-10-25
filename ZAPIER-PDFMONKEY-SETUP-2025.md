# 🚀 Zapier Workflow met PDFMonkey - Complete Setup Guide

## 📋 Overzicht

Deze workflow genereert AI-gedreven recruitment rapporten als **professionele PDF** via PDFMonkey.

---

## 🎯 Workflow Structuur (9 stappen)

### **Stap 1: JotForm Trigger**
- App: **JotForm**
- Trigger: **New Submission**
- Form ID: `252881347421054`

**Velden die je nodig hebt:**
- Bedrijfsnaam
- Contactpersoon
- Email
- Telefoon
- Functietitel
- Sector
- Locatie
- Urgentie
- Aantal posities
- Upload Jobdigger PDF (optioneel)
- Upload LinkedIn TI PDF (optioneel)
- Upload Vacature PDF (optioneel)
- Extra info (textarea)

---

### **Stap 2-7: PDF Text Extraction (Conditional)**

**Optie A - Zapier's Extract Text (Vereist Zapier Professional+):**
```
Step 2: Filter - Check if Jobdigger PDF exists
Step 3: Extract Text from PDF - Jobdigger
Step 4: Filter - Check if LinkedIn PDF exists
Step 5: Extract Text from PDF - LinkedIn
Step 6: Filter - Check if Vacature PDF exists
Step 7: Extract Text from PDF - Vacature
```

**Optie B - Gebruik PDFMonkey's Text Extraction (Geen extra Zapier kosten):**

PDFMonkey heeft **geen** text extraction. Als je PDFs wilt lezen, gebruik dan:
- **Parseur.com** (gratis tier beschikbaar)
- **DocParser** (betaald)
- **OCR.space API** (gratis tier)

**Aanbeveling:** Sla Step 2-7 OVER als je geen PDF text extraction nodig hebt. De AI kan ook zonder PDF content werken met fallback data.

---

### **Stap 8: Python AI Analysis**

**App:** Code by Zapier
**Runtime:** Python 3.11

**Input Data:**
```
claude_api_key: [JE CLAUDE API KEY]
pdfmonkey_api_key: [JE PDFMONKEY API KEY]
pdfmonkey_template_id: [JE PDFMONKEY TEMPLATE ID]

bedrijfsnaam: {{1. bedrijfsnaam}}
contactpersoon: {{1. contactpersoon}}
email: {{1. email}}
telefoon: {{1. telefoon}}
functietitel: {{1. functietitel}}
sector: {{1. sector}}
locatie: {{1. locatie}}
urgentie: {{1. urgentie}}
aantal_posities: {{1. aantal_posities}}

vacature_text: {{3. Output}} (if extraction ran)
jobdigger_text: {{5. Output}} (if extraction ran)
linkedin_ti_text: {{7. Output}} (if extraction ran)

vacature_url: {{1. vacature_pdf_url}}
jobdigger_url: {{1. jobdigger_pdf_url}}
linkedin_ti_url: {{1. linkedin_ti_pdf_url}}

extra_info: {{1. extra_info}}
submission_url: {{1. Submission URL}}
submission_id: {{1. Submission ID}}
```

**Code:**
Kopieer volledige inhoud van `zapier-ai-rapport-pdfmonkey-2025.py`

---

### **Stap 9: PDFMonkey - Generate PDF**

**App:** PDFMonkey
**Action:** Generate Document

**Setup:**
1. Ga naar https://app.pdfmonkey.io/
2. Maak een account aan
3. Maak een nieuwe Template:
   - Template Name: "Recruitment Intelligence Report"
   - Template Type: "JSON Payload"

**Template Fields (JSON):**
```json
{
  "datum": "{{8. current_date}}",
  "bedrijfsnaam": "{{8. notion_bedrijfsnaam}}",
  "functietitel": "{{8. notion_functietitel}}",
  "contactpersoon": "{{8. notion_contactpersoon}}",
  "email": "{{8. notion_email}}",
  "telefoon": "{{8. notion_telefoon}}",
  "sector": "{{8. notion_sector}}",
  "locatie": "{{8. notion_locatie}}",
  "urgentie": "{{8. notion_urgentie}}",
  "schaarste_niveau": "{{8. notion_ai_schaarste}}",
  "time_to_hire": "{{8. notion_ai_time_to_hire}}",
  "salaris_range": "{{8. notion_salaris_range}}"
}
```

**Of gebruik de volledige payload:**
```
Payload: {{8. pdfmonkey_payload}}
```

**Output:**
- PDF Download URL: `{{9. download_url}}`

---

### **Stap 10: Gmail - Send Email with PDF**

**App:** Gmail
**Action:** Send Email

**Setup:**
```
To: {{8. email_to}}
CC: {{8. email_cc}}
Subject: {{8. email_subject}}
Body Type: HTML
Body: {{8. email_body_html}}
Attachments: {{9. download_url}}  ← PDFMonkey PDF URL
```

---

## 🔑 API Keys Nodig

### **1. Claude API Key**
1. Ga naar: https://console.anthropic.com/settings/keys
2. Klik "Create Key"
3. Kopieer key (begint met `sk-ant-api03-...`)
4. Voeg toe aan Python step (Input Data: `claude_api_key`)

**Kosten:** ~$0.01-0.03 per rapport (zeer goedkoop)

---

### **2. PDFMonkey API Key**
1. Ga naar: https://app.pdfmonkey.io/
2. Account aanmaken (gratis tier: 300 documenten/maand)
3. Ga naar Settings → API Keys
4. Kopieer Private API Key
5. Voeg toe aan Python step (Input Data: `pdfmonkey_api_key`)

**Pricing:**
- **Free:** 300 PDFs/maand
- **Starter ($19/mo):** 3,000 PDFs/maand
- **Pro ($99/mo):** 30,000 PDFs/maand

---

### **3. PDFMonkey Template ID**
1. Maak template aan in PDFMonkey dashboard
2. Kopieer Template ID (rechts bovenin bij template details)
3. Voeg toe aan Python step (Input Data: `pdfmonkey_template_id`)

---

## 🎨 PDFMonkey Template Maken

### **Stap-voor-stap:**

1. **Login** bij PDFMonkey: https://app.pdfmonkey.io/

2. **Maak Template:**
   - Klik "New Template"
   - Name: "Recruitment Intelligence Report"
   - Template Type: "HTML to PDF"

3. **Upload HTML Template:**

   Gebruik deze basis template (of maak je eigen):

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 40px;
            color: #1f2937;
        }
        .header {
            background: linear-gradient(135deg, #4B4F51 0%, #77797B 100%);
            color: white;
            padding: 40px;
            text-align: center;
            border-radius: 12px;
            margin-bottom: 30px;
        }
        .section {
            margin-bottom: 30px;
            page-break-inside: avoid;
        }
        .stat-box {
            background: #f3f4f6;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #EF7D00;
            margin: 10px 0;
        }
        .highlight {
            color: #EF7D00;
            font-weight: bold;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #e5e7eb;
        }
        th {
            background: #f9fafb;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <!-- Header -->
    <div class="header">
        <h1>🤖 AI Recruitment Intelligence</h1>
        <p>Arbeidsmarkt Analyse • {{datum}}</p>
    </div>

    <!-- Executive Summary -->
    <div class="section">
        <h2>📊 Executive Summary</h2>
        <div class="stat-box">
            <p><strong>Bedrijf:</strong> {{bedrijfsnaam}}</p>
            <p><strong>Vacature:</strong> {{functietitel}}</p>
            <p><strong>Sector:</strong> {{sector}}</p>
            <p><strong>Locatie:</strong> {{locatie}}</p>
            <p><strong>Urgentie:</strong> <span class="highlight">{{urgentie}}</span></p>
        </div>
    </div>

    <!-- Contact -->
    <div class="section">
        <h2>👤 Contactpersoon</h2>
        <table>
            <tr>
                <td><strong>Naam:</strong></td>
                <td>{{contactpersoon}}</td>
            </tr>
            <tr>
                <td><strong>Email:</strong></td>
                <td>{{email}}</td>
            </tr>
            <tr>
                <td><strong>Telefoon:</strong></td>
                <td>{{telefoon}}</td>
            </tr>
        </table>
    </div>

    <!-- AI Insights -->
    <div class="section">
        <h2>📈 AI Arbeidsmarkt Analyse</h2>
        <div class="stat-box">
            <p><strong>Schaarste Niveau:</strong> <span class="highlight">{{schaarste_niveau}}</span></p>
            <p><strong>Time-to-Hire:</strong> {{time_to_hire}}</p>
            <p><strong>Salaris Range:</strong> {{salaris_range}}</p>
        </div>
    </div>

    <!-- Footer -->
    <div style="text-align: center; margin-top: 50px; padding-top: 20px; border-top: 2px solid #e5e7eb; color: #6b7280; font-size: 12px;">
        <p><strong>Recruitin</strong> | AI-Powered Recruitment Intelligence</p>
        <p>warts@recruitin.nl | recruitin.com</p>
        <p>Powered by Claude AI • Generated: {{datum}}</p>
    </div>

</body>
</html>
```

4. **Test Template:**
   - Klik "Test Document"
   - Vul test data in
   - Check PDF output

5. **Kopieer Template ID** (staat rechtsboven)

---

## 🧪 Testing Checklist

### **Pre-Launch:**
- [ ] Claude API key werkt (test in console.anthropic.com)
- [ ] PDFMonkey account aangemaakt
- [ ] PDFMonkey template gemaakt en getest
- [ ] Template ID gekopieerd
- [ ] Alle velden correct gemapt in Zapier

### **Test Scenario 1 - Minimaal (zonder PDFs):**
- Functietitel: "Test Developer"
- Bedrijfsnaam: "Test BV"
- Email: jouw@test.com
- Verwacht: Email + PDF met fallback AI data

### **Test Scenario 2 - Met PDFs:**
- Upload 1-3 test PDFs
- Verwacht: Email + PDF met AI analyse van PDFs

### **Controleer:**
- [ ] Email ontvangen
- [ ] PDF attachment aanwezig
- [ ] PDF bevat alle data
- [ ] AI analyse ziet er logisch uit
- [ ] Salaris ranges kloppen
- [ ] Contact info correct

---

## 🐛 Troubleshooting

### **Problem: "PDFMonkey PDF not generated"**
- **Oorzaak:** Template ID verkeerd of API key invalid
- **Oplossing:** Check Template ID in PDFMonkey dashboard

### **Problem: "PDF is empty/broken"**
- **Oorzaak:** JSON payload format verkeerd
- **Oplossing:** Test template met sample data in PDFMonkey

### **Problem: "PDF takes too long"**
- **Oorzaak:** PDFMonkey free tier heeft rate limits
- **Oplossing:** Upgrade naar Starter plan of wacht 30 sec tussen tests

### **Problem: "Email has no attachment"**
- **Oorzaak:** PDF URL niet correct doorgegeven
- **Oplossing:** Check {{9. download_url}} field in Gmail step

---

## 💡 Pro Tips

1. **PDF Template Design:**
   - Gebruik maximaal 2-3 fonts voor consistentie
   - Houd page breaks in gedachten (use `page-break-inside: avoid`)
   - Test altijd met realistische data lengtes

2. **Cost Optimization:**
   - Free tier PDFMonkey = 300/maand = gratis voor small volume
   - Claude AI kost ~$0.02 per rapport
   - Totaal: ~€0.02 per rapport (super goedkoop!)

3. **Quality:**
   - PDFMonkey genereert professionele PDFs
   - Veel mooier dan HTML email screenshots
   - Klanten kunnen PDF opslaan/printen/delen

4. **Branding:**
   - Voeg Recruitin logo toe aan PDF template
   - Gebruik merkk kleuren (#EF7D00, #4B4F51)
   - Voeg footer toe met contact info

---

## 🚀 Go-Live Checklist

- [ ] Workflow volledig geconfigureerd (10 stappen)
- [ ] Claude API key toegevoegd en getest
- [ ] PDFMonkey account actief
- [ ] PDFMonkey template gemaakt
- [ ] Template ID toegevoegd aan Python code
- [ ] Test submission succesvol
- [ ] PDF ziet er professioneel uit
- [ ] Email + PDF ontvangen
- [ ] Alle data correct in PDF
- [ ] Zap turned ON

---

## 📊 Workflow Overzicht

```
┌─────────────────────┐
│  JotForm Submission │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Python AI Analysis  │  ← Claude API
│ (Stap 8)            │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ PDFMonkey Generate  │  ← Creates PDF
│ (Stap 9)            │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Gmail Send Email    │  ← Email + PDF
│ (Stap 10)           │
└─────────────────────┘
```

---

## 🎯 Alternatief: Simplified Flow (ZONDER PDF Extraction)

Als je GEEN text extraction uit PDFs nodig hebt:

```
Step 1: JotForm Trigger
Step 2: Python AI Analysis (zonder PDF text)
Step 3: PDFMonkey Generate PDF
Step 4: Gmail Send (Email + PDF attachment)
```

Dit is **goedkoper** (geen Zapier Professional nodig) en **sneller**!

---

**Klaar om te starten? Volg de stappen en test! 🚀**

Vragen? Check:
- PDFMonkey docs: https://docs.pdfmonkey.io/
- Claude API docs: https://docs.anthropic.com/
- Zapier help: https://help.zapier.com/
