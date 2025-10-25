# 🚀 ZAPIER FLOW B - Zonder PDFMonkey (Budget Versie)

## 📋 Overzicht

Deze flow genereert **HTML email rapporten** zonder PDF, maar met Formatter voor data transformatie.

**Voordelen:**
- ✅ Goedkoper (geen PDFMonkey nodig)
- ✅ Sneller (geen PDF generatie)
- ✅ Geschikt voor snelle interne rapporten
- ✅ Email kan direct gelezen worden

**Kosten:**
- Zapier Free tier: €0
- Claude AI: ~€0.02 per rapport
- **Totaal: ~€0.02 per rapport**

---

## 🔧 Complete Workflow (4 stappen)

### **STAP 1: JotForm Trigger**

**App:** JotForm
**Trigger:** New Submission
**Form ID:** `252881347421054`

**Test:** Submit test form

---

### **STAP 2: Formatter - Text (Optional - Data Cleaning)**

**App:** Formatter by Zapier
**Transform:** Text

**Use Cases:**
1. **Capitalize Names:**
   - Input: `{{1. contactpersoon}}`
   - Transform: Title Case
   - Output: Proper capitalization

2. **Clean Phone Numbers:**
   - Input: `{{1. telefoon}}`
   - Transform: Remove Non-Numbers
   - Output: Clean phone number

3. **Format Date:**
   - Input: `{{1. submission_date}}`
   - Transform: Format (DD MMMM YYYY)
   - Output: Nederlandstalige datum

**Multiple Formatters (Optional):**
Je kunt meerdere formatter steps toevoegen:
- Step 2A: Format contactpersoon (Title Case)
- Step 2B: Format telefoon (Clean)
- Step 2C: Format datum (Dutch date)

**Of sla deze stap OVER** als je geen data cleaning nodig hebt.

---

### **STAP 3: Python AI Analysis**

**App:** Code by Zapier
**Runtime:** Python 3.11

**Input Data Mapping:**
```
claude_api_key: sk-ant-[JE_CLAUDE_API_KEY]

bedrijfsnaam: {{1. bedrijfsnaam}}
contactpersoon: {{2. output}} (als Formatter gebruikt, anders {{1. contactpersoon}})
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
# Kopieer de code uit: zapier-ai-rapport-pdfmonkey-2025.py
# Deze code werkt ZONDER PDFMonkey
# Output bevat alleen email_body_html (geen PDF)
```

**Output Fields:**
- `email_to`
- `email_cc`
- `email_subject`
- `email_body_html`
- `notion_*` (voor Notion integratie)
- `ai_used`
- `data_betrouwbaarheid`
- `current_date`

---

### **STAP 4: Gmail - Send HTML Email**

**App:** Gmail
**Action:** Send Email

**Configuration:**
```
To: {{3. email_to}}
CC: {{3. email_cc}}
Subject: {{3. email_subject}}
Body Type: HTML
Body: {{3. email_body_html}}
```

**Advanced Options:**
- Reply To: warts@recruitin.nl
- From Name: Recruitin AI Intelligence
- Attachments: (geen - dit is de budget versie)

---

## 🎨 Formatter Use Cases (Advanced)

### **Use Case 1: Clean & Format Contact Data**

**Step 2A - Format Naam:**
```
App: Formatter
Transform: Text
Function: Title Case
Input: {{1. contactpersoon}}
```
Output: "Jan De Vries" → "Jan de Vries"

**Step 2B - Clean Telefoon:**
```
App: Formatter
Transform: Text
Function: Replace
Input: {{1. telefoon}}
Find: [^0-9+]
Replace with: (empty)
```
Output: "+31 (0)6-1234 5678" → "+31612345678"

**Step 2C - Format Bedrijfsnaam:**
```
App: Formatter
Transform: Text
Function: Trim Whitespace
Input: {{1. bedrijfsnaam}}
```
Output: " Tech BV  " → "Tech BV"

---

### **Use Case 2: Generate Custom Subject Line**

**Step 2: Formatter - Text**
```
Transform: Text
Function: Default Value
Input: {{1. urgentie}}
Default: Normaal
```

**Then in Python or Gmail step:**
```python
subject_prefix = "🔥 URGENT:" if urgentie == "Hoog" else "📊"
email_subject = f"{subject_prefix} AI Recruitment Intelligence: {functietitel}"
```

---

### **Use Case 3: Date Formatting (Dutch)**

**Step 2: Formatter - Date/Time**
```
Transform: Format
Input: {{1. submission_date}}
To Format: DD MMMM YYYY
Timezone: Europe/Amsterdam
```
Output: "25 Oktober 2025"

---

### **Use Case 4: Skills List Cleanup**

**If JotForm gives comma-separated skills:**

**Step 2: Formatter - Text**
```
Transform: Split Text
Input: {{1. key_skills}}
Separator: ,
Segment Index: all
```
Output: Array van skills

**Then gebruik in Python:**
```python
key_skills = input_data.get('key_skills', [])
if isinstance(key_skills, str):
    key_skills = [s.strip() for s in key_skills.split(',')]
```

---

## 🔧 Formatter Strategies

### **Strategie 1: Minimaal (Geen Formatter)**
```
JotForm → Python → Gmail
```
**Pro:** Simpel, snel
**Con:** Ruwe data (mogelijke formatting issues)

### **Strategie 2: Basic Cleanup (1 Formatter step)**
```
JotForm → Formatter (naam cleanup) → Python → Gmail
```
**Pro:** Kleine verbetering, weinig extra work
**Con:** Beperkte cleaning

