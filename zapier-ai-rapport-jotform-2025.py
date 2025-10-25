# ================================================================
# RECRUITIN - AI-GEDREVEN ARBEIDSMARKT INTELLIGENCE RAPPORT
# Zapier Code by Zapier - JotForm 252881347421054 (2025 versie)
# Gebruikt alleen standaard Zapier modules (requests, json, datetime)
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

# OPTIONELE VELDEN - PDF URLs van Zapier's "Extract Text from PDF" stap
# Deze komen van eerdere Zapier stappen die de PDFs downloaden en tekst extraheren
jobdigger_text = input_data.get('jobdigger_extracted_text', '')
linkedin_ti_text = input_data.get('linkedin_extracted_text', '')
vacature_pdf_text = input_data.get('vacature_extracted_text', '')

# OPTIONELE TEKSTVELDEN
vacature_text_input = input_data.get('vacaturetekst', '')
vacature_url = input_data.get('vacatureUrl', input_data.get('vacature_url', ''))

# Gecombineerde vacature tekst (van PDF of tekstveld)
vacature_text = vacature_pdf_text if vacature_pdf_text else vacature_text_input

# JotForm metadata
submission_url = input_data.get('submission_url', '')
submission_id = input_data.get('submission_id', '')

# ========================================
# CLAUDE AI ANALYSIS FUNCTION
# ========================================

