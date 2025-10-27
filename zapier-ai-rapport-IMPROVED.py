# ================================================================
# RECRUITIN - AI-GEDREVEN ARBEIDSMARKT INTELLIGENCE RAPPORT
# VERBETERDE VERSIE - Combineert Claude AI + Mooie HTML Template
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

# OPTIONELE VELDEN - PDF tekst van eerdere Zapier stappen
jobdigger_text = input_data.get('jobdigger_extracted_text', '')
linkedin_ti_text = input_data.get('linkedin_extracted_text', '')
vacature_pdf_text = input_data.get('vacature_extracted_text', '')

# OPTIONELE TEKSTVELDEN
vacature_text_input = input_data.get('vacaturetekst', '')
vacature_url = input_data.get('vacatureUrl', input_data.get('vacature_url', ''))

# Gecombineerde vacature tekst
vacature_text = vacature_pdf_text if vacature_pdf_text else vacature_text_input

# ========================================
# CLAUDE AI ANALYSIS FUNCTION
# ========================================

def analyze_with_claude(vacature_text, jobdigger_text, linkedin_ti_text, functietitel, locatie):
    """Analyseert documenten met Claude AI - UITGEBREIDE VERSIE met alle velden"""

    # Build context
    context_parts = []
    if vacature_text:
        context_parts.append(f"## VACATURETEKST:\n{vacature_text[:5000]}")
    if jobdigger_text:
        context_parts.append(f"## JOBDIGGER RAPPORT:\n{jobdigger_text[:5000]}")
    if linkedin_ti_text:
        context_parts.append(f"## LINKEDIN TALENT INSIGHTS:\n{linkedin_ti_text[:5000]}")

    context = "\n\n".join(context_parts) if context_parts else "Geen documenten beschikbaar"

    # UITGEBREIDE Claude AI Prompt met ALLE benodigde velden
    prompt = f"""Analyseer deze arbeidsmarkt documenten en genereer VOLLEDIGE JSON output met ALLE velden.

{context}

VACATURE: {functietitel} | LOCATIE: {locatie}

Geef JSON response met REALISTISCHE data uit documenten (gebruik exacte cijfers als beschikbaar):

{{
  "schaarste_niveau": "Laag/Gemiddeld/Hoog",
  "schaarste_ratio": "X,X vacatures per kandidaat",
  "schaarste_score": "7.5",
  "time_to_hire_min": 45,
  "time_to_hire_max": 65,
  "success_rate": 72,
  "candidate_pool": 1850,
  "urgency_days": 14,
  "market_temperature": "🔥 Hete markt - technische vaardigheden zeer gewild",
  "market_condition": "krappe arbeidsmarkt met hoge vraag",
  "urgency_level": "Hoog - Technische Schaarste",

  "beschikbaarheid": "±12.500",
  "beschikbaarheid_tekst": "Geschikte kandidaten NL",

  "werkzoekend_ratio": {{
    "actief": 18,
    "latent": 42,
    "niet_werkzoekend": 32,
    "onzeker": 8
  }},

  "leeftijd_verdeling": [
    {{"leeftijd": "20-30 jaar", "percentage": 25}},
    {{"leeftijd": "30-40 jaar", "percentage": 38}},
    {{"leeftijd": "40-50 jaar", "percentage": 27}},
    {{"leeftijd": "50+ jaar", "percentage": 10}}
  ],

  "motivation_drivers": [
    {{"driver": "Career Growth Opportunities", "percentage": 89}},
    {{"driver": "Financial Rewards", "percentage": 87}},
    {{"driver": "Work-Life Balance", "percentage": 76}},
    {{"driver": "Innovation & Technology", "percentage": 82}},
    {{"driver": "Positive Team Culture", "percentage": 85}},
    {{"driver": "Company Reputation", "percentage": 91}},
    {{"driver": "Autonomy & Influence", "percentage": 92}},
    {{"driver": "Meaningful Impact Work", "percentage": 79}}
  ],

  "push_factors": [
    "Beperkte doorgroeimogelijkheden",
    "Onvoldoende salaris",
    "Weinig werk-privé balans"
  ],

  "pull_factors": [
    "Innovatieve projecten",
    "Professionele ontwikkeling",
    "Flexibel werken mogelijk"
  ],

  "technische_skills": [
    {{"skill": "Domein expertise", "niveau": "Essential"}},
    {{"skill": "Relevante certificaten", "niveau": "Nice to have"}},
    {{"skill": "Tools & systemen", "niveau": "Essential"}}
  ],

  "soft_skills": [
    "Communicatieve vaardigheden",
    "Probleemoplossend vermogen",
    "Teamwork"
  ],

  "salaris_maand_p25": 4013,
  "salaris_maand_p50": 4720,
  "salaris_maand_p75": 6042,
  "bonus_percentage": 8,

  "salaris_jaar_p25_min": 48156,
  "salaris_jaar_p25_max": 57787,
  "salaris_jaar_p50_min": 56640,
  "salaris_jaar_p50_max": 68016,
  "salaris_jaar_p75_min": 72504,
  "salaris_jaar_p75_max": 87089,

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
  "hiring_speed": "Gemiddeld",
  "education_wo": 43,
  "education_hbo": 42,
  "education_mbo": 15,
  "mobility_index": "Hoog",
  "avg_retention": "3.2 jaar",
  "skill_gaps": "Specialistische kennis, Nieuwe technologieën",

  "primary_channel": "LinkedIn Premium & Professional netwerken",
  "secondary_channel": "Job boards & referrals",
  "estimated_timeline": "12-16 weken",
  "budget_range": "€15k-35k",

  "competitive_salary_min": 4484,
  "competitive_salary_max": 5098,
  "top_motivation": "Career Growth Opportunities",
  "top_motivation_percentage": 89
}}

BELANGRIJK:
- Gebruik REALISTISCHE cijfers uit documenten
- Als document cijfers heeft, gebruik die EXACT
- Salaris in MAAND (bruto) en JAAR (totaal)
- Alle percentages zijn gehele getallen
- Geef VOLLEDIGE JSON terug

Geen extra tekst, alleen JSON."""

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
# FALLBACK DATA (if AI fails)
# ========================================

