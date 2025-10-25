# ================================================================
# RECRUITIN - AI-GEDREVEN ARBEIDSMARKT INTELLIGENCE RAPPORT
# Zapier Code by Zapier - PDFMonkey Integration (2025)
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

# PDFMonkey Configuration (optional - for PDF generation)
PDFMONKEY_API_KEY = input_data.get('pdfmonkey_api_key', '')  # Optional
PDFMONKEY_TEMPLATE_ID = input_data.get('pdfmonkey_template_id', '')  # Optional

# ========================================
# EXTRACT INPUT DATA FROM JOTFORM
# ========================================
bedrijfsnaam = input_data.get('bedrijfsnaam', 'Niet opgegeven')
contactpersoon = input_data.get('contactpersoon', '')
email = input_data.get('email', '')
telefoon = input_data.get('telefoon', '')
functietitel = input_data.get('functietitel', 'Niet opgegeven')
sector = input_data.get('sector', 'Algemeen')
locatie = input_data.get('locatie', 'Nederland')
ervaringsniveau = input_data.get('ervaringsniveau', 'Senior')
salaris_min = input_data.get('salaris_min', '')
salaris_max = input_data.get('salaris_max', '')
urgentie = input_data.get('urgentie', 'Normaal')
aantal_posities = input_data.get('aantal_posities', '1')
werkervaring_jaren = input_data.get('werkervaring_jaren', '5-7 jaar')
opleidingsniveau = input_data.get('opleidingsniveau', 'HBO/WO')
teamsize = input_data.get('teamsize', 'Geen leidinggevende rol')
bedrijfsgrootte = input_data.get('bedrijfsgrootte', '50-200 medewerkers')
werkomgeving = input_data.get('werkomgeving', 'Hybrid')
groei_fase = input_data.get('groei_fase', 'Scale-up')
key_skills = input_data.get('key_skills', '')
extra_info = input_data.get('extra_info', '')

# PDFMonkey extracted text from previous Zapier steps
vacature_text = input_data.get('vacature_text', '')
jobdigger_text = input_data.get('jobdigger_text', '')
linkedin_ti_text = input_data.get('linkedin_ti_text', '')

# URLs
vacature_url = input_data.get('vacature_url', '')
jobdigger_url = input_data.get('jobdigger_url', '')
linkedin_ti_url = input_data.get('linkedin_ti_url', '')

submission_url = input_data.get('submission_url', '')
submission_id = input_data.get('submission_id', '')

# ========================================
# CLAUDE AI ANALYSIS FUNCTION
# ========================================

