---
title: "Personvern og GDPR"
emne: sikkerhet
kompetansemaal:

  - km-11

kilder:

  - ndla
  - datatilsynet
  - <https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/>
  - <https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/>
  - <https://www.datatilsynet.no/>
  - <https://owasp.org/www-project-top-ten/>
  - <https://www.digdir.no/informasjonssikkerhet/>

video: <https://www.youtube.com/watch?v=u6p_G7w89Uo>
notebooklm: true
tags: []
flashcards: <https://notebooklm.google.com/notebook/3e72e53a-b0ca-4f05-a597-a8eea5ea7ea9>
public: true
---

## Introduksjon

PPersonvern handler om enkeltmenneskets rett til å kontrollere informasjon om seg selv.
PPI vår digitale hverdag – der apper, tjenester og virksomheter samler inn enorme mengder data om oss – er personvern
Pbåde en grunnleggende rettighet og et juridisk krav.

II EU og Norge reguleres personvern av**GDPR**(General Data Protection Regulation), en EU-forordning som trådte i kraft i
IImai 2018.[^1] GDPR gjelder i Norge gjennom EØS-avtalen og er gjennomført i norsk rett via**personopplysningsloven**.
IIFor deg som jobber i IT-drift er personvern ikke noe juridisk avdeling håndterer alene – tekniske valg som
Idatabasestruktur, tilgangskontroll, logging og backup har direkte personvernkonsekvenser.

SSom IT-drifter vil du møte personvern i sammenheng med [[kryptering]] (GDPR krever kryptering av personopplysninger),
SS[[bruker-og-tilgangsstyring]] (hvem har tilgang til persondata?) og [[risikoanalyse]] (GDPR art.
S32 krever risikovurdering som grunnlag for sikkerhetstiltak). Personvern er ikke isolert juss – det er teknisk praksis.

---

## Teori

### De 7 personvernprinsippene (GDPR art. 5)

GGDPR artikkel 5 fastsetter syv grunnleggende prinsipper for behandling av personopplysninger.[^2] Alle virksomheter som
Gbehandler personopplysninger er forpliktet til å følge disse:

|| Nr | Prinsipp | Kort forklaring |
|| --- | --- | --- |
|| 1 | **Lovlighet, rettferdighet og åpenhet** | Behandlingen må ha et rettslig grunnlag og være åpen overfor de registrerte |
|| 2 | **Formålsbegrensning** | Data samles inn til et bestemt formål og kan ikke brukes til noe annet uten nytt grunnlag |
|| 3 | **Dataminimering** | Kun de opplysningene som er nødvendige for formålet skal samles inn |
|| 4 | **Riktighet** | Personopplysninger skal være korrekte og holdes oppdaterte |
|| 5 | **Lagringsbegrensning** | Data skal slettes når de ikke lenger er nødvendige for formålet |
|| 6 | **Integritet og konfidensialitet** | Egnede tekniske og organisatoriske tiltak skal sikre data mot uautorisert tilgang og tap |
|| 7 | **Ansvarlighet** | Virksomheten må kunne dokumentere at den overholder alle prinsippene |

---

### Behandlingsgrunnlag (GDPR art. 6)

FFor å behandle personopplysninger lovlig trenger man alltid et**behandlingsgrunnlag**. GDPR art.
F6 lister seks gyldige grunnlag:

1.**Samtykke**– Den registrerte har gitt eksplisitt, informert samtykke. Kan trekkes tilbake når som helst.
2.**Avtale**– Behandlingen er nødvendig for å oppfylle en avtale med den registrerte
3.**Rettslig plikt**– Virksomheten er lovpålagt å behandle opplysningene (f.eks. skatteregistre)
4.**Vitale interesser**– Nødvendig for å beskytte den registrertes liv
5.**Allmenn interesse**– Nødvendig for å utføre en oppgave i allmennhetens interesse
6.**Berettiget interesse**– Virksomhetens interesse veier tyngre enn den registrertes personverninteresse

FFor sensitive personopplysninger (helseopplysninger, politisk overbevisning, etnisk opprinnelse m.fl.) gjelder strengere
Fregler (GDPR art. 9).

