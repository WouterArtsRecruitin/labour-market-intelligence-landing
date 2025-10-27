# 📦 ZAPIER PYTHON CODE VERSIES - OVERZICHT

**Laatst bijgewerkt:** 27 Oktober 2025

---

## 🎯 WELKE CODE MOET IK GEBRUIKEN?

### ✅ **AANBEVOLEN: `zapier-simple-rapport-BACKUP.py`**

**Gebruik deze als:**
- Je een simpele, werkende versie wilt zonder complexiteit
- Je geen Anthropic SDK dependency issues wilt
- Je een clean, tabel-based HTML rapport wilt
- Je snel wilt starten zonder veel setup

**Voordelen:**
- ✅ Compact (250 regels)
- ✅ Simple HTML styling (goed leesbaar)
- ✅ Gebruikt `requests` library (standaard in Zapier)
- ✅ Gecondenseerde maar complete Claude prompt
- ✅ Makkelijk te debuggen

**Nadelen:**
- ⚠️ Hardcoded API key (security risk)
- ⚠️ Minder fancy HTML design
- ⚠️ Geen environment variable support

---

### 🚀 **ADVANCED: `zapier-executive-rapport-generator.py`**

**Gebruik deze als:**
- Je een executive-level professional design wilt
- Je de officiële Anthropic SDK wilt gebruiken
- Je environment variables wilt voor API key
- Je uitgebreide error handling nodig hebt
- Je maximale flexibiliteit wilt

**Voordelen:**
- ✅ Officiële `anthropic` SDK
- ✅ Executive-level HTML design (gradients, cards, etc.)
- ✅ Environment variable support (`CLAUDE_API_KEY`)
- ✅ Uitgebreide 500+ regels Claude prompt
- ✅ Comprehensive error handling
- ✅ Notion integration output

**Nadelen:**
- ⚠️ Grotere codebase (1,950+ regels)
- ⚠️ Vereist Anthropic SDK in Zapier (kan issues geven)
- ⚠️ Complexer om te debuggen

---

### 📊 **ALTERNATIVE: `zapier-ai-rapport-REAL-DATA-ONLY.py`**

**Gebruik deze als:**
- Je GEEN intelligente estimates wilt
- Je alleen data uit PDFs wilt gebruiken
- Je transparantie wilt over ontbrekende data
- Je "N/A" wilt zien waar data niet beschikbaar is

**Voordelen:**
- ✅ Strikte "only real data" policy
- ✅ Claude prompt verbiedt aannames
- ✅ Toont "N/A" bij ontbrekende data
- ✅ Data availability note in rapport
- ✅ Transparent over reliability

**Nadelen:**
- ⚠️ Rapporten kunnen veel "N/A" bevatten
- ⚠️ Minder bruikbaar zonder goede PDFs
- ⚠️ Kan teleurstellend zijn voor klanten

---

## 📋 VOLLEDIGE VERGELIJKINGSTABEL

| Feature | Simple Backup | Executive Generator | Real Data Only |
|---------|---------------|---------------------|----------------|
| **Code Size** | 250 regels | 1,950 regels | 656 regels |
| **API Method** | `requests` | `anthropic` SDK | `requests` |
| **HTML Design** | Simple tables | Executive gradients | Simple with warnings |
| **API Key** | Hardcoded ⚠️ | Environment var ✅ | Environment var ✅ |
| **Claude Prompt** | Condensed | Very detailed (500+ lines) | Strict extraction |
| **Missing Data** | Intelligent estimates | Intelligent estimates | Shows "N/A" |
| **Error Handling** | Basic | Comprehensive | Comprehensive |
| **Notion Output** | Yes | Yes | Yes |
| **Complexity** | Low | High | Medium |
| **Setup Time** | 5 min | 30 min | 15 min |
| **Best For** | Quick start | Professional clients | Strict data compliance |

---

## 🔧 SETUP INSTRUCTIES PER VERSIE

### **SIMPLE BACKUP VERSION**

**Stap 1:** Kopieer code uit `zapier-simple-rapport-BACKUP.py`

**Stap 2:** Plak in Zapier Step 5 (Code by Zapier)

