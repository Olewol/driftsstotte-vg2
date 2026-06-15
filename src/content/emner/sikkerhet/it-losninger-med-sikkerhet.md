---
title: "IT-løsninger med innebygd sikkerhet"
emne: sikkerhet
kompetansemaal:

  - km-10

kilder:

  - ndla
  - nsm
  - microsoft
  - <https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/>
  - <https://www.digdir.no/nasjonal-arkitektur/nulltillitsarkitektur/4054>
  - <https://www.datatilsynet.no/>
  - <https://owasp.org/www-project-top-ten/>
  - <https://www.digdir.no/informasjonssikkerhet/>

video: <https://www.youtube.com/watch?v=R9NCYvR3h3w>
notebooklm: true
tags: []
flashcards: <https://notebooklm.google.com/notebook/3e72e53a-b0ca-4f05-a597-a8eea5ea7ea9>
public: true
---

## Introduksjon

SSikkerhet er ikke noe du legger til etter at et system er bygget. Det er et designkrav som må integreres fra første
SSkravspesifikasjon til løpende drift. Denne artikkelen handler om prinsippene og praksisen bak det å bygge og drifte
SIT-løsninger der sikkerhet er en naturlig del av arkitekturen – ikke en ettertanke.

NNSM Grunnprinsipper for IKT-sikkerhet (v2.1, 2024) understreker at god IKT-sikkerhet krever både tekniske og
Norganisatoriske tiltak over hele livssyklusen til et system.[^1] Her ser vi på de viktigste prinsippene og metodene.

PPrinsippene i denne artikkelen henger tett sammen med [[brannmur|brannmur og nettverkssikkerhet]],
PP[[bruker-og-tilgangsstyring]] og [[backup-og-gjenoppretting]]. God IT-sikkerhet er aldri ett enkelt tiltak – det er
Psummen av mange overlappende lag.

---

## Teori

### Security by Design

***Security by Design**er prinsippet om at sikkerhet integreres i alle faser av systemutvikling og -drift – fra
*kravspesifikasjon, design, utvikling og testing til produksjon og avvikling.

Microsofts**SDL (Security Development Lifecycle)**er en referansemodell[^2] med fasene:

1. Opplæring i sikker koding
2. Kravspesifikasjon inkl. sikkerhetskrav
3. Trusselmodellering (threat modeling)
4. Sikkerhetsorientert design
5. Sikker koding og code review
6. Sikkerhetstest og penetrasjonstest
7. Respons og vedlikehold

MMotsetningen – å legge til sikkerhet etter at systemet er bygget – er dyrere, vanskeligere og gir svakere sikkerhet.
MMDet er langt enklere å innlemme kryptering og tilgangskontroll i et system fra start enn å retrofitte det inn i
Meksisterende arkitektur.

---

### Zero Trust-modellen

**Zero Trust**er en sikkerhetsarkitektur basert på prinsippet:

>**«Aldri stol – alltid verifiser»**(Never trust, always verify)

TTradisjonell sikkerhetstenkning antok at alt innenfor bedriftsnettverket var trygt.
TTZero Trust forkaster denne antagelsen og behandler all tilgang som potensielt farlig – uavhengig av om brukeren er
Tinnenfor eller utenfor bedriftsnettverket.

**Tre kjerneprinsippler (Microsoft Zero Trust):**[^3]

|| Prinsipp | Norsk | Hva betyr det i praksis |
|| --- | --- | --- |
|| **Verify explicitly** | Verifiser alltid | Autentiser basert på alle tilgjengelige datapunkter: brukeridentitet, enhet, lokasjon, tid |
|| **Use least privilege** | Minste privilegium | Gi kun den tilgangen som er strengt nødvendig. Bruk JIT (Just-In-Time) og JEA (Just-Enough-Access) |
|| **Assume breach** | Anta brudd | Design systemet som om det allerede er kompromittert. Segmenter tilgang, krypter end-to-end, overvåk aktivt |

*## Praktiske Zero Trust-tiltak:

- MFA (tofaktorautentisering) for alle brukere – alltid
- Betinget tilgang (Conditional Access): gi tilgang kun fra godkjente enheter med oppdatert programvare
- Mikrosegmentering: begrens hvilke systemer brukere og applikasjoner kan nå
- Ingen implisitt tillit til bedriftsnettverket – VPN er ikke lenger nok

