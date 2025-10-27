# 🚀 ZAPIER EXECUTIVE RAPPORT GENERATOR - COMPLETE SETUP GUIDE

**Version:** 2.0
**Date:** 27 Oktober 2025
**Author:** Wouter Arts - Recruitin AI

---

## 📊 WORKFLOW OVERZICHT

```
┌─────────────────────────────────────────────────────────┐
│                   COMPLETE ZAP FLOW                     │
└─────────────────────────────────────────────────────────┘

Step 1: JotForm Trigger (New Submission)
   ↓ (Formulier data + 3 PDF uploads)
Step 2-4: Extract Text from PDFs
   ↓ (Jobdigger, LinkedIn, Vacature PDFs → Text)
Step 5: Python Code - Claude AI Analysis ⭐ MAIN LOGIC
   ↓ (AI genereert complete executive rapport)
Step 6: Gmail - Send HTML Report
   ↓ (Email naar klant)
Step 7: Notion - Database Entry (optional)
   ↓ (Tracking & CRM)
Done! ✅
```

**Total Execution Time:** 60-120 seconden
**Cost per Report:** €0.15-0.25 (Claude API)

---

## 🎯 BELANGRIJKSTE BESTANDEN

| Bestand | Doel |
|---------|------|
| `zapier-executive-rapport-generator.py` | **MAIN** - Complete Python code voor Step 5 |
| `ZAPIER-PDF-MAPPING-FIX.md` | Fix guide voor PDF field mappings |
| `ZAPIER-EXECUTIVE-SETUP-COMPLETE.md` | Deze guide - complete setup |

---

## ⚙️ STAP-VOOR-STAP SETUP

### STEP 1: JotForm Trigger ✅

**App:** JotForm
**Trigger:** New Submission
**Form:** "Arbeidsmarkt Intelligence | Recruitin"

**Velden die Zapier ontvangt:**
```json
{
  "functietitel": "Productiemanager",
  "locatie": "Nijmegen",
  "bedrijfsnaam": "ACME BV",
  "email": "hr@acme.nl",
  "vacature_url": "https://...",
  "jobdigger_pdf": "https://eu.jotform.com/uploads/...",
  "linkedin_pdf": "https://eu.jotform.com/uploads/...",
  "vacature_pdf": "https://eu.jotform.com/uploads/...",
  "vacaturetekst": "Optionele tekst..."
}
```

**Setup:**
1. Kies JotForm app
2. Event: "New Submission"
3. Selecteer form: `252881347421054`
4. Test trigger → Should show recent submission

---

### STEPS 2-4: PDF Text Extraction

**⚠️ KRITIEK: Dit is waar de field mapping bug zat!**

Je hebt 3 opties voor PDF extraction:

#### **Optie A: Zapier Built-in "Extract Text from PDF"**
```
Step 2: Extract Text from PDF
  - Input: {{Step 1: Upload Jobdigger PDF}}
  - Output variable: jobdigger_extracted_text

Step 3: Extract Text from PDF
  - Input: {{Step 1: Upload LinkedIn PDF}}
  - Output variable: linkedin_extracted_text

Step 4: Extract Text from PDF
  - Input: {{Step 1: Upload Vacature PDF}}
  - Output variable: vacature_extracted_text
```

#### **Optie B: Dropbox + PDF Extraction**
Als PDFs via Dropbox gaan:
```
Step 2: Dropbox - Download File → Extract Text
Step 3: Dropbox - Download File → Extract Text
Step 4: Dropbox - Download File → Extract Text
```

#### **Optie C: Custom Python OCR**
Voor gescande PDFs (geen native text):
```python
# In Step 2-4: Python Code met PyPDF2 of pdfplumber
import pdfplumber
# Extract text from uploaded PDF URL
```

**⚠️ BELANGRIJK: Noteer de step IDs!**
```
Step 2 ID: _________ (bijv. 329388908)
Step 3 ID: _________ (bijv. 329388909)
Step 4 ID: _________ (bijv. 329388910)
```

---

### STEP 5: Python Code - Claude AI Analysis ⭐

**Dit is de MAIN stap - De executive rapport generator**

**App:** Code by Zapier
**Runtime:** Python 3.11

