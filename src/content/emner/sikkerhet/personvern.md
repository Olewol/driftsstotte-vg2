---
title: "Personvern og GDPR"
emne: sikkerhet
kompetansemaal:
  - km-11
kilder:
  - ndla
  - datatilsynet
tags: []
flashcards: true
public: true
---

## Introduksjon

Personvern handler om enkeltmenneskets rett til å kontrollere informasjon om seg selv. I vår digitale hverdag – der apper, tjenester og virksomheter samler inn enorme mengder data om oss – er personvern både en grunnleggende rettighet og et juridisk krav.

I EU og Norge reguleres personvern av **GDPR** (General Data Protection Regulation), en EU-forordning som trådte i kraft i mai 2018. GDPR gjelder i Norge gjennom EØS-avtalen og er gjennomført i norsk rett via **personopplysningsloven**. For deg som jobber i IT-drift er personvern ikke noe juridisk avdeling håndterer alene – tekniske valg som databasestruktur, tilgangskontroll, logging og backup har direkte personvernkonsekvenser.

---

## Teori

### De 7 personvernprinsippene (GDPR art. 5)

GDPR artikkel 5 fastsetter syv grunnleggende prinsipper for behandling av personopplysninger. Alle virksomheter som behandler personopplysninger er forpliktet til å følge disse:

| Nr | Prinsipp | Kort forklaring |
|---|---|---|
| 1 | **Lovlighet, rettferdighet og åpenhet** | Behandlingen må ha et rettslig grunnlag og være åpen overfor de registrerte |
| 2 | **Formålsbegrensning** | Data samles inn til et bestemt formål og kan ikke brukes til noe annet uten nytt grunnlag |
| 3 | **Dataminimering** | Kun de opplysningene som er nødvendige for formålet skal samles inn |
| 4 | **Riktighet** | Personopplysninger skal være korrekte og holdes oppdaterte |
| 5 | **Lagringsbegrensning** | Data skal slettes når de ikke lenger er nødvendige for formålet |
| 6 | **Integritet og konfidensialitet** | Egnede tekniske og organisatoriske tiltak skal sikre data mot uautorisert tilgang og tap |
| 7 | **Ansvarlighet** | Virksomheten må kunne dokumentere at den overholder alle prinsippene |

---

### Behandlingsgrunnlag (GDPR art. 6)

For å behandle personopplysninger lovlig trenger man alltid et **behandlingsgrunnlag**. GDPR art. 6 lister seks gyldige grunnlag:

1. **Samtykke** – Den registrerte har gitt eksplisitt, informert samtykke. Kan trekkes tilbake når som helst.
2. **Avtale** – Behandlingen er nødvendig for å oppfylle en avtale med den registrerte
3. **Rettslig plikt** – Virksomheten er lovpålagt å behandle opplysningene (f.eks. skatteregistre)
4. **Vitale interesser** – Nødvendig for å beskytte den registrertes liv
5. **Allmenn interesse** – Nødvendig for å utføre en oppgave i allmennhetens interesse
6. **Berettiget interesse** – Virksomhetens interesse veier tyngre enn den registrertes personverninteresse

For sensitive personopplysninger (helseopplysninger, politisk overbevisning, etnisk opprinnelse m.fl.) gjelder strengere regler (GDPR art. 9).

---

### Registrertes rettigheter

GDPR gir enkeltpersoner en rekke rettigheter som virksomheter er forpliktet til å oppfylle:

| Rettighet | Forklaring |
|---|---|
| **Innsyn (art. 15)** | Rett til å vite hvilke opplysninger som behandles om deg |
| **Retting (art. 16)** | Rett til å korrigere uriktige opplysninger |
| **Sletting (art. 17)** | «Rett til å bli glemt» – sletting av opplysninger når de ikke lenger er nødvendige |
| **Portabilitet (art. 20)** | Rett til å motta egne data i et maskinlesbart format og overføre dem til annen leverandør |
| **Innsigelse (art. 21)** | Rett til å protestere mot behandling basert på berettiget interesse |
| **Begrensning (art. 18)** | Rett til å kreve at behandlingen begrenses i visse situasjoner |

---

### Innebygd personvern – Privacy by Design

**Privacy by Design** (innebygd personvern) er prinsippet om at personvern skal integreres i systemdesign fra starten av, ikke legges til etterpå. Dette er lovfestet i GDPR art. 25.