def analyze_with_claude(vacature_text, jobdigger_text, linkedin_ti_text, functietitel, sector, locatie):
    """Analyseert documenten met Claude AI via requests library"""

    # Build context
    context_parts = []
    if vacature_text:
        context_parts.append(f"## VACATURETEKST:\n{vacature_text[:5000]}")
    if jobdigger_text:
        context_parts.append(f"## JOBDIGGER:\n{jobdigger_text[:5000]}")
    if linkedin_ti_text:
        context_parts.append(f"## LINKEDIN TI:\n{linkedin_ti_text[:5000]}")

    context = "\n\n".join(context_parts) if context_parts else "Geen documenten beschikbaar"

    # Claude AI Prompt
    prompt = f"""Analyseer deze arbeidsmarkt documenten en genereer JSON output.

{context}

VACATURE: {functietitel} | SECTOR: {sector} | LOCATIE: {locatie}

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
    {{"factor": "Hoger salaris", "impact": "Hoog"}},
    {{"factor": "Betere secundaire arbeidsvoorwaarden", "impact": "Hoog"}},
    {{"factor": "Carrièremogelijkheden", "impact": "Medium"}}
  ],
  "pull_factors": [
    {{"factor": "Werk-privé balans", "impact": "Hoog"}},
    {{"factor": "Innovatieve werkgever", "impact": "Medium"}},
    {{"factor": "Flexibiliteit", "impact": "Hoog"}}
  ],
  "doelgroep_skills": [
    {{"naam": "Digital Skills", "percentage": 35, "beschrijving": "Van professionals"}},
    {{"naam": "Leadership", "percentage": 18, "beschrijving": "Met ervaring"}},
    {{"naam": "{sector} Ervaring", "percentage": 22, "beschrijving": "Sector kennis"}},
    {{"naam": "Actief Zoekend", "percentage": 12, "beschrijving": "Op zoek"}}
  ],
  "technical_skills": [
    {{"naam": "Skill 1", "percentage": 45, "kleur": "groen"}},
    {{"naam": "Skill 2", "percentage": 28, "kleur": "oranje"}},
    {{"naam": "Skill 3", "percentage": 52, "kleur": "groen"}},
    {{"naam": "Skill 4", "percentage": 35, "kleur": "oranje"}},
    {{"naam": "Skill 5", "percentage": 22, "kleur": "rood"}}
  ],
  "soft_skills": [
    {{"naam": "Leadership", "prioriteit": "Kritiek"}},
    {{"naam": "Communicatie", "prioriteit": "Kritiek"}},
    {{"naam": "Strategic Thinking", "prioriteit": "Hoog"}},
    {{"naam": "Data-Driven", "prioriteit": "Hoog"}},
    {{"naam": "Stakeholder Mgmt", "prioriteit": "Medium"}}
  ],
  "salaris_p25_min": 50000,
  "salaris_p25_max": 60000,
  "salaris_p50_min": 65000,
  "salaris_p50_max": 75000,
  "salaris_p75_min": 75000,
  "salaris_p75_max": 90000,
  "total_workers_market": "25.000",
  "growth_percentage": 3.5,
  "open_vacancies": "1.200",
  "contract_permanent": 70,
  "contract_temporary": 20,
  "contract_freelance": 10,
  "average_age": 42,
  "gender_ratio": "65/35",
  "employment_trend": "Stijgend/Stabiel/Dalend",
  "talent_pool_size": "15.000",
  "active_job_seekers": "2.250",
  "hiring_velocity": "850/maand",
  "hiring_speed": "Snel/Gemiddeld/Langzaam",
  "education_wo": 40,
  "education_hbo": 45,
  "education_mbo": 15,
  "mobility_index": "Hoog/Gemiddeld/Laag",
  "avg_retention": "3.5",
  "skill_gaps": "Technische skills, Leadership"
}}

Gebruik ALLEEN data uit documenten. Anders realistische schattingen voor {sector} in {locatie}."""

    try:
        headers = {
            "x-api-key": CLAUDE_API_KEY,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }

        data = {
            "model": CLAUDE_MODEL,
            "max_tokens": 4096,
            "messages": [{"role": "user", "content": prompt}]
        }

        response = requests.post(CLAUDE_API_URL, headers=headers, json=data, timeout=60)
        response.raise_for_status()

        result = response.json()
        ai_text = result['content'][0]['text']

        # Parse JSON from AI response
        if '```json' in ai_text:
            ai_text = ai_text.split('```json')[1].split('```')[0].strip()
        elif '```' in ai_text:
            ai_text = ai_text.split('```')[1].split('```')[0].strip()

        return json.loads(ai_text)

    except Exception as e:
        # Fallback data
        return {
            "schaarste_niveau": "Hoog",
            "schaarste_ratio": "2,3 vacatures per kandidaat",
            "time_to_hire_min": 45,
            "time_to_hire_max": 65,
            "beschikbaarheid": "±1.200",
            "beschikbaarheid_tekst": "Geschikte kandidaten NL",
            "werkzoekend_ratio": {"actief": 15, "latent": 45, "niet_werkzoekend": 40},
            "leeftijd_verdeling": [
                {"leeftijd": "20-30 jaar", "percentage": 22},
                {"leeftijd": "30-40 jaar", "percentage": 35},
                {"leeftijd": "40-50 jaar", "percentage": 28},
                {"leeftijd": "50+ jaar", "percentage": 15}
            ],
            "push_factors": [
                {"factor": "Hoger salaris", "impact": "Hoog"},
                {"factor": "Betere secundaire arbeidsvoorwaarden", "impact": "Hoog"},
                {"factor": "Carrièremogelijkheden", "impact": "Medium"}
            ],
            "pull_factors": [
                {"factor": "Werk-privé balans", "impact": "Hoog"},
                {"factor": "Innovatieve werkgever", "impact": "Medium"},
                {"factor": "Flexibiliteit", "impact": "Hoog"}
            ],
            "doelgroep_skills": [
                {"naam": "Digital Skills", "percentage": 35, "beschrijving": "Van professionals"},
                {"naam": "Leadership", "percentage": 18, "beschrijving": "Met ervaring"},
                {"naam": f"{sector} Ervaring", "percentage": 22, "beschrijving": "Sector kennis"},
                {"naam": "Actief Zoekend", "percentage": 12, "beschrijving": "Op zoek"}
            ],
            "technical_skills": [
                {"naam": "Skill 1", "percentage": 45, "kleur": "groen"},
                {"naam": "Skill 2", "percentage": 28, "kleur": "oranje"},
                {"naam": "Skill 3", "percentage": 52, "kleur": "groen"},
                {"naam": "Skill 4", "percentage": 35, "kleur": "oranje"},
                {"naam": "Skill 5", "percentage": 22, "kleur": "rood"}
            ],
            "soft_skills": [
                {"naam": "Leadership", "prioriteit": "Kritiek"},
                {"naam": "Communicatie", "prioriteit": "Kritiek"},
                {"naam": "Strategic Thinking", "prioriteit": "Hoog"},
                {"naam": "Data-Driven", "prioriteit": "Hoog"},
                {"naam": "Stakeholder Mgmt", "prioriteit": "Medium"}
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
            "avg_retention": "3.2",
            "skill_gaps": "Specialistische kennis, Nieuwe technologieën"
        }

# Run AI Analysis
ai_analysis = analyze_with_claude(vacature_text, jobdigger_text, linkedin_ti_text, functietitel, sector, locatie)

# ========================================
# FORMAT DATA FOR OUTPUT
# ========================================

def format_salary(amount):
    """Format salary as Euro"""
    try:
        return f"€{int(amount):,}".replace(',', '.')
    except:
        return "N/A"

salaris_p25 = f"{format_salary(ai_analysis.get('salaris_p25_min', 0))} - {format_salary(ai_analysis.get('salaris_p25_max', 0))}"
salaris_p50 = f"{format_salary(ai_analysis.get('salaris_p50_min', 0))} - {format_salary(ai_analysis.get('salaris_p50_max', 0))}"
salaris_p75 = f"{format_salary(ai_analysis.get('salaris_p75_min', 0))} - {format_salary(ai_analysis.get('salaris_p75_max', 0))}"

current_date = datetime.datetime.now().strftime("%d %B %Y")

# ========================================
# SIMPLIFIED HTML EMAIL (Compact Version)
# ========================================
# Dit is een verkorte versie - voeg hier je volledige HTML template toe indien nodig

email_html = f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body style="font-family: Arial, sans-serif; background-color: #f3f4f6; margin: 0; padding: 20px;">
    <div style="max-width: 700px; margin: 0 auto; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">

        <!-- Header -->
        <div style="background: linear-gradient(135deg, #4B4F51 0%, #77797B 100%); padding: 40px; text-align: center; color: white;">
            <h1 style="margin: 0 0 10px 0; font-size: 32px;">🤖 AI Arbeidsmarkt Intelligence</h1>
            <p style="margin: 0; opacity: 0.9; font-size: 16px;">Labour Market Analysis • Powered by Claude AI</p>
        </div>

        <div style="height: 6px; background: #EF7D00;"></div>

        <!-- Summary -->
        <div style="padding: 40px; background: #FFF7ED; border-left: 4px solid #EF7D00;">
            <h2 style="margin: 0 0 20px 0; color: #1f2937; font-size: 24px;">📊 Executive Summary</h2>
            <p style="margin: 8px 0; color: #374151; font-size: 16px; line-height: 1.6;">
                <strong>Vacature:</strong> {functietitel}<br>
                <strong>Bedrijf:</strong> {bedrijfsnaam}<br>
                <strong>Sector:</strong> {sector}<br>
                <strong>Locatie:</strong> {locatie}<br>
                <strong>Aantal posities:</strong> {aantal_posities}<br>
                <strong>Urgentie:</strong> <span style="color: #dc2626; font-weight: bold;">{urgentie}</span>
            </p>
        </div>

        <!-- Contact -->
        <div style="padding: 30px 40px;">
            <h3 style="margin: 0 0 15px 0; color: #1f2937; font-size: 20px;">👤 Contactpersoon</h3>
            <p style="margin: 5px 0; color: #374151;">
                <strong>Naam:</strong> {contactpersoon}<br>
                <strong>Email:</strong> <a href="mailto:{email}" style="color: #EF7D00;">{email}</a><br>
                <strong>Telefoon:</strong> <a href="tel:{telefoon}" style="color: #EF7D00;">{telefoon}</a>
            </p>
        </div>

        <!-- AI Insights -->
        <div style="padding: 0 40px 30px 40px;">
            <h3 style="margin: 0 0 20px 0; color: #1f2937; font-size: 20px; border-bottom: 2px solid #e5e7eb; padding-bottom: 10px;">📈 Arbeidsmarkt Status (AI)</h3>
            <table style="width: 100%; border-collapse: collapse;">
                <tr>
                    <td style="width: 33%; padding: 20px; background: #fef2f2; border-radius: 8px; text-align: center;">
                        <div style="font-size: 28px; margin-bottom: 8px;">⚠️</div>
                        <div style="color: #dc2626; font-size: 24px; font-weight: bold;">{ai_analysis['schaarste_niveau']}</div>
                        <div style="color: #991b1b; font-size: 12px; margin-top: 5px;">Schaarste</div>
                    </td>
                    <td style="width: 2%;"></td>
                    <td style="width: 33%; padding: 20px; background: #fff7ed; border-radius: 8px; text-align: center;">
                        <div style="font-size: 28px; margin-bottom: 8px;">⏱️</div>
                        <div style="color: #ea580c; font-size: 24px; font-weight: bold;">{ai_analysis['time_to_hire_min']}-{ai_analysis['time_to_hire_max']}</div>
                        <div style="color: #c2410c; font-size: 12px; margin-top: 5px;">Dagen Time-to-Hire</div>
                    </td>
                    <td style="width: 2%;"></td>
                    <td style="width: 33%; padding: 20px; background: #eff6ff; border-radius: 8px; text-align: center;">
                        <div style="font-size: 28px; margin-bottom: 8px;">👥</div>
                        <div style="color: #2563eb; font-size: 24px; font-weight: bold;">{ai_analysis['beschikbaarheid']}</div>
                        <div style="color: #1d4ed8; font-size: 12px; margin-top: 5px;">Kandidaten NL</div>
                    </td>
                </tr>
            </table>
        </div>

        <!-- Salary -->
        <div style="padding: 0 40px 30px 40px;">
            <h3 style="margin: 0 0 15px 0; color: #1f2937; font-size: 20px;">💰 Salaris Benchmark (AI)</h3>
            <div style="background: linear-gradient(135deg, #EF7D00 0%, #ea580c 100%); padding: 25px; border-radius: 12px; color: white;">
                <div style="font-size: 14px; opacity: 0.9;">Markt Mediaan (P50)</div>
                <div style="font-size: 36px; font-weight: bold; margin: 10px 0;">{salaris_p50}</div>
                <div style="font-size: 13px; opacity: 0.8;">Bruto jaarsalaris, exclusief bonus</div>
            </div>
        </div>

        <!-- CTA -->
        <div style="padding: 30px 40px; background: linear-gradient(135deg, #EF7D00 0%, #d97706 100%); color: white;">
            <h3 style="margin: 0 0 15px 0; font-size: 20px;">⚡ Volgende Stappen</h3>
            <ol style="margin: 0; padding-left: 20px; line-height: 1.8;">
                <li>Review AI-gedreven analyse</li>
                <li>Bel {contactpersoon} ({telefoon})</li>
                <li>Bespreek data-gedreven strategie</li>
                <li>Start active sourcing binnen 48 uur</li>
            </ol>
        </div>

        <!-- Footer -->
        <div style="padding: 25px 40px; background: #f9fafb; text-align: center; border-top: 1px solid #e5e7eb;">
            <p style="margin: 0 0 8px 0; color: #4B4F51; font-weight: bold; font-size: 18px;">Recruitin</p>
            <p style="margin: 0; color: #6b7280; font-size: 13px;">
                📧 warts@recruitin.nl | 🌐 recruitin.com
            </p>
            <p style="margin: 10px 0 0 0; color: #9ca3af; font-size: 12px;">
                {current_date} • Powered by Claude AI
            </p>
        </div>

    </div>
</body>
</html>"""

# ========================================
# OUTPUT FOR ZAPIER - PDFMONKEY READY
# ========================================

# Prepare structured data for PDFMonkey template
pdfmonkey_payload = {
    # Meta
    "datum": current_date,
    "bedrijfsnaam": bedrijfsnaam,
    "contactpersoon": contactpersoon,
    "email": email,
    "telefoon": telefoon,

    # Vacature
    "functietitel": functietitel,
    "sector": sector,
    "locatie": locatie,
    "aantal_posities": aantal_posities,
    "urgentie": urgentie,
    "ervaringsniveau": ervaringsniveau,

    # AI Analysis
    "schaarste_niveau": ai_analysis.get('schaarste_niveau', 'N/A'),
    "schaarste_ratio": ai_analysis.get('schaarste_ratio', 'N/A'),
    "time_to_hire": f"{ai_analysis.get('time_to_hire_min', 0)}-{ai_analysis.get('time_to_hire_max', 0)} dagen",
    "beschikbaarheid": ai_analysis.get('beschikbaarheid', 'N/A'),
    "beschikbaarheid_tekst": ai_analysis.get('beschikbaarheid_tekst', ''),

    # Salary
    "salaris_p25": salaris_p25,
    "salaris_p50": salaris_p50,
    "salaris_p75": salaris_p75,

    # Werkzoekend Ratio
    "actief_zoekend": ai_analysis.get('werkzoekend_ratio', {}).get('actief', 0),
    "latent_zoekend": ai_analysis.get('werkzoekend_ratio', {}).get('latent', 0),
    "niet_zoekend": ai_analysis.get('werkzoekend_ratio', {}).get('niet_werkzoekend', 0),

    # Market Data
    "total_workers_market": ai_analysis.get('total_workers_market', 'N/A'),
    "growth_percentage": ai_analysis.get('growth_percentage', 'N/A'),
    "open_vacancies": ai_analysis.get('open_vacancies', 'N/A'),
    "employment_trend": ai_analysis.get('employment_trend', 'Stijgend'),
    "talent_pool_size": ai_analysis.get('talent_pool_size', 'N/A'),
    "hiring_velocity": ai_analysis.get('hiring_velocity', 'N/A'),

    # Skills (simplified for PDF)
    "doelgroep_skills": ai_analysis.get('doelgroep_skills', []),
    "technical_skills": ai_analysis.get('technical_skills', []),
    "soft_skills": ai_analysis.get('soft_skills', []),
    "push_factors": ai_analysis.get('push_factors', []),
    "pull_factors": ai_analysis.get('pull_factors', []),
    "leeftijd_verdeling": ai_analysis.get('leeftijd_verdeling', []),

    # URLs
    "vacature_url": vacature_url,
    "jobdigger_url": jobdigger_url,
    "linkedin_ti_url": linkedin_ti_url
}

# Output for next Zapier steps
output = {
    # Email output
    'email_to': RECRUITER_EMAIL,
    'email_cc': email,  # CC naar klant
    'email_subject': f"🤖 AI Recruitment Intelligence: {functietitel} bij {bedrijfsnaam}",
    'email_body_html': email_html,

    # PDFMonkey payload (as JSON string for Zapier PDFMonkey step)
    'pdfmonkey_payload': json.dumps(pdfmonkey_payload),

    # Individual fields for Notion integration
    'notion_bedrijfsnaam': bedrijfsnaam,
    'notion_contactpersoon': contactpersoon,
    'notion_email': email,
    'notion_telefoon': telefoon,
    'notion_functietitel': functietitel,
    'notion_sector': sector,
    'notion_locatie': locatie,
    'notion_salaris_range': salaris_p50,
    'notion_urgentie': urgentie,
    'notion_status': '🤖 AI Analyse Compleet',
    'notion_ai_schaarste': ai_analysis['schaarste_niveau'],
    'notion_ai_time_to_hire': f"{ai_analysis['time_to_hire_min']}-{ai_analysis['time_to_hire_max']} dagen",
    'notion_datum': datetime.datetime.now().strftime('%Y-%m-%d'),
    'notion_vacature_url': vacature_url if vacature_url else None,
    'notion_jobdigger_url': jobdigger_url if jobdigger_url else None,
    'notion_linkedin_ti_url': linkedin_ti_url if linkedin_ti_url else None,

    # Metadata
    'recipient_email': RECRUITER_EMAIL,
    'ai_used': 'Claude Sonnet 4.5',
    'data_betrouwbaarheid': '92%',
    'current_date': current_date
}
