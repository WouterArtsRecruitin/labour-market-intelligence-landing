# 🤖 CLAUDE AI ANALYSE - Hoe JotForm Data Wordt Verwerkt

## 📊 Overzicht Proces

```
JotForm Submission (Website)
        ↓
Zapier Trigger (Stap 1)
        ↓
PDF Text Extractie (Stap 2-4)
        ↓
Claude AI Analyse (Stap 5)
        ↓
Email Rapport (Stap 6)
```

---

## 🔍 STAP 5: Claude AI Analyse (Python Code)

### **Input Data die Claude AI Ontvangt:**

```python
# VEREIST (van JotForm formulier):
functietitel: "Senior Data Engineer"
locatie: "Amsterdam, Noord-Holland"
email: "klant@bedrijf.nl"

# OPTIONEEL (geëxtraheerde PDF tekst):
jobdigger_text: "[Volledige tekst uit Jobdigger PDF]"
linkedin_ti_text: "[Volledige tekst uit LinkedIn Talent Insights PDF]"
vacature_pdf_text: "[Volledige tekst uit vacature PDF]"

# OPTIONEEL (rechtstreeks ingevoerd):
vacaturetekst: "We zoeken een senior data engineer..."
vacatureUrl: "https://example.com/vacature"
```

---

## 🧠 CLAUDE AI PROMPT (Wat AI Krijgt)

### **Volledige Prompt Template:**

```
Analyseer deze arbeidsmarkt documenten en genereer JSON output.

## VACATURETEKST:
[Hier komt de vacaturetekst of PDF inhoud]

## JOBDIGGER RAPPORT:
[Hier komt de geëxtraheerde Jobdigger data]

## LINKEDIN TALENT INSIGHTS:
[Hier komt de LinkedIn TI data]

VACATURE: Senior Data Engineer | LOCATIE: Amsterdam, Noord-Holland

Geef JSON response (gebruik realistische data uit documenten):

{
  "schaarste_niveau": "Laag/Gemiddeld/Hoog",
  "schaarste_ratio": "X,X vacatures per kandidaat",
  "time_to_hire_min": 30,
  "time_to_hire_max": 50,
  "beschikbaarheid": "±X.XXX",
  "beschikbaarheid_tekst": "Geschikte kandidaten NL",
  "werkzoekend_ratio": {
    "actief": 15,
    "latent": 45,
    "niet_werkzoekend": 40
  },
  "leeftijd_verdeling": [
    {"leeftijd": "20-30 jaar", "percentage": 25},
    {"leeftijd": "30-40 jaar", "percentage": 35},
    {"leeftijd": "40-50 jaar", "percentage": 28},
    {"leeftijd": "50+ jaar", "percentage": 12}
  ],
  "push_factors": [
    "Factor 1",
    "Factor 2",
    "Factor 3"
  ],
  "pull_factors": [
    "Factor 1",
    "Factor 2",
    "Factor 3"
  ],
  "technische_skills": [
    {"skill": "Skill 1", "niveau": "Essential"},
    {"skill": "Skill 2", "niveau": "Nice to have"},
    {"skill": "Skill 3", "niveau": "Essential"}
  ],
  "soft_skills": [
    "Soft skill 1",
    "Soft skill 2",
    "Soft skill 3"
  ],
  "salaris_p25_min": 50000,
  "salaris_p25_max": 60000,
  "salaris_p50_min": 65000,
  "salaris_p50_max": 75000,
  "salaris_p75_min": 75000,
  "salaris_p75_max": 90000,
  "total_workers_market": "25.000",
  "growth_percentage": 3.2,
  "open_vacancies": "1.150",
  "contract_permanent": 72,
  "contract_temporary": 18,
  "contract_freelance": 10,
  "average_age": 41,
  "gender_ratio": "68/32",
  "employment_trend": "Stijgend",
  "talent_pool_size": "14.500",
  "active_job_seekers": "2.100",
  "hiring_velocity": "820/maand",
  "hiring_speed": "Snel",
  "education_wo": 43,
  "education_hbo": 42,
  "education_mbo": 15,
  "mobility_index": "Hoog",
  "avg_retention": "3.2 jaar",
  "skill_gaps": "Specialistische kennis, Nieuwe technologieën"
}

Geen extra tekst, alleen JSON.
```

---

## 📋 Wat Claude AI Doet

### **Analyse Stappen:**

1. **Leest alle documenten:**
   - Vacaturetekst (max 5.000 karakters)
   - Jobdigger rapport (max 5.000 karakters)
   - LinkedIn Talent Insights (max 5.000 karakters)