DDigitaliseringsdirektoratet (Digdir) har publisert en norsk veileder for nulltillitsarkitektur som beskriver hvordan
DZero Trust implementeres i offentlig sektor.[^4]

---

### Patchhåndtering

KKjente sårbarheter i programvare er en av de hyppigste inngangsdørene for angripere.
KPatchhåndtering er den systematiske prosessen med å holde all programvare, firmware og operativsystemer oppdatert.

*## Patch-syklus:
1.**Identifiser:**kartlegg hvilke systemer og versjoner som er i bruk (inventarliste)
2.**Evaluer:**vurder alvorlighetsgrad av nye patcher (kritisk / viktig / moderat)
3.**Test:**test patcher i et testmiljø før produksjonsrullering
4.**Rull ut:**distribuer patcher via administrasjonsverktøy (WSUS, Intune, apt/yum)
5.**Verifiser:**bekreft at patchene er installert og systemene fungerer

*## Verktøy:

- Windows:**WSUS**(Windows Server Update Services),**Microsoft Intune**
- Linux: `apt update && apt upgrade`(Debian/Ubuntu),`dnf update` (RHEL/Fedora)
- Nettverk: leverandørens administrasjonsportal for firmware

***NSM anbefaling:**Kritiske patcher bør installeres innen 24–72 timer. Eldre OWASP A06 (Vulnerable and Outdated
*Components) understreker at utdaterte komponenter er en av de hyppigste angrepsvektorene.[^5]

AAutomatisering av patchprosessen er nøkkelen til å redusere sårbarhetsvinduet – jo kortere tid fra en patch er
Atilgjengelig til den er installert, jo mindre tid har angripere til å utnytte kjente hull.

---

### Logging og SIEM

LLogging er registrering av hendelser i et IT-system. Uten logging er det umulig å oppdage angrep, rekonstruere
Lhendelsesforløp eller etterforsake brudd.

*## Hva bør logges:

- Innloggingsforsøk (vellykkede og mislykkede)
- Tilgangsendringer (nye brukere, endrede rettigheter)
- Systemendringer og konfigurasjonsendringer
- Brannmuraktivitet (blokkert trafikk)
- Applikasjonsfeil og sikkerhetshendelser

*## SIEM (Security Information and Event Management):
SIEM samler logger fra alle systemer til et sentralt sted, korrelerer hendelser og varsler om mistenkelig aktivitet.

--**Azure Monitor / Microsoft Sentinel:**skybasert SIEM. Sentinel bruker ML-basert anomalideteksjon og kan automatisk
-trigge respons.
-**Splunk, IBM QRadar:**kommersielle SIEM-løsninger
-**Wazuh, Graylog:**åpne alternativer

OOWASP identifiserer manglende logging og overvåkning (A09) som en kritisk sårbarhet – uten logger vet du ikke at du er
Oangrepet.[^5]

---

### Tilgangskontroll og IAM

**IAM (Identity and Access Management)**handler om å kontrollere hvem som kan gjøre hva i IT-systemene.

*## Prinsippet om minste privilegium:
BBrukere, applikasjoner og tjenester skal kun ha de tilgangene som er strengt nødvendige for jobben.
BIngen bruker bør ha domeneadministratorrettigheter til daglig.

*## Rollebasert tilgangskontroll (RBAC):
TTilganger knyttes til roller (f.eks. «Helpdesk», «Regnskapsmedarbeider», «IT-admin»), ikke til individuelle brukere.
TBrukere tildeles roller.

*## Verktøy:
-**Active Directory (AD):**brukerkontoer, grupper og rettighetsstyring on-premises. Se [[active-directory]].
-**Azure Entra ID (tidligere Azure AD):**skybasert IAM. Støtter SSO (Single Sign-On), MFA og Conditional Access.
--**MFA:**kombinerer noe du vet (passord), noe du har (autentiseringsapp/SMS) og/eller noe du er (biometri).
-Blokkerer over 99 % av kontoovertak ifølge Microsoft.[^6]

Se også [[bruker-og-tilgangsstyring]] for praktisk gjennomgang av tilgangsstyring.

---

### Backup som sikkerhetstiltak

Backup er ikke bare en driftsrutine – det er et sikkerhetstiltak og det viktigste reaktive tiltaket mot ransomware.

*## 3-2-1-regelen:
-**3**kopier av dataene

