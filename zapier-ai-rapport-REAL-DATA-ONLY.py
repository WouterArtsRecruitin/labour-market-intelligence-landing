# ================================================================
# RECRUITIN - AI-GEDREVEN ARBEIDSMARKT INTELLIGENCE RAPPORT
# REAL DATA ONLY - GEEN AANNAMES OF VERZONNEN CIJFERS
# ================================================================

import json
import datetime
import requests

# ========================================
# CONFIGURATION
# ========================================
RECRUITER_EMAIL = "warts@recruitin.nl"

# Claude AI API Configuration
CLAUDE_API_KEY = input_data.get('claude_api_key', 'sk-ant-xxx')
CLAUDE_API_URL = "https://api.anthropic.com/v1/messages"
CLAUDE_MODEL = "claude-sonnet-4-5-20250929"

# ========================================
# EXTRACT INPUT DATA FROM JOTFORM
# ========================================

# VEREISTE VELDEN
functietitel = input_data.get('functietitel', 'Niet opgegeven')
locatie = input_data.get('locatieRegio', input_data.get('locatie', 'Nederland'))
email = input_data.get('emailVoorRapportage', input_data.get('email', ''))
company_name = input_data.get('company_name', f'Organisatie in {locatie}')

# PDF TEKST van extraction stappen (Steps 2-4)
jobdigger_text = input_data.get('jobdigger_extracted_text', '')
linkedin_ti_text = input_data.get('linkedin_extracted_text', '')
vacature_pdf_text = input_data.get('vacature_extracted_text', '')

# OPTIONELE TEKSTVELDEN
vacature_text_input = input_data.get('vacaturetekst', '')
vacature_url = input_data.get('vacatureUrl', input_data.get('vacature_url', ''))

# Gecombineerde vacature tekst
vacature_text = vacature_pdf_text if vacature_pdf_text else vacature_text_input

# ========================================
# CLAUDE AI ANALYSIS FUNCTION - REAL DATA ONLY
# ========================================

