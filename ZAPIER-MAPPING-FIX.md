# 🔧 ZAPIER MAPPING FIX - JotForm Data komt niet door

## ❌ Probleem

**Symptomen:**
- ✅ JotForm trigger werkt (Stap 1)
- ❌ Stap 2 gebruikt **oude/test data** in plaats van nieuwe submission
- ❌ Formulier data komt niet door naar Python code

**Oorzaak:**
De Zapier veld mapping gebruikt **oude veldnamen** of **hardcoded test data** in plaats van dynamische JotForm velden.

---

## ✅ Oplossing: Field Mapping Opnieuw Configureren

### 🔍 Stap 1: Check JotForm Veldnamen

**In Zapier:**
1. Ga naar je Zap
2. Open **Stap 1: JotForm trigger**
3. Klik op **Test Trigger** (doe eerst een test submission!)
4. **Noteer de exacte veldnamen** die JotForm retourneert

**Voorbeeld JotForm output:**
```json
{
  "q3_functietitel": "Senior Developer",
  "q5_locatieregio": "Amsterdam",
  "q7_emailVoor": "test@example.com",
  "q9_uploadJobdigger": "https://www.jotform.com/uploads/...",
  "q11_uploadLinkedin": "https://www.jotform.com/uploads/...",
  "q13_uploadVacature": "https://www.jotform.com/uploads/...",
  "q15_vacaturetekst": "We zoeken een...",
  "q17_vacatureUrl": "https://example.com/job"
}
```

**⚠️ BELANGRIJK:** Jouw veldnamen kunnen anders zijn! Let op de **q-nummers** (bijv. `q3_`, `q5_`, etc.)

---

### 🔧 Stap 2: Update Alle Volgende Stappen

**Voor ELKE stap die JotForm data gebruikt, check de mapping:**

#### **Stap 2: Extract Text from Jobdigger PDF**

**FOUT ❌:**
```
PDF File: [hardcoded URL of oude test data]
```

**GOED ✅:**
```
PDF File: {{1. Upload Jobdigger PDF (optioneel)}}
   of
PDF File: {{1. q9_uploadJobdigger}}
```

**Hoe te fixen:**
1. Klik op het **PDF File** veld
2. Verwijder de oude waarde
3. Klik op het **"+" icoon** om velden te kiezen
4. Selecteer **"1. JotForm"** uit de dropdown
5. Zoek het veld: **"Upload Jobdigger PDF"** of **"q9_uploadJobdigger"**
6. Klik erop om te mappen

---

#### **Stap 3: Extract Text from LinkedIn PDF**

**GOED ✅:**
```
PDF File: {{1. Upload LinkedIn Talent Insights PDF (optioneel)}}
   of
PDF File: {{1. q11_uploadLinkedin}}
```

---

#### **Stap 4: Extract Text from Vacature PDF**

**GOED ✅:**
```
PDF File: {{1. Upload vacature (optioneel)}}
   of
PDF File: {{1. q13_uploadVacature}}
```

---

#### **Stap 5: Python Code - KRITIEK!**

Dit is waarschijnlijk waar het misgaat! Check ALLE input velden:

**Input Data Mapping:**

```python
claude_api_key: [JE CLAUDE API KEY]

# ✅ GEBRUIK DYNAMISCHE VELDEN, NIET HARDCODED!
functietitel: {{1. Functietitel}}  # of {{1. q3_functietitel}}
locatieRegio: {{1. Locatie/Regio}}  # of {{1. q5_locatieregio}}
emailVoorRapportage: {{1. E-mail voor Rapportage}}  # of {{1. q7_emailVoor}}

# OPTIONELE PDF TEKST (alleen als stap bestaat)
jobdigger_extracted_text: {{2. Output Text}}  # Output van Stap 2
linkedin_extracted_text: {{3. Output Text}}   # Output van Stap 3
vacature_extracted_text: {{4. Output Text}}    # Output van Stap 4

# OPTIONELE TEKST VELDEN
vacaturetekst: {{1. Vacaturetekst (optioneel)}}  # of {{1. q15_vacaturetekst}}
vacatureUrl: {{1. Vacature URL (optioneel)}}      # of {{1. q17_vacatureUrl}}
```

**⚠️ KRITIEKE FOUT:**
Als je hier **hardcoded test data** of **oude waardes** ziet, vervang dan ALLES met de dynamische velden hierboven!

---

### 🔄 Stap 3: Re-test de HELE Zap

**Nadat je alles hebt aangepast:**

1. **Sla de Zap op** (Save)
2. **Doe een NIEUWE test submission** via de website
3. **Klik "Test & Continue"** in elke stap
4. **Verificeer dat NIEUWE data wordt gebruikt**

**Hoe te checken:**
- In Stap 5 (Python), kijk naar de **Input Data**
- Je zou de **nieuwe functietitel, locatie, email** moeten zien die je net hebt ingevuld
- NIET de oude test data!

---

## 🎯 Veelvoorkomende Fouten

### ❌ Fout 1: Oude Test Data Hardcoded
```python
# FOUT:
functietitel: "Test Functie"  # Dit is hardcoded!
```

```python
# GOED:
functietitel: {{1. Functietitel}}  # Dynamisch veld!
```

---

### ❌ Fout 2: Verkeerde Stap Nummer
```python
# FOUT:
jobdigger_extracted_text: {{1. Output Text}}  # Stap 1 is JotForm, niet PDF!
```

```python
# GOED:
jobdigger_extracted_text: {{2. Output Text}}  # Stap 2 is PDF extraction
```

---