**Configuration:**

1. **Klik "Set up action"**
2. **Scroll naar "Input Data"** - Map deze velden:

```python
# ✅ CORRECTE FIELD MAPPING (let op step numbers!)

functietitel: {{1. Functietitel}}
locatie: {{1. Locatie Regio}}
bedrijfsnaam: {{1. Bedrijfsnaam}}
email: {{1. Email Voor Rapportage}}
vacature_url: {{1. Vacature URL}}

# ⚠️ KRITIEK: Gebruik de JUISTE step numbers voor PDF extraction!
jobdigger_pdf_text: {{2. Extract PDF Jobdigger: Extracted Text}}
linkedin_pdf_text: {{3. Extract PDF LinkedIn: Extracted Text}}
vacature_text: {{4. Extract PDF Vacature: Extracted Text}}
```

**❌ FOUT (oude step IDs):**
```python
# Dit werkt NIET als steps zijn veranderd:
jobdigger_pdf_text: {{329388874__extracted_text}}  # Oude ID!
```

**✅ CORRECT (dynamische references):**
```python
# Klik in veld → Select step → Select "Extracted Text" field
jobdigger_pdf_text: {{2. Extract Text from PDF: Extracted Text}}
```

3. **Code:** Kopieer VOLLEDIGE code uit `zapier-executive-rapport-generator.py`

4. **Environment Variables:**
```
CLAUDE_API_KEY = sk-ant-api03-[YOUR_KEY]
```
Get key from: https://console.anthropic.com/settings/keys

5. **Test Step** - Should output:
```json
{
  "to": "hr@acme.nl",
  "subject": "🤖 Executive AI Intelligence: ...",
  "body": "<html>...</html>",
  "notion_company": "ACME BV",
  ...
}
```

---

### STEP 6: Gmail - Send Report

**App:** Gmail
**Action:** Send Email

**Configuration:**
```
To: {{5. To}}
Subject: {{5. Subject}}
Body Type: HTML
Body: {{5. Body}}
From Name: Recruitin

Optional:
- CC: warts@recruitin.nl (for tracking)
```

---

### STEP 7: Notion - Database Entry (Optional)

**App:** Notion
**Action:** Create Database Item
**Database:** "Company Research Intelligence"

**Field Mappings:**
```
Name (Title): {{5. Notion Company}}
Job Title: {{5. Notion Job Title}}
Location: {{5. Notion Location}}
Salary P50: {{5. Notion Salary P50}}
Scarcity Index: {{5. Notion Scarcity Index}}
Time to Hire: {{5. Notion Time To Hire}}
Reliability: {{5. Notion Reliability}}
Vacancy URL: {{5. Notion URL}}
Analysis JSON: {{5. Notion Analysis JSON}}
Status: "Completed"
Created: {{1. Submission Date}}
```

---

## 🔧 ANTHROPIC API SETUP

### 1. Get API Key

1. Ga naar: https://console.anthropic.com/settings/keys
2. Klik "Create Key"
3. Name: "Zapier Labour Market Intelligence"
4. Copy key (starts with `sk-ant-api03-`)

### 2. Add to Zapier

1. In Step 5 (Python Code)
2. Click "Settings" tab
3. Scroll to "Environment Variables"
4. Add:
   - Key: `CLAUDE_API_KEY`
   - Value: [paste your key]
5. Save

### 3. Cost Monitoring

**Per rapport kosten:**
```
Input tokens:  ~5,000  (PDFs + prompt)
Output tokens: ~10,000 (JSON analysis)
Model: Claude Sonnet 4
Cost: ~€0.15-0.25 per rapport
```

**Maandelijkse kosten:**
- 100 rapporten = €20
- 200 rapporten = €40
- 500 rapporten = €100

**Budget Alert Setup:**
1. Anthropic Console → Usage
2. Set budget: €50/maand
3. Alert at 75% (€37.50)

---

## 🧪 TESTING PROTOCOL

### Test 1: Volledig (Alle 3 PDFs)