def analyze_with_claude(vacature_text, jobdigger_text, linkedin_ti_text, functietitel, locatie):
    """Analyseert documenten met Claude AI - ALLEEN ECHTE DATA UIT DOCUMENTEN"""

    # Build context
    context_parts = []
    if vacature_text:
        context_parts.append(f"## VACATURETEKST:\n{vacature_text[:5000]}")
    if jobdigger_text:
        context_parts.append(f"## JOBDIGGER RAPPORT:\n{jobdigger_text[:5000]}")
    if linkedin_ti_text:
        context_parts.append(f"## LINKEDIN TALENT INSIGHTS:\n{linkedin_ti_text[:5000]}")

    if not context_parts:
        return None  # Geen documenten = geen analyse

    context = "\n\n".join(context_parts)

    # STRICT PROMPT - ALLEEN DATA UIT DOCUMENTEN
    prompt = f"""Je bent een data extraction expert. Extraheer ALLEEN informatie die letterlijk in de documenten staat.

{context}

VACATURE: {functietitel} | LOCATIE: {locatie}

STRIKTE REGELS:
- EXTRACT alleen data die LETTERLIJK in documenten staat
- GEEN aannames, GEEN schattingen, GEEN verzonnen cijfers
- Als informatie NIET in documenten staat → gebruik "N/A"
- Gebruik EXACTE cijfers uit documenten (niet afronden tenzij document dat doet)
- Als meerdere bronnen tegenstrijdig zijn → neem de meest recente/betrouwbare

Geef JSON response:

{{
  "schaarste_niveau": "Laag/Gemiddeld/Hoog of N/A",
  "schaarste_ratio": "X,X vacatures per kandidaat of N/A",
  "schaarste_score": "X.X of N/A",
  "time_to_hire_min": null of getal,
  "time_to_hire_max": null of getal,
  "success_rate": null of getal (percentage),
  "candidate_pool": null of getal,
  "urgency_days": null of getal,
  "market_temperature": "tekst uit document of N/A",
  "market_condition": "tekst uit document of N/A",
  "urgency_level": "tekst uit document of N/A",

  "beschikbaarheid": "getal uit document of N/A",
  "beschikbaarheid_tekst": "tekst uit document of N/A",

  "werkzoekend_ratio": {{
    "actief": null of getal (percentage),
    "latent": null of getal (percentage),
    "niet_werkzoekend": null of getal (percentage),
    "onzeker": null of getal (percentage)
  }},

  "leeftijd_verdeling": [
    {{"leeftijd": "20-30 jaar", "percentage": null of getal}},
    {{"leeftijd": "30-40 jaar", "percentage": null of getal}},
    {{"leeftijd": "40-50 jaar", "percentage": null of getal}},
    {{"leeftijd": "50+ jaar", "percentage": null of getal}}
  ],

  "motivation_drivers": [
    {{"driver": "naam uit document", "percentage": null of getal}}
  ],

  "push_factors": ["tekst uit document"],
  "pull_factors": ["tekst uit document"],

  "technische_skills": [
    {{"skill": "naam uit document", "niveau": "Essential/Nice to have/N/A"}}
  ],

  "soft_skills": ["tekst uit document"],

  "salaris_maand_p25": null of getal (bruto maandelijks),
  "salaris_maand_p50": null of getal,
  "salaris_maand_p75": null of getal,
  "bonus_percentage": null of getal,

  "salaris_jaar_p25_min": null of getal,
  "salaris_jaar_p25_max": null of getal,
  "salaris_jaar_p50_min": null of getal,
  "salaris_jaar_p50_max": null of getal,
  "salaris_jaar_p75_min": null of getal,
  "salaris_jaar_p75_max": null of getal,

  "total_workers_market": "getal uit document of N/A",
  "growth_percentage": null of getal,
  "open_vacancies": "getal uit document of N/A",
  "contract_permanent": null of getal (percentage),
  "contract_temporary": null of getal (percentage),
  "contract_freelance": null of getal (percentage),
  "average_age": null of getal,
  "gender_ratio": "tekst uit document of N/A",
  "employment_trend": "tekst uit document of N/A",
  "talent_pool_size": "getal uit document of N/A",
  "active_job_seekers": "getal uit document of N/A",
  "hiring_velocity": "tekst uit document of N/A",
  "hiring_speed": "tekst uit document of N/A",
  "education_wo": null of getal (percentage),
  "education_hbo": null of getal (percentage),
  "education_mbo": null of getal (percentage),
  "mobility_index": "tekst uit document of N/A",
  "avg_retention": "tekst uit document of N/A",
  "skill_gaps": "tekst uit document of N/A",

  "primary_channel": "tekst uit document of N/A",
  "secondary_channel": "tekst uit document of N/A",
  "estimated_timeline": "tekst uit document of N/A",
  "budget_range": "tekst uit document of N/A",

  "competitive_salary_min": null of getal,
  "competitive_salary_max": null of getal,
  "top_motivation": "tekst uit document of N/A",
  "top_motivation_percentage": null of getal
}}

BELANGRIJKE NOTES:
- null = data niet beschikbaar in documenten
- "N/A" = data niet beschikbaar (voor text velden)
- [] = lege array als geen data beschikbaar
- Gebruik exacte cijfers uit documenten
- Als salaris in jaar staat, bereken maand: jaar/12
- Als salaris in maand staat, bereken jaar: maand*12

Geef ALLEEN JSON, geen extra tekst."""

    # API Request
    headers = {
        "x-api-key": CLAUDE_API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }

    payload = {
        "model": CLAUDE_MODEL,
        "max_tokens": 4096,
        "messages": [{
            "role": "user",
            "content": prompt
        }]
    }

    try:
        response = requests.post(CLAUDE_API_URL, headers=headers, json=payload, timeout=60)

        if response.status_code != 200:
            return None

        result = response.json()
        content = result['content'][0]['text']

        # Extract JSON from response
        json_start = content.find('{')
        json_end = content.rfind('}') + 1

        if json_start >= 0 and json_end > json_start:
            json_str = content[json_start:json_end]
            return json.loads(json_str)

        return None

    except Exception as e:
        return None

# ========================================
# RUN ANALYSIS
# ========================================

