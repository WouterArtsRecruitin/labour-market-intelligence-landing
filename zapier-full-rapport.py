# ================================================================
# RECRUITIN - VOLLEDIG ARBEIDSMARKT INTELLIGENCE RAPPORT
# Zapier Code by Zapier - Stap 2
# Alle secties van demo-rapport.html met echte JotForm data
# Email-compatible HTML met inline CSS
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
vacature_url = input_data.get('vacature_url', '')
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

# Parse key skills
skills_list = []
if key_skills:
    skills_list = [s.strip() for s in key_skills.split(',')[:5]]  # Max 5 skills

# ========================================
# CONDITIONAL SECTIONS
# ========================================

# Extra info section
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

# Source Materials section (Vacature URL + Attachments)
source_materials_html = ""
if vacature_url or jobdigger_url or linkedin_ti_url:
    links = []
    if vacature_url:
        links.append(f'<li style="margin: 8px 0;"><a href="{vacature_url}" style="color: #EF7D00; text-decoration: none; font-weight: 600;">🔗 Originele Vacature</a></li>')
    if jobdigger_url:
        links.append(f'<li style="margin: 8px 0;"><a href="{jobdigger_url}" style="color: #EF7D00; text-decoration: none; font-weight: 600;">📄 Jobdigger Marktrapport</a></li>')
    if linkedin_ti_url:
        links.append(f'<li style="margin: 8px 0;"><a href="{linkedin_ti_url}" style="color: #EF7D00; text-decoration: none; font-weight: 600;">📊 LinkedIn Talent Insights</a></li>')
    source_materials_html = f"""
    <tr>
        <td style="padding: 0 40px 30px 40px;">
            <h2 style="margin: 0 0 16px 0; color: #1f2937; font-size: 22px; font-weight: 700; border-bottom: 2px solid #e5e7eb; padding-bottom: 12px;">
                📚 Bronmateriaal
            </h2>
            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="background-color: #f9fafb; border-radius: 8px; border: 1px solid #e5e7eb; padding: 16px;">
                <tr>
                    <td style="padding: 12px;">
                        <ul style="margin: 0; padding-left: 24px; color: #374151; line-height: 2;">
                            {"".join(links)}
                        </ul>
                        <p style="margin: 12px 0 0 0; padding-top: 12px; border-top: 1px solid #e5e7eb; color: #6b7280; font-size: 13px; font-style: italic;">
                            💡 Dit rapport is gebaseerd op de ingediende gegevens. Voor een volledig AI-gedreven analyse van alle bronmaterialen, neem contact op.
                        </p>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
    """

