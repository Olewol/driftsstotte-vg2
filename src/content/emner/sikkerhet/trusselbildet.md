---
title: "Trusselbildet"
emne: sikkerhet
kompetansemaal:
  - km-07
kilder:
  - ndla
  - nsm
  - owasp
  - https://nsm.no/publikasjoner/risiko-2024
  - https://owasp.org/www-project-top-ten/
notebooklm: true
tags: []
flashcards: true
public: true
---

## Introduksjon

Trusselbildet innen digital sikkerhet endrer seg raskt. Det som var eksotiske angrepsmetoder for ti år siden, er i dag hverdagskost for norske virksomheter og enkeltpersoner. NSM (Nasjonal sikkerhetsmyndighet) publiserer hvert år en trusselrapport som viser at norske bedrifter, sykehus, kommuner og kritisk infrastruktur stadig er under press fra digitale angrep.

For å jobbe med IT-sikkerhet må du kjenne de vanligste truslene: hva de er, hvordan de virker, og hvilken påvirkning de har på samfunnet.

For å gå fra kunnskap om trusler til konkrete tiltak, er det nødvendig å gjennomføre en strukturert [[risikoanalyse]]. Trusselbildet gir deg råvarene – risikoanalysen hjelper deg å prioritere. [[it-losninger-med-sikkerhet]] viser hvilke tekniske og organisatoriske mottiltak som finnes.

---

## Teori

### Malware – ondsinnet programvare

Malware er en samlebetegnelse for programvare som er laget for å skade, forstyrre eller skaffe uautorisert tilgang til systemer.

**Virus**
Et virus kopierer seg selv ved å legge seg inn i andre filer. Det sprer seg når infiserte filer åpnes eller deles. Virus trenger brukerhandling for å spre seg.

**Orm (worm)**
En orm sprer seg automatisk over nettverk uten å trenge brukerhandling. Den utnytter sårbarheter i nettverksprotokollene. WannaCry (2017) var en orm som rammet over 200 000 systemer i 150 land på kort tid – inkludert britiske NHS-sykehus.

**Trojaner**
En trojaner later som den er nyttig programvare, men inneholder skjult ondsinnet kode. Eksempel: et gratis spill som i virkeligheten installerer spyware. Trojanere gir ofte angriperen bakdørstilgang.

**Ransomware**
Ransomware krypterer offerets filer og krever løsepenger for dekrypteringsnøkkelen. Dette er den dominerende trusselen mot norske virksomheter ifølge NSM. I 2021 rammet Conti-ransomware Østre Toten kommune og la ned all digital drift i uker. Helsesektoren, kommuner og industribedrifter er hyppige mål.

**Spyware**
Spyware overvåker brukerens aktivitet uten samtykke – tastaturlogging, skjermopptak, innsamling av passord og bankinformasjon. Kan inngå i kommersielle «stalkerware»-produkter brukt til overvåking av partnere.

**Rootkit**
Et rootkit skjuler sin egen tilstedeværelse og tilstedeværelsen av annen malware dypt i operativsystemet. Svært vanskelig å oppdage og fjerne. Krever ofte reinstallering av OS.

---

### Phishing og sosial manipulering

**Phishing** er forsøk på å lure brukere til å oppgi sensitiv informasjon (passord, kredittkortinfo) ved å utgi seg for å være en legitim aktør – bank, arbeidsgiver, Skatteetaten eller Posten.

- **Spear phishing:** Målrettet phishing mot én spesifikk person eller organisasjon, basert på innsamlet informasjon om offeret. Langt mer effektivt enn masseutsendelser.
- **Vishing:** Voice phishing – svindel via telefon. Angriperen utgir seg for å være IT-support, bank eller politi.
- **Smishing:** SMS-phishing. Typisk eksempel: «Din pakke er holdt tilbake, klikk her for å betale tollavgift.»
- **Pretexting:** Angriperen konstruerer en troverdig falsk bakgrunnshistorie for å manipulere offeret.

Den menneskelige faktoren er hyppigste angrepsvektor. De fleste vellykkede cyberangrep starter med sosial manipulering, ikke med teknisk hacking.

---

### DDoS – Tjenestenektangrep

**DDoS (Distributed Denial of Service)** oversvømmer en tjeneste med så mange forespørsler at den ikke klarer å betjene reelle brukere. Angrepet koordineres fra tusenvis av kompromitterte maskiner (et botnet).

NSM og NCSC varsler jevnlig om DDoS-angrep mot norsk kritisk infrastruktur, særlig i kjølvannet av geopolitiske hendelser. I 2022, etter Norges støtte til Ukraina, ble flere norske offentlige nettsider rammet av DDoS-angrep fra pro-russiske hackergrupper.

