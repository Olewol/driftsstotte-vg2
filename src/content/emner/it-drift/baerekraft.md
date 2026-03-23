---
title: "Bærekraft i IT-drift"
emne: it-drift
kompetansemaal:
  - km-12
kilder:
  - ndla
  - https://ndla.no/nb/subject:1:43a4e98f-ce79-42b3-9022-297e68266455/topic:1:94c5e317-0f9c-486a-8686-2678683519d5/resource:1:115939
  - https://www.nkom.no/aktuelt/digital-infrastruktur-og-miljo-hvordan-paivirker-vi-klimaet
video: https://www.youtube.com/watch?v=68D0v7Y-eIk
tags: []
flashcards: true
public: true
notebooklm: true
---

## Introduksjon

IT-bransjen er ikke bare digital – den er fysisk, energikrevende og ressursintensiv. Servere, nettverk og klientutstyr produserer varme, bruker strøm og skaper avfall. Å forstå og redusere IT-driftens miljøpåvirkning er en del av fagkompetansen i Driftsstøtte VG2.

Kompetansemål km-12 handler om å utforske dataindustriens miljøavtrykk og vurdere tiltak for mer bærekraftig IT-drift. Det er et felt i rask utvikling, der bransjen selv setter ambisiøse mål – og der det gjenstår mye arbeid. Valg av [[skytjenester]] og [[driftsarkitektur]] har direkte innvirkning på miljøavtrykket.

---

## Teori

### Datasentrenes energiforbruk

Datasentre er den mest energikrevende enkeltkomponenten i IT-infrastrukturen.

**Globalt:**
> "Estimated global data centre electricity consumption in 2022 was 240–340 TWh, or around 1–1.3% of global final electricity demand." – IEA (2023)

I tillegg bruker dataoverføringsnettverk 260–360 TWh per år. Til sammen utgjør dette ca. 1–2,8 % av globalt el-forbruk.

CO₂-utslippene fra IT-sektoren (inkl. produksjon av utstyr) er estimert til rundt **330 millioner tonn CO₂-ekvivalenter i 2020**.

**Konsentrasjonseksempel – Irland:**
I 2022 sto datasentre for **18 % av Irlands totale el-forbruk**. Irland er et attraktivt land for store tech-selskaper (lav skatt, gunstig lokalisering) og har fått merke presset på strømnettet.

**Danmark** anslår en seksdobling av datasenterforbruk innen 2030, noe som kan utgjøre opptil 15 % av landets el-forbruk.

De fire store – Amazon, Microsoft, Google og Meta – brukte samlet over **72 TWh i 2021**.

---

### PUE – Power Usage Effectiveness

PUE er bransjens standardmål for energieffektivitet i datasentre:

$$\text{PUE} = \frac{\text{Totalt el-forbruk i datasenteret}}{\text{El-forbruk til IT-utstyr}}$$

- **PUE = 1,0** er teoretisk perfekt – all strøm går til IT-utstyret
- **PUE = 1,5** betyr at 50 % ekstra strøm brukes til kjøling, belysning og annet
- **PUE = 2,0** betyr at like mye energi sløses som brukes nyttig

**Benchmarks:**
| Aktør | PUE |
|-------|-----|
| Google | ~1,10 |
| Meta | ~1,10 |
| Microsoft Azure | ~1,12 |
| Bransjegjennomsnitt | ~1,50 |
| Eldre datasenter | 2,0+ |

Hyperscalerne (Google, Meta, Microsoft, Amazon) er best i klassen med PUE rundt 1,1. Eldre og mindre datasentre kan ha PUE over 2,0, som betyr ekstremt dårlig effektivitet.

**Eksempel:** Et datasenter med IT-utstyr som bruker 1 000 kW og PUE = 1,5 bruker totalt 1 500 kW. De 500 kW som «sløses» går i stor grad til kjøling.

---

### Mørke data (Dark Data)