ai_analysis = analyze_with_claude(
    vacature_text,
    jobdigger_text,
    linkedin_ti_text,
    functietitel,
    locatie
)

# ========================================
# EXTRACT DATA FROM AI ANALYSIS
# ========================================

# Helper functions
def safe_get(data, key, default="N/A"):
    """Get value from dict, return default if None or missing"""
    if data is None:
        return default
    value = data.get(key)
    return value if value is not None else default

def format_number(value, default="N/A"):
    """Format number or return N/A"""
    if value is None or value == "N/A":
        return default
    if isinstance(value, (int, float)):
        return f"{value:,}" if isinstance(value, int) else f"{value:.1f}"
    return str(value)

# Check if we have any analysis
if not ai_analysis:
    # NO ANALYSIS AVAILABLE - Gebruik minimale data
    schaarste_niveau = "N/A"
    schaarste_ratio = "N/A"
    schaarste_score = "N/A"
    time_to_hire = "N/A"
    success_rate = "N/A"
    candidate_pool = "N/A"
    urgency_days = "N/A"
    temperature = "Geen marktdata beschikbaar"
    market_condition = "N/A"
    urgency_level = "N/A"

    median_salary = "N/A"
    p25_salary = "N/A"
    p75_salary = "N/A"
    bonus_percentage = "N/A"
    comp_sal_min = "N/A"
    comp_sal_max = "N/A"

    actief_zoekend = "N/A"
    latent_geinteresseerd = "N/A"
    niet_werkzoekend = "N/A"
    onzeker_switch = "N/A"

    motivation_drivers = []
    top_motivation = "N/A"
    top_motivation_pct = "N/A"

    primary_channel = "N/A"
    secondary_channel = "N/A"
    estimated_timeline = "N/A"
    budget_range = "N/A"

    # Bericht voor gebruiker
    data_availability_note = "⚠️ Geen PDF documenten geanalyseerd. Upload Jobdigger, LinkedIn TI en/of Vacature PDFs voor een complete analyse."
else:
    # Extract all variables from AI analysis
    schaarste_niveau = safe_get(ai_analysis, 'schaarste_niveau', 'N/A')
    schaarste_ratio = safe_get(ai_analysis, 'schaarste_ratio', 'N/A')
    schaarste_score = safe_get(ai_analysis, 'schaarste_score', 'N/A')

    time_to_hire_min = safe_get(ai_analysis, 'time_to_hire_min', None)
    time_to_hire_max = safe_get(ai_analysis, 'time_to_hire_max', None)
    if time_to_hire_min and time_to_hire_max:
        time_to_hire = f"{time_to_hire_min}-{time_to_hire_max} dagen"
    else:
        time_to_hire = "N/A"

    success_rate = safe_get(ai_analysis, 'success_rate', 'N/A')
    candidate_pool = format_number(safe_get(ai_analysis, 'candidate_pool', None))
    urgency_days = safe_get(ai_analysis, 'urgency_days', 'N/A')
    temperature = safe_get(ai_analysis, 'market_temperature', 'N/A')
    market_condition = safe_get(ai_analysis, 'market_condition', 'N/A')
    urgency_level = safe_get(ai_analysis, 'urgency_level', 'N/A')

    # Salaris
    median_salary = safe_get(ai_analysis, 'salaris_maand_p50', None)
    p25_salary = safe_get(ai_analysis, 'salaris_maand_p25', None)
    p75_salary = safe_get(ai_analysis, 'salaris_maand_p75', None)
    bonus_percentage = safe_get(ai_analysis, 'bonus_percentage', None)

    comp_sal_min = safe_get(ai_analysis, 'competitive_salary_min', None)
    comp_sal_max = safe_get(ai_analysis, 'competitive_salary_max', None)

    # Werkzoekend ratio
    werkzoekend = safe_get(ai_analysis, 'werkzoekend_ratio', {})
    if isinstance(werkzoekend, dict):
        actief_zoekend = safe_get(werkzoekend, 'actief', 'N/A')
        latent_geinteresseerd = safe_get(werkzoekend, 'latent', 'N/A')
        niet_werkzoekend = safe_get(werkzoekend, 'niet_werkzoekend', 'N/A')
        onzeker_switch = safe_get(werkzoekend, 'onzeker', 'N/A')
    else:
        actief_zoekend = latent_geinteresseerd = niet_werkzoekend = onzeker_switch = "N/A"

    # Motivation drivers
    motivation_drivers = safe_get(ai_analysis, 'motivation_drivers', [])
    if not motivation_drivers:
        motivation_drivers = []

    top_motivation = safe_get(ai_analysis, 'top_motivation', 'N/A')
    top_motivation_pct = safe_get(ai_analysis, 'top_motivation_percentage', 'N/A')

    # Channels
    primary_channel = safe_get(ai_analysis, 'primary_channel', 'N/A')
    secondary_channel = safe_get(ai_analysis, 'secondary_channel', 'N/A')
    estimated_timeline = safe_get(ai_analysis, 'estimated_timeline', 'N/A')
    budget_range = safe_get(ai_analysis, 'budget_range', 'N/A')

    data_availability_note = "✅ Data geëxtraheerd uit geüploade PDF documenten."

