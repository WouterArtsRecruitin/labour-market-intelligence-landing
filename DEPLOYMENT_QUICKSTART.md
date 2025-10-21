# 🚀 Quick Deployment Guide - Labour Market Intelligence

## Stap-voor-stap deployment naar productie in 10 minuten!

---

## ✅ Prerequisites

Voordat je begint, zorg dat je hebt:
- [ ] GitHub account (je hebt dit al!)
- [ ] Anthropic API key → [Get one here](https://console.anthropic.com/)
- [ ] Render.com account → [Sign up here](https://render.com) (gratis)
- [ ] (Optioneel) Gmail account voor email rapporten

---

## 📝 Stap 1: Get Anthropic API Key (2 minuten)

1. Ga naar **https://console.anthropic.com/**
2. Log in of maak account aan
3. Klik op **"API Keys"** in het menu
4. Klik **"Create Key"**
5. Geef een naam: `labour-market-intelligence`
6. **Kopieer de key** (begint met `sk-ant-api03-...`)
7. ⚠️ **Bewaar deze key veilig** - je kan hem maar 1x zien!

**Kosten:** ~$0.10 per rapport (6,000-8,000 tokens)

---

## 🚀 Stap 2: Deploy Backend naar Render (5 minuten)

### Optie A: Via Render Dashboard (Makkelijkst)

1. **Ga naar [Render Dashboard](https://dashboard.render.com/)**
   - Log in of sign up (gratis met GitHub)

2. **Create New Web Service**
   - Klik **"New +"** → **"Web Service"**

3. **Connect GitHub Repository**
   - Click **"Connect a repository"**
   - Authorize Render om toegang te krijgen tot je GitHub
   - Selecteer: **`WouterArtsRecruitin/labour-market-intelligence-landing`**

4. **Configure Service**
   Vul in:
   ```
   Name: labour-market-intelligence-api
   Region: Frankfurt (EU Central)
   Branch: claude/analyze-data-011CULWAqM1avorwNM2vKva9
   Root Directory: api
   Runtime: Node
   Build Command: npm install
   Start Command: npm start
   ```

5. **Select Plan**
   - Kies **"Free"** (voor testing)
   - ⚠️ Free tier: server slaapt na 15 min inactiviteit
   - Upgrade later naar **$7/maand** voor 24/7 uptime

6. **Add Environment Variables**
   Scroll naar beneden naar "Environment Variables" en klik **"Add Environment Variable"**

   Voeg deze toe (klik "Add" na elke):

   **VERPLICHT:**
   ```
   Key: ANTHROPIC_API_KEY
   Value: [plak je API key hier]
   ```

   ```
   Key: NODE_ENV
   Value: production
   ```

   ```
   Key: ALLOWED_ORIGINS
   Value: https://labour-market-intelligence.netlify.app
   ```

   **OPTIONEEL (voor email rapporten):**
   ```
   Key: EMAIL_USER
   Value: jouw.email@gmail.com
   ```

   ```
   Key: EMAIL_PASSWORD
   Value: [je Gmail app password]
   ```

   > **Gmail App Password:** Ga naar [Google App Passwords](https://myaccount.google.com/apppasswords), enable 2FA, genereer app password

7. **Create Web Service**
   - Klik onderaan **"Create Web Service"**
   - ⏳ Render zal nu je app deployen (duurt ~2-3 minuten)
   - ✅ Wacht tot je **"Live"** ziet met een groene dot

8. **Kopieer je API URL**
   - Je krijgt een URL zoals: `https://labour-market-intelligence-api.onrender.com`
   - **⭐ Kopieer deze URL** - je hebt hem straks nodig!

### Optie B: Via Render Blueprint (Sneller)

Als je `render.yaml` al hebt gepusht naar GitHub:

1. Ga naar [Render Dashboard](https://dashboard.render.com/)
2. Click **"New +"** → **"Blueprint"**
3. Selecteer je repository
4. Render detecteert automatisch `render.yaml`
5. Vul alleen de secrets in:
   - `ANTHROPIC_API_KEY`
   - `EMAIL_USER` (optioneel)
   - `EMAIL_PASSWORD` (optioneel)
6. Click **"Apply"**

---

## 🌐 Stap 3: Test Backend API (1 minuut)

Test of je backend draait:

**Open in browser:**
```
https://your-api-url.onrender.com/api/status
```

Je zou moeten zien:
```json
{
  "status": "ok",
  "message": "Labour Market Intelligence API is running",
  "timestamp": "2025-10-21T..."
}
```

**Test health check:**
```
https://your-api-url.onrender.com/api/health
```

✅ Als beide werken, je backend is LIVE! 🎉

---

## 🔧 Stap 4: Update Frontend (2 minuten)

Nu moeten we de frontend vertellen waar de backend is.

**Ik ga dit voor je doen**, maar onthoud je API URL!

Je API URL is waarschijnlijk:
```
https://labour-market-intelligence-api.onrender.com
```

---

## 🧪 Stap 5: Test Complete Flow (3 minuten)

1. **Ga naar je website:**
   ```
   https://labour-market-intelligence.netlify.app
   ```

2. **Scroll naar "Analyseer Je Arbeidsmarkt"**

3. **Vul het formulier in:**
   - Email: `jouw@email.com`
   - Bedrijf: `Test BV`
   - Functie: `Marketing Manager`
   - Sector: `Technology`
   - Locatie: `Amsterdam`
   - Ervaring: `Senior`
   - Skills: `Marketing, SEO, Leadership`

4. **Klik "Genereer Arbeidsmarkt Rapport"**

5. **Wacht 8-12 seconden** (Claude AI genereert rapport)

6. **Check:**
   - ✅ Success melding verschijnt
   - ✅ Email ontvangen (als email geconfigureerd)
   - ✅ Rapport is in Markdown formaat

---

## 🎯 Troubleshooting

### ❌ "Failed to generate report"

**Probleem:** API key niet correct geconfigureerd

**Oplossing:**
1. Ga naar [Render Dashboard](https://dashboard.render.com/)
2. Click op je service
3. Ga naar "Environment"
4. Check of `ANTHROPIC_API_KEY` correct is
5. Click "Manual Deploy" → "Clear build cache & deploy"

### ❌ CORS Error in browser console

**Probleem:** Frontend URL niet toegestaan

**Oplossing:**
1. Ga naar Render Dashboard → Environment
2. Update `ALLOWED_ORIGINS`:
   ```
   https://labour-market-intelligence.netlify.app,http://localhost:3000
   ```
3. Manual Deploy

### ❌ 504 Gateway Timeout

**Probleem:** Free tier heeft cold starts (eerste request duurt langer)

**Oplossing:**
- Wacht 30 seconden en probeer opnieuw
- Of: upgrade naar $7/maand plan (geen cold starts)

### ❌ Email niet ontvangen

**Probleem:** Email credentials niet geconfigureerd

**Check:**
1. Render Dashboard → Environment
2. Check `EMAIL_USER` en `EMAIL_PASSWORD`
3. Voor Gmail: gebruik App Password, niet normaal wachtwoord

---

## 💰 Kosten Overzicht

### Backend Hosting (Render):
- **Free Tier:** €0/maand
  - ✅ 750 uur/maand
  - ⚠️ Cold starts na 15 min inactiviteit
  - ⚠️ Eerste request duurt ~30 sec

- **Starter Plan:** $7/maand (~€6.50)
  - ✅ Altijd actief (no cold starts)
  - ✅ Snellere respons
  - ✅ 512MB RAM

### Claude AI API:
- **Per rapport:** ~$0.10
- **100 rapporten/maand:** ~$10
- **1000 rapporten/maand:** ~$100

Anthropic heeft gratis credits voor nieuwe accounts!

### Frontend Hosting (Netlify):
- **Gratis!** (al geconfigureerd)

**Totaal voor testing:** €0
**Totaal voor productie:** €6.50 - €16.50/maand (afhankelijk van gebruik)

---

## 📊 Monitoring

### Render Dashboard

Check je deployment stats:
1. Ga naar [Render Dashboard](https://dashboard.render.com/)
2. Click op je service
3. Tabs:
   - **Logs:** Real-time logs
   - **Metrics:** CPU/Memory usage
   - **Events:** Deployment history

### Logs Bekijken

**In Render Dashboard:**
- Click "Logs" tab
- Live logs worden getoond
- Search functionaliteit beschikbaar

**Via CLI (advanced):**
```bash
# Install Render CLI
npm install -g @render/cli

# Login
render login

# View logs
render logs labour-market-intelligence-api
```

---

## 🔄 Updates Deployen

Je code wordt **automatisch gedeployed** wanneer je pusht naar GitHub!

```bash
# Make changes
git add .
git commit -m "Update feature X"
git push

# Render detecteert push en deployed automatisch! 🎉
```

**Manual Deploy:**
1. Ga naar Render Dashboard
2. Click "Manual Deploy"
3. Selecteer branch
4. Click "Deploy"

---

## ⚡ Performance Tips

### Reduce Cold Starts (Free Tier)

**Optie 1:** Ping je API elke 10 minuten
```bash
# Add cron job (bijv. cron-job.org)
*/10 * * * * curl https://your-api.onrender.com/api/status
```

**Optie 2:** Upgrade naar $7/maand (aanbevolen voor productie)

### Speed Up Response Time

Claude API calls duren 8-12 seconden. Dit is normaal.

**Voor betere UX:**
1. Toon loading animation tijdens generatie
2. Update button text naar "Rapport wordt gegenereerd..."
3. Toon progress indicator

---

## 🎉 Success!

Als alles werkt:
- ✅ Backend draait op Render
- ✅ Frontend verbindt met backend
- ✅ Rapporten worden gegenereerd
- ✅ Emails worden verstuurd

**Je hebt nu een volledig werkend Labour Market Intelligence platform! 🚀**

---

## 📞 Hulp Nodig?

**Render Support:**
- Docs: https://render.com/docs
- Community: https://community.render.com/

**Anthropic Support:**
- Docs: https://docs.anthropic.com/
- Discord: https://www.anthropic.com/discord

**Project Issues:**
- GitHub Issues: https://github.com/WouterArtsRecruitin/labour-market-intelligence-landing/issues

---

## 🔐 Security Checklist

Voordat je live gaat:

- [ ] API keys zijn **niet** in de code (alleen in Render environment)
- [ ] CORS is geconfigureerd (alleen jouw domain toegestaan)
- [ ] Rate limiting is actief (10 req/15min)
- [ ] HTTPS is enabled (Render doet dit automatisch)
- [ ] Email credentials zijn veilig opgeslagen
- [ ] `.env` files zijn **niet** in git
- [ ] Privacy Policy en Terms zijn up-to-date

---

**Made with ❤️ by WouterArts Recruitin • Powered by Claude AI**