Et undervurdert miljøproblem er **mørke data** – data som lagres i datasentre, men aldri brukes. Studier anslår at opptil 80 % av alle lagrede data aldri aksesseres etter at de er opprettet.

Dette er problematisk fordi:
- Lagring av ubrukte data krever strøm til servere og kjøling
- Store organisasjoner akkumulerer terabytes med duplikater, utdaterte filer og ubrukte backuper

Tiltak: regelmessig opprydding av datalagre, klare retningslinjer for oppbevaring og sletting, og dataklassifisering.

---

### E-avfall og WEEE-direktivet

IT-utstyr har begrenset levetid. Når det skiftes ut, blir det **e-avfall** (elektrisk og elektronisk avfall).

E-avfall er problematisk fordi:
- IT-utstyr inneholder **sjeldne jordmetaller** (f.eks. neodym, indium, dysprosium) som er vanskelige å utvinne og produsere
- Utstyret inneholder **giftige stoffer** som bly, kadmium og kvikksølv
- Ulovlig deponering av e-avfall er et globalt problem, særlig i Vest-Afrika og Sørøst-Asia

**WEEE-direktivet** (Waste Electrical and Electronic Equipment) er EU-lovgivning som også gjelder i Norge. Direktivet krever:
- Produsenter og importører er ansvarlige for å samle inn og resirkulere e-avfall
- Forbrukere og virksomheter skal levere utstyr til godkjente innsamlingspunkter
- Visse materialer (plast, metaller, glass) skal gjenvinnes

I Norge håndteres e-avfall gjennom **Elretur** og andre godkjente retursystemer.

---

### Levetidsforlengelse av utstyr

En av de mest effektive miljøtiltakene er å bruke IT-utstyr lenger:

- Produksjonen av en bærbar PC utgjør typisk **70–80 % av det totale karbonavtrykket** over utstyrets levetid
- Å forlenge levetiden fra 3 til 5 år kan halvere miljøpåvirkningen per år
- **Refurbished utstyr** (brukt, renovert utstyr) er et voksende marked som reduserer behovet for ny produksjon

Tiltak for levetidsforlengelse:
- Oppgradering av RAM og lagring i stedet for å kjøpe ny PC
- Bruk av tynne klienter med lang levetid og enkel administrasjon
- Sentraliserte systemer (VDI, terminalservere) der klientene er enkle og holdbare

**Sirkulær IT** er en driftsmodell som prioriterer gjenbruk, reparasjon og oppgradering for å holde maskinvare i bruk så lenge som mulig – i tråd med sirkulær økonomi-prinsippene.

---

### Green IT-sertifiseringer

Virksomheter og produkter kan sertifiseres for energieffektivitet:

**Energy Star**
Amerikansk sertifiseringsordning for energieffektivt utstyr (PC-er, servere, monitorer). Produkter med Energy Star-merket bruker typisk 25–50 % mindre energi enn ukvalifiserte produkter.

**EPEAT**
(Electronic Product Environmental Assessment Tool) – et globalt register for miljøvennlig IT-utstyr. Vurderer livsløp, energibruk, design for gjenbruk og produksjonsforhold. Brukes i offentlige anskaffelser i mange land, inkludert Norge.

**ISO 50001**
Internasjonal standard for energiledelse. Stiller krav til systematisk energiarbeid i organisasjonen.

**TCO Certified**
Internasjonal bærekraftssertifisering for IT-utstyr som vurderer både miljø og sosiale forhold i produksjonskjeden. Mye brukt i norsk offentlig sektor.

---

### Grønne tiltak i virksomheter

Konkrete tiltak IT-ansvarlige kan gjøre:

1. **Konsolidering og virtualisering** – færre fysiske servere gir lavere energiforbruk
2. **Slå av utstyr som ikke brukes** – automatisert strømstyring
3. **Velg energieffektivt utstyr** – se etter Energy Star og EPEAT ved innkjøp
4. **Skymigrering** – store skyleverandører har bedre PUE enn de fleste interne datasentre
5. **Forleng levetiden på utstyr** – ikke bytt før nødvendig
6. **Riktig avhending** – bruk godkjente e-avfallsmottak (Elretur)
7. **Overvåk og rapporter energiforbruk** – det som måles, kan forbedres
8. **Rydd i mørke data** – slett ubrukte data og duplikater regelmessig
9. **Varmegjenvinning** – overskuddsvarme fra serverrom kan brukes til oppvarming av bygget

Amazon, Microsoft, Meta og Google har samlet inngått kontrakter for over **50 GW fornybar energi** – langt mer enn noe annet enkeltbransje.

IEA understreker at globale utslipp fra datasentre må **halveres innen 2030** for å nå netto-null-målene.

---

### Norsk perspektiv

Norge er i en privilegert posisjon innen bærekraftig IT:

**Fornybar energi**
Ca. 90 % av norsk strømproduksjon kommer fra **vannkraft** – noe som gjør norske datasentre blant de grønneste i verden. Statkraft er Europas største produsent av fornybar energi.

**Naturlig kjøling**
Norges kalde klima gjør det mulig å bruke **fri-kjøling** (outside air cooling) store deler av året, noe som reduserer behovet for energikrevende kjøleanlegg. Noen datasentre bruker sjøvann/fjordvann til kjøling.

**Grønn datasenterindustri**
Datasentre i Norden (Norge, Sverige, Finland) markedsføres internasjonalt som bærekraftige alternativer. Selskaper som Green Mountain (Ryfylke) og Lefdal Mine Datacenter er eksempler på norske aktører som bygger på disse fordelene.

**Norsk regelverk**
Nkom (Nasjonal kommunikasjonsmyndighet) og Miljødirektoratet regulerer e-avfall og IKT-sektoren. Offentlige anskaffelser i Norge kan stille krav til miljøsertifisering (EPEAT) ved innkjøp av IT-utstyr.

---

## Eksempel / lab

**Oppgave: Beregn PUE og vurder tiltak**

En skole har et serverrom med følgende målinger:
- Samlet strømmåler (alt utstyr i rommet): 12 kW
- Strømmåler kun for servere og nettverksutstyr: 8 kW

1. Beregn PUE for serverrommet.
2. Sammenlign med bransjegjennomsnitt (~1,5) og hyperscalere (~1,1).
3. Hva bruker de «ekstra» kWene til? (Hint: kjøling, belysning, UPS-tap)
4. Foreslå minst to tiltak for å forbedre PUE.
5. Diskuter: Bør skolen vurdere å flytte tjenester til en skyleverandør med bedre PUE? Hvilke faktorer avgjør?

**Tilleggsoppgave: Livssyklus for en bærbar PC**

Kartlegg miljøavtrykket til én bærbar PC gjennom hele livssyklusen: råvareproduksjon, produksjon, bruksfasen og avhending. Hvor i syklusen er miljøpåvirkningen størst? Hvilke valg kan du som IT-ansvarlig gjøre for å redusere det?

---

## Study guide

### Kjerneinnhold

Bærekraft i IT-drift handler om å forstå og redusere IT-sektorens miljøpåvirkning – fra energiforbruk i datasentre til avhending av gammelt utstyr.

**Energiforbruk:**
- Datasentre bruker 1–1,3 % av globalt el-forbruk (IEA 2022)
- PUE måler energieffektivitet: 1,0 er perfekt, 1,5 er bransjegjennomsnitt
- Hyperscalere (Google, Microsoft, AWS) oppnår ~1,1

**E-avfall:**
- 70–80 % av en PC-s karbonavtrykk skjer under produksjon
- WEEE-direktivet pålegger produsentansvar og krav til gjenvinning
- Elretur håndterer e-avfall i Norge