# ========================================
# BUILD HTML EMAIL
# ========================================

# Generate current date/time
current_date = datetime.datetime.now().strftime("%d %B %Y")
current_time = datetime.datetime.now().strftime("%H:%M")

# Helper function voor motivation drivers HTML
def build_motivation_html(drivers):
    if not drivers or len(drivers) == 0:
        return '<p style="text-align: center; color: rgba(255,255,255,0.7);">📊 Geen motivation driver data beschikbaar in documenten</p>'

    # Split in twee kolommen
    half = (len(drivers) + 1) // 2
    left_column = drivers[:half]
    right_column = drivers[half:]

    def driver_html(d):
        driver_name = d.get('driver', 'N/A')
        pct = d.get('percentage')
        if pct is None or pct == "N/A":
            return f"<p>🎯 {driver_name}: <strong>N/A</strong></p>"
        return f"<p>🎯 {driver_name}: <strong>{pct}%</strong></p>"

    left_html = "".join([driver_html(d) for d in left_column])
    right_html = "".join([driver_html(d) for d in right_column])

    return f'<div class="column">{left_html}</div><div class="column">{right_html}</div>'

motivation_html = build_motivation_html(motivation_drivers)

# Helper function voor salary display
def format_salary(value):
    if value is None or value == "N/A":
        return "N/A"
    if isinstance(value, (int, float)):
        return f"€{int(value):,}"
    return str(value)

# Format salaries
median_salary_fmt = format_salary(median_salary)
p25_salary_fmt = format_salary(p25_salary)
p75_salary_fmt = format_salary(p75_salary)
comp_sal_min_fmt = format_salary(comp_sal_min)
comp_sal_max_fmt = format_salary(comp_sal_max)

# Bonus percentage display
bonus_display = f"{bonus_percentage}%" if bonus_percentage != "N/A" and bonus_percentage is not None else "N/A"

# Candidate pool display
candidate_pool_display = candidate_pool if candidate_pool != "N/A" else "N/A"