---

### Registrertes rettigheter

GDPR gir enkeltpersoner en rekke rettigheter som virksomheter er forpliktet til å oppfylle:

|| Rettighet | Forklaring |
|| --- | --- |
|| **Innsyn (art. 15)** | Rett til å vite hvilke opplysninger som behandles om deg |
|| **Retting (art. 16)** | Rett til å korrigere uriktige opplysninger |
|| **Sletting (art. 17)** | «Rett til å bli glemt» – sletting av opplysninger når de ikke lenger er nødvendige |
|| **Portabilitet (art. 20)** | Rett til å motta egne data i et maskinlesbart format og overføre dem til annen leverandør |
|| **Innsigelse (art. 21)** | Rett til å protestere mot behandling basert på berettiget interesse |
|| **Begrensning (art. 18)** | Rett til å kreve at behandlingen begrenses i visse situasjoner |

---

### Innebygd personvern – Privacy by Design

***Privacy by Design**(innebygd personvern) er prinsippet om at personvern skal integreres i systemdesign fra starten av,
*ikke legges til etterpå. Dette er lovfestet i GDPR art. 25.[^3]

Praktiske eksempler:

- Kryptere all datalagring fra dag én – ikke som en ettertanke
- Kun samle inn nødvendige felter i registreringsskjemaer (dataminimering)
- Implementere tilgangskontroll slik at kun autoriserte brukere ser sensitive data
- Automatisk slette data etter en fastsatt periode (lagringsbegrensning)
- Pseudonymisering: erstatte direkte identifikatorer med pseudonymer i testdatabaser

PPrivacy by Design er søsterprinsippet til Security by Design – begge handler om at sikkerhet (og personvern) er et
Pdesignkrav, ikke en ettertanke. Se [[it-losninger-med-sikkerhet]] for Security by Design i bredere kontekst.

---

### Behandlingsansvarlig og databehandler

En nøkkel distinksjon i GDPR er rollene i behandlingskjeden:

--**Behandlingsansvarlig:**Den virksomheten eller personen som bestemmer formålet med behandlingen av personopplysninger
-og hvilke verktøy som skal brukes. Det er behandlingsansvarlig som har det overordnede juridiske ansvaret.
--**Databehandler:**En ekstern part (f.eks. en skytjeneste) som behandler personopplysninger på vegne av den
-behandlingsansvarlige.

DDenne distinksjonen er avgjørende for hvem som har ansvar hvis noe går galt, og den styrer hvilke avtaler som kreves
Dmellom partene.

---

### Personvernombud (DPO)

Noen virksomheter er pålagt å ha et**personvernombud (Data Protection Officer – DPO)**.[^5] Dette gjelder:

- Offentlige organer (alle norske kommuner, etater osv.)
- Virksomheter som driver systematisk overvåking av enkeltpersoner i stor skala
- Virksomheter som behandler sensitive personopplysninger i stor skala

DPO-en fungerer som intern ekspert og kontaktpunkt for Datatilsynet.

---

### Databehandleravtale (GDPR art. 28)

NNår en virksomhet bruker en tredjepart til å behandle personopplysninger på vegne av seg (f.eks.
NNen skyløsning, et lønningssystem, en e-posttjeneste), kreves det en**databehandleravtale**(GDPR art.
N28).[^4] Avtalen regulerer hva behandleren kan gjøre med dataene, og sikrer at de kun brukes til angitt formål.

EEksempel: En norsk skole bruker Microsoft 365. Skolen er da**behandlingsansvarlig**, Microsoft er**databehandler**, og
Edet må foreligge en databehandleravtale.

EEn viktig praktisk oppgave for IT-ansvarlige er å ha oversikt over alle underleverandører og skytjenester som behandler
Epersonopplysninger på vegne av virksomheten, og sikre at gyldige databehandleravtaler er på plass for alle.

---

### Brudd på personvern og varslingsplikten

HHvis personopplysninger kompromitteres (uautorisert tilgang, tap av data, feil utsendelse) foreligger det
Het**personvernbrudd (data breach)**.

