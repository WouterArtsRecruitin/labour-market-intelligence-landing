# Deployment Guide - Labour Market Intelligence API

Complete gids voor het deployen van de backend API.

## 🎯 Deployment Opties

### 1. Render (Aanbevolen - Gratis Tier Beschikbaar)

**Voordelen:**
- Gratis tier beschikbaar
- Automatische deploys vanaf GitHub
- Environment variabelen via dashboard
- SSL certificates automatisch
- Simpele setup

**Stappen:**

1. **Push code naar GitHub** (als nog niet gedaan)

2. **Ga naar [Render](https://render.com)** en log in/sign up

3. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect je GitHub repository
   - Selecteer de repo: `labour-market-intelligence-landing`

4. **Configureer de service:**
   ```
   Name: labour-market-intelligence-api
   Region: Frankfurt (EU)
   Branch: main (of je feature branch)
   Root Directory: api
   Runtime: Node
   Build Command: npm install
   Start Command: npm start
   ```

5. **Stel Environment Variables in:**
   In het Render dashboard, ga naar "Environment":
   ```
   ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USER=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password
   EMAIL_FROM="Recruitin <noreply@recruitin.com>"
   ALLOWED_ORIGINS=https://labour-market-intelligence.netlify.app
   NODE_ENV=production
   ```

6. **Deploy!**
   - Click "Create Web Service"
   - Render zal automatisch deployen
   - Je krijgt een URL zoals: `https://labour-market-intelligence-api.onrender.com`

7. **Update Frontend:**
   Update `script.js` met je nieuwe API URL:
   ```javascript
   this.apiUrl = 'https://labour-market-intelligence-api.onrender.com';
   ```

**⚠️ Gratis Tier Limiet:**
- Na 15 minuten inactiviteit gaat de server slapen
- Eerste request daarna duurt ~30 seconden (cold start)
- Betaald plan ($7/maand) voorkomt dit

---

### 2. Railway

**Voordelen:**
- $5 gratis credits per maand
- Zeer snelle deploys
- Automatische SSL
- Database hosting beschikbaar

**Stappen:**

1. **Install Railway CLI:**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login:**
   ```bash
   railway login
   ```

3. **Initialize project:**
   ```bash
   cd api
   railway init
   ```

4. **Add environment variables:**
   ```bash
   railway variables set ANTHROPIC_API_KEY=sk-ant-xxxxx
   railway variables set EMAIL_USER=your@email.com
   railway variables set EMAIL_PASSWORD=your_password
   # ... etc voor alle env vars
   ```

5. **Deploy:**
   ```bash
   railway up
   ```

6. **Get URL:**
   ```bash
   railway domain
   ```

---

### 3. Vercel (Met Serverless Functions)

**Voordelen:**
- Gratis tier
- Geoptimaliseerd voor serverless
- Automatische scaling

**Nadelen:**
- Serverless functions hebben 10s timeout (free tier)
- Claude API calls kunnen langer duren

**Stappen:**

1. **Install Vercel CLI:**
   ```bash
   npm i -g vercel
   ```

2. **Create `vercel.json` in api folder:**
   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "src/server.js",
         "use": "@vercel/node"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "src/server.js"
       }
     ],
     "env": {
       "NODE_ENV": "production"
     }
   }
   ```

3. **Deploy:**
   ```bash
   cd api
   vercel
   ```

4. **Set environment variables:**
   ```bash
   vercel env add ANTHROPIC_API_KEY
   vercel env add EMAIL_USER
   # ... etc
   ```

5. **Deploy to production:**
   ```bash
   vercel --prod
   ```

---

### 4. DigitalOcean App Platform

**Voordelen:**
- Stabiele uptime
- Gratis tier ($0 tier voor static sites)
- Betaalde tiers vanaf $5/maand

**Stappen:**

1. **Ga naar [DigitalOcean App Platform](https://cloud.digitalocean.com/apps)**

2. **Create App** → Connect GitHub repo

3. **Configure:**
   - Source: `api` directory
   - Run Command: `npm start`
   - HTTP Port: 3002

4. **Environment Variables:**
   Voeg toe via dashboard

5. **Launch App**

---

### 5. Docker + VPS (Hetzner, Linode, etc.)

**Voordelen:**
- Volledige controle
- Goedkoop (€3-5/maand)
- Geen cold starts

**Stappen:**

1. **Create Dockerfile** (al aanwezig in README):
   ```dockerfile
   FROM node:18-alpine
   WORKDIR /app
   COPY package*.json ./
   RUN npm install --production
   COPY . .
   EXPOSE 3002
   CMD ["npm", "start"]
   ```

2. **Build image:**
   ```bash
   docker build -t lmi-api .
   ```

3. **Test locally:**
   ```bash
   docker run -p 3002:3002 --env-file .env lmi-api
   ```

4. **Deploy to VPS:**
   ```bash
   # SSH into VPS
   ssh user@your-vps-ip

   # Install Docker
   curl -fsSL https://get.docker.com | sh

   # Clone repo
   git clone https://github.com/WouterArtsRecruitin/labour-market-intelligence-landing.git
   cd labour-market-intelligence-landing/api

   # Create .env file
   nano .env  # Add all environment variables

   # Run with Docker Compose
   docker compose up -d
   ```

5. **Setup nginx reverse proxy** (optional):
   ```nginx
   server {
       listen 80;
       server_name api.yourdomain.com;

       location / {
           proxy_pass http://localhost:3002;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection 'upgrade';
           proxy_set_header Host $host;
           proxy_cache_bypass $http_upgrade;
       }
   }
   ```

---

## 🔐 Environment Variables Checklist

Zorg ervoor dat deze variabelen zijn ingesteld in je deployment:

### Verplicht:
- [x] `ANTHROPIC_API_KEY` - Claude AI API key
- [x] `NODE_ENV=production`
- [x] `ALLOWED_ORIGINS` - Comma-separated list van frontend URLs

### Optioneel (maar aanbevolen):
- [ ] `EMAIL_HOST` - SMTP host
- [ ] `EMAIL_PORT` - SMTP port
- [ ] `EMAIL_USER` - Email username
- [ ] `EMAIL_PASSWORD` - Email password
- [ ] `EMAIL_FROM` - From address
- [ ] `PORT` - Server port (default: 3002)
- [ ] `RATE_LIMIT_MAX_REQUESTS` - Max requests per window
- [ ] `LOG_LEVEL` - Logging level (info/debug/error)

---

## 🧪 Testen na Deployment

### 1. Health Check
```bash
curl https://your-api-url.com/api/health
```

Verwachte output:
```json
{
  "status": "healthy",
  "services": {
    "claude": { "status": "healthy" },
    "email": { "status": "healthy" }
  }
}
```

### 2. Test Report Generation
```bash
curl -X POST https://your-api-url.com/api/generate-report \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "company": "TestCorp",
    "position": "Software Engineer",
    "sector": "Technology",
    "location": "Amsterdam",
    "experienceLevel": "senior",
    "keySkills": ["JavaScript", "React"],
    "salaryRange": { "min": 70000, "max": 90000 }
  }'
