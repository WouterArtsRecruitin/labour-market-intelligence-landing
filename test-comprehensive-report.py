"""
TEST SCRIPT voor Comprehensive AI Recruitment Intelligence Report
Dit script simuleert Zapier input_data en genereert een test HTML rapport
"""

# ================================================================
# MOCK ZAPIER INPUT DATA
# ================================================================

# Simuleer input_data zoals Zapier dat zou doen
input_data = {
    'claude_api_key': 'sk-ant-test-key',  # Gebruik fallback data
    'bedrijfsnaam': 'TechVision BV',
    'contactpersoon': 'Sarah van der Berg',
    'email': 's.vandenberg@techvision.nl',
    'telefoon': '+31 6 12345678',
    'functietitel': 'Senior Data Engineer',
    'sector': 'IT & Technology',
    'locatie': 'Amsterdam',
    'ervaringsniveau': 'Senior',
    'salaris_min': '65000',
    'salaris_max': '85000',
    'urgentie': 'Hoog',
    'aantal_posities': '2',
    'werkervaring_jaren': '5-7 jaar',
    'opleidingsniveau': 'HBO/WO',
    'teamsize': 'Team van 8 mensen',
    'bedrijfsgrootte': '200-500 medewerkers',
    'werkomgeving': 'Hybrid (2 dagen kantoor)',
    'groei_fase': 'Scale-up',
    'key_skills': 'Python, SQL, Apache Spark, AWS',
    'extra_info': 'We zoeken iemand met passie voor data en ervaring met big data pipelines. Goede werk-privé balans is belangrijk voor ons team.',

    # Document URLs
    'vacature_url': 'https://techvision.nl/vacatures/senior-data-engineer',
    'jobdigger_url': 'https://example.com/jobdigger-report.pdf',
    'linkedin_ti_url': 'https://example.com/linkedin-ti-report.pdf',

    # Extracted text van documenten (simulatie)
    'vacature_text': """
Senior Data Engineer bij TechVision BV

Locatie: Amsterdam (Hybrid)
Salaris: €65.000 - €85.000 per jaar
Ervaring: 5-7 jaar

Over de functie:
Ben jij een ervaren Data Engineer die grote datasets kan transformeren naar waardevolle inzichten?
Bij TechVision werk je aan cutting-edge data platforms voor onze enterprise klanten.

Wat ga je doen:
- Ontwerpen en bouwen van schaalbare data pipelines met Apache Spark en Python
- Optimaliseren van data workflows in AWS cloud omgeving
- Samenwerken met Data Scientists en Analytics teams
- Implementeren van data quality checks en monitoring
- Mentoren van junior engineers

Wat vragen wij:
- HBO/WO diploma in Informatica, Wiskunde of verwante richting
- 5-7 jaar ervaring als Data Engineer
- Expert kennis van Python en SQL
- Ervaring met Apache Spark, Kafka, Airflow
- Hands-on ervaring met AWS (S3, EMR, Redshift, Glue)
- Ervaring met CI/CD pipelines en Infrastructure as Code
- Uitstekende communicatieve vaardigheden in Nederlands en Engels

Nice to have:
- Kennis van machine learning pipelines
- Ervaring met real-time streaming data
- Certificeringen (AWS, Databricks, etc.)

Wat bieden wij:
- Salaris €65.000 - €85.000 afhankelijk van ervaring
- 25 vakantiedagen + 13e maand
- Lease auto of mobiliteitsbudget €800/maand
- Pensioenregeling met 7% werkgeversbijdrage
- Opleidingsbudget €3.000 per jaar
- Thuiswerkvergoeding €50/maand
- Flexibel hybrid werken (2 dagen kantoor)
- Moderne laptop en setup
- Team uitjes en lunches
- Platte organisatie met korte lijnen

Bedrijfscultuur:
Wij zijn een innovatieve scale-up die data-driven oplossingen bouwt voor enterprise klanten.
Ons team van 8 engineers werkt met de nieuwste technologieën en heeft veel autonomie.
We geloven in continuous learning, experimenteren en een goede werk-privé balans.
    """,

    'jobdigger_text': """
JOBDIGGER MARKTRAPPORT - DATA ENGINEER
Peildatum: Oktober 2024

SAMENVATTING:
De arbeidsmarkt voor Data Engineers is zeer krap met hoge vraag naar professionals met
moderne tech skills. Er is een tekort van 2.800 gekwalificeerde kandidaten.

WERKGELEGENHEID:
- Totaal werkenden in Nederland: 28.500 Data Engineers
- Groei afgelopen jaar: +4,2% (1.200 nieuwe banen)
- Trend: Sterk stijgend door digitalisering
- Aantal openstaande vacatures: 1.850

CONTRACTVORMEN:
- Vast contract: 68%
- Tijdelijk contract: 17%
- ZZP/Freelance: 15%

DEMOGRAFIE:
- Gemiddelde leeftijd: 38 jaar
- Man/Vrouw ratio: 73/27
- Opleidingsniveau: 85% HBO/WO, 15% MBO met ervaring

REGIONALE VERDELING:
- Noord-Holland (Amsterdam): 38%
- Zuid-Holland (Rotterdam/Den Haag): 24%
- Utrecht: 16%
- Noord-Brabant (Eindhoven): 12%
- Overig: 10%

TOP WERKGEVERS:
1. ING Bank (650 Data Engineers)
2. Booking.com (420 Data Engineers)
3. Rabobank (380 Data Engineers)
4. ABN AMRO (340 Data Engineers)
5. Adyen (280 Data Engineers)

SALARIS:
- P25 (Junior/Medior): €48.000 - €62.000
- P50 (Medior/Senior): €62.000 - €78.000
- P75 (Senior/Lead): €78.000 - €95.000

VEREISTE SKILLS (top 10):
1. Python (85%)
2. SQL (92%)
3. Cloud platforms (AWS/Azure/GCP) (78%)
4. Apache Spark (62%)
5. Data warehousing (68%)
6. ETL/ELT pipelines (75%)
7. Kafka/streaming (45%)
8. Docker/Kubernetes (52%)
9. Git/CI/CD (70%)
10. Data modeling (65%)

TOEKOMSTVERWACHTING:
- Sector groei prognose: Zeer positief (+6-8% per jaar tot 2028)
- Automatisering risico: Laag (AI augmenteert maar vervangt niet)
- Skills van de toekomst: ML Ops, Real-time analytics, Data mesh architectuur
- Arbeidsmarkt blijft krap met voorspelde tekort van 4.500 professionals in 2026

MOBILITEIT:
- Gemiddelde dienstverband: 3,8 jaar
- 18% van professionals wisselt jaarlijks van baan
- Belangrijkste redenen voor switch: Salaris (72%), Technologie/innovatie (68%), Werk-privé balans (54%)
    """,

    'linkedin_ti_text': """
LINKEDIN TALENT INSIGHTS REPORT
Functie: Data Engineer | Locatie: Nederland | Datum: Oktober 2024

TALENT POOL ANALYSE:
- Totaal professionals met "Data Engineer" in profiel: 16.200
- Actief zoekend naar werk: 2.430 (15%)
- Open voor kansen: 7.290 (45%)
- Niet werkzoekend: 6.480 (40%)

HIRING VELOCITY:
- Gemiddeld aantal hires per maand in NL: 890
- Hiring speed: Snel (gemiddeld 42 dagen time-to-fill)
- Competition voor talent: Hoog

TOP CONCURRERENDE WERKGEVERS (met aantal Data Engineers):
1. ING - 650 werknemers | 45 hires/maand
2. Booking.com - 420 werknemers | 28 hires/maand
3. Rabobank - 380 werknemers | 32 hires/maand
4. ABN AMRO - 340 werknemers | 25 hires/maand
5. Adyen - 280 werknemers | 22 hires/maand
6. bol.com - 220 werknemers | 18 hires/maand
7. Coolblue - 180 werknemers | 15 hires/maand

MEEST VOORKOMENDE JOB TITLES:
- Data Engineer (62%)
- Senior Data Engineer (18%)
- Lead Data Engineer (8%)
- Principal Data Engineer (4%)
- Staff Data Engineer (3%)
- Cloud Data Engineer (5%)

OPLEIDINGSNIVEAU:
- WO (Universiteit): 48%
- HBO (Hogeschool): 43%
- MBO met ervaring: 9%

MEEST VOORKOMENDE STUDIES:
- Computer Science (38%)
- Information Technology (22%)
- Mathematics/Statistics (15%)
- Engineering (12%)
- Business Analytics (8%)
- Overig (5%)

TOP SKILLS (volgens LinkedIn profielen):
1. Python (88%)
2. SQL (91%)
3. Apache Spark (64%)
4. AWS (72%)
5. Azure (58%)
6. Data Warehousing (69%)
7. ETL (76%)
8. Kafka (48%)
9. Kubernetes (54%)
10. Airflow (62%)

SKILL GAPS (moeilijk te vinden):
- Real-time streaming architectuur (Kafka, Flink)
- ML Ops ervaring
- Data mesh kennis
- Scala programming
- Advanced cloud-native architectuur

GEMIDDELD SALARIS (volgens LinkedIn data):
- €68.000 per jaar (alle levels)
- Range: €45.000 - €98.000

MOBILITEIT:
- Gemiddelde tenure: 3,2 jaar
- Retention rate: 81% (blijft >2 jaar bij werkgever)
- Mobiliteit index: Hoog (veel movement tussen bedrijven)

REMOTE WORK:
- Volledig remote: 12%
- Hybrid (2-3 dagen kantoor): 68%
- Volledig op kantoor: 20%

KANDIDAAT MOTIVATIE (volgens profile data):
Top redenen om van baan te wisselen:
1. Werken met moderne technologie (78%)
2. Salaris en benefits (72%)
3. Leer- en groeimogelijkheden (69%)
4. Flexibiliteit en work-life balance (65%)
5. Impact maken (58%)
6. Werkomgeving en cultuur (54%)
    """,

    # Zapier meta data
    'submission_url': 'https://eu.jotform.com/submissions/240123456789',
    'submission_id': '240123456789'
}

