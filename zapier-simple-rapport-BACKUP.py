"""
ZAPIER STEP 5: SIMPLE READABLE REPORT
======================================
Version: 4.0 - Simple & Clean (No fancy styling)
"""

import json
import os
from datetime import datetime
import requests

# API Configuration
# ⚠️ IMPORTANT: Replace with YOUR Anthropic API key
# Get your key from: https://console.anthropic.com/settings/keys
CLAUDE_API_KEY = "sk-ant-api03-YOUR_API_KEY_HERE"  # Replace this!
CLAUDE_API_URL = "https://api.anthropic.com/v1/messages"
CLAUDE_MODEL = "claude-sonnet-4-20250514"

print(f"✅ API key loaded")

# =====================================
# CLAUDE PROMPT (same as before)
# =====================================

def build_analysis_prompt(job_title, location, company, email, vacancy_url,
                          jobdigger_pdf, linkedin_pdf, vacancy_text):
    current_date = datetime.now().strftime("%d %B %Y om %H:%M")

    prompt = f"""Je bent een Elite Nederlandse Arbeidsmarkt Intelligence Expert met 15+ jaar ervaring.

INPUT DATA:
- Functietitel: {job_title}
- Locatie: {location}
- Bedrijf: {company or 'Niet opgegeven'}

Jobdigger PDF: {jobdigger_pdf[:8000] if jobdigger_pdf else 'Geen data'}
LinkedIn PDF: {linkedin_pdf[:8000] if linkedin_pdf else 'Geen data'}
Vacaturetekst: {vacancy_text[:5000] if vacancy_text else 'Geen data'}

RETURN EXACT JSON:
{{
  "executive_summary": {{
    "markt_assessment": "[2-3 zinnen]",
    "time_to_hire_range": "XX-XX dagen",
    "actieve_kandidaten": XXX,
    "urgentie": "Kritiek|Hoog|Normaal",
    "recruitment_classificatie": "Executive Schaarste|High Demand|Normaal"
  }},
  "market_intelligence_dashboard": {{
    "talent_schaarste_index": "X.X",
    "time_to_hire_min": XX,
    "time_to_hire_max": XX,
    "success_rate_pct": XX,
    "markt_actie_window_days": XX,
    "markt_status": "Extreem hete markt|Krappe markt|Normaal",
    "actie_urgentie": "onmiddellijke actie|spoedige actie|normaal"
  }},
  "salary_intelligence": {{
    "p25_junior": XXXX,
    "p50_mediaan": XXXX,
    "p75_senior": XXXX,
    "bonus_avg_pct": XX
  }},
  "total_compensation": {{
    "components": {{
      "base_salary": XXXX,
      "variable_bonus_pct": XX,
      "stock_options_pct": XX,
      "pension_employer_pct": 8.5,
      "lease_auto_eligibility_pct": XX,
      "home_office_allowance_yearly": 950
    }},
    "growth_benefits": {{
      "salary_growth_1yr_pct": XX,
      "salary_growth_3yr_pct": XX,
      "talent_scarcity_factor": "X.X",
      "avg_notice_period": "1-2 maanden"
    }}
  }},
  "workforce_availability": {{
    "actief_werkzoekend": {{"percentage": XX, "aantal": XXX, "description": "Direct beschikbaar"}},
    "latent_werkzoekend": {{"percentage": XX, "aantal": XXX, "description": "Open voor kansen"}},
    "niet_werkzoekend": {{"percentage": XX, "aantal": XXX, "description": "Tevreden in rol"}},
    "total_candidates": XXXX
  }},
  "demographics": {{
    "leeftijd": {{
      "25-35": {{"percentage": XX, "aantal": XXX}},
      "36-45": {{"percentage": XX, "aantal": XXX}},
      "46-55": {{"percentage": XX, "aantal": XXX}},
      "55+": {{"percentage": XX, "aantal": XXX}}
    }},
    "opleiding": {{
      "MBO": {{"percentage": XX, "aantal": XXX}},
      "HBO": {{"percentage": XX, "aantal": XXX}},
      "WO": {{"percentage": XX, "aantal": XXX}}
    }}
  }},
  "motivation_drivers": {{
    "autonomy_influence": XX, "financial_rewards": XX, "work_life_balance": XX,
    "career_growth": XX, "innovation_tech": XX, "team_culture": XX,
    "company_reputation": XX, "meaningful_impact": XX
  }},
  "recruitment_strategy": {{
    "primary_channel": "Executive search|LinkedIn Premium|Jobboards",
    "secondary_channels": "Professional netwerken|Referrals",
    "timeline_weeks_min": XX, "timeline_weeks_max": XX,
    "budget_range_min_k": XX, "budget_range_max_k": XX
  }},
  "strategic_priorities": [
    {{"title": "Compensation", "description": "Target €X-X"}},
    {{"title": "Sourcing", "description": "Channel mix"}},
    {{"title": "Timeline", "description": "Launch binnen X dagen"}},
    {{"title": "Success Rate", "description": "Target XX%"}}
  ],
  "meta": {{
    "generated_date": "{current_date}",
    "reliability_score": XX,
    "data_sources_count": XXX,
    "ai_model": "Claude AI Sonnet 4"
  }}
}}

BEREKENINGSLOGICA NL 2025:
Schaarste: Tech 7-9, Management 7-9, Productie 5-7, Sales 4-6
Time-to-hire: Tech 60-120d, Management 75-120d, Productie 45-75d
Salary: Junior €2.5-3.5k, Medior €3.5-5.5k, Senior €5.5-7.5k
Workforce: Tech 20/40/40%, Management 15/35/50%, Productie 25/45/30%
Opleiding: Tech 15/60/25%, Management 10/50/40%, Productie 60/35/5%

Return ALLEEN valid JSON!"""

    return prompt

