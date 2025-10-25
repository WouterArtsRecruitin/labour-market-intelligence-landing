# 🚀 ZAPIER FLOW A - Met PDFMonkey (Premium Rapport)

## 📋 Overzicht

Deze flow genereert **professionele PDF rapporten** via PDFMonkey + HTML email.

**Voordelen:**
- ✅ Professionele PDF output
- ✅ Klant kan PDF downloaden/printen/delen
- ✅ Mooiere presentatie
- ✅ Geschikt voor formele rapportage

**Kosten:**
- PDFMonkey Free: 300 PDFs/maand (€0)
- Claude AI: ~€0.02 per rapport
- **Totaal: ~€0.02 per rapport**

---

## 🔧 Complete Workflow (5 stappen)

### **STAP 1: JotForm Trigger**

**App:** JotForm
**Trigger:** New Submission
**Form ID:** `252881347421054`

**Test:** Submit test form

---

### **STAP 2: Python AI Analysis**

**App:** Code by Zapier
**Runtime:** Python 3.11

**Input Data Mapping:**
```
claude_api_key: [JE_CLAUDE_API_KEY]

bedrijfsnaam: {{1. bedrijfsnaam}}
contactpersoon: {{1. contactpersoon}}
email: {{1. email}}
telefoon: {{1. telefoon}}
functietitel: {{1. functietitel}}
sector: {{1. sector}}
locatie: {{1. locatie}}
urgentie: {{1. urgentie}}
aantal_posities: {{1. aantal_posities}}
ervaringsniveau: {{1. ervaringsniveau}}
salaris_min: {{1. salaris_min}}
salaris_max: {{1. salaris_max}}
werkervaring_jaren: {{1. werkervaring_jaren}}
opleidingsniveau: {{1. opleidingsniveau}}
teamsize: {{1. teamsize}}
bedrijfsgrootte: {{1. bedrijfsgrootte}}
werkomgeving: {{1. werkomgeving}}
groei_fase: {{1. groei_fase}}
key_skills: {{1. key_skills}}
extra_info: {{1. extra_info}}

vacature_url: {{1. vacature_url}}
jobdigger_url: {{1. jobdigger_url}}
linkedin_ti_url: {{1. linkedin_ti_url}}

submission_url: {{1. Submission URL}}
submission_id: {{1. Submission ID}}
```

**Code:**
```python
# Kopieer volledige inhoud van: zapier-ai-rapport-pdfmonkey-2025.py
```

**Output Fields:**
- `email_to`
- `email_subject`
- `email_body_html`
- `pdfmonkey_payload` (JSON string)
- `notion_*` (voor Notion integratie)

---

### **STAP 3: PDFMonkey - Generate Document**

**App:** PDFMonkey
**Action:** Generate Document

**Setup:**
1. Connect PDFMonkey account
2. **Template:** Selecteer je template (zie template setup hieronder)
3. **Payload:**
   - **Meta:** Gebruik "Use a Custom Value"
   - **Value:** `{{2. pdfmonkey_payload}}`

**Alternative - Manual Mapping:**
Als je custom payload niet werkt, map handmatig:
```
datum: {{2. current_date}}
bedrijfsnaam: {{2. notion_bedrijfsnaam}}
contactpersoon: {{2. notion_contactpersoon}}
email: {{2. notion_email}}
telefoon: {{2. notion_telefoon}}
functietitel: {{2. notion_functietitel}}
sector: {{2. notion_sector}}
locatie: {{2. notion_locatie}}
urgentie: {{2. notion_urgentie}}
schaarste_niveau: {{2. notion_ai_schaarste}}
time_to_hire: {{2. notion_ai_time_to_hire}}
salaris_p50: {{2. notion_salaris_range}}
```

**Output:**
- `download_url` - PDF download link

---

### **STAP 4: Delay (Optional maar aanbevolen)**

**App:** Delay by Zapier
**Action:** Delay For
**Time:** 5 seconds

**Waarom?** PDFMonkey heeft soms 2-3 seconden nodig om PDF te genereren.

---

### **STAP 5: Gmail - Send Email with PDF**

