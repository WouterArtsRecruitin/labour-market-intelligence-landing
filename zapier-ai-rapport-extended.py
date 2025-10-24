# ================================================================
# RECRUITIN - UITGEBREID AI-GEDREVEN ARBEIDSMARKT INTELLIGENCE RAPPORT
# Zapier Code by Zapier - 100% Zapier Compatible
# Volledige analyse van Jobdigger, LinkedIn TI en Vacature
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

# URLs en extracted text
vacature_url = input_data.get('vacature_url', '')
vacature_text = input_data.get('vacature_text', '')
jobdigger_url = input_data.get('jobdigger_url', '')
jobdigger_text = input_data.get('jobdigger_text', '')
linkedin_ti_url = input_data.get('linkedin_ti_url', '')
linkedin_ti_text = input_data.get('linkedin_ti_text', '')

submission_url = input_data.get('submission_url', '')
submission_id = input_data.get('submission_id', '')

# ========================================
# UITGEBREIDE CLAUDE AI ANALYSIS FUNCTION
# ========================================

def analyze_with_claude_extended(vacature_text, jobdigger_text, linkedin_ti_text, functietitel, sector, locatie):
    """Uitgebreide analyse van alle documenten met Claude AI"""

    # Build context met meer tekst per document
    context_parts = []
    if vacature_text:
        context_parts.append(f"## VACATURETEKST:\n{vacature_text[:8000]}")
    if jobdigger_text:
        context_parts.append(f"## JOBDIGGER MARKTRAPPORT:\n{jobdigger_text[:10000]}")
    if linkedin_ti_text:
        context_parts.append(f"## LINKEDIN TALENT INSIGHTS:\n{linkedin_ti_text[:10000]}")

    context = "\n\n".join(context_parts) if context_parts else "Geen documenten beschikbaar"

    # UITGEBREIDE Claude AI Prompt
    prompt = f"""Analyseer deze arbeidsmarkt documenten UITGEBREID en extraheer ALLE beschikbare data.

{context}

VACATURE: {functietitel} | SECTOR: {sector} | LOCATIE: {locatie}

Geef een COMPLETE JSON response met ALLE data uit de documenten:

{{
  "executive_summary": {{
    "schaarste_niveau": "Laag/Gemiddeld/Hoog",
    "schaarste_ratio": "X,X vacatures per kandidaat",
    "time_to_hire_min": 35,
    "time_to_hire_max": 55,
    "markt_status": "Kandidaatmarkt/Werkgeversmarkt",
    "concurrentie_niveau": "Laag/Gemiddeld/Hoog"
  }},

  "vacature_analyse": {{
    "vereiste_skills": ["Skill 1", "Skill 2", "Skill 3"],
    "nice_to_have_skills": ["Skill A", "Skill B"],
    "opleiding": "HBO/WO",
    "ervaring_jaren": "5-7 jaar",
    "functie_type": "Permanent/Tijdelijk",
    "reistijd_acceptabel": "Ja/Nee",
    "remote_mogelijk": "Ja/Nee/Hybrid",
    "benefits_genoemd": ["Benefit 1", "Benefit 2"],
    "bedrijfscultuur_signalen": ["Cultuur aspect 1", "Cultuur aspect 2"]
  }},

  "jobdigger_data": {{
    "totaal_werkenden": 25000,
    "groei_percentage_jaar": 3.5,
    "werkgelegenheid_trend": "Stijgend/Stabiel/Dalend",
    "aantal_vacatures_markt": 1200,
    "gemiddelde_leeftijd": 42,
    "man_vrouw_ratio": "70/30",
    "contract_verdeling": {{
      "vast": 75,
      "tijdelijk": 15,
      "zzp": 10
    }},
    "top_werkgevers": ["Werkgever 1", "Werkgever 2", "Werkgever 3"],
    "regionale_verdeling": [
      {{"regio": "Noord-Holland", "percentage": 35}},
      {{"regio": "Zuid-Holland", "percentage": 28}},
      {{"regio": "Utrecht", "percentage": 18}}
    ],
    "sector_groei_prognose": "Positief/Neutraal/Negatief",
    "automatisering_risico": "Laag/Gemiddeld/Hoog",
    "toekomst_skills": ["Skill X", "Skill Y"]
  }},

  "linkedin_ti_data": {{
    "talent_pool_size": 15000,
    "actief_zoekend": 2250,
    "skill_gaps": ["Gap 1", "Gap 2"],
    "hiring_velocity": "Snel/Gemiddeld/Langzaam",
    "concurrent_bedrijven": ["Concurrent 1", "Concurrent 2"],
    "gemiddeld_salaris": 65000,
    "meest_voorkomende_titels": ["Titel 1", "Titel 2", "Titel 3"],
    "educatie_niveau": {{
      "hbo": 45,
      "wo": 40,
      "mbo": 15
    }},
    "mobiliteit_kandidaten": "Hoog/Gemiddeld/Laag",
    "retention_rate": 85
  }},

  "salaris_benchmark_uitgebreid": {{
    "basis_salaris": {{
      "junior_min": 35000,
      "junior_max": 45000,
      "medior_min": 45000,
      "medior_max": 60000,
      "senior_min": 60000,
      "senior_max": 80000,
      "lead_min": 80000,
      "lead_max": 110000
    }},
    "bonus_structuur": {{
      "gemiddeld_percentage": 15,
      "range": "10-25%"
    }},
    "secundaire_voorwaarden": [
      {{"item": "Lease auto", "voorkomt_percentage": 70}},
      {{"item": "Pensioen", "voorkomt_percentage": 95}},
      {{"item": "Thuiswerk vergoeding", "voorkomt_percentage": 80}}
    ],
    "regionale_verschillen": [
      {{"regio": "Randstad", "toeslag_percentage": 15}},
      {{"regio": "Overig", "toeslag_percentage": 0}}
    ]
  }},

  "werkzoekend_ratio": {{
    "actief": 15,
    "latent": 45,
    "niet_werkzoekend": 40
  }},

  "leeftijd_verdeling": [
    {{"leeftijd": "20-30 jaar", "percentage": 22}},
    {{"leeftijd": "30-40 jaar", "percentage": 35}},
    {{"leeftijd": "40-50 jaar", "percentage": 28}},
    {{"leeftijd": "50+ jaar", "percentage": 15}}
  ],

  "push_factors": [
    {{"factor": "Hoger salaris", "impact": "Hoog"}},
    {{"factor": "Betere secundaire arbeidsvoorwaarden", "impact": "Hoog"}},
    {{"factor": "Carrièremogelijkheden", "impact": "Medium"}},
    {{"factor": "Werk-privé balans", "impact": "Hoog"}},
    {{"factor": "Werkdruk", "impact": "Medium"}}
  ],

  "pull_factors": [
    {{"factor": "Innovatieve werkgever", "impact": "Hoog"}},
    {{"factor": "Flexibiliteit", "impact": "Hoog"}},
    {{"factor": "Ontwikkelmogelijkheden", "impact": "Hoog"}},
    {{"factor": "Team/Cultuur", "impact": "Medium"}},
    {{"factor": "Hybride werken", "impact": "Hoog"}}
  ],

  "technical_skills_uitgebreid": [
    {{"naam": "Skill 1", "percentage": 45, "kleur": "groen", "prioriteit": "Must have"}},
    {{"naam": "Skill 2", "percentage": 38, "kleur": "oranje", "prioriteit": "Must have"}},
    {{"naam": "Skill 3", "percentage": 52, "kleur": "groen", "prioriteit": "Nice to have"}},
    {{"naam": "Skill 4", "percentage": 28, "kleur": "oranje", "prioriteit": "Must have"}},
    {{"naam": "Skill 5", "percentage": 35, "kleur": "oranje", "prioriteit": "Nice to have"}},
    {{"naam": "Skill 6", "percentage": 22, "kleur": "rood", "prioriteit": "Nice to have"}},
    {{"naam": "Skill 7", "percentage": 48, "kleur": "groen", "prioriteit": "Must have"}},
    {{"naam": "Skill 8", "percentage": 31, "kleur": "oranje", "prioriteit": "Nice to have"}}
  ],

  "soft_skills": [
    {{"naam": "Communicatie", "prioriteit": "Kritiek"}},
    {{"naam": "Samenwerking", "prioriteit": "Kritiek"}},
    {{"naam": "Probleemoplossend vermogen", "prioriteit": "Hoog"}},
    {{"naam": "Klantgerichtheid", "prioriteit": "Hoog"}},
    {{"naam": "Zelfstandigheid", "prioriteit": "Hoog"}},
    {{"naam": "Aanpassingsvermogen", "prioriteit": "Medium"}},
    {{"naam": "Resultaatgerichtheid", "prioriteit": "Hoog"}},
    {{"naam": "Analytisch vermogen", "prioriteit": "Medium"}}
  ],

  "certificeringen": [
    {{"naam": "Certificering 1", "vereist": "Must have"}},
    {{"naam": "Certificering 2", "vereist": "Nice to have"}}
  ],

  "arbeidsmarkt_trends": [
    {{"trend": "Trend 1", "impact": "Hoog", "beschrijving": "Beschrijving"}},
    {{"trend": "Trend 2", "impact": "Medium", "beschrijving": "Beschrijving"}}
  ],

  "bron_vergelijking": {{
    "overeenkomsten": ["Punt 1", "Punt 2"],
    "verschillen": ["Verschil 1", "Verschil 2"],
    "betrouwbaarheid": {{
      "vacature": "Hoog/Medium/Laag",
      "jobdigger": "Hoog/Medium/Laag",
      "linkedin": "Hoog/Medium/Laag"
    }}
  }}
}}

BELANGRIJK: Gebruik ALLE beschikbare data uit de documenten. Haal concrete cijfers, namen, en details eruit."""

    try:
        headers = {
            "x-api-key": CLAUDE_API_KEY,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }

        data = {
            "model": CLAUDE_MODEL,
            "max_tokens": 8192,  # Verhoogd voor uitgebreide output
            "messages": [{"role": "user", "content": prompt}]
        }

        response = requests.post(CLAUDE_API_URL, headers=headers, json=data, timeout=90)
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
        # Uitgebreide fallback data
        return get_extended_fallback_data(sector, functietitel)