- på**2**forskjellige medier (f.eks. disk + tape eller disk + sky)
- med**1**offsite-kopi (fysisk eller sky-basert)

*## Praktisk:

- Test gjenoppretting jevnlig – en backup er verdiløs hvis den ikke kan gjenopprettes
- Isoler backup-systemer fra produksjonsnettverket (ransomware krypterer alt det når)
- Azure Backup: integrert skybackup for virtuelle maskiner, databaser og filservere

Se [[backup-og-gjenoppretting]] for detaljert gjennomgang av backup-strategier og gjenopprettingsplaner.

---

### BCDR – Business Continuity og Disaster Recovery

**Business Continuity (BC)**handler om å opprettholde kritiske funksjoner under en krise.
**Disaster Recovery (DR)**handler om å gjenopprette IT-systemer etter en katastrofal hendelse.

Sentrale begreper:

|| Begrep | Forklaring |
|| --- | --- |
|| **RTO (Recovery Time Objective)** | Maksimalt akseptabel nedetid – hvor lang tid tar gjenoppretting? |
|| **RPO (Recovery Point Objective)** | Maksimalt akseptabelt tap av data – hvor gammel kan siste backup være? |
|| **Failover** | Automatisk overgang til et redundant system ved svikt |
|| **DR-plan** | Dokumentert prosedyre for gjenoppretting – testes jevnlig |

EEksempel: Et sykehus kan ha RTO = 4 timer og RPO = 1 time for pasientjournalsystemet.
EEDette krever replikering av data med maksimalt 1 times mellomrom og en gjenopprettingsprosedyre som er testet og tar
Eunder 4 timer.

---

### Defense in Depth

***Defense in Depth**(lagdelt forsvar) er prinsippet om at ingen enkelt sikkerhetsmekanisme er tilstrekkelig – sikkerhet
*bygges opp i lag, slik at selv om ett lag svikter, stopper neste lag angriperen.

```diff
Lag 7: Data          → Kryptering, tilgangskontroll, DLP
Lag 6: Applikasjon   → WAF, sikker koding, patchhåndtering
Lag 5: Identitet     → MFA, Zero Trust, IAM, RBAC
Lag 4: Nettverk      → Brannmur, DMZ, segmentering, IPS
Lag 3: Datamaskin    → Antivirus/EDR, vertsbasert brannmur, OS-patcher
Lag 2: Fysisk        → Adgangskontroll til serverrom, låste rack
Lag 1: Retningslinjer→ Sikkerhetspolicyer, opplæring, rutiner
```

Azure benytter eksplisitt denne modellen i sin sikkerhetsdokumentasjon.[^7]

MMikrosegmentering er et konkret tiltak for å implementere Defense in Depth på nettverksnivå: ved å begrense hvilke
Msystemer og tjenester som kan snakke sammen, reduseres skadeomfanget dramatisk hvis ett system kompromitteres.

---

## Eksempel / lab

*## Scenario: Vurder sikkerhetsnivået til et fiktivt skolenettverk

Solberg vgs har følgende IT-infrastruktur:

- Windows Server 2022 (AD, filserver, WSUS)
- 350 Windows 11-klienter administrert via Intune
- Microsoft 365 med Entra ID og MFA aktivert for ansatte
- Ubiquiti-ruter med VLAN for ansatte, elever og gjester
- Brannmur med stateful inspection, default-deny
- Daglig backup til Azure Backup med offsite-kopi

*## Vurder med Defense in Depth-modellen:

|| Lag | Tiltak til stede | Mangler |
|| --- | --- | --- |
|| Retningslinjer | Sikkerhetspolicy finnes | Ingen jevnlig phishing-trening |
|| Fysisk | Serverrom er låst | Ingen adgangslogg |
|| Nettverk | VLAN-segmentering, brannmur | IDS/IPS mangler |
|| Datamaskin | Windows Defender EDR | Elev-PC-er mangler Intune-administrasjon |
|| Identitet | MFA for ansatte | MFA ikke aktivert for elever |
|| Applikasjon | WSUS-patching | Applikasjonsprogramvare patchet manuelt |
|| Data | Azure Backup | Backup-gjenoppretting ikke testet siste 6 måneder |

***Konklusjon:**God grunnleggende sikkerhet. Prioriterte forbedringstiltak: aktiver MFA for elever, implementer IDS,
*integrer elev-PC-er i Intune, og planlegg kvartalsvis DR-test.