Konsekvenser: nettbanker utilgjengelige, offentlige portaler nede, kommunikasjonstjenester forstyrret.

---

### Zero-day-sårbarheter

En **zero-day** (nulldagssårbarhet) er en ukjent svakhet i programvare som leverandøren ennå ikke har oppdaget eller utbedret. Angriperen utnytter sårbarheten *før* en patch finnes – derav «null dager» til forsvar.

Zero-day-exploits er svært verdifulle og omsettes på kriminelle markeder. Statsstøttede aktører har ressurser til å kjøpe eller selv utvikle slike verktøy.

---

### Innsidetrusler

Ikke alle trusler kommer utenfra. **Innsidetrusler** kan være:

- **Utilsiktede:** En ansatt klikker på en phishing-lenke, bruker et svakt passord eller sender konfidensielle dokumenter til feil e-postadresse.
- **Tilsiktede:** En misfornøyd ansatt saboterer systemer, stjeler data for konkurrenter eller selger tilgang til kriminelle.

Tiltak: prinsippet om minste privilegium (least privilege), logging av brukeraktivitet, tilgangsstyring og bakgrunnssjekk av ansatte i sensitive roller.

---

### APT – Advanced Persistent Threats

**APT** er langvarige, sofistikerte angrep utført av ressurssterke aktører – typisk statsstøttede hackergrupper. Kjennetegn:

- Planlegges over måneder
- Bruker skreddersydde verktøy og zero-days
- Målet er spionasje, sabotasje eller destabilisering, ikke rask gevinst
- Angriperen kan oppholde seg skjult i et nettverk i årevis

NSM peker på statlige aktører knyttet til Russland, Kina og Nord-Korea som aktive trusler mot norske interesser. APT29 (Cozy Bear) og APT28 (Fancy Bear) er kjente russiske grupper som har angrepet norske mål.

Kontinuerlig overvåking og logganalyse er avgjørende for å oppdage APT-aktivitet. En angriper som har tilgang i årevis uten å bli oppdaget kan eksfiltrere enormt med data.

---

### OWASP Top 10 – Webapplikasjonssårbarheter

OWASP (Open Web Application Security Project) publiserer en liste over de ti vanligste sikkerhetsfeilene i webapplikasjoner. 2021-versjonen er gjeldende:

| Nr | Kategori |
|---|---|
| A01 | Broken Access Control – feil tilgangskontroll |
| A02 | Cryptographic Failures – svak eller manglende kryptering |
| A03 | Injection – SQL-injeksjon og lignende |
| A04 | Insecure Design – usikker systemarkitektur |
| A05 | Security Misconfiguration – feilkonfigurerte systemer |
| A06 | Vulnerable and Outdated Components – utdaterte biblioteker |
| A07 | Identification and Authentication Failures – svak autentisering |
| A08 | Software and Data Integrity Failures – mangelfull integritetssjekk |
| A09 | Security Logging and Monitoring Failures – manglende logging |
| A10 | Server-Side Request Forgery (SSRF) |

---

### Samfunnspåvirkning og demokrati

Digitale trusler stopper ikke ved bedriftene. De påvirker demokratiet og samfunnsdebatten:

**Desinformasjonskampanjer:** Statsstøttede aktører sprer falske nyheter via sosiale medier for å så tvil, polarisere befolkningen og svekke tilliten til institusjoner. Valgpåvirkning i USA (2016), Frankrike (2017) og påstått påvirkning av norsk opinion er dokumenterte eksempler.

**Angrep mot kritisk infrastruktur:** Kraft, vann, helse og kommunikasjon er avhengige av IT-systemer. Et vellykket angrep mot strømnettet eller sykehussystemer kan koste menneskeliv.

**Psykologisk krigføring:** Truende eller lammende cyberangrep kan brukes som pressmiddel i diplomatiske konflikter uten at en eneste soldat krysser en grense.

NSM understreker at digital sikkerhet er nasjonal sikkerhet. Derfor er IKT-kompetanse et samfunnsbehov, ikke bare et yrkesfag.

---

## Eksempel / lab

**Scenariobeskrivelse: Gjenkjenn phishing-e-poster**

Du mottar følgende e-poster. Vurder hvilke som er phishing og hvorfor:

1. *«Kjære kunde, kontoen din er midlertidig sperret. Klikk her for å bekrefte identiteten din: www.dnb-sikkerhet.net»*
   → Mistenkelig: domenet er ikke dnb.no. Hasteappell. Lenke til ukjent nettside.