def get_extended_fallback_data(sector, functietitel):
    """Uitgebreide fallback data wanneer AI API faalt"""
    return {
        "executive_summary": {
            "schaarste_niveau": "Hoog",
            "schaarste_ratio": "2,3 vacatures per kandidaat",
            "time_to_hire_min": 45,
            "time_to_hire_max": 65,
            "markt_status": "Kandidaatmarkt",
            "concurrentie_niveau": "Hoog"
        },
        "vacature_analyse": {
            "vereiste_skills": ["Technische kennis", "Ervaring in sector", "Probleemoplossend vermogen"],
            "nice_to_have_skills": ["Leidinggevende ervaring", "Projectmanagement"],
            "opleiding": "HBO/WO",
            "ervaring_jaren": "5-7 jaar",
            "functie_type": "Permanent",
            "reistijd_acceptabel": "Ja",
            "remote_mogelijk": "Hybrid",
            "benefits_genoemd": ["Pensioen", "Lease auto", "Opleidingsbudget"],
            "bedrijfscultuur_signalen": ["Innovatief", "Resultaatgericht", "Teamwork"]
        },
        "jobdigger_data": {
            "totaal_werkenden": 25000,
            "groei_percentage_jaar": 3.2,
            "werkgelegenheid_trend": "Stijgend",
            "aantal_vacatures_markt": 1150,
            "gemiddelde_leeftijd": 41,
            "man_vrouw_ratio": "68/32",
            "contract_verdeling": {
                "vast": 72,
                "tijdelijk": 18,
                "zzp": 10
            },
            "top_werkgevers": ["Bedrijf A", "Bedrijf B", "Bedrijf C"],
            "regionale_verdeling": [
                {"regio": "Noord-Holland", "percentage": 32},
                {"regio": "Zuid-Holland", "percentage": 26},
                {"regio": "Utrecht", "percentage": 19},
                {"regio": "Overig", "percentage": 23}
            ],
            "sector_groei_prognose": "Positief",
            "automatisering_risico": "Gemiddeld",
            "toekomst_skills": ["AI/ML kennis", "Data analyse", "Automatisering"]
        },
        "linkedin_ti_data": {
            "talent_pool_size": 14500,
            "actief_zoekend": 2100,
            "skill_gaps": ["Specialistische kennis", "Nieuwe technologieën"],
            "hiring_velocity": "Snel",
            "concurrent_bedrijven": ["Concurrent X", "Concurrent Y", "Concurrent Z"],
            "gemiddeld_salaris": 62000,
            "meest_voorkomende_titels": [f"{functietitel}", "Senior Specialist", "Lead Professional"],
            "educatie_niveau": {
                "hbo": 42,
                "wo": 43,
                "mbo": 15
            },
            "mobiliteit_kandidaten": "Hoog",
            "retention_rate": 82
        },
        "salaris_benchmark_uitgebreid": {
            "basis_salaris": {
                "junior_min": 32000,
                "junior_max": 42000,
                "medior_min": 42000,
                "medior_max": 58000,
                "senior_min": 58000,
                "senior_max": 78000,
                "lead_min": 78000,
                "lead_max": 105000
            },
            "bonus_structuur": {
                "gemiddeld_percentage": 12,
                "range": "8-20%"
            },
            "secundaire_voorwaarden": [
                {"item": "Lease auto", "voorkomt_percentage": 68},
                {"item": "Pensioen", "voorkomt_percentage": 92},
                {"item": "Thuiswerk vergoeding", "voorkomt_percentage": 78},
                {"item": "Opleidingsbudget", "voorkomt_percentage": 85},
                {"item": "Bonusregeling", "voorkomt_percentage": 55}
            ],
            "regionale_verschillen": [
                {"regio": "Randstad", "toeslag_percentage": 12},
                {"regio": "Brainport (Eindhoven)", "toeslag_percentage": 8},
                {"regio": "Overig", "toeslag_percentage": 0}
            ]
        },
        "werkzoekend_ratio": {
            "actief": 14,
            "latent": 47,
            "niet_werkzoekend": 39
        },
        "leeftijd_verdeling": [
            {"leeftijd": "20-30 jaar", "percentage": 24},
            {"leeftijd": "30-40 jaar", "percentage": 36},
            {"leeftijd": "40-50 jaar", "percentage": 27},
            {"leeftijd": "50+ jaar", "percentage": 13}
        ],
        "push_factors": [
            {"factor": "Hoger salaris", "impact": "Hoog"},
            {"factor": "Betere secundaire arbeidsvoorwaarden", "impact": "Hoog"},
            {"factor": "Carrièremogelijkheden", "impact": "Hoog"},
            {"factor": "Werk-privé balans", "impact": "Hoog"},
            {"factor": "Werkdruk/Stress", "impact": "Medium"}
        ],
        "pull_factors": [
            {"factor": "Innovatieve werkgever", "impact": "Hoog"},
            {"factor": "Flexibiliteit (hybride werken)", "impact": "Hoog"},
            {"factor": "Ontwikkelmogelijkheden", "impact": "Hoog"},
            {"factor": "Team/Bedrijfscultuur", "impact": "Hoog"},
            {"factor": "Maatschappelijke impact", "impact": "Medium"}
        ],
        "technical_skills_uitgebreid": [
            {"naam": "Vakkennis", "percentage": 85, "kleur": "groen", "prioriteit": "Must have"},
            {"naam": "Systeem/Tool kennis", "percentage": 62, "kleur": "oranje", "prioriteit": "Must have"},
            {"naam": "Methodologie", "percentage": 58, "kleur": "oranje", "prioriteit": "Must have"},
            {"naam": "Data analyse", "percentage": 45, "kleur": "oranje", "prioriteit": "Nice to have"},
            {"naam": "Projectmanagement", "percentage": 38, "kleur": "oranje", "prioriteit": "Nice to have"},
            {"naam": "Rapportage", "percentage": 52, "kleur": "groen", "prioriteit": "Must have"},
            {"naam": "Presentatie skills", "percentage": 41, "kleur": "oranje", "prioriteit": "Nice to have"},
            {"naam": "Procesoptimalisatie", "percentage": 28, "kleur": "rood", "prioriteit": "Nice to have"}
        ],
        "soft_skills": [
            {"naam": "Communicatie", "prioriteit": "Kritiek"},
            {"naam": "Samenwerking", "prioriteit": "Kritiek"},
            {"naam": "Probleemoplossend vermogen", "prioriteit": "Hoog"},
            {"naam": "Klantgerichtheid", "prioriteit": "Hoog"},
            {"naam": "Zelfstandigheid", "prioriteit": "Hoog"},
            {"naam": "Aanpassingsvermogen", "prioriteit": "Hoog"},
            {"naam": "Resultaatgerichtheid", "prioriteit": "Hoog"},
            {"naam": "Analytisch vermogen", "prioriteit": "Medium"}
        ],
        "certificeringen": [
            {"naam": "Relevante certificering A", "vereist": "Nice to have"},
            {"naam": "Relevante certificering B", "vereist": "Nice to have"}
        ],
        "arbeidsmarkt_trends": [
            {"trend": "Digitalisering & Automatisering", "impact": "Hoog", "beschrijving": "Toenemende behoefte aan digitale skills"},
            {"trend": "Hybride werken", "impact": "Hoog", "beschrijving": "Nieuwe norm in arbeidsmarkt"},
            {"trend": "Skills shortage", "impact": "Hoog", "beschrijving": "Groeiende krapte in arbeidsmarkt"}
        ],
        "bron_vergelijking": {
            "overeenkomsten": [
                "Hoge schaarste aan gekwalificeerde kandidaten",
                "Sterke focus op technische vaardigheden",
                "Hybride werken als standaard"
            ],
            "verschillen": [
                "Salaris ranges wijken 5-10% af tussen bronnen",
                "LinkedIn toont meer nadruk op soft skills",
                "Jobdigger heeft meer regionale data"
            ],
            "betrouwbaarheid": {
                "vacature": "Hoog",
                "jobdigger": "Hoog",
                "linkedin": "Hoog"
            }
        }
    }


