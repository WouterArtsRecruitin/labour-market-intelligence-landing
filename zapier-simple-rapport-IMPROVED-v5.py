"""
ZAPIER STEP 5: IMPROVED SIMPLE REPORT GENERATOR
================================================
Version: 5.0 - Enhanced with Security, Validation & Error Handling

IMPROVEMENTS:
✅ Environment variable support (security)
✅ Retry logic for API calls (reliability)
✅ Input validation (robustness)
✅ Detailed logging (debugging)
✅ Cost estimation (monitoring)
✅ Data validation (quality)
✅ HTML escaping (security)
✅ Better error messages (troubleshooting)
"""

import json
import os
import time
from datetime import datetime
import requests
import html as html_lib

# =====================================
# CONFIGURATION
# =====================================

# API Configuration - Use Environment Variable (SECURE) or fallback to placeholder
CLAUDE_API_KEY = os.environ.get('CLAUDE_API_KEY', 'sk-ant-api03-YOUR_API_KEY_HERE')
CLAUDE_API_URL = "https://api.anthropic.com/v1/messages"
CLAUDE_MODEL = "claude-sonnet-4-20250514"

# Settings
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds
REQUEST_TIMEOUT = 120  # seconds
MAX_PDF_CHARS = 8000  # per PDF to stay within token limits
MAX_TOKENS = 16000
TEMPERATURE = 0.3

# Cost estimation (approximate, in EUR)
COST_PER_1M_INPUT_TOKENS = 3.0
COST_PER_1M_OUTPUT_TOKENS = 15.0

print(f"✅ Configuration loaded")
print(f"   Model: {CLAUDE_MODEL}")
print(f"   Max retries: {MAX_RETRIES}")
print(f"   API key source: {'Environment Variable' if 'CLAUDE_API_KEY' in os.environ else 'Placeholder (UPDATE REQUIRED!)'}")

# =====================================
# HELPER FUNCTIONS
# =====================================

def validate_input_data(data):
    """Validate required input fields"""
    errors = []

    # Required fields
    if not data.get('functietitel'):
        errors.append("Missing 'functietitel' (job title)")
    if not data.get('locatie'):
        errors.append("Missing 'locatie' (location)")
    if not data.get('email'):
        errors.append("Missing 'email' (recipient email)")

    # Validate email format (basic)
    email = data.get('email', '')
    if email and '@' not in email:
        errors.append(f"Invalid email format: {email}")

    # Check if we have at least some content
    has_content = any([
        data.get('jobdigger_pdf_text'),
        data.get('linkedin_pdf_text'),
        data.get('vacature_text')
    ])

    if not has_content:
        print("⚠️ Warning: No PDF or text content provided - using Claude's market knowledge only")

    return errors

def truncate_text(text, max_chars, label):
    """Truncate text and log if truncated"""
    if not text:
        return ""

    original_length = len(text)
    truncated = text[:max_chars]

    if original_length > max_chars:
        print(f"   📄 {label}: Truncated from {original_length:,} to {max_chars:,} chars ({original_length - max_chars:,} chars removed)")
    else:
        print(f"   📄 {label}: {original_length:,} chars (no truncation needed)")

    return truncated

def estimate_tokens(text):
    """Rough token estimation (1 token ≈ 4 chars)"""
    return len(text) // 4

def estimate_cost(input_tokens, output_tokens):
    """Estimate API call cost in EUR"""
    input_cost = (input_tokens / 1_000_000) * COST_PER_1M_INPUT_TOKENS
    output_cost = (output_tokens / 1_000_000) * COST_PER_1M_OUTPUT_TOKENS
    total_cost = input_cost + output_cost
    return total_cost

def escape_html(text):
    """Escape HTML to prevent XSS"""
    return html_lib.escape(str(text))

# =====================================
# CLAUDE PROMPT
# =====================================

