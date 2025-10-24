# NOTION DATABASE TEMPLATE
## Recruitment Intelligence Tracker

---

## 📋 STAP 1: Maak een Nieuwe Notion Database

1. Open Notion
2. Ga naar je workspace waar je de recruitment data wilt opslaan
3. Type `/database` en kies "Table - Inline"
4. Geef de database een naam: **"Recruitment Intelligence"**

---

## 🏗️ STAP 2: Voeg Deze Properties Toe

Klik op de "+" knop bovenaan de tabel om nieuwe properties toe te voegen:

### Basis Informatie
| Property Name | Type | Beschrijving |
|---------------|------|--------------|
| **Bedrijfsnaam** | Title | Naam van het bedrijf (auto title) |
| **Functietitel** | Text | Titel van de vacature |
| **Contactpersoon** | Text | Naam contactpersoon |
| **Email** | Email | Email adres |
| **Telefoon** | Phone | Telefoonnummer |
| **Status** | Select | Status van de aanvraag |
| **Datum** | Date | Datum van aanvraag |

### Vacature Details
| Property Name | Type | Beschrijving |
|---------------|------|--------------|
| **Sector** | Select | Sector/branche |
| **Locatie** | Text | Werklocatie |
| **Salaris Range** | Text | Salaris range (bijv. €60k-€80k) |
| **Urgentie** | Select | Urgentie niveau |
| **Intelligence Type** | Select | Type rapport |

### AI Analysis Results
| Property Name | Type | Beschrijving |
|---------------|------|--------------|
| **AI Schaarste** | Select | Schaarste niveau (Laag/Gemiddeld/Hoog) |
| **AI Time to Hire** | Text | Verwachte time to hire |

### Bronmateriaal URLs
| Property Name | Type | Beschrijving |
|---------------|------|--------------|
| **Vacature URL** | URL | Link naar originele vacature |
| **Jobdigger URL** | URL | Link naar Jobdigger PDF |
| **LinkedIn TI URL** | URL | Link naar LinkedIn Talent Insights PDF |

---

## ⚙️ STAP 3: Configureer Select Options

### Status Options
- 🤖 AI Analyse Compleet (groen)
- ⏳ In Verwerking (geel)
- ❌ Error (rood)

### Sector Options (voeg toe wat nodig is)
- IT & Technology
- Finance
- Healthcare
- Marketing & Sales
- HR & Recruitment
- Operations
- Engineering
- Algemeen

### Urgentie Options
- 🔥 Zeer Urgent
- ⚡ Urgent
- 📊 Normaal
- 📅 Geen haast

### Intelligence Type Options
- AI-Gedreven Rapport
- Demo Rapport
- Quick Summary

### AI Schaarste Options
- 🟢 Laag
- 🟡 Gemiddeld
- 🔴 Hoog

---

## 🔗 STAP 4: Zapier Notion Step Configuration

Open je Zapier workflow, ga naar **Step 7: Create Database Item in Notion**

### Action Event
- **App**: Notion
- **Action**: Create Database Item

### Database
- Selecteer: **Recruitment Intelligence** (de database die je net hebt gemaakt)

### Properties Mapping

```yaml
# Notion Title (Required)
Bedrijfsnaam: {{5. notion_bedrijfsnaam}}

# Basis Properties
Functietitel: {{5. notion_functietitel}}
Contactpersoon: {{5. notion_contactpersoon}}
Email: {{5. notion_email}}
Telefoon: {{5. notion_telefoon}}
Status: {{5. notion_status}}
Datum: {{5. notion_datum}}

# Vacature Details
Sector: {{5. notion_sector}}
Locatie: {{5. notion_locatie}}
Salaris Range: {{5. notion_salaris_range}}
Urgentie: {{5. notion_urgentie}}
Intelligence Type: {{5. notion_intelligence}}

# AI Analysis
AI Schaarste: {{5. notion_ai_schaarste}}
AI Time to Hire: {{5. notion_ai_time_to_hire}}

# URLs (BELANGRIJK: Gebruik de nieuwe fields!)
Vacature URL: {{5. notion_vacature_url}}
Jobdigger URL: {{5. notion_jobdigger_url}}
LinkedIn TI URL: {{5. notion_linkedin_ti_url}}
```