### **Strategie 3: Full Cleanup (Multiple Formatters)**
```
JotForm →
  Formatter A (naam) →
  Formatter B (telefoon) →
  Formatter C (datum) →
Python → Gmail
```
**Pro:** Schone, consistente data
**Con:** Meer Zapier steps (hogere task count)

**Aanbeveling:** Start met Strategie 1, voeg Formatter toe als je data quality issues ziet.

---

## 🧪 Testing Checklist

### **Pre-Test:**
- [ ] Claude API key toegevoegd aan Step 3 (of Step 2 als geen Formatter)
- [ ] Gmail connected en geauthorized
- [ ] All form fields mapped correctly
- [ ] Formatter steps tested (if used)

### **Test 1 - Minimaal:**
```
Bedrijfsnaam: Test BV
Functietitel: Test Developer
Email: jouw@test.com
```
**Verwacht:** HTML email met fallback AI data

### **Test 2 - Met Formatter:**
```
Contactpersoon: jAn dE vRiEs (bad formatting)
Telefoon: +31 (0)6-1234 5678 (with spaces)
```
**Verwacht:** Cleaned data in email

### **Test 3 - Volledig:**
```
Alle velden ingevuld
URLs toegevoegd
```
**Verwacht:** Email met complete AI analyse

### **Controleer:**
- [ ] Email ontvangen binnen 1 minuut
- [ ] HTML renders correctly (open in Gmail/Outlook)
- [ ] Alle data zichtbaar
- [ ] Formatter cleaned data correctly
- [ ] AI analyse logisch
- [ ] Recruitin branding correct

---

## 🎨 Email Styling Tips

De HTML email gebruikt responsive tables. Test in:
- ✅ Gmail (web + mobile app)
- ✅ Outlook (web + desktop)
- ✅ Apple Mail
- ✅ Thunderbird

**Common Issues:**

**Issue 1: "Email looks broken in Outlook"**
**Fix:** Email template gebruikt table-based layout (Outlook compatible)

**Issue 2: "Colors not showing"**
**Fix:** Use inline styles (already done in template)

**Issue 3: "Images missing"**
**Fix:** Template uses emoji icons (no external images needed)

---

## 🐛 Troubleshooting

### **"Formatter step failed"**
**Oplossing:**
1. Check input value exists (not empty)
2. Use "Continue on Error" in Formatter settings
3. Provide default value

### **"Email HTML looks broken"**
**Oplossing:**
1. Test in Gmail first (best HTML support)
2. Check for missing closing tags in template
3. Validate HTML syntax

### **"Variables showing as {{variable}}"**
**Oplossing:**
1. Check variable mapping in Python step
2. Ensure output dict has all keys
3. Add fallback values in Python code

### **"Email too large"**
**Oplossing:**
1. Gmail limit: 25 MB (should be fine)
2. Reduce AI analysis text length
3. Remove base64 images if any

---

## 💰 Cost Comparison

### **Flow A (Met PDFMonkey):**
- Zapier: Free tier OK
- PDFMonkey: €0 (tot 300/maand)
- Claude AI: ~€0.02
- **Total: ~€0.02/rapport + PDF**

### **Flow B (Met Formatter):**
- Zapier: Free tier OK
- Formatter: Included in Free tier
- Claude AI: ~€0.02
- **Total: ~€0.02/rapport (alleen email)**

**Besparing Flow B:** €0 per maand, maar geen PDF

---

## 📊 Workflow Diagrams

### **Minimaal (Zonder Formatter):**
```
┌─────────────────────┐
│  JotForm Submission │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Python AI Analysis  │  ← Claude AI
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Gmail Send Email    │  ← HTML Email
└─────────────────────┘
```

### **Met Formatter:**
```
┌─────────────────────┐
│  JotForm Submission │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Formatter (cleanup) │  ← Data cleaning
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Python AI Analysis  │  ← Claude AI
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Gmail Send Email    │  ← HTML Email
└─────────────────────┘
```

**Total time:** ~10-20 seconden per rapport

---

## 🚀 Go-Live Checklist

- [ ] Workflow compleet (3-4 stappen)
- [ ] Claude API key werkend
- [ ] Formatter tested (if used)
- [ ] Test succesvol (minimaal + volledig)
- [ ] Email HTML ziet er goed uit
- [ ] Data formatting correct
- [ ] Recruitin branding correct
- [ ] Zap turned ON

---

## 💡 When to Use Flow B vs Flow A?

### **Use Flow B when:**
- ✅ Budget is priority
- ✅ Interne rapporten (niet klant-facing)
- ✅ Email voldoende is
- ✅ Snelheid belangrijker dan presentatie

### **Use Flow A when:**
- ✅ Professionele rapportage nodig
- ✅ Klant moet PDF kunnen delen/printen
- ✅ Formele documentatie vereist
- ✅ Betere presentatie gewenst

**Aanbeveling:** Start met Flow B, upgrade naar Flow A als klanten om PDF vragen.

---

## 🔄 Upgraden van Flow B naar Flow A

Als je later wilt upgraden:

1. **Voeg toe na Python step:**
   - PDFMonkey Generate (Step 4)
   - Delay 5 sec (Step 5)

2. **Update Gmail step:**
   - Attachments: {{4. download_url}}

3. **Test:** Submit test form

**Geen wijzigingen nodig aan:**
- ✅ JotForm
- ✅ Formatter
- ✅ Python code
- ✅ Email HTML

---

**Klaar voor productie! 🎉**

**Next:** Kies Flow A of B, configureer in Zapier, en test!