Praktiske eksempler:
- Kryptere all datalagring fra dag én – ikke som en ettertanke
- Kun samle inn nødvendige felter i registreringsskjemaer (dataminimering)
- Implementere tilgangskontroll slik at kun autoriserte brukere ser sensitive data
- Automatisk slette data etter en fastsatt periode (lagringsbegrensning)
- Pseudonymisering: erstatte direkte identifikatorer med pseudonymer i testdatabaser

---

### Personvernombud (DPO)

Noen virksomheter er pålagt å ha et **personvernombud (Data Protection Officer – DPO)**. Dette gjelder:
- Offentlige organer (alle norske kommuner, etater osv.)
- Virksomheter som driver systematisk overvåking av enkeltpersoner i stor skala
- Virksomheter som behandler sensitive personopplysninger i stor skala

DPO-en fungerer som intern ekspert og kontaktpunkt for Datatilsynet.

---

### Databehandleravtale (GDPR art. 28)

Når en virksomhet bruker en tredjepart til å behandle personopplysninger på vegne av seg (f.eks. en skyløsning, et lønningssystem, en e-posttjeneste), kreves det en **databehandleravtale**. Avtalen regulerer hva behandleren kan gjøre med dataene, og sikrer at de kun brukes til angitt formål.

Eksempel: En norsk skole bruker Microsoft 365. Skolen er da **behandlingsansvarlig**, Microsoft er **databehandler**, og det må foreligge en databehandleravtale.

---

### Brudd på personvern og varslingsplikten

Hvis personopplysninger kompromitteres (uautorisert tilgang, tap av data, feil utsendelse) foreligger det et **personvernbrudd (data breach)**.

**GDPR art. 33 – 72-timers-regelen:**
Brudd med risiko for de registrerte skal varsles til Datatilsynet innen **72 timer** etter at virksomheten oppdaget bruddet. Varselet skal inneholde:
- Beskrivelse av bruddet (hva skjedde)
- Kategorier og omtrentlig antall berørte
- Mulige konsekvenser
- Tiltak som er iverksatt

**GDPR art. 34:** Brudd med høy risiko for de registrerte skal også varsles direkte til de berørte personene uten ubegrunnet opphold.

---

### Datatilsynet og sanksjoner

**Datatilsynet** er den norske tilsynsmyndigheten for personvern. Datatilsynet:
- Håndhever GDPR og personopplysningsloven
- Veileder virksomheter og enkeltpersoner
- Kan ilegge administrative gebyrer

**Sanksjoner etter GDPR:**
- Inntil **10 millioner euro** eller 2 % av global årsomsetning for tekniske brudd (art. 83.4)
- Inntil **20 millioner euro** eller 4 % av global årsomsetning for grunnleggende brudd (art. 83.5)

*Eksempel: Meta ble i 2023 ilagt en bot på 1,2 milliarder euro av den irske Datatilsynsmyndigheten for ulovlig overføring av europeiske brukeres data til USA.*

---

### Konsekvenser av personvernbrudd

**For enkeltpersoner:**
- Identitetstyveri og svindel (lekkede personnumre, kontonumre)
- Psykologisk skade og tap av kontroll over eget liv
- Diskriminering (lekkede opplysninger om helse, seksualitet, politisk overbevisning)
- Stalking og trakassering (lekkede adresse- eller posisjonsdata)

**For virksomheter:**
- Millionbøter fra Datatilsynet
- Svekket omdømme og tap av kundenes tillit
- Søksmål fra skadelidte
- Tap av kontrakter i offentlig sektor

**For samfunnet:**
- Svekket tillit til digitale tjenester
- Økt motstand mot nødvendig digitalisering
- Mulig misbruk av persondata i politiske kampanjer (Cambridge Analytica-skandalen)
- Trussel mot ytringsfriheten når folk vet at de overvåkes

---

## Eksempel / lab

**Scenariobeskrivelse: Vurder personvernkonsekvenser**

Du er IT-ansvarlig ved Solberg ungdomsskole. Skolen vurderer å innføre et nytt system som bruker ansiktsgjenkjenning for å registrere elevers fremmøte automatisk.

Vurder følgende:

1. **Behandlingsgrunnlag:** Hva er grunnlaget for å behandle biometriske data? Samtykke fra elever? Fra foresatte? Er dette tilstrekkelig for biometriske data (art. 9)?