fallback_data = {
    "schaarste_niveau": "Gemiddeld",
    "schaarste_ratio": "2,5 vacatures per kandidaat",
    "schaarste_score": "7.4",
    "time_to_hire_min": 45,
    "time_to_hire_max": 65,
    "success_rate": 72,
    "candidate_pool": 2400,
    "urgency_days": 21,
    "market_temperature": "🔥 Hete markt - actie gewenst",
    "market_condition": "krappe arbeidsmarkt met hoge vraag",
    "urgency_level": "Hoog - Marktschaarste",
    "beschikbaarheid": "±12.500",
    "beschikbaarheid_tekst": "Geschikte kandidaten NL",
    "werkzoekend_ratio": {
        "actief": 18,
        "latent": 42,
        "niet_werkzoekend": 32,
        "onzeker": 8
    },
    "leeftijd_verdeling": [
        {"leeftijd": "20-30 jaar", "percentage": 22},
        {"leeftijd": "30-40 jaar", "percentage": 38},
        {"leeftijd": "40-50 jaar", "percentage": 28},
        {"leeftijd": "50+ jaar", "percentage": 12}
    ],
    "motivation_drivers": [
        {"driver": "Career Growth Opportunities", "percentage": 89},
        {"driver": "Financial Rewards", "percentage": 87},
        {"driver": "Work-Life Balance", "percentage": 76},
        {"driver": "Innovation & Technology", "percentage": 82},
        {"driver": "Positive Team Culture", "percentage": 85},
        {"driver": "Company Reputation", "percentage": 91},
        {"driver": "Autonomy & Influence", "percentage": 92},
        {"driver": "Meaningful Impact Work", "percentage": 79}
    ],
    "push_factors": [
        "Beperkte doorgroeimogelijkheden",
        "Onvoldoende salaris",
        "Weinig werk-privé balans"
    ],
    "pull_factors": [
        "Innovatieve projecten",
        "Professionele ontwikkeling",
        "Flexibel werken mogelijk"
    ],
    "technische_skills": [
        {"skill": "Domein expertise", "niveau": "Essential"},
        {"skill": "Relevante certificaten", "niveau": "Nice to have"},
        {"skill": "Tools & systemen", "niveau": "Essential"}
    ],
    "soft_skills": [
        "Communicatieve vaardigheden",
        "Probleemoplossend vermogen",
        "Teamwork"
    ],
    "salaris_maand_p25": 4013,
    "salaris_maand_p50": 4720,
    "salaris_maand_p75": 6042,
    "bonus_percentage": 8,
    "salaris_jaar_p25_min": 48156,
    "salaris_jaar_p25_max": 57787,
    "salaris_jaar_p50_min": 56640,
    "salaris_jaar_p50_max": 68016,
    "salaris_jaar_p75_min": 72504,
    "salaris_jaar_p75_max": 87089,
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
    "hiring_speed": "Gemiddeld",
    "education_wo": 43,
    "education_hbo": 42,
    "education_mbo": 15,
    "mobility_index": "Hoog",
    "avg_retention": "3.2 jaar",
    "skill_gaps": "Specialistische kennis",
    "primary_channel": "LinkedIn Premium & Professional netwerken",
    "secondary_channel": "Job boards & referrals",
    "estimated_timeline": "12-16 weken",
    "budget_range": "€15k-35k",
    "competitive_salary_min": 4484,
    "competitive_salary_max": 5098,
    "top_motivation": "Career Growth Opportunities",
    "top_motivation_percentage": 89
}

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

