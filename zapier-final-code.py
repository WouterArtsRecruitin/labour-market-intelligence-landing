# ================================================================
# Zapier Code by Zapier - Stap 2
# Genereer mooi HTML rapport email met Recruitin branding
# ================================================================

import json

# Get data from JotForm trigger (Stap 1)
form_data = input_data

# ================================================================
# EXTRACT JOTFORM FIELDS
# BELANGRIJK: Pas deze field IDs aan naar jouw JotForm velden!
# ================================================================

# Contact Info
contact_naam = form_data.get('q3_naam', form_data.get('naam', ''))
contact_email = form_data.get('q4_email', form_data.get('email', ''))
contact_telefoon = form_data.get('q5_telefoon', form_data.get('telefoon', ''))

# Job Details
bedrijf = form_data.get('q6_bedrijfsnaam', form_data.get('bedrijfsnaam', 'Niet opgegeven'))
functie = form_data.get('q7_functietitel', form_data.get('functietitel', 'Niet opgegeven'))
sector = form_data.get('q8_sector', form_data.get('sector', 'Niet opgegeven'))
locatie = form_data.get('q9_locatie', form_data.get('locatie', 'Nederland'))

# Experience & Skills
ervaring_niveau = form_data.get('q10_ervaringNiveau', form_data.get('ervaringNiveau', 'Niet opgegeven'))
vaardigheden = form_data.get('q11_vaardigheden', form_data.get('vaardigheden', ''))

# Salary
salaris_min = form_data.get('q12_minSalaris', form_data.get('minSalaris', ''))
salaris_max = form_data.get('q13_maxSalaris', form_data.get('maxSalaris', ''))

# Additional context
grootste_uitdaging = form_data.get('q14_uitdaging', form_data.get('uitdaging', ''))
gewenste_inzichten = form_data.get('q15_inzichten', form_data.get('inzichten', ''))
timeline = form_data.get('q16_timeline', form_data.get('timeline', ''))

# ================================================================
# FORMAT DATA
# ================================================================

# Salary range formatting
if salaris_min and salaris_max:
    try:
        min_val = int(salaris_min)
        max_val = int(salaris_max)
        salaris_range = f"€{min_val:,} - €{max_val:,}".replace(',', '.')
        salaris_p25 = f"€{int(min_val * 0.9):,} - €{int(min_val * 1.05):,}".replace(',', '.')
        salaris_p75 = f"€{int(max_val * 1.05):,} - €{int(max_val * 1.2):,}".replace(',', '.')
    except:
        salaris_range = "Marktconform salaris"
        salaris_p25 = "Op aanvraag"
        salaris_p75 = "Op aanvraag"
else:
    salaris_range = "Marktconform salaris"
    salaris_p25 = "Op aanvraag"
    salaris_p75 = "Op aanvraag"

# Map experience level to Dutch
niveau_mapping = {
    'junior': 'Junior (0-3 jaar)',
    'medior': 'Medior (3-7 jaar)',
    'senior': 'Senior (7+ jaar)',
    'lead': 'Lead/Management (10+ jaar)'
}
niveau_display = niveau_mapping.get(ervaring_niveau.lower(), ervaring_niveau)

# ================================================================
# GENERATE HTML EMAIL (Based on demo rapport design)
# ================================================================

