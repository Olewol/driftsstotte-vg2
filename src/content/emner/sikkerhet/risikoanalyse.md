---
title: "Risikoanalyse"
emne: sikkerhet
kompetansemaal:
  - km-08
kilder:
  - ndla
  - nsm
  - datatilsynet
tags: []
flashcards: true
public: true
---

## Introduksjon

En risikoanalyse er et strukturert verktøy for å identifisere hva som kan gå galt med et IT-system, hvor sannsynlig det er, og hva konsekvensene vil være. Formålet er ikke å eliminere all risiko – det er umulig – men å forstå risikoen godt nok til å prioritere de riktige tiltakene.

NSM Grunnprinsipper for IKT-sikkerhet (v2.1, 2024) plasserer «Identifiser og kartlegg» som første og grunnleggende steg. GDPR artikkel 32 krever dessuten at alle virksomheter som behandler personopplysninger gjennomfører risikovurdering som grunnlag for sine sikkerhetstiltak.

---

## Teori

### Hva er risiko?

**Risiko** defineres som produktet av sannsynlighet og konsekvens:

> **Risiko = Sannsynlighet × Konsekvens**

- **Sannsynlighet:** Hvor trolig er det at hendelsen inntreffer? (svært liten / liten / middels / stor / svært stor)
- **Konsekvens:** Hva er skadeomfanget hvis hendelsen inntreffer? (ubetydelig / liten / moderat / alvorlig / svært alvorlig)

En hendelse med lav sannsynlighet men katastrofale konsekvenser kan være like viktig å håndtere som en hendelse som inntreffer ofte men med liten skade.

---

### 4-stegs risikoanalyseprosess

#### Steg 1: Identifiser verdier og trusler

**Verdier (assets)** er alt som har verdi og som kan bli rammet:
- Maskinvare (servere, nettverksutstyr, PC-er)
- Programvare og systemer
- Data (personopplysninger, regnskapsdata, IP)
- Tjenester (e-post, ERP, nettsted)
- Ansatte og kompetanse

**Trusler** er hendelser som kan skade verdiene:
- Ransomware-angrep
- Phishing mot ansatte
- Brann eller flom i serverrom
- Strømbrudd
- Menneskelig feil (slette filer ved uhell)
- Innsidetrusler

#### Steg 2: Identifiser sårbarheter

En sårbarhet er en svakhet som gjør at en trussel kan materialisere seg:
- Utdatert programvare uten patcher
- Svake passord eller manglende MFA
- Manglende brannmur
- Ingen backup-rutine
- Ansatte som ikke er opplært i phishing-gjenkjenning

#### Steg 3: Vurder og ranger risiko

Bruk **risikomatrisen** (5×5) til å plassere og rangere risikoscenarioer:

| | **1 Ubetydelig** | **2 Liten** | **3 Moderat** | **4 Alvorlig** | **5 Svært alvorlig** |
|---|---|---|---|---|---|
| **5 Svært stor** | 5 | 10 | 15 | 20 | **25** |
| **4 Stor** | 4 | 8 | 12 | **16** | **20** |
| **3 Middels** | 3 | 6 | **9** | 12 | 15 |
| **2 Liten** | 2 | 4 | 6 | 8 | 10 |
| **1 Svært liten** | 1 | 2 | 3 | 4 | 5 |

*Fargekode: 1–4 = lav (grønn), 5–9 = middels (gul), 10–19 = høy (oransje), 20–25 = kritisk (rød)*

#### Steg 4: Foreslå tiltak og aksepter restrisiko

For hvert høyt- eller kritisk-rangert risikoscenario velger virksomheten ett av fire alternativer:

| Strategi | Forklaring |
|---|---|
| **Reduser** | Innfør tiltak som senker sannsynlighet eller konsekvens |
| **Unngå** | Slutt med aktiviteten som skaper risikoen |
| **Overfør** | Forsikre deg mot risikoen (eks. cyberforsikring) |
| **Aksepter** | Ledelsen godkjenner at risikoen er innenfor akseptabelt nivå |