def call_claude_api(prompt):
    headers = {
        'x-api-key': CLAUDE_API_KEY,
        'anthropic-version': '2023-06-01',
        'content-type': 'application/json'
    }

    payload = {
        'model': CLAUDE_MODEL,
        'max_tokens': 16000,
        'temperature': 0.3,
        'messages': [{'role': 'user', 'content': prompt}]
    }

    print("🤖 Calling Claude API...")
    response = requests.post(CLAUDE_API_URL, headers=headers, json=payload, timeout=120)

    if response.status_code != 200:
        raise Exception(f"Claude API error {response.status_code}: {response.text}")

    result = response.json()
    print(f"✅ Claude API success!")
    return result['content'][0]['text']

def clean_json_response(text):
    text = text.strip()
    if text.startswith('```json'):
        text = text[7:]
    elif text.startswith('```'):
        text = text[3:]
    if text.endswith('```'):
        text = text[:-3]
    return text.strip()

# =====================================
# SIMPLE HTML REPORT
# =====================================

def generate_simple_html(data, job_title, location):
    """Simple, readable HTML - no fancy styling"""

    def fmt(amount):
        return f"€{amount:,}".replace(',', '.')

    base = data['total_compensation']['components']['base_salary']
    bonus_pct = data['total_compensation']['components']['variable_bonus_pct']
    bonus_amount = int(base * bonus_pct / 100)

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 20px auto; padding: 20px; background: #f5f5f5; }}
.container {{ background: white; padding: 30px; border-radius: 5px; }}
h1 {{ color: #2c3e50; font-size: 24px; border-bottom: 3px solid #FF6B35; padding-bottom: 10px; }}
h2 {{ color: #34495e; font-size: 20px; margin-top: 30px; border-bottom: 2px solid #ddd; padding-bottom: 8px; }}
h3 {{ color: #555; font-size: 16px; margin-top: 20px; }}
.highlight {{ background: #FFF3E0; padding: 15px; border-left: 4px solid #FF6B35; margin: 15px 0; }}
.salary-box {{ background: #FF6B35; color: white; padding: 20px; text-align: center; border-radius: 5px; margin: 20px 0; }}
.salary-box h2 {{ color: white; border: none; margin: 0; }}
.salary-main {{ font-size: 48px; font-weight: bold; margin: 15px 0; }}
.grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin: 15px 0; }}
.box {{ background: #f8f9fa; padding: 15px; border-radius: 5px; border-left: 3px solid #3498db; }}
table {{ width: 100%; border-collapse: collapse; margin: 15px 0; }}
td {{ padding: 10px; border-bottom: 1px solid #eee; }}
td:first-child {{ font-weight: bold; width: 40%; }}
.footer {{ background: #2c3e50; color: white; padding: 20px; text-align: center; margin-top: 30px; border-radius: 5px; }}
.footer a {{ color: #FF6B35; text-decoration: none; }}
</style>
</head>
<body>
<div class="container">

<h1>AI Arbeidsmarkt Intelligence Rapport</h1>
<p><strong>Functie:</strong> {job_title} | <strong>Locatie:</strong> {location}</p>
<p><strong>Gegenereerd:</strong> {data['meta']['generated_date']} | <strong>Betrouwbaarheid:</strong> {data['meta']['reliability_score']}%</p>

<div class="highlight">
<h3>Executive Summary</h3>
<p><strong>Markt Assessment:</strong> {data['executive_summary']['markt_assessment']}</p>
<p><strong>Urgentie:</strong> {data['executive_summary']['urgentie']} - {data['executive_summary']['recruitment_classificatie']}</p>
<p><strong>Actie Window:</strong> {data['market_intelligence_dashboard']['markt_actie_window_days']} dagen voor optimale positionering</p>
</div>

<h2>Markt Intelligence</h2>
<table>
<tr>
<td>Talent Schaarste Index</td>
<td>{data['market_intelligence_dashboard']['talent_schaarste_index']}/10 ({data['market_intelligence_dashboard']['markt_status']})</td>
</tr>
<tr>
<td>Time-to-Hire Range</td>
<td>{data['market_intelligence_dashboard']['time_to_hire_min']}-{data['market_intelligence_dashboard']['time_to_hire_max']} dagen</td>
</tr>
<tr>
<td>Success Rate</td>
<td>{data['market_intelligence_dashboard']['success_rate_pct']}%</td>
</tr>
<tr>
<td>Totaal Kandidaten</td>
<td>{data['workforce_availability']['total_candidates']} kandidaten beschikbaar</td>
</tr>
</table>

<div class="salary-box">
<h2>Salaris Intelligence 2025</h2>
<div class="salary-main">{fmt(data['salary_intelligence']['p50_mediaan'])}</div>
<p>Markt Mediaan (P50) - Bruto per maand</p>
<p><strong>P25 (Junior):</strong> {fmt(data['salary_intelligence']['p25_junior'])} | <strong>P75 (Senior):</strong> {fmt(data['salary_intelligence']['p75_senior'])}</p>
<p><strong>Bonus gemiddeld:</strong> {data['salary_intelligence']['bonus_avg_pct']}% ({fmt(bonus_amount)}/maand)</p>
</div>

<h2>Total Compensation</h2>
<div class="grid">
<div class="box">
<h3>Compensation Components</h3>
<table>
<tr><td>Base Salary</td><td>{fmt(base)}</td></tr>
<tr><td>Variable Bonus</td><td>{bonus_pct}%</td></tr>
<tr><td>Pensioen (werkgever)</td><td>{data['total_compensation']['components']['pension_employer_pct']}%</td></tr>
<tr><td>Lease Auto</td><td>{data['total_compensation']['components']['lease_auto_eligibility_pct']}% eligibility</td></tr>
<tr><td>Home Office</td><td>€{data['total_compensation']['components']['home_office_allowance_yearly']}/jaar</td></tr>
</table>
</div>
<div class="box">
<h3>Growth & Benefits</h3>
<table>
<tr><td>1-jaar groei</td><td>+{data['total_compensation']['growth_benefits']['salary_growth_1yr_pct']}%</td></tr>
<tr><td>3-jaar groei</td><td>+{data['total_compensation']['growth_benefits']['salary_growth_3yr_pct']}%</td></tr>
<tr><td>Schaarste factor</td><td>{data['total_compensation']['growth_benefits']['talent_scarcity_factor']}/10</td></tr>
<tr><td>Notice period</td><td>{data['total_compensation']['growth_benefits']['avg_notice_period']}</td></tr>
</table>
</div>
</div>

<h2>Workforce Availability</h2>
<table>
<tr>
<td>Actief werkzoekend</td>
<td>{data['workforce_availability']['actief_werkzoekend']['percentage']}% ({data['workforce_availability']['actief_werkzoekend']['aantal']} kandidaten)</td>
</tr>
<tr>
<td>Latent werkzoekend</td>
<td>{data['workforce_availability']['latent_werkzoekend']['percentage']}% ({data['workforce_availability']['latent_werkzoekend']['aantal']} kandidaten)</td>
</tr>
<tr>
<td>Niet werkzoekend</td>
<td>{data['workforce_availability']['niet_werkzoekend']['percentage']}% ({data['workforce_availability']['niet_werkzoekend']['aantal']} kandidaten)</td>
</tr>
</table>

<p><strong>Actief:</strong> {data['workforce_availability']['actief_werkzoekend']['description']}<br>
<strong>Latent:</strong> {data['workforce_availability']['latent_werkzoekend']['description']}<br>
<strong>Niet werkzoekend:</strong> {data['workforce_availability']['niet_werkzoekend']['description']}</p>

<h2>Demographics</h2>
<div class="grid">
<div class="box">
<h3>Leeftijd</h3>
<table>"""

    for age, item in data['demographics']['leeftijd'].items():
        html += f"<tr><td>{age} jaar</td><td>{item['percentage']}% ({item['aantal']})</td></tr>"

    html += """</table>
</div>
<div class="box">
<h3>Opleiding</h3>
<table>"""

    for edu, item in data['demographics']['opleiding'].items():
        html += f"<tr><td>{edu}</td><td>{item['percentage']}% ({item['aantal']})</td></tr>"

    html += f"""</table>
</div>
</div>

<h2>Motivation Drivers</h2>
<table>
<tr><td>Autonomy & Influence</td><td>{data['motivation_drivers']['autonomy_influence']}%</td></tr>
<tr><td>Financial Rewards</td><td>{data['motivation_drivers']['financial_rewards']}%</td></tr>
<tr><td>Work-Life Balance</td><td>{data['motivation_drivers']['work_life_balance']}%</td></tr>
<tr><td>Career Growth</td><td>{data['motivation_drivers']['career_growth']}%</td></tr>
<tr><td>Innovation & Tech</td><td>{data['motivation_drivers']['innovation_tech']}%</td></tr>
<tr><td>Team Culture</td><td>{data['motivation_drivers']['team_culture']}%</td></tr>
<tr><td>Company Reputation</td><td>{data['motivation_drivers']['company_reputation']}%</td></tr>
<tr><td>Meaningful Impact</td><td>{data['motivation_drivers']['meaningful_impact']}%</td></tr>
</table>

<h2>Recruitment Strategy</h2>
<table>
<tr><td>Primary Channel</td><td>{data['recruitment_strategy']['primary_channel']}</td></tr>
<tr><td>Secondary Channels</td><td>{data['recruitment_strategy']['secondary_channels']}</td></tr>
<tr><td>Timeline</td><td>{data['recruitment_strategy']['timeline_weeks_min']}-{data['recruitment_strategy']['timeline_weeks_max']} weken</td></tr>
<tr><td>Budget Range</td><td>€{data['recruitment_strategy']['budget_range_min_k']}k - €{data['recruitment_strategy']['budget_range_max_k']}k</td></tr>
</table>

<h2>Strategic Action Plan</h2>
<ol>"""

    for priority in data['strategic_priorities']:
        html += f"<li><strong>{priority['title']}:</strong> {priority['description']}</li>"

    html += f"""</ol>

</div>

<div class="footer">
<h3>Recruitin - AI Recruitment Intelligence</h3>
<p>Wouter Arts | <a href="mailto:warts@recruitin.nl">warts@recruitin.nl</a> | 06-14314593</p>
<p style="font-size: 12px; opacity: 0.8; margin-top: 15px;">
Powered by Claude AI Sonnet 4 | Reliability: {data['meta']['reliability_score']}% | &copy; 2025 Recruitin BV
</p>
</div>

</body>
</html>"""

    return html

# =====================================
# MAIN EXECUTION
# =====================================

try:
    job_title = input.get('functietitel', 'Niet opgegeven')
    location = input.get('locatie', 'Nederland')
    company = input.get('bedrijfsnaam', '')
    email = input.get('email', 'warts@recruitin.nl')
    vacancy_url = input.get('vacature_url', '')
    jobdigger_pdf = input.get('jobdigger_pdf_text', '')
    linkedin_pdf = input.get('linkedin_pdf_text', '')
    vacancy_text = input.get('vacature_text', '')

    prompt = build_analysis_prompt(job_title, location, company, email, vacancy_url, jobdigger_pdf, linkedin_pdf, vacancy_text)
    response_text = call_claude_api(prompt)
    clean_text = clean_json_response(response_text)
    analysis_data = json.loads(clean_text)

    print(f"✅ Analysis complete! Reliability: {analysis_data['meta']['reliability_score']}%")

    html_report = generate_simple_html(analysis_data, job_title, location)

    output = {
        'to': email,
        'subject': f"Arbeidsmarkt Rapport: {job_title} in {location}",
        'body': html_report,
        'notion_company': company,
        'notion_job_title': job_title,
        'notion_location': location,
        'notion_salary_p50': analysis_data['salary_intelligence']['p50_mediaan'],
        'notion_scarcity': analysis_data['market_intelligence_dashboard']['talent_schaarste_index'],
        'notion_time_to_hire': f"{analysis_data['market_intelligence_dashboard']['time_to_hire_min']}-{analysis_data['market_intelligence_dashboard']['time_to_hire_max']} dagen",
        'notion_reliability': f"{analysis_data['meta']['reliability_score']}%",
        'notion_url': vacancy_url,
        'notion_json': json.dumps(analysis_data, ensure_ascii=False)
    }

    print(f"📧 Email: {output['to']} | Subject: {output['subject']}")
    print("🎉 SUCCESS!")

except Exception as e:
    print(f"❌ Error: {str(e)}")
    output = {
        'to': 'warts@recruitin.nl',
        'subject': 'Error in Report Generation',
        'body': f'<html><body><h1>Error</h1><p>{str(e)}</p></body></html>',
        'notion_reliability': '0%'
    }