**Input:**
```json
{
  "functietitel": "Productiemanager",
  "locatie": "Nijmegen",
  "bedrijfsnaam": "Test BV",
  "email": "warts@recruitin.nl",
  "jobdigger_pdf": "✅ Uploaded",
  "linkedin_pdf": "✅ Uploaded",
  "vacature_pdf": "✅ Uploaded"
}
```

**Expected Output:**
- ✅ Email binnen 90 seconden
- ✅ HTML rapport met alle secties
- ✅ Reliability score: 90-98%
- ✅ Notion entry created
- ✅ No errors in Zapier log

**Checklist:**
- [ ] Email ontvangen?
- [ ] HTML correct rendered?
- [ ] Salary data realistisch?
- [ ] Workforce availability getoond?
- [ ] Demographics getoond?
- [ ] Notion entry correct?

---

### Test 2: Minimaal (Geen PDFs)

**Input:**
```json
{
  "functietitel": "Software Engineer",
  "locatie": "Amsterdam",
  "email": "warts@recruitin.nl",
  "jobdigger_pdf": "❌ None",
  "linkedin_pdf": "❌ None",
  "vacature_pdf": "❌ None",
  "vacaturetekst": "We zoeken een software engineer..."
}
```

**Expected Output:**
- ✅ Email binnen 90 seconden
- ✅ Reliability score: 60-74%
- ⚠️ Data based on Claude's market knowledge (intelligent estimates)

---

### Test 3: Foutieve Input

**Input:**
```json
{
  "functietitel": "",
  "locatie": "",
  "email": "invalid-email"
}
```

**Expected Output:**
- ❌ Zapier should catch errors
- ✅ Error email sent to warts@recruitin.nl
- ✅ Notion entry with status "Error"

---

## 🐛 TROUBLESHOOTING

### Error: "Field mapping not found"

**Symptoom:**
```
Error in Step 5: KeyError: 'jobdigger_pdf_text'
```

**Oorzaak:** PDF extraction step ID is veranderd

**Fix:** Zie `ZAPIER-PDF-MAPPING-FIX.md`
1. Open Step 5 → Input Data
2. Klik in `jobdigger_pdf_text` veld
3. Selecteer de JUISTE PDF extraction step
4. Selecteer "Extracted Text" field
5. Herhaal voor `linkedin_pdf_text` en `vacature_text`

---

### Error: "Claude API key not found"

**Symptoom:**
```
Error: CLAUDE_API_KEY environment variable not set
```

**Fix:**
1. Step 5 → Settings tab
2. Environment Variables → Add
3. Key: `CLAUDE_API_KEY`
4. Value: `sk-ant-api03-...`
5. Save & Test

---

### Error: "JSON parse error"

**Symptoom:**
```
JSONDecodeError: Expecting value: line 1 column 1
```

**Oorzaak:** Claude returned non-JSON (bijv. markdown)

**Fix:** Code heeft al cleanup logic:
```python
# This is already in the code:
if response_text.startswith('```json'):
    response_text = response_text[7:]
