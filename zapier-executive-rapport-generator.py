"""
ZAPIER STEP 5: EXECUTIVE LABOUR MARKET INTELLIGENCE REPORT GENERATOR
=====================================================================

Genereert professional executive rapporten zoals het voorbeeld.
Gebruikt Claude AI voor intelligente analyse van PDF data + workforce intelligence.

Version: 2.0
Author: Wouter Arts - Recruitin AI
Date: 27 Oktober 2025
"""

import anthropic
import json
import os
from datetime import datetime

# =====================================
# CONFIGURATION
# =====================================

CLAUDE_API_KEY = os.environ.get('CLAUDE_API_KEY')  # Set in Zapier
CLAUDE_MODEL = "claude-sonnet-4-20250514"

# =====================================
# AWARD-WINNING CLAUDE PROMPT
# =====================================

EXECUTIVE_ANALYSIS_PROMPT = """
Je bent een **Elite Nederlandse Arbeidsmarkt Intelligence Expert** met 15+ jaar ervaring.
Je specialisme: Executive-level strategic market analysis voor recruitment.

🎯 MISSIE: Genereer een PROFESSIONEEL executive rapport EXACT zoals het voorbeeld.

---

## INPUT DATA

**Functietitel:** {job_title}
**Locatie:** {location}
**Bedrijf:** {company_name}
**Contact Email:** {contact_email}
**Vacature URL:** {vacancy_url}

**Jobdigger PDF Data:**
```
{jobdigger_pdf_text}
```

**LinkedIn Talent Insights PDF Data:**
```
{linkedin_pdf_text}
```

**Vacaturetekst:**
```
{vacancy_text}
```

---

## ANALYSE REQUIREMENTS

Je MOET een **complete, data-driven analyse** maken met deze secties:

### 1. EXECUTIVE SUMMARY & STRATEGIC INTELLIGENCE
- **Markt Assessment:** Krappe/ruime markt analyse (2-3 zinnen professional)
- **Time-to-hire:** Range in dagen (realistisch voor NL markt)
- **Talent pipeline:** Aantal actieve kandidaten (estimate op basis van functie/regio)
- **Urgentie Classificatie:** Kritiek/Hoog/Normaal/Laag

### 2. ADVANCED MARKET INTELLIGENCE DASHBOARD

Bereken deze **exacte metrics**:

```json
{{
  "talent_schaarste_index": "X.X/10.0",  // 1.0 = ruim, 10.0 = extreem schaars
  "time_to_hire_min": XX,                // dagen minimum
  "time_to_hire_max": XX,                // dagen maximum (incl notice)
  "success_rate": "XX%",                 // offer acceptance rate
  "markt_actie_window": XX               // dagen voor optimale positionering
}}
```

**Berekeningslogica:**
- Tech/IT rollen: schaarste 7-9/10, time-to-hire 60-120 dagen
- Management: schaarste 7-9/10, time-to-hire 75-120 dagen
- Productie/operations: schaarste 5-7/10, time-to-hire 45-75 dagen
- Sales/marketing: schaarste 4-6/10, time-to-hire 30-60 dagen
- Admin/support: schaarste 2-4/10, time-to-hire 20-45 dagen

### 3. COMPREHENSIVE SALARY INTELLIGENCE 2025

Bereken **Nederlandse markt benchmarks** (bruto maandsalaris):

```json
{{
  "p25_junior": "€X,XXX",     // 25th percentile
  "p50_mediaan": "€X,XXX",    // Mediaan (MAIN metric)
  "p75_senior": "€X,XXX",     // 75th percentile
  "bonus_avg_pct": XX         // Bonus % van basis
}}
```

**Salary Guidelines NL 2025:**
- Entry/Junior: €2,500-3,500
- Medior: €3,500-5,500
- Senior: €5,500-7,500
- Lead/Manager: €6,500-9,500
- Director/Executive: €9,500-15,000+

**Regio correcties:**
- Amsterdam/Utrecht: +10-15%
- Rotterdam/Den Haag: +5-10%
- Eindhoven/Nijmegen: Baseline
- Overige steden: -5-10%

### 4. TOTAL COMPENSATION ANALYSIS

Bereken **complete compensation package**:

**💰 Compensation Components Breakdown:**
```json
{{
  "base_salary": "€X,XXX",              // P50 mediaan
  "variable_bonus_pct": XX,              // 8-15% typisch
  "stock_options_pct": XX,               // 0-20% (startup>corporate)
  "pension_employer_pct": 8.5,           // Standaard NL
  "lease_auto_eligibility_pct": XX,      // 60-80% management
  "home_office_allowance_yearly": 950    // €950 standaard NL
}}
```

**📈 Growth & Benefits Intelligence:**
```json
{{
  "salary_growth_1yr_pct": XX,           // 5-12% typisch
  "salary_growth_3yr_pct": XX,           // 15-35% cumulatief
  "talent_scarcity_factor": "X.X/10",    // Same as dashboard
  "avg_notice_period_months": "1-2"      // Standaard NL
}}
```

### 5. ⭐ WORKFORCE AVAILABILITY INTELLIGENCE (KRITIEK!)

Dit is **NIEUWE SECTIE** - zeer belangrijk voor klant!

Bereken **kandidaat beschikbaarheid segmentatie**:

```json
{{
  "actief_werkzoekend": {{
    "percentage": XX,        // Typisch 15-25% van totale pool
    "aantal": XXX,
    "description": "Direct beschikbaar, actief solliciteren, notice period 0-1 maand"
  }},
  "latent_werkzoekend": {{
    "percentage": XX,        // Typisch 35-45% van totale pool
    "aantal": XXX,
    "description": "Open voor kansen, niet actief zoekend, notice period 1-3 maanden"
  }},
  "niet_werkzoekend": {{
    "percentage": XX,        // Typisch 35-45% van totale pool
    "aantal": XXX,
    "description": "Tevreden in huidige rol, moeilijk te bewegen, premium offer nodig"
  }},
  "total_candidates": XXXX   // Som van alle segmenten
}}
```

**Berekeningslogica Workforce:**
- Total candidates = functie schaarste × regio size × sector factor
- Actief % hoger bij: economische onzekerheid, sector krimp, junior rollen
- Latent % hoger bij: stabiele markt, medior/senior, goede arbeidsvoorwaarden
- Niet werkzoekend % hoger bij: schaarse skills, senior+, niche expertise

**Realistische ranges:**
- Tech/IT: 500-2000 candidates, 20% actief, 40% latent, 40% niet
- Management: 300-1000 candidates, 15% actief, 35% latent, 50% niet
- Productie: 1000-3000 candidates, 25% actief, 45% latent, 30% niet
- Sales: 800-2500 candidates, 30% actief, 45% latent, 25% niet

### 6. ⭐ DEMOGRAFISCHE INTELLIGENCE (KRITIEK!)

Dit is **NIEUWE SECTIE** - zeer belangrijk voor klant!

Bereken **leeftijdsverdeling** van talent pool:

```json
{{
  "leeftijd": {{
    "25-35": {{"percentage": XX, "aantal": XXX}},   // Typisch 35-45%
    "36-45": {{"percentage": XX, "aantal": XXX}},   // Typisch 30-40%
    "46-55": {{"percentage": XX, "aantal": XXX}},   // Typisch 20-25%
    "55+": {{"percentage": XX, "aantal": XXX}}      // Typisch 5-10%
  }}
}}
```

Bereken **opleidingsniveau verdeling**:

```json
{{
  "opleiding": {{
    "MBO": {{"percentage": XX, "aantal": XXX}},
    "HBO": {{"percentage": XX, "aantal": XXX}},
    "WO": {{"percentage": XX, "aantal": XXX}}
  }}
}}
```

**Berekeningslogica Opleiding:**
- Tech/IT: 15% MBO, 60% HBO, 25% WO
- Management: 10% MBO, 50% HBO, 40% WO
- Productie/Operations: 60% MBO, 35% HBO, 5% WO
- Sales/Marketing: 20% MBO, 60% HBO, 20% WO
- Finance/Legal: 5% MBO, 40% HBO, 55% WO

### 7. CANDIDATE MOTIVATION INTELLIGENCE

Top 8 motivatie drivers met **realistische percentages**:

```json
{{
  "autonomy_influence": XX,        // 85-95% voor senior
  "financial_rewards": XX,         // 80-90% altijd hoog
  "work_life_balance": XX,         // 70-85% stijgende trend
  "career_growth": XX,             // 85-95% vooral medior
  "innovation_tech": XX,           // 75-90% tech/startup
  "team_culture": XX,              // 80-90% altijd belangrijk
  "company_reputation": XX,        // 85-95% senior+
  "meaningful_impact": XX          // 70-85% varies per sector
}}
```

### 8. RECRUITMENT STRATEGY & CHANNEL INTELLIGENCE

Bepaal **optimale sourcing strategie**:

```json
{{
  "primary_channel": "...",          // Kies beste kanaal
  "secondary_channels": "...",       // Support kanalen
  "timeline_weeks": "XX-XX",         // Realistische timeline
  "budget_range_total": "€XXk-XXk"   // Total cost of hire
}}
```

**Channel Decision Matrix:**
- Executive/Senior: "Executive search & LinkedIn Premium"
- Tech/IT: "LinkedIn Premium & Tech communities"
- Management: "Executive search & Professional netwerken"
- Productie: "Jobboards & Referrals"
- Junior: "Jobboards & LinkedIn"

**Budget Guidelines:**
- Executive: €25k-50k (search fee + ads)
- Senior: €15k-30k
- Medior: €8k-15k
- Junior: €3k-8k

### 9. STRATEGIC CONCLUSIONS & ACTION PLAN

Genereer **4 concrete immediate priorities**:

1. **Competitive Compensation Positioning**
   - Target range: €X,XXX - €X,XXX (±7% van P50)
   - Include X% variable + comprehensive benefits

2. **Strategic Channel & Sourcing Mix**
   - [Primary channel] als main approach
   - Ondersteund door [secondary] voor pipeline

3. **Timeline Acceleration & Market Response**
   - Launch binnen X dagen - [markt urgentie reden]

4. **Success Rate Optimization**
   - Target XX% door focus op [top motivatie driver]

---

## OUTPUT FORMAT REQUIREMENTS

**KRITIEK:** Return **ALLEEN** een JSON object, geen extra tekst:

```json
{{
  "executive_summary": {{
    "markt_assessment": "2-3 professionele zinnen...",
    "time_to_hire_range": "XX-XX dagen",
    "actieve_kandidaten": XXX,
    "urgentie": "Kritiek|Hoog|Normaal|Laag",
    "recruitment_classificatie": "Executive Schaarste|High Demand|Normaal|Beschikbaar"
  }},

  "market_intelligence_dashboard": {{
    "talent_schaarste_index": "X.X",
    "time_to_hire_min": XX,
    "time_to_hire_max": XX,
    "success_rate_pct": XX,
    "markt_actie_window_days": XX,
    "markt_status": "Extreem hete markt|Krappe markt|Normale markt|Ruime markt",
    "actie_urgentie": "onmiddellijke actie vereist|spoedige actie|normale planning|geen urgentie"
  }},

  "salary_intelligence": {{
    "p25_junior": XXXX,
    "p50_mediaan": XXXX,
    "p75_senior": XXXX,
    "bonus_avg_pct": XX
  }},

  "total_compensation": {{
    "components": {{
      "base_salary": XXXX,
      "variable_bonus_pct": XX,
      "stock_options_pct": XX,
      "pension_employer_pct": 8.5,
      "lease_auto_eligibility_pct": XX,
      "home_office_allowance_yearly": 950
    }},
    "growth_benefits": {{
      "salary_growth_1yr_pct": XX,
      "salary_growth_3yr_pct": XX,
      "talent_scarcity_factor": "X.X",
      "avg_notice_period": "1-2 maanden"
    }}
  }},

  "workforce_availability": {{
    "actief_werkzoekend": {{
      "percentage": XX,
      "aantal": XXX,
      "description": "Direct beschikbaar, actief solliciteren"
    }},
    "latent_werkzoekend": {{
      "percentage": XX,
      "aantal": XXX,
      "description": "Open voor kansen, niet actief zoekend"
    }},
    "niet_werkzoekend": {{
      "percentage": XX,
      "aantal": XXX,
      "description": "Tevreden in huidige rol, moeilijk te bewegen"
    }},
    "total_candidates": XXXX
  }},

  "demographics": {{
    "leeftijd": {{
      "25-35": {{"percentage": XX, "aantal": XXX}},
      "36-45": {{"percentage": XX, "aantal": XXX}},
      "46-55": {{"percentage": XX, "aantal": XXX}},
      "55+": {{"percentage": XX, "aantal": XXX}}
    }},
    "opleiding": {{
      "MBO": {{"percentage": XX, "aantal": XXX}},
      "HBO": {{"percentage": XX, "aantal": XXX}},
      "WO": {{"percentage": XX, "aantal": XXX}}
    }}
  }},

  "motivation_drivers": {{
    "autonomy_influence": XX,
    "financial_rewards": XX,
    "work_life_balance": XX,
    "career_growth": XX,
    "innovation_tech": XX,
    "team_culture": XX,
    "company_reputation": XX,
    "meaningful_impact": XX
  }},

  "recruitment_strategy": {{
    "primary_channel": "...",
    "secondary_channels": "...",
    "timeline_weeks_min": XX,
    "timeline_weeks_max": XX,
    "budget_range_min_k": XX,
    "budget_range_max_k": XX
  }},

  "strategic_priorities": [
    {{
      "title": "Competitive Compensation Positioning",
      "description": "Target salary range: €X,XXX - €X,XXX voor markt-competitieve positie. Include XX% variable component en comprehensive benefits package."
    }},
    {{
      "title": "Strategic Channel & Sourcing Mix",
      "description": "[Primary] als primary approach, ondersteund door [Secondary] voor comprehensive pipeline coverage."
    }},
    {{
      "title": "Timeline Acceleration & Market Response",
      "description": "Launch binnen XX dagen - [urgentie reden]."
    }},
    {{
      "title": "Candidate Experience & Success Rate Optimization",
      "description": "Target XX% success rate door focus op top motivatie driver: [driver] (XX% importance factor)."
    }}
  ],

  "meta": {{
    "generated_date": "{current_date}",
    "reliability_score": XX,
    "data_sources_count": X,
    "ai_model": "Claude AI Sonnet 4",
    "analysis_type": "Executive Strategic Market Analysis"
  }}
}}
```

---

## QUALITY STANDARDS

✅ **Data Realism:** Alle cijfers moeten realistisch zijn voor NL markt 2025
✅ **Professional Tone:** Executive-level language, geen casual taal
✅ **Completeness:** ALLE secties moeten gevuld zijn (geen "N/A" of "Unknown")
✅ **Consistency:** Cijfers moeten logisch samenhangen (bijv. schaarste vs time-to-hire)
✅ **Actionability:** Concrete, implementeerbare recommendations

---

## RELIABILITY SCORING

Bereken **overall reliability score**:

```
Reliability = (
  PDF_quality_score × 0.4 +
  Market_knowledge_score × 0.3 +
  Logic_consistency_score × 0.2 +
  Completeness_score × 0.1
)

- Met beide PDFs vol data: 90-98%
- Met 1 goede PDF: 75-89%
- Met alleen vacancy text: 60-74%
- Zonder PDFs: 50-59%
```

---

## 🎯 FINAL INSTRUCTION

Analyseer de input data GRONDIG. Gebruik je expertise om **intelligente estimates** te maken waar data ontbreekt. Genereer een **COMPLEET JSON object** dat direct gebruikt kan worden voor HTML rapport generatie.

**BELANGRIJK:** Return ALLEEN valid JSON, geen markdown code blocks, geen extra tekst!
"""