**Restrisiko** er den risikoen som gjenstår etter at tiltak er innført. Ledelsen må formelt akseptere restrisikoen.

---

### Tiltakstyper

| Type | Beskrivelse | Eksempel |
|---|---|---|
| **Forebyggende (preventive)** | Hindrer at hendelsen inntreffer | Patcher, MFA, brannmur |
| **Oppdagende (detektive)** | Oppdager at noe skjer | Logging, IDS, antivirusovervåkning |
| **Reaktive (korrigerende)** | Begrenser skaden etter hendelsen | Backup, incident response-plan, DR-plan |

God sikkerhetspraksis kombinerer alle tre typer – du kan ikke bare forebygge, du må også oppdage og reagere.

---

### GDPR artikkel 32 og risikovurdering

GDPR artikkel 32 krever at virksomheter som behandler personopplysninger skal implementere «egnede tekniske og organisatoriske sikkerhetstiltak» basert på en risikovurdering. Vurderingen skal ta hensyn til:

- Behandlingens art, omfang, sammenheng og formål
- Sannsynligheten for og alvorligheten av risikoen for de registrertes rettigheter

Dette betyr at risikoanalyse ikke bare er god praksis – det er et lovkrav dersom du behandler persondata.

---

## Eksempel / lab

### Risikoanalyse for Bakke videregående skole – skolenettverk

**Scenario:** Bakke vgs har et skolenettverk med følgende komponenter: Active Directory-server, filserver med elevarbeider, trådløst gjestenettverk, 350 elevmaskiner og ansatt-PC-er.

**Steg 1 – Identifiser verdier og trusler:**

| Verdi | Trussel |
|---|---|
| AD-server | Ransomware, passordangrep |
| Filserver med elevarbeider | Ransomware, utilsiktet sletting, brann |
| Trådløst gjestenettverk | Uautorisert tilgang, sniffer-angrep |
| Ansatt-PC-er | Phishing, malware via USB |

**Steg 2 – Identifiser sårbarheter:**
- AD-server kjører Windows Server 2016 uten automatisk patching
- Ansatte bruker enkle passord uten MFA
- Gjestenettverk har ikke VLAN-isolasjon fra internett
- Ingen backup-rutine testes jevnlig

**Steg 3 – Risikomatrise (utvalg):**

| Scenario | Sannsynlighet | Konsekvens | Risikoverdi |
|---|---|---|---|
| Ransomware mot filserver | 3 (middels) | 5 (svært alvorlig) | **15 – høy** |
| Phishing mot ansatt | 4 (stor) | 3 (moderat) | **12 – høy** |
| Brann i serverrom | 1 (svært liten) | 5 (svært alvorlig) | **5 – middels** |
| Elev kobler til skadevare via USB | 3 (middels) | 2 (liten) | **6 – middels** |

**Steg 4 – Tiltak:**

| Risiko | Tiltak | Type |
|---|---|---|
| Ransomware mot filserver | Innfør automatisk patching, installer backup med offsite-kopi | Forebyggende + reaktiv |
| Phishing mot ansatt | Obligatorisk phishing-trening, aktiver MFA på alle kontoer | Forebyggende |
| Brann i serverrom | Brannslukkingsanlegg, offsite backup, DR-plan | Forebyggende + reaktiv |
| USB-bruk | Deaktiver USB-porter via GPO, tilat kun godkjente enheter | Forebyggende |

**Restrisiko:** Ransomware-risikoen reduseres fra 15 til anslagsvis 6 (middels) etter tiltakene. Ledelsen aksepterer restrisikoen.

---

### Klasseromscase: ROS-analyse for MediaHuset AS