**Stap 3:** ⚠️ **BELANGRIJK: Verander de API key!**
```python
# Regel 15: Update deze regel met JOUW API key
CLAUDE_API_KEY = "sk-ant-api03-YOUR_API_KEY_HERE"  # Replace this!

# Verander naar jouw echte key:
CLAUDE_API_KEY = "sk-ant-api03-[PASTE_JOUW_KEY_HIER]"
```

Get je API key van: https://console.anthropic.com/settings/keys

**Stap 4:** Input Data mapping (zelfde als andere versies):
```
functietitel: {{1. Functietitel}}
locatie: {{1. Locatie Regio}}
bedrijfsnaam: {{1. Bedrijfsnaam}}
email: {{1. Email Voor Rapportage}}
vacature_url: {{1. Vacature URL}}
jobdigger_pdf_text: {{2. Extract PDF: Extracted Text}}
linkedin_pdf_text: {{3. Extract PDF: Extracted Text}}
vacature_text: {{4. Extract PDF: Extracted Text}}
```

**Stap 5:** Test! ✅

**Total Setup Time:** 5-10 minuten

---

### **EXECUTIVE VERSION**

**Stap 1:** Kopieer code uit `zapier-executive-rapport-generator.py`

**Stap 2:** Plak in Zapier Step 5

**Stap 3:** Ga naar Settings tab → Environment Variables

**Stap 4:** Add variable:
```
Key: CLAUDE_API_KEY
Value: sk-ant-api03-[JOUW_KEY]
```

**Stap 5:** Input Data mapping (zie hierboven)

**Stap 6:** Test! ✅

**Total Setup Time:** 20-30 minuten

**Note:** Als je "ModuleNotFoundError: anthropic" krijgt:
- Gebruik de Simple Backup versie in plaats daarvan
- OF contact Zapier support voor SDK installatie

---

### **REAL DATA ONLY VERSION**

**Stap 1:** Kopieer code uit `zapier-ai-rapport-REAL-DATA-ONLY.py`

**Stap 2:** Plak in Zapier Step 5

**Stap 3:** Environment variable:
```
Key: CLAUDE_API_KEY
Value: sk-ant-api03-[JOUW_KEY]
```

**Stap 4:** Input Data mapping (zie hierboven)

**Stap 5:** Test met GOEDE PDFs (veel data) ✅

**Total Setup Time:** 15-20 minuten

---

## 💡 DECISION TREE

```
Wil je snel starten zonder complexity?
├─ JA → Use SIMPLE BACKUP ⭐
└─ NEE
    │
    Wil je professional executive-level design?
    ├─ JA → Use EXECUTIVE GENERATOR
    └─ NEE
        │
        Wil je alleen echte data (geen estimates)?
        ├─ JA → Use REAL DATA ONLY
        └─ NEE → Use SIMPLE BACKUP (default)
```

---

## 🔒 SECURITY NOTES

### ⚠️ **Simple Backup - Hardcoded API Key**

**Standaard:** De code heeft een placeholder `"sk-ant-api03-YOUR_API_KEY_HERE"` op regel 15

**Je MOET deze vervangen met je echte API key!**

**Risico's van hardcoded key:**
- Als iemand je Zapier account ziet, kunnen ze je key stelen
- Als je code deelt, deel je je key
- Moeilijk om key te roteren

**Oplossingen:**

**1. Optie A: Direct in code plaatsen (snelste, minder veilig)**
```python
# Regel 15: Plak je echte key
CLAUDE_API_KEY = "sk-ant-api03-[JOUW_ECHTE_KEY]"
```

**2. Optie B: Environment Variables (veiliger) ✅ AANBEVOLEN**
```python
# Verander regel 15 naar:
CLAUDE_API_KEY = os.environ.get('CLAUDE_API_KEY', 'sk-ant-api03-fallback')
```

Dan in Zapier Settings → Environment Variables:
```
CLAUDE_API_KEY = sk-ant-api03-[JOUW_ECHTE_KEY]
```

**3. Optie C: Gebruik Executive versie (heeft dit al ingebouwd)**

---

## 🧪 TESTING CHECKLIST

Na setup, test met deze scenario's:

### **Test 1: Volledig (Alle 3 PDFs)**
```json
{
  "functietitel": "Productiemanager",
  "locatie": "Nijmegen",
  "email": "jouw@email.com",
  "jobdigger_pdf_text": "[Veel tekst uit PDF]",
  "linkedin_pdf_text": "[Veel tekst uit PDF]",
  "vacature_text": "[Veel tekst uit PDF]"
}
```