# =====================================
# MAIN EXECUTION FUNCTION
# =====================================

def generate_executive_report(input_data):
    """
    Main function aangeroepen door Zapier

    Input format van Zapier:
    {
        'functietitel': 'productiemanager',
        'locatie': 'Nijmegen',
        'bedrijfsnaam': 'ACME BV',
        'email': 'hr@acme.nl',
        'vacature_url': 'https://...',
        'jobdigger_pdf_text': '...',
        'linkedin_pdf_text': '...',
        'vacature_text': '...'
    }
    """

    try:
        # Initialize Claude client
        client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

        # Prepare prompt with input data
        current_date = datetime.now().strftime("%d %B %Y om %H:%M")

        filled_prompt = EXECUTIVE_ANALYSIS_PROMPT.format(
            job_title=input_data.get('functietitel', 'Niet opgegeven'),
            location=input_data.get('locatie', 'Nederland'),
            company_name=input_data.get('bedrijfsnaam', 'Niet opgegeven'),
            contact_email=input_data.get('email', ''),
            vacancy_url=input_data.get('vacature_url', ''),
            jobdigger_pdf_text=input_data.get('jobdigger_pdf_text', 'Geen Jobdigger PDF data beschikbaar')[:15000],
            linkedin_pdf_text=input_data.get('linkedin_pdf_text', 'Geen LinkedIn Talent Insights data beschikbaar')[:15000],
            vacancy_text=input_data.get('vacature_text', 'Geen vacaturetekst beschikbaar')[:10000],
            current_date=current_date
        )

        # Call Claude AI
        print("🤖 Calling Claude AI for executive analysis...")

        message = client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=16000,
            temperature=0.3,  # Lower for more consistent/reliable output
            messages=[{
                "role": "user",
                "content": filled_prompt
            }]
        )

        # Extract JSON from response
        response_text = message.content[0].text

        # Clean response (remove potential markdown)
        response_text = response_text.strip()
        if response_text.startswith('```json'):
            response_text = response_text[7:]
        if response_text.startswith('```'):
            response_text = response_text[3:]
        if response_text.endswith('```'):
            response_text = response_text[:-3]
        response_text = response_text.strip()

        # Parse JSON
        analysis_data = json.loads(response_text)

        print("✅ Claude AI analysis complete!")
        print(f"📊 Reliability Score: {analysis_data['meta']['reliability_score']}%")

        return analysis_data

    except json.JSONDecodeError as e:
        print(f"❌ JSON Parse Error: {str(e)}")
        print(f"Response was: {response_text[:500]}")
        raise

    except Exception as e:
        print(f"❌ Error in generate_executive_report: {str(e)}")
        raise