**App:** Gmail
**Action:** Send Email

**Configuration:**
```
To: {{2. email_to}}
CC: {{2. notion_email}}
Subject: {{2. email_subject}}
Body Type: HTML
Body: {{2. email_body_html}}
Attachments: {{3. download_url}}
```

**Advanced Options:**
- Reply To: warts@recruitin.nl
- From Name: Recruitin AI Intelligence

---

## 🎨 PDFMonkey Template Setup

### **Stap 1: Maak Template in PDFMonkey**

1. Login: https://app.pdfmonkey.io/
2. Click **"New Template"**
3. Name: `Recruitment Intelligence Report`
4. Click **"Create Template"**

### **Stap 2: Upload HTML Template**

1. In de template editor, klik **"Edit HTML"**
2. Kopieer de volledige inhoud van: `pdfmonkey-template-recruitment-intelligence.html`
3. Plak in de HTML editor
4. Click **"Save"**

### **Stap 3: Test Template**

1. Click **"Test Document"**
2. Vul test data in (of gebruik JSON hieronder)
3. Click **"Generate PDF"**
4. Check output

**Test JSON:**
```json
{
  "datum": "25 Oktober 2025",
  "bedrijfsnaam": "Tech Innovators BV",
  "contactpersoon": "Jan de Vries",
  "email": "jan@techinnovators.nl",
  "telefoon": "+31 6 1234 5678",
  "functietitel": "Senior Python Developer",
  "sector": "Tech/IT",
  "locatie": "Amsterdam",
  "urgentie": "Hoog",
  "aantal_posities": "2",
  "schaarste_niveau": "Hoog",
  "schaarste_ratio": "3.2 vacatures per kandidaat",
  "time_to_hire": "45-65 dagen",
  "beschikbaarheid": "±1.200",
  "beschikbaarheid_tekst": "Geschikte kandidaten NL",
  "salaris_p25": "€50.000 - €60.000",
  "salaris_p50": "€65.000 - €75.000",
  "salaris_p75": "€75.000 - €90.000",
  "actief_zoekend": 15,
  "latent_zoekend": 45,
  "niet_zoekend": 40,
  "total_workers_market": "25.000",
  "growth_percentage": 3.5,
  "open_vacancies": "1.200",
  "employment_trend": "Stijgend",
  "talent_pool_size": "15.000",
  "contract_permanent": 70,
  "contract_temporary": 20,
  "contract_freelance": 10,
  "average_age": 42,
  "gender_ratio": "65/35",
  "doelgroep_skills": [
    {"naam": "Python Skills", "percentage": 35, "beschrijving": "Van professionals"},
    {"naam": "Leadership", "percentage": 18, "beschrijving": "Met ervaring"}
  ],
  "leeftijd_verdeling": [
    {"leeftijd": "20-30 jaar", "percentage": 22},
    {"leeftijd": "30-40 jaar", "percentage": 35},
    {"leeftijd": "40-50 jaar", "percentage": 28},
    {"leeftijd": "50+ jaar", "percentage": 15}
  ],
  "push_factors": [
    {"factor": "Hoger salaris", "impact": "Hoog"},
    {"factor": "Carrièremogelijkheden", "impact": "Medium"}
  ],
  "pull_factors": [
    {"factor": "Werk-privé balans", "impact": "Hoog"},
    {"factor": "Innovatieve werkgever", "impact": "Medium"}
  ],
  "technical_skills": [
    {"naam": "Python", "percentage": 45, "kleur": "groen"},
    {"naam": "Django", "percentage": 28, "kleur": "oranje"}
  ],
  "soft_skills": [
    {"naam": "Leadership", "prioriteit": "Kritiek"},
    {"naam": "Communicatie", "prioriteit": "Hoog"}
  ]
}
```

### **Stap 4: Kopieer Template ID**

1. Na het maken van de template, zie je rechts bovenin de Template ID
2. Format: `XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX`
3. Kopieer deze voor later gebruik

---

## 🔑 API Keys Benodigdheden

