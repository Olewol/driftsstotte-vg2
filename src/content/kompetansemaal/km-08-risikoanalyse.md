---
title: "KM-08: Risikoanalyse / Risk Analysis"
emne: kompetansemaal
kompetansemaal:
  - km-08
kilder:
  - https://www.udir.no/lk20/itk02-01/kompetansemaal-og-vurdering/kv372
  - https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/
  - https://www.digdir.no/informasjonssikkerhet/
  - https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/
tags: [km-08, risikoanalyse, risikovurdering, sikkerhet]
flashcards: false
public: true
---

# KM-08: Risikoanalyse / Risk Analysis

## 🎯 Mål / Competency Goal

**Norsk:** Gjennomføre risikoanalyse av nettverk og tjenester i en virksomhets systemer og foreslå tiltak for å redusere risikoen

**English:** Conduct risk analysis of networks and services in an organization's systems and propose measures to reduce risk

---

## 📘 Forklaring / Explanation

### Norsk
Risikoanalyse er en systematisk metode for å identifisere, vurdere og prioritere risikoer. Målet er å finne ut hva som kan gå galt, hvor sannsynlig det er, og hvor alvorlig konsekvensen vil bli[^1].

**Risiko = Sannsynlighet × Konsekvens** — jo høyere sannsynlighet og/eller alvorligere konsekvens, desto høyere risiko.

**Stegene i en risikoanalyse:**
1. **Identifisere** — Hvilke trusler finnes? (brann, hacking, strømbrudd)
2. **Analysere** — Hvor sannsynlig? Hvor alvorlig?
3. **Evaluere** — Hvilke risikoer må håndteres?
4. **Behandle** — Hva gjør vi? (redusere, overføre, akseptere, unngå)
5. **Overvåke** — Har tiltakene effekt? Har trusselbildet endret seg?

**Metoder for risikohåndtering:**
- **Redusere** — Installere brannmur, oppdatere programvare
- **Overføre** — Tegne forsikring, bruke skytjeneste
- **Akseptere** — Godta risikoen (for små/ukritiske systemer)
- **Unngå** — Slutte å bruke systemet

### English
Risk analysis is a systematic method to identify, assess, and prioritize risks. The goal is to find out what can go wrong, how likely it is, and how serious the consequences will be[^1].

**Risk = Probability × Impact** — the higher the probability and/or more serious the impact, the higher the risk.

**Steps in a risk analysis:**
1. **Identify** — What threats exist? (fire, hacking, power outage)
2. **Analyze** — How likely? How serious?
3. **Evaluate** — Which risks must be handled?
4. **Treat** — What do we do? (reduce, transfer, accept, avoid)
5. **Monitor** — Are the measures effective? Has the threat landscape changed?

**Risk treatment methods:**
- **Reduce** — Install firewall, update software
- **Transfer** — Take out insurance, use cloud service
- **Accept** — Accept the risk (for small/non-critical systems)
- **Avoid** — Stop using the system

---

## 💡 Eksempler / Examples

### Norsk

**Eksempel 1: Risikomatrise for skolens systemer**
| Risiko | Sannsynlighet | Konsekvens | Risikonivå | Tiltak |
|--------|--------------|------------|------------|--------|
| Strømbrudd | Middels | Høy | Høy | UPS + nødstrømsaggregat |
| Phishing-epost | Høy | Middels | Høy | Opplæring av ansatte |
| Brann i serverrom | Lav | Svært høy | Middels | Brannslukking + backup |

**Eksempel 2: Risikoanalyse for skolens nettside**
Skolens hjemmeside kan bli utsatt for DDoS-angrep. Det er middels sannsynlig, men konsekvensen er lav (siden er ikke kritisk). Risikoen aksepteres uten tiltak.

### English

**Example: Risk Matrix for School Systems**
| Risk | Probability | Impact | Risk Level | Measure |
|------|------------|--------|------------|---------|
| Power outage | Medium | High | High | UPS + generator |
| Phishing | High | Medium | High | Staff training |
| Server room fire | Low | Very high | Medium | Fire suppression + backup |

**Example: Risk Analysis of School Website**
The school's website could be targeted by a DDoS attack. The probability is medium, but the impact is low (the site is not critical). The risk is accepted without measures.

---

## 📝 Oppsummering / Summary