2. **Extraheert relevante data:**
   - Schaarste niveau in de markt
   - Salaris ranges
   - Vereiste skills (technisch + soft)
   - Demografische data
   - Time-to-hire prognoses
   - Push/pull factoren

3. **Genereert JSON output:**
   - Gestructureerde data voor rapport
   - Realistische cijfers gebaseerd op documenten
   - Fallback data als documenten ontbreken

4. **Gebruikt Claude Sonnet 4.5 model:**
   - Model: `claude-sonnet-4-5-20250929`
   - Max tokens: 4096
   - Response tijd: ~10-15 seconden

---

## 🔢 Output Data Structuur

### **JSON Response van Claude AI:**

```json
{
  // SCHAARSTE ANALYSE
  "schaarste_niveau": "Hoog",
  "schaarste_ratio": "3,8 vacatures per kandidaat",

  // TIME TO HIRE
  "time_to_hire_min": 45,
  "time_to_hire_max": 65,

  // BESCHIKBAARHEID
  "beschikbaarheid": "±8.500",
  "beschikbaarheid_tekst": "Geschikte kandidaten NL",

  // WERKZOEKEND GEDRAG
  "werkzoekend_ratio": {
    "actief": 12,
    "latent": 43,
    "niet_werkzoekend": 45
  },

  // DEMOGRAFIE
  "leeftijd_verdeling": [
    {"leeftijd": "20-30 jaar", "percentage": 28},
    {"leeftijd": "30-40 jaar", "percentage": 42},
    {"leeftijd": "40-50 jaar", "percentage": 22},
    {"leeftijd": "50+ jaar", "percentage": 8}
  ],

  // MOTIVATIE FACTOREN
  "push_factors": [
    "Gebrek aan innovatie",
    "Beperkte ontwikkelmogelijkheden",
    "Onvoldoende werk-privé balans"
  ],
  "pull_factors": [
    "Moderne tech stack",
    "Remote werken mogelijk",
    "Competitief salaris"
  ],

  // SKILLS VEREIST
  "technische_skills": [
    {"skill": "Python/Spark", "niveau": "Essential"},
    {"skill": "Cloud platforms (AWS/Azure)", "niveau": "Essential"},
    {"skill": "Machine Learning", "niveau": "Nice to have"}
  ],
  "soft_skills": [
    "Analytisch denkvermogen",
    "Communicatievaardigheden",
    "Zelfstandig werken"
  ],

  // SALARIS RANGES
  "salaris_p25_min": 60000,
  "salaris_p25_max": 70000,
  "salaris_p50_min": 75000,
  "salaris_p50_max": 85000,
  "salaris_p75_min": 90000,
  "salaris_p75_max": 110000,

  // MARKT STATISTIEKEN
  "total_workers_market": "18.500",
  "growth_percentage": 4.5,
  "open_vacancies": "1.850",
  "contract_permanent": 68,
  "contract_temporary": 22,
  "contract_freelance": 10,
  "average_age": 38,
  "gender_ratio": "72/28",
  "employment_trend": "Sterk stijgend",
  "talent_pool_size": "11.200",
  "active_job_seekers": "1.680",
  "hiring_velocity": "1.250/maand",
  "hiring_speed": "Gemiddeld",

  // OPLEIDING
  "education_wo": 52,
  "education_hbo": 38,
  "education_mbo": 10,

  // MOBILITEIT & RETENTIE
  "mobility_index": "Zeer hoog",
  "avg_retention": "2.8 jaar",
  "skill_gaps": "Advanced ML, Real-time data processing"
}
```

---

## 🎯 Hoe Claude AI de Documenten Analyseert

### **Voorbeeld Analyse:**

**Input:** Jobdigger PDF met:
```
Data Engineer - Amsterdam
Vacatures: 1.850
Kandidaten: 487
Ratio: 3,8:1
Gemiddeld salaris: €75.000 - €85.000
```

**Claude AI Output:**
```json
{
  "schaarste_niveau": "Hoog",
  "schaarste_ratio": "3,8 vacatures per kandidaat",
  "salaris_p50_min": 75000,
  "salaris_p50_max": 85000,
  "open_vacancies": "1.850",
  "talent_pool_size": "487"
}
```

### **Intelligente Interpretatie:**

Claude AI:
- ✅ Herkent cijfers en trends
- ✅ Vertaalt naar begrijpelijke metrics
- ✅ Vult ontbrekende data aan met realistische schattingen
- ✅ Past data aan op locatie (Amsterdam vs Nederland)
- ✅ Gebruikt context uit alle documenten

---

## 🛡️ Fallback Data

**Als Claude AI faalt of geen PDFs zijn geüpload:**

