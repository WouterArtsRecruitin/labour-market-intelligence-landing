# 🚀 Deployment Guide - Labour Market Intelligence Landing

## ✅ Current Status

**Platform Type:** FREE Lead Generation (no payment system)
**Stripe Status:** ❌ Completely removed (0 references)
**Files:** 2 HTML pages (index.html + demo-rapport.html)

## 📦 Deployment Branch

**Production Branch:** `claude/deploy-recruitment-platform-011CULXiBNFSx3CpMax1nPBC`

This branch contains:
- ✅ index.html - NO Stripe payment system
- ✅ demo-rapport.html - Recruitin brand colors
- ✅ Clean codebase (207 lines of Stripe code removed)
- ✅ Free "Vraag Gratis Rapport Aan" button

## 🆕 Setup New Netlify Site (Recommended)

### Step 1: Create New Site
1. Go to: https://app.netlify.com/
2. Click: **"Add new site"** → **"Import an existing project"**
3. Choose: **GitHub**
4. Select repository: **WouterArtsRecruitin/labour-market-intelligence-landing**
5. **IMPORTANT:** Branch to deploy: `claude/deploy-recruitment-platform-011CULXiBNFSx3CpMax1nPBC`
6. Build settings:
   - Build command: (leave empty)
   - Publish directory: `.`
7. Click: **"Deploy site"**

### Step 2: Configure Access (CRITICAL!)
1. **Immediately** after site creation, go to: Site settings → Access control
2. Ensure: **"Public"** is selected (NOT "Visitor access")
3. Save settings

### Step 3: Verify Deployment
Test these URLs work:
- Homepage: `https://[your-site].netlify.app/`
- Demo report: `https://[your-site].netlify.app/demo-rapport.html`

**Check:**
- ✅ No 403 errors
- ✅ No Stripe scripts
- ✅ Button says "Vraag Gratis Rapport Aan"
- ✅ Recruitin brand colors (#EF7D00, #4B4F51)

## 📊 What's Included

| File | Description | Stripe? |
|------|-------------|---------|
| `index.html` | Main landing page with free report request | ❌ NO |
| `demo-rapport.html` | Sample labour market report | ❌ NO |
| `styles.css` | Styles with Recruitin brand colors | ❌ NO |
| `script.js` | JavaScript (no payment logic) | ❌ NO |

## 🗑️ What Was Removed

- ❌ Stripe.js script tag
- ❌ Payment form section (€59/€71 pricing)
- ❌ Payment processing functions
- ❌ Card input elements
- ❌ 207 lines of payment-related code
- ❌ intelligence-landing.html (Versie B)

**Total cleanup:** 1,267 lines removed

## 🔧 Troubleshooting

### Issue: Site shows 403 Forbidden
**Solution:** Disable "Visitor access control" in Netlify settings

### Issue: Stripe still visible
**Solution:** Ensure deploying from `claude/deploy-recruitment-platform-011CULXiBNFSx3CpMax1nPBC` branch (NOT main)

### Issue: Old version cached
**Solution:** Hard refresh (Ctrl+Shift+R / Cmd+Shift+R) or Incognito mode

## 🎯 Domain Setup (Optional)

**Custom Domain:** `labour-market-intelligence.recruitin.nl`

1. Netlify: Site settings → Domain management
2. Add custom domain
3. Configure DNS at domain provider

## 📞 Support

Questions? Check the deployment logs at:
https://app.netlify.com/sites/[your-site]/deploys

---
Last updated: 22 October 2025