> **Kilde:** Klasseromsnotater (2ITA)
>
> I undervisningen gjennomfører elevene en ROS-analyse for en tenkt Dark Web-lab som gravejournalistene i «MediaHuset AS» skal bruke. Caset illustrerer strukturert risikostyring:
>
> **Tre verdier å beskytte:**
> - Hovednettverket til bedriften
> - Kildevern / journalistenes anonymitet
> - Bedriftens omdømme
>
> **Tre identifiserte trusler:**
> - Journalist laster ned malware som sprer seg til bedriftsnettet
> - Journalist logger på privat Facebook i Tor og avsløres (bryter anonymitet)
> - Renholder setter inn infisert minnepenn i lab-maskinen
>
> **Vurdering:** For hver trussel vurderes sannsynlighet og konsekvens (Lav/Middels/Høy). Den farligste kombinasjonen (typisk malware-spredning med Høy konsekvens) krever et konkret tiltak — for eksempel å fysisk koble lab-maskinen fra bedriftsnettet og bruke en dedikert 4G-ruter.
>
> **Poenget med caset:** Risikostyring er ikke magefølelse, men en strukturert prosess: definer verdier → identifiser trusler → vurder sannsynlighet og konsekvens → foreslå tiltak.

## Quiz

<details><summary>Spørsmål 1: Hva er formelen for risiko?</summary>

**Svar:** Risiko = Sannsynlighet × Konsekvens. Begge faktorer vurderes typisk på en skala fra 1 til 5.

</details>

<details><summary>Spørsmål 2: Hva er de fire stegene i en risikoanalyseprosess?</summary>

**Svar:**
1. Identifiser verdier og trusler
2. Identifiser sårbarheter
3. Vurder og ranger risiko (risikomatrise)
4. Foreslå tiltak og aksepter restrisiko

</details>

<details><summary>Spørsmål 3: Hva er forskjellen mellom forebyggende, oppdagende og reaktive tiltak?</summary>

**Svar:** Forebyggende tiltak hindrer at hendelsen inntreffer (f.eks. brannmur, MFA). Oppdagende tiltak avslører at noe skjer (f.eks. logging, IDS). Reaktive tiltak begrenser skaden etter hendelsen (f.eks. backup, incident response-plan).

</details>

<details><summary>Spørsmål 4: Hva krever GDPR artikkel 32?</summary>

**Svar:** GDPR artikkel 32 krever at virksomheter som behandler personopplysninger gjennomfører risikovurdering og implementerer egnede tekniske og organisatoriske sikkerhetstiltak basert på denne vurderingen.

</details>

<details><summary>Spørsmål 5: Hva er restrisiko?</summary>

**Svar:** Restrisiko er den risikoen som gjenstår etter at tiltak er innført. Det er ikke mulig å eliminere all risiko – ledelsen må formelt akseptere den gjenværende risikoen.

</details>

---

## Flashcards

Risiko :: Sannsynlighet multiplisert med konsekvens. Uttrykker hvor alvorlig en potensiell hendelse er
Risikomatrise :: Visuelt verktøy (typisk 5×5) som rangerer risikoscenarioer etter sannsynlighet og konsekvens
Sårbarhet :: En svakhet i et system som kan utnyttes av en trussel (eks. utdatert programvare, svakt passord)
Trussel :: En potensiell hendelse som kan skade verdier i et IT-system (eks. ransomware, brann, menneskelig feil)
Forebyggende tiltak :: Tiltak som hindrer at en hendelse inntreffer, f.eks. brannmur, MFA og patcher
Oppdagende tiltak :: Tiltak som avslører at noe er under angrep, f.eks. logging, IDS og antivirusovervåkning
Reaktive tiltak :: Tiltak som begrenser skaden etter en hendelse, f.eks. backup-gjenoppretting og DR-plan
Restrisiko :: Risikoen som gjenstår etter at tiltak er innført – aksepteres formelt av ledelsen
GDPR art. 32 :: Lovkrav om å gjennomføre risikovurdering og innføre egnede sikkerhetstiltak ved behandling av personopplysninger
Risikoaksept :: En ledelsesbeslutning om at en gjenværende risikonivå er innenfor akseptable grenser

---

## Ressurser

- [NSM Grunnprinsipper for IKT-sikkerhet](https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/)
- [Datatilsynet – Risikovurdering og personvern](https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/risikovurdering/)
- [NDLA – Risikovurdering for kontoradministrasjon](https://ndla.no)
