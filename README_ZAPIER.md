# 🔄 Pipedrive Zapier Integration - Overzicht

## 📁 Welk Bestand Moet Ik Gebruiken?

### Voor Snelle Setup (AANBEVOLEN):
✅ **`ZAPIER_QUICK_START.txt`** - Open dit bestand en kopieer/plak in Zapier
   - Simpel format, direct te kopiëren
   - Alle settings op 1 pagina
   - Perfect voor beginners

### Voor Gedetailleerde Instructies:
📖 **`ZAPIER_FLOW_CONFIG.md`** - Complete gids met uitleg
   - Stap-voor-stap screenshots beschrijving
   - Field mappings met uitleg
   - Google Sheets formatting tips
   - Troubleshooting sectie

### Voor Technische Referentie:
🔧 **`zapier_config.json`** - Gestructureerde configuratie
   - JSON formaat
   - Alle instellingen gedocumenteerd
   - Voor developers / API gebruik

### Voor Algemene Context:
📚 **`ZAPIER_SETUP.md`** - Originele setup guide
   - Achtergrond informatie
   - Waarom deze workaround
   - Volledige context

---

## 🚀 Quick Start (5 Minuten)

1. **Open:** `ZAPIER_QUICK_START.txt`
2. **Volg de 3 stappen:**
   - Step 1: Schedule trigger
   - Step 2: Pipedrive action
   - Step 3: Google Sheets action
3. **Test & Publish**
4. **Klaar!** ✅

---

## 📊 Alle Bestanden Overzicht

| Bestand | Doel | Voor Wie |
|---------|------|----------|
| `ZAPIER_QUICK_START.txt` | ⚡ Snelle setup | Iedereen - **start hier** |
| `ZAPIER_FLOW_CONFIG.md` | 📖 Gedetailleerde gids | Eerste keer Zapier gebruiken |
| `ZAPIER_SETUP.md` | 📚 Complete context | Wil alles begrijpen |
| `zapier_config.json` | 🔧 Technische config | Developers / API |
| `pipedrive_zapier_workaround.py` | 🐍 Python script | Na Zapier setup |
| `pipedrive_jobdigger_status.py` | ⏸️ Directe API | Later (als API werkt) |

---

## 🎯 Workflow

```
┌─────────────┐
│   Zapier    │  ← Start hier: ZAPIER_QUICK_START.txt
└──────┬──────┘
       │ Daily at 09:00
       ↓
┌─────────────┐
│  Pipedrive  │  ← Haalt deals op (OAuth - werkt!)
└──────┬──────┘
       │
       ↓
┌─────────────┐
│Google Sheets│  ← Slaat data op
└──────┬──────┘
       │
       ↓ Download CSV
┌─────────────┐
│   Python    │  ← pipedrive_zapier_workaround.py
└─────────────┘
       │
       ↓
   📊 Rapport
```

---

## ❓ Welke Heb Ik Nodig?

### Als je wilt beginnen:
→ Open **`ZAPIER_QUICK_START.txt`**

### Als je vast loopt:
→ Lees **`ZAPIER_FLOW_CONFIG.md`**

### Als je wilt begrijpen waarom:
→ Lees **`ZAPIER_SETUP.md`**

### Als je technische details wilt:
→ Bekijk **`zapier_config.json`**

---

## 🎓 Meer Hulp Nodig?

- **Zapier documentatie:** https://zapier.com/help
- **Pipedrive velden:** Zie `zapier_config.json` → "pipedrive_fields_reference"
- **Google Sheets setup:** Zie `ZAPIER_FLOW_CONFIG.md` → sectie "Google Sheets Setup"
- **Python script:** Run `python pipedrive_zapier_workaround.py` na CSV download

---

**© 2025 WouterArts Recruitin - Labour Market Intelligence**
