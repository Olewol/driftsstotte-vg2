---
title: "IT-løsninger med innebygd sikkerhet"
emne: sikkerhet
kompetansemaal:
  - km-10
kilder:
  - ndla
  - nsm
  - microsoft
tags: []
flashcards: true
public: true
---

## Introduksjon

Sikkerhet er ikke noe du legger til etter at et system er bygget. Det er et designkrav som må integreres fra første kravspesifikasjon til løpende drift. Denne artikkelen handler om prinsippene og praksisen bak det å bygge og drifte IT-løsninger der sikkerhet er en naturlig del av arkitekturen – ikke en ettertanke.

NSM Grunnprinsipper for IKT-sikkerhet (v2.1, 2024) understreker at god IKT-sikkerhet krever både tekniske og organisatoriske tiltak over hele livssyklusen til et system. Her ser vi på de viktigste prinsippene og metodene.

---

## Teori

### Security by Design

**Security by Design** er prinsippet om at sikkerhet integreres i alle faser av systemutvikling og -drift – fra kravspesifikasjon, design, utvikling og testing til produksjon og avvikling.

Microsofts **SDL (Security Development Lifecycle)** er en referansemodell med fasene:
1. Opplæring i sikker koding
2. Kravspesifikasjon inkl. sikkerhetskrav
3. Trusselmodellering (threat modeling)
4. Sikkerhetsorientert design
5. Sikker koding og code review
6. Sikkerhetstest og penetrasjonstest
7. Respons og vedlikehold

Motsetningen – å legge til sikkerhet etter at systemet er bygget – er dyrere, vanskeligere og gir svakere sikkerhet. Det er langt enklere å innlemme kryptering og tilgangskontroll i et system fra start enn å retrofitte det inn i eksisterende arkitektur.

---

### Zero Trust-modellen

**Zero Trust** er en sikkerhetsarkitektur basert på prinsippet:

> **«Aldri stol – alltid verifiser»** (Never trust, always verify)

Tradisjonell sikkerhetstenkning antok at alt innenfor bedriftsnettverket var trygt. Zero Trust forkaster denne antagelsen og behandler all tilgang som potensielt farlig – uavhengig av om brukeren er innenfor eller utenfor bedriftsnettverket.

**Tre kjerneprinsippler (Microsoft Zero Trust):**

| Prinsipp | Norsk | Hva betyr det i praksis |
|---|---|---|
| **Verify explicitly** | Verifiser alltid | Autentiser basert på alle tilgjengelige datapunkter: brukeridentitet, enhet, lokasjon, tid |
| **Use least privilege** | Minste privilegium | Gi kun den tilgangen som er strengt nødvendig. Bruk JIT (Just-In-Time) og JEA (Just-Enough-Access) |
| **Assume breach** | Anta brudd | Design systemet som om det allerede er kompromittert. Segmenter tilgang, krypter end-to-end, overvåk aktivt |

**Praktiske Zero Trust-tiltak:**
- MFA (tofaktorautentisering) for alle brukere – alltid
- Betinget tilgang (Conditional Access): gi tilgang kun fra godkjente enheter med oppdatert programvare
- Mikrosegmentering: begrens hvilke systemer brukere og applikasjoner kan nå
- Ingen implisitt tillit til bedriftsnettverket – VPN er ikke lenger nok

---

### Patchhåndtering

Kjente sårbarheter i programvare er en av de hyppigste inngangsdørene for angripere. Patchhåndtering er den systematiske prosessen med å holde all programvare, firmware og operativsystemer oppdatert.

**Patch-syklus:**
1. **Identifiser:** kartlegg hvilke systemer og versjoner som er i bruk (inventarliste)
2. **Evaluer:** vurder alvorlighetsgrad av nye patcher (kritisk / viktig / moderat)
3. **Test:** test patcher i et testmiljø før produksjonsrullering
4. **Rull ut:** distribuer patcher via administrasjonsverktøy (WSUS, Intune, apt/yum)
5. **Verifiser:** bekreft at patchene er installert og systemene fungerer

**Verktøy:**
- Windows: **WSUS** (Windows Server Update Services), **Microsoft Intune**
- Linux: `apt update && apt upgrade` (Debian/Ubuntu), `dnf update` (RHEL/Fedora)
- Nettverk: leverandørens administrasjonsportal for firmware

**NSM anbefaling:** Kritiske patcher bør installeres innen 24–72 timer. Eldre OWASP A06 (Vulnerable and Outdated Components) understreker at utdaterte komponenter er en av de hyppigste angrepsvektorene.

---

### Logging og SIEM

Logging er registrering av hendelser i et IT-system. Uten logging er det umulig å oppdage angrep, rekonstruere hendelsesforløp eller etterforsake brudd.