**Verwacht:**
- ✅ Email binnen 90 seconden
- ✅ Reliability score: 90-98%
- ✅ Alle secties gevuld

---

### **Test 2: Minimaal (Geen PDFs)**
```json
{
  "functietitel": "Software Engineer",
  "locatie": "Amsterdam",
  "email": "jouw@email.com",
  "jobdigger_pdf_text": "",
  "linkedin_pdf_text": "",
  "vacature_text": "We zoeken een ervaren software engineer..."
}
```

**Verwacht:**
- ✅ Email binnen 90 seconden
- ⚠️ Reliability score: 60-74%
- **Simple/Executive:** Data met intelligent estimates
- **Real Data Only:** Veel "N/A" waardes

---

### **Test 3: Foutief**
```json
{
  "functietitel": "",
  "locatie": "",
  "email": "invalid-email"
}
```

**Verwacht:**
- ❌ Error handling kicks in
- ✅ Error email naar warts@recruitin.nl

---

## 📊 COST COMPARISON

Alle versies gebruiken dezelfde Claude API, dus kosten zijn identiek:

**Per rapport:**
- Input tokens: ~5,000 (PDFs + prompt)
- Output tokens: ~10,000 (JSON analysis)
- Model: Claude Sonnet 4
- **Cost: €0.15-0.25**

**Maandelijks:**
- 100 rapporten = **€20**
- 200 rapporten = **€40**
- 500 rapporten = **€100**

---

## 🐛 COMMON ISSUES

### **Issue: "ModuleNotFoundError: anthropic"**

**Versie:** Executive Generator

**Fix:**
- Switch naar Simple Backup (gebruikt `requests` library)
- OF contact Zapier support

---

### **Issue: "Claude API key not found"**

**Versie:** Executive Generator, Real Data Only

**Fix:**
1. Ga naar Step 5 → Settings → Environment Variables
2. Add: `CLAUDE_API_KEY = sk-ant-api03-...`
3. Save & Test

---

### **Issue: "JSON parse error"**

**Alle versies**

**Fix:**
- Check Claude prompt syntax
- Ensure `temperature=0.3` (not higher)
- Test prompt in Anthropic Console first

---

### **Issue: "Timeout after 30 seconds"**

**Alle versies**

**Fix:**
- Reduce PDF input size (max 15k chars)
- Lower `max_tokens` to 12000
- Check Anthropic API status

---

## 📞 SUPPORT

**Code vragen:**
- Email: warts@recruitin.nl

**Zapier issues:**
- Zapier Support Portal

**Anthropic API:**
- support@anthropic.com
- Status: https://status.anthropic.com/

---

## 🚀 DEPLOYMENT RECOMMENDATION

Voor **productie gebruik**, aanbeveling:

1. **Week 1: Start Simple**
   - Use `zapier-simple-rapport-BACKUP.py`
   - Get familiar with flow
   - Test with 10-20 real submissions

2. **Week 2-3: Monitor & Iterate**
   - Track success rate
   - Monitor costs
   - Collect user feedback

3. **Week 4: Upgrade if Needed**
   - Als alles werkt → Stay with Simple ✅
   - Als je fancy design wilt → Upgrade naar Executive
   - Als je strict data policy nodig hebt → Switch naar Real Data Only

**Bottom line:** Start simple, upgrade later if needed.

---

## 📦 FILES OVERVIEW

```
labour-market-intelligence-landing/
├── zapier-simple-rapport-BACKUP.py           ⭐ RECOMMENDED
├── zapier-executive-rapport-generator.py     🚀 ADVANCED
├── zapier-ai-rapport-REAL-DATA-ONLY.py       📊 ALTERNATIVE
├── ZAPIER-CODE-VERSIES-README.md             📖 This file
├── ZAPIER-EXECUTIVE-SETUP-COMPLETE.md        📚 Complete setup guide
├── ZAPIER-PDF-MAPPING-FIX.md                 🔧 PDF field mapping fix
└── CLAUDE-AI-ANALYSE-UITLEG.md               💡 Claude AI explanation
```

---

**Version:** 1.0
**Last Updated:** 27 Oktober 2025

**Questions? Email: warts@recruitin.nl**
