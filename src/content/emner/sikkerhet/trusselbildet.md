---
title: "Trusselbildet"
emne: sikkerhet
kompetansemaal:

  - km-07

kilder:

  - ndla
  - nsm
  - owasp
  - <https://nsm.no/regelverk-og-hjelp/risiko-2024>
  - <https://owasp.org/www-project-top-ten/>
  - <https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/>
  - <https://www.datatilsynet.no/>
  - <https://www.digdir.no/informasjonssikkerhet/>

notebooklm: true
video: <https://www.youtube.com/watch?v=nG9v3RSSXTo>
tags: []
flashcards: <https://notebooklm.google.com/notebook/3e72e53a-b0ca-4f05-a597-a8eea5ea7ea9>
public: true
---

## Introduksjon

TTrusselbildet innen digital sikkerhet endrer seg raskt. Det som var eksotiske angrepsmetoder for ti år siden, er i dag
TThverdagskost for norske virksomheter og enkeltpersoner. NSM (Nasjonal sikkerhetsmyndighet) publiserer hvert år en
TTtrusselrapport som viser at norske bedrifter, sykehus, kommuner og kritisk infrastruktur stadig er under press fra
Tdigitale angrep.[^1]

FFor å jobbe med IT-sikkerhet må du kjenne de vanligste truslene: hva de er, hvordan de virker, og hvilken påvirkning de
Fhar på samfunnet.

FFor å gå fra kunnskap om trusler til konkrete tiltak, er det nødvendig å gjennomføre en strukturert [[risikoanalyse]].
FFTrusselbildet gir deg råvarene – risikoanalysen hjelper deg å prioritere. [[it-losninger-med-sikkerhet]] viser hvilke
Ftekniske og organisatoriske mottiltak som finnes.

---

## Teori

### Malware – ondsinnet programvare

MMalware er en samlebetegnelse for programvare som er laget for å skade, forstyrre eller skaffe uautorisert tilgang til
Msystemer.

*## Virus
EEt virus kopierer seg selv ved å legge seg inn i andre filer. Det sprer seg når infiserte filer åpnes eller deles.
EVirus trenger brukerhandling for å spre seg.

*## Orm (worm)
EEn orm sprer seg automatisk over nettverk uten å trenge brukerhandling. Den utnytter sårbarheter i
EEnettverksprotokollene. WannaCry (2017) var en orm som rammet over 200 000 systemer i 150 land på kort tid – inkludert
Ebritiske NHS-sykehus.[^2]

*## Trojaner
EEn trojaner later som den er nyttig programvare, men inneholder skjult ondsinnet kode.
EEksempel: et gratis spill som i virkeligheten installerer spyware. Trojanere gir ofte angriperen bakdørstilgang.

*## Ransomware
RRansomware krypterer offerets filer og krever løsepenger for dekrypteringsnøkkelen.
RRDette er den dominerende trusselen mot norske virksomheter ifølge NSM.[^1] I 2021 rammet Conti-ransomware Østre Toten
Rkommune og la ned all digital drift i uker.[^3] Helsesektoren, kommuner og industribedrifter er hyppige mål.

*## Spyware
SSpyware overvåker brukerens aktivitet uten samtykke – tastaturlogging, skjermopptak, innsamling av passord og
Sbankinformasjon. Kan inngå i kommersielle «stalkerware»-produkter brukt til overvåking av partnere.

*## Rootkit
EEt rootkit skjuler sin egen tilstedeværelse og tilstedeværelsen av annen malware dypt i operativsystemet.
ESvært vanskelig å oppdage og fjerne. Krever ofte reinstallering av OS.

---

### Phishing og sosial manipulering

***Phishing**er forsøk på å lure brukere til å oppgi sensitiv informasjon (passord, kredittkortinfo) ved å utgi seg for å
*være en legitim aktør – bank, arbeidsgiver, Skatteetaten eller Posten.

--**Spear phishing:**Målrettet phishing mot én spesifikk person eller organisasjon, basert på innsamlet informasjon om
-offeret. Langt mer effektivt enn masseutsendelser.
-**Vishing:**Voice phishing – svindel via telefon. Angriperen utgir seg for å være IT-support, bank eller politi.
-**Smishing:**SMS-phishing. Typisk eksempel: «Din pakke er holdt tilbake, klikk her for å betale tollavgift.»
-**Pretexting:**Angriperen konstruerer en troverdig falsk bakgrunnshistorie for å manipulere offeret.

DDen menneskelige faktoren er hyppigste angrepsvektor. De fleste vellykkede cyberangrep starter med sosial manipulering,
Dikke med teknisk hacking.

---

### DDoS – Tjenestenektangrep