**Hva bør logges:**
- Innloggingsforsøk (vellykkede og mislykkede)
- Tilgangsendringer (nye brukere, endrede rettigheter)
- Systemendringer og konfigurasjonsendringer
- Brannmuraktivitet (blokkert trafikk)
- Applikasjonsfeil og sikkerhetshendelser

**SIEM (Security Information and Event Management):**
SIEM samler logger fra alle systemer til et sentralt sted, korrelerer hendelser og varsler om mistenkelig aktivitet.

- **Azure Monitor / Microsoft Sentinel:** skybasert SIEM. Sentinel bruker ML-basert anomalideteksjon og kan automatisk trigge respons.
- **Splunk, IBM QRadar:** kommersielle SIEM-løsninger
- **Wazuh, Graylog:** åpne alternativer

OWASP identifiserer manglende logging og overvåkning (A09) som en kritisk sårbarhet – uten logger vet du ikke at du er angrepet.

---

### Tilgangskontroll og IAM

**IAM (Identity and Access Management)** handler om å kontrollere hvem som kan gjøre hva i IT-systemene.

**Prinsippet om minste privilegium:**
Brukere, applikasjoner og tjenester skal kun ha de tilgangene som er strengt nødvendige for jobben. Ingen bruker bør ha domeneadministratorrettigheter til daglig.

**Rollebasert tilgangskontroll (RBAC):**
Tilganger knyttes til roller (f.eks. «Helpdesk», «Regnskapsmedarbeider», «IT-admin»), ikke til individuelle brukere. Brukere tildeles roller.

**Verktøy:**
- **Active Directory (AD):** brukerkontoer, grupper og rettighetsstyring on-premises
- **Azure Entra ID (tidligere Azure AD):** skybasert IAM. Støtter SSO (Single Sign-On), MFA og Conditional Access.
- **MFA:** kombinerer noe du vet (passord), noe du har (autentiseringsapp/SMS) og/eller noe du er (biometri). Blokkerer over 99 % av kontoovertak ifølge Microsoft.

---

### Backup som sikkerhetstiltak

Backup er ikke bare en driftsrutine – det er et sikkerhetstiltak og det viktigste reaktive tiltaket mot ransomware.

**3-2-1-regelen:**
- **3** kopier av dataene
- på **2** forskjellige medier (f.eks. disk + tape eller disk + sky)
- med **1** offsite-kopi (fysisk eller sky-basert)

**Praktisk:**
- Test gjenoppretting jevnlig – en backup er verdiløs hvis den ikke kan gjenopprettes
- Isoler backup-systemer fra produksjonsnettverket (ransomware krypterer alt det når)
- Azure Backup: integrert skybackup for virtuelle maskiner, databaser og filservere

---

### BCDR – Business Continuity og Disaster Recovery

**Business Continuity (BC)** handler om å opprettholde kritiske funksjoner under en krise.
**Disaster Recovery (DR)** handler om å gjenopprette IT-systemer etter en katastrofal hendelse.

Sentrale begreper:

| Begrep | Forklaring |
|---|---|
| **RTO (Recovery Time Objective)** | Maksimalt akseptabel nedetid – hvor lang tid tar gjenoppretting? |
| **RPO (Recovery Point Objective)** | Maksimalt akseptabelt tap av data – hvor gammel kan siste backup være? |
| **Failover** | Automatisk overgang til et redundant system ved svikt |
| **DR-plan** | Dokumentert prosedyre for gjenoppretting – testes jevnlig |

Eksempel: Et sykehus kan ha RTO = 4 timer og RPO = 1 time for pasientjournalsystemet. Dette krever replikering av data med maksimalt 1 times mellomrom og en gjenopprettingsprosedyre som er testet og tar under 4 timer.

---

### Defense in Depth

**Defense in Depth** (lagdelt forsvar) er prinsippet om at ingen enkelt sikkerhetsmekanisme er tilstrekkelig – sikkerhet bygges opp i lag, slik at selv om ett lag svikter, stopper neste lag angriperen.

```
Lag 7: Data          → Kryptering, tilgangskontroll, DLP
Lag 6: Applikasjon   → WAF, sikker koding, patchhåndtering
Lag 5: Identitet     → MFA, Zero Trust, IAM, RBAC
Lag 4: Nettverk      → Brannmur, DMZ, segmentering, IPS
Lag 3: Datamaskin    → Antivirus/EDR, vertsbasert brannmur, OS-patcher
Lag 2: Fysisk        → Adgangskontroll til serverrom, låste rack
Lag 1: Retningslinjer→ Sikkerhetspolicyer, opplæring, rutiner
```

Azure benytter eksplisitt denne modellen i sin sikkerhetsdokumentasjon.

---

## Eksempel / lab

**Scenario: Vurder sikkerhetsnivået til et fiktivt skolenettverk**