---

## 📄 OPTIONEEL: Page Content Blocks

Als je ook page content wilt toevoegen (zoals een samenvatting in de Notion page zelf), voeg dan **Page Content Blocks** toe:

### Block 1: Header
- **Type**: Heading 1
- **Content**: `Recruitment Intelligence Report`

### Block 2: Company Info
- **Type**: Paragraph
- **Content**:
```
Bedrijf: {{5. notion_bedrijfsnaam}}
Functie: {{5. notion_functietitel}}
Locatie: {{5. notion_locatie}}
Sector: {{5. notion_sector}}
```

### Block 3: AI Insights Header
- **Type**: Heading 2
- **Content**: `AI Analysis`

### Block 4: AI Results
- **Type**: Paragraph
- **Content**:
```
Schaarste: {{5. notion_ai_schaarste}}
Time to Hire: {{5. notion_ai_time_to_hire}}
Status: {{5. notion_status}}
```

### Block 5: Bronmateriaal Header
- **Type**: Heading 2
- **Content**: `Bronmateriaal`

### Block 6: Vacature Link (CONDITIONAL)
- **Type**: Bulleted List Item
- **Content**: `Originele Vacature`
- **Filter**: Only continue if `{{5. notion_vacature_url}}` exists
- **Als je een hyperlink wilt in de text**:
  - Content: `[Originele Vacature]({{5. notion_vacature_url}})`

### Block 7: Jobdigger Link (CONDITIONAL)
- **Type**: Bulleted List Item
- **Content**: `Jobdigger Marktrapport`
- **Filter**: Only continue if `{{5. notion_jobdigger_url}}` exists

### Block 8: LinkedIn TI Link (CONDITIONAL)
- **Type**: Bulleted List Item
- **Content**: `LinkedIn Talent Insights`
- **Filter**: Only continue if `{{5. notion_linkedin_ti_url}}` exists

---

## ✅ STAP 5: Test de Zapier Workflow

1. Klik op **Test & Continue** in Zapier Step 7
2. Controleer of de data correct in Notion verschijnt
3. Check dat lege URLs geen error geven (ze worden gewoon overgeslagen)

---

## 🎨 BONUS: Notion Views

Maak handige views in je Notion database:

### View 1: "Open Reports"
- **Type**: Table
- **Filter**: Status = "🤖 AI Analyse Compleet"
- **Sort**: Datum (newest first)

### View 2: "By Urgentie"
- **Type**: Board (Kanban)
- **Group by**: Urgentie
- **Sort**: Datum

### View 3: "By Sector"
- **Type**: Gallery
- **Group by**: Sector
- **Properties to show**: Functietitel, Bedrijfsnaam, AI Schaarste

---

## 🔧 Troubleshooting

### "URL should be populated" Error
- ✅ **OPGELOST**: De nieuwe code gebruikt `None` in plaats van `""`
- Update je Zapier Code step naar de nieuwe `zapier-ai-rapport-clean.py` versie
- URLs die leeg zijn worden automatisch overgeslagen

### Links werken niet in Page Content
- Gebruik het URL property type in plaats van blocks
- Of gebruik conditional filters: "Only add if field exists"

### Select options niet beschikbaar
- Zorg dat je eerst de Select options hebt aangemaakt in Notion
- De naam moet EXACT overeenkomen (hoofdlettergevoelig)

---

## 📊 Voorbeeld Output

Na een succesvolle run zie je in Notion:

```
Bedrijfsnaam: TechCorp BV
Functietitel: Senior Python Developer
Status: 🤖 AI Analyse Compleet
Sector: IT & Technology
Locatie: Amsterdam
AI Schaarste: 🔴 Hoog
AI Time to Hire: 35-45 dagen
Datum: 24-10-2025

Links:
🔗 Vacature URL → https://techcorp.nl/vacature/123
📄 Jobdigger URL → https://drive.google.com/file/d/abc123
📊 LinkedIn TI URL → https://drive.google.com/file/d/xyz789
```

---

Klaar! Je Notion database is nu volledig geconfigureerd om AI-gedreven recruitment intelligence reports op te slaan.