---

## Study guide

### IT-løsninger med innebygd sikkerhet – kjerneinnhold

*## Security by Design:
SSikkerhet må bygges inn fra start – i kravspesifikasjon, design og utvikling – ikke legges til som et etterarbeid.
SMicrosofts SDL er referansemodellen med syv faser fra opplæring til respons.

*## Zero Trust:
UUtgangspunktet er at ingen – verken brukere, enheter eller nettverk – er automatisk betrodde.
UUDe tre prinsippene er: verifiser alltid (Verify explicitly), minste privilegium (Use least privilege) og anta brudd
U(Assume breach). MFA og Conditional Access er de viktigste praktiske tiltakene.

*## Patchhåndtering:
EEn strukturert prosess: identifiser → evaluer → test → rull ut → verifiser. Kritiske patcher bør installeres innen 72
Etimer. OWASP A06 understreker at utdaterte komponenter er en av de hyppigste angrepsvektorene.

*## Logging og SIEM:
LLogging er forutsetningen for å oppdage angrep. SIEM samler logger sentralt og korrelerer dem.
LOWASP A09 er manglende logging. Microsoft Sentinel er en skybasert SIEM med ML-drevet anomalideteksjon.

*## IAM og minste privilegium:
BBrukere får kun tilganger de faktisk trenger. RBAC kobler rettigheter til roller, ikke enkeltpersoner.
BActive Directory on-premises og Azure Entra ID i skyen er de primære verktøyene.

*## Backup og BCDR:
33-2-1-regelen er standarden. RTO definerer maks nedetid, RPO definerer maks datatap.
3Backup er verdiløs uten testet gjenoppretting. Isolasjon fra produksjonsnett er kritisk mot ransomware.

*## Defense in Depth:
SSikkerhet i lag – retningslinjer, fysisk, nettverk, maskin, identitet, applikasjon, data.
SIngen enkelt mekanisme er tilstrekkelig alene.

---

## FAQ

*## Hva er forskjellen mellom Security by Design og Privacy by Design?
SSecurity by Design handler om å integrere informasjonssikkerhet generelt i alle faser av systemutvikling.
SSPrivacy by Design (GDPR art. 25) handler spesifikt om å integrere personvernhensyn fra starten.
SDe overlapper mye, men Privacy by Design er et juridisk krav, mens Security by Design er en faglig best practice.

*## Hvorfor er VPN ikke lenger tilstrekkelig med Zero Trust?
TTradisjonell VPN gir full tilgang til bedriftsnettverket når du er tilkoblet. Zero Trust erstatter dette med betinget
TTtilgang: selv autentiserte brukere inne i nettverket må kontinuerlig verifiseres, og de får kun tilgang til de
Tspesifikke ressursene de trenger.

*## Hva er JIT og JEA?
JJIT (Just-In-Time) gir midlertidig, tidsavgrenset tilgang til sensitive systemer – kun når det er nødvendig.
JJJEA (Just-Enough-Access) sørger for at tilgangen er minimert til akkurat det som trengs.
JBegge reduserer angrepsflaten dersom en konto kompromitteres.

*## Hvorfor er det viktig å teste backup-gjenoppretting?
EEn backup som ikke kan gjenopprettes er verdiløs. Filer kan bli korrupte, backup-prosessen kan feile stille, eller
EEgjenopprettingsprosedyren kan vise seg å ta mye lengre tid enn RTO tillater. Jevnlig testing avslører disse problemene
Efør de blir kritiske.

*## Hva er forskjellen mellom RTO og RPO?
RRTO (Recovery Time Objective) er maks akseptabel nedetid – hvor lang tid det kan ta å gjenopprette systemet.
RRRPO (Recovery Point Objective) er maks akseptabelt datatap – hvor gammel den nyeste backupen kan være.
REt sykehus kan ha RTO = 4 timer og RPO = 1 time, mens en blogg kan akseptere RTO = 24 timer og RPO = 7 dager.

*## Hva menes med mikrosegmentering?
MMikrosegmentering deler nettverket inn i svært fine soner – gjerne ned på enkeltapplikasjon eller enkeltserver-nivå –
MMmed brannmurregler mellom. Dette begrenser lateral bevegelse drastisk: selv om en server er kompromittert, kan
Mangriperen ikke bevege seg fritt til andre systemer.