```

---

## 📊 Monitoring & Logging

### Render
- Logs beschikbaar in dashboard
- Metrics voor CPU/memory
- Uptime monitoring

### Railway
- Real-time logs via CLI: `railway logs`
- Metrics in dashboard

### Custom VPS
Installeer monitoring tools:

```bash
# PM2 voor process management
npm install -g pm2
pm2 start src/server.js --name lmi-api
pm2 startup  # Auto-start on reboot
pm2 save

# View logs
pm2 logs lmi-api
```

---

## 🚨 Troubleshooting

### API niet bereikbaar
- Check firewall settings op VPS
- Verify CORS settings in `.env`
- Check logs voor errors

### Claude API errors
- Verify `ANTHROPIC_API_KEY` is correct
- Check API credits in Anthropic console
- Check logs voor rate limiting

### Email niet verzonden
- Verify email credentials
- Check email provider settings
- Gmail: ensure "Less secure app access" is enabled OR use App Password

### Slow performance
- Render free tier heeft cold starts
- Upgrade naar paid tier ($7/maand)
- Of gebruik Railway/VPS voor altijd-actieve server

---

## 💰 Kosten Overzicht

| Platform | Gratis Tier | Betaald Tier | Opmerking |
|----------|-------------|--------------|-----------|
| **Render** | ✅ 750u/maand | $7/maand | Cold starts op gratis tier |
| **Railway** | $5 credits | $5+ credits | Pay-as-you-go |
| **Vercel** | ✅ Unlimited | $20/maand | 10s timeout limit |
| **DigitalOcean** | ❌ | $5/maand | Stabiel |
| **Hetzner VPS** | ❌ | €3/maand | Beste prijs/prestatie |

**Claude AI kosten:** ~$0.10 per rapport (geschat)

---

## 📚 Volgende Stappen

Na deployment:

1. **Update Frontend:** Wijzig API URL in `script.js`
2. **Test Volledig:** Genereer test rapport
3. **Monitor:** Check logs voor errors
4. **Backup:** Backup environment variables
5. **Documentation:** Update README met productie URL

---

**Vragen? Contact: info@recruitin.com**