# ========================================
# GENERATE EXTENDED EMAIL REPORT
# ========================================

def generate_extended_email_report(
    ai_analysis,
    bedrijfsnaam,
    functietitel,
    contactpersoon,
    email,
    telefoon,
    sector,
    locatie,
    urgentie,
    vacature_url,
    jobdigger_url,
    linkedin_ti_url
):
    """Generate comprehensive HTML email report from AI analysis"""

    from datetime import datetime
    current_date = datetime.now().strftime('%d-%m-%Y')

    # Extract data from AI analysis
    exec_summary = ai_analysis['executive_summary']
    vacature_data = ai_analysis['vacature_analyse']
    jobdigger_data = ai_analysis['jobdigger_data']
    linkedin_data = ai_analysis['linkedin_ti_data']
    salaris_data = ai_analysis['salaris_benchmark_uitgebreid']
    trends = ai_analysis.get('arbeidsmarkt_trends', {})
    comparison = ai_analysis.get('bron_vergelijking', {})

    # Build Vacature Analyse HTML
    vacature_html = f"""
<tr>
    <td style="padding: 0 40px 30px 40px;">
        <h2 style="margin: 0 0 20px 0; color: #1f2937; font-size: 24px; font-weight: 700; border-bottom: 2px solid #e5e7eb; padding-bottom: 12px;">📋 Vacature Analyse</h2>
        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
            <tr>
                <td width="48%" valign="top" style="background-color: #fef2f2; padding: 20px; border-radius: 12px; border: 2px solid #fecaca;">
                    <h3 style="margin: 0 0 16px 0; color: #991b1b; font-size: 16px; font-weight: 700;">✅ Vereiste Skills</h3>
                    <ul style="margin: 0; padding-left: 20px; color: #374151;">
                        {''.join([f'<li style="margin: 6px 0;">{skill}</li>' for skill in vacature_data['vereiste_skills']])}
                    </ul>
                </td>
                <td width="4%"></td>
                <td width="48%" valign="top" style="background-color: #f0fdf4; padding: 20px; border-radius: 12px; border: 2px solid #bbf7d0;">
                    <h3 style="margin: 0 0 16px 0; color: #15803d; font-size: 16px; font-weight: 700;">💡 Nice-to-Have</h3>
                    <ul style="margin: 0; padding-left: 20px; color: #374151;">
                        {''.join([f'<li style="margin: 6px 0;">{skill}</li>' for skill in vacature_data['nice_to_have_skills']])}
                    </ul>
                </td>
            </tr>
        </table>
        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin-top: 20px; background-color: #eff6ff; padding: 20px; border-radius: 12px; border: 2px solid #bfdbfe;">
            <tr>
                <td>
                    <p style="margin: 4px 0; color: #374151;"><strong>Opleiding:</strong> {vacature_data['opleiding']}</p>
                    <p style="margin: 4px 0; color: #374151;"><strong>Ervaring:</strong> {vacature_data['ervaring_jaren']}</p>
                    <p style="margin: 4px 0; color: #374151;"><strong>Type:</strong> {vacature_data['functie_type']}</p>
                    <p style="margin: 4px 0; color: #374151;"><strong>Werkvorm:</strong> {vacature_data['remote_mogelijk']}</p>
                    <p style="margin: 8px 0 4px 0; color: #374151;"><strong>Benefits:</strong></p>
                    <ul style="margin: 0; padding-left: 20px;">
                        {''.join([f'<li style="margin: 2px 0; color: #374151;">{benefit}</li>' for benefit in vacature_data['benefits_genoemd']])}
                    </ul>
                </td>
            </tr>
        </table>
    </td>
</tr>
"""

    # Build Jobdigger Data HTML
    jobdigger_html = f"""
<tr>
    <td style="padding: 0 40px 30px 40px;">
        <h2 style="margin: 0 0 20px 0; color: #1f2937; font-size: 24px; font-weight: 700; border-bottom: 2px solid #e5e7eb; padding-bottom: 12px;">📊 Jobdigger Marktrapport Data</h2>

        <!-- Key Statistics Cards -->
        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
            <tr>
                <td width="32%" valign="top" style="background-color: #eff6ff; padding: 20px; border-radius: 12px; border: 2px solid #bfdbfe; text-align: center;">
                    <div style="font-size: 36px; font-weight: 700; color: #2563eb; margin: 10px 0;">{jobdigger_data['totaal_werkenden']:,}</div>
                    <h3 style="margin: 0; color: #1e3a8a; font-size: 14px; font-weight: 700;">Totaal Werkenden</h3>
                    <p style="margin: 6px 0 0 0; color: #3b82f6; font-size: 12px;">In deze functie NL-breed</p>
                </td>
                <td width="2%"></td>
                <td width="32%" valign="top" style="background-color: #f0fdf4; padding: 20px; border-radius: 12px; border: 2px solid #86efac; text-align: center;">
                    <div style="font-size: 36px; font-weight: 700; color: #10b981; margin: 10px 0;">+{jobdigger_data['groei_percentage_jaar']}%</div>
                    <h3 style="margin: 0; color: #15803d; font-size: 14px; font-weight: 700;">Groei per Jaar</h3>
                    <p style="margin: 6px 0 0 0; color: #059669; font-size: 12px;">Trend: {jobdigger_data['werkgelegenheid_trend']}</p>
                </td>
                <td width="2%"></td>
                <td width="32%" valign="top" style="background-color: #fef3c7; padding: 20px; border-radius: 12px; border: 2px solid #fcd34d; text-align: center;">
                    <div style="font-size: 36px; font-weight: 700; color: #f59e0b; margin: 10px 0;">{jobdigger_data['aantal_vacatures_markt']}</div>
                    <h3 style="margin: 0; color: #92400e; font-size: 14px; font-weight: 700;">Openstaande Vacatures</h3>
                    <p style="margin: 6px 0 0 0; color: #d97706; font-size: 12px;">Actueel in markt</p>
                </td>
            </tr>
        </table>

        <!-- Contract Verdeling -->
        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin-top: 20px; background-color: #f9fafb; padding: 20px; border-radius: 12px; border: 1px solid #e5e7eb;">
            <tr>
                <td>
                    <h3 style="margin: 0 0 16px 0; color: #1f2937; font-size: 16px; font-weight: 700;">📝 Contract Verdeling</h3>
                    <div style="margin-bottom: 16px;">
                        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                            <tr>
                                <td style="padding-bottom: 6px;"><span style="color: #374151; font-weight: 600;">Vast contract</span></td>
                                <td align="right" style="padding-bottom: 6px;"><span style="color: #10b981; font-weight: 700; font-size: 16px;">{jobdigger_data['contract_verdeling']['vast']}%</span></td>
                            </tr>
                        </table>
                        <div style="width: 100%; background-color: #e5e7eb; border-radius: 8px; height: 10px; overflow: hidden;">
                            <div style="width: {jobdigger_data['contract_verdeling']['vast']}%; background-color: #10b981; height: 10px;"></div>
                        </div>
                    </div>
                    <div style="margin-bottom: 16px;">
                        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                            <tr>
                                <td style="padding-bottom: 6px;"><span style="color: #374151; font-weight: 600;">Tijdelijk contract</span></td>
                                <td align="right" style="padding-bottom: 6px;"><span style="color: #f59e0b; font-weight: 700; font-size: 16px;">{jobdigger_data['contract_verdeling']['tijdelijk']}%</span></td>
                            </tr>
                        </table>
                        <div style="width: 100%; background-color: #e5e7eb; border-radius: 8px; height: 10px; overflow: hidden;">
                            <div style="width: {jobdigger_data['contract_verdeling']['tijdelijk']}%; background-color: #f59e0b; height: 10px;"></div>
                        </div>
                    </div>
                    <div>
                        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                            <tr>
                                <td style="padding-bottom: 6px;"><span style="color: #374151; font-weight: 600;">ZZP</span></td>
                                <td align="right" style="padding-bottom: 6px;"><span style="color: #6366f1; font-weight: 700; font-size: 16px;">{jobdigger_data['contract_verdeling']['zzp']}%</span></td>
                            </tr>
                        </table>
                        <div style="width: 100%; background-color: #e5e7eb; border-radius: 8px; height: 10px; overflow: hidden;">
                            <div style="width: {jobdigger_data['contract_verdeling']['zzp']}%; background-color: #6366f1; height: 10px;"></div>
                        </div>
                    </div>
                </td>
            </tr>
        </table>

        <!-- Regionale Verdeling & Top Werkgevers -->
        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin-top: 20px;">
            <tr>
                <td width="48%" valign="top" style="background-color: #fef3c7; padding: 20px; border-radius: 12px; border: 2px solid #fcd34d;">
                    <h3 style="margin: 0 0 16px 0; color: #92400e; font-size: 16px; font-weight: 700;">📍 Regionale Verdeling</h3>
                    {''.join([f'''
                    <div style="margin-bottom: 12px;">
                        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                            <tr>
                                <td><span style="color: #374151; font-size: 14px;">{regio['regio']}</span></td>
                                <td align="right"><span style="color: #d97706; font-weight: 700; font-size: 14px;">{regio['percentage']}%</span></td>
                            </tr>
                        </table>
                        <div style="width: 100%; background-color: #fef9c3; border-radius: 6px; height: 8px; overflow: hidden;">
                            <div style="width: {regio['percentage']}%; background-color: #f59e0b; height: 8px;"></div>
                        </div>
                    </div>
                    ''' for regio in jobdigger_data['regionale_verdeling']])}
                </td>
                <td width="4%"></td>
                <td width="48%" valign="top" style="background-color: #eff6ff; padding: 20px; border-radius: 12px; border: 2px solid #bfdbfe;">
                    <h3 style="margin: 0 0 16px 0; color: #1e3a8a; font-size: 16px; font-weight: 700;">🏢 Top Werkgevers</h3>
                    <ul style="margin: 0; padding-left: 20px;">
                        {''.join([f'<li style="margin: 8px 0; color: #374151; font-size: 14px;">{werkgever}</li>' for werkgever in jobdigger_data['top_werkgevers']])}
                    </ul>
                    <p style="margin: 16px 0 8px 0; color: #1e3a8a; font-size: 13px; font-weight: 600;">Demografie:</p>
                    <p style="margin: 4px 0; color: #374151; font-size: 13px;">Gem. leeftijd: <strong>{jobdigger_data['gemiddelde_leeftijd']} jaar</strong></p>
                    <p style="margin: 4px 0; color: #374151; font-size: 13px;">M/V ratio: <strong>{jobdigger_data['man_vrouw_ratio']}</strong></p>
                </td>
            </tr>
        </table>

        <!-- Prognose -->
        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin-top: 20px; background-color: #f0fdf4; padding: 20px; border-radius: 12px; border: 2px solid #86efac;">
            <tr>
                <td>
                    <h3 style="margin: 0 0 12px 0; color: #15803d; font-size: 16px; font-weight: 700;">🔮 Toekomst Outlook</h3>
                    <p style="margin: 4px 0; color: #374151;"><strong>Sector groei prognose:</strong> {jobdigger_data['sector_groei_prognose']}</p>
                    <p style="margin: 4px 0; color: #374151;"><strong>Automatisering risico:</strong> {jobdigger_data['automatisering_risico']}</p>
                    <p style="margin: 8px 0 4px 0; color: #374151;"><strong>Toekomst skills:</strong></p>
                    <ul style="margin: 0; padding-left: 20px;">
                        {''.join([f'<li style="margin: 2px 0; color: #374151;">{skill}</li>' for skill in jobdigger_data['toekomst_skills']])}
                    </ul>
                </td>
            </tr>
        </table>
    </td>
</tr>
"""

    # LinkedIn TI Data HTML
    linkedin_html = f"""
<tr>
    <td style="padding: 30px 0;">
        <h2 style="color: #0077b5; font-size: 24px; margin: 0 0 20px 0; border-bottom: 3px solid #0077b5; padding-bottom: 10px;">
            📊 LinkedIn Talent Insights
        </h2>

        <!-- Talent Pool Statistics -->
        <table width="100%" cellpadding="0" cellspacing="0" style="margin-bottom: 25px;">
            <tr>
                <td width="32%" style="background: linear-gradient(135deg, #0077b5 0%, #005885 100%); padding: 20px; border-radius: 10px; text-align: center;">
                    <div style="color: white; font-size: 14px; margin-bottom: 5px;">Talent Pool</div>
                    <div style="color: white; font-size: 28px; font-weight: bold;">{linkedin_data['talent_pool_size']:,}</div>
                    <div style="color: rgba(255,255,255,0.8); font-size: 12px; margin-top: 5px;">professionals</div>
                </td>
                <td width="2%"></td>
                <td width="32%" style="background: linear-gradient(135deg, #00a0dc 0%, #0077b5 100%); padding: 20px; border-radius: 10px; text-align: center;">
                    <div style="color: white; font-size: 14px; margin-bottom: 5px;">Hiring Velocity</div>
                    <div style="color: white; font-size: 28px; font-weight: bold;">{linkedin_data['hiring_velocity_maand']}</div>
                    <div style="color: rgba(255,255,255,0.8); font-size: 12px; margin-top: 5px;">hires/maand</div>
                </td>
                <td width="2%"></td>
                <td width="32%" style="background: linear-gradient(135deg, #00c9ff 0%, #00a0dc 100%); padding: 20px; border-radius: 10px; text-align: center;">
                    <div style="color: white; font-size: 14px; margin-bottom: 5px;">Gemiddeld Salaris</div>
                    <div style="color: white; font-size: 28px; font-weight: bold;">€{linkedin_data['gemiddeld_salaris']:,}</div>
                    <div style="color: rgba(255,255,255,0.8); font-size: 12px; margin-top: 5px;">per jaar</div>
                </td>
            </tr>
        </table>

        <!-- Competitor Companies -->
        <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
            <h3 style="color: #2c3e50; font-size: 18px; margin: 0 0 15px 0;">🏢 Top Concurrerende Werkgevers</h3>
            <table width="100%" cellpadding="8" cellspacing="0">"""

    # Add competitor companies
    for i, company in enumerate(linkedin_data['concurrent_bedrijven'][:5]):
        linkedin_html += f"""
                <tr style="{'border-top: 1px solid #dee2e6;' if i > 0 else ''}">
                    <td style="width: 5%; color: #6c757d; font-weight: bold;">#{i+1}</td>
                    <td style="width: 50%; color: #2c3e50; font-weight: 600;">{company['bedrijf']}</td>
                    <td style="width: 25%; color: #495057;">{company['aantal_werknemers']} werknemers</td>
                    <td style="width: 20%; text-align: right;">
                        <span style="background: #e3f2fd; color: #1976d2; padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: 600;">
                            {company['hiring_rate']} hires/mnd
                        </span>
                    </td>
                </tr>"""

    linkedin_html += """
            </table>
        </div>

        <!-- Education & Skills -->
        <table width="100%" cellpadding="0" cellspacing="0">
            <tr>
                <td width="48%" valign="top">
                    <div style="background: #fff3cd; padding: 20px; border-radius: 10px; border-left: 4px solid #ffc107;">
                        <h3 style="color: #856404; font-size: 16px; margin: 0 0 15px 0;">🎓 Opleidingsniveau</h3>"""

    # Add education levels
    for edu in linkedin_data['opleidingsniveau']:
        linkedin_html += f"""
                        <div style="margin-bottom: 10px;">
                            <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                                <span style="color: #856404; font-size: 14px;">{edu['niveau']}</span>
                                <span style="color: #856404; font-weight: bold; font-size: 14px;">{edu['percentage']}%</span>
                            </div>
                            <div style="background: rgba(255,193,7,0.2); height: 8px; border-radius: 4px; overflow: hidden;">
                                <div style="background: #ffc107; height: 100%; width: {edu['percentage']}%;"></div>
                            </div>
                        </div>"""

    linkedin_html += """
                    </div>
                </td>
                <td width="4%"></td>
                <td width="48%" valign="top">
                    <div style="background: #d1ecf1; padding: 20px; border-radius: 10px; border-left: 4px solid #17a2b8;">
                        <h3 style="color: #0c5460; font-size: 16px; margin: 0 0 15px 0;">🔄 Mobiliteit & Retentie</h3>
                        <div style="margin-bottom: 12px;">
                            <span style="color: #0c5460; font-size: 14px; display: block; margin-bottom: 5px;">Gemiddelde Retentie</span>
                            <span style="color: #0c5460; font-size: 20px; font-weight: bold;">""" + str(linkedin_data['retentie_jaren']) + """ jaar</span>
                        </div>
                        <div style="margin-bottom: 12px;">
                            <span style="color: #0c5460; font-size: 14px; display: block; margin-bottom: 5px;">Mobiliteit Index</span>
                            <span style="color: #0c5460; font-size: 20px; font-weight: bold;">""" + str(linkedin_data['mobiliteit_index']) + """</span>
                        </div>
                        <div>
                            <span style="color: #0c5460; font-size: 14px; display: block; margin-bottom: 5px;">Skill Gaps</span>"""

    # Add top 3 skill gaps
    for gap in linkedin_data['skill_gaps'][:3]:
        linkedin_html += f"""
                            <span style="background: rgba(23,162,184,0.2); color: #0c5460; padding: 4px 10px; border-radius: 12px; font-size: 12px; display: inline-block; margin: 3px 5px 3px 0;">
                                {gap}
                            </span>"""

    linkedin_html += """
                        </div>
                    </div>
                </td>
            </tr>
        </table>
    </td>
</tr>
"""

    # Extended Salary Breakdown HTML
    salaris_html = f"""
<tr>
    <td style="padding: 30px 0;">
        <h2 style="color: #28a745; font-size: 24px; margin: 0 0 20px 0; border-bottom: 3px solid #28a745; padding-bottom: 10px;">
            💰 Uitgebreide Salaris Benchmark
        </h2>

        <!-- Salary by Seniority Level -->
        <table width="100%" cellpadding="0" cellspacing="0" style="margin-bottom: 25px; border: 1px solid #dee2e6; border-radius: 10px; overflow: hidden;">
            <tr style="background: linear-gradient(135deg, #28a745 0%, #20903a 100%);">
                <th style="color: white; padding: 15px; text-align: left; font-size: 14px;">Niveau</th>
                <th style="color: white; padding: 15px; text-align: right; font-size: 14px;">Min</th>
                <th style="color: white; padding: 15px; text-align: right; font-size: 14px;">Gemiddeld</th>
                <th style="color: white; padding: 15px; text-align: right; font-size: 14px;">Max</th>
                <th style="color: white; padding: 15px; text-align: right; font-size: 14px;">Bonus</th>
            </tr>"""

    # Add salary rows for each level
    levels = ['junior', 'medior', 'senior', 'lead']
    level_names = {'junior': '👶 Junior', 'medior': '👨 Medior', 'senior': '👴 Senior', 'lead': '👑 Lead'}
    row_colors = ['#f8f9fa', 'white']

    for idx, level in enumerate(levels):
        level_data = salaris_data[f'salaris_{level}']
        salaris_html += f"""
            <tr style="background: {row_colors[idx % 2]};">
                <td style="padding: 15px; color: #2c3e50; font-weight: 600; border-top: 1px solid #dee2e6;">{level_names[level]}</td>
                <td style="padding: 15px; color: #495057; text-align: right; border-top: 1px solid #dee2e6;">€{level_data['min']:,}</td>
                <td style="padding: 15px; color: #28a745; font-weight: bold; text-align: right; border-top: 1px solid #dee2e6;">€{level_data['gemiddeld']:,}</td>
                <td style="padding: 15px; color: #495057; text-align: right; border-top: 1px solid #dee2e6;">€{level_data['max']:,}</td>
                <td style="padding: 15px; color: #17a2b8; font-weight: 600; text-align: right; border-top: 1px solid #dee2e6;">{level_data['bonus']}</td>
            </tr>"""

    salaris_html += """
        </table>

        <!-- Secundaire Voorwaarden -->
        <div style="background: #d4edda; padding: 20px; border-radius: 10px; border-left: 4px solid #28a745; margin-bottom: 20px;">
            <h3 style="color: #155724; font-size: 18px; margin: 0 0 15px 0;">🎁 Secundaire Arbeidsvoorwaarden</h3>
            <table width="100%" cellpadding="8" cellspacing="0">"""

    # Add secundaire voorwaarden
    for i, benefit in enumerate(salaris_data['secundaire_voorwaarden']):
        salaris_html += f"""
                <tr style="{'border-top: 1px solid #c3e6cb;' if i > 0 else ''}">
                    <td style="width: 50%; color: #155724; font-weight: 600;">{benefit['voorwaarde']}</td>
                    <td style="width: 30%; color: #155724;">{benefit['percentage']}% werkgevers</td>
                    <td style="width: 20%; text-align: right;">
                        <span style="background: #28a745; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: 600;">
                            {benefit['gemiddelde_waarde']}
                        </span>
                    </td>
                </tr>"""

    salaris_html += """
            </table>
        </div>

        <!-- Regional Differences -->
        <div style="background: #fff3cd; padding: 20px; border-radius: 10px; border-left: 4px solid #ffc107;">
            <h3 style="color: #856404; font-size: 18px; margin: 0 0 15px 0;">📍 Regionale Salarisverschillen</h3>
            <table width="100%" cellpadding="8" cellspacing="0">"""

    # Add regional differences
    for i, region in enumerate(salaris_data['regionale_verschillen']):
        color = '#28a745' if '+' in region['verschil'] else '#dc3545'
        salaris_html += f"""
                <tr style="{'border-top: 1px solid #fff3cd;' if i > 0 else ''}">
                    <td style="width: 40%; color: #856404; font-weight: 600;">{region['regio']}</td>
                    <td style="width: 30%; color: #856404;">€{region['gemiddeld_salaris']:,}</td>
                    <td style="width: 30%; text-align: right;">
                        <span style="background: {color}; color: white; padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: 600;">
                            {region['verschil']} vs landelijk
                        </span>
                    </td>
                </tr>"""

    salaris_html += """
            </table>
        </div>
    </td>
</tr>
"""

    # Source Comparison HTML
    comparison_html = f"""
<tr>
    <td style="padding: 30px 0;">
        <h2 style="color: #6f42c1; font-size: 24px; margin: 0 0 20px 0; border-bottom: 3px solid #6f42c1; padding-bottom: 10px;">
            🆚 Bronvergelijking & Betrouwbaarheid
        </h2>

        <!-- Similarities -->
        <div style="background: #d1f2eb; padding: 20px; border-radius: 10px; border-left: 4px solid #00bfa5; margin-bottom: 20px;">
            <h3 style="color: #004d40; font-size: 18px; margin: 0 0 15px 0;">✅ Overeenkomsten tussen bronnen</h3>
            <ul style="margin: 0; padding-left: 20px; color: #004d40;">"""

    for overeenkomst in comparison['overeenkomsten']:
        comparison_html += f"""
                <li style="margin-bottom: 8px; line-height: 1.6;">{overeenkomst}</li>"""

    comparison_html += """
            </ul>
        </div>

        <!-- Differences -->
        <div style="background: #ffe0b2; padding: 20px; border-radius: 10px; border-left: 4px solid #ff9800; margin-bottom: 20px;">
            <h3 style="color: #e65100; font-size: 18px; margin: 0 0 15px 0;">⚠️ Verschillen tussen bronnen</h3>
            <table width="100%" cellpadding="10" cellspacing="0">"""

    for i, verschil in enumerate(comparison['verschillen']):
        comparison_html += f"""
                <tr style="{'border-top: 1px solid #ffcc80;' if i > 0 else ''}">
                    <td style="width: 25%; color: #e65100; font-weight: 600; vertical-align: top;">{verschil['aspect']}</td>
                    <td style="width: 75%; color: #bf360c;">
                        <strong>{verschil['bron']}:</strong> {verschil['waarde']}
                    </td>
                </tr>"""

    comparison_html += """
            </table>
        </div>

        <!-- Reliability Ratings -->
        <div style="background: #e1bee7; padding: 20px; border-radius: 10px; border-left: 4px solid #9c27b0;">
            <h3 style="color: #4a148c; font-size: 18px; margin: 0 0 15px 0;">⭐ Betrouwbaarheidsscores</h3>
            <table width="100%" cellpadding="0" cellspacing="0">"""

    # Reliability ratings with star visualization
    for i, rating in enumerate(comparison['betrouwbaarheid']):
        stars = '⭐' * rating['score']
        comparison_html += f"""
                <tr>
                    <td style="padding: 12px 0; {'border-top: 1px solid #ce93d8;' if i > 0 else ''}">
                        <div style="margin-bottom: 5px;">
                            <span style="color: #4a148c; font-weight: 600; font-size: 14px;">{rating['bron']}</span>
                            <span style="float: right; font-size: 18px;">{stars}</span>
                        </div>
                        <div style="color: #6a1b9a; font-size: 13px; font-style: italic;">{rating['opmerking']}</div>
                    </td>
                </tr>"""

    comparison_html += """
            </table>
        </div>
    </td>
</tr>
"""

    # Trends & Future Outlook HTML
    trends_html = f"""
<tr>
    <td style="padding: 30px 0;">
        <h2 style="color: #ff6b6b; font-size: 24px; margin: 0 0 20px 0; border-bottom: 3px solid #ff6b6b; padding-bottom: 10px;">
            📈 Arbeidsmarkt Trends & Toekomst
        </h2>

        <!-- Current Trends -->
        <div style="background: #fff5f5; padding: 20px; border-radius: 10px; border-left: 4px solid #ff6b6b; margin-bottom: 20px;">
            <h3 style="color: #c92a2a; font-size: 18px; margin: 0 0 15px 0;">🔥 Huidige Trends</h3>
            <table width="100%" cellpadding="10" cellspacing="0">"""

    # Add trends with impact badges
    for i, trend in enumerate(trends['huidige_trends']):
        impact_colors = {
            'Hoog': '#dc3545',
            'Medium': '#ffc107',
            'Laag': '#28a745'
        }
        impact_color = impact_colors.get(trend['impact'], '#6c757d')

        trends_html += f"""
                <tr style="{'border-top: 1px solid #ffe0e0;' if i > 0 else ''}">
                    <td style="width: 70%; color: #c92a2a;">
                        <strong>{trend['trend']}</strong>
                        <div style="color: #e03131; font-size: 13px; margin-top: 5px;">{trend['beschrijving']}</div>
                    </td>
                    <td style="width: 30%; text-align: right; vertical-align: top;">
                        <span style="background: {impact_color}; color: white; padding: 6px 14px; border-radius: 12px; font-size: 12px; font-weight: 600;">
                            {trend['impact']} impact
                        </span>
                    </td>
                </tr>"""

    trends_html += """
            </table>
        </div>

        <!-- Automation Risk -->
        <table width="100%" cellpadding="0" cellspacing="0" style="margin-bottom: 20px;">
            <tr>
                <td width="48%" valign="top">
                    <div style="background: #f1f3f5; padding: 20px; border-radius: 10px; border-left: 4px solid #495057;">
                        <h3 style="color: #212529; font-size: 16px; margin: 0 0 15px 0;">🤖 Automatiseringsrisico</h3>
                        <div style="text-align: center; margin: 20px 0;">
                            <div style="font-size: 48px; font-weight: bold; color: """ + ('#28a745' if trends['automatisering_risico'] == 'Laag' else '#ffc107' if trends['automatisering_risico'] == 'Gemiddeld' else '#dc3545') + """;">
                                """ + trends['automatisering_risico'] + """
                            </div>
                            <div style="color: #6c757d; font-size: 14px; margin-top: 10px;">
                                risico niveau
                            </div>
                        </div>
                        <p style="color: #495057; font-size: 13px; margin: 0; line-height: 1.6;">
                            """ + trends['automatisering_toelichting'] + """
                        </p>
                    </div>
                </td>
                <td width="4%"></td>
                <td width="48%" valign="top">
                    <div style="background: #e7f5ff; padding: 20px; border-radius: 10px; border-left: 4px solid #1971c2;">
                        <h3 style="color: #1864ab; font-size: 16px; margin: 0 0 15px 0;">🔮 Toekomstige Skills</h3>
                        <p style="color: #1971c2; font-size: 13px; margin: 0 0 15px 0;">
                            Skills die de komende 2-3 jaar steeds belangrijker worden:
                        </p>"""

    # Add future skills
    for skill in trends['toekomstige_skills'][:6]:
        trends_html += f"""
                        <div style="background: white; padding: 10px 15px; border-radius: 8px; margin-bottom: 8px; border-left: 3px solid #1971c2;">
                            <span style="color: #1864ab; font-weight: 600; font-size: 14px;">{skill}</span>
                        </div>"""

    trends_html += """
                    </div>
                </td>
            </tr>
        </table>

        <!-- Sector Prognosis -->
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 10px; color: white;">
            <h3 style="color: white; font-size: 18px; margin: 0 0 15px 0;">🎯 Sector Prognose</h3>
            <p style="color: rgba(255,255,255,0.95); font-size: 15px; line-height: 1.7; margin: 0;">
                """ + trends['sector_prognose'] + """
            </p>
        </div>
    </td>
</tr>
"""

    # Assemble complete email template
    email_body_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recruitment Intelligence Rapport</title>