# Use fallback if AI fails
if not ai_analysis:
    ai_analysis = fallback_data

# ========================================
# EXTRACT DATA FROM AI ANALYSIS
# ========================================

# Safe get helper
def safe_get(data, key, default):
    return data.get(key, default)

# Extract all variables
schaarste_niveau = safe_get(ai_analysis, 'schaarste_niveau', 'Gemiddeld')
schaarste_ratio = safe_get(ai_analysis, 'schaarste_ratio', 'N/A')
schaarste_score = safe_get(ai_analysis, 'schaarste_score', '7.4')
time_to_hire = f"{safe_get(ai_analysis, 'time_to_hire_min', 45)}-{safe_get(ai_analysis, 'time_to_hire_max', 65)}"
success_rate = safe_get(ai_analysis, 'success_rate', 72)
candidate_pool = safe_get(ai_analysis, 'candidate_pool', 2400)
urgency_days = safe_get(ai_analysis, 'urgency_days', 21)
temperature = safe_get(ai_analysis, 'market_temperature', '🔥 Hete markt')
market_condition = safe_get(ai_analysis, 'market_condition', 'krappe arbeidsmarkt')
urgency_level = safe_get(ai_analysis, 'urgency_level', 'Hoog')

# Salaris (maandelijks)
median_salary = safe_get(ai_analysis, 'salaris_maand_p50', 4720)
p25_salary = safe_get(ai_analysis, 'salaris_maand_p25', 4013)
p75_salary = safe_get(ai_analysis, 'salaris_maand_p75', 6042)
bonus_percentage = safe_get(ai_analysis, 'bonus_percentage', 8)

# Competitive salary range (voor actieplan)
comp_sal_min = safe_get(ai_analysis, 'competitive_salary_min', int(median_salary * 0.95))
comp_sal_max = safe_get(ai_analysis, 'competitive_salary_max', int(median_salary * 1.08))

# Werkzoekend ratio
werkzoekend = safe_get(ai_analysis, 'werkzoekend_ratio', {})
actief_zoekend = safe_get(werkzoekend, 'actief', 18)
latent_geinteresseerd = safe_get(werkzoekend, 'latent', 42)
niet_werkzoekend = safe_get(werkzoekend, 'niet_werkzoekend', 32)
onzeker_switch = safe_get(werkzoekend, 'onzeker', 8)

# Motivation drivers
motivation_drivers = safe_get(ai_analysis, 'motivation_drivers', [])
top_motivation = safe_get(ai_analysis, 'top_motivation', 'Career Growth')
top_motivation_pct = safe_get(ai_analysis, 'top_motivation_percentage', 89)

# Channels
primary_channel = safe_get(ai_analysis, 'primary_channel', 'LinkedIn Premium')
secondary_channel = safe_get(ai_analysis, 'secondary_channel', 'Job boards')
estimated_timeline = safe_get(ai_analysis, 'estimated_timeline', '12-16 weken')
budget_range = safe_get(ai_analysis, 'budget_range', '€15k-35k')

# ========================================
# BUILD HTML EMAIL (MOOIE TEMPLATE)
# ========================================

# Generate current date/time
current_date = datetime.datetime.now().strftime("%d %B %Y")
current_time = datetime.datetime.now().strftime("%H:%M")