### ❌ Fout 3: Filter Blokkeert Stap
Als stap 2, 3, of 4 een **Filter** heeft:

**Filter instellingen:**
```
Only continue if: Upload Jobdigger PDF (optioneel) exists
```

**Check dat:**
- De filter kijkt naar het **juiste veld** uit stap 1
- De conditie is: **"(Exists)"** of **"(is not empty)"**
- NIET: **"(Text) Exactly matches"** met een hardcoded waarde!

---

## 🧪 Test Scenario

**Stap-voor-stap test:**

1. **Vul formulier in op website:**
   - Functietitel: "DevOps Engineer"
   - Locatie: "Utrecht"
   - Email: "jouw@email.com"
   - Upload 1 PDF (test)

2. **Check Zapier Trigger:**
   - Open Zap → Stap 1
   - Klik "Test trigger"
   - Zie je de nieuwe data? ✅

3. **Check Stap 2 (PDF Extraction):**
   - Zie je de **nieuwe PDF URL** in het PDF File veld?
   - Test de stap - wordt er tekst geëxtraheerd?

4. **Check Stap 5 (Python):**
   - Open Input Data
   - Zie je **"DevOps Engineer"** en **"Utrecht"**?
   - Of zie je nog oude test data? ❌ → FIX MAPPING!

5. **Run volledige test:**
   - Klik "Test & Continue" door ALLE stappen
   - Check output van Python stap
   - Ontvang je email met het NIEUWE rapport?

---

## 📸 Visuele Guide - Hoe te Mappen

**In Zapier Python stap:**

```
┌─────────────────────────────────────────────┐
│ Input Data                                  │
├─────────────────────────────────────────────┤
│                                             │
│ functietitel                                │
│ ┌─────────────────────────────────────────┐ │
│ │ + Insert Data                     ▼    │ │ ← Klik hier!
│ └─────────────────────────────────────────┘ │
│                                             │
│ Dropdown opent:                             │
│ ┌─────────────────────────────────────────┐ │
│ │ 1. JotForm ▼                            │ │ ← Selecteer stap 1
│ │   - Functietitel                        │ │ ← Klik op dit veld!
│ │   - Locatie/Regio                       │ │
│ │   - E-mail voor Rapportage              │ │
│ │   - Upload Jobdigger PDF (optioneel)    │ │
│ │   ...                                   │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ Na selectie:                                │
│ ┌─────────────────────────────────────────┐ │
│ │ {{1. Functietitel}}                     │ │ ← Dit zou je moeten zien!
│ └─────────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
```

---

## ✅ Checklist - Is Mapping Correct?

Ga door ELKE stap en check:

**Stap 1: JotForm Trigger**
- [ ] Test trigger werkt
- [ ] Zie je de nieuwe submission data?
- [ ] Veldnamen zijn duidelijk (q3_, q5_, etc.)

**Stap 2: PDF Extract (Jobdigger)**
- [ ] PDF File veld = `{{1. Upload Jobdigger...}}`
- [ ] GEEN hardcoded URL!
- [ ] Filter ingesteld correct (if exists)

**Stap 3: PDF Extract (LinkedIn)**
- [ ] PDF File veld = `{{1. Upload LinkedIn...}}`
- [ ] Filter correct

**Stap 4: PDF Extract (Vacature)**
- [ ] PDF File veld = `{{1. Upload vacature...}}`
- [ ] Filter correct

**Stap 5: Python Code**
- [ ] `functietitel` = `{{1. Functietitel}}`
- [ ] `locatieRegio` = `{{1. Locatie/Regio}}`
- [ ] `emailVoorRapportage` = `{{1. E-mail...}}`
- [ ] `jobdigger_extracted_text` = `{{2. Output Text}}`
- [ ] `linkedin_extracted_text` = `{{3. Output Text}}`
- [ ] `vacature_extracted_text` = `{{4. Output Text}}`
- [ ] `vacaturetekst` = `{{1. Vacaturetekst...}}`
- [ ] `vacatureUrl` = `{{1. Vacature URL...}}`
- [ ] **GEEN hardcoded waardes!**

**Stap 6: Gmail**
- [ ] To = `{{5. recipient_email}}`
- [ ] Subject = `Arbeidsmarkt... {{5. functietitel}}`
- [ ] Body = `{{5. html_email}}`

---

## 🚨 CRITICAL: Zapier Caching

**Zapier cached soms oude test data!**

**Fix:**
1. In elke stap, klik **"Retest" of "Test & Continue"**
2. Dit haalt **nieuwe data** op
3. Update de veld mappings met de **nieuwe test data**
4. Sla op en test opnieuw

---

## 💡 Quick Fix Samenvatting

**Als stap 2 oude data gebruikt:**

1. ✅ Open Stap 1 → Test Trigger → Noteer veldnamen
2. ✅ Open Stap 2 → Check PDF File veld → Map naar Stap 1
3. ✅ Doe dit voor ALLE stappen
4. ✅ Let extra op Stap 5 (Python) Input Data
5. ✅ Sla op → Test HELE Zap → Nieuwe submission
6. ✅ Verificeer dat nieuwe data doorkomt

**Verwacht resultaat:**
- Email met rapport over de **nieuwe** functie die je invulde
- Niet meer oude test data!

---

## 📞 Hulp Nodig?

Als dit niet werkt, deel dan:
1. Screenshot van Stap 1 output (test trigger)
2. Screenshot van Stap 5 Input Data mapping
3. Welke stap gebruikt oude data?

Dan kan ik precies zien waar het misgaat! 🔍