def build_analysis_prompt(job_title, location, company, email, vacancy_url,
                          jobdigger_pdf, linkedin_pdf, vacancy_text):
    current_date = datetime.now().strftime("%d %B %Y om %H:%M")

    prompt = f"""Je bent een Elite Nederlandse Arbeidsmarkt Intelligence Expert met 15+ jaar ervaring.

INPUT DATA:
- Functietitel: {job_title}
- Locatie: {location}
- Bedrijf: {company or 'Niet opgegeven'}

Jobdigger PDF: {jobdigger_pdf if jobdigger_pdf else 'Geen data'}
LinkedIn PDF: {linkedin_pdf if linkedin_pdf else 'Geen data'}
Vacaturetekst: {vacancy_text if vacancy_text else 'Geen data'}

RETURN EXACT JSON:
{{
  "executive_summary": {{
    "markt_assessment": "[2-3 zinnen over markt conditie]",
    "time_to_hire_range": "XX-XX dagen",
    "actieve_kandidaten": XXX,
    "urgentie": "Kritiek|Hoog|Normaal|Laag",
    "recruitment_classificatie": "Executive Schaarste|High Demand|Normaal|Beschikbaar"
  }},
  "market_intelligence_dashboard": {{
    "talent_schaarste_index": "X.X",
    "time_to_hire_min": XX,
    "time_to_hire_max": XX,
    "success_rate_pct": XX,
    "markt_actie_window_days": XX,
    "markt_status": "Extreem hete markt|Krappe markt|Normale markt|Ruime markt",
    "actie_urgentie": "onmiddellijke actie|spoedige actie|normale planning|geen urgentie"
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
    "primary_channel": "Executive search|LinkedIn Premium|Jobboards|Tech communities",
    "secondary_channels": "Professional netwerken|Referrals|Headhunting",
    "timeline_weeks_min": XX, "timeline_weeks_max": XX,
    "budget_range_min_k": XX, "budget_range_max_k": XX
  }},
  "strategic_priorities": [
    {{"title": "Compensation Positioning", "description": "Target salary range en benefits"}},
    {{"title": "Sourcing Mix", "description": "Channel strategie"}},
    {{"title": "Timeline & Urgentie", "description": "Launch planning"}},
    {{"title": "Success Rate Optimization", "description": "Candidate experience focus"}}
  ],
  "meta": {{
    "generated_date": "{current_date}",
    "reliability_score": XX,
    "data_sources_count": X,
    "ai_model": "Claude AI Sonnet 4",
    "analysis_type": "Market Intelligence"
  }}
}}

BEREKENINGSLOGICA NL 2025:
- Schaarste: Tech 7-9, Management 7-9, Productie 5-7, Sales 4-6, Admin 2-4
- Time-to-hire: Tech 60-120d, Management 75-120d, Productie 45-75d, Sales 30-60d
- Salary (bruto/maand): Junior €2.5-3.5k, Medior €3.5-5.5k, Senior €5.5-7.5k, Lead €6.5-9.5k
- Workforce: Tech 20/40/40%, Management 15/35/50%, Productie 25/45/30%, Sales 30/45/25%
- Opleiding: Tech 15/60/25%, Management 10/50/40%, Productie 60/35/5%, Sales 20/60/20%
- Regio correctie: Amsterdam/Utrecht +10-15%, Rotterdam/Den Haag +5-10%, Overig baseline

KWALITEIT VEREISTEN:
- Alle cijfers moeten realistisch zijn voor NL markt 2025
- Percentages moeten optellen tot 100%
- Consistency tussen gerelateerde metrics (schaarste ↔ time-to-hire)
- Professional tone, geen casual taal

Return ALLEEN valid JSON zonder markdown backticks!"""

    return prompt

# =====================================
# CLAUDE API CALL WITH RETRY LOGIC
# =====================================