2. *«Hei Kari, her er referat fra møtet i går. Se vedlagt PDF.»* – avsender er kollega@bedrift.no
   → Kan være legitimt, men: sjekk om vedlegget er forventet, og om avsenderadressen stemmer nøyaktig.

3. *«Du har vunnet en iPhone 15. Skriv inn kredittkortinfo for å betale frakt.»*
   → Klassisk svindel. Ingen legitim premie krever betaling for frakt med kredittkort på forhånd.

**Tiltak for phishing-forsvar:**
- Bruk av MFA (tofaktorautentisering) – selv om passordet stjeles, hindres innlogging
- E-postfilter med SPF, DKIM og DMARC
- Bevissthetstrening for ansatte

---

## Study guide

### Trusselbildet – kjerneinnhold

**Malware-typer og kjennetegn:**
Virus (trenger brukerhandling), orm (sprer seg selv over nettverk), trojaner (skjult ondsinnet kode i tilsynelatende nyttig programvare), ransomware (krypterer filer og krever løsepenger), spyware (overvåker stille), rootkit (gjemmer seg dypt i OS).

**Phishing og sosial manipulering:**
Phishing er den hyppigste angrepsvektoren – de fleste vellykkede angrep starter her. Variantene er spear phishing (målrettet), vishing (telefon), smishing (SMS) og pretexting (falsk bakgrunnshistorie). Forsvar: MFA, e-postfilter, opplæring.

**DDoS:**
Oversvømmelse med trafikk fra et botnet. Rammer tilgjengelighet, ikke konfidensialitet. Typisk brukt som geopolitisk pressmiddel eller mot nettbanker. Motmiddel: CDN, rate limiting, scrubbing-sentre.

**Zero-day:**
Ukjent sårbarhet uten tilgjengelig patch. Svært verdifull for angripere. Eneste forsvar er Defence in Depth – begrens skaden selv om ett lag svikter.

**APT:**
Langsiktige statsstøttede angrep. Kjennetegn: skreddersydde verktøy, skjuler seg i årevis, mål er spionasje/sabotasje. Oppdages med god logging og SIEM.

**OWASP Top 10:**
De vanligste sårbarhetene i webapplikasjoner: brutt tilgangskontroll (A01), kryptografifeil (A02), injeksjon (A03) og manglende logging (A09) er de viktigste å kjenne.

**Samfunnsperspektivet:**
Digital sikkerhet = nasjonal sikkerhet. Desinformasjon, angrep på kritisk infrastruktur og psykologisk krigføring er reelle trusler mot demokrati og samfunnsfunksjoner.

---

## FAQ

**Hva er forskjellen mellom ransomware og et vanlig virus?**
Et virus kopierer seg selv og kan skade filer eller systemer, men det primære formålet er spredning. Ransomware er optimalisert for å tjene penger: det krypterer offerets data og krever betaling for dekrypteringsnøkkelen. Ransomware er i dag den mest lønnsomme formen for cyberkriminalitet.

**Hvorfor er phishing så effektivt?**
Phishing utnytter menneskelig psykologi – tillit til kjente avsendere, hasteappell («kontoen din stenges om 24 timer»), nysgjerrighet og frykt. Teknisk sikkerhet er sterk nok til at det er lettere å lure et menneske enn å hacke et system. Spear phishing er spesielt effektivt fordi det er skreddersydd med ekte informasjon om offeret.

**Kan man beskytte seg mot zero-day-angrep?**
Ikke direkte – det finnes ingen patch mot ukjente sårbarheter. Forsvar bygger på Defence in Depth: segmentering begrenser spredningen, logging oppdager unormal aktivitet, og rask respons begrenser skaden. Regelmessig patching reduserer antall kjente sårbarheter og gjør zero-days vanskeligere å kombinere.

**Hva er et botnet?**
Et botnet er et nettverk av kompromitterte maskiner («bots» eller «zombier») kontrollert av en angriper uten at eierne vet om det. Botnets brukes til DDoS-angrep, spam-utsendelse og kryptomining. Maskiner kan bli del av et botnet via malware lastet ned fra usikre nettsider eller e-postvedlegg.

**Hva er forskjellen mellom APT og «vanlig» hacking?**
Vanlig hacking er gjerne opportunistisk – angriperen ser etter lett tilgjengelige mål. APT er målrettet, planlegges over tid og gjennomføres av ressurssterke aktører (typisk statsstøttede). APT-aktøren er tålmodig, skjuler seg og har et langsiktig strategisk mål – ikke bare rask gevinst.