2. **Dataminimering:** Er ansiktsgjenkjenning nødvendig for fremmøteregistrering, eller kan dette oppnås med enklere metoder?

3. **Privacy by Design:** Hvis skolen går videre – hvilke tekniske tiltak bør integreres fra start? (kryptering av biometrisk database, begrenset tilgang, automatisk sletting ved skoleårets slutt)

4. **Varsling:** Hvis biometrisk database lekker – hvem varsler du, innen hvilken frist, og hva skriver du?

**Konklusjon:** Et slikt system vil nesten uten tvil kreve DPIA (Data Protection Impact Assessment – personvernkonsekvensvurdering, GDPR art. 35) fordi det innebærer systematisk behandling av biometriske data om barn.

---

## Quiz

<details><summary>Spørsmål 1: Hva er de sju personvernprinsippene i GDPR artikkel 5?</summary>

**Svar:** Lovlighet, rettferdighet og åpenhet / Formålsbegrensning / Dataminimering / Riktighet / Lagringsbegrensning / Integritet og konfidensialitet / Ansvarlighet.

</details>

<details><summary>Spørsmål 2: Hva er 72-timers-regelen i GDPR?</summary>

**Svar:** GDPR art. 33 krever at brudd på personvernet som innebærer risiko for de registrerte, skal varsles til Datatilsynet innen 72 timer etter at virksomheten oppdaget bruddet.

</details>

<details><summary>Spørsmål 3: Hva er Privacy by Design?</summary>

**Svar:** Privacy by Design (innebygd personvern) er prinsippet om at personvern skal integreres i systemdesign fra starten, ikke legges til etterpå. Det er lovfestet i GDPR art. 25 og innebærer tiltak som kryptering, dataminimering og tilgangskontroll fra dag én.

</details>

<details><summary>Spørsmål 4: Hva er en databehandleravtale, og når kreves den?</summary>

**Svar:** En databehandleravtale (GDPR art. 28) kreves når en virksomhet lar en tredjepart behandle personopplysninger på sine vegne. Avtalen regulerer hva tredjeparten kan gjøre med dataene. Eksempel: en skole som bruker Microsoft 365 må ha databehandleravtale med Microsoft.

</details>

<details><summary>Spørsmål 5: Hvilke konsekvenser kan et personvernbrudd ha for enkeltpersoner?</summary>

**Svar:** Identitetstyveri, svindel, psykologisk skade, diskriminering, stalking/trakassering, og tap av kontroll over eget liv. Brudd på sensitive kategorier (helse, seksualitet, politikk) kan ha særlig alvorlige konsekvenser.

</details>

---

## Flashcards

GDPR :: EUs personvernforordning (General Data Protection Regulation), gjeldende i Norge via EØS. Trådte i kraft mai 2018
Personopplysningsloven :: Norsk lov som gjennomfører GDPR i norsk rett
Behandlingsgrunnlag :: Juridisk grunnlag for å behandle personopplysninger (GDPR art. 6): samtykke, avtale, rettslig plikt m.fl.
Dataminimering :: Prinsipp om at kun nødvendige personopplysninger samles inn (GDPR art. 5 nr. 1 c)
Privacy by Design :: Prinsipp om at personvern integreres i systemdesign fra starten (GDPR art. 25)
72-timers-regelen :: Brudd med risiko for registrerte skal varsles til Datatilsynet innen 72 timer (GDPR art. 33)
Datatilsynet :: Norsk tilsynsmyndighet for personvern. Håndhever GDPR og personopplysningsloven
DPO :: Data Protection Officer / personvernombud – obligatorisk for offentlige organer og visse private virksomheter
Rett til å bli glemt :: Retten til å kreve sletting av egne personopplysninger når de ikke lenger er nødvendige (GDPR art. 17)
Databehandleravtale :: Avtale (GDPR art. 28) som regulerer hvordan en tredjepart behandler personopplysninger på vegne av virksomheten

---

## Ressurser

- [Datatilsynet – Personvernprinsippene](https://www.datatilsynet.no/rettigheter-og-plikter/personvernprinsippene/)
- [Datatilsynet – Rettigheter og plikter](https://www.datatilsynet.no/rettigheter-og-plikter/)
- [dubestemmer.no – Personvern for unge](https://www.dubestemmer.no)
- [slettmeg.no – Hjelp til å slette innhold på nett](https://www.slettmeg.no)
- [NDLA – Innebygd personvern](https://ndla.no)