# BUILD COMPLETE HTML
html_report = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>AI Arbeidsmarkt Intelligence Rapport</title>
    <style>
        body {{ font-family: Arial, sans-serif; color: #333; background-color: #f5f5f5; margin: 0; padding: 20px; }}
        .container {{ max-width: 800px; margin: 0 auto; background: white; padding: 40px; border-radius: 8px; }}
        .header {{ background: #4CAF50; color: white; padding: 30px; text-align: center; margin: -40px -40px 40px -40px; border-radius: 8px 8px 0 0; }}
        .section {{ margin-bottom: 30px; }}
        .section-title {{ color: #2E7D32; font-size: 24px; font-weight: bold; margin-bottom: 20px; border-bottom: 3px solid #FF6B35; padding-bottom: 10px; }}
        .highlight {{ background: #E8F5E9; padding: 20px; border-radius: 5px; border-left: 5px solid #4CAF50; margin: 15px 0; }}
        .metric {{ background: #FFF3E0; padding: 15px; border-radius: 5px; text-align: center; margin: 10px 0; }}
        .metric-big {{ font-size: 36px; font-weight: bold; color: #E65100; }}
        .salary-box {{ background: #FF9800; color: white; padding: 30px; text-align: center; border-radius: 8px; margin: 20px 0; }}
        .two-column {{ display: table; width: 100%; }}
        .column {{ display: table-cell; width: 50%; padding: 0 10px; vertical-align: top; }}
        .four-column {{ display: table; width: 100%; }}
        .four-column .column {{ width: 25%; padding: 0 5px; }}
        .green-box {{ background: #4CAF50; color: white; padding: 25px; border-radius: 8px; margin: 20px 0; }}
        .footer {{ background: #37474F; color: white; padding: 30px; text-align: center; margin: 40px -40px -40px -40px; border-radius: 0 0 8px 8px; }}
        .doelgroep-box {{ background: #E1F5FE; padding: 25px; border-radius: 8px; border-left: 6px solid #03A9F4; margin: 20px 0; }}
        .data-note {{ background: #FFF3CD; color: #856404; padding: 15px; border-radius: 5px; border-left: 5px solid #FFC107; margin: 20px 0; text-align: center; font-weight: bold; }}
        .na-indicator {{ color: #999; font-style: italic; }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <div class="header">
            <h1>🤖 AI Arbeidsmarkt Intelligence</h1>
            <p>Executive Strategic Market Analysis & Intelligence Report</p>
            <p>Gegenereerd {current_date} om {current_time}</p>
        </div>

        <!-- Data Availability Note -->
        <div class="data-note">
            {data_availability_note}
        </div>

        <!-- Company Info -->
        <div style="text-align: center; margin-bottom: 30px;">
            <h2>{company_name}</h2>
            <p style="font-size: 18px; color: #666;">{functietitel} • {locatie}</p>
            <p style="color: #4CAF50;">📅 Strategic Analysis Datum: {current_date}</p>
        </div>

        <!-- Executive Summary -->
        <div class="section">
            <h2 class="section-title">📋 Executive Summary & Strategic Intelligence</h2>
            <div class="highlight">
                <h3>🎯 Strategische Marktpositie</h3>
                <p><strong>Markt Assessment:</strong> {market_condition}</p>
                <p><strong>Time-to-hire:</strong> {time_to_hire}</p>
                <p><strong>Kandidaten Pool:</strong> {candidate_pool_display}</p>
                <p><strong>Recruitment Urgentie:</strong> {urgency_level}</p>
            </div>
        </div>

        <!-- Market Intelligence -->
        <div class="section">
            <h2 class="section-title">📊 Advanced Market Intelligence Dashboard</h2>

            <div style="background: #FF5722; color: white; padding: 20px; text-align: center; border-radius: 8px; margin: 20px 0;">
                <div style="font-size: 18px;">🌡️ {temperature}</div>
                <div style="font-size: 14px; margin-top: 8px;">Markt Actie Window: {urgency_days} dagen</div>
            </div>

            <div class="two-column">
                <div class="column">
                    <div class="metric">
                        <div class="metric-big">{schaarste_score}</div>
                        <div>TALENT SCHAARSTE INDEX</div>
                        <small>10.0 = Extreem schaars talent</small>
                    </div>
                </div>
                <div class="column">
                    <div class="metric">
                        <div class="metric-big">{time_to_hire}</div>
                        <div>TIME-TO-HIRE RANGE</div>
                        <small>Inclusief notice periods</small>
                    </div>
                </div>
            </div>
            <div style="text-align: center;">
                <div class="metric" style="display: inline-block;">
                    <div class="metric-big">{success_rate}{"%" if success_rate != "N/A" else ""}</div>
                    <div>SUCCESS RATE</div>
                    <small>Offer acceptance ratio</small>
                </div>
            </div>
        </div>

        <!-- DOELGROEP ANALYSE -->
        <div class="section">
            <h2 class="section-title">👥 Doelgroep Analyse & Beschikbaarheid</h2>

            <div class="doelgroep-box">
                <h3 style="text-align: center; margin-bottom: 25px;">📈 Kandidaat Beschikbaarheid Segmentatie</h3>

                <div class="four-column">
                    <div class="column">
                        <div style="background: #4CAF50; color: white; padding: 20px; border-radius: 8px; text-align: center; margin: 5px;">
                            <div style="font-size: 32px; font-weight: bold; margin-bottom: 8px;">{actief_zoekend}{"%" if actief_zoekend != "N/A" else ""}</div>
                            <div style="font-size: 12px; text-transform: uppercase; font-weight: bold; margin-bottom: 8px;">ACTIEF ZOEKEND</div>
                            <p style="font-size: 11px; margin: 0;">Immediate beschikbaar</p>
                        </div>
                    </div>
                    <div class="column">
                        <div style="background: #FF9800; color: white; padding: 20px; border-radius: 8px; text-align: center; margin: 5px;">
                            <div style="font-size: 32px; font-weight: bold; margin-bottom: 8px;">{latent_geinteresseerd}{"%" if latent_geinteresseerd != "N/A" else ""}</div>
                            <div style="font-size: 12px; text-transform: uppercase; font-weight: bold; margin-bottom: 8px;">LATENT GEÏNTERESSEERD</div>
                            <p style="font-size: 11px; margin: 0;">Open voor goede kansen</p>
                        </div>
                    </div>
                    <div class="column">
                        <div style="background: #F44336; color: white; padding: 20px; border-radius: 8px; text-align: center; margin: 5px;">
                            <div style="font-size: 32px; font-weight: bold; margin-bottom: 8px;">{niet_werkzoekend}{"%" if niet_werkzoekend != "N/A" else ""}</div>
                            <div style="font-size: 12px; text-transform: uppercase; font-weight: bold; margin-bottom: 8px;">NIET WERKZOEKEND</div>
                            <p style="font-size: 11px; margin: 0;">Tevreden in huidige rol</p>
                        </div>
                    </div>
                    <div class="column">
                        <div style="background: #9C27B0; color: white; padding: 20px; border-radius: 8px; text-align: center; margin: 5px;">
                            <div style="font-size: 32px; font-weight: bold; margin-bottom: 8px;">{onzeker_switch}{"%" if onzeker_switch != "N/A" else ""}</div>
                            <div style="font-size: 12px; text-transform: uppercase; font-weight: bold; margin-bottom: 8px;">ONZEKER SWITCH</div>
                            <p style="font-size: 11px; margin: 0;">Overweegt verandering</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Salary Intelligence -->
        <div class="section">
            <h2 class="section-title">💰 Comprehensive Salary Intelligence 2025</h2>

            <div class="salary-box">
                <h3>🇳🇱 Nederlandse Markt Benchmark</h3>
                <div style="font-size: 48px; font-weight: bold; margin: 15px 0;">{median_salary_fmt}</div>
                <p>Markt Mediaan (P50) - Bruto maandsalaris</p>

                <div class="two-column" style="border-top: 2px solid rgba(255,255,255,0.3); padding-top: 15px; margin-top: 15px;">
                    <div class="column">
                        <div style="text-align: center;">
                            <div style="font-size: 12px; opacity: 0.8;">P25 (Junior)</div>
                            <div style="font-size: 18px; font-weight: bold;">{p25_salary_fmt}</div>
                        </div>
                    </div>
                    <div class="column">
                        <div style="text-align: center;">
                            <div style="font-size: 12px; opacity: 0.8;">P75 (Senior)</div>
                            <div style="font-size: 18px; font-weight: bold;">{p75_salary_fmt}</div>
                        </div>
                    </div>
                </div>
                <div style="text-align: center; margin-top: 15px;">
                    <div style="font-size: 12px; opacity: 0.8;">Bonus Gemiddeld</div>
                    <div style="font-size: 18px; font-weight: bold;">{bonus_display}</div>
                </div>
            </div>
        </div>

        <!-- Candidate Motivation -->
        <div class="section">
            <h2 class="section-title">🎯 Candidate Motivation Intelligence</h2>
            <div style="background: #E91E63; color: white; padding: 25px; border-radius: 8px;">
                <h4 style="text-align: center;">💡 Key Motivation Drivers</h4>
                <div class="two-column">
                    {motivation_html}
                </div>
            </div>
        </div>

        <!-- Recruitment Strategy -->
        <div class="section">
            <h2 class="section-title">🎯 Recruitment Strategy & Channel Intelligence</h2>

            <div style="background: #E8F5E8; padding: 25px; border-radius: 8px; border-left: 6px solid #4CAF50;">
                <h3>💡 Strategic Sourcing Approach</h3>
                <p><strong>Primary Channel:</strong> {primary_channel}</p>
                <p><strong>Secondary Channels:</strong> {secondary_channel}</p>
                <p><strong>Estimated Timeline:</strong> {estimated_timeline}</p>
                <p><strong>Budget Range:</strong> {budget_range}</p>
            </div>
        </div>

        <!-- Strategic Action Plan -->
        <div class="section">
            <h2 class="section-title">🚀 Strategic Conclusions & Executive Action Plan</h2>

            <div class="green-box">
                <h3>⚡ Immediate Strategic Priorities</h3>

                <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 8px; margin: 15px 0;">
                    <strong>1. Competitive Compensation Positioning</strong>
                    <p>Target salary range: {comp_sal_min_fmt} - {comp_sal_max_fmt}</p>
                    <p>Variable component: {bonus_display}</p>
                </div>

                <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 8px; margin: 15px 0;">
                    <strong>2. Strategic Channel & Sourcing Mix</strong>
                    <p>Primary: {primary_channel}</p>
                    <p>Secondary: {secondary_channel}</p>
                </div>

                <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 8px; margin: 15px 0;">
                    <strong>3. Timeline & Market Response</strong>
                    <p>Launch target: {urgency_days} dagen</p>
                    <p>Market temperature: {temperature}</p>
                </div>

                <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 8px;">
                    <strong>4. Candidate Experience Optimization</strong>
                    <p>Target success rate: {success_rate}{"%" if success_rate != "N/A" else ""}</p>
                    <p>Top motivatie driver: {top_motivation} ({top_motivation_pct}{"%" if top_motivation_pct != "N/A" else ""})</p>
                </div>
            </div>

            <div style="text-align: center; margin: 30px 0;">
                <a href="mailto:{RECRUITER_EMAIL}?subject=Executive Strategy Session - {functietitel} bij {company_name}" style="background: #FF6B35; color: white; padding: 15px 30px; text-decoration: none; border-radius: 25px; font-weight: bold; display: inline-block;">📞 Schedule Executive Strategy Session</a>
                <p style="color: #666; margin-top: 10px;">Persoonlijk strategic alignment gesprek binnen 24 uur</p>
            </div>
        </div>

        <!-- Footer -->
        <div class="footer">
            <h3>Recruitin</h3>
            <p>AI-Powered Executive Recruitment Intelligence</p>
            <div style="border-top: 1px solid rgba(255,255,255,0.2); padding-top: 20px; margin-top: 20px;">
                <p><strong>Wouter Arts</strong> - Director AI Development & Strategic Intelligence</p>
                <p>📧 {RECRUITER_EMAIL} | 📞 06-14314593 | 🌐 recruitin.nl</p>
                <p style="font-size: 12px; opacity: 0.8; margin-top: 15px;">
                    Executive Intelligence Report gegenereerd op {current_date} om {current_time}<br/>
                    Powered by Claude AI Sonnet 4.5 • Market Data: Document Extraction Only<br/>
                    © 2025 Recruitin BV
                </p>
            </div>
        </div>
    </div>
</body>
</html>'''

# ========================================
# OUTPUT FOR ZAPIER
# ========================================

email_subject = f'🤖 Executive AI Intelligence: {functietitel} in {locatie} | Market Analysis Report'

output = {
    'subject': email_subject,
    'body': html_report,
    'to': email,
    'html_email': html_report,
    'recipient_email': email,
    'company': company_name,
    'position': functietitel,
    'region': locatie,
    'functietitel': functietitel,
    'locatie': locatie,
    'current_date': current_date,
    'schaarste_niveau': schaarste_niveau,
    'ai_used': 'Yes' if ai_analysis else 'No - No documents provided',
    'data_source': 'PDF Documents Only' if ai_analysis else 'No Data',
    'status': 'success'
}