**GDPR art. 33 – 72-timers-regelen:**[^6]
BBrudd med risiko for de registrerte skal varsles til Datatilsynet innen**72 timer**etter at virksomheten oppdaget
Bbruddet. Varselet skal inneholde:

- Beskrivelse av bruddet (hva skjedde)
- Kategorier og omtrentlig antall berørte
- Mulige konsekvenser
- Tiltak som er iverksatt

***GDPR art. 34:**Brudd med høy risiko for de registrerte skal også varsles direkte til de berørte personene uten
*ubegrunnet opphold.

AAvvikshåndtering – de rutinene som håndterer oppdagelse, stopp og rapportering av brudd – er et krav GDPR stiller til
Aalle virksomheter. IT-driftere er ofte de første som oppdager et brudd.

---

### Datatilsynet og sanksjoner

**Datatilsynet**er den norske tilsynsmyndigheten for personvern.[^7] Datatilsynet:

- Håndhever GDPR og personopplysningsloven
- Veileder virksomheter og enkeltpersoner
- Kan ilegge administrative gebyrer

*## Sanksjoner etter GDPR:

- Inntil**10 millioner euro**eller 2 % av global årsomsetning for tekniske brudd (art. 83.4)
- Inntil**20 millioner euro**eller 4 % av global årsomsetning for grunnleggende brudd (art. 83.5)

**Eksempel: Meta ble i 2023 ilagt en bot på 1,2 milliarder euro av den irske Datatilsynsmyndigheten for ulovlig
*overføring av europeiske brukeres data til USA.*[^8]

---

### Konsekvenser av personvernbrudd

*## For enkeltpersoner:

- Identitetstyveri og svindel (lekkede personnumre, kontonumre)
- Psykologisk skade og tap av kontroll over eget liv
- Diskriminering (lekkede opplysninger om helse, seksualitet, politisk overbevisning)
- Stalking og trakassering (lekkede adresse- eller posisjonsdata)

*## For virksomheter:

- Millionbøter fra Datatilsynet
- Svekket omdømme og tap av kundenes tillit
- Søksmål fra skadelidte
- Tap av kontrakter i offentlig sektor

*## For samfunnet:

- Svekket tillit til digitale tjenester
- Økt motstand mot nødvendig digitalisering
- Mulig misbruk av persondata i politiske kampanjer (Cambridge Analytica-skandalen)[^9]
- Trussel mot ytringsfriheten når folk vet at de overvåkes

---

## Eksempel / lab

*## Scenariobeskrivelse: Vurder personvernkonsekvenser

DDu er IT-ansvarlig ved Solberg ungdomsskole. Skolen vurderer å innføre et nytt system som bruker ansiktsgjenkjenning for
Då registrere elevers fremmøte automatisk.

Vurder følgende:

11.**Behandlingsgrunnlag:**Hva er grunnlaget for å behandle biometriske data? Samtykke fra elever? Fra foresatte? Er
1dette tilstrekkelig for biometriske data (art. 9)?

22.**Dataminimering:**Er ansiktsgjenkjenning nødvendig for fremmøteregistrering, eller kan dette oppnås med enklere
2metoder?

33.**Privacy by Design:**Hvis skolen går videre – hvilke tekniske tiltak bør integreres fra start? (kryptering av
3biometrisk database, begrenset tilgang, automatisk sletting ved skoleårets slutt)

4.**Varsling:**Hvis biometrisk database lekker – hvem varsler du, innen hvilken frist, og hva skriver du?

***Konklusjon:**Et slikt system vil nesten uten tvil kreve DPIA (Data Protection Impact Assessment –
*personvernkonsekvensvurdering, GDPR art. 35) fordi det innebærer systematisk behandling av biometriske data om barn.

---

## Study guide

### Personvern og GDPR – kjerneinnhold

*## Hva er GDPR?
GGDPR er EUs personvernforordning, gjeldende i Norge via EØS. Den gir enkeltpersoner rettigheter over sine
GGpersonopplysninger og stiller krav til alle virksomheter som behandler slike data.
GDatatilsynet er norsk tilsynsmyndighet.

