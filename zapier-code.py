# Zapier Code by Zapier - Python
# Stap 2: Process JotForm data and generate HTML email

import json

# Get JotForm data from previous step
form_data = input_data

# Extract form fields (adjust field IDs based on your JotForm)
bedrijf = form_data.get('bedrijfsnaam', 'Niet opgegeven')
functie = form_data.get('functietitel', 'Niet opgegeven')
locatie = form_data.get('locatie', 'Niet opgegeven')
ervaring = form_data.get('ervaringNiveau', 'Niet opgegeven')
sector = form_data.get('sector', 'Niet opgegeven')
skills = form_data.get('vaardigheden', '')
salaris_min = form_data.get('minSalaris', '')
salaris_max = form_data.get('maxSalaris', '')
contact_naam = form_data.get('naam', '')
contact_email = form_data.get('email', '')

# Format salary range
if salaris_min and salaris_max:
    salaris_range = f"€{salaris_min:,} - €{salaris_max:,}"
else:
    salaris_range = "Niet opgegeven"

# Generate Claude AI Analysis (placeholder - replace with actual API call)
ai_analyse = f"""
<p><strong>Marktanalyse voor {functie}:</strong></p>
<p>Op basis van de huidige arbeidsmarkt in {locatie} zien we dat de vraag naar {functie} professionals hoog is.
De sector {sector} toont sterke groei met uitdagende recruitment kansen.</p>

<p><strong>Belangrijkste bevindingen:</strong></p>
<ul style="margin: 8px 0; padding-left: 24px;">
    <li style="margin: 6px 0;">Hoge concurrentie voor ervaren kandidaten ({ervaring})</li>
    <li style="margin: 6px 0;">Vaardigheden zoals {skills} zijn zeer gewild</li>
    <li style="margin: 6px 0;">Gemiddelde time-to-hire: 6-8 weken</li>
    <li style="margin: 6px 0;">Kandidaten verwachten hybride werkmodellen</li>
</ul>
"""

# Market status
markt_status = "Kandidaatmarkt - Hoge concurrentie voor talent"

# Recommendations
aanbevelingen = """
<ul style="margin: 8px 0; padding-left: 24px;">
    <li style="margin: 8px 0;"><strong>Salarispositionering:</strong> Bied competitieve salarissen aan om top talent aan te trekken</li>
    <li style="margin: 8px 0;"><strong>Employer Branding:</strong> Versterk je werkgeversmerk via LinkedIn en andere kanalen</li>
    <li style="margin: 8px 0;"><strong>Snelheid:</strong> Verkort je recruitmentproces om kandidaten niet te verliezen aan concurrenten</li>
    <li style="margin: 8px 0;"><strong>Flexibiliteit:</strong> Toon mogelijkheden voor remote/hybride werken</li>
    <li style="margin: 8px 0;"><strong>Ontwikkeling:</strong> Benadruk groeimogelijkheden en trainingen</li>
</ul>

<p style="margin-top: 16px; padding: 16px; background-color: #FFF7ED; border-left: 4px solid #EF7D00; border-radius: 4px;">
    <strong>💡 Volgende stap:</strong> Plan een gratis 15-minuten adviesgesprek om deze inzichten om te zetten naar concrete recruitment acties.
</p>
"""