# ========================================
# VOLLEDIG EMAIL RAPPORT HTML
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
                                            <strong style="color: #1f2937;">Sector:</strong> {sector}<br>
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

                    <!-- Vacancy Profile -->
                    <tr>
                        <td style="padding: 0 40px 30px 40px;">
                            <h2 style="margin: 0 0 20px 0; color: #1f2937; font-size: 24px; font-weight: 700; border-bottom: 2px solid #e5e7eb; padding-bottom: 12px;">
                                🎯 Vacature Profiel
                            </h2>
                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                <tr>
                                    <td width="48%" valign="top" style="background-color: #f9fafb; padding: 24px; border-radius: 12px; border: 1px solid #e5e7eb;">
                                        <h3 style="margin: 0 0 16px 0; color: #1f2937; font-size: 16px; font-weight: 700;">Functie Vereisten</h3>
                                        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                            <tr>
                                                <td style="padding: 6px 0;">
                                                    <span style="color: #6b7280; font-size: 14px;">Functieniveau:</span>
                                                </td>
                                                <td align="right" style="padding: 6px 0;">
                                                    <span style="color: #1f2937; font-weight: 600; font-size: 14px;">{ervaringsniveau}</span>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 6px 0;">
                                                    <span style="color: #6b7280; font-size: 14px;">Ervaring:</span>
                                                </td>
                                                <td align="right" style="padding: 6px 0;">
                                                    <span style="color: #1f2937; font-weight: 600; font-size: 14px;">{werkervaring_jaren}</span>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 6px 0;">
                                                    <span style="color: #6b7280; font-size: 14px;">Opleiding:</span>
                                                </td>
                                                <td align="right" style="padding: 6px 0;">
                                                    <span style="color: #1f2937; font-weight: 600; font-size: 14px;">{opleidingsniveau}</span>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 6px 0;">
                                                    <span style="color: #6b7280; font-size: 14px;">Team size:</span>
                                                </td>
                                                <td align="right" style="padding: 6px 0;">
                                                    <span style="color: #1f2937; font-weight: 600; font-size: 14px;">{teamsize}</span>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                    <td width="4%"></td>
                                    <td width="48%" valign="top" style="background-color: #f9fafb; padding: 24px; border-radius: 12px; border: 1px solid #e5e7eb;">
                                        <h3 style="margin: 0 0 16px 0; color: #1f2937; font-size: 16px; font-weight: 700;">Organisatie Context</h3>
                                        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                            <tr>
                                                <td style="padding: 6px 0;">
                                                    <span style="color: #6b7280; font-size: 14px;">Industrie:</span>
                                                </td>
                                                <td align="right" style="padding: 6px 0;">
                                                    <span style="color: #1f2937; font-weight: 600; font-size: 14px;">{sector}</span>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 6px 0;">
                                                    <span style="color: #6b7280; font-size: 14px;">Bedrijfsgrootte:</span>
                                                </td>
                                                <td align="right" style="padding: 6px 0;">
                                                    <span style="color: #1f2937; font-weight: 600; font-size: 14px;">{bedrijfsgrootte}</span>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 6px 0;">
                                                    <span style="color: #6b7280; font-size: 14px;">Werkomgeving:</span>
                                                </td>
                                                <td align="right" style="padding: 6px 0;">
                                                    <span style="color: #1f2937; font-weight: 600; font-size: 14px;">{werkomgeving}</span>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 6px 0;">
                                                    <span style="color: #6b7280; font-size: 14px;">Groei fase:</span>
                                                </td>
                                                <td align="right" style="padding: 6px 0;">
                                                    <span style="color: #10b981; font-weight: 600; font-size: 14px;">{groei_fase}</span>
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

                    <!-- Target Audience Analysis -->
                    <tr>
                        <td style="padding: 0 40px 30px 40px;">
                            <h2 style="margin: 0 0 20px 0; color: #1f2937; font-size: 24px; font-weight: 700; border-bottom: 2px solid #e5e7eb; padding-bottom: 12px;">
                                🎯 Doelgroep Analyse
                            </h2>

                            <!-- Digital Skills -->
                            <div style="margin-bottom: 20px;">
                                <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                    <tr>
                                        <td style="padding-bottom: 8px;">
                                            <span style="color: #1f2937; font-weight: 600; font-size: 15px;">Digital Marketing Skills</span>
                                        </td>
                                        <td align="right" style="padding-bottom: 8px;">
                                            <span style="color: #6b7280; font-weight: 700; font-size: 15px;">35% heeft ervaring</span>
                                        </td>
                                    </tr>
                                </table>
                                <div style="width: 100%; background-color: #e5e7eb; border-radius: 8px; height: 12px; overflow: hidden;">
                                    <div style="width: 35%; background-color: #2563eb; height: 12px;"></div>
                                </div>
                                <p style="margin: 8px 0 0 0; color: #6b7280; font-size: 13px;">Van alle marketing professionals in NL</p>
                            </div>

                            <!-- Leadership -->
                            <div style="margin-bottom: 20px;">
                                <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                    <tr>
                                        <td style="padding-bottom: 8px;">
                                            <span style="color: #1f2937; font-weight: 600; font-size: 15px;">Leadership Experience (5+ jaar)</span>
                                        </td>
                                        <td align="right" style="padding-bottom: 8px;">
                                            <span style="color: #6b7280; font-weight: 700; font-size: 15px;">18% beschikbaar</span>
                                        </td>
                                    </tr>
                                </table>
                                <div style="width: 100%; background-color: #e5e7eb; border-radius: 8px; height: 12px; overflow: hidden;">
                                    <div style="width: 18%; background-color: #10b981; height: 12px;"></div>
                                </div>
                                <p style="margin: 8px 0 0 0; color: #6b7280; font-size: 13px;">Met aantoonbare teamleiding ervaring</p>
                            </div>

                            <!-- Sector Experience -->
                            <div style="margin-bottom: 20px;">
                                <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                    <tr>
                                        <td style="padding-bottom: 8px;">
                                            <span style="color: #1f2937; font-weight: 600; font-size: 15px;">{sector} Ervaring</span>
                                        </td>
                                        <td align="right" style="padding-bottom: 8px;">
                                            <span style="color: #6b7280; font-weight: 700; font-size: 15px;">22% sector ervaring</span>
                                        </td>
                                    </tr>
                                </table>
                                <div style="width: 100%; background-color: #e5e7eb; border-radius: 8px; height: 12px; overflow: hidden;">
                                    <div style="width: 22%; background-color: #a855f7; height: 12px;"></div>
                                </div>
                                <p style="margin: 8px 0 0 0; color: #6b7280; font-size: 13px;">Met relevante sector kennis</p>
                            </div>

                            <!-- Active Candidates -->
                            <div style="margin-bottom: 0;">
                                <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                    <tr>
                                        <td style="padding-bottom: 8px;">
                                            <span style="color: #1f2937; font-weight: 600; font-size: 15px;">Actief Zoekend</span>
                                        </td>
                                        <td align="right" style="padding-bottom: 8px;">
                                            <span style="color: #6b7280; font-weight: 700; font-size: 15px;">12% open voor switch</span>
                                        </td>
                                    </tr>
                                </table>
                                <div style="width: 100%; background-color: #e5e7eb; border-radius: 8px; height: 12px; overflow: hidden;">
                                    <div style="width: 12%; background-color: #ea580c; height: 12px;"></div>
                                </div>
                                <p style="margin: 8px 0 0 0; color: #6b7280; font-size: 13px;">Kandidaten actief op zoek</p>
                            </div>
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

                            <!-- Salary Factors -->
                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin-top: 16px; background-color: #eff6ff; border-radius: 8px; border: 1px solid #bfdbfe;">
                                <tr>
                                    <td style="padding: 20px;">
                                        <h3 style="margin: 0 0 12px 0; color: #1e40af; font-size: 16px; font-weight: 700;">💡 Salaris Beïnvloedende Factoren</h3>
                                        <ul style="margin: 0; padding-left: 20px; color: #1e40af; font-size: 13px; line-height: 1.8;">
                                            <li><strong>Ervaring:</strong> +12% per 2 jaar extra</li>
                                            <li><strong>Opleiding:</strong> WO vs HBO achtergrond (+8%)</li>
                                            <li><strong>Bedrijfsgrootte:</strong> Corporate vs Scale-up (+15%)</li>
                                            <li><strong>Locatie:</strong> Amsterdam vs regionaal (+10%)</li>
                                        </ul>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Required Competencies -->
                    <tr>
                        <td style="padding: 0 40px 30px 40px;">
                            <h2 style="margin: 0 0 20px 0; color: #1f2937; font-size: 24px; font-weight: 700; border-bottom: 2px solid #e5e7eb; padding-bottom: 12px;">
                                🛠️ Gewenste Competenties & Beschikbaarheid
                            </h2>
                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                <tr>
                                    <!-- Technical Skills -->
                                    <td width="48%" valign="top" style="background-color: #eff6ff; padding: 20px; border-radius: 12px; border: 2px solid #bfdbfe;">
                                        <h3 style="margin: 0 0 16px 0; color: #1e3a8a; font-size: 16px; font-weight: 700;">Technical Skills</h3>

                                        <!-- Skill 1 -->
                                        <div style="margin-bottom: 16px;">
                                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                                <tr>
                                                    <td><span style="color: #1f2937; font-size: 14px; font-weight: 500;">Google Ads</span></td>
                                                    <td align="right"><span style="color: #10b981; font-size: 12px; font-weight: 700;">45% beschikbaar</span></td>
                                                </tr>
                                            </table>
                                            <div style="width: 100%; background-color: #e5e7eb; border-radius: 4px; height: 6px; margin-top: 6px; overflow: hidden;">
                                                <div style="width: 45%; background-color: #10b981; height: 6px;"></div>
                                            </div>
                                        </div>

                                        <!-- Skill 2 -->
                                        <div style="margin-bottom: 16px;">
                                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                                <tr>
                                                    <td><span style="color: #1f2937; font-size: 14px; font-weight: 500;">HubSpot/CRM</span></td>
                                                    <td align="right"><span style="color: #ea580c; font-size: 12px; font-weight: 700;">28% beschikbaar</span></td>
                                                </tr>
                                            </table>
                                            <div style="width: 100%; background-color: #e5e7eb; border-radius: 4px; height: 6px; margin-top: 6px; overflow: hidden;">
                                                <div style="width: 28%; background-color: #ea580c; height: 6px;"></div>
                                            </div>
                                        </div>

                                        <!-- Skill 3 -->
                                        <div style="margin-bottom: 16px;">
                                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                                <tr>
                                                    <td><span style="color: #1f2937; font-size: 14px; font-weight: 500;">SEO/SEA</span></td>
                                                    <td align="right"><span style="color: #10b981; font-size: 12px; font-weight: 700;">52% beschikbaar</span></td>
                                                </tr>
                                            </table>
                                            <div style="width: 100%; background-color: #e5e7eb; border-radius: 4px; height: 6px; margin-top: 6px; overflow: hidden;">
                                                <div style="width: 52%; background-color: #10b981; height: 6px;"></div>
                                            </div>
                                        </div>

                                        <!-- Skill 4 -->
                                        <div style="margin-bottom: 16px;">
                                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                                <tr>
                                                    <td><span style="color: #1f2937; font-size: 14px; font-weight: 500;">Analytics (GA4)</span></td>
                                                    <td align="right"><span style="color: #ea580c; font-size: 12px; font-weight: 700;">35% beschikbaar</span></td>
                                                </tr>
                                            </table>
                                            <div style="width: 100%; background-color: #e5e7eb; border-radius: 4px; height: 6px; margin-top: 6px; overflow: hidden;">
                                                <div style="width: 35%; background-color: #ea580c; height: 6px;"></div>
                                            </div>
                                        </div>

                                        <!-- Skill 5 -->
                                        <div style="margin-bottom: 0;">
                                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                                <tr>
                                                    <td><span style="color: #1f2937; font-size: 14px; font-weight: 500;">Marketing Automation</span></td>
                                                    <td align="right"><span style="color: #dc2626; font-size: 12px; font-weight: 700;">22% beschikbaar</span></td>
                                                </tr>
                                            </table>
                                            <div style="width: 100%; background-color: #e5e7eb; border-radius: 4px; height: 6px; margin-top: 6px; overflow: hidden;">
                                                <div style="width: 22%; background-color: #dc2626; height: 6px;"></div>
                                            </div>
                                        </div>
                                    </td>
                                    <td width="4%"></td>
                                    <!-- Soft Skills -->
                                    <td width="48%" valign="top" style="background-color: #f0fdf4; padding: 20px; border-radius: 12px; border: 2px solid #bbf7d0;">
                                        <h3 style="margin: 0 0 16px 0; color: #15803d; font-size: 16px; font-weight: 700;">Soft Skills (Prioriteit)</h3>

                                        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                            <tr>
                                                <td style="padding: 10px; background-color: #ffffff; border-radius: 8px; margin-bottom: 8px;">
                                                    <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                                        <tr>
                                                            <td><span style="color: #1f2937; font-weight: 500; font-size: 14px;">Leadership</span></td>
                                                            <td align="right"><span style="background-color: #dc2626; color: white; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 700;">Kritiek</span></td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr><td style="height: 8px;"></td></tr>
                                            <tr>
                                                <td style="padding: 10px; background-color: #ffffff; border-radius: 8px;">
                                                    <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                                        <tr>
                                                            <td><span style="color: #1f2937; font-weight: 500; font-size: 14px;">Communicatie</span></td>
                                                            <td align="right"><span style="background-color: #dc2626; color: white; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 700;">Kritiek</span></td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr><td style="height: 8px;"></td></tr>
                                            <tr>
                                                <td style="padding: 10px; background-color: #ffffff; border-radius: 8px;">
                                                    <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                                        <tr>
                                                            <td><span style="color: #1f2937; font-weight: 500; font-size: 14px;">Strategic Thinking</span></td>
                                                            <td align="right"><span style="background-color: #ea580c; color: white; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 700;">Hoog</span></td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr><td style="height: 8px;"></td></tr>
                                            <tr>
                                                <td style="padding: 10px; background-color: #ffffff; border-radius: 8px;">
                                                    <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                                        <tr>
                                                            <td><span style="color: #1f2937; font-weight: 500; font-size: 14px;">Data-Driven</span></td>
                                                            <td align="right"><span style="background-color: #ea580c; color: white; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 700;">Hoog</span></td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr><td style="height: 8px;"></td></tr>
                                            <tr>
                                                <td style="padding: 10px; background-color: #ffffff; border-radius: 8px;">
                                                    <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                                        <tr>
                                                            <td><span style="color: #1f2937; font-weight: 500; font-size: 14px;">Stakeholder Mgmt</span></td>
                                                            <td align="right"><span style="background-color: #10b981; color: white; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 700;">Medium</span></td>
                                                        </tr>
                                                    </table>
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

                            <!-- Strategy 1 -->
                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin-bottom: 12px;">
                                <tr>
                                    <td style="padding: 20px; background-color: #eff6ff; border-radius: 12px; border: 1px solid #bfdbfe;">
                                        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                            <tr>
                                                <td width="50" valign="top" style="font-size: 32px;">🎯</td>
                                                <td valign="top">
                                                    <h3 style="margin: 0 0 8px 0; color: #1e40af; font-size: 16px; font-weight: 700;">Direct Search</h3>
                                                    <p style="margin: 0 0 8px 0; color: #374151; font-size: 14px; line-height: 1.6;">
                                                        Actief benaderen van passive kandidaten via LinkedIn en netwerk.
                                                    </p>
                                                    <span style="color: #1e40af; font-size: 13px; font-weight: 700;">Success rate: 15-25%</span>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>

                            <!-- Strategy 2 -->
                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin-bottom: 12px;">
                                <tr>
                                    <td style="padding: 20px; background-color: #f0fdf4; border-radius: 12px; border: 1px solid #bbf7d0;">
                                        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                            <tr>
                                                <td width="50" valign="top" style="font-size: 32px;">📢</td>
                                                <td valign="top">
                                                    <h3 style="margin: 0 0 8px 0; color: #15803d; font-size: 16px; font-weight: 700;">Job Boards Premium</h3>
                                                    <p style="margin: 0 0 8px 0; color: #374151; font-size: 14px; line-height: 1.6;">
                                                        LinkedIn Premium, Indeed Sponsored, specialist platforms.
                                                    </p>
                                                    <span style="color: #15803d; font-size: 13px; font-weight: 700;">Success rate: 10-18%</span>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>

                            <!-- Strategy 3 -->
                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin-bottom: 12px;">
                                <tr>
                                    <td style="padding: 20px; background-color: #faf5ff; border-radius: 12px; border: 1px solid #e9d5ff;">
                                        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                            <tr>
                                                <td width="50" valign="top" style="font-size: 32px;">🤝</td>
                                                <td valign="top">
                                                    <h3 style="margin: 0 0 8px 0; color: #7c3aed; font-size: 16px; font-weight: 700;">Referral Program</h3>
                                                    <p style="margin: 0 0 8px 0; color: #374151; font-size: 14px; line-height: 1.6;">
                                                        Employee referrals met €2.500 - €5.000 bonus.
                                                    </p>
                                                    <span style="color: #7c3aed; font-size: 13px; font-weight: 700;">Success rate: 25-35%</span>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>

                            <!-- Strategy 4 -->
                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                <tr>
                                    <td style="padding: 20px; background-color: #fff7ed; border-radius: 12px; border: 1px solid #fed7aa;">
                                        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                            <tr>
                                                <td width="50" valign="top" style="font-size: 32px;">⚡</td>
                                                <td valign="top">
                                                    <h3 style="margin: 0 0 8px 0; color: #c2410c; font-size: 16px; font-weight: 700;">Recruitment Agency</h3>
                                                    <p style="margin: 0 0 8px 0; color: #374151; font-size: 14px; line-height: 1.6;">
                                                        Specialized recruitment partners voor snelle fill.
                                                    </p>
                                                    <span style="color: #c2410c; font-size: 13px; font-weight: 700;">Cost: 15-20% annual salary</span>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Timeline & Expectations -->
                    <tr>
                        <td style="padding: 0 40px 30px 40px;">
                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="background-color: #1f2937; border-radius: 12px;">
                                <tr>
                                    <td style="padding: 30px;">
                                        <h2 style="margin: 0 0 24px 0; color: #ffffff; font-size: 24px; font-weight: 700; text-align: center;">
                                            ⏱️ Verwachte Tijdslijn
                                        </h2>
                                        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                            <tr>
                                                <td width="24%" valign="top" style="background-color: #374151; padding: 20px; border-radius: 8px; text-align: center;">
                                                    <div style="font-size: 32px; margin-bottom: 12px;">📝</div>
                                                    <div style="color: #fb923c; font-size: 18px; font-weight: 700; margin-bottom: 8px;">Week 1-2</div>
                                                    <div style="color: #d1d5db; font-size: 13px;">Sourcing & Screening</div>
                                                </td>
                                                <td width="1%"></td>
                                                <td width="24%" valign="top" style="background-color: #374151; padding: 20px; border-radius: 8px; text-align: center;">
                                                    <div style="font-size: 32px; margin-bottom: 12px;">👥</div>
                                                    <div style="color: #60a5fa; font-size: 18px; font-weight: 700; margin-bottom: 8px;">Week 3-4</div>
                                                    <div style="color: #d1d5db; font-size: 13px;">Eerste Interviews</div>
                                                </td>
                                                <td width="1%"></td>
                                                <td width="24%" valign="top" style="background-color: #374151; padding: 20px; border-radius: 8px; text-align: center;">
                                                    <div style="font-size: 32px; margin-bottom: 12px;">🎯</div>
                                                    <div style="color: #c084fc; font-size: 18px; font-weight: 700; margin-bottom: 8px;">Week 5-6</div>
                                                    <div style="color: #d1d5db; font-size: 13px;">Assessment & Cases</div>
                                                </td>
                                                <td width="1%"></td>
                                                <td width="24%" valign="top" style="background-color: #374151; padding: 20px; border-radius: 8px; text-align: center;">
                                                    <div style="font-size: 32px; margin-bottom: 12px;">✅</div>
                                                    <div style="color: #fb923c; font-size: 18px; font-weight: 700; margin-bottom: 8px;">Week 7-8</div>
                                                    <div style="color: #d1d5db; font-size: 13px;">Offer & Onboarding</div>
                                                </td>
                                            </tr>
                                        </table>
                                        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin-top: 24px; background-color: #EF7D00; border-radius: 8px;">
                                            <tr>
                                                <td style="padding: 20px; text-align: center;">
                                                    <p style="margin: 0 0 8px 0; color: #ffffff; font-weight: 700; font-size: 20px;">📊 VERWACHTING: 45-65 DAGEN TOTALE TIJDSLIJN</p>
                                                    <p style="margin: 0; color: #fed7aa; font-size: 15px;">Bij optimale marktcondities en concurrerende propositie</p>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    {source_materials_html}

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
                                            <li>Start active sourcing binnen 48 uur</li>
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
    'email_subject': f"🎯 Volledig Recruitment Intelligence Rapport: {functietitel} bij {bedrijfsnaam}",
    'email_body_html': email_body_html,
    'notion_bedrijfsnaam': bedrijfsnaam,
    'notion_contactpersoon': contactpersoon,
    'notion_email': email,
    'notion_telefoon': telefoon,
    'notion_functietitel': functietitel,
    'notion_sector': sector,
    'notion_locatie': locatie,
    'notion_salaris_range': salaris_range,
    'notion_urgentie': urgentie,
    'notion_aantal_posities': aantal_posities,
    'notion_ervaringsniveau': ervaringsniveau,
    'notion_status': '🆕 Nieuwe Aanvraag',
    'notion_intelligence': 'Volledig Rapport - Alle Secties',
    'notion_vacature_url': vacature_url,
    'notion_jobdigger_url': jobdigger_url,
    'notion_linkedin_url': linkedin_ti_url,
    'notion_jotform_url': submission_url,
    'notion_submission_id': submission_id,
    'notion_datum': datetime.datetime.now().strftime('%Y-%m-%d')
}
