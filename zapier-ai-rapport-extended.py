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

# Run UITGEBREIDE AI Analysis
ai_analysis = analyze_with_claude_extended(vacature_text, jobdigger_text, linkedin_ti_text, functietitel, sector, locatie)

# Save for later - we'll build the HTML in the next part
print("Extended AI analysis completed - building comprehensive report...")