```

If still failing:
1. Check Claude prompt for syntax errors
2. Test prompt in Anthropic Console first
3. Ensure `temperature=0.3` (not too high)

---

### Error: "Timeout in Step 5"

**Symptoom:**
```
Error: Code execution timed out after 30 seconds
```

**Oorzaak:** Claude API call te langzaam

**Fix:**
1. Reduce PDF input size (max 15k chars per PDF)
2. Lower `max_tokens` from 16000 to 12000
3. Check Anthropic API status: https://status.anthropic.com/

---

### Error: "Email not sent"

**Symptoom:**
```
Gmail step failed: Invalid recipient
```

**Fix:**
1. Check `{{5. To}}` contains valid email
2. Test with your own email first
3. Verify Gmail account connected in Zapier
4. Check HTML body size (<1MB)

---

## 📊 VERSCHILLEN MET EERDERE VERSIES

| Feature | `zapier-ai-rapport-IMPROVED.py` | `zapier-executive-rapport-generator.py` (NIEUW) |
|---------|--------------------------------|--------------------------------------------------|
| **API Method** | `requests` library | Official `anthropic` SDK ✅ |
| **Data Approach** | Fallback demo data | Intelligent estimates ✅ |
| **Missing Data** | Shows "N/A" | Claude fills with realistic market data ✅ |
| **Workforce Analysis** | Basic | Advanced segmentation (actief/latent/niet) ✅ |
| **Demographics** | Limited | Full age + education breakdown ✅ |
| **HTML Design** | Good | Executive-level professional ✅ |
| **Notion Integration** | No | Full database output ✅ |
| **Error Handling** | Basic | Comprehensive ✅ |

**Aanbeveling:** Gebruik `zapier-executive-rapport-generator.py` (de nieuwe versie)

---

## 🎯 QUALITY CHECKLIST

Before going live:

**Technical:**
- [ ] All 7 Zapier steps configured
- [ ] PDF extraction steps tested
- [ ] Field mappings correct (no old step IDs!)
- [ ] Claude API key set
- [ ] Environment variables configured
- [ ] Error handling tested

**Testing:**
- [ ] Test 1 (volledig) passed
- [ ] Test 2 (minimaal) passed
- [ ] Test 3 (foutief) handled gracefully
- [ ] Email HTML renders correctly
- [ ] Notion entries created

**Monitoring:**
- [ ] Budget alert set (€50/maand)
- [ ] Zapier email notifications on
- [ ] Cost tracking dashboard setup

**Legal:**
- [ ] GDPR compliance verified
- [ ] Privacy policy updated
- [ ] Data retention policy set (90 dagen)
- [ ] User informed about Claude AI processing

---

## 📈 SUCCESS METRICS

**Target KPIs:**
```
✅ Report generation time: <90 seconden
✅ Success rate: >95%
✅ Reliability score avg: >80%
✅ Email delivery: 100%
✅ Cost per report: <€0.25
✅ User satisfaction: >4.5/5
```

**Monitoring Dashboard:**
- Zapier: Task history → Filter last 30 days
- Anthropic Console: Usage → Monthly costs
- Gmail: Sent emails → Delivery rate
- Notion: Database → Count entries

---

## 🔗 BELANGRIJKE LINKS

- **Anthropic Console:** https://console.anthropic.com/
- **Anthropic API Docs:** https://docs.anthropic.com/
- **Zapier Support:** https://zapier.com/app/support
- **JotForm Admin:** https://eu.jotform.com/myforms
- **Notion Workspace:** [Your workspace URL]

---

## 📞 SUPPORT

**Setup vragen:**
- Email: warts@recruitin.nl

**Zapier issues:**
- Zapier Support Portal

**Anthropic API issues:**
- support@anthropic.com
- Status: https://status.anthropic.com/

---

## 🚀 DEPLOYMENT CHECKLIST

Voordat je live gaat:

**Week 1: Setup**
- [ ] Anthropic account + API key
- [ ] Zapier account (Professional plan for Code steps)
- [ ] JotForm form created
- [ ] Notion database setup (optional)
- [ ] Gmail connected to Zapier

**Week 2: Configuration**
- [ ] All 7 Zapier steps configured
- [ ] PDF extraction working
- [ ] Field mappings correct
- [ ] Claude API tested
- [ ] HTML email template verified

**Week 3: Testing**
- [ ] 10+ test submissions
- [ ] All scenarios tested (volledig/minimaal/foutief)
- [ ] Error handling verified
- [ ] Cost monitoring confirmed
- [ ] Performance benchmarks met

**Week 4: Launch**
- [ ] Soft launch (internal team only)
- [ ] Monitor first 20 reports
- [ ] Fix any issues
- [ ] Public launch
- [ ] Marketing announcement

---

## 📦 FILES OVERVIEW

```
labour-market-intelligence-landing/
├── zapier-executive-rapport-generator.py  ⭐ MAIN CODE
├── ZAPIER-EXECUTIVE-SETUP-COMPLETE.md     📖 This guide
├── ZAPIER-PDF-MAPPING-FIX.md              🔧 PDF fix guide
├── CLAUDE-AI-ANALYSE-UITLEG.md            📚 How Claude works
├── index.html                             🌐 Landing page
├── script.js                              ⚡ Landing page JS
└── styles.css                             🎨 Landing page CSS
```

---

**Version:** 2.0
**Last Updated:** 27 Oktober 2025
**Status:** Production Ready ✅

**Let's go! 🚀**
