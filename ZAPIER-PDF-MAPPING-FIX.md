# 🔧 Zapier PDF Field Mapping Fix
## Probleem: Step 2 verwijst naar verkeerde PDF extraction step IDs

---

## ⚠️ HET PROBLEEM

Je Zapier Step 2 (Python Code) probeert te verwijzen naar:
- `{{329388874__extracted_text}}` ← **Bestaat niet (meer)**
- `{{_GEN_1761503019716__extracted_text}}` ← **Bestaat niet (meer)**
- `{{_GEN_1761503019717__extracted_text}}` ← **Bestaat niet (meer)**

**Resultaat:** Python code krijgt geen data van de 3 PDF extraction stappen.

---

## ✅ DE OPLOSSING - Stap voor Stap

### **STAP 1: Vind de JUISTE Step IDs**

1. **Open je Zap in Zapier editor**
2. **Bekijk alle stappen tussen JotForm en Python Code**
3. **Identificeer de 3 PDF extraction stappen:**
   - Bijvoorbeeld: "Extract Text from PDF in Dropbox" of "Parse PDF"
   - Elke stap heeft een **uniek step ID nummer**

4. **Noteer de step IDs:**
   ```
   Step ?: PDF Extraction 1 (Jobdigger) → ID: _______
   Step ?: PDF Extraction 2 (LinkedIn)  → ID: _______
   Step ?: PDF Extraction 3 (Vacature)  → ID: _______
   ```

### **STAP 2: Vind de Juiste Field Names**

Voor elke PDF extraction step:

1. **Klik op de step**
2. **Scroll naar "Test Result"** (onderaan)
3. **Zoek naar het veld met de extracted text:**
   - Meestal heet dit: `text`, `extracted_text`, `content`, of `plain_text`
4. **Noteer de exacte field name**

**Voorbeeld van wat je ziet:**
```json
{
  "id": "329388908",
  "extracted_text": "Dit is de tekst uit de PDF...",
  "file_name": "jobdigger_rapport.pdf"
}
```
→ Field name = `extracted_text`

---

### **STAP 3: Update Python Code Input Mapping**

1. **Ga naar je Python Code step (Step 2)**
2. **Klik op "Set up action"**
3. **Scroll naar "Input Data"**
4. **Vind deze 3 velden:**
   - `jobdigger_extracted_text`
   - `linkedin_extracted_text`
   - `vacature_extracted_text`

5. **Klik in elk veld en selecteer de JUISTE step + field:**

**VOOR (❌ FOUT):**
```
jobdigger_extracted_text: {{329388874__extracted_text}}  ← Bestaat niet!
```

**NA (✅ CORRECT):**
```
jobdigger_extracted_text: {{3. Extract Text from PDF (Jobdigger): Extracted Text}}
```

---

## 🎯 EXACTE MAPPING INSTRUCTIES

In je Python Code step, update deze Input Data velden:

### **Input Data Veld 1: `jobdigger_extracted_text`**
- **Klik in het veld**
- **Zoek de PDF extraction step voor Jobdigger rapport**
- **Selecteer het `extracted_text` veld (of `text`, `content`)**
- **Voorbeeld:** `{{3. Extract PDF Jobdigger: Extracted Text}}`

### **Input Data Veld 2: `linkedin_extracted_text`**
- **Klik in het veld**
- **Zoek de PDF extraction step voor LinkedIn Talent Insights**
- **Selecteer het `extracted_text` veld**
- **Voorbeeld:** `{{4. Extract PDF LinkedIn: Extracted Text}}`

### **Input Data Veld 3: `vacature_extracted_text`**
- **Klik in het veld**
- **Zoek de PDF extraction step voor Vacature PDF**
- **Selecteer het `extracted_text` veld**
- **Voorbeeld:** `{{5. Extract PDF Vacature: Extracted Text}}`

---

## 📸 HOE VIND JE DE JUISTE FIELD MAPPING?

### **Methode 1: Via het Dropdown Menu**
1. Klik in het Input Data veld
2. Je ziet een dropdown met alle vorige stappen
3. Zoek de PDF extraction step
4. Klik erop → Zoek "Extracted Text" of "Text" of "Content"
5. Klik om te selecteren

### **Methode 2: Via "Insert Data" Button**
1. Klik op het **"+"** icoontje naast het veld
2. Je ziet "Choose an option" dropdown
3. Selecteer de PDF extraction step
4. Selecteer het text veld

### **Methode 3: Test & Check**
1. Update één veld
2. Klik "Test action" onderaan
3. Check of de Python output nu wél PDF tekst bevat
4. Herhaal voor de andere 2 velden

---

## ✅ VERIFICATIE CHECKLIST

Na het updaten van de mappings:

- [ ] **Test de Python step:** Klik "Test action"
- [ ] **Check de output:** Zie je tekst uit de 3 PDFs in de `ai_analysis` output?
- [ ] **Check HTML email:** Bevat het rapport realistische data (geen demo data)?
- [ ] **Test volledige flow:** Doe een test submission via de website
- [ ] **Check Gmail:** Komt het rapport binnen met goede data?

---

## 🔍 DEBUGGING - Als het nog niet werkt

### **Probleem: Python step krijgt nog steeds lege data**

**Check 1: Zijn de PDF extraction steps succesvol?**
- Klik op elke PDF extraction step
- Klik "Test action"
- Zie je extracted tekst in de output?
- Zo niet → Fix eerst de PDF extraction

**Check 2: Zijn de field names correct gespeld?**
- Case-sensitive! `Extracted Text` ≠ `extracted_text`
- Spaties tellen! `Extracted Text` ≠ `ExtractedText`

**Check 3: Gebruikt Python code de juiste input variable names?**
- Python code moet deze variabelen gebruiken:
  ```python
  jobdigger_text = input_data.get('jobdigger_extracted_text', '')
  linkedin_ti_text = input_data.get('linkedin_extracted_text', '')
  vacature_pdf_text = input_data.get('vacature_extracted_text', '')
  ```
- De Input Data keys moeten EXACT overeenkomen!

---

## 🎯 SAMENVATTING

**Wat je moet doen:**
1. ✅ Vind de 3 PDF extraction step IDs in je Zap
2. ✅ Vind de extracted text field names (meestal `extracted_text`)
3. ✅ Update de 3 input mappings in Python Code step
4. ✅ Test de flow end-to-end
5. ✅ Verify dat email realistische AI-gegenereerde data bevat

**Het resultaat:**
- Python code krijgt tekst uit alle 3 PDFs ✅
- Claude AI analyseert de volledige context ✅
- Email rapport bevat realistische market intelligence ✅

---

## 📞 Hulp Nodig?

Als je de juiste step IDs hebt gevonden maar niet weet hoe te mappen, geef me:
1. Screenshot van je Zap steps overview
2. De step numbers van de 3 PDF extraction stappen
3. De field names die je ziet in de Test Results

Dan kan ik de exacte mapping voor je maken! 🚀