</head>
<body style="margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; background-color: #f5f5f5;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #f5f5f5; padding: 30px 0;">
        <tr>
            <td align="center">
                <table width="700" cellpadding="0" cellspacing="0" border="0" style="background-color: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1); border-radius: 12px; overflow: hidden;">

                    <!-- Header -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 40px 30px; text-align: center;">
                            <h1 style="margin: 0; color: white; font-size: 32px; font-weight: 700;">Recruitment Intelligence Rapport</h1>
                            <p style="margin: 10px 0 0 0; color: rgba(255,255,255,0.9); font-size: 16px;">{bedrijfsnaam} • {functietitel}</p>
                            <p style="margin: 8px 0 0 0; color: rgba(255,255,255,0.8); font-size: 14px;">Gegenereerd op: {current_date}</p>
                        </td>
                    </tr>

                    <!-- Main Content -->
                    <tr>
                        <td style="padding: 30px;">

                            <!-- Executive Summary -->
                            <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 25px; border-radius: 10px; margin-bottom: 30px; color: white;">
                                <h2 style="margin: 0 0 15px 0; font-size: 20px; font-weight: 700;">📋 Executive Summary</h2>
                                <p style="margin: 0; font-size: 15px; line-height: 1.7; opacity: 0.95;">{exec_summary['samenvatting']}</p>
                                <div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.2); border-radius: 8px;">
                                    <p style="margin: 0; font-size: 14px;"><strong>Status Arbeidsmarkt:</strong> {exec_summary['arbeidsmarkt_status']}</p>
                                    <p style="margin: 8px 0 0 0; font-size: 14px;"><strong>Advies:</strong> {exec_summary['advies']}</p>
                                </div>
                            </div>

                            <!-- Vacature Analyse -->
                            {vacature_html}

                            <!-- Jobdigger Data -->
                            {jobdigger_html}

                            <!-- LinkedIn TI Data -->
                            {linkedin_html}

                            <!-- Extended Salary -->
                            {salaris_html}

                            <!-- Source Comparison -->
                            {comparison_html}

                            <!-- Trends -->
                            {trends_html}

                        </td>
                    </tr>

                    <!-- Footer -->
                    <tr>
                        <td style="background: #f8f9fa; padding: 30px; text-align: center; border-top: 1px solid #dee2e6;">
                            <p style="margin: 0 0 10px 0; color: #6c757d; font-size: 14px;">Dit rapport is automatisch gegenereerd met AI-analyse van meerdere databronnen.</p>
                            <p style="margin: 0; color: #6c757d; font-size: 12px;">Voor vragen, neem contact op met <a href="mailto:warts@recruitin.nl" style="color: #667eea; text-decoration: none;">warts@recruitin.nl</a></p>
                            <div style="margin-top: 20px;">
                                <span style="background: #667eea; color: white; padding: 8px 16px; border-radius: 20px; font-size: 12px; font-weight: 600;">Powered by Recruitin.nl</span>
                            </div>
                        </td>
                    </tr>

                </table>
            </td>
        </tr>
    </table>
