# ================================================================
# RECRUITIN - AI RECRUITMENT INTELLIGENCE
# Zapier Code by Zapier - Stap 2
# Combineert: Claude AI + Professional Email Design + Notion Data
# ================================================================

import json
import datetime
import requests

# ========================================
# CONFIGURATION
# ⚠️ IMPORTANT: Vul deze waarden in binnen Zapier!
# ========================================
CLAUDE_API_KEY = "JOUW_CLAUDE_API_KEY_HIER"  # ← Vul in Zapier in
RECRUITER_EMAIL = "warts@recruitin.nl"

# ========================================
# EXTRACT INPUT DATA FROM JOTFORM
# ========================================
bedrijfsnaam = input_data.get('bedrijfsnaam', 'Niet opgegeven')
contactpersoon = input_data.get('contactpersoon', '')
email = input_data.get('email', '')
telefoon = input_data.get('telefoon', '')
functietitel = input_data.get('functietitel', 'Niet opgegeven')
locatie = input_data.get('locatie', 'Nederland')
salaris_min = input_data.get('salaris_min', '')
salaris_max = input_data.get('salaris_max', '')
urgentie = input_data.get('urgentie', 'Normaal')
aantal_posities = input_data.get('aantal_posities', '1')
jobdigger_url = input_data.get('jobdigger_url', '')
linkedin_ti_url = input_data.get('linkedin_ti_url', '')
extra_info = input_data.get('extra_info', '')
submission_url = input_data.get('submission_url', '')
submission_id = input_data.get('submission_id', '')

# Format salary
if salaris_min and salaris_max:
    try:
        min_val = int(salaris_min)
        max_val = int(salaris_max)
        salaris_range = f"€{min_val:,} - €{max_val:,}".replace(',', '.')
        salaris_p25 = f"€{int(min_val * 0.9):,} - €{int(min_val * 1.05):,}".replace(',', '.')
        salaris_p75 = f"€{int(max_val * 1.05):,} - €{int(max_val * 1.2):,}".replace(',', '.')
    except:
        salaris_range = "Op aanvraag"
        salaris_p25 = "Op aanvraag"
        salaris_p75 = "Op aanvraag"
else:
    salaris_range = "Op aanvraag"
    salaris_p25 = "Op aanvraag"
    salaris_p75 = "Op aanvraag"

# ========================================
# IMPROVED AI PROMPT
# ========================================
prompt = f"""Je bent een senior recruitment intelligence analist gespecialiseerd in de Nederlandse arbeidsmarkt. Genereer een data-gedreven arbeidsmarkt analyse.

**VACATURE DATA:**
Bedrijf: {bedrijfsnaam}
Functie: {functietitel}
Locatie: {locatie}
Salaris: {salaris_range}
Urgentie: {urgentie}
Aantal posities: {aantal_posities}
Extra context: {extra_info}

**GENEREER EEN GESTRUCTUREERD RAPPORT:**

## 📊 ARBEIDSMARKT STATUS
- Schaarste (1-10): [cijfer + uitleg]
- Vraag/Aanbod ratio: [aantal vacatures vs kandidaten]
- Time-to-hire: [dagen]
- Beschikbare kandidaten NL: [schatting]

## 💰 SALARIS ANALYSE
- Markt mediaan: [bedrag]
- Beoordeling opgegeven salaris: [onder/marktconform/boven markt]
- Aanbeveling: [concreet advies]

## 🎯 KANDIDAAT PROFIEL
- Typische achtergrond: [opleiding, ervaring]
- Must-have competenties: [top 3]
- Marktbeschikbaarheid: [percentage]

## 📈 RECRUITMENT STRATEGIE
**Beste kanalen:**
1. [Kanaal + waarom]
2. [Kanaal + waarom]
3. [Kanaal + waarom]

**Sourcing:**
- Actief zoekend: [%]
- Aanbeveling: [active sourcing/job ads]

## ⚠️ UITDAGINGEN & OPLOSSINGEN
1. [Uitdaging]: [oplossing]
2. [Uitdaging]: [oplossing]

## 📅 TIJDLIJN
- Week 1: [acties]
- Week 2-4: [acties]
- Verwachte hire: [tijdsindicatie]

Gebruik concrete cijfers. Focus op NL arbeidsmarkt 2025."""

# ========================================
# CALL CLAUDE API
# ========================================
intelligence = ""
api_success = False

try:
    response = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "Content-Type": "application/json",
            "x-api-key": CLAUDE_API_KEY,
            "anthropic-version": "2023-06-01"
        },
        json={
            "model": "claude-sonnet-4-5-20250929",
            "max_tokens": 2048,
            "messages": [{"role": "user", "content": prompt}]
        },
        timeout=25
    )

    if response.status_code == 200:
        intelligence = response.json()["content"][0]["text"]
        api_success = True
    else:
        intelligence = f"⚠️ API Error {response.status_code}"

except requests.exceptions.Timeout:
    intelligence = "⚠️ API Timeout - Probeer opnieuw"

