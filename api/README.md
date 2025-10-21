# Labour Market Intelligence API 🚀

Backend API voor Labour Market Intelligence platform met Claude AI integratie voor het genereren van arbeidsmarkt analyse rapporten.

## 🎯 Features

- **Claude AI Integratie**: Uitgebreide arbeidsmarkt rapporten gegenereerd door Claude 3.5 Sonnet
- **Email Delivery**: Automatische verzending van rapporten via email
- **Rate Limiting**: Bescherming tegen misbruik (10 requests per 15 minuten)
- **CORS Support**: Veilige cross-origin requests
- **Security**: Helmet.js voor HTTP headers beveiliging
- **Logging**: Winston logger voor gedetailleerde logging
- **Health Checks**: Status endpoints voor monitoring

## 📋 Prerequisites

- **Node.js** >= 18.0.0
- **Anthropic API Key** (Claude AI)
- **Email account** (Gmail/SMTP) voor rapport verzending

## 🚀 Quick Start

### 1. Installatie

```bash
cd api
npm install
```

### 2. Environment Configuratie

Kopieer `.env.example` naar `.env`:

```bash
cp .env.example .env
```

Vul de environment variabelen in:

```env
# Server
PORT=3002
NODE_ENV=development

# Claude AI (VERPLICHT)
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password_here
EMAIL_FROM="Recruitin <noreply@recruitin.com>"

# CORS
ALLOWED_ORIGINS=http://localhost:3000,https://labour-market-intelligence.netlify.app
```

### 3. Start de Server

**Development mode (met auto-reload):**
```bash
npm run dev
```

**Production mode:**
```bash
npm start
```

Server draait op: `http://localhost:3002`

## 📡 API Endpoints

### 1. Generate Report

**POST** `/api/generate-report`

Genereer een arbeidsmarkt intelligence rapport met Claude AI.

**Request Body:**
```json
{
  "email": "user@example.com",
  "company": "TechCorp BV",
  "position": "Senior Marketing Manager",
  "sector": "Technology",
  "location": "Amsterdam, Nederland",
  "experienceLevel": "senior",
  "keySkills": ["Digital Marketing", "SEO", "Leadership"],
  "salaryRange": {
    "min": 60000,
    "max": 80000
  },
  "analysisFocus": "Focus op tech startup markt",
  "priorities": {
    "marketDemand": 9,
    "competitionAnalysis": 8,
    "salaryBenchmarking": 8,
    "recruitmentStrategy": 7
  }
}
```

**Response:**
```json
{
  "success": true,
  "message": "Rapport succesvol gegenereerd en verzonden naar uw email",
  "report": "# ARBEIDSMARKT INTELLIGENCE RAPPORT\n\n...",
  "metadata": {
    "generatedAt": "2025-10-21T14:30:00.000Z",
    "generationTime": 8.45,
    "emailSentTo": "user@example.com",
    "reportId": "RPT-1729521000000-A3F9X2P1Q"
  }
}
```

### 2. Health Check

**GET** `/api/health`

Check de status van alle services (Claude AI, Email).

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-10-21T14:30:00.000Z",
  "services": {
    "claude": {
      "status": "healthy",
      "model": "claude-3-5-sonnet-20241022",
      "apiConnected": true
    },
    "email": {
      "status": "healthy",
      "configured": true
    }
  },
  "version": "1.0.0"
}
```

### 3. Status Check

**GET** `/api/status`

Eenvoudige status check zonder externe dependencies.

**Response:**
```json
{
  "status": "ok",
  "message": "Labour Market Intelligence API is running",
  "timestamp": "2025-10-21T14:30:00.000Z"
}
```

## 🔑 Anthropic API Key Verkrijgen

1. Ga naar [Anthropic Console](https://console.anthropic.com/)
2. Maak een account aan of log in
3. Ga naar "API Keys" in het dashboard
4. Klik op "Create Key"
5. Kopieer de key en plak in `.env` als `ANTHROPIC_API_KEY`

**Pricing:** Claude API rekent per token. Geschatte kosten per rapport:
- Input: ~2,000 tokens (~$0.006)
- Output: ~6,000 tokens (~$0.090)
- **Totaal: ~$0.096 per rapport**

## 📧 Email Configuratie

### Gmail Setup

1. **App Password genereren:**
   - Ga naar [Google Account Security](https://myaccount.google.com/security)
   - Enable "2-Step Verification"
   - Ga naar "App passwords"
   - Genereer een app password voor "Mail"
   - Gebruik dit password als `EMAIL_PASSWORD` in `.env`

2. **Environment variables:**
```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_SECURE=false
EMAIL_USER=jouw.email@gmail.com
EMAIL_PASSWORD=your_16_character_app_password
```

### Andere Email Providers

**Outlook/Hotmail:**
```env
EMAIL_HOST=smtp-mail.outlook.com
EMAIL_PORT=587
```

**Custom SMTP:**
Configureer met je eigen SMTP credentials.

## 🏗️ Project Structuur

```
api/
├── src/
│   ├── routes/
│   │   └── report.routes.js       # API endpoint handlers
│   ├── services/
│   │   ├── claude.service.js      # Claude AI integratie
│   │   └── email.service.js       # Email verzending
│   ├── prompts/
│   │   └── market-analysis.js     # Claude AI prompts
│   ├── utils/
│   │   └── logger.js              # Winston logger
│   └── server.js                  # Main Express server
├── logs/                          # Log files (auto-generated)
├── .env                           # Environment variabelen
├── .env.example                   # Environment template
├── package.json                   # Dependencies
└── README.md                      # Deze file
```

## 🔒 Security Features

- **Helmet.js**: HTTP headers beveiliging
- **Rate Limiting**: 10 requests per 15 minuten per IP
- **CORS**: Whitelist van toegestane origins
- **Input Validation**: Validatie van alle request data
- **Error Handling**: Veilige error responses zonder sensitive data

## 📊 Logging

Logs worden geschreven naar:
- **Console**: Alle logs met colors (development)
- **logs/combined.log**: Alle logs (max 5MB, 5 files)
- **logs/error.log**: Alleen errors (max 5MB, 5 files)

Log levels: `error`, `warn`, `info`, `debug`

## 🧪 Testing

### Manual Testing met cURL

```bash
# Health check
curl http://localhost:3002/api/health