# ================================================================
# RUN DE COMPREHENSIVE REPORT CODE
# ================================================================

print("🤖 Starting AI Recruitment Intelligence Report generation...")
print(f"📋 Vacature: {input_data['functietitel']} bij {input_data['bedrijfsnaam']}")
print(f"📊 Test Mode: Gebruik fallback data (geen echte AI call)")
print("")

# Importeer de comprehensive report code
exec(open('zapier-ai-rapport-comprehensive.py').read())

print("")
print("✅ Report generated successfully!")
print(f"📧 Email would be sent to: {output['email_to']}")
print(f"📝 Subject: {output['email_subject']}")
print("")

# Sla HTML op naar file
output_file = 'test-report-output.html'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(output['email_body_html'])

print(f"💾 HTML rapport opgeslagen naar: {output_file}")
print(f"🌐 Open het bestand in je browser om het rapport te bekijken!")
print("")
print("📊 Notion data die zou worden opgeslagen:")
print(f"   - Bedrijf: {output['notion_bedrijfsnaam']}")
print(f"   - Functie: {output['notion_functietitel']}")
print(f"   - Salaris: {output['notion_salaris_range']}")
print(f"   - Schaarste: {output['notion_ai_schaarste']}")
print(f"   - Time-to-hire: {output['notion_ai_time_to_hire']}")
print("")
print("🎉 Test complete!")