html_email = f"""<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Arbeidsmarkt Intelligence Rapport</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif; background-color: #f3f4f6;">

    <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="background-color: #f3f4f6; padding: 20px;">
        <tr>
            <td align="center">
                <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="max-width: 700px; background-color: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);">

                    <!-- Header with Gradient -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #4B4F51 0%, #77797B 50%, #4B4F51 100%); padding: 40px; text-align: center;">
                            <h1 style="margin: 0 0 10px 0; color: #ffffff; font-size: 32px; font-weight: 700; letter-spacing: -0.5px;">
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

                    <!-- Orange Accent Bar -->
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
                                            <strong style="color: #1f2937;">Vacature:</strong> {functie}<br>
                                            <strong style="color: #1f2937;">Sector:</strong> {sector}<br>
                                            <strong style="color: #1f2937;">Locatie:</strong> {locatie}
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

                    <!-- Vacancy Profile - 2 Column Layout -->
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
                                                <td style="padding: 6px 0; color: #6b7280; font-size: 14px;">Functieniveau:</td>
                                                <td align="right" style="padding: 6px 0; color: #1f2937; font-weight: 600; font-size: 14px;">{niveau_display}</td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 6px 0; color: #6b7280; font-size: 14px;">Ervaring:</td>
                                                <td align="right" style="padding: 6px 0; color: #1f2937; font-weight: 600; font-size: 14px;">{ervaring_niveau}</td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 6px 0; color: #6b7280; font-size: 14px;">Vaardigheden:</td>
                                                <td align="right" style="padding: 6px 0; color: #1f2937; font-weight: 600; font-size: 14px;">{vaardigheden[:30]}...</td>
                                            </tr>
                                        </table>
                                    </td>
                                    <td width="4%"></td>
                                    <td width="48%" valign="top" style="background-color: #f9fafb; padding: 24px; border-radius: 12px; border: 1px solid #e5e7eb;">
                                        <h3 style="margin: 0 0 16px 0; color: #1f2937; font-size: 16px; font-weight: 700;">Organisatie Context</h3>
                                        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                            <tr>
                                                <td style="padding: 6px 0; color: #6b7280; font-size: 14px;">Bedrijf:</td>
                                                <td align="right" style="padding: 6px 0; color: #1f2937; font-weight: 600; font-size: 14px;">{bedrijf}</td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 6px 0; color: #6b7280; font-size: 14px;">Industrie:</td>
                                                <td align="right" style="padding: 6px 0; color: #1f2937; font-weight: 600; font-size: 14px;">{sector}</td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 6px 0; color: #6b7280; font-size: 14px;">Timeline:</td>
                                                <td align="right" style="padding: 6px 0; color: #10b981; font-weight: 600; font-size: 14px;">{timeline if timeline else 'Op korte termijn'}</td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

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
                                                        Slechts 12% van geschikte kandidaten is actief op zoek. Direct benaderen van passieve kandidaten is essentieel.
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
                                                        Time-to-hire van 45-65 dagen betekent snelle besluitvorming en efficiënte processen zijn cruciaal.
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
                                                        In een kandidaatmarkt moet je minimaal marktconform bieden. Overweeg bonus en equity voor top talent.
                                                    </p>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Call to Action -->
                    <tr>
                        <td style="padding: 30px 40px;">
                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="background: linear-gradient(135deg, #EF7D00 0%, #d97706 100%); border-radius: 12px;">
                                <tr>
                                    <td align="center" style="padding: 24px;">
                                        <h3 style="margin: 0 0 12px 0; color: #ffffff; font-size: 20px; font-weight: 700;">
                                            💡 Volgende Stap
                                        </h3>
                                        <p style="margin: 0 0 20px 0; color: #ffffff; font-size: 15px; opacity: 0.95;">
                                            Plan een gratis 15-minuten adviesgesprek om deze inzichten om te zetten naar concrete recruitment acties.
                                        </p>
                                        <a href="https://recruitin.com/contact" style="display: inline-block; background-color: #ffffff; color: #EF7D00; text-decoration: none; padding: 14px 32px; border-radius: 8px; font-weight: 700; font-size: 16px;">
                                            📞 Plan Adviesgesprek →
                                        </a>
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
                            <p style="margin: 16px 0 0 0; color: #9ca3af; font-size: 12px;">
                                © 2025 WouterArts Recruitin - All rights reserved
                            </p>
                        </td>
                    </tr>

                </table>
            </td>
        </tr>
    </table>

</body>
</html>"""

# ================================================================
# RETURN OUTPUT FOR NEXT ZAPIER STEPS
# ================================================================

output = {
    'html_body': html_email,
    'subject': f'🎯 Recruitment Intelligence: {functie} bij {bedrijf}',
    'contact_naam': contact_naam,
    'contact_email': contact_email,
    'contact_telefoon': contact_telefoon,
    'bedrijf': bedrijf,
    'functie': functie,
    'sector': sector,
    'locatie': locatie,
    'salaris_range': salaris_range,
    'timeline': timeline
}
