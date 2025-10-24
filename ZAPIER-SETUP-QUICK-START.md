# ⚡ ZAPIER QUICK START GUIDE
## AI-Gedreven Recruitment Intelligence

---

## 🎯 STAP 1: Update Code in Zapier

1. **Open je Zapier workflow**
2. **Ga naar Step 5: Code by Zapier**
3. **Delete de oude code volledig**
4. **Copy-paste de nieuwe code** uit `zapier-ai-rapport-clean.py`
5. **Klik "Save"**

---

## 🔧 STAP 2: Configureer Input Fields (Step 5)

Scroll naar beneden in Step 5 naar "Input Data". Map deze velden:

### ✅ Verplichte Velden
```
claude_api_key: [JE CLAUDE API KEY HIER - zie eerder in conversatie]

bedrijfsnaam: {{1. Bedrijfsnaam}}
functietitel: {{1. Functietitel}}
contactpersoon: {{1. Contactpersoon}}
email: {{1. Email}}
telefoon: {{1. Telefoon}}
sector: {{1. Sector}}
locatie: {{1. Locatie}}
urgentie: {{1. Urgentie}}
```

### 📄 Document URLs (van JotForm uploads)
```
jobdigger_url: {{1. Jobdigger PDF URL}}
linkedin_ti_url: {{1. LinkedIn TI PDF URL}}
vacature_url: {{1. Vacature URL}}
```

### 📝 Extracted Text (van Steps 2, 3, 4)
```
jobdigger_text: {{2. Output Text}}
linkedin_ti_text: {{3. Output Text}}
vacature_text: {{4. Output Text}}
```

### 📋 Optionele Velden
```
extra_info: {{1. Extra Informatie}}
aantal_posities: {{1. Aantal Posities}}
submission_url: {{1. Submission URL}}
submission_id: {{1. Submission ID}}
```

---

## 📧 STAP 3: Configureer Gmail Step (Step 6)

1. **To**: `{{5. email_to}}` (of handmatig: warts@recruitin.nl)
2. **Subject**: `{{5. email_subject}}`
3. **Body Type**: HTML
4. **Body**: `{{5. email_body_html}}`

---

## 📊 STAP 4: Configureer Notion Step (Step 7)

### Database Properties Mapping

```yaml
# Title (verplicht)
Bedrijfsnaam: {{5. notion_bedrijfsnaam}}

# Basis Info
Functietitel: {{5. notion_functietitel}}
Contactpersoon: {{5. notion_contactpersoon}}
Email: {{5. notion_email}}
Telefoon: {{5. notion_telefoon}}

# Vacature Details
Sector: {{5. notion_sector}}
Locatie: {{5. notion_locatie}}
Salaris Range: {{5. notion_salaris_range}}
Urgentie: {{5. notion_urgentie}}
Intelligence Type: {{5. notion_intelligence}}

# Status & Datum
Status: {{5. notion_status}}
Datum: {{5. notion_datum}}

# AI Analysis
AI Schaarste: {{5. notion_ai_schaarste}}
AI Time to Hire: {{5. notion_ai_time_to_hire}}

# URLs (DE FIX VOOR JE ERROR!)
Vacature URL: {{5. notion_vacature_url}}
Jobdigger URL: {{5. notion_jobdigger_url}}
LinkedIn TI URL: {{5. notion_linkedin_ti_url}}
```

**⚠️ BELANGRIJK**: Deze laatste 3 URL velden zijn de fix voor je error!

---

## 🧪 STAP 5: Test de Workflow

1. **Klik "Test" in Zapier** (rechtsboven)
2. **Selecteer een recent JotForm submission**
3. **Run test voor elke step**
4. **Check**:
   - ✅ Step 5 (Code) geeft output zonder errors
   - ✅ Step 6 (Gmail) verstuurt email
   - ✅ Step 7 (Notion) maakt database item **zonder URL error**

---

## ❌ ERROR CHECKLIST

### Error: "ModuleNotFoundError: No module named 'anthropic'"
- ✅ **OPGELOST**: Gebruik de nieuwe `zapier-ai-rapport-clean.py` code

### Error: "body.children[9].bulleted_list_item.rich_text[0].text.link.url should be populated"
- ✅ **OPGELOST**: Nieuwe code gebruikt `None` in plaats van `""` voor lege URLs
- Zorg dat je de 3 URL output velden correct mapped hebt in Notion

### Error: "API key invalid"
- Check of je Claude API key correct is: `sk-ant-api03-uUH...`
- Test op https://console.anthropic.com/

### Error: "Timeout"
- Claude AI call duurt max 60 seconden
- Als het faalt, gebruikt code automatisch fallback demo data

---

## 💰 KOSTEN INDICATIE

**Per rapport met AI analyse**:
- Input: ~5.000 tokens (3x documenten @ 5KB each)
- Output: ~1.000 tokens (JSON response)
- Cost: **€0,50 - €2,00** per rapport

**Claude Sonnet 4.5 Pricing**:
- Input: $3 per 1M tokens
- Output: $15 per 1M tokens

**Tip**: Monitor gebruik op https://console.anthropic.com/settings/cost

---

## 🚀 PRODUCTION CHECKLIST

- [ ] Code updated in Zapier Step 5
- [ ] All input fields configured
- [ ] Claude API key added
- [ ] Gmail step configured
- [ ] Notion step configured met 3 URL velden
- [ ] Test run succesvol (geen errors)
- [ ] Email ontvangen en HTML ziet er goed uit
- [ ] Notion item aangemaakt zonder errors
- [ ] Workflow "ON" gezet in Zapier

---

## 📞 VOLGENDE STAPPEN

1. ✅ **Deploy**: Zet workflow op "ON"
2. 🧪 **Test**: Vul JotForm in met echte data
3. 📊 **Monitor**: Check eerste 5 submissions
4. 🎉 **Live**: Deel form link met klanten!

---

**Vragen?** Check `notion-database-template.md` voor meer details over Notion setup.

**Succes!** 🚀