*## De 7 prinsippene (GDPR art. 5):
LLovlighet/rettferdighet/åpenhet, formålsbegrensning, dataminimering, riktighet, lagringsbegrensning,
Lintegritet/konfidensialitet, ansvarlighet. Alle er obligatoriske.

*## Behandlingsgrunnlag (GDPR art. 6):
DDu trenger alltid et grunnlag for å behandle personopplysninger: samtykke, avtale, rettslig plikt, vitale interesser,
Dallmenn interesse eller berettiget interesse. Uten grunnlag er behandlingen ulovlig.

*## Registrertes rettigheter:
IInnsyn, retting, sletting («rett til å bli glemt»), portabilitet, innsigelse og begrensning.
IVirksomheter plikter å oppfylle disse rettighetene innen fastsatte frister.

*## Privacy by Design:
PPersonvern integreres fra starten av systemutvikling – ikke legges på etterpå. Kryptering, dataminimering, automatisk
Psletting og tilgangskontroll er tekniske tiltak som implementeres fra dag én.

*## 72-timers-regelen:
PPersonvernbrudd med risiko for de registrerte skal varsles til Datatilsynet innen 72 timer.
PHøyrisiko-brudd varsles også direkte til de berørte.

*## Sanksjoner:
IInntil 20 millioner euro eller 4 % av global årsomsetning for alvorlige brudd. Personvern er ikke bare etisk – det er et
Ilovkrav med dramatiske konsekvenser ved brudd.

---

## FAQ

*## Hva er forskjellen mellom behandlingsansvarlig og databehandler?
BBehandlingsansvarlig bestemmer formålet med behandlingen og har det overordnede juridiske ansvaret.
BBDatabehandler (f.eks. en skytjeneste) behandler data på vegne av den behandlingsansvarlige etter instruksjoner.
BEn skole er behandlingsansvarlig; Microsoft er databehandler for Microsoft 365.

*## Må man alltid innhente samtykke for å behandle personopplysninger?
NNei. Samtykke er bare ett av seks behandlingsgrunnlag. En arbeidsgiver trenger ikke samtykke for å behandle
NNlønnsinformasjon – det er nødvendig for å oppfylle en avtale. Mange offentlige organer behandler personopplysninger
Nbasert på rettslig plikt.

*## Hva er en DPIA?
DDPIA (Data Protection Impact Assessment) er en personvernkonsekvensvurdering som kreves av GDPR art.
DD35 når en behandling medfører høy risiko for enkeltpersoner. Eksempler: systematisk overvåking, behandling av
Dbiometriske data, eller ny teknologi med ukjente personvernkonsekvenser.

*## Hva er pseudonymisering og anonymisering?
PPseudonymisering erstatter direkte identifikatorer (navn, personnummer) med et pseudonym – data kan fortsatt kobles
PPtilbake til personen med tilleggsinformasjon. Anonymisering fjerner all mulighet for identifikasjon – data faller da
Putenfor GDPR. Pseudonymisering er et GDPR-tiltak; anonymisering fjerner GDPR-kravene.

*## Hva betyr «rett til å bli glemt» i praksis?
EEnkeltpersoner kan kreve at virksomheter sletter personopplysninger om dem når dataene ikke lenger er nødvendige,
EEsamtykket trekkes tilbake, eller det ikke finnes annet behandlingsgrunnlag. Retten er ikke absolutt – den kan
Eoverstyres av lovpålagt oppbevaringsplikt (f.eks. regnskapsdata).

*## Hva må varslet til Datatilsynet inneholde?
BBeskrivelse av bruddet, kategorier og omtrentlig antall berørte personer og personopplysninger, mulige konsekvenser for
Bde registrerte, og tiltak som er iverksatt for å håndtere bruddet og begrense skaden.

*## Hvordan skiller GDPR mellom normale og sensitive personopplysninger?
GGDPR art. 9 definerer spesielle kategorier (sensitive data): helseopplysninger, biometriske data, genetiske data, etnisk
GGopprinnelse, politisk overbevisning, religiøs overbevisning, fagforeningsmedlemskap og seksuelle forhold.
GFor disse kreves et strengere grunnlag og ytterligere sikkerhetstiltak.

---