def call_claude_api(prompt):
    """Call Claude API with retry logic"""
    headers = {
        'x-api-key': CLAUDE_API_KEY,
        'anthropic-version': '2023-06-01',
        'content-type': 'application/json'
    }

    payload = {
        'model': CLAUDE_MODEL,
        'max_tokens': MAX_TOKENS,
        'temperature': TEMPERATURE,
        'messages': [{'role': 'user', 'content': prompt}]
    }

    # Estimate input tokens
    input_tokens = estimate_tokens(prompt)
    print(f"📊 Estimated input tokens: {input_tokens:,}")

    for attempt in range(MAX_RETRIES):
        try:
            print(f"🤖 Calling Claude API (attempt {attempt + 1}/{MAX_RETRIES})...")

            start_time = time.time()
            response = requests.post(
                CLAUDE_API_URL,
                headers=headers,
                json=payload,
                timeout=REQUEST_TIMEOUT
            )
            elapsed_time = time.time() - start_time

            print(f"   Response time: {elapsed_time:.2f}s")

            if response.status_code == 200:
                result = response.json()

                # Extract usage stats
                usage = result.get('usage', {})
                actual_input_tokens = usage.get('input_tokens', input_tokens)
                output_tokens = usage.get('output_tokens', 0)

                # Calculate cost
                cost = estimate_cost(actual_input_tokens, output_tokens)

                print(f"✅ Claude API success!")
                print(f"   Input tokens: {actual_input_tokens:,}")
                print(f"   Output tokens: {output_tokens:,}")
                print(f"   Estimated cost: €{cost:.4f}")

                return result['content'][0]['text']

            elif response.status_code == 429:  # Rate limit
                print(f"⚠️ Rate limit hit (attempt {attempt + 1})")
                if attempt < MAX_RETRIES - 1:
                    wait_time = RETRY_DELAY * (2 ** attempt)  # Exponential backoff
                    print(f"   Waiting {wait_time}s before retry...")
                    time.sleep(wait_time)
                    continue

            elif response.status_code == 401:  # Auth error
                raise Exception(f"Authentication failed - Check your API key! (Status: {response.status_code})")

            else:
                print(f"❌ API error {response.status_code}: {response.text[:200]}")
                if attempt < MAX_RETRIES - 1:
                    print(f"   Retrying in {RETRY_DELAY}s...")
                    time.sleep(RETRY_DELAY)
                    continue

        except requests.Timeout:
            print(f"⏱️ Request timeout (attempt {attempt + 1})")
            if attempt < MAX_RETRIES - 1:
                print(f"   Retrying in {RETRY_DELAY}s...")
                time.sleep(RETRY_DELAY)
                continue

        except requests.RequestException as e:
            print(f"🌐 Network error: {str(e)}")
            if attempt < MAX_RETRIES - 1:
                print(f"   Retrying in {RETRY_DELAY}s...")
                time.sleep(RETRY_DELAY)
                continue

    # All retries failed
    raise Exception(f"Claude API call failed after {MAX_RETRIES} attempts")

def clean_json_response(text):
    """Clean and extract JSON from response"""
    text = text.strip()

    # Remove markdown code blocks
    if text.startswith('```json'):
        text = text[7:]
    elif text.startswith('```'):
        text = text[3:]
    if text.endswith('```'):
        text = text[:-3]

    text = text.strip()

    # Validate it looks like JSON
    if not text.startswith('{'):
        raise ValueError("Response doesn't start with '{' - not valid JSON")
    if not text.endswith('}'):
        raise ValueError("Response doesn't end with '}' - not valid JSON")

    return text

def validate_analysis_data(data):
    """Validate Claude's analysis response"""
    errors = []

    # Check required top-level keys
    required_keys = [
        'executive_summary', 'market_intelligence_dashboard',
        'salary_intelligence', 'total_compensation', 'workforce_availability',
        'demographics', 'motivation_drivers', 'recruitment_strategy',
        'strategic_priorities', 'meta'
    ]

    for key in required_keys:
        if key not in data:
            errors.append(f"Missing required key: {key}")

    # Validate numeric ranges
    if 'salary_intelligence' in data:
        sal = data['salary_intelligence']
        if sal.get('p50_mediaan', 0) < sal.get('p25_junior', 0):
            errors.append("Invalid salary data: P50 < P25")
        if sal.get('p75_senior', 0) < sal.get('p50_mediaan', 0):
            errors.append("Invalid salary data: P75 < P50")

    # Validate percentages sum to ~100
    if 'workforce_availability' in data:
        workforce = data['workforce_availability']
        total_pct = (
            workforce.get('actief_werkzoekend', {}).get('percentage', 0) +
            workforce.get('latent_werkzoekend', {}).get('percentage', 0) +
            workforce.get('niet_werkzoekend', {}).get('percentage', 0)
        )
        if abs(total_pct - 100) > 5:  # Allow 5% tolerance
            errors.append(f"Workforce percentages don't sum to 100% (got {total_pct}%)")

    if errors:
        print("⚠️ Data validation warnings:")
        for error in errors:
            print(f"   - {error}")

    return len(errors) == 0

# =====================================
# SIMPLE HTML REPORT
# =====================================