**Hva betyr Broken Access Control (OWASP A01)?**
Det betyr at applikasjonen ikke håndhever tilgangskontroll korrekt – brukere kan gjøre ting de ikke burde ha tilgang til. Eksempel: en vanlig bruker kan redigere URL-en og få tilgang til en annen brukers data. Det er konsekvent rangert som den vanligste webapplikasjonssårbarheten.

**Hvordan kan desinformasjon true demokratiet?**
Statsstøttede aktører kan bruke sosiale medier til å spre falske nyheter systematisk, forsterke polarisering og svekke tillit til medier, politikere og institusjoner. Når borgere ikke kan skille mellom fakta og løgn, svekkes grunnlaget for informerte valg. Cambridge Analytica-skandalen viste at persondata kombinert med målrettet desinformasjon kan påvirke valgresultater.

---

## Quiz

<details><summary>Spørsmål 1: Hva skiller en orm fra et virus?</summary>

**Svar:** En orm sprer seg automatisk over nettverk uten brukerhandling, mens et virus trenger at en infisert fil åpnes eller deles for å spre seg.

</details>

<details><summary>Spørsmål 2: Hva er spear phishing?</summary>

**Svar:** Spear phishing er målrettet phishing mot én spesifikk person eller organisasjon, basert på innsamlet informasjon om offeret. Det er langt mer effektivt enn generelle masseutsendelser.

</details>

<details><summary>Spørsmål 3: Hva menes med en zero-day-sårbarhet?</summary>

**Svar:** En zero-day er en ukjent svakhet i programvare som leverandøren ennå ikke har oppdaget eller laget en oppdatering for. Angriperen kan utnytte sårbarheten uten at forsvareren har mulighet til å patche.

</details>

<details><summary>Spørsmål 4: Hva er APT, og hvem står typisk bak?</summary>

**Svar:** APT (Advanced Persistent Threat) er langvarige, sofistikerte angrep utført av ressurssterke aktører – typisk statsstøttede hackergrupper. De bruker avanserte verktøy og kan oppholde seg skjult i et nettverk i måneder eller år.

</details>

<details><summary>Spørsmål 5: Hvordan kan desinformasjonskampanjer true demokratiet?</summary>

**Svar:** Statsstøttede aktører kan spre falske nyheter via sosiale medier for å polarisere befolkningen, svekke tilliten til demokratiske institusjoner og påvirke valg. Dette er en form for digital krigføring som ikke krever tradisjonelle militære midler.

</details>

---

## Flashcards

Malware :: Samlebetegnelse for ondsinnet programvare som virus, ormer, trojaner, ransomware, spyware og rootkit
Ransomware :: Malware som krypterer filer og krever løsepenger. Dominerende trussel mot norske virksomheter (NSM)
Phishing :: Forsøk på å lure brukere til å oppgi sensitiv informasjon ved å utgi seg for en legitim aktør
Spear phishing :: Målrettet phishing mot én spesifikk person eller organisasjon, basert på innsamlet informasjon
DDoS :: Distributed Denial of Service – oversvømmer en tjeneste med trafikk fra et botnet for å gjøre den utilgjengelig
Zero-day :: Ukjent sårbarhet i programvare som utnyttes før leverandøren har utviklet en patch
APT :: Advanced Persistent Threat – langsiktige, sofistikerte angrep fra ressurssterke (ofte statsstøttede) aktører
Botnet :: Nettverk av kompromitterte maskiner kontrollert av en angriper, brukes bl.a. til DDoS
Innsidetrussel :: Trussel fra ansatte eller andre med intern tilgang, enten utilsiktet (feil) eller tilsiktet (sabotasje)
OWASP Top 10 :: Liste over de ti vanligste sikkerhetsfeilene i webapplikasjoner, utgitt av OWASP
Pretexting :: Sosial manipulering der angriperen konstruerer en troverdig falsk bakgrunnshistorie for å lure offeret
Smishing :: SMS-phishing – svindelforsøk via tekstmelding som utgir seg for å være bank, pakkeleverandør e.l.

---

## Ressurser

- [NSM – Digital sikkerhet](https://nsm.no/fagomrader/digital-sikkerhet/)
- [NCSC – Norsk varslingssenter for digital infrastruktur](https://nsm.no/ncsc)
- [OWASP Top 10:2021](https://owasp.org/Top10/)
- [NDLA – Informasjonssikkerhet](https://ndla.no)
- [NSM – Risikovurdering 2024 (årsrapport)](https://nsm.no/publikasjoner/risiko-2024)
- [OWASP – Top 10 prosjektside (full dokumentasjon)](https://owasp.org/www-project-top-ten/)