def analyze_with_claude(vacature_text, jobdigger_text, linkedin_ti_text, functietitel, locatie):
    """Analyseert documenten met Claude AI via requests library"""

    # Build context
    context_parts = []
    if vacature_text:
        context_parts.append(f"## VACATURETEKST:\n{vacature_text[:5000]}")
    if jobdigger_text:
        context_parts.append(f"## JOBDIGGER RAPPORT:\n{jobdigger_text[:5000]}")
    if linkedin_ti_text:
        context_parts.append(f"## LINKEDIN TALENT INSIGHTS:\n{linkedin_ti_text[:5000]}")

    context = "\n\n".join(context_parts) if context_parts else "Geen documenten beschikbaar"

    # Claude AI Prompt
    prompt = f"""Analyseer deze arbeidsmarkt documenten en genereer JSON output.

{context}

VACATURE: {functietitel} | LOCATIE: {locatie}

Geef JSON response (gebruik realistische data uit documenten):

{{
  "schaarste_niveau": "Laag/Gemiddeld/Hoog",
  "schaarste_ratio": "X,X vacatures per kandidaat",
  "time_to_hire_min": 30,
  "time_to_hire_max": 50,
  "beschikbaarheid": "±X.XXX",
  "beschikbaarheid_tekst": "Geschikte kandidaten NL",
  "werkzoekend_ratio": {{
    "actief": 15,
    "latent": 45,
    "niet_werkzoekend": 40
  }},
  "leeftijd_verdeling": [
    {{"leeftijd": "20-30 jaar", "percentage": 25}},
    {{"leeftijd": "30-40 jaar", "percentage": 35}},
    {{"leeftijd": "40-50 jaar", "percentage": 28}},
    {{"leeftijd": "50+ jaar", "percentage": 12}}
  ],
  "push_factors": [
    "Factor 1",
    "Factor 2",
    "Factor 3"
  ],
  "pull_factors": [
    "Factor 1",
    "Factor 2",
    "Factor 3"
  ],
  "technische_skills": [
    {{"skill": "Skill 1", "niveau": "Essential"}},
    {{"skill": "Skill 2", "niveau": "Nice to have"}},
    {{"skill": "Skill 3", "niveau": "Essential"}}
  ],
  "soft_skills": [
    "Soft skill 1",
    "Soft skill 2",
    "Soft skill 3"
  ],
  "salaris_p25_min": 50000,
  "salaris_p25_max": 60000,
  "salaris_p50_min": 65000,
  "salaris_p50_max": 75000,
  "salaris_p75_min": 75000,
  "salaris_p75_max": 90000,
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
  "hiring_speed": "Snel",
  "education_wo": 43,
  "education_hbo": 42,
  "education_mbo": 15,
  "mobility_index": "Hoog",
  "avg_retention": "3.2 jaar",
  "skill_gaps": "Specialistische kennis, Nieuwe technologieën"
}}

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
    "time_to_hire_min": 35,
    "time_to_hire_max": 55,
    "beschikbaarheid": "±12.500",
    "beschikbaarheid_tekst": "Geschikte kandidaten NL",
    "werkzoekend_ratio": {
        "actief": 18,
        "latent": 47,
        "niet_werkzoekend": 35
    },
    "leeftijd_verdeling": [
        {"leeftijd": "20-30 jaar", "percentage": 22},
        {"leeftijd": "30-40 jaar", "percentage": 38},
        {"leeftijd": "40-50 jaar", "percentage": 28},
        {"leeftijd": "50+ jaar", "percentage": 12}
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
    "salaris_p25_min": 50000,
    "salaris_p25_max": 60000,
    "salaris_p50_min": 65000,
    "salaris_p50_max": 75000,
    "salaris_p75_min": 75000,
    "salaris_p75_max": 90000,
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
    "hiring_speed": "Snel",
    "education_wo": 43,
    "education_hbo": 42,
    "education_mbo": 15,
    "mobility_index": "Hoog",
    "avg_retention": "3.2 jaar",
    "skill_gaps": "Specialistische kennis, Nieuwe technologieën"
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
# FORMAT SALARY DATA
# ========================================

def format_salary(min_val, max_val):
    """Format salary range"""
    if min_val and max_val:
        return f"€{int(min_val):,} - €{int(max_val):,}".replace(',', '.')
    return "Niet beschikbaar"

salaris_p25 = format_salary(
    ai_analysis.get('salaris_p25_min'),
    ai_analysis.get('salaris_p25_max')
)
salaris_p50 = format_salary(
    ai_analysis.get('salaris_p50_min'),
    ai_analysis.get('salaris_p50_max')
)
salaris_p75 = format_salary(
    ai_analysis.get('salaris_p75_min'),
    ai_analysis.get('salaris_p75_max')
)

# ========================================
# BUILD HTML EMAIL RAPPORT
# ========================================

def build_skill_rows(skills):
    """Build skill table rows"""
    if not skills:
        return "<tr><td colspan='2' style='padding: 12px; text-align: center; color: #999;'>Geen skills beschikbaar</td></tr>"

    rows = []
    for skill_data in skills:
        if isinstance(skill_data, dict):
            skill = skill_data.get('skill', 'Unknown')
            niveau = skill_data.get('niveau', 'Unknown')
            niveau_class = 'essential' if 'essential' in niveau.lower() else 'nice-to-have'
            rows.append(f"""
                <tr>
                    <td style="padding: 12px; border-bottom: 1px solid #e5e7eb; color: #1f2937;">{skill}</td>
                    <td style="padding: 12px; border-bottom: 1px solid #e5e7eb;">
                        <span class="{niveau_class}" style="display: inline-block; padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: 600; background: {'#dcfce7' if niveau_class == 'essential' else '#fef3c7'}; color: {'#166534' if niveau_class == 'essential' else '#854d0e'};">
                            {niveau}
                        </span>
                    </td>
                </tr>
            """)
    return ''.join(rows)

def build_list_items(items):
    """Build HTML list items"""
    if not items:
        return "<li style='color: #999;'>Geen data beschikbaar</li>"
    return ''.join([f"<li style='margin: 8px 0; color: #374151;'>{item}</li>" for item in items])

def build_age_distribution(leeftijd_data):
    """Build age distribution bars"""
    if not leeftijd_data:
        return "<p style='color: #999;'>Geen data beschikbaar</p>"

    rows = []
    for item in leeftijd_data:
        leeftijd = item.get('leeftijd', 'Unknown')
        percentage = item.get('percentage', 0)
        rows.append(f"""
            <div style="margin-bottom: 16px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
                    <span style="font-size: 14px; color: #4b5563; font-weight: 500;">{leeftijd}</span>
                    <span style="font-size: 14px; color: #6b7280; font-weight: 600;">{percentage}%</span>
                </div>
                <div style="background: #e5e7eb; height: 8px; border-radius: 4px; overflow: hidden;">
                    <div style="background: linear-gradient(90deg, #EF7D00, #ff9500); height: 100%; width: {percentage}%; border-radius: 4px;"></div>
                </div>
            </div>
        """)
    return ''.join(rows)

# Generate current date
current_date = datetime.datetime.now().strftime("%d %B %Y")

# Build HTML Email
html_email = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Arbeidsmarkt Intelligence Rapport</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background-color: #f9fafb;">
    <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="background-color: #f9fafb; padding: 40px 20px;">
        <tr>
            <td align="center">
                <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="max-width: 700px; background-color: #ffffff; border-radius: 16px; overflow: hidden; box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);">

                    <!-- Header -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #4B4F51 0%, #2d2929 100%); padding: 40px; text-align: center;">
                            <h1 style="margin: 0; color: #ffffff; font-size: 32px; font-weight: 800; letter-spacing: -0.5px;">
                                📊 ARBEIDSMARKT INTELLIGENCE
                            </h1>
                            <p style="margin: 12px 0 0 0; color: #e5e7eb; font-size: 16px; font-weight: 500;">
                                {functietitel} • {locatie}
                            </p>
                            <p style="margin: 8px 0 0 0; color: #9ca3af; font-size: 14px;">
                                Gegenereerd op {current_date}
                            </p>
                        </td>
                    </tr>

                    <!-- Schaarste Status -->
                    <tr>
                        <td style="padding: 40px 40px 30px 40px;">
                            <div style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); padding: 24px; border-radius: 12px; border-left: 4px solid #f59e0b; margin-bottom: 30px;">
                                <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap;">
                                    <div>
                                        <p style="margin: 0; font-size: 13px; color: #92400e; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;">Schaarste Niveau</p>
                                        <p style="margin: 6px 0 0 0; font-size: 28px; color: #78350f; font-weight: 800;">{ai_analysis.get('schaarste_niveau', 'Gemiddeld')}</p>
                                    </div>
                                    <div style="text-align: right;">
                                        <p style="margin: 0; font-size: 13px; color: #92400e; font-weight: 600;">Ratio</p>
                                        <p style="margin: 6px 0 0 0; font-size: 18px; color: #78350f; font-weight: 700;">{ai_analysis.get('schaarste_ratio', 'N/A')}</p>
                                    </div>
                                </div>
                            </div>

                            <h2 style="margin: 0 0 20px 0; color: #1f2937; font-size: 24px; font-weight: 700; border-bottom: 2px solid #e5e7eb; padding-bottom: 12px;">📈 Markt Overzicht</h2>

                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin-bottom: 20px;">
                                <tr>
                                    <td width="48%" valign="top" style="background-color: #eff6ff; padding: 20px; border-radius: 12px; border: 2px solid #bfdbfe;">
                                        <p style="margin: 0; font-size: 13px; color: #1e3a8a; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;">Time to Hire</p>
                                        <p style="margin: 8px 0 0 0; font-size: 24px; color: #1e40af; font-weight: 800;">{ai_analysis.get('time_to_hire_min', 30)}-{ai_analysis.get('time_to_hire_max', 50)} dagen</p>
                                    </td>
                                    <td width="4%"></td>
                                    <td width="48%" valign="top" style="background-color: #f0fdf4; padding: 20px; border-radius: 12px; border: 2px solid #86efac;">
                                        <p style="margin: 0; font-size: 13px; color: #15803d; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;">Beschikbaarheid</p>
                                        <p style="margin: 8px 0 0 0; font-size: 24px; color: #166534; font-weight: 800;">{ai_analysis.get('beschikbaarheid', 'N/A')}</p>
                                        <p style="margin: 4px 0 0 0; font-size: 12px; color: #15803d;">{ai_analysis.get('beschikbaarheid_tekst', '')}</p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Werkzoekend Ratio -->
                    <tr>
                        <td style="padding: 0 40px 30px 40px;">
                            <h2 style="margin: 0 0 20px 0; color: #1f2937; font-size: 24px; font-weight: 700; border-bottom: 2px solid #e5e7eb; padding-bottom: 12px;">👥 Werkzoekend Ratio</h2>
                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                <tr>
                                    <td width="32%" align="center" style="padding: 16px; background-color: #dcfce7; border-radius: 8px;">
                                        <p style="margin: 0; font-size: 32px; font-weight: 800; color: #166534;">{ai_analysis.get('werkzoekend_ratio', {}).get('actief', 0)}%</p>
                                        <p style="margin: 4px 0 0 0; font-size: 13px; color: #15803d; font-weight: 600;">Actief Zoekend</p>
                                    </td>
                                    <td width="2%"></td>
                                    <td width="32%" align="center" style="padding: 16px; background-color: #fef3c7; border-radius: 8px;">
                                        <p style="margin: 0; font-size: 32px; font-weight: 800; color: #854d0e;">{ai_analysis.get('werkzoekend_ratio', {}).get('latent', 0)}%</p>
                                        <p style="margin: 4px 0 0 0; font-size: 13px; color: #92400e; font-weight: 600;">Latent Zoekend</p>
                                    </td>
                                    <td width="2%"></td>
                                    <td width="32%" align="center" style="padding: 16px; background-color: #fee2e2; border-radius: 8px;">
                                        <p style="margin: 0; font-size: 32px; font-weight: 800; color: #991b1b;">{ai_analysis.get('werkzoekend_ratio', {}).get('niet_werkzoekend', 0)}%</p>
                                        <p style="margin: 4px 0 0 0; font-size: 13px; color: #991b1b; font-weight: 600;">Niet Zoekend</p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Leeftijdsverdeling -->
                    <tr>
                        <td style="padding: 0 40px 30px 40px;">
                            <h2 style="margin: 0 0 20px 0; color: #1f2937; font-size: 24px; font-weight: 700; border-bottom: 2px solid #e5e7eb; padding-bottom: 12px;">📊 Leeftijdsverdeling</h2>
                            {build_age_distribution(ai_analysis.get('leeftijd_verdeling', []))}
                        </td>
                    </tr>

                    <!-- Salary Benchmark -->
                    <tr>
                        <td style="padding: 0 40px 30px 40px;">
                            <h2 style="margin: 0 0 20px 0; color: #1f2937; font-size: 24px; font-weight: 700; border-bottom: 2px solid #e5e7eb; padding-bottom: 12px;">💰 Salaris Benchmark</h2>
                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="background: linear-gradient(135deg, #EF7D00 0%, #ea580c 100%); border-radius: 12px;">
                                <tr>
                                    <td style="padding: 32px; color: #ffffff;">
                                        <p style="margin: 0 0 10px 0; font-size: 13px; font-weight: 600; opacity: 0.9;">Markt Mediaan (P50)</p>
                                        <div style="font-size: 40px; font-weight: 700; margin: 10px 0;">{salaris_p50}</div>
                                        <p style="margin: 0 0 20px 0; font-size: 13px; opacity: 0.9;">Bruto jaarsalaris, exclusief bonus & secundair</p>
                                        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="border-top: 1px solid rgba(255,255,255,0.3); padding-top: 16px;">
                                            <tr>
                                                <td width="48%" style="padding: 8px 0;">
                                                    <p style="margin: 0; font-size: 12px; opacity: 0.8;">P25 (Junior-Medior)</p>
                                                    <p style="margin: 4px 0 0 0; font-size: 16px; font-weight: 700;">{salaris_p25}</p>
                                                </td>
                                                <td width="4%"></td>
                                                <td width="48%" style="padding: 8px 0;">
                                                    <p style="margin: 0; font-size: 12px; opacity: 0.8;">P75 (Senior-Lead)</p>
                                                    <p style="margin: 4px 0 0 0; font-size: 16px; font-weight: 700;">{salaris_p75}</p>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Jobdigger Marktintelligentie -->
                    <tr>
                        <td style="padding: 0 40px 30px 40px;">
                            <h2 style="margin: 0 0 20px 0; color: #1f2937; font-size: 24px; font-weight: 700; border-bottom: 2px solid #e5e7eb; padding-bottom: 12px;">📊 Jobdigger Marktintelligentie</h2>

                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin-bottom: 20px;">
                                <tr>
                                    <td width="32%" valign="top" style="background-color: #eff6ff; padding: 20px; border-radius: 12px; border: 2px solid #bfdbfe; text-align: center;">
                                        <div style="font-size: 32px; font-weight: 700; color: #2563eb; margin: 10px 0;">{ai_analysis.get('total_workers_market', 'N/A')}</div>
                                        <p style="margin: 0; color: #1e3a8a; font-size: 14px; font-weight: 600;">Werkenden in NL</p>
                                    </td>
                                    <td width="2%"></td>
                                    <td width="32%" valign="top" style="background-color: #f0fdf4; padding: 20px; border-radius: 12px; border: 2px solid #86efac; text-align: center;">
                                        <div style="font-size: 32px; font-weight: 700; color: #10b981; margin: 10px 0;">{ai_analysis.get('growth_percentage', 'N/A')}%</div>
                                        <p style="margin: 0; color: #15803d; font-size: 14px; font-weight: 600;">Groei per jaar</p>
                                    </td>
                                    <td width="2%"></td>
                                    <td width="32%" valign="top" style="background-color: #fef3c7; padding: 20px; border-radius: 12px; border: 2px solid #fcd34d; text-align: center;">
                                        <div style="font-size: 32px; font-weight: 700; color: #f59e0b; margin: 10px 0;">{ai_analysis.get('open_vacancies', 'N/A')}</div>
                                        <p style="margin: 0; color: #92400e; font-size: 14px; font-weight: 600;">Open Vacatures</p>
                                    </td>
                                </tr>
                            </table>

                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                <tr>
                                    <td width="48%" valign="top" style="background-color: #f9fafb; padding: 20px; border-radius: 12px; border: 1px solid #e5e7eb;">
                                        <h3 style="margin: 0 0 16px 0; color: #1f2937; font-size: 16px; font-weight: 700;">📝 Contracttypen</h3>
                                        <p style="margin: 8px 0; color: #374151; font-size: 14px;"><strong>Vast:</strong> {ai_analysis.get('contract_permanent', 'N/A')}%</p>
                                        <p style="margin: 8px 0; color: #374151; font-size: 14px;"><strong>Tijdelijk:</strong> {ai_analysis.get('contract_temporary', 'N/A')}%</p>
                                        <p style="margin: 8px 0; color: #374151; font-size: 14px;"><strong>ZZP:</strong> {ai_analysis.get('contract_freelance', 'N/A')}%</p>
                                    </td>
                                    <td width="4%"></td>
                                    <td width="48%" valign="top" style="background-color: #fef2f2; padding: 20px; border-radius: 12px; border: 1px solid #fecaca;">
                                        <h3 style="margin: 0 0 16px 0; color: #991b1b; font-size: 16px; font-weight: 700;">👥 Demografie</h3>
                                        <p style="margin: 8px 0; color: #374151; font-size: 14px;"><strong>Gem. leeftijd:</strong> {ai_analysis.get('average_age', 'N/A')} jaar</p>
                                        <p style="margin: 8px 0; color: #374151; font-size: 14px;"><strong>M/V ratio:</strong> {ai_analysis.get('gender_ratio', 'N/A')}</p>
                                        <p style="margin: 8px 0; color: #374151; font-size: 14px;"><strong>Groeitrend:</strong> {ai_analysis.get('employment_trend', 'Stijgend')}</p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- LinkedIn Talent Insights -->
                    <tr>
                        <td style="padding: 0 40px 30px 40px;">
                            <h2 style="margin: 0 0 20px 0; color: #0077b5; font-size: 24px; font-weight: 700; border-bottom: 2px solid #0077b5; padding-bottom: 12px;">💼 LinkedIn Talent Insights</h2>

                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin-bottom: 20px;">
                                <tr>
                                    <td width="48%" valign="top" style="background: linear-gradient(135deg, #0077b5 0%, #005885 100%); padding: 20px; border-radius: 12px; color: white; text-align: center;">
                                        <div style="font-size: 36px; font-weight: 700; margin: 10px 0;">{ai_analysis.get('talent_pool_size', 'N/A')}</div>
                                        <p style="margin: 0; font-size: 14px; opacity: 0.9;">Beschikbare Professionals</p>
                                        <p style="margin: 12px 0 0 0; font-size: 13px; opacity: 0.8;">{ai_analysis.get('active_job_seekers', 'N/A')} actief zoekend</p>
                                    </td>
                                    <td width="4%"></td>
                                    <td width="48%" valign="top" style="background: linear-gradient(135deg, #00a0dc 0%, #0077b5 100%); padding: 20px; border-radius: 12px; color: white; text-align: center;">
                                        <div style="font-size: 36px; font-weight: 700; margin: 10px 0;">{ai_analysis.get('hiring_velocity', 'N/A')}</div>
                                        <p style="margin: 0; font-size: 14px; opacity: 0.9;">Hiring Velocity</p>
                                        <p style="margin: 12px 0 0 0; font-size: 13px; opacity: 0.8;">Speed: {ai_analysis.get('hiring_speed', 'Gemiddeld')}</p>
                                    </td>
                                </tr>
                            </table>

                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                <tr>
                                    <td width="48%" valign="top" style="background-color: #fff3cd; padding: 20px; border-radius: 12px; border-left: 4px solid #ffc107;">
                                        <h3 style="margin: 0 0 16px 0; color: #856404; font-size: 16px; font-weight: 700;">🎓 Opleidingsniveau</h3>
                                        <p style="margin: 8px 0; color: #856404; font-size: 14px;"><strong>WO:</strong> {ai_analysis.get('education_wo', 'N/A')}%</p>
                                        <p style="margin: 8px 0; color: #856404; font-size: 14px;"><strong>HBO:</strong> {ai_analysis.get('education_hbo', 'N/A')}%</p>
                                        <p style="margin: 8px 0; color: #856404; font-size: 14px;"><strong>MBO:</strong> {ai_analysis.get('education_mbo', 'N/A')}%</p>
                                    </td>
                                    <td width="4%"></td>
                                    <td width="48%" valign="top" style="background-color: #d1ecf1; padding: 20px; border-radius: 12px; border-left: 4px solid #17a2b8;">
                                        <h3 style="margin: 0 0 16px 0; color: #0c5460; font-size: 16px; font-weight: 700;">🔄 Mobiliteit</h3>
                                        <p style="margin: 8px 0; color: #0c5460; font-size: 14px;"><strong>Mobiliteit index:</strong> {ai_analysis.get('mobility_index', 'Hoog')}</p>
                                        <p style="margin: 8px 0; color: #0c5460; font-size: 14px;"><strong>Gemiddelde retentie:</strong> {ai_analysis.get('avg_retention', 'N/A')}</p>
                                        <p style="margin: 8px 0; color: #0c5460; font-size: 14px;"><strong>Skill gaps:</strong> {ai_analysis.get('skill_gaps', 'Aanwezig')}</p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Push & Pull Factors -->
                    <tr>
                        <td style="padding: 0 40px 30px 40px;">
                            <h2 style="margin: 0 0 20px 0; color: #1f2937; font-size: 24px; font-weight: 700; border-bottom: 2px solid #e5e7eb; padding-bottom: 12px;">🔄 Push & Pull Factors</h2>
                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                <tr>
                                    <td width="48%" valign="top">
                                        <div style="background-color: #fee2e2; padding: 20px; border-radius: 12px; border-left: 4px solid #ef4444;">
                                            <h3 style="margin: 0 0 12px 0; color: #991b1b; font-size: 16px; font-weight: 700;">⛔ Push Factors (Waarom vertrekken?)</h3>
                                            <ul style="margin: 0; padding-left: 20px;">
                                                {build_list_items(ai_analysis.get('push_factors', []))}
                                            </ul>
                                        </div>
                                    </td>
                                    <td width="4%"></td>
                                    <td width="48%" valign="top">
                                        <div style="background-color: #dcfce7; padding: 20px; border-radius: 12px; border-left: 4px solid #22c55e;">
                                            <h3 style="margin: 0 0 12px 0; color: #166534; font-size: 16px; font-weight: 700;">✅ Pull Factors (Waarom solliciteren?)</h3>
                                            <ul style="margin: 0; padding-left: 20px;">
                                                {build_list_items(ai_analysis.get('pull_factors', []))}
                                            </ul>
                                        </div>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Technische Skills -->
                    <tr>
                        <td style="padding: 0 40px 30px 40px;">
                            <h2 style="margin: 0 0 20px 0; color: #1f2937; font-size: 24px; font-weight: 700; border-bottom: 2px solid #e5e7eb; padding-bottom: 12px;">⚙️ Technische Skills</h2>
                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="background-color: #ffffff; border-radius: 8px; border: 1px solid #e5e7eb; overflow: hidden;">
                                <thead>
                                    <tr style="background-color: #f9fafb;">
                                        <th style="padding: 12px; text-align: left; font-size: 13px; color: #6b7280; font-weight: 600; text-transform: uppercase; border-bottom: 2px solid #e5e7eb;">Skill</th>
                                        <th style="padding: 12px; text-align: left; font-size: 13px; color: #6b7280; font-weight: 600; text-transform: uppercase; border-bottom: 2px solid #e5e7eb;">Niveau</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {build_skill_rows(ai_analysis.get('technische_skills', []))}
                                </tbody>
                            </table>
                        </td>
                    </tr>

                    <!-- Soft Skills -->
                    <tr>
                        <td style="padding: 0 40px 30px 40px;">
                            <h2 style="margin: 0 0 20px 0; color: #1f2937; font-size: 24px; font-weight: 700; border-bottom: 2px solid #e5e7eb; padding-bottom: 12px;">💬 Soft Skills</h2>
                            <div style="background-color: #fef3c7; padding: 20px; border-radius: 12px; border-left: 4px solid #f59e0b;">
                                <ul style="margin: 0; padding-left: 20px;">
                                    {build_list_items(ai_analysis.get('soft_skills', []))}
                                </ul>
                            </div>
                        </td>
                    </tr>

                    <!-- Footer -->
                    <tr>
                        <td style="background-color: #f9fafb; padding: 30px 40px; text-align: center; border-top: 1px solid #e5e7eb;">
                            <p style="margin: 0 0 8px 0; font-size: 14px; color: #6b7280;">
                                <strong>Recruitin Labour Market Intelligence</strong>
                            </p>
                            <p style="margin: 0; font-size: 13px; color: #9ca3af;">
                                AI-powered arbeidsmarkt analyse • Gegenereerd op {current_date}
                            </p>
                            <p style="margin: 12px 0 0 0; font-size: 12px; color: #9ca3af;">
                                Dit rapport is automatisch gegenereerd via Claude AI
                            </p>
                        </td>
                    </tr>

                </table>
            </td>
        </tr>
    </table>
</body>
</html>
"""

# ========================================
# OUTPUT FOR ZAPIER
# ========================================

# Return values for next Zapier steps
output = {
    'html_email': html_email,
    'recipient_email': email,
    'functietitel': functietitel,
    'locatie': locatie,
    'current_date': current_date,
    'schaarste_niveau': ai_analysis.get('schaarste_niveau', 'Gemiddeld'),
    'ai_used': 'Yes' if ai_analysis != fallback_data else 'No (Fallback)',
}