def generate_simple_html(data, job_title, location):
    """Generate simple, readable HTML report"""

    # Escape user inputs for security
    job_title_safe = escape_html(job_title)
    location_safe = escape_html(location)

    def fmt(amount):
        return f"€{amount:,}".replace(',', '.')

    base = data['total_compensation']['components']['base_salary']
    bonus_pct = data['total_compensation']['components']['variable_bonus_pct']
    bonus_amount = int(base * bonus_pct / 100)

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 20px auto; padding: 20px; background: #f5f5f5; }}
.container {{ background: white; padding: 30px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
h1 {{ color: #2c3e50; font-size: 24px; border-bottom: 3px solid #FF6B35; padding-bottom: 10px; margin-top: 0; }}
h2 {{ color: #34495e; font-size: 20px; margin-top: 30px; border-bottom: 2px solid #ddd; padding-bottom: 8px; }}
h3 {{ color: #555; font-size: 16px; margin-top: 20px; }}
.highlight {{ background: #FFF3E0; padding: 15px; border-left: 4px solid #FF6B35; margin: 15px 0; border-radius: 3px; }}
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
.reliability {{ display: inline-block; padding: 5px 10px; background: #27ae60; color: white; border-radius: 3px; font-size: 12px; font-weight: bold; }}
@media (max-width: 600px) {{ .grid {{ grid-template-columns: 1fr; }} }}
</style>
</head>
<body>
<div class="container">

<h1>🤖 AI Arbeidsmarkt Intelligence Rapport</h1>
<p><strong>Functie:</strong> {job_title_safe} | <strong>Locatie:</strong> {location_safe}</p>
<p><strong>Gegenereerd:</strong> {escape_html(data['meta']['generated_date'])}</p>
<p><strong>Betrouwbaarheid:</strong> <span class="reliability">{data['meta']['reliability_score']}%</span></p>

<div class="highlight">
<h3>📋 Executive Summary</h3>
<p><strong>Markt Assessment:</strong> {escape_html(data['executive_summary']['markt_assessment'])}</p>
<p><strong>Urgentie:</strong> {escape_html(data['executive_summary']['urgentie'])} - {escape_html(data['executive_summary']['recruitment_classificatie'])}</p>
<p><strong>Actie Window:</strong> {data['market_intelligence_dashboard']['markt_actie_window_days']} dagen voor optimale positionering</p>
</div>

<h2>📊 Markt Intelligence</h2>
<table>
<tr>
<td>Talent Schaarste Index</td>
<td>{data['market_intelligence_dashboard']['talent_schaarste_index']}/10.0 ({escape_html(data['market_intelligence_dashboard']['markt_status'])})</td>
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
<td>{data['workforce_availability']['total_candidates']:,} kandidaten beschikbaar</td>
</tr>
</table>

<div class="salary-box">
<h2>💰 Salaris Intelligence 2025</h2>
<div class="salary-main">{fmt(data['salary_intelligence']['p50_mediaan'])}</div>
<p>Markt Mediaan (P50) - Bruto per maand</p>
<p><strong>P25 (Junior):</strong> {fmt(data['salary_intelligence']['p25_junior'])} | <strong>P75 (Senior):</strong> {fmt(data['salary_intelligence']['p75_senior'])}</p>
<p><strong>Bonus gemiddeld:</strong> {data['salary_intelligence']['bonus_avg_pct']}% (≈{fmt(bonus_amount)}/maand)</p>
</div>

<h2>💼 Total Compensation</h2>
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
<tr><td>Notice period</td><td>{escape_html(data['total_compensation']['growth_benefits']['avg_notice_period'])}</td></tr>
</table>
</div>
</div>

<h2>👥 Workforce Availability</h2>
<table>
<tr>
<td>🟢 Actief werkzoekend</td>
<td>{data['workforce_availability']['actief_werkzoekend']['percentage']}% ({data['workforce_availability']['actief_werkzoekend']['aantal']:,} kandidaten)</td>
</tr>
<tr>
<td>🟡 Latent werkzoekend</td>
<td>{data['workforce_availability']['latent_werkzoekend']['percentage']}% ({data['workforce_availability']['latent_werkzoekend']['aantal']:,} kandidaten)</td>
</tr>
<tr>
<td>🔴 Niet werkzoekend</td>
<td>{data['workforce_availability']['niet_werkzoekend']['percentage']}% ({data['workforce_availability']['niet_werkzoekend']['aantal']:,} kandidaten)</td>
</tr>
</table>

<p style="font-size: 14px; color: #666; line-height: 1.8;">
<strong>🟢 Actief:</strong> {escape_html(data['workforce_availability']['actief_werkzoekend']['description'])}<br>
<strong>🟡 Latent:</strong> {escape_html(data['workforce_availability']['latent_werkzoekend']['description'])}<br>
<strong>🔴 Niet werkzoekend:</strong> {escape_html(data['workforce_availability']['niet_werkzoekend']['description'])}
</p>

<h2>📊 Demographics</h2>
<div class="grid">
<div class="box">
<h3>🎂 Leeftijd</h3>
<table>"""

    for age, item in data['demographics']['leeftijd'].items():
        html += f"<tr><td>{escape_html(age)} jaar</td><td>{item['percentage']}% ({item['aantal']:,})</td></tr>"

    html += """</table>
</div>
<div class="box">
<h3>🎓 Opleiding</h3>
<table>"""

    for edu, item in data['demographics']['opleiding'].items():
        html += f"<tr><td>{escape_html(edu)}</td><td>{item['percentage']}% ({item['aantal']:,})</td></tr>"

    html += f"""</table>
</div>
</div>

<h2>🎯 Motivation Drivers</h2>
<table>
<tr><td>🎯 Autonomy & Influence</td><td>{data['motivation_drivers']['autonomy_influence']}%</td></tr>
<tr><td>💰 Financial Rewards</td><td>{data['motivation_drivers']['financial_rewards']}%</td></tr>
<tr><td>⚖️ Work-Life Balance</td><td>{data['motivation_drivers']['work_life_balance']}%</td></tr>
<tr><td>📚 Career Growth</td><td>{data['motivation_drivers']['career_growth']}%</td></tr>
<tr><td>🚀 Innovation & Tech</td><td>{data['motivation_drivers']['innovation_tech']}%</td></tr>
<tr><td>👥 Team Culture</td><td>{data['motivation_drivers']['team_culture']}%</td></tr>
<tr><td>🏢 Company Reputation</td><td>{data['motivation_drivers']['company_reputation']}%</td></tr>
<tr><td>🎖️ Meaningful Impact</td><td>{data['motivation_drivers']['meaningful_impact']}%</td></tr>
</table>

<h2>🎯 Recruitment Strategy</h2>
<table>
<tr><td>Primary Channel</td><td>{escape_html(data['recruitment_strategy']['primary_channel'])}</td></tr>
<tr><td>Secondary Channels</td><td>{escape_html(data['recruitment_strategy']['secondary_channels'])}</td></tr>
<tr><td>Timeline</td><td>{data['recruitment_strategy']['timeline_weeks_min']}-{data['recruitment_strategy']['timeline_weeks_max']} weken</td></tr>
<tr><td>Budget Range</td><td>€{data['recruitment_strategy']['budget_range_min_k']}k - €{data['recruitment_strategy']['budget_range_max_k']}k</td></tr>
</table>

<h2>🚀 Strategic Action Plan</h2>
<ol style="line-height: 1.8;">"""

    for priority in data['strategic_priorities']:
        html += f"<li><strong>{escape_html(priority['title'])}:</strong> {escape_html(priority['description'])}</li>"

    html += f"""</ol>

</div>

<div class="footer">
<h3>Recruitin - AI Recruitment Intelligence</h3>
<p>Wouter Arts | <a href="mailto:warts@recruitin.nl">warts@recruitin.nl</a> | 📞 06-14314593</p>
<p style="font-size: 12px; opacity: 0.8; margin-top: 15px;">
Powered by {escape_html(data['meta']['ai_model'])} | Reliability: {data['meta']['reliability_score']}%<br>
Analysis Type: {escape_html(data['meta']['analysis_type'])} | &copy; 2025 Recruitin BV
</p>
</div>

</body>
</html>"""

    return html

# =====================================
# MAIN EXECUTION
# =====================================

print("\n" + "="*60)
print("🚀 STARTING LABOUR MARKET INTELLIGENCE REPORT GENERATION")
print("="*60 + "\n")

try:
    # Get input data
    print("📥 Extracting input data...")
    input_data = {
        'functietitel': input.get('functietitel', ''),
        'locatie': input.get('locatie', ''),
        'bedrijfsnaam': input.get('bedrijfsnaam', ''),
        'email': input.get('email', ''),
        'vacature_url': input.get('vacature_url', ''),
        'jobdigger_pdf_text': input.get('jobdigger_pdf_text', ''),
        'linkedin_pdf_text': input.get('linkedin_pdf_text', ''),
        'vacature_text': input.get('vacature_text', '')
    }

    # Validate input
    print("\n✔️ Validating input data...")
    validation_errors = validate_input_data(input_data)
    if validation_errors:
        error_msg = "Input validation failed:\n" + "\n".join(f"  - {e}" for e in validation_errors)
        raise ValueError(error_msg)

    print("   ✅ All required fields present")

    # Extract and truncate text
    print("\n📄 Processing PDF content...")
    job_title = input_data['functietitel']
    location = input_data['locatie']
    company = input_data['bedrijfsnaam']
    email = input_data['email']
    vacancy_url = input_data['vacature_url']

    jobdigger_pdf = truncate_text(input_data['jobdigger_pdf_text'], MAX_PDF_CHARS, "Jobdigger PDF")
    linkedin_pdf = truncate_text(input_data['linkedin_pdf_text'], MAX_PDF_CHARS, "LinkedIn PDF")
    vacancy_text = truncate_text(input_data['vacature_text'], MAX_PDF_CHARS // 2, "Vacaturetekst")

    # Build prompt
    print("\n🔨 Building analysis prompt...")
    prompt = build_analysis_prompt(job_title, location, company, email, vacancy_url,
                                   jobdigger_pdf, linkedin_pdf, vacancy_text)
    print(f"   Prompt length: {len(prompt):,} chars")

    # Call Claude API
    print("\n" + "-"*60)
    response_text = call_claude_api(prompt)
    print("-"*60 + "\n")

    # Parse JSON
    print("📋 Parsing JSON response...")
    clean_text = clean_json_response(response_text)
    analysis_data = json.loads(clean_text)
    print("   ✅ Valid JSON parsed")

    # Validate data
    print("\n✔️ Validating analysis data...")
    is_valid = validate_analysis_data(analysis_data)
    if is_valid:
        print("   ✅ Data validation passed")
    else:
        print("   ⚠️ Data validation warnings (see above) - continuing anyway")

    print(f"\n✅ Analysis complete!")
    print(f"   Reliability score: {analysis_data['meta']['reliability_score']}%")
    print(f"   Data sources: {analysis_data['meta']['data_sources_count']}")

    # Generate HTML
    print("\n🎨 Generating HTML report...")
    html_report = generate_simple_html(analysis_data, job_title, location)
    print(f"   HTML size: {len(html_report):,} chars")

    # Prepare output
    output = {
        'to': email,
        'subject': f"🤖 Arbeidsmarkt Intelligence: {job_title} in {location}",
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

    print(f"\n📧 Email details:")
    print(f"   To: {output['to']}")
    print(f"   Subject: {output['subject']}")

    print("\n" + "="*60)
    print("🎉 SUCCESS! Report generated successfully")
    print("="*60 + "\n")

except ValueError as e:
    print(f"\n❌ Validation Error: {str(e)}")
    output = {
        'to': 'warts@recruitin.nl',
        'subject': '❌ Validation Error in Report Generation',
        'body': f'<html><body><h1>Validation Error</h1><p>{escape_html(str(e))}</p><p>Please check input data and try again.</p></body></html>',
        'notion_reliability': '0%',
        'notion_company': 'Error',
        'notion_job_title': 'Error'
    }

except json.JSONDecodeError as e:
    print(f"\n❌ JSON Parse Error: {str(e)}")
    print(f"   Response preview: {clean_text[:500] if 'clean_text' in locals() else 'N/A'}")
    output = {
        'to': 'warts@recruitin.nl',
        'subject': '❌ JSON Parse Error in Report Generation',
        'body': f'<html><body><h1>JSON Parse Error</h1><p>{escape_html(str(e))}</p><p>Claude did not return valid JSON. Check prompt or retry.</p></body></html>',
        'notion_reliability': '0%',
        'notion_company': 'Error',
        'notion_job_title': 'Error'
    }

except Exception as e:
    print(f"\n❌ Unexpected Error: {str(e)}")
    import traceback
    print(f"\n📋 Traceback:")
    traceback.print_exc()

    output = {
        'to': 'warts@recruitin.nl',
        'subject': '❌ Error in Report Generation',
        'body': f'<html><body><h1>Error</h1><p>{escape_html(str(e))}</p><p>Check Zapier logs for details.</p></body></html>',
        'notion_reliability': '0%',
        'notion_company': 'Error',
        'notion_job_title': 'Error'
    }