*## Hvordan henger SIEM og logging sammen med trusseldeteksjon?
LLogging alene gir deg rå data – du kan ikke manuelt lese gjennom millioner av logglinjer.
LLSIEM automatiserer analyse, korrelerer hendelser på tvers av systemer (f.eks. mislykket innlogging + ny bruker
Lopprettet + stor filnedlasting = alarm) og varsler om mønstre som indikerer angrep.

---

## Quiz

<details><summary>Spørsmål 1: Hva er de tre kjerneprinsippene i Zero Trust?</summary>

***Svar:**Verify explicitly (verifiser alltid), Use least privilege (minste privilegium), og Assume breach (anta brudd).
*Sammen betyr dette at ingen bruker, enhet eller nettverk automatisk stoler på – all tilgang verifiseres og begrenses.

</details>

<details><summary>Spørsmål 2: Hva er 3-2-1-regelen for backup?</summary>

***Svar:**3 kopier av dataene, på 2 forskjellige medier, med 1 offsite-kopi. Offsite-kopien sikrer at backup overlever
*lokale katastrofer som brann eller ransomware-angrep.

</details>

<details><summary>Spørsmål 3: Hva er forskjellen mellom RTO og RPO?</summary>

***Svar:**RTO (Recovery Time Objective) er maksimalt akseptabel nedetid – hvor lang tid gjenoppretting kan ta.
*RPO (Recovery Point Objective) er maksimalt akseptabelt datatap – hvor gammel siste backup kan være.

</details>

<details><summary>Spørsmål 4: Hvorfor er patchhåndtering viktig for sikkerhet?</summary>

***Svar:**Kjente sårbarheter i programvare er en av de vanligste angrepsvektorene. Patcher lukker disse sårbarhetene.
*Utdaterte komponenter (OWASP A06) er konsekvent blant de hyppigste årsaker til kompromitteringer.

</details>

<details><summary>Spørsmål 5: Hva er SIEM, og hvilken sårbarhet kobler OWASP til manglende logging?</summary>

***Svar:**SIEM (Security Information and Event Management) samler logger fra alle systemer sentralt, korrelerer hendelser
**og varsler om mistenkelig aktivitet. OWASP Top 10 A09 identifiserer manglende logging og overvåkning som en kritisk
*sårbarhet – uten logger oppdager du ikke angrep.

</details>

---

## Ressurser

- [Microsoft – Zero Trust (engelsk)](<https://learn.microsoft.com/en-us/security/zero-trust/zero-trust-overview>)
- [Microsoft – Azure sikkerhetsoversikt](<https://learn.microsoft.com/en-us/azure/security/fundamentals/overview>)
- [NSM Grunnprinsipper – Beskytt og oppretthold](<https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/>)
- [NDLA – Oppdatere Linux med APT](<https://ndla.no>)
- [NDLA – Brukerkontoer i Active Directory](<https://ndla.no>)
- [NSM – Grunnprinsipper for IKT-sikkerhet (full versjon)](<https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/>)
- [Digdir – Nulltillitsarkitektur (norsk)](<https://www.digdir.no/nasjonal-arkitektur/nulltillitsarkitektur/4054>)
- [YouTube: What is Zero Trust? (IBM Technology, 6 min)](<https://www.youtube.com/watch?v=R9NCYvR3h3w>)

## Kilder

[^1]: NSM – Grunnprinsipper for IKT-sikkerhet v2.1 (2024). <https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/>
[^2]: Microsoft – Security Development Lifecycle (SDL). <https://learn.microsoft.com/en-us/security/sdl/>
[^3]: Microsoft – Zero Trust-modellen. <https://learn.microsoft.com/en-us/security/zero-trust/zero-trust-overview>
[^4]: Digdir – Nulltillitsarkitektur (norsk veileder). <https://www.digdir.no/nasjonal-arkitektur/nulltillitsarkitektur/4054>
[^5]: OWASP Top 10:2021. <https://owasp.org/www-project-top-ten/>
[^6]: Microsoft – MFA blokkerer over 99 % av kontoovertak. <https://learn.microsoft.com/en-us/azure/active-directory/authentication/concept-mfa-how-it-works>
[^7]: Microsoft – Azure Defense in Depth. <https://learn.microsoft.com/en-us/azure/security/fundamentals/infrastructure>