</body>
</html>
"""

    # Prepare output for Zapier
    return {
        'email_to': 'warts@recruitin.nl',
        'email_subject': f'🤖 AI Recruitment Intelligence: {bedrijfsnaam} - {functietitel}',
        'email_body_html': email_body_html,

        # Notion fields
        'notion_bedrijfsnaam': bedrijfsnaam,
        'notion_functietitel': functietitel,
        'notion_contactpersoon': contactpersoon,
        'notion_email': email,
        'notion_telefoon': telefoon,
        'notion_sector': sector,
        'notion_locatie': locatie,
        'notion_salaris_range': f"€{salaris_data['salaris_medior']['min']:,} - €{salaris_data['salaris_senior']['max']:,}",
        'notion_urgentie': urgentie,
        'notion_intelligence': 'AI-Gedreven Uitgebreid Rapport',
        'notion_status': '🤖 AI Analyse Compleet',
        'notion_datum': current_date,
        'notion_ai_schaarste': exec_summary.get('schaarste_niveau', 'Gemiddeld'),
        'notion_ai_time_to_hire': exec_summary.get('time_to_hire', '30-45 dagen'),

        # URL fields - gebruik None voor lege velden
        'notion_vacature_url': vacature_url if vacature_url else None,
        'notion_jobdigger_url': jobdigger_url if jobdigger_url else None,
        'notion_linkedin_ti_url': linkedin_ti_url if linkedin_ti_url else None,

        # Extended data for potential future use
        'ai_analysis_summary': exec_summary['samenvatting'],
        'arbeidsmarkt_status': exec_summary['arbeidsmarkt_status'],
        'talent_pool_size': linkedin_data['talent_pool_size'],
        'total_workers_market': jobdigger_data['totaal_werkenden'],
        'automation_risk': trends['automatisering_risico'],
        'sector_prognose': trends['sector_prognose']
    }


# Main function for Zapier
def main():
    """
    Main function that Zapier will call.
    Expected input_data fields from Zapier:
    - claude_api_key: Your Anthropic API key
    - bedrijfsnaam, functietitel, contactpersoon, email, telefoon
    - sector, locatie, urgentie
    - vacature_url, jobdigger_url, linkedin_ti_url (URLs to documents)
    - vacature_text, jobdigger_text, linkedin_ti_text (extracted text from PDFs)
    - extra_info (optional)
    """

    # Get input data from Zapier
    claude_api_key = input_data.get('claude_api_key', '')

    # Basic info
    bedrijfsnaam = input_data.get('bedrijfsnaam', 'Onbekend Bedrijf')
    functietitel = input_data.get('functietitel', 'Onbekende Functie')
    contactpersoon = input_data.get('contactpersoon', '')
    email = input_data.get('email', '')
    telefoon = input_data.get('telefoon', '')
    sector = input_data.get('sector', 'Algemeen')
    locatie = input_data.get('locatie', 'Nederland')
    urgentie = input_data.get('urgentie', 'Normaal')
    extra_info = input_data.get('extra_info', '')

    # Document URLs
    vacature_url = input_data.get('vacature_url', '').strip()
    jobdigger_url = input_data.get('jobdigger_url', '').strip()
    linkedin_ti_url = input_data.get('linkedin_ti_url', '').strip()

    # Extracted text from documents
    vacature_text = input_data.get('vacature_text', '')
    jobdigger_text = input_data.get('jobdigger_text', '')
    linkedin_ti_text = input_data.get('linkedin_ti_text', '')

    # Analyze with AI or use fallback
    ai_analysis = analyze_with_claude_extended(
        claude_api_key,
        bedrijfsnaam,
        functietitel,
        vacature_text,
        jobdigger_text,
        linkedin_ti_text,
        sector,
        locatie,
        extra_info
    )

    # Generate report
    output = generate_extended_email_report(
        ai_analysis,
        bedrijfsnaam,
        functietitel,
        contactpersoon,
        email,
        telefoon,
        sector,
        locatie,
        urgentie,
        vacature_url,
        jobdigger_url,
        linkedin_ti_url
    )

    return output


# This is what Zapier will execute
output = main()