**Tiltak (i prioritert rekkefølge av effekt):**
1. Forleng levetiden på utstyr (størst effekt per krone)
2. Virtualiser og konsolider servere
3. Velg sertifisert utstyr (Energy Star, EPEAT)
4. Migrer til energieffektive skyleverandører
5. Rydd i mørke data

**Norsk særstilling:** vannkraft + kaldt klima = lavt karbonavtrykk for norske datasentre.

---

## FAQ

**Er IT en stor kilde til klimagasser?**
IT-sektoren utgjør ca. 2–4 % av globale CO₂-utslipp – omtrent som luftfarten. Det inkluderer produksjon av utstyr, drift av datasentre og overføring av data. Det er ikke enormt, men det vokser raskt i takt med digitaliseringen.

**Er skybasert drift alltid mer miljøvennlig enn on-premise?**
Ikke nødvendigvis, men store skyleverandører (Google, Microsoft, AWS) har PUE-verdier rundt 1,1 og investerer masivt i fornybar energi. Et eldre internt datasenter med PUE 2,0 og kullkraft kan ha et mye høyere karbonavtrykk enn å bruke en stor skyleverandør med fornybarenergi.

**Hva er mørke data og hvordan blir det et problem?**
Mørke data er data som lagres men aldri brukes – duplikater, utdaterte filer, glemte backuper. De bruker lagringsplass som krever strøm. Regelmessig opprydding og klare retningslinjer for dataoppbevaring reduserer problemet.

**Hva er TCO Certified og er det bedre enn Energy Star?**
TCO Certified vurderer hele livssyklusen og inkluderer sosiale forhold i produksjonskjeden (arbeidsmiljø, kjemikalier), mens Energy Star primært fokuserer på energibruk i driftsfasen. De er komplementære, og norsk offentlig sektor bruker begge.

**Hva er «sirkulær IT»?**
Sirkulær IT er en driftsmodell basert på sirkulær økonomi: utstyr holdes i bruk så lenge som mulig gjennom oppgradering, reparasjon og refurbishment. Når utstyret til slutt kasseres, gjenvinnes materialene. Det motvirker det lineære mønsteret «produser – bruk – kast».

**Hva gjør Norge spesielt egnet for grønne datasentre?**
Tre faktorer: nesten 100 % fornybar strøm fra vannkraft, kaldt klima som muliggjør naturlig kjøling store deler av året, og tilgang til fjordvann for kjøling. Dette gir svært lav PUE og nær-null CO₂ fra strøm. Lefdal Mine Datacenter i en norsk fjordside er et konkret eksempel.

---

## Quiz

<details><summary>Spørsmål 1: Hva er PUE og hva betyr en PUE på 1,0?</summary>

**Svar:** PUE (Power Usage Effectiveness) er et mål på energieffektivitet i datasentre. PUE = totalt el-forbruk / el-forbruk til IT-utstyr. En PUE på 1,0 er teoretisk perfekt – all strøm går til IT-utstyret. I praksis oppnår de beste datasentrene PUE rundt 1,1.

</details>

<details><summary>Spørsmål 2: Hva brukte datasentre globalt av elektrisitet i 2022, og hva utgjorde det som andel av globalt forbruk?</summary>

**Svar:** Ifølge IEA brukte datasentre 240–340 TWh i 2022, tilsvarende ca. 1–1,3 % av globalt el-forbruk.

</details>

<details><summary>Spørsmål 3: Hva er WEEE-direktivet?</summary>

**Svar:** WEEE er EU-direktivet om elektrisk og elektronisk avfall. Det pålegger produsentene ansvar for innsamling og gjenvinning av e-avfall, og stiller krav til virksomheter og forbrukere om å levere utstyr til godkjente mottak. Gjelder i Norge gjennom EØS.

</details>

<details><summary>Spørsmål 4: Hvorfor er Norge gunstig for grønne datasentre?</summary>

