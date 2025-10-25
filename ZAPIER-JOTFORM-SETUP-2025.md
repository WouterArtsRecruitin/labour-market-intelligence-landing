# 🚀 Zapier Workflow Setup Guide - JotForm 252881347421054 (2025)

## 📋 Overzicht

Deze guide helpt je de Zapier workflow op te zetten voor de **nieuwe simplified JotForm** met alleen essentiële velden en PDF uploads.

---

## 📝 JotForm Velden (8 totaal)

### ✅ **VEREIST** (3 velden):
1. **Functietitel** - Tekstveld
2. **Locatie/Regio** - Tekstveld
3. **E-mail voor Rapportage** - Email veld

### 📎 **OPTIONEEL** (5 velden):
4. **Upload Jobdigger PDF** - File upload
5. **Upload LinkedIn Talent Insights PDF** - File upload
6. **Upload vacature** - File upload
7. **Vacaturetekst** - Textarea
8. **Vacature URL** - Tekstveld

---

## 🔧 Zapier Workflow Stappen

### **Stap 1: Trigger - JotForm (New Submission)**

**Setup:**
1. Kies **JotForm** app
2. Trigger: **New Submission**
3. Selecteer form: **252881347421054**
4. Test de trigger

**Veld Mapping:**
- `functietitel` → JotForm veld "Functietitel"
- `locatieRegio` → JotForm veld "Locatie/Regio"
- `emailVoorRapportage` → JotForm veld "E-mail voor Rapportage"
- `uploadJobdiggerPdf` → JotForm veld "Upload Jobdigger PDF (optioneel)"
- `uploadLinkedinPdf` → JotForm veld "Upload LinkedIn Talent Insights PDF (optioneel)"
- `uploadVacature` → JotForm veld "Upload vacature (optioneel)"
- `vacaturetekst` → JotForm veld "Vacaturetekst (optioneel)"
- `vacatureUrl` → JotForm veld "Vacature URL (optioneel)"

---

### **Stap 2: Extract Text from PDF - Jobdigger (Only If...)**

**Conditional Logic:**
- **Only continue if:** `uploadJobdiggerPdf` exists / is not empty

**Setup:**
1. Kies **Extract Text from PDF** (Zapier built-in)
2. **PDF File:** `{{Step 1: uploadJobdiggerPdf}}`
3. **Output:** Plain text

**Map als:**
- `jobdigger_extracted_text` → Output van deze stap

---

### **Stap 3: Extract Text from PDF - LinkedIn TI (Only If...)**

**Conditional Logic:**
- **Only continue if:** `uploadLinkedinPdf` exists / is not empty

**Setup:**
1. Kies **Extract Text from PDF**
2. **PDF File:** `{{Step 1: uploadLinkedinPdf}}`
3. **Output:** Plain text

**Map als:**
- `linkedin_extracted_text` → Output van deze stap

---

### **Stap 4: Extract Text from PDF - Vacature (Only If...)**

**Conditional Logic:**
- **Only continue if:** `uploadVacature` exists / is not empty

**Setup:**
1. Kies **Extract Text from PDF**
2. **PDF File:** `{{Step 1: uploadVacature}}`
3. **Output:** Plain text

**Map als:**
- `vacature_extracted_text` → Output van deze stap

---

### **Stap 5: Code by Zapier - Python**

**Setup:**
1. Kies **Code by Zapier**
2. Language: **Python 3.11**
3. **Input Data:**

```
claude_api_key: [JE CLAUDE API KEY]
functietitel: {{Step 1: functietitel}}
locatieRegio: {{Step 1: locatieRegio}}
emailVoorRapportage: {{Step 1: emailVoorRapportage}}
jobdigger_extracted_text: {{Step 2: Output}} (if exists)
linkedin_extracted_text: {{Step 3: Output}} (if exists)
vacature_extracted_text: {{Step 4: Output}} (if exists)
vacaturetekst: {{Step 1: vacaturetekst}}
vacatureUrl: {{Step 1: vacatureUrl}}
```

4. **Code:** Kopieer de volledige inhoud van `zapier-ai-rapport-jotform-2025.py`

---