| Norsk | English |
|-------|---------|
| Risikoanalyse = systematisering av usikkerhet | Risk analysis = systematizing uncertainty |
| Risiko = sannsynlighet × konsekvens | Risk = probability × impact |
| Fire måter å håndtere risiko på: redusere, overføre, akseptere, unngå | Four ways to handle risk: reduce, transfer, accept, avoid |
| Risikoanalyse er en kontinuerlig prosess — trusselbildet endrer seg | Risk analysis is a continuous process — threats change over time |

---

## 🔧 Bridging Exercises / Praksisoppgaver

### Norsk — Praksisoppgaver

**Oppgave 1: Lag en risikomatrise for skolens IT-systemer**
Eleven skal gjennomføre en risikoanalyse for en videregående skole.
- Identifiser minst 10 risikoer innen: maskinvare, programvare, nettverk, mennesker, ytre miljø
- For hver risiko: beskriv trusselen, vurder sannsynlighet (1-5) og konsekvens (1-5)
- Regn ut risikonivå = S × K
- Plasser risikoene i en risikomatrise (fargekodet: grønn/gul/rød)
- Foreslå minst 3 tiltak for hver risiko på rødt nivå
- Konkluder: Hvilke tre risikoer bør skolen prioritere å håndtere først?

**Oppgave 2: Risikoanalyse av skolens nettside**
Skolens hjemmeside (WordPress) skal risikovurderes for 5 scenarier:
- DDoS-angrep slår siden ut i en uke
- Hackere får tilgang til publiseringssystemet
- Personopplysninger lekkes via sårbarhet i innloggingsskjema
- Innhold blir erstattet med upassende materiale
- Serverkrasj på grunn av strømbrudd
For hvert scenario: sannsynlighet, konsekvens, risikonivå, risikostrategi (redusere/overføre/akseptere/unngå), konkrete tiltak.

**Veiledning / Solution Guidelines:**
- Oppgave 1: Typiske risikoer: ransomware (S:3 K:5 = 15 → rød), strømbrudd (S:3 K:4 = 12 → rød), phishing (S:4 K:3 = 12 → rød), brann (S:1 K:5 = 5 → gul), harddisk-feil (S:3 K:3 = 9 → gul). Prioriter etter risikonivå.
- Oppgave 2: DDoS — middels sannsynlig, middels konsekvens → aksepteres med enkel DDoS-beskyttelse. Personopplysninger — lav sannsynlighet, høy konsekvens → må ha kryptering og sikkerhetsskanning. Innholdskapring — middels sannsynlig, høy konsekvens → 2FA.

### English — Practical Exercises

**Exercise 1: Create a Risk Matrix for the School's IT Systems**
Identify at least 10 risks across: hardware, software, network, people, environment.
- For each: describe the threat, rate probability (1-5) and impact (1-5)
- Calculate risk level = P × I
- Map risks in a color-coded risk matrix (green/yellow/red)
- Propose at least 3 measures for each red-level risk
- Conclude: Which three risks should the school prioritize first?

**Exercise 2: Risk Analysis of the School Website**
Assess the school's website for 5 scenarios (DDoS, hacking, data leak, content hijack, server crash). For each: probability, impact, risk level, strategy (reduce/transfer/accept/avoid), concrete measures.

**Solution Guidelines:**
- Exercise 1: Typical risks — ransomware (3×5=15 red), power outage (3×4=12 red), phishing (4×3=12 red), fire (1×5=5 yellow), disk failure (3×3=9 yellow). Prioritize by risk level.
- Exercise 2: DDoS — medium/low prob, medium impact → accept with basic DDoS protection. Data leak — low prob, high impact → encryption + scanning. Content hijack — medium prob, high impact → 2FA.

## 🔗 Relevante artikler / Related Articles

- [[risikoanalyse]] — Gjennomføring av risikoanalyse i praksis
- [[trusselbildet]] — Forstå truslene for å kunne analysere risiko
- [[it-losninger-med-sikkerhet]] — Sikkerhetstiltak for å redusere risiko (KM-10)

## 📚 Kilder / Sources

[^1]: Udir (2020). Læreplan i Vg2 informasjonsteknologi. https://www.udir.no/lk20/itk02-01/
[^2]: NSM. Grunnprinsipper for IKT-sikkerhet. https://nsm.no/
[^3]: Digdir. Informasjonssikkerhet. https://www.digdir.no/informasjonssikkerhet/