De code gebruikt **fallback data** om toch een rapport te genereren:

```python
fallback_data = {
    "schaarste_niveau": "Gemiddeld",
    "schaarste_ratio": "2,5 vacatures per kandidaat",
    "time_to_hire_min": 35,
    "time_to_hire_max": 55,
    # ... etc (generieke marktdata)
}
```

**Waarom?**
- Gebruiker krijgt ALTIJD een rapport
- Beter generieke data dan geen rapport
- Kan later worden vervangen door echte data

---

## 📧 Rapport Generatie

**Na Claude AI analyse:**

```python
# JSON data wordt omgezet naar HTML email
html_email = generate_html_email(
    functietitel=functietitel,
    locatie=locatie,
    data=claude_output  # of fallback_data
)

# Verzonden via Gmail (Stap 6)
recipient_email = email
subject = f"Arbeidsmarkt Intelligence Rapport - {functietitel}"
```

---

## 💡 Tips voor Betere Analyse

### **Optimale Input voor Claude AI:**

1. **Upload Jobdigger PDF** met:
   - Vacature aantallen
   - Kandidaat aantallen
   - Salaris ranges
   - Trends

2. **Upload LinkedIn Talent Insights** met:
   - Demografie data
   - Skills data
   - Mobility indices

3. **Upload/type Vacaturetekst** met:
   - Vereiste skills
   - Salaris indicatie
   - Ervaring niveau

**Hoe meer data → Hoe beter de analyse!**

---

## 🔧 Technical Details

**API Call:**
```python
POST https://api.anthropic.com/v1/messages
Headers:
  x-api-key: [YOUR_CLAUDE_API_KEY]
  anthropic-version: 2023-06-01
  content-type: application/json

Body:
{
  "model": "claude-sonnet-4-5-20250929",
  "max_tokens": 4096,
  "messages": [{
    "role": "user",
    "content": "[FULL PROMPT WITH DOCUMENTS]"
  }]
}
```

**Response Time:** ~10-15 seconden
**Cost:** ~$0.01 per rapport (zeer goedkoop!)

---

## 📊 Data Flow Diagram

```
┌─────────────────────────────────────────────────┐
│ JOTFORM SUBMISSION (Website)                    │
│ - Functietitel: "Data Engineer"                 │
│ - Locatie: "Amsterdam"                          │
│ - Email: "klant@bedrijf.nl"                     │
│ - PDFs: Jobdigger, LinkedIn TI                  │
└────────────────┬────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────────────┐
│ ZAPIER STEP 2-4: PDF TEXT EXTRACTION           │
│ - Jobdigger PDF → tekst                         │
│ - LinkedIn TI PDF → tekst                       │
│ - Vacature PDF → tekst                          │
└────────────────┬────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────────────┐
│ ZAPIER STEP 5: CLAUDE AI ANALYSIS              │
│                                                  │
│ Input:                                          │
│ • Functietitel + Locatie                       │
│ • Alle PDF teksten (max 15.000 chars)         │
│                                                  │
│ Prompt:                                         │
│ "Analyseer documenten, genereer JSON"          │
│                                                  │
│ Claude AI Verwerkt:                            │
│ • Extraheert cijfers en trends                 │
│ • Identificeert skills                         │
│ • Bepaalt schaarste niveau                    │
│ • Berekent salaris ranges                     │
│ • Voorspelt time-to-hire                      │
│                                                  │
│ Output: Gestructureerde JSON (30+ velden)      │
└────────────────┬────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────────────┐
│ PYTHON CODE: HTML EMAIL GENERATION             │
│ - JSON → HTML template                          │
│ - Grafieken en tabellen                        │
│ - Professional styling                          │
└────────────────┬────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────────────┐
│ ZAPIER STEP 6: GMAIL SEND EMAIL                │
│ To: klant@bedrijf.nl                           │
│ Subject: "Arbeidsmarkt Rapport - Data Engineer"│
│ Body: [Volledig HTML rapport]                  │
└─────────────────────────────────────────────────┘
```

---

## ✅ Samenvatting

**Claude AI:**
- Leest max 15.000 karakters aan documenten
- Analyseert met Sonnet 4.5 model
- Genereert 30+ data punten
- Output in 10-15 seconden
- Kost ~€0.01 per rapport

**Output gebruikt voor:**
- HTML email rapport
- Grafieken (salaris, demografie)
- Aanbevelingen en inzichten
- Time-to-hire prognoses

**Fallback:** Als AI faalt → Gebruik generieke marktdata

**Resultaat:** Professioneel arbeidsmarkt intelligence rapport in klant's inbox binnen 2 minuten!