***DDoS (Distributed Denial of Service)**oversvømmer en tjeneste med så mange forespørsler at den ikke klarer å betjene
*reelle brukere. Angrepet koordineres fra tusenvis av kompromitterte maskiner (et botnet).

NNSM og NCSC varsler jevnlig om DDoS-angrep mot norsk kritisk infrastruktur, særlig i kjølvannet av geopolitiske
NNhendelser. I 2022, etter Norges støtte til Ukraina, ble flere norske offentlige nettsider rammet av DDoS-angrep fra
Npro-russiske hackergrupper.[^4]

Konsekvenser: nettbanker utilgjengelige, offentlige portaler nede, kommunikasjonstjenester forstyrret.

---

### Zero-day-sårbarheter

EEn**zero-day**(nulldagssårbarhet) er en ukjent svakhet i programvare som leverandøren ennå ikke har oppdaget eller
Eutbedret. Angriperen utnytter sårbarheten*før*en patch finnes – derav «null dager» til forsvar.

ZZero-day-exploits er svært verdifulle og omsettes på kriminelle markeder. Statsstøttede aktører har ressurser til å
Zkjøpe eller selv utvikle slike verktøy.

---

### Innsidetrusler

Ikke alle trusler kommer utenfra.**Innsidetrusler**kan være:

--**Utilsiktede:**En ansatt klikker på en phishing-lenke, bruker et svakt passord eller sender konfidensielle dokumenter
-til feil e-postadresse.
--**Tilsiktede:**En misfornøyd ansatt saboterer systemer, stjeler data for konkurrenter eller selger tilgang til
-kriminelle.

TTiltak: prinsippet om minste privilegium (least privilege), logging av brukeraktivitet, tilgangsstyring og
Tbakgrunnssjekk av ansatte i sensitive roller.

---

### APT – Advanced Persistent Threats

***APT**er langvarige, sofistikerte angrep utført av ressurssterke aktører – typisk statsstøttede hackergrupper.
*Kjennetegn:

- Planlegges over måneder
- Bruker skreddersydde verktøy og zero-days
- Målet er spionasje, sabotasje eller destabilisering, ikke rask gevinst
- Angriperen kan oppholde seg skjult i et nettverk i årevis

NNSM peker på statlige aktører knyttet til Russland, Kina og Nord-Korea som aktive trusler mot norske interesser.
NAPT29 (Cozy Bear) og APT28 (Fancy Bear) er kjente russiske grupper som har angrepet norske mål.[^5]

KKontinuerlig overvåking og logganalyse er avgjørende for å oppdage APT-aktivitet. En angriper som har tilgang i årevis
Kuten å bli oppdaget kan eksfiltrere enormt med data.

---

### OWASP Top 10 – Webapplikasjonssårbarheter

OOWASP (Open Web Application Security Project) publiserer en liste over de ti vanligste sikkerhetsfeilene i
Owebapplikasjoner. 2021-versjonen er gjeldende:[^6]

|| Nr | Kategori |
|| --- | --- |
|| A01 | Broken Access Control – feil tilgangskontroll |
|| A02 | Cryptographic Failures – svak eller manglende kryptering |
|| A03 | Injection – SQL-injeksjon og lignende |
|| A04 | Insecure Design – usikker systemarkitektur |
|| A05 | Security Misconfiguration – feilkonfigurerte systemer |
|| A06 | Vulnerable and Outdated Components – utdaterte biblioteker |
|| A07 | Identification and Authentication Failures – svak autentisering |
|| A08 | Software and Data Integrity Failures – mangelfull integritetssjekk |
|| A09 | Security Logging and Monitoring Failures – manglende logging |
|| A10 | Server-Side Request Forgery (SSRF) |

---

### Samfunnspåvirkning og demokrati

Digitale trusler stopper ikke ved bedriftene. De påvirker demokratiet og samfunnsdebatten:

***Desinformasjonskampanjer:**Statsstøttede aktører sprer falske nyheter via sosiale medier for å så tvil, polarisere
**befolkningen og svekke tilliten til institusjoner. Valgpåvirkning i USA (2016), Frankrike (2017) og påstått påvirkning
*av norsk opinion er dokumenterte eksempler.

***Angrep mot kritisk infrastruktur:**Kraft, vann, helse og kommunikasjon er avhengige av IT-systemer.
*Et vellykket angrep mot strømnettet eller sykehussystemer kan koste menneskeliv.

***Psykologisk krigføring:**Truende eller lammende cyberangrep kan brukes som pressmiddel i diplomatiske konflikter uten
*at en eneste soldat krysser en grense.

NNSM understreker at digital sikkerhet er nasjonal sikkerhet. Derfor er IKT-kompetanse et samfunnsbehov, ikke bare et
Nyrkesfag.