## Quiz

<details><summary>Spørsmål 1: Hva er de sju personvernprinsippene i GDPR artikkel 5?</summary>

***Svar:**Lovlighet, rettferdighet og åpenhet / Formålsbegrensning / Dataminimering / Riktighet / Lagringsbegrensning /
*Integritet og konfidensialitet / Ansvarlighet.

</details>

<details><summary>Spørsmål 2: Hva er 72-timers-regelen i GDPR?</summary>

***Svar:**GDPR art. 33 krever at brudd på personvernet som innebærer risiko for de registrerte, skal varsles til
*Datatilsynet innen 72 timer etter at virksomheten oppdaget bruddet.

</details>

<details><summary>Spørsmål 3: Hva er Privacy by Design?</summary>

***Svar:**Privacy by Design (innebygd personvern) er prinsippet om at personvern skal integreres i systemdesign fra
**starten, ikke legges til etterpå. Det er lovfestet i GDPR art. 25 og innebærer tiltak som kryptering, dataminimering og
*tilgangskontroll fra dag én.

</details>

<details><summary>Spørsmål 4: Hva er en databehandleravtale, og når kreves den?</summary>

***Svar:**En databehandleravtale (GDPR art. 28) kreves når en virksomhet lar en tredjepart behandle personopplysninger på
**sine vegne. Avtalen regulerer hva tredjeparten kan gjøre med dataene. Eksempel: en skole som bruker Microsoft 365 må ha
*databehandleravtale med Microsoft.

</details>

<details><summary>Spørsmål 5: Hvilke konsekvenser kan et personvernbrudd ha for enkeltpersoner?</summary>

***Svar:**Identitetstyveri, svindel, psykologisk skade, diskriminering, stalking/trakassering, og tap av kontroll over
*eget liv. Brudd på sensitive kategorier (helse, seksualitet, politikk) kan ha særlig alvorlige konsekvenser.

</details>

---

## Ressurser

- [Datatilsynet – Personvernprinsippene](<https://www.datatilsynet.no/rettigheter-og-plikter/personvernprinsippene/>)
- [Datatilsynet – Rettigheter og plikter](<https://www.datatilsynet.no/rettigheter-og-plikter/>)
- [dubestemmer.no – Personvern for unge](<https://www.dubestemmer.no>)
- [slettmeg.no – Hjelp til å slette innhold på nett](<https://www.slettmeg.no>)
- [NDLA – Innebygd personvern](<https://ndla.no>)
- [Datatilsynet – Virksomhetenes plikter (fullstendig oversikt)](<https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/>)
- [YouTube: Personvern og GDPR – hva betyr det for deg? (Simployer, 10 min)](<https://www.youtube.com/watch?v=u6p_G7w89Uo>)

## Kilder

[^1]: GDPR (General Data Protection Regulation), EU-forordning 2016/679, gjeldende fra 25. mai 2018. Gjennomført i norsk rett ved personopplysningsloven. <https://lovdata.no/dokument/NL/lov/2018-06-15-38>
[^2]: GDPR art. 5 – Prinsipper for behandling av personopplysninger. <https://eur-lex.europa.eu/eli/reg/2016/679/oj>
[^3]: GDPR art. 25 – Innebygd personvern (Privacy by Design). Datatilsynet: <https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/innebygd-personvern/>
[^4]: GDPR art. 28 – Databehandleravtale. <https://eur-lex.europa.eu/eli/reg/2016/679/oj>
[^5]: GDPR art. 37–39 – Personvernombud (DPO). <https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/personvernombud/>
[^6]: GDPR art. 33 – Varsling om brudd. <https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/melde-og-varsle-om-brudd/>
[^7]: Datatilsynet – Norsk tilsynsmyndighet for personvern. <https://www.datatilsynet.no/>
[^8]: Meta-bot 2023 – irsk DPC: <https://www.datatilsynet.no/aktuelt/aktuelle-nyheter-2023/irc-dpc-meta-bot/>
[^9]: Cambridge Analytica-skandalen (2018). <https://www.datatilsynet.no/aktuelt/aktuelle-nyheter-2018/cambridge-analytica/>
