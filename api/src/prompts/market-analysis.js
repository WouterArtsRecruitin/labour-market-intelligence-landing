/**
 * Claude AI Prompt for Labour Market Intelligence Report Generation
 */

export function generateMarketAnalysisPrompt(analysisData) {
  const {
    company,
    position,
    sector,
    location,
    experienceLevel,
    keySkills,
    salaryRange,
    analysisFocus,
    priorities
  } = analysisData;

  const skillsList = Array.isArray(keySkills) ? keySkills.join(', ') : keySkills;
  const salaryInfo = salaryRange?.min && salaryRange?.max
    ? `€${salaryRange.min.toLocaleString()} - €${salaryRange.max.toLocaleString()}`
    : 'Geen specifieke range opgegeven';

  return `Je bent een expert arbeidsmarkt analist en recruitment strategist. Genereer een uitgebreid, professioneel en data-gedreven Labour Market Intelligence rapport voor de volgende functie:

# OPDRACHTGEGEVENS

**Bedrijf:** ${company}
**Functietitel:** ${position}
**Sector/Industrie:** ${sector}
**Locatie/Regio:** ${location}
**Ervaring Niveau:** ${experienceLevel}
**Belangrijkste Vaardigheden:** ${skillsList}
**Salaris Range:** ${salaryInfo}
**Specifieke Analyse Focus:** ${analysisFocus || 'Algemene markt analyse'}

**Analyse Prioriteiten (1-10 schaal):**
- Markt Vraag: ${priorities?.marketDemand || 5}/10
- Concurrentie Analyse: ${priorities?.competitionAnalysis || 5}/10
- Salaris Benchmarking: ${priorities?.salaryBenchmarking || 5}/10
- Recruitment Strategie: ${priorities?.recruitmentStrategy || 5}/10

# RAPPORTSTRUCTUUR

Genereer een comprehensive rapport met de volgende secties. Gebruik realistische marktdata en geef specifieke, actionable insights:

## 1. EXECUTIVE SUMMARY (2-3 alinea's)
- Overall markt assessment
- Belangrijkste conclusies en aanbevelingen
- Urgentie/timing advies
- Key risk & opportunity highlights

## 2. MARKT VRAAG & AANBOD ANALYSE
### 2.1 Huidige Markt Conditie
- Geschatte aantal openstaande vacatures voor deze functie in ${location}
- Vraag/aanbod ratio (kandidaten per vacature)
- Trend analyse (groeiend/krimpend/stabiel)
- Seizoensinvloeden en timing factoren

### 2.2 Markt Drivers
- Waarom is er vraag naar deze rol?
- Welke bedrijfstypes zoeken deze functie?
- Groei drivers en future outlook

### 2.3 Talent Beschikbaarheid
- Geschat aantal beschikbare kandidaten
- Actief vs. passief zoekend
- Geografische spreiding
- Mobiliteit en remote work trends

## 3. CONCURRENTIE ANALYSE
### 3.1 Hiring Concurrentie
- Top 5-10 bedrijven die voor dezelfde kandidaten strijden
- Employer branding sterkte van concurrenten
- Unique selling points van concurrenten
- Market positioning strategie

### 3.2 Recruitment Metrics
- Gemiddelde tijd om te werven (time-to-hire)
- Gemiddeld aantal sollicitaties per vacature
- Conversion ratios (view → apply → interview → offer)
- Acceptance rates in de markt

## 4. SALARIS & COMPENSATIE BENCHMARKING
### 4.1 Salaris Ranges (in €, jaarlijks bruto)
- P10 (laagste 10%): €XX,XXX
- P25 (eerste kwartiel): €XX,XXX
- P50 (mediaan/markt gemiddelde): €XX,XXX
- P75 (derde kwartiel): €XX,XXX
- P90 (hoogste 10%): €XX,XXX

### 4.2 Salaris Drivers
- Impact van ervaring, skills, locatie
- Premium voor specifieke vaardigheden (${skillsList})
- Sector specifieke verschillen
- Remote work impact op compensatie

### 4.3 Totale Compensatie Pakket
- Typische bonus structuren (%)
- Secundaire arbeidsvoorwaarden (auto, pensioen, etc.)
- Stock options / equity (indien relevant)
- Flexibiliteit en work-life balance benefits

### 4.4 Competitive Positioning
- Is de opgegeven range ${salaryInfo} competitief?
- Aanbevelingen voor optimal salary positioning
- Risk van onder/overbetalen

## 5. COMPETENTIE & SKILLS ANALYSE
### 5.1 Must-Have Skills
- Top 5 essentiële technische vaardigheden
- Top 5 essentiële soft skills
- Certificeringen en opleidingen

### 5.2 Nice-to-Have Skills
- Differentiërende vaardigheden
- Emerging skills in deze rol
- Skills gap in de huidige markt

### 5.3 Skills Availability Matrix
Voor elk van de key skills (${skillsList}):
- Beschikbaarheid in de markt (hoog/medium/laag)
- Impact op salaris verwachtingen
- Alternatieven en trainingsmogelijkheden

## 6. RECRUITMENT STRATEGIE & AANBEVELINGEN
### 6.1 Sourcing Strategie
- Best performing channels (LinkedIn, job boards, referrals, etc.)
- Passive vs. active sourcing mix
- Niche platforms en communities
- Recruitment marketing aanpak

### 6.2 Job Description Optimalisatie
- Aanbevolen functietitel varianten
- Key selling points voor de rol
- Must-avoid red flags
- Diversity & inclusion considerations

### 6.3 Interview & Selection Process
- Aanbevolen aantal interview rondes
- Assessment methodes
- Key competenties om te testen
- Time-to-decision optimalisatie

### 6.4 Employer Value Proposition (EVP)
- Wat moeten jullie uitdragen?
- Competitive advantages te benadrukken
- Hoe te differentiëren van concurrenten

### 6.5 Timing & Planning
- Best time to post (dag/maand)
- Campaign duration aanbeveling
- Follow-up strategie
- Contingency planning

## 7. RISICO'S & UITDAGINGEN
### 7.1 Recruitment Risks
- Talent shortage risks
- Budget constraints impact
- Competition van andere employers
- Market timing risks

### 7.2 Mitigation Strategies
- Concrete actieplannen voor elk risico
- Plan B opties
- Budget flexibiliteit aanbevelingen

## 8. MARKET OPPORTUNITY SCORE & INSIGHTS
### 8.1 Overall Score (1-100)
Geef een overall market opportunity score gebaseerd op:
- Markt vraag niveau (30%)
- Talent beschikbaarheid (25%)
- Salaris competitiviteit (25%)
- Timing (20%)

**SCORE: XX/100**

### 8.2 Sentiment Analysis
- BULLISH / NEUTRAL / BEARISH market sentiment
- Reasoning voor dit sentiment
- Forward looking indicators

### 8.3 Quick Wins
- 3-5 immediate actions die impact maken
- Low hanging fruit opportunities
- 30-60-90 dagen roadmap

## 9. DATA BRONNEN & METHODOLOGIE
Lijst de (fictieve maar realistische) databronnen:
- LinkedIn Talent Insights
- Glassdoor Salary Data
- Indeed Hiring Lab Statistics
- CBS Nederland Arbeidsmarkt Data
- Randstad/ManpowerGroup Reports
- Custom surveys en benchmark studies

## 10. NEXT STEPS & ACTION ITEMS
Concrete checklist van acties:
1. [ ] Actie 1
2. [ ] Actie 2
3. [ ] etc.

---

# BELANGRIJK:
- Gebruik realistische cijfers en data (fictief maar geloofwaardig)
- Geef specifieke, actionable insights - geen vage adviezen
- Houd rekening met Nederlandse arbeidsmarkt context
- Gebruik professionele toon geschikt voor C-level executives
- Vermijd AI clichés zoals "delve into", "tapestry", "landscape"
- Wees direct, data-driven en praktisch

Genereer nu het volledige rapport in Markdown formaat:`;
}

/**
 * Generate a shorter, summary version prompt for faster responses
 */
export function generateQuickAnalysisPrompt(analysisData) {
  const { company, position, sector, location, keySkills, salaryRange } = analysisData;

  return `Genereer een beknopte arbeidsmarkt analyse (max 1000 woorden) voor:
- Functie: ${position} bij ${company}
- Sector: ${sector}
- Locatie: ${location}
- Key Skills: ${Array.isArray(keySkills) ? keySkills.join(', ') : keySkills}
- Salaris: ${salaryRange?.min && salaryRange?.max ? `€${salaryRange.min}-${salaryRange.max}` : 'n.v.t.'}

Focus op:
1. Markt vraag & aanbod (kort)
2. Salaris benchmark (P50 + range)
3. Top 3 concrete recruitment aanbevelingen
4. Overall opportunity score (1-100)

Wees direct, data-driven en geef concrete cijfers.`;
}