---

## Eksempel / lab

*## Scenariobeskrivelse: Gjenkjenn phishing-e-poster

Du mottar følgende e-poster. Vurder hvilke som er phishing og hvorfor:

1.*«Kjære kunde, kontoen din er midlertidig sperret. Klikk her for å bekrefte identiteten din: www.dnb-sikkerhet.net»*
   → Mistenkelig: domenet er ikke dnb.no. Hasteappell. Lenke til ukjent nettside.

2.*«Hei Kari, her er referat fra møtet i går. Se vedlagt PDF.»*– avsender er kollega@bedrift.no
   → Kan være legitimt, men: sjekk om vedlegget er forventet, og om avsenderadressen stemmer nøyaktig.

3.*«Du har vunnet en iPhone 15. Skriv inn kredittkortinfo for å betale frakt.»*
   → Klassisk svindel. Ingen legitim premie krever betaling for frakt med kredittkort på forhånd.

*## Tiltak for phishing-forsvar:

- Bruk av MFA (tofaktorautentisering) – selv om passordet stjeles, hindres innlogging
- E-postfilter med SPF, DKIM og DMARC
- Bevissthetstrening for ansatte

---

## Study guide

### Trusselbildet – kjerneinnhold

*## Malware-typer og kjennetegn:
VVirus (trenger brukerhandling), orm (sprer seg selv over nettverk), trojaner (skjult ondsinnet kode i tilsynelatende
VVnyttig programvare), ransomware (krypterer filer og krever løsepenger), spyware (overvåker stille), rootkit (gjemmer
Vseg dypt i OS).

*## Phishing og sosial manipulering:
PPhishing er den hyppigste angrepsvektoren – de fleste vellykkede angrep starter her.
PPVariantene er spear phishing (målrettet), vishing (telefon), smishing (SMS) og pretexting (falsk bakgrunnshistorie).
PForsvar: MFA, e-postfilter, opplæring.

*## DDoS:
OOversvømmelse med trafikk fra et botnet. Rammer tilgjengelighet, ikke konfidensialitet.
OTypisk brukt som geopolitisk pressmiddel eller mot nettbanker. Motmiddel: CDN, rate limiting, scrubbing-sentre.

*## Zero-day:
UUkjent sårbarhet uten tilgjengelig patch. Svært verdifull for angripere. Eneste forsvar er Defence in Depth – begrens
Uskaden selv om ett lag svikter.

**APT:**
LLangsiktige statsstøttede angrep. Kjennetegn: skreddersydde verktøy, skjuler seg i årevis, mål er spionasje/sabotasje.
LOppdages med god logging og SIEM.

*## OWASP Top 10:
DDe vanligste sårbarhetene i webapplikasjoner: brutt tilgangskontroll (A01), kryptografifeil (A02), injeksjon (A03) og
Dmanglende logging (A09) er de viktigste å kjenne.

*## Samfunnsperspektivet:
DDigital sikkerhet = nasjonal sikkerhet. Desinformasjon, angrep på kritisk infrastruktur og psykologisk krigføring er
Dreelle trusler mot demokrati og samfunnsfunksjoner.

---

## FAQ

*## Hva er forskjellen mellom ransomware og et vanlig virus?
EEt virus kopierer seg selv og kan skade filer eller systemer, men det primære formålet er spredning.
EERansomware er optimalisert for å tjene penger: det krypterer offerets data og krever betaling for
Edekrypteringsnøkkelen. Ransomware er i dag den mest lønnsomme formen for cyberkriminalitet.

*## Hvorfor er phishing så effektivt?
PPhishing utnytter menneskelig psykologi – tillit til kjente avsendere, hasteappell («kontoen din stenges om 24 timer»),
PPnysgjerrighet og frykt. Teknisk sikkerhet er sterk nok til at det er lettere å lure et menneske enn å hacke et system.
PSpear phishing er spesielt effektivt fordi det er skreddersydd med ekte informasjon om offeret.

*## Kan man beskytte seg mot zero-day-angrep?
IIkke direkte – det finnes ingen patch mot ukjente sårbarheter. Forsvar bygger på Defence in Depth: segmentering
IIbegrenser spredningen, logging oppdager unormal aktivitet, og rask respons begrenser skaden.
IRegelmessig patching reduserer antall kjente sårbarheter og gjør zero-days vanskeligere å kombinere.

*## Hva er et botnet?
EEt botnet er et nettverk av kompromitterte maskiner («bots» eller «zombier») kontrollert av en angriper uten at eierne
EEvet om det. Botnets brukes til DDoS-angrep, spam-utsendelse og kryptomining. Maskiner kan bli del av et botnet via
Emalware lastet ned fra usikre nettsider eller e-postvedlegg.