# =====================================
# HTML REPORT GENERATOR
# =====================================

def generate_html_report(data, input_data):
    """
    Genereert professional HTML email zoals in voorbeeld
    """

    job_title = input_data.get('functietitel', 'Niet opgegeven')
    location = input_data.get('locatie', 'Nederland')

    # Helper function: format currency
    def fmt_eur(amount):
        return f"€{amount:,}".replace(',', '.')

    html = f"""
<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Executive AI Intelligence: {job_title}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 0;
            background: #f5f5f5;
        }}

        .container {{
            background: white;
            margin: 20px;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}

        .header {{
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            color: white;
            padding: 40px 30px;
            text-align: center;
        }}

        .header h1 {{
            margin: 0 0 10px 0;
            font-size: 28px;
            font-weight: 600;
        }}

        .header .subtitle {{
            font-size: 18px;
            opacity: 0.9;
            margin: 5px 0;
        }}

        .header .meta {{
            font-size: 14px;
            opacity: 0.8;
            margin-top: 15px;
        }}

        .section {{
            padding: 30px;
            border-bottom: 1px solid #eee;
        }}

        .section:last-child {{
            border-bottom: none;
        }}

        .section h2 {{
            color: #2c3e50;
            font-size: 24px;
            margin: 0 0 20px 0;
            padding-bottom: 10px;
            border-bottom: 3px solid #FF6B35;
        }}

        .section h3 {{
            color: #34495e;
            font-size: 18px;
            margin: 20px 0 10px 0;
        }}

        .alert-box {{
            background: #FF6B35;
            color: white;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
            text-align: center;
        }}

        .alert-box .icon {{
            font-size: 24px;
            margin-bottom: 10px;
        }}

        .alert-box .title {{
            font-size: 20px;
            font-weight: 600;
            margin-bottom: 8px;
        }}

        .alert-box .subtitle {{
            font-size: 14px;
            opacity: 0.95;
        }}

        .metrics-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }}

        .metric-box {{
            background: #FFF3E0;
            padding: 25px;
            border-radius: 8px;
            text-align: center;
            border: 2px solid #FFE0B2;
        }}

        .metric-box .value {{
            font-size: 36px;
            font-weight: 700;
            color: #FF6B35;
            margin: 0 0 5px 0;
        }}

        .metric-box .label {{
            font-size: 12px;
            font-weight: 600;
            color: #666;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .metric-box .sublabel {{
            font-size: 11px;
            color: #999;
            margin-top: 5px;
        }}

        .salary-banner {{
            background: linear-gradient(135deg, #FF6B35 0%, #FF8C42 100%);
            color: white;
            padding: 40px 30px;
            text-align: center;
            margin: 30px 0;
            border-radius: 8px;
        }}

        .salary-banner h2 {{
            color: white;
            border: none;
            margin: 0 0 10px 0;
            font-size: 20px;
        }}

        .salary-banner .amount {{
            font-size: 56px;
            font-weight: 700;
            margin: 20px 0;
        }}

        .salary-banner .description {{
            font-size: 14px;
            opacity: 0.95;
            margin-bottom: 30px;
        }}

        .salary-range {{
            display: flex;
            justify-content: space-around;
            margin-top: 20px;
        }}

        .salary-range .range-item {{
            text-align: center;
        }}

        .salary-range .range-value {{
            font-size: 24px;
            font-weight: 600;
        }}

        .salary-range .range-label {{
            font-size: 12px;
            opacity: 0.9;
            margin-top: 5px;
        }}

        .compensation-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin: 20px 0;
        }}

        .comp-box {{
            background: #f8f9fa;
            padding: 25px;
            border-radius: 8px;
            border-left: 4px solid #FF6B35;
        }}

        .comp-box.blue {{
            border-left-color: #3498db;
        }}

        .comp-box.purple {{
            border-left-color: #9b59b6;
        }}

        .comp-box h3 {{
            margin-top: 0;
            font-size: 16px;
        }}

        .comp-item {{
            display: flex;
            justify-content: space-between;
            padding: 8px 0;
            border-bottom: 1px solid #e0e0e0;
        }}

        .comp-item:last-child {{
            border-bottom: none;
        }}

        .comp-item .label {{
            color: #666;
            font-size: 14px;
        }}

        .comp-item .value {{
            font-weight: 600;
            color: #333;
            font-size: 14px;
        }}

        .workforce-chart {{
            margin: 20px 0;
        }}

        .workforce-bar {{
            margin: 15px 0;
            background: #f0f0f0;
            border-radius: 8px;
            overflow: hidden;
        }}

        .workforce-bar-fill {{
            padding: 15px 20px;
            color: white;
            font-weight: 600;
            display: flex;
            align-items: center;
            justify-content: space-between;
            transition: width 0.3s ease;
        }}

        .workforce-bar-fill.active {{
            background: linear-gradient(90deg, #27ae60 0%, #2ecc71 100%);
        }}

        .workforce-bar-fill.latent {{
            background: linear-gradient(90deg, #f39c12 0%, #f1c40f 100%);
        }}

        .workforce-bar-fill.niet {{
            background: linear-gradient(90deg, #e74c3c 0%, #c0392b 100%);
        }}

        .workforce-detail {{
            background: #f8f9fa;
            padding: 15px;
            margin: 10px 0;
            border-radius: 6px;
            border-left: 4px solid #ddd;
        }}

        .workforce-detail.active {{
            border-left-color: #27ae60;
        }}

        .workforce-detail.latent {{
            border-left-color: #f39c12;
        }}

        .workforce-detail.niet {{
            border-left-color: #e74c3c;
        }}

        .demo-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin: 20px 0;
        }}

        .demo-box {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
        }}

        .demo-item {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 0;
            border-bottom: 1px solid #e0e0e0;
        }}

        .demo-item:last-child {{
            border-bottom: none;
        }}

        .demo-bar {{
            width: 100%;
            height: 8px;
            background: #e0e0e0;
            border-radius: 4px;
            overflow: hidden;
            margin-top: 5px;
        }}

        .demo-bar-fill {{
            height: 100%;
            background: linear-gradient(90deg, #3498db 0%, #2980b9 100%);
            transition: width 0.3s ease;
        }}

        .motivation-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }}

        .motivation-item {{
            background: #f8f9fa;
            padding: 15px;
            border-radius: 6px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-left: 3px solid #3498db;
        }}

        .motivation-label {{
            font-size: 14px;
            color: #555;
        }}

        .motivation-value {{
            font-size: 18px;
            font-weight: 700;
            color: #3498db;
        }}

        .strategy-box {{
            background: #e8f5e9;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
            border-left: 4px solid #4caf50;
        }}

        .strategy-item {{
            margin: 15px 0;
        }}

        .strategy-item strong {{
            color: #2e7d32;
        }}

        .priority-list {{
            list-style: none;
            padding: 0;
            margin: 20px 0;
        }}

        .priority-item {{
            background: #fff3e0;
            padding: 20px;
            margin: 15px 0;
            border-radius: 8px;
            border-left: 4px solid #FF6B35;
        }}

        .priority-item h4 {{
            margin: 0 0 10px 0;
            color: #e65100;
            font-size: 16px;
        }}

        .priority-item p {{
            margin: 0;
            color: #666;
            font-size: 14px;
            line-height: 1.5;
        }}

        .footer {{
            background: #2c3e50;
            color: white;
            padding: 30px;
            text-align: center;
        }}

        .footer h3 {{
            color: white;
            margin: 0 0 20px 0;
            font-size: 18px;
        }}

        .footer .contact {{
            font-size: 14px;
            margin: 5px 0;
        }}

        .footer .contact a {{
            color: #FF6B35;
            text-decoration: none;
        }}

        .footer .meta {{
            font-size: 12px;
            opacity: 0.7;
            margin-top: 20px;
            padding-top: 20px;
            border-top: 1px solid rgba(255,255,255,0.1);
        }}

        @media (max-width: 600px) {{
            .compensation-grid,
            .demo-grid {{
                grid-template-columns: 1fr;
            }}

            .metrics-grid {{
                grid-template-columns: 1fr;
            }}

            .container {{
                margin: 10px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- HEADER -->
        <div class="header">
            <h1>🤖 Executive AI Intelligence: {job_title} in {location}</h1>
            <div class="subtitle">Complete Strategic Analysis & Intelligence Report</div>
            <div class="meta">Gegenereerd {data['meta']['generated_date']}</div>
            <div class="meta">{job_title} • {location}</div>
        </div>

        <!-- EXECUTIVE SUMMARY -->
        <div class="section">
            <h2>📅 Strategic Analysis Datum: {datetime.now().strftime("%d %B %Y")}</h2>
            <h2>📋 Executive Summary & Strategic Intelligence</h2>

            <h3>🎯 Strategische Marktpositie</h3>
            <p><strong>Markt Assessment:</strong> {data['executive_summary']['markt_assessment']}</p>

            <p><strong>Recruitment Urgentie Classificatie:</strong> {data['executive_summary']['urgentie']} - {data['executive_summary']['recruitment_classificatie']} -
            Deze beoordeling is gebaseerd op real-time markt intelligence, vraag/aanbod dynamiek en concurrentie analyse.</p>
        </div>

        <!-- MARKET INTELLIGENCE DASHBOARD -->
        <div class="section">
            <h2>📊 Advanced Market Intelligence Dashboard</h2>

            <div class="alert-box">
                <div class="icon">🌡 🔥🔥 {data['market_intelligence_dashboard']['markt_status']}</div>
                <div class="subtitle">Markt Actie Window: {data['market_intelligence_dashboard']['markt_actie_window_days']} dagen voor optimale positionering</div>
            </div>

            <div class="metrics-grid">
                <div class="metric-box">
                    <div class="value">{data['market_intelligence_dashboard']['talent_schaarste_index']}</div>
                    <div class="label">TALENT SCHAARSTE INDEX</div>
                    <div class="sublabel">10.0 = Extreem schaars talent</div>
                </div>

                <div class="metric-box">
                    <div class="value">{data['market_intelligence_dashboard']['time_to_hire_min']}-{data['market_intelligence_dashboard']['time_to_hire_max']}</div>
                    <div class="label">TIME-TO-HIRE RANGE</div>
                    <div class="sublabel">Inclusief notice periods</div>
                </div>

                <div class="metric-box">
                    <div class="value">{data['market_intelligence_dashboard']['success_rate_pct']}%</div>
                    <div class="label">SUCCESS RATE</div>
                    <div class="sublabel">Offer acceptance ratio</div>
                </div>
            </div>
        </div>

        <!-- SALARY INTELLIGENCE -->
        <div class="section">
            <div class="salary-banner">
                <h2>💰 Comprehensive Salary Intelligence 2025</h2>
                <h3 style="color: white; margin: 0;">🇳🇱 Nederlandse Markt Benchmark - Total Compensation</h3>
                <div class="amount">{fmt_eur(data['salary_intelligence']['p50_mediaan'])}</div>
                <div class="description">Markt Mediaan (P50) - Bruto maandsalaris basis, exclusief variabele componenten</div>

                <div class="salary-range">
                    <div class="range-item">
                        <div class="range-label">P25 (Junior)</div>
                        <div class="range-value">{fmt_eur(data['salary_intelligence']['p25_junior'])}</div>
                    </div>
                    <div class="range-item">
                        <div class="range-label">P75 (Senior)</div>
                        <div class="range-value">{fmt_eur(data['salary_intelligence']['p75_senior'])}</div>
                    </div>
                </div>

                <div style="margin-top: 20px; font-size: 16px;">
                    Bonus Gemiddeld<br>
                    <span style="font-size: 28px; font-weight: 700;">{data['salary_intelligence']['bonus_avg_pct']}%</span>
                </div>
            </div>
        </div>

        <!-- TOTAL COMPENSATION ANALYSIS -->
        <div class="section">
            <h2>💼 Total Compensation Analysis</h2>

            <div class="compensation-grid">
                <div class="comp-box blue">
                    <h3>📊 Compensation Components Breakdown</h3>
                    <div class="comp-item">
                        <span class="label">💰 Base Salary:</span>
                        <span class="value">{fmt_eur(data['total_compensation']['components']['base_salary'])} (markt mediaan)</span>
                    </div>
                    <div class="comp-item">
                        <span class="label">🎯 Variable Bonus:</span>
                        <span class="value">{data['total_compensation']['components']['variable_bonus_pct']}% gemiddeld ({fmt_eur(int(data['total_compensation']['components']['base_salary'] * data['total_compensation']['components']['variable_bonus_pct'] / 100))})</span>
                    </div>
                    <div class="comp-item">
                        <span class="label">📈 Stock Options:</span>
                        <span class="value">{data['total_compensation']['components']['stock_options_pct']}% van vergelijkbare rollen</span>
                    </div>
                    <div class="comp-item">
                        <span class="label">🏦 Pensioen Bijdrage:</span>
                        <span class="value">{data['total_compensation']['components']['pension_employer_pct']}% werkgever</span>
                    </div>
                    <div class="comp-item">
                        <span class="label">🚗 Lease Auto Eligibility:</span>
                        <span class="value">{data['total_compensation']['components']['lease_auto_eligibility_pct']}% van posities</span>
                    </div>
                    <div class="comp-item">
                        <span class="label">🏠 Home Office Allowance:</span>
                        <span class="value">€{data['total_compensation']['components']['home_office_allowance_yearly']}/jaar standaard</span>
                    </div>
                </div>

                <div class="comp-box purple">
                    <h3>📈 Growth & Benefits Intelligence</h3>
                    <div class="comp-item">
                        <span class="label">📊 1-jaar salary groeitrend:</span>
                        <span class="value">+{data['total_compensation']['growth_benefits']['salary_growth_1yr_pct']}% (marktgemiddeld)</span>
                    </div>
                    <div class="comp-item">
                        <span class="label">🚀 3-jaar salary groeitrend:</span>
                        <span class="value">+{data['total_compensation']['growth_benefits']['salary_growth_3yr_pct']}% (cumulatief)</span>
                    </div>
                    <div class="comp-item">
                        <span class="label">💡 Talent schaarste factor:</span>
                        <span class="value">{data['total_compensation']['growth_benefits']['talent_scarcity_factor']}/10 (hoog = schaars)</span>
                    </div>
                    <div class="comp-item">
                        <span class="label">⏰ Gemiddelde notice period:</span>
                        <span class="value">{data['total_compensation']['growth_benefits']['avg_notice_period']}</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- ⭐ WORKFORCE AVAILABILITY (NIEUW!) -->
        <div class="section">
            <h2>👥 Workforce Availability Intelligence</h2>
            <p><strong>Kandidaat Beschikbaarheid Analyse:</strong> Total pipeline van {data['workforce_availability']['total_candidates']} kandidaten</p>

            <div class="workforce-chart">
                <div class="workforce-bar">
                    <div class="workforce-bar-fill active" style="width: {data['workforce_availability']['actief_werkzoekend']['percentage']}%">
                        <span>🟢 Actief werkzoekend: {data['workforce_availability']['actief_werkzoekend']['percentage']}%</span>
                        <span>{data['workforce_availability']['actief_werkzoekend']['aantal']} kandidaten</span>
                    </div>
                </div>

                <div class="workforce-bar">
                    <div class="workforce-bar-fill latent" style="width: {data['workforce_availability']['latent_werkzoekend']['percentage']}%">
                        <span>🟡 Latent werkzoekend: {data['workforce_availability']['latent_werkzoekend']['percentage']}%</span>
                        <span>{data['workforce_availability']['latent_werkzoekend']['aantal']} kandidaten</span>
                    </div>
                </div>

                <div class="workforce-bar">
                    <div class="workforce-bar-fill niet" style="width: {data['workforce_availability']['niet_werkzoekend']['percentage']}%">
                        <span>🔴 Niet werkzoekend: {data['workforce_availability']['niet_werkzoekend']['percentage']}%</span>
                        <span>{data['workforce_availability']['niet_werkzoekend']['aantal']} kandidaten</span>
                    </div>
                </div>
            </div>

            <div class="workforce-detail active">
                <strong>🟢 Actief werkzoekend ({data['workforce_availability']['actief_werkzoekend']['percentage']}%):</strong> {data['workforce_availability']['actief_werkzoekend']['description']}
            </div>

            <div class="workforce-detail latent">
                <strong>🟡 Latent werkzoekend ({data['workforce_availability']['latent_werkzoekend']['percentage']}%):</strong> {data['workforce_availability']['latent_werkzoekend']['description']}
            </div>

            <div class="workforce-detail niet">
                <strong>🔴 Niet werkzoekend ({data['workforce_availability']['niet_werkzoekend']['percentage']}%):</strong> {data['workforce_availability']['niet_werkzoekend']['description']}
            </div>
        </div>

        <!-- ⭐ DEMOGRAPHICS (NIEUW!) -->
        <div class="section">
            <h2>📊 Demografische Intelligence</h2>

            <div class="demo-grid">
                <div class="demo-box">
                    <h3>Leeftijdsverdeling:</h3>
                    """

    # Leeftijd items
    for age_range, data_item in data['demographics']['leeftijd'].items():
        html += f"""
                    <div class="demo-item">
                        <div style="flex: 1;">
                            <strong>{age_range} jaar:</strong> {data_item['percentage']}% ({data_item['aantal']} kandidaten)
                            <div class="demo-bar">
                                <div class="demo-bar-fill" style="width: {data_item['percentage']}%"></div>
                            </div>
                        </div>
                    </div>
        """

    html += """
                </div>

                <div class="demo-box">
                    <h3>🎓 Opleidingsniveau Verdeling:</h3>
    """

    # Opleiding items
    for edu_level, data_item in data['demographics']['opleiding'].items():
        html += f"""
                    <div class="demo-item">
                        <div style="flex: 1;">
                            <strong>{edu_level} niveau:</strong> {data_item['percentage']}% ({data_item['aantal']} kandidaten)
                            <div class="demo-bar">
                                <div class="demo-bar-fill" style="width: {data_item['percentage']}%"></div>
                            </div>
                        </div>
                    </div>
        """

    html += """
                </div>
            </div>
        </div>

        <!-- MOTIVATION DRIVERS -->
        <div class="section">
            <h2>🎯 Candidate Motivation Intelligence</h2>
            <p><strong>💡 Key Motivation Drivers (AI-Analyzed from """ + str(data['workforce_availability']['total_candidates']) + """ candidates):</strong></p>

            <div class="motivation-grid">
                <div class="motivation-item">
                    <span class="motivation-label">🎯 Autonomy & Influence</span>
                    <span class="motivation-value">""" + str(data['motivation_drivers']['autonomy_influence']) + """%</span>
                </div>
                <div class="motivation-item">
                    <span class="motivation-label">💰 Financial Rewards</span>
                    <span class="motivation-value">""" + str(data['motivation_drivers']['financial_rewards']) + """%</span>
                </div>
                <div class="motivation-item">
                    <span class="motivation-label">⚖️ Work-Life Balance</span>
                    <span class="motivation-value">""" + str(data['motivation_drivers']['work_life_balance']) + """%</span>
                </div>
                <div class="motivation-item">
                    <span class="motivation-label">📚 Career Growth</span>
                    <span class="motivation-value">""" + str(data['motivation_drivers']['career_growth']) + """%</span>
                </div>
                <div class="motivation-item">
                    <span class="motivation-label">🚀 Innovation & Tech</span>
                    <span class="motivation-value">""" + str(data['motivation_drivers']['innovation_tech']) + """%</span>
                </div>
                <div class="motivation-item">
                    <span class="motivation-label">👥 Team Culture</span>
                    <span class="motivation-value">""" + str(data['motivation_drivers']['team_culture']) + """%</span>
                </div>
                <div class="motivation-item">
                    <span class="motivation-label">🏢 Company Reputation</span>
                    <span class="motivation-value">""" + str(data['motivation_drivers']['company_reputation']) + """%</span>
                </div>
                <div class="motivation-item">
                    <span class="motivation-label">🎖 Meaningful Impact</span>
                    <span class="motivation-value">""" + str(data['motivation_drivers']['meaningful_impact']) + """%</span>
                </div>
            </div>
        </div>

        <!-- RECRUITMENT STRATEGY -->
        <div class="section">
            <h2>🎯 Recruitment Strategy & Channel Intelligence</h2>
            <p><strong>💡 AI-Optimized Strategic Sourcing Approach</strong></p>

            <div class="strategy-box">
                <div class="strategy-item">
                    <strong>Primary Channel Strategy:</strong> """ + data['recruitment_strategy']['primary_channel'] + """
                </div>
                <div class="strategy-item">
                    <strong>Secondary Support Channels:</strong> """ + data['recruitment_strategy']['secondary_channels'] + """
                </div>
                <div class="strategy-item">
                    <strong>Estimated Timeline:</strong> """ + str(data['recruitment_strategy']['timeline_weeks_min']) + """-""" + str(data['recruitment_strategy']['timeline_weeks_max']) + """ weken volledige cyclus
                </div>
                <div class="strategy-item">
                    <strong>Budget Range Projection:</strong> €""" + str(data['recruitment_strategy']['budget_range_min_k']) + """k-""" + str(data['recruitment_strategy']['budget_range_max_k']) + """k total cost of hire
                </div>
            </div>
        </div>

        <!-- STRATEGIC CONCLUSIONS -->
        <div class="section">
            <h2>🚀 Strategic Conclusions & Executive Action Plan</h2>
            <p><strong>⚡ Immediate Strategic Priorities (Next 30 Days):</strong></p>

            <ul class="priority-list">
    """

    # Priority items
    for i, priority in enumerate(data['strategic_priorities'], 1):
        html += f"""
                <li class="priority-item">
                    <h4>{i}. {priority['title']}</h4>
                    <p>{priority['description']}</p>
                </li>
        """

    html += f"""
            </ul>
        </div>

        <!-- FOOTER -->
        <div class="footer">
            <h3>📞 Schedule Executive Strategy Session</h3>
            <p>Persoonlijk strategic alignment gesprek binnen 24 uur</p>
            <p>Gratis executive consultation & market intelligence briefing</p>

            <div style="margin-top: 30px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.2);">
                <h3>Recruitin</h3>
                <p style="font-size: 14px;">AI-Powered Executive Recruitment Intelligence & Strategic Consulting</p>
            </div>

            <div class="contact">
                <strong>Wouter Arts</strong> - Director AI Development & Strategic Intelligence
            </div>
            <div class="contact">
                📧 <a href="mailto:warts@recruitin.nl">warts@recruitin.nl</a> |
                📞 06-14314593 |
                🌐 <a href="https://recruitin.nl">recruitin.nl</a>
            </div>

            <div class="meta">
                Executive Intelligence Report gegenereerd op {data['meta']['generated_date']}<br>
                Powered by {data['meta']['ai_model']} • Market Reliability Score: {data['meta']['reliability_score']}%<br>
                Data Sources: {data['meta']['data_sources_count']} verified market intelligence indicators • © 2025 Recruitin BV
            </div>
        </div>
    </div>
</body>
</html>
    """

    return html