# Generate report
curl -X POST http://localhost:3002/api/generate-report \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "company": "TestCorp",
    "position": "Software Engineer",
    "sector": "Technology",
    "location": "Amsterdam",
    "experienceLevel": "senior",
    "keySkills": ["JavaScript", "React", "Node.js"],
    "salaryRange": { "min": 70000, "max": 90000 }
  }'
```

### Testing met Postman

1. Import de collection (TODO: create Postman collection)
2. Set environment variables
3. Run tests

## 🚀 Deployment

### Option 1: Render (Recommended)

1. Push code naar GitHub
2. Ga naar [Render](https://render.com)
3. Create new "Web Service"
4. Connect je GitHub repo
5. Configureer:
   - **Build Command**: `cd api && npm install`
   - **Start Command**: `cd api && npm start`
   - **Environment Variables**: Voeg alle `.env` variables toe
6. Deploy!

### Option 2: Railway

1. Install Railway CLI: `npm install -g @railway/cli`
2. Login: `railway login`
3. Init project: `railway init`
4. Add env vars: `railway variables`
5. Deploy: `railway up`

### Option 3: Docker

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install --production
COPY . .
EXPOSE 3002
CMD ["npm", "start"]
```

Build & Run:
```bash
docker build -t lmi-api .
docker run -p 3002:3002 --env-file .env lmi-api
```

## 🔧 Troubleshooting

### "ANTHROPIC_API_KEY not set"
- Controleer of `.env` file bestaat
- Controleer of `ANTHROPIC_API_KEY` correct is ingevuld
- Restart de server na `.env` wijzigingen

### Email niet verzonden
- Check `EMAIL_USER` en `EMAIL_PASSWORD` in `.env`
- Voor Gmail: gebruik App Password, niet normaal wachtwoord
- Check logs: `logs/error.log`

### CORS errors
- Voeg frontend URL toe aan `ALLOWED_ORIGINS` in `.env`
- Check of frontend op correcte port draait

### Rate limit exceeded
- Default: 10 requests per 15 minuten
- Verhoog via `RATE_LIMIT_MAX_REQUESTS` in `.env`
- Of wacht 15 minuten

## 📈 Performance

- **Gemiddelde response tijd**: 8-12 seconden
- **Claude API latency**: 6-10 seconden
- **Email verzending**: Async (non-blocking)
- **Memory usage**: ~50-100MB

## 📝 TODO / Roadmap

- [ ] Add unit tests (Jest)
- [ ] Add integration tests
- [ ] Database voor rapport opslag (PostgreSQL)
- [ ] Caching layer (Redis)
- [ ] Webhook support voor async processing
- [ ] API authentication (JWT)
- [ ] Usage analytics
- [ ] PDF generation (currently Markdown only)
- [ ] Multi-language support

## 🤝 Contributing

1. Fork het project
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push naar branch (`git push origin feature/AmazingFeature`)
5. Open een Pull Request

## 📄 License

MIT License - zie LICENSE file voor details

## 💬 Contact

**WouterArts Recruitin**
- Website: https://recruitin.com
- Email: info@recruitin.com
- GitHub: https://github.com/WouterArtsRecruitin

---

**Made with ❤️ by WouterArts Recruitin • Powered by Claude AI**