except Exception as e:
    intelligence = f"⚠️ Error: {str(e)[:200]}"

# Fallback if too short
if len(intelligence) < 100:
    intelligence += f"\n\n**BASIS ADVIES:**\n- Review vacature\n- Contact {contactpersoon}\n- Check markt salaris\n- Start LinkedIn sourcing"

# ========================================
# PROFESSIONAL EMAIL TEMPLATE
# ========================================

# Attachments section
attachments_html = ""
if jobdigger_url or linkedin_ti_url:
    links = []
    if jobdigger_url:
        links.append(f'<li style="margin: 8px 0;"><a href="{jobdigger_url}" style="color: #EF7D00; text-decoration: none;">📄 Jobdigger PDF</a></li>')
    if linkedin_ti_url:
        links.append(f'<li style="margin: 8px 0;"><a href="{linkedin_ti_url}" style="color: #EF7D00; text-decoration: none;">📄 LinkedIn TI PDF</a></li>')
    attachments_html = f"""
    <tr>
        <td style="padding: 20px 40px 30px 40px;">
            <h2 style="margin: 0 0 16px 0; color: #1f2937; font-size: 22px; font-weight: 700; border-bottom: 2px solid #e5e7eb; padding-bottom: 12px;">
                📎 Uploads
            </h2>
            <ul style="margin: 0; padding-left: 24px; color: #374151;">
                {"".join(links)}
            </ul>
        </td>
    </tr>
    """

# Extra info section
extra_info_html = ""
if extra_info:
    extra_info_html = f"""
    <tr>
        <td style="padding: 0 40px 30px 40px;">
            <div style="background-color: #FFF7ED; border-left: 4px solid #EF7D00; border-radius: 8px; padding: 20px;">
                <h3 style="margin: 0 0 12px 0; color: #1f2937; font-size: 18px; font-weight: 700;">📝 Extra Informatie</h3>
                <p style="margin: 0; color: #374151; font-size: 15px; line-height: 1.6; white-space: pre-wrap;">{extra_info}</p>
            </div>
        </td>
    </tr>
    """

api_status = "✅ Succesvol" if api_success else "⚠️ Gefaald"