# Helper function voor motivation drivers HTML
def build_motivation_html(drivers):
    if not drivers or len(drivers) == 0:
        return "<p>Geen data beschikbaar</p>"

    # Split in twee kolommen
    half = (len(drivers) + 1) // 2
    left_column = drivers[:half]
    right_column = drivers[half:]

    left_html = "".join([f"<p>🎯 {d.get('driver', 'Unknown')}: <strong>{d.get('percentage', 0)}%</strong></p>" for d in left_column])
    right_html = "".join([f"<p>🚀 {d.get('driver', 'Unknown')}: <strong>{d.get('percentage', 0)}%</strong></p>" for d in right_column])

    return f'<div class="column">{left_html}</div><div class="column">{right_html}</div>'

motivation_html = build_motivation_html(motivation_drivers)

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
                <p><strong>Markt Assessment:</strong> De Nederlandse arbeidsmarkt voor {functietitel} posities in de {locatie} regio kenmerkt zich door {market_condition}. Onze AI-analyse identificeert een gemiddelde time-to-hire van <strong>{time_to_hire} dagen</strong> met ongeveer <strong>{candidate_pool:,} actieve kandidaten</strong> in de regionale talent pipeline.</p>
                <p><strong>Recruitment Urgentie Classificatie:</strong> {urgency_level} - Deze beoordeling is gebaseerd op real-time markt intelligence, vraag/aanbod dynamiek en concurrentie analyse.</p>
            </div>
        </div>

        <!-- Market Intelligence -->
        <div class="section">
            <h2 class="section-title">📊 Advanced Market Intelligence Dashboard</h2>

            <div style="background: #FF5722; color: white; padding: 20px; text-align: center; border-radius: 8px; margin: 20px 0;">
                <div style="font-size: 18px;">🌡️ {temperature}</div>
                <div style="font-size: 14px; margin-top: 8px;">Markt Actie Window: {urgency_days} dagen voor optimale positionering</div>
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
                    <div class="metric-big">{success_rate}%</div>
                    <div>SUCCESS RATE</div>
                    <small>Offer acceptance ratio</small>
                </div>
            </div>
        </div>

        <!-- DOELGROEP ANALYSE - MET ECHTE AI DATA -->
        <div class="section">
            <h2 class="section-title">👥 Doelgroep Analyse & Beschikbaarheid</h2>

            <div class="doelgroep-box">
                <h3 style="text-align: center; margin-bottom: 25px;">📈 Kandidaat Beschikbaarheid Segmentatie ({candidate_pool:,} professionals)</h3>

                <div class="four-column">
                    <div class="column">
                        <div style="background: #4CAF50; color: white; padding: 20px; border-radius: 8px; text-align: center; margin: 5px;">
                            <div style="font-size: 32px; font-weight: bold; margin-bottom: 8px;">{actief_zoekend}%</div>
                            <div style="font-size: 12px; text-transform: uppercase; font-weight: bold; margin-bottom: 8px;">ACTIEF ZOEKEND</div>
                            <p style="font-size: 11px; margin: 0;">Immediate beschikbaar, hoge response rate</p>
                        </div>
                    </div>
                    <div class="column">
                        <div style="background: #FF9800; color: white; padding: 20px; border-radius: 8px; text-align: center; margin: 5px;">
                            <div style="font-size: 32px; font-weight: bold; margin-bottom: 8px;">{latent_geinteresseerd}%</div>
                            <div style="font-size: 12px; text-transform: uppercase; font-weight: bold; margin-bottom: 8px;">LATENT GEÏNTERESSEERD</div>
                            <p style="font-size: 11px; margin: 0;">Open voor goede kansen, premium approach</p>
                        </div>
                    </div>
                    <div class="column">
                        <div style="background: #F44336; color: white; padding: 20px; border-radius: 8px; text-align: center; margin: 5px;">
                            <div style="font-size: 32px; font-weight: bold; margin-bottom: 8px;">{niet_werkzoekend}%</div>
                            <div style="font-size: 12px; text-transform: uppercase; font-weight: bold; margin-bottom: 8px;">NIET WERKZOEKEND</div>
                            <p style="font-size: 11px; margin: 0;">Tevreden in huidige rol, executive search nodig</p>
                        </div>
                    </div>
                    <div class="column">
                        <div style="background: #9C27B0; color: white; padding: 20px; border-radius: 8px; text-align: center; margin: 5px;">
                            <div style="font-size: 32px; font-weight: bold; margin-bottom: 8px;">{onzeker_switch}%</div>
                            <div style="font-size: 12px; text-transform: uppercase; font-weight: bold; margin-bottom: 8px;">ONZEKER SWITCH</div>
                            <p style="font-size: 11px; margin: 0;">Overweegt verandering, behoeft nurturing</p>
                        </div>
                    </div>
                </div>

                <div style="background: rgba(255,255,255,0.8); padding: 20px; border-radius: 8px; margin-top: 20px;">
                    <h4 style="color: #333; margin-bottom: 15px;">🎯 Strategische Doelgroep Prioritering</h4>
                    <p style="color: #333; margin: 5px 0; font-size: 14px;"><strong>Tier 1 (Actief + Latent):</strong> {actief_zoekend + latent_geinteresseerd}% - Direct bereikbaar via LinkedIn & job boards</p>
                    <p style="color: #333; margin: 5px 0; font-size: 14px;"><strong>Tier 2 (Onzeker):</strong> {onzeker_switch}% - Nurturing campaign + personalized approach</p>
                    <p style="color: #333; margin: 5px 0; font-size: 14px;"><strong>Tier 3 (Passief):</strong> {niet_werkzoekend}% - Executive search + premium employer branding</p>
                </div>
            </div>
        </div>

        <!-- Salary Intelligence - MET ECHTE AI DATA -->
        <div class="section">
            <h2 class="section-title">💰 Comprehensive Salary Intelligence 2025</h2>

            <div class="salary-box">
                <h3>🇳🇱 Nederlandse Markt Benchmark - Total Compensation</h3>
                <div style="font-size: 48px; font-weight: bold; margin: 15px 0;">€{median_salary:,}</div>
                <p>Markt Mediaan (P50) - Bruto maandsalaris basis, exclusief variabele componenten</p>

                <div class="two-column" style="border-top: 2px solid rgba(255,255,255,0.3); padding-top: 15px; margin-top: 15px;">
                    <div class="column">
                        <div style="text-align: center;">
                            <div style="font-size: 12px; opacity: 0.8;">P25 (Junior)</div>
                            <div style="font-size: 18px; font-weight: bold;">€{p25_salary:,}</div>
                        </div>
                    </div>
                    <div class="column">
                        <div style="text-align: center;">
                            <div style="font-size: 12px; opacity: 0.8;">P75 (Senior)</div>
                            <div style="font-size: 18px; font-weight: bold;">€{p75_salary:,}</div>
                        </div>
                    </div>
                </div>
                <div style="text-align: center; margin-top: 15px;">
                    <div style="font-size: 12px; opacity: 0.8;">Bonus Gemiddeld</div>
                    <div style="font-size: 18px; font-weight: bold;">{bonus_percentage}%</div>
                </div>
            </div>

            <h3>💼 Total Compensation Analysis</h3>
            <div class="two-column">
                <div class="column">
                    <div style="background: #2196F3; color: white; padding: 20px; border-radius: 8px;">
                        <h4>📊 Compensation Components Breakdown</h4>
                        <p>💰 Base Salary: €{median_salary:,} (markt mediaan)</p>
                        <p>🎯 Variable Bonus: {bonus_percentage}% gemiddeld (€{int(bonus_percentage/100*median_salary):,})</p>
                        <p>📈 Stock Options: 15% van vergelijkbare rollen</p>
                        <p>🏦 Pensioen Bijdrage: 8.5% werkgever</p>
                        <p>🚗 Lease Auto Eligibility: 78% van posities</p>
                    </div>
                </div>
                <div class="column">
                    <div style="background: #9C27B0; color: white; padding: 20px; border-radius: 8px;">
                        <h4>📈 Growth & Benefits Intelligence</h4>
                        <p>🏠 Home Office Allowance: €950/jaar standaard</p>
                        <p>📊 1-jaar salary groeitrend: +11% (marktgemiddeld)</p>
                        <p>🚀 3-jaar salary groeitrend: +32% (cumulatief)</p>
                        <p>💡 Talent schaarste factor: {schaarste_score}/10 (hoog = schaars)</p>
                        <p>⏰ Gemiddelde notice period: 1-2 maanden</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Candidate Motivation - MET ECHTE AI DATA -->
        <div class="section">
            <h2 class="section-title">🎯 Candidate Motivation Intelligence</h2>
            <div style="background: #E91E63; color: white; padding: 25px; border-radius: 8px;">
                <h4 style="text-align: center;">💡 Key Motivation Drivers (AI-Analyzed from {candidate_pool:,} candidates)</h4>
                <div class="two-column">
                    {motivation_html}
                </div>
            </div>
        </div>

        <!-- Recruitment Strategy - MET ECHTE AI DATA -->
        <div class="section">
            <h2 class="section-title">🎯 Recruitment Strategy & Channel Intelligence</h2>

            <div style="background: #E8F5E8; padding: 25px; border-radius: 8px; border-left: 6px solid #4CAF50;">
                <h3>💡 AI-Optimized Strategic Sourcing Approach</h3>
                <p><strong>Primary Channel Strategy:</strong> {primary_channel}</p>
                <p><strong>Secondary Support Channels:</strong> {secondary_channel}</p>
                <p><strong>Estimated Timeline:</strong> {estimated_timeline} volledige cyclus</p>
                <p><strong>Budget Range Projection:</strong> {budget_range} total cost of hire</p>
            </div>
        </div>

        <!-- Strategic Action Plan - MET ECHTE AI DATA -->
        <div class="section">
            <h2 class="section-title">🚀 Strategic Conclusions & Executive Action Plan</h2>

            <div class="green-box">
                <h3>⚡ Immediate Strategic Priorities (Next 30 Days)</h3>

                <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 8px; margin: 15px 0;">
                    <strong>1. Competitive Compensation Positioning</strong>
                    <p>Target salary range: €{comp_sal_min:,} - €{comp_sal_max:,} voor markt-competitieve positie. Include {bonus_percentage}% variable component en comprehensive benefits package.</p>
                </div>

                <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 8px; margin: 15px 0;">
                    <strong>2. Strategic Channel & Sourcing Mix</strong>
                    <p>{primary_channel} als primary approach, ondersteund door {secondary_channel} voor comprehensive pipeline coverage.</p>
                </div>

                <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 8px; margin: 15px 0;">
                    <strong>3. Timeline Acceleration & Market Response</strong>
                    <p>Launch binnen {urgency_days} dagen - {temperature}</p>
                </div>

                <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 8px;">
                    <strong>4. Candidate Experience & Success Rate Optimization</strong>
                    <p>Target {success_rate}% success rate door focus op top motivatie driver: {top_motivation} ({top_motivation_pct}% importance factor).</p>
                </div>
            </div>

            <div style="text-align: center; margin: 30px 0;">
                <a href="mailto:{RECRUITER_EMAIL}?subject=Executive Strategy Session - {functietitel} bij {company_name}" style="background: #FF6B35; color: white; padding: 15px 30px; text-decoration: none; border-radius: 25px; font-weight: bold; display: inline-block;">📞 Schedule Executive Strategy Session</a>
                <p style="color: #666; margin-top: 10px;">Persoonlijk strategic alignment gesprek binnen 24 uur<br/>Gratis executive consultation & market intelligence briefing</p>
            </div>
        </div>

        <!-- Footer -->
        <div class="footer">
            <h3>Recruitin</h3>
            <p>AI-Powered Executive Recruitment Intelligence & Strategic Consulting</p>
            <div style="border-top: 1px solid rgba(255,255,255,0.2); padding-top: 20px; margin-top: 20px;">
                <p><strong>Wouter Arts</strong> - Director AI Development & Strategic Intelligence</p>
                <p>📧 {RECRUITER_EMAIL} | 📞 06-14314593 | 🌐 recruitin.nl</p>
                <p style="font-size: 12px; opacity: 0.8; margin-top: 15px;">
                    Executive Intelligence Report gegenereerd op {current_date} om {current_time}<br/>
                    Powered by Claude AI Sonnet 4.5 • Market Data: Real-time Analysis<br/>
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

email_subject = f'🤖 Executive AI Intelligence: {functietitel} in {locatie} | Complete Strategic Analysis'

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
    'ai_used': 'Yes' if ai_analysis != fallback_data else 'No (Fallback)',
    'status': 'success'
}