Solberg vgs har følgende IT-infrastruktur:
- Windows Server 2022 (AD, filserver, WSUS)
- 350 Windows 11-klienter administrert via Intune
- Microsoft 365 med Entra ID og MFA aktivert for ansatte
- Ubiquiti-ruter med VLAN for ansatte, elever og gjester
- Brannmur med stateful inspection, default-deny
- Daglig backup til Azure Backup med offsite-kopi

**Vurder med Defense in Depth-modellen:**

| Lag | Tiltak til stede | Mangler |
|---|---|---|
| Retningslinjer | Sikkerhetspolicy finnes | Ingen jevnlig phishing-trening |
| Fysisk | Serverrom er låst | Ingen adgangslogg |
| Nettverk | VLAN-segmentering, brannmur | IDS/IPS mangler |
| Datamaskin | Windows Defender EDR | Elev-PC-er mangler Intune-administrasjon |
| Identitet | MFA for ansatte | MFA ikke aktivert for elever |
| Applikasjon | WSUS-patching | Applikasjonsprogramvare patchet manuelt |
| Data | Azure Backup | Backup-gjenoppretting ikke testet siste 6 måneder |

**Konklusjon:** God grunnleggende sikkerhet. Prioriterte forbedringstiltak: aktiver MFA for elever, implementer IDS, integrer elev-PC-er i Intune, og planlegg kvartalsvis DR-test.

---

## Quiz

<details><summary>Spørsmål 1: Hva er de tre kjerneprinsippene i Zero Trust?</summary>

**Svar:** Verify explicitly (verifiser alltid), Use least privilege (minste privilegium), og Assume breach (anta brudd). Sammen betyr dette at ingen bruker, enhet eller nettverk automatisk stoler på – all tilgang verifiseres og begrenses.

</details>

<details><summary>Spørsmål 2: Hva er 3-2-1-regelen for backup?</summary>

**Svar:** 3 kopier av dataene, på 2 forskjellige medier, med 1 offsite-kopi. Offsite-kopien sikrer at backup overlever lokale katastrofer som brann eller ransomware-angrep.

</details>

<details><summary>Spørsmål 3: Hva er forskjellen mellom RTO og RPO?</summary>

**Svar:** RTO (Recovery Time Objective) er maksimalt akseptabel nedetid – hvor lang tid gjenoppretting kan ta. RPO (Recovery Point Objective) er maksimalt akseptabelt datatap – hvor gammel siste backup kan være.

</details>

<details><summary>Spørsmål 4: Hvorfor er patchhåndtering viktig for sikkerhet?</summary>

**Svar:** Kjente sårbarheter i programvare er en av de vanligste angrepsvektorene. Patcher lukker disse sårbarhetene. Utdaterte komponenter (OWASP A06) er konsekvent blant de hyppigste årsaker til kompromitteringer.

</details>

<details><summary>Spørsmål 5: Hva er SIEM, og hvilken sårbarhet kobler OWASP til manglende logging?</summary>

**Svar:** SIEM (Security Information and Event Management) samler logger fra alle systemer sentralt, korrelerer hendelser og varsler om mistenkelig aktivitet. OWASP Top 10 A09 identifiserer manglende logging og overvåkning som en kritisk sårbarhet – uten logger oppdager du ikke angrep.

</details>

---

## Flashcards

Security by Design :: Prinsipp om at sikkerhet integreres i alle faser av systemutvikling og -drift, ikke legges til etterpå
Zero Trust :: Sikkerhetsarkitektur basert på «aldri stol, alltid verifiser» – ingen implisitt tillit til brukere, enheter eller nettverk
Minste privilegium :: Prinsipp om at brukere og systemer kun gis de tilgangene som er strengt nødvendige
SIEM :: Security Information and Event Management – sentralisert logginnsamling og hendelsesanalyse. Eks: Microsoft Sentinel
3-2-1-regelen :: Backup-prinsipp: 3 kopier, 2 medier, 1 offsite-kopi
RTO :: Recovery Time Objective – maksimalt akseptabel nedetid under gjenoppretting
RPO :: Recovery Point Objective – maksimalt akseptabelt datatap, angir hvor gammel siste backup kan være
BCDR :: Business Continuity and Disaster Recovery – planer for å opprettholde og gjenopprette IT-tjenester under og etter katastrofale hendelser
Defense in Depth :: Lagdelt sikkerhet – retningslinjer, fysisk, nettverk, datamaskin, identitet, applikasjon og data
RBAC :: Role-Based Access Control – tilganger knyttes til roller, ikke individuelle brukere

---

## Ressurser

- [Microsoft – Zero Trust (engelsk)](https://learn.microsoft.com/en-us/security/zero-trust/zero-trust-overview)
- [Microsoft – Azure sikkerhetsoversikt](https://learn.microsoft.com/en-us/azure/security/fundamentals/overview)
- [NSM Grunnprinsipper – Beskytt og oppretthold](https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/)
- [NDLA – Oppdatere Linux med APT](https://ndla.no)
- [NDLA – Brukerkontoer i Active Directory](https://ndla.no)