### **Claude API Key:**
1. https://console.anthropic.com/settings/keys
2. Create Key
3. Kopieer key (begint met `sk-ant-api03-`)
4. Voeg toe aan Zapier Step 2

### **PDFMonkey API Key:**
1. https://app.pdfmonkey.io/settings/api
2. Kopieer "Private API Key"
3. Gebruikt automatisch door Zapier PDFMonkey app

---

## 🧪 Testing Checklist

### **Pre-Test:**
- [ ] Claude API key toegevoegd aan Step 2
- [ ] PDFMonkey account connected in Zapier
- [ ] PDFMonkey template gemaakt en getest
- [ ] All form fields mapped correctly

### **Test 1 - Minimaal:**
```
Bedrijfsnaam: Test BV
Functietitel: Test Developer
Email: jouw@test.com
```
**Verwacht:** Email + PDF met fallback AI data

### **Test 2 - Volledig:**
```
Alle velden ingevuld
URLs toegevoegd
```
**Verwacht:** Email + PDF met complete AI analyse

### **Controleer:**
- [ ] Email ontvangen binnen 2 minuten
- [ ] PDF attachment aanwezig
- [ ] PDF opent correct
- [ ] Alle data zichtbaar in PDF
- [ ] Recruitin branding correct
- [ ] AI analyse logisch

---

## 🐛 Troubleshooting

### **"PDFMonkey step failed"**
**Oplossing:**
1. Check PDFMonkey dashboard voor errors
2. Verify template exists
3. Check payload format (must be valid JSON)
4. Test template manually in PDFMonkey

### **"PDF is blank/incomplete"**
**Oplossing:**
1. Check template HTML syntax
2. Verify all variables exist in payload
3. Test with simplified payload first

### **"Email has no attachment"**
**Oplossing:**
1. Add Delay step (5 sec) before Gmail
2. Check {{3. download_url}} is not empty
3. Verify PDFMonkey step completed successfully

### **"PDF takes too long"**
**Oplossing:**
1. Free tier heeft rate limits
2. Upgrade naar Starter plan
3. Add longer Delay (10 sec)

---

## 💡 Pro Tips

1. **PDF Design:**
   - Test op verschillende PDF readers (Adobe, Chrome, Preview)
   - Gebruik web-safe fonts
   - Page breaks voorkomen afgebroken content

2. **Performance:**
   - Delay step voorkomt "attachment not found" errors
   - PDFMonkey caches templates (snel bij herhaald gebruik)

3. **Branding:**
   - Upload Recruitin logo naar PDFMonkey
   - Gebruik in template: `<img src="{{logo_url}}">`

4. **Cost Optimization:**
   - Free tier = 300 PDFs/maand
   - Monitor usage in PDFMonkey dashboard
   - Upgrade pas nodig bij >300/maand

---

## 🚀 Go-Live Checklist

- [ ] Workflow compleet (5 stappen)
- [ ] Claude API key werkend
- [ ] PDFMonkey template live
- [ ] Test succesvol (minimaal + volledig)
- [ ] PDF ziet er professioneel uit
- [ ] Email + PDF ontvangen
- [ ] Recruitin branding correct
- [ ] Zap turned ON

---

## 📊 Workflow Diagram

```
┌─────────────────────┐
│  JotForm Submission │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Python AI Analysis  │  ← Claude Sonnet 4.5
│ (Step 2)            │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ PDFMonkey Generate  │  ← Creates PDF
│ (Step 3)            │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Delay 5 seconds     │
│ (Step 4)            │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Gmail Send          │  ← Email + PDF
│ (Step 5)            │
└─────────────────────┘
```

**Total time:** ~15-30 seconden per rapport

---

## 📈 Expected Results

**Email bevat:**
- ✅ Professionele HTML email body
- ✅ PDF attachment (2-5 MB)
- ✅ CC naar klant
- ✅ Recruitin branding

**PDF bevat:**
- ✅ 3-5 pagina's met complete analyse
- ✅ AI-gedreven insights
- ✅ Charts/progressbars (CSS-based)
- ✅ Printable/shareable format

---

**Klaar voor productie! 🎉**