email_body_html = f"""<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin: 0; padding: 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif; background-color: #f3f4f6;">

    <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="background-color: #f3f4f6; padding: 20px;">
        <tr>
            <td align="center">
                <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="max-width: 700px; background-color: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);">

                    <!-- Header -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #4B4F51 0%, #77797B 50%, #4B4F51 100%); padding: 40px; text-align: center;">
                            <h1 style="margin: 0 0 10px 0; color: #ffffff; font-size: 32px; font-weight: 700;">
                                🎯 Recruitment Intelligence
                            </h1>
                            <p style="margin: 0; color: #d1d5db; font-size: 16px;">
                                AI-Powered Labour Market Analysis
                            </p>
                            <div style="margin-top: 20px; display: inline-block; background-color: #10b981; color: white; padding: 10px 20px; border-radius: 20px; font-weight: 700; font-size: 13px;">
                                API Status: {api_status}
                            </div>
                        </td>
                    </tr>

                    <!-- Orange Bar -->
                    <tr>
                        <td style="background-color: #EF7D00; height: 6px;"></td>
                    </tr>

                    <!-- Executive Summary -->
                    <tr>
                        <td style="padding: 40px;">
                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="background-color: #FFF7ED; border-left: 4px solid #EF7D00; border-radius: 8px;">
                                <tr>
                                    <td style="padding: 30px;">
                                        <h2 style="margin: 0 0 20px 0; color: #1f2937; font-size: 24px; font-weight: 700;">
                                            📊 Opdracht Details
                                        </h2>
                                        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                            <tr>
                                                <td style="padding: 6px 0; color: #6b7280; font-size: 15px; width: 35%;">Bedrijf:</td>
                                                <td style="padding: 6px 0; color: #1f2937; font-weight: 600; font-size: 15px;"><strong>{bedrijfsnaam}</strong></td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 6px 0; color: #6b7280; font-size: 15px;">Functie:</td>
                                                <td style="padding: 6px 0; color: #EF7D00; font-weight: 700; font-size: 16px;">{functietitel}</td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 6px 0; color: #6b7280; font-size: 15px;">Locatie:</td>
                                                <td style="padding: 6px 0; color: #1f2937; font-weight: 600; font-size: 15px;">{locatie}</td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 6px 0; color: #6b7280; font-size: 15px;">Salaris:</td>
                                                <td style="padding: 6px 0; color: #1f2937; font-weight: 600; font-size: 15px;">{salaris_range}</td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 6px 0; color: #6b7280; font-size: 15px;">Urgentie:</td>
                                                <td style="padding: 6px 0; color: #dc2626; font-weight: 700; font-size: 15px;">{urgentie}</td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 6px 0; color: #6b7280; font-size: 15px;">Posities:</td>
                                                <td style="padding: 6px 0; color: #1f2937; font-weight: 600; font-size: 15px;">{aantal_posities}</td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Contact Info -->
                    <tr>
                        <td style="padding: 0 40px 30px 40px;">
                            <h2 style="margin: 0 0 16px 0; color: #1f2937; font-size: 22px; font-weight: 700; border-bottom: 2px solid #e5e7eb; padding-bottom: 12px;">
                                👤 Contactpersoon
                            </h2>
                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="background-color: #f9fafb; border-radius: 8px; border: 1px solid #e5e7eb;">
                                <tr>
                                    <td style="padding: 20px;">
                                        <p style="margin: 6px 0; color: #374151; font-size: 15px;">
                                            <strong style="color: #1f2937;">Naam:</strong> {contactpersoon}
                                        </p>
                                        <p style="margin: 6px 0; color: #374151; font-size: 15px;">
                                            <strong style="color: #1f2937;">Email:</strong> <a href="mailto:{email}" style="color: #EF7D00; text-decoration: none;">{email}</a>
                                        </p>
                                        <p style="margin: 6px 0; color: #374151; font-size: 15px;">
                                            <strong style="color: #1f2937;">Telefoon:</strong> <a href="tel:{telefoon}" style="color: #EF7D00; text-decoration: none;">{telefoon}</a>
                                        </p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    {extra_info_html}

                    <!-- AI Intelligence -->
                    <tr>
                        <td style="padding: 0 40px 30px 40px;">
                            <h2 style="margin: 0 0 20px 0; color: #1f2937; font-size: 24px; font-weight: 700; border-bottom: 2px solid #e5e7eb; padding-bottom: 12px;">
                                🤖 Claude AI Analyse
                            </h2>
                            <div style="background-color: #ffffff; border: 2px solid #667eea; border-radius: 12px; padding: 24px;">
                                <div style="color: #374151; font-size: 15px; line-height: 1.8; white-space: pre-wrap;">{intelligence}</div>
                            </div>
                        </td>
                    </tr>

                    {attachments_html}

                    <!-- Call to Action -->
                    <tr>
                        <td style="padding: 30px 40px;">
                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="background: linear-gradient(135deg, #EF7D00 0%, #d97706 100%); border-radius: 12px;">
                                <tr>
                                    <td style="padding: 24px;">
                                        <h3 style="margin: 0 0 12px 0; color: #ffffff; font-size: 20px; font-weight: 700;">
                                            ⚡ Volgende Stappen
                                        </h3>
                                        <ol style="margin: 0; padding-left: 20px; color: #ffffff; font-size: 15px; line-height: 1.8;">
                                            <li>Review AI analyse</li>
                                            <li>Bel {contactpersoon} ({telefoon})</li>
                                            <li>Bespreek recruitment strategie</li>
                                            <li>Start sourcing</li>
                                        </ol>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Footer -->
                    <tr>
                        <td style="background-color: #f9fafb; padding: 30px 40px; text-align: center; border-top: 1px solid #e5e7eb;">
                            <p style="margin: 0 0 8px 0; color: #4B4F51; font-weight: 700; font-size: 20px;">
                                Recruitin
                            </p>
                            <p style="margin: 0 0 16px 0; color: #6b7280; font-size: 14px;">
                                AI-Powered Recruitment Intelligence
                            </p>
                            <p style="margin: 0; color: #6b7280; font-size: 13px;">
                                📧 info@recruitin.com | 📞 {telefoon}
                            </p>
                            <p style="margin: 12px 0 0 0; color: #9ca3af; font-size: 12px;">
                                {datetime.datetime.now().strftime('%d-%m-%Y %H:%M')} •
                                <a href="{submission_url}" style="color: #EF7D00; text-decoration: none;">Jotform #{submission_id}</a>
                            </p>
                        </td>
                    </tr>

                </table>
            </td>
        </tr>
    </table>

</body>
</html>"""

# ========================================
# PREPARE OUTPUT FOR NEXT STEPS
# ========================================
output = {
    'email_to': RECRUITER_EMAIL,
    'email_subject': f"🎯 Recruitment Intelligence: {functietitel} bij {bedrijfsnaam}",
    'email_body_html': email_body_html,
    'notion_bedrijfsnaam': bedrijfsnaam,
    'notion_contactpersoon': contactpersoon,
    'notion_email': email,
    'notion_telefoon': telefoon,
    'notion_functietitel': functietitel,
    'notion_locatie': locatie,
    'notion_salaris_range': salaris_range,
    'notion_urgentie': urgentie,
    'notion_aantal_posities': aantal_posities,
    'notion_status': '🆕 Nieuwe Aanvraag',
    'notion_intelligence': intelligence[:10000],
    'notion_jobdigger_url': jobdigger_url,
    'notion_linkedin_url': linkedin_ti_url,
    'notion_jotform_url': submission_url,
    'notion_submission_id': submission_id,
    'notion_datum': datetime.datetime.now().strftime('%Y-%m-%d'),
    'api_success': str(api_success),
    'api_model': 'claude-sonnet-4-5-20250929'
}