### **Stap 6: Gmail - Send Email**

**Setup:**
1. Kies **Gmail** app
2. Action: **Send Email**
3. **To:** `{{Step 5: recipient_email}}`
4. **Subject:** `Arbeidsmarkt Intelligence Rapport - {{Step 5: functietitel}}`
5. **Body Type:** HTML
6. **Body:** `{{Step 5: html_email}}`

**Optional CC:**
- Add: `warts@recruitin.nl`

---

## 🔑 Belangrijke Notes

### **Claude API Key:**
Je hebt een Claude API key nodig van Anthropic:
1. Ga naar: https://console.anthropic.com/
2. Maak een API key aan
3. Voeg toe aan Stap 5 input: `claude_api_key`

### **Veld Namen in JotForm:**
JotForm geeft velden automatisch namen zoals:
- `q3_functietitel`
- `q5_locatieregio`
- `q7_emailVoor`
- etc.

**Gebruik deze exacte namen** in de Zapier mapping.

### **PDF File URLs:**
JotForm retourneert file uploads als **URLs**. Zapier's "Extract Text from PDF" kan deze URLs direct lezen.

### **Conditional Steps:**
De PDF extraction stappen (2, 3, 4) gebruiken "Filter" of "Only continue if" zodat ze alleen runnen als er een PDF geüpload is.

---

## 🧪 Testing Workflow

### **Test Data:**
1. **Functietitel:** "Senior Data Engineer"
2. **Locatie:** "Amsterdam, Noord-Holland"
3. **Email:** "jouw@email.com"
4. Upload minimaal 1 PDF voor testing

### **Expected Output:**
- ✅ HTML email rapport verzonden naar opgegeven email
- ✅ CC naar warts@recruitin.nl
- ✅ Rapport bevat AI-gegenereerde data uit PDFs
- ✅ Rapport bevat alle secties (schaarste, salaris, skills, etc.)

---

## 🐛 Troubleshooting

### **Problem: "No PDF text extracted"**
- **Oorzaak:** PDF is een scan/afbeelding zonder OCR
- **Oplossing:** Gebruik PDF's met echte tekst, of voeg OCR toe

### **Problem: "Claude API error"**
- **Oorzaak:** Ongeldige API key of rate limit
- **Oplossing:** Check API key in Anthropic Console

### **Problem: "Email not sent"**
- **Oorzaak:** Gmail permissions
- **Oplossing:** Reconnect Gmail in Zapier

### **Problem: "Missing fields in rapport"**
- **Oorzaak:** Geen PDF's geüpload
- **Oplossing:** AI gebruikt fallback data - dit is normaal!

---

## 📊 Workflow Diagram

```
JotForm Submission
        ↓
[If Jobdigger PDF exists]
        ↓
Extract Text from Jobdigger PDF
        ↓
[If LinkedIn PDF exists]
        ↓
Extract Text from LinkedIn PDF
        ↓
[If Vacature PDF exists]
        ↓
Extract Text from Vacature PDF
        ↓
Python Code (AI Analysis)
        ↓
Send Email (Gmail)
        ↓
Done! ✅
```

---

## 🚀 Go Live Checklist

- [ ] JotForm trigger geconfigureerd
- [ ] PDF extraction stappen toegevoegd (met filters)
- [ ] Python code gekopieerd naar Stap 5
- [ ] Claude API key toegevoegd
- [ ] Gmail connected en getest
- [ ] Test submission succesvol
- [ ] Email ontvangen met volledig rapport
- [ ] Zap is ON (published)

---

## 💡 Tips

1. **Test met minimaal 1 PDF** om te zien dat extraction werkt
2. **Check spam folder** als email niet aankomt
3. **Claude API kosten:** ~$0.01 per rapport (zeer goedkoop)
4. **Fallback data werkt prima** als PDF's ontbreken
5. **Email template is responsive** - werkt op mobiel

---

## 📞 Support

Vragen? Check:
- `zapier-ai-rapport-jotform-2025.py` - De Python code
- `NOTION-ERROR-DEBUG.md` - Error handling
- Zapier Community: https://community.zapier.com/

**Let's go! 🚀**