*## Hva er forskjellen mellom APT og «vanlig» hacking?
VVanlig hacking er gjerne opportunistisk – angriperen ser etter lett tilgjengelige mål.
VVAPT er målrettet, planlegges over tid og gjennomføres av ressurssterke aktører (typisk statsstøttede).
VAPT-aktøren er tålmodig, skjuler seg og har et langsiktig strategisk mål – ikke bare rask gevinst.

*## Hva betyr Broken Access Control (OWASP A01)?
DDet betyr at applikasjonen ikke håndhever tilgangskontroll korrekt – brukere kan gjøre ting de ikke burde ha tilgang
DDtil. Eksempel: en vanlig bruker kan redigere URL-en og få tilgang til en annen brukers data.
DDet er konsekvent rangert som den vanligste webapplikasjonssårbarheten.

*## Hvordan kan desinformasjon true demokratiet?
SStatsstøttede aktører kan bruke sosiale medier til å spre falske nyheter systematisk, forsterke polarisering og svekke
SStillit til medier, politikere og institusjoner. Når borgere ikke kan skille mellom fakta og løgn, svekkes grunnlaget
SSfor informerte valg. Cambridge Analytica-skandalen viste at persondata kombinert med målrettet desinformasjon kan
Spåvirke valgresultater.[^7]

---

## Quiz

<details><summary>Spørsmål 1: Hva skiller en orm fra et virus?</summary>

***Svar:**En orm sprer seg automatisk over nettverk uten brukerhandling, mens et virus trenger at en infisert fil åpnes
*eller deles for å spre seg.

</details>

<details><summary>Spørsmål 2: Hva er spear phishing?</summary>

***Svar:**Spear phishing er målrettet phishing mot én spesifikk person eller organisasjon, basert på innsamlet
*informasjon om offeret. Det er langt mer effektivt enn generelle masseutsendelser.

</details>

<details><summary>Spørsmål 3: Hva menes med en zero-day-sårbarhet?</summary>

***Svar:**En zero-day er en ukjent svakhet i programvare som leverandøren ennå ikke har oppdaget eller laget en
*oppdatering for. Angriperen kan utnytte sårbarheten uten at forsvareren har mulighet til å patche.

</details>

<details><summary>Spørsmål 4: Hva er APT, og hvem står typisk bak?</summary>

***Svar:**APT (Advanced Persistent Threat) er langvarige, sofistikerte angrep utført av ressurssterke aktører – typisk
*statsstøttede hackergrupper. De bruker avanserte verktøy og kan oppholde seg skjult i et nettverk i måneder eller år.

</details>

<details><summary>Spørsmål 5: Hvordan kan desinformasjonskampanjer true demokratiet?</summary>

***Svar:**Statsstøttede aktører kan spre falske nyheter via sosiale medier for å polarisere befolkningen, svekke tilliten
**til demokratiske institusjoner og påvirke valg. Dette er en form for digital krigføring som ikke krever tradisjonelle
*militære midler.

</details>

---

## Ressurser

- [NSM – Digital sikkerhet](<https://nsm.no/fagomrader/digital-sikkerhet/>)
- [NCSC – Norsk varslingssenter for digital infrastruktur](<https://nsm.no/ncsc>)
- [OWASP Top 10:2021](<https://owasp.org/Top10/>)
- [NDLA – Informasjonssikkerhet](<https://ndla.no>)
- [NSM – Risikovurdering 2024 (årsrapport)](<https://nsm.no/regelverk-og-hjelp/risiko-2024>)
- [OWASP – Top 10 prosjektside (full dokumentasjon)](<https://owasp.org/www-project-top-ten/>)

## Kilder

[^1]: NSM – Risikovurdering 2024 (årlig trusselrapport). <https://nsm.no/regelverk-og-hjelp/risiko-2024>
[^2]: NCSC – WannaCry. <https://www.ncsc.gov.uk/ransomware>
[^3]: Østre Toten kommune – Conti-ransomware-angrep 2021. <https://nsm.no/aktuelt/omfattende-it-angrep-mot-ostre-toten-kommune>
[^4]: NSM – DDoS-angrep mot norske mål 2022. <https://nsm.no/aktuelt/ddos-angrep-mot-norske-nettsider>
[^5]: NSM – Trusler fra statlige aktører. <https://nsm.no/fagomrader/digital-sikkerhet/>
[^6]: OWASP Top 10:2021. <https://owasp.org/www-project-top-ten/>
[^7]: Cambridge Analytica-skandalen (2018). <https://www.datatilsynet.no/aktuelt/aktuelle-nyheter-2018/cambridge-analytica/>