**Svar:** Norge har ca. 90 % fornybar strømproduksjon fra vannkraft, lavt strømpris, kaldt klima som muliggjør naturlig kjøling, og tilgang til sjø-/fjordvann for kjøling. Dette gir svært lave CO₂-utslipp og lav PUE for norske datasentre.

</details>

<details><summary>Spørsmål 5: Hva er det mest effektive enkeltiltaket for å redusere miljøpåvirkningen fra klientutstyr?</summary>

**Svar:** Å forlenge levetiden på utstyret. Produksjon av en PC utgjør 70–80 % av det totale karbonavtrykket over levetiden. Å bruke utstyret 5 år i stedet for 3 år halverer nesten den årlige miljøpåvirkningen. Refurbished utstyr er en relatert tilnærming.

</details>

---

## Flashcards

PUE :: Power Usage Effectiveness – mål på energieffektivitet i datasentre. PUE = totalt forbruk / IT-forbruk. 1,0 er perfekt; bransjegjennomsnitt ~1,5.

E-avfall :: Elektrisk og elektronisk avfall. Inneholder sjeldne jordmetaller og giftige stoffer. Skal leveres til godkjente mottak.

WEEE-direktivet :: EU-direktiv om elektrisk og elektronisk avfall. Produsentansvar og krav til gjenvinning. Gjelder i Norge.

Energy Star :: Sertifiseringsordning for energieffektivt IT-utstyr. Produkter bruker typisk 25–50 % mindre energi.

EPEAT :: Electronic Product Environmental Assessment Tool – global sertifisering for miljøvennlig IT-utstyr. Brukes i offentlige anskaffelser.

Levetidsforlengelse :: Tiltak for å bruke IT-utstyr lenger. Et av de mest effektive miljøtiltakene siden produksjon er den største miljøbelastningen.

Fri-kjøling :: Bruk av kald uteluft eller vann til å kjøle datasentre. Reduserer behovet for energikrevende kjølemaskiner.

Hyperscaler :: De største skyleverandørene (Google, Microsoft, Amazon, Meta). Har de beste PUE-verdiene (~1,1) og størst fornybarenergi-kontrakter.

Refurbished utstyr :: Brukt IT-utstyr som er renovert og selges på nytt. Reduserer behovet for ny produksjon og miljøbelastning.

Statkraft :: Norsk statlig energiselskap og Europas største produsent av fornybar energi. Viktig for Norges posisjon innen grønn IT.

IEA :: International Energy Agency – internasjonal organisasjon som overvåker energibruk globalt. Autoritativ kilde for datasentrestatistikk.

Sirkulær IT :: Driftsmodell som prioriterer gjenbruk, reparasjon og oppgradering for å holde maskinvare i bruk så lenge som mulig.

Mørke data (Dark Data) :: Data som lagres i datasentre men aldri brukes. Fører til unødvendig energiforbruk til lagring og kjøling.

TCO Certified :: Internasjonal bærekraftssertifisering for IT-utstyr som vurderer både miljø og sosiale forhold i produksjonskjeden.

EE-avfall :: Elektrisk og elektronisk avfall som inneholder miljøgifter og verdifulle metaller som krever spesialisert gjenvinning.

---

## Ressurser

- [IEA: Data Centres and Data Transmission Networks](https://www.iea.org/energy-system/buildings/data-centres-and-data-transmission-networks)
- [NDLA: Bærekraft og IT-utstyr](https://ndla.no/nb/subject:1:43a4e98f-ce79-42b3-9022-297e68266455/topic:1:94c5e317-0f9c-486a-8686-2678683519d5/resource:1:115939)
- [Nkom: Digital infrastruktur og miljø](https://www.nkom.no/aktuelt/digital-infrastruktur-og-miljo-hvordan-paivirker-vi-klimaet)
- [Elretur: E-avfall i Norge](https://www.elretur.no/)
- [YouTube: The life cycle of a smartphone – TED-Ed](https://www.youtube.com/watch?v=68D0v7Y-eIk)
- [[driftsarkitektur]]
- [[skytjenester]]
