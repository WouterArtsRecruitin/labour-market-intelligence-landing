# Pipedrive + Zapier Workaround Setup

Deze guide helpt je om Pipedrive deal data op te halen via Zapier (omdat directe API toegang geblokkeerd is).

## 🎯 Wat We Gaan Doen

1. Zapier verbinden met Pipedrive (dit werkt al bij jou!)
2. Een Zap maken die dagelijks deals ophaalt
3. Data naar Google Sheets sturen
4. Python script gebruiken om data te lezen en tonen

## 📋 Benodigdheden

- ✅ Pipedrive account (heb je)
- ✅ Zapier account (heb je - is al connected)
- 📝 Google account (voor Google Sheets)
- 🐍 Python 3.x

---

## 🚀 Stap 1: Maak een Nieuwe Zap

### 1.1 Ga naar Zapier
- Log in op https://zapier.com
- Klik **"Create Zap"**

### 1.2 Stel de Trigger In

**Trigger:**
- Zoek en selecteer: **"Schedule by Zapier"**
- Event: **"Every Day"**
- Kies tijd: bijvoorbeeld **09:00** (wanneer je de update wilt)
- Klik **"Continue"**

### 1.3 Test de Trigger
- Klik **"Test trigger"**
- Je zou een test resultaat moeten zien
- Klik **"Continue"**

---

## 🔍 Stap 2: Pipedrive Deals Ophalen

### 2.1 Voeg Actie Toe
- Klik **"+"** om een actie toe te voegen
- Zoek en selecteer: **"Pipedrive"**

### 2.2 Kies Event
- Event: **"Find Deal"** of **"Find Many Deals"**
- Klik **"Continue"**

### 2.3 Verbind Pipedrive
- Zapier vraagt om in te loggen bij Pipedrive
- ✅ Dit zou moeten werken (OAuth toegang)
- Klik **"Continue"**

### 2.4 Configureer de Search
- **Search by:** Laat leeg of kies filter (bijv. status = "open")
- **Limit:** 100 (of hoeveel je wilt)
- Klik **"Continue"**

### 2.5 Test de Actie
- Klik **"Test action"**
- Je zou Pipedrive deals moeten zien! ✅
- Klik **"Continue"**

---

## 📊 Stap 3: Data naar Google Sheets Sturen

### 3.1 Voeg Nog Een Actie Toe
- Klik **"+"** om een actie toe te voegen
- Zoek en selecteer: **"Google Sheets"**

### 3.2 Kies Event
- Event: **"Create Spreadsheet Row"** of **"Update Spreadsheet Row"**
- Klik **"Continue"**

### 3.3 Verbind Google Sheets
- Log in met je Google account
- Geef Zapier toegang
- Klik **"Continue"**

### 3.4 Maak een Google Sheet

**In een nieuw tabblad:**
1. Ga naar https://sheets.google.com
2. Maak een nieuw sheet genaamd: **"Pipedrive Deals"**
3. Voeg deze kolommen toe in rij 1:

| A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|
| Title | Status | Value | Person | Organization | Stage | Created | Updated |

### 3.5 Configureer Google Sheets in Zapier

- **Spreadsheet:** Selecteer "Pipedrive Deals"
- **Worksheet:** Sheet1
- **Map de velden:**
  - **Title** → Pipedrive: Deal Title
  - **Status** → Pipedrive: Status
  - **Value** → Pipedrive: Value
  - **Person** → Pipedrive: Person Name
  - **Organization** → Pipedrive: Organization Name
  - **Stage** → Pipedrive: Stage ID
  - **Created** → Pipedrive: Add Time
  - **Updated** → Pipedrive: Update Time

### 3.6 Test de Actie
- Klik **"Test action"**
- Check je Google Sheet - er zou een rij moeten zijn toegevoegd! ✅

### 3.7 Publish de Zap
- Geef je Zap een naam: **"Pipedrive Deals to Google Sheets"**
- Klik **"Publish"**
- Zet de Zap **ON** (toggle switch)

---

## 🐍 Stap 4: Python Script Gebruiken

### 4.1 Download de Data als CSV

1. Ga naar je Google Sheet: **"Pipedrive Deals"**
2. **File → Download → Comma Separated Values (.csv)**
3. Sla op als: **`pipedrive_deals.csv`**
4. Plaats in de map: `/home/user/labour-market-intelligence-landing/`

### 4.2 Run het Script

```bash
cd /home/user/labour-market-intelligence-landing
python pipedrive_zapier_workaround.py
```

### 4.3 Verwacht Resultaat

Je zou moeten zien:
```
====================================================================================================
                                   PIPEDRIVE DEALS (VIA ZAPIER)
====================================================================================================

Total Deals: 15

1. Labour Market Analysis - Tech Sector
   Status: open | Value: €59.00
   Contact: John Doe | Organization: Tech Corp
   ------------------------------------------------------------------------------------------------

====================================================================================================
                                            SUMMARY
====================================================================================================

Total Deals:     15
Open Deals:      8
Won Deals:       5
Lost Deals:      2
Total Value:     €885.00
```

---

## 🔄 Dagelijkse Updates

De Zap draait nu **automatisch elke dag** op de tijd die je hebt ingesteld.

**Om de nieuwste data te zien:**
1. Download opnieuw de CSV van Google Sheets
2. Run het Python script

---

## 🎨 Bonus: Automatische CSV Download (Optioneel)

Als je de Google Sheets API wilt gebruiken voor automatische sync:

### Installeer Dependencies
```bash
pip install gspread oauth2client
```

### Volg Google Sheets API Setup
1. Ga naar: https://console.cloud.google.com
2. Maak een project
3. Enable Google Sheets API
4. Create Service Account credentials
5. Download JSON credentials
6. Share je Google Sheet met de service account email

Dan kan het script direct van Google Sheets lezen zonder CSV download!

---

## ❓ Troubleshooting

### Zap werkt niet
- Check of Pipedrive connectie nog actief is in Zapier
- Test elke stap individueel

### Geen data in Google Sheets
- Check of de Zap ON staat
- Run de Zap handmatig: "Test & Review" → "Test step"

### Python script vindt CSV niet
- Check of bestand heet: `pipedrive_deals.csv`
- Check of het in de juiste map staat
- Run: `ls -la pipedrive_deals.csv`

---

## 🎯 Volgende Stappen

Zodra je directe API toegang krijgt (via de andere admin of Pipedrive support):
1. Je kunt overschakelen naar `pipedrive_jobdigger_status.py`
2. Zapier kan uitgeschakeld worden (of blijven draaien als backup)

---

**© 2025 WouterArts Recruitin - Labour Market Intelligence**