# HTML Email Template with inline CSS
html_email = f"""<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recruitment Intelligence Rapport</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif; background-color: #f3f4f6; line-height: 1.6;">

    <!-- Main Container -->
    <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="background-color: #f3f4f6; padding: 40px 20px;">
        <tr>
            <td align="center">

                <!-- Email Content -->
                <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="max-width: 650px; background-color: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">

                    <!-- Header -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #4B4F51 0%, #77797B 100%); padding: 40px 40px; text-align: center;">
                            <h1 style="margin: 0; color: #ffffff; font-size: 28px; font-weight: 700; letter-spacing: -0.5px;">
                                🎯 Recruitment Intelligence Rapport
                            </h1>
                            <p style="margin: 10px 0 0 0; color: #e5e7eb; font-size: 16px;">
                                Arbeidsmarkt Analyse • Powered by Claude AI
                            </p>
                        </td>
                    </tr>

                    <!-- Orange Accent Bar -->
                    <tr>
                        <td style="background-color: #EF7D00; height: 6px;"></td>
                    </tr>

                    <!-- Executive Summary -->
                    <tr>
                        <td style="padding: 40px 40px 20px 40px;">
                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="background-color: #FFF7ED; border-left: 4px solid #EF7D00; border-radius: 8px;">
                                <tr>
                                    <td style="padding: 24px;">
                                        <h2 style="margin: 0 0 16px 0; color: #1f2937; font-size: 22px; font-weight: 700;">
                                            📊 Executive Summary
                                        </h2>
                                        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                            <tr>
                                                <td style="padding: 8px 0; color: #374151; font-size: 15px;">
                                                    <strong style="color: #1f2937;">Bedrijf:</strong> {bedrijf}
                                                </td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 8px 0; color: #374151; font-size: 15px;">
                                                    <strong style="color: #1f2937;">Functie:</strong> {functie}
                                                </td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 8px 0; color: #374151; font-size: 15px;">
                                                    <strong style="color: #1f2937;">Locatie:</strong> {locatie}
                                                </td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 8px 0; color: #374151; font-size: 15px;">
                                                    <strong style="color: #1f2937;">Ervaring:</strong> {ervaring}
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- AI Analysis -->
                    <tr>
                        <td style="padding: 20px 40px;">
                            <h2 style="margin: 0 0 16px 0; color: #1f2937; font-size: 22px; font-weight: 700; border-bottom: 2px solid #f3f4f6; padding-bottom: 12px;">
                                🤖 Claude AI Analyse
                            </h2>
                            <div style="color: #374151; font-size: 15px; line-height: 1.8;">
                                {ai_analyse}
                            </div>
                        </td>
                    </tr>

                    <!-- Market Insights -->
                    <tr>
                        <td style="padding: 20px 40px;">
                            <h2 style="margin: 0 0 16px 0; color: #1f2937; font-size: 22px; font-weight: 700; border-bottom: 2px solid #f3f4f6; padding-bottom: 12px;">
                                📈 Arbeidsmarkt Inzichten
                            </h2>
                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                <tr>
                                    <td style="padding: 12px; background-color: #f9fafb; border-radius: 6px; margin-bottom: 8px;">
                                        <strong style="color: #EF7D00;">💰 Salaris Range:</strong>
                                        <span style="color: #374151; font-size: 15px;">{salaris_range}</span>
                                    </td>
                                </tr>
                                <tr><td style="height: 8px;"></td></tr>
                                <tr>
                                    <td style="padding: 12px; background-color: #f9fafb; border-radius: 6px;">
                                        <strong style="color: #EF7D00;">📊 Markt Status:</strong>
                                        <span style="color: #374151; font-size: 15px;">{markt_status}</span>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Recommendations -->
                    <tr>
                        <td style="padding: 20px 40px;">
                            <h2 style="margin: 0 0 16px 0; color: #1f2937; font-size: 22px; font-weight: 700; border-bottom: 2px solid #f3f4f6; padding-bottom: 12px;">
                                💡 Aanbevelingen
                            </h2>
                            <div style="color: #374151; font-size: 15px; line-height: 1.8;">
                                {aanbevelingen}
                            </div>
                        </td>
                    </tr>

                    <!-- CTA Button -->
                    <tr>
                        <td style="padding: 30px 40px;">
                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                                <tr>
                                    <td align="center" style="background: linear-gradient(135deg, #EF7D00 0%, #d97706 100%); border-radius: 8px; padding: 16px 32px;">
                                        <a href="https://recruitin.com/contact" style="color: #ffffff; text-decoration: none; font-weight: 600; font-size: 16px; display: block;">
                                            📞 Plan een Gratis Adviesgesprek →
                                        </a>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Footer -->
                    <tr>
                        <td style="background-color: #f9fafb; padding: 30px 40px; text-align: center; border-top: 1px solid #e5e7eb;">
                            <p style="margin: 0 0 8px 0; color: #4B4F51; font-weight: 700; font-size: 18px;">
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

# Return output for next Zapier step (Gmail)
output = {{
    'html_body': html_email,
    'subject': f'🎯 Recruitment Intelligence: {functie} bij {bedrijf}',
    'contact_naam': contact_naam,
    'contact_email': contact_email,
    'bedrijf': bedrijf,
    'functie': functie
}}