# =====================================
# ZAPIER ENTRY POINT
# =====================================

# This is what Zapier calls
try:
    # Get input from Zapier
    input_data = {
        'functietitel': input.get('functietitel', ''),
        'locatie': input.get('locatie', 'Nederland'),
        'bedrijfsnaam': input.get('bedrijfsnaam', ''),
        'email': input.get('email', ''),
        'vacature_url': input.get('vacature_url', ''),
        'jobdigger_pdf_text': input.get('jobdigger_pdf_text', ''),
        'linkedin_pdf_text': input.get('linkedin_pdf_text', ''),
        'vacature_text': input.get('vacature_text', '')
    }

    # Generate analysis
    analysis_data = generate_executive_report(input_data)

    # Generate HTML report
    html_report = generate_html_report(analysis_data, input_data)

    # Prepare output for Zapier
    output = {
        'to': input_data['email'],
        'subject': f"🤖 Executive AI Intelligence: {input_data['functietitel']} in {input_data['locatie']} | Complete Strategic Analysis",
        'body': html_report,

        # For Notion integration
        'notion_company': input_data['bedrijfsnaam'],
        'notion_job_title': input_data['functietitel'],
        'notion_location': input_data['locatie'],
        'notion_salary_p50': analysis_data['salary_intelligence']['p50_mediaan'],
        'notion_scarcity_index': analysis_data['market_intelligence_dashboard']['talent_schaarste_index'],
        'notion_time_to_hire': f"{analysis_data['market_intelligence_dashboard']['time_to_hire_min']}-{analysis_data['market_intelligence_dashboard']['time_to_hire_max']} dagen",
        'notion_reliability': f"{analysis_data['meta']['reliability_score']}%",
        'notion_url': input_data['vacature_url'],
        'notion_analysis_json': json.dumps(analysis_data, ensure_ascii=False)
    }

except Exception as e:
    # Error handling
    output = {
        'to': input.get('email', 'warts@recruitin.nl'),
        'subject': '❌ Error in Labour Market Intelligence Report',
        'body': f'<html><body><h1>Error</h1><p>Er is een fout opgetreden: {str(e)}</p></body></html>',
        'notion_company': input.get('bedrijfsnaam', 'Error'),
        'notion_job_title': input.get('functietitel', 'Error'),
        'notion_reliability': '0%'
    }
