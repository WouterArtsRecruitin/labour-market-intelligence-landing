# ================================================================
# RECRUITIN - DEMO RAPPORT EMAIL
# Zapier Code by Zapier - Stap 2
# Gebruikt fixed demo rapport (GEEN Claude AI - gratis!)
# ================================================================

import json
import datetime

# ========================================
# CONFIGURATION
# ========================================
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
        salaris_range = "€55.000 - €75.000"
        salaris_p25 = "€50.000 - €60.000"
        salaris_p75 = "€75.000 - €90.000"
else:
    salaris_range = "€55.000 - €75.000"
    salaris_p25 = "€50.000 - €60.000"
    salaris_p75 = "€75.000 - €90.000"

# ========================================
# DEMO RAPPORT DATA (Email-Compatible HTML)
# Gebaseerd op demo-rapport.html maar met inline CSS
# ========================================

# Attachments
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
                📎 Bijgevoegde Documenten
            </h2>
            <ul style="margin: 0; padding-left: 24px; color: #374151;">
                {"".join(links)}
            </ul>
        </td>
    </tr>
    """

# Extra info
extra_info_html = ""
if extra_info:
    extra_info_html = f"""
    <tr>
        <td style="padding: 0 40px 30px 40px;">
            <div style="background-color: #FFF7ED; border-left: 4px solid #EF7D00; border-radius: 8px; padding: 20px;">
                <h3 style="margin: 0 0 12px 0; color: #1f2937; font-size: 18px; font-weight: 700;">📝 Extra Informatie van Klant</h3>
                <p style="margin: 0; color: #374151; font-size: 15px; line-height: 1.6; white-space: pre-wrap;">{extra_info}</p>
            </div>
        </td>
    </tr>
    """

# ========================================
# PROFESSIONAL EMAIL WITH DEMO RAPPORT DESIGN
# ========================================

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
                                Arbeidsmarkt Intelligence Rapport
                            </h1>
                            <p style="margin: 0; color: #d1d5db; font-size: 16px;">
                                Labour Market Analysis • Professional Edition
                            </p>
                            <div style="margin-top: 20px; display: inline-block; background-color: #10b981; color: white; padding: 10px 20px; border-radius: 20px; font-weight: 700; font-size: 13px;">
                                Data Betrouwbaarheid: 92%
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
                                            📊 Executive Summary
                                        </h2>
                                        <p style="margin: 8px 0; color: #374151; font-size: 16px; line-height: 1.6;">
                                            <strong style="color: #1f2937;">Vacature:</strong> {functietitel}<br>
                                            <strong style="color: #1f2937;">Bedrijf:</strong> {bedrijfsnaam}<br>
                                            <strong style="color: #1f2937;">Locatie:</strong> {locatie}<br>
                                            <strong style="color: #1f2937;">Aantal posities:</strong> {aantal_posities}
                                        </p>
                                        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin-top: 20px; background-color: #ffffff; border: 1px solid #fed7aa; border-radius: 8px;">
                                            <tr>
                                                <td style="padding: 16px;">
                                                    <p style="margin: 0 0 5px 0; font-weight: 600; color: #1f2937; font-size: 15px;">Markt Status:</p>
                                                    <p style="margin: 0; color: #EF7D00; font-weight: 700; font-size: 20px;">Kandidaatmarkt - Hoge concurrentie voor talent</p>
                                                </td>
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
                                        <p style="margin: 6px 0; color: #374151; font-size: 15px;">
                                            <strong style="color: #1f2937;">Urgentie:</strong> <span style="color: #dc2626; font-weight: 700;">{urgentie}</span>
                                        </p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    {extra_info_html}

                    <!-- Labour Market Status - 3 Cards -->
                    <tr>
                        <td style="padding: 0 40px 30px 40px;">
                            <h2 style="margin: 0 0 20px 0; color: #1f2937; font-size: 24px; font-weight: 700; border-bottom: 2px solid #e5e7eb; padding-bottom: 12px;">
                                📈 Arbeidsmarkt Status
                            </h2>
                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                <tr>
                                    <td width="32%" valign="top" style="background-color: #fef2f2; padding: 20px; border-radius: 12px; border: 2px solid #fecaca; text-align: center;">
                                        <div style="font-size: 32px; margin-bottom: 10px;">⚠️</div>
                                        <h3 style="margin: 0 0 8px 0; color: #7f1d1d; font-size: 15px; font-weight: 700;">Schaarste</h3>
                                        <div style="color: #dc2626; font-size: 28px; font-weight: 700; margin: 8px 0;">Hoog</div>
                                        <p style="margin: 0; color: #991b1b; font-size: 12px;">2,3 vacatures per kandidaat</p>
                                    </td>
                                    <td width="2%"></td>
                                    <td width="32%" valign="top" style="background-color: #fff7ed; padding: 20px; border-radius: 12px; border: 2px solid #fed7aa; text-align: center;">
                                        <div style="font-size: 32px; margin-bottom: 10px;">⏱️</div>
                                        <h3 style="margin: 0 0 8px 0; color: #7c2d12; font-size: 15px; font-weight: 700;">Time-to-Hire</h3>
                                        <div style="color: #ea580c; font-size: 28px; font-weight: 700; margin: 8px 0;">45-65 dagen</div>
                                        <p style="margin: 0; color: #c2410c; font-size: 12px;">Sector gemiddelde</p>
                                    </td>
                                    <td width="2%"></td>
                                    <td width="32%" valign="top" style="background-color: #eff6ff; padding: 20px; border-radius: 12px; border: 2px solid #bfdbfe; text-align: center;">
                                        <div style="font-size: 32px; margin-bottom: 10px;">👥</div>
                                        <h3 style="margin: 0 0 8px 0; color: #1e3a8a; font-size: 15px; font-weight: 700;">Beschikbaarheid</h3>
                                        <div style="color: #2563eb; font-size: 28px; font-weight: 700; margin: 8px 0;">±1.200</div>
                                        <p style="margin: 0; color: #1d4ed8; font-size: 12px;">Geschikte kandidaten NL</p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Salary Benchmark -->
                    <tr>
                        <td style="padding: 0 40px 30px 40px;">
                            <h2 style="margin: 0 0 20px 0; color: #1f2937; font-size: 24px; font-weight: 700; border-bottom: 2px solid #e5e7eb; padding-bottom: 12px;">
                                💰 Salaris Benchmark
                            </h2>
                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="background: linear-gradient(135deg, #EF7D00 0%, #ea580c 100%); border-radius: 12px; box-shadow: 0 4px 12px rgba(239, 125, 0, 0.3);">
                                <tr>
                                    <td style="padding: 32px; color: #ffffff;">
                                        <p style="margin: 0 0 10px 0; font-size: 13px; font-weight: 600; opacity: 0.9;">Markt Mediaan (P50)</p>
                                        <div style="font-size: 40px; font-weight: 700; margin: 10px 0;">{salaris_range}</div>
                                        <p style="margin: 0 0 20px 0; font-size: 13px; opacity: 0.9;">Bruto jaarsalaris, exclusief bonus & secundair</p>
                                        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="border-top: 1px solid rgba(255,255,255,0.3); padding-top: 16px; margin-top: 16px;">
                                            <tr>
                                                <td width="48%" style="padding: 8px 0;">
                                                    <p style="margin: 0; font-size: 12px; opacity: 0.8;">P25 (Junior Senior)</p>
                                                    <p style="margin: 4px 0 0 0; font-size: 16px; font-weight: 700;">{salaris_p25}</p>
                                                </td>
                                                <td width="4%"></td>
                                                <td width="48%" style="padding: 8px 0;">
                                                    <p style="margin: 0; font-size: 12px; opacity: 0.8;">P75 (Top talent)</p>
                                                    <p style="margin: 4px 0 0 0; font-size: 16px; font-weight: 700;">{salaris_p75}</p>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Recruitment Strategy -->
                    <tr>
                        <td style="padding: 0 40px 30px 40px;">
                            <h2 style="margin: 0 0 20px 0; color: #1f2937; font-size: 24px; font-weight: 700; border-bottom: 2px solid #e5e7eb; padding-bottom: 12px;">
                                🎯 Aanbevolen Recruitment Strategie
                            </h2>
                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                <tr>
                                    <td style="padding: 20px; background-color: #eff6ff; border-radius: 12px; border: 1px solid #bfdbfe;">
                                        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                            <tr>
                                                <td width="50" valign="top" style="font-size: 32px;">💼</td>
                                                <td valign="top">
                                                    <h3 style="margin: 0 0 8px 0; color: #1e40af; font-size: 16px; font-weight: 700;">Active Sourcing Vereist</h3>
                                                    <p style="margin: 0; color: #374151; font-size: 14px; line-height: 1.6;">
                                                        Slechts 12% van geschikte kandidaten is actief op zoek. Direct benaderen van passieve kandidaten is essentieel voor succes.
                                                    </p>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                                <tr><td style="height: 12px;"></td></tr>
                                <tr>
                                    <td style="padding: 20px; background-color: #f0fdf4; border-radius: 12px; border: 1px solid #bbf7d0;">
                                        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                            <tr>
                                                <td width="50" valign="top" style="font-size: 32px;">⚡</td>
                                                <td valign="top">
                                                    <h3 style="margin: 0 0 8px 0; color: #15803d; font-size: 16px; font-weight: 700;">Snelheid is Kritiek</h3>
                                                    <p style="margin: 0; color: #374151; font-size: 14px; line-height: 1.6;">
                                                        Time-to-hire van 45-65 dagen betekent dat snelle besluitvorming en efficiënte processen cruciaal zijn.
                                                    </p>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                                <tr><td style="height: 12px;"></td></tr>
                                <tr>
                                    <td style="padding: 20px; background-color: #fef2f2; border-radius: 12px; border: 1px solid #fecaca;">
                                        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                            <tr>
                                                <td width="50" valign="top" style="font-size: 32px;">💰</td>
                                                <td valign="top">
                                                    <h3 style="margin: 0 0 8px 0; color: #991b1b; font-size: 16px; font-weight: 700;">Competitief Salaris Pakket</h3>
                                                    <p style="margin: 0; color: #374151; font-size: 14px; line-height: 1.6;">
                                                        In een kandidaatmarkt moet je minimaal marktconform bieden. Overweeg bonus structuren en equity voor top talent.
                                                    </p>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
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
                                            <li>Review arbeidsmarkt analyse</li>
                                            <li>Bel {contactpersoon} ({telefoon})</li>
                                            <li>Bespreek recruitment strategie</li>
                                            <li>Start active sourcing</li>
                                        </ol>
                                        <p style="margin: 16px 0 0 0; color: #ffffff; font-size: 14px; opacity: 0.9;">
                                            💡 Plan een gratis 15-minuten adviesgesprek voor concrete acties.
                                        </p>
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
                                📧 info@recruitin.com | 🌐 <a href="https://recruitin.com" style="color: #EF7D00; text-decoration: none;">recruitin.com</a>
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
# OUTPUT FOR ZAPIER
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
    'notion_intelligence': 'Demo Rapport - Fixed Data',
    'notion_jobdigger_url': jobdigger_url,
    'notion_linkedin_url': linkedin_ti_url,
    'notion_jotform_url': submission_url,
    'notion_submission_id': submission_id,
    'notion_datum': datetime.datetime.now().strftime('%Y-%m-%d')
}
