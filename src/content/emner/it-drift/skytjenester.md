---
title: "Skytjenester"
emne: it-drift
kompetansemaal:
  - km-03
kilder:
  - ndla
  - https://ndla.no/resource:160100
  - https://www.digdir.no/nasjonal-arkitektur/skytjenester/2153
video: https://ndla.no/resource:46761
tags: []
flashcards: https://notebooklm.google.com/notebook/bc9a5656-7a9b-4dc5-a59e-ef4a96aa8ccd
public: true
notebooklm: true
---

## Introduksjon

Skyberegning (cloud computing) har endret måten virksomheter bygger og drifter IT-systemer. I stedet for å eie og vedlikeholde egne servere kan en virksomhet leie datakraft, lagring og programvare over internett – og betale kun for det de bruker.

AWS definerer det slik: *"Cloud computing is the on-demand delivery of IT resources over the Internet with pay-as-you-go pricing."*

I dag bruker de fleste virksomheter en eller annen form for skytjeneste, fra e-post og fillagring til fullstendige serverinfrastrukturer. Å forstå de ulike tjenestemodellene og driftsmodellene er en grunnleggende kompetanse i IT-faget. For å forstå sky i sammenheng, se [[driftsarkitektur]] for oversikten over on-premise, sky og hybrid.

---

## Teori

### De tre tjenestemodellene

#### IaaS – Infrastructure as a Service

IaaS gir tilgang til grunnleggende IT-infrastruktur over nett: virtuelle maskiner, lagring, nettverk og brannmurer. Du leier infrastruktur, men er selv ansvarlig for operativsystem, applikasjoner og konfigurering.

> "In an IaaS model, the cloud provider is responsible for maintaining the hardware, network connectivity (to the internet), and physical security. You're responsible for everything else: operating system installation, configuration, and maintenance; network configuration; database and storage configuration." – Microsoft Learn

**Eksempler:** Azure Virtual Machines, AWS EC2, Google Compute Engine

**Typisk bruker:** Virksomheter som vil flytte eksisterende servere til skyen (*lift-and-shift*) uten å endre arkitekturen.

---

#### PaaS – Platform as a Service

PaaS er ett steg høyere. Skyleverandøren håndterer infrastrukturen og operativsystemet – du fokuserer på å utvikle og kjøre applikasjoner.

> "In a PaaS environment, the cloud provider maintains the physical infrastructure, physical security, and connection to the internet. They also maintain the operating systems, middleware, development tools, and business intelligence services." – Microsoft Learn

**Eksempler:** Azure App Service, Google App Engine, Heroku

**Typisk bruker:** Utviklere og IT-team som vil lage og rulle ut applikasjoner uten å administrere servere.

**Serverless** er en variant av PaaS der leverandøren automatisk tildeler ressurser basert på kodekjøring – man trenger ikke tenke på underliggende servere i det hele tatt. Eksempel: Azure Functions, AWS Lambda.

---

#### SaaS – Software as a Service

SaaS er ferdig programvare levert som en nettbasert tjeneste. Leverandøren håndterer alt – infrastruktur, operativsystem, applikasjon og oppdateringer. Brukeren logger inn og bruker tjenesten.

**Eksempler:** Microsoft 365, Google Workspace, Salesforce, Zoom

**Typisk bruker:** Sluttbrukere og virksomheter som vil ha programvare uten installasjon eller driftsansvar.

---

### Sammenligning av tjenestemodellene

| Ansvar | On-premise | IaaS | PaaS | SaaS |
|--------|-----------|------|------|------|
| Fysisk maskinvare | Virksomheten | Leverandøren | Leverandøren | Leverandøren |
| Nettverk/virtualisering | Virksomheten | Leverandøren | Leverandøren | Leverandøren |
| Operativsystem | Virksomheten | Virksomheten | Leverandøren | Leverandøren |
| Applikasjoner | Virksomheten | Virksomheten | Virksomheten | Leverandøren |
| Data | Virksomheten | Virksomheten | Virksomheten | Virksomheten* |

*Virksomheten er alltid ansvarlig for sine egne data, uansett tjenestemodell.

---

### Driftsmodeller: offentlig, privat og hybrid sky

**Offentlig sky (public cloud)**
Ressurser deles mellom mange kunder hos leverandøren. Billigst, mest skalerbart, men minst kontroll. Eksempler: Microsoft Azure, AWS, Google Cloud.

**Privat sky (private cloud)**
Dedikert sky for én organisasjon – enten hosted eksternt eller on-premise. Gir mer kontroll og kan tilfredsstille strenge compliance-krav. Dyrere enn offentlig sky.

**Hybrid sky**
Kombinasjon av offentlig og privat sky (og/eller on-premise). Gir fleksibilitet til å plassere arbeidsbelastninger der det passer best. Den vanligste modellen i norske bedrifter.

**Multi-sky (Multi-cloud)**
Bruk av flere offentlige skyleverandører parallelt (f.eks. Azure for e-post og AD, AWS for spesifikke tjenester). Reduserer risikoen for **vendor lock-in** og øker redundansen, men øker kompleksiteten i drift og administrasjon.

---

### Shared Responsibility Model

En viktig del av å jobbe med skytjenester er å forstå hvem som er ansvarlig for hva. Dette kalles *Shared Responsibility Model*:

- **Leverandøren** er alltid ansvarlig for den fysiske infrastrukturen (bygninger, servere, nettverk).
- **Kunden** er alltid ansvarlig for sine egne data og tilgangsstyring.
- Alt imellom avhenger av om man bruker IaaS, PaaS eller SaaS (se tabellen over).

Misforståelse av ansvarsmodellen er en vanlig årsak til sikkerhetsproblemer i skymiljøer. For mer om tilgangsstyring i sky, se [[bruker-og-tilgangsstyring]].

---

### Microsoft Azure og Amazon Web Services

De to største skyleverandørene globalt er Microsoft Azure og AWS (Amazon Web Services). Begge tilbyr alle tre tjenestemodellene og har datasentre over hele verden.

| Tjeneste | Azure | AWS |
|---------|-------|-----|
| Virtuelle maskiner | Azure Virtual Machines | EC2 |
| Fillagring | Azure Blob Storage | S3 |
| Databaser | Azure SQL, Cosmos DB | RDS, DynamoDB |
| Serverless | Azure Functions | AWS Lambda |
| Kubernetes | AKS | EKS |
| E-post/produktivitet | Microsoft 365 (SaaS) | AWS WorkMail |

**Azure** er særlig sterk i virksomheter som allerede bruker Microsoft-produkter (Windows Server, Active Directory, Teams).

**AWS** har det bredeste tjenesteutvalget globalt og er markedsleder målt i omsetning.

Norske skyleverandører som Telenor og Basefarm tilbyr alternativer for virksomheter med særskilte krav til **datasuverenitet** – prinsippet om at data er underlagt lovene i landet der de lagres fysisk.

---

### Fordeler og ulemper med sky

**Fordeler:**
- **Elastisitet** – skaleringsressurser opp og ned etter behov
- **Kostnadskontroll** – betaler kun for faktisk bruk (OPEX)
- **Global rekkevidde** – datasentre over hele verden gir lav latens
- **Høy tilgjengelighet** – leverandørene garanterer SLA (Service Level Agreement) på 99,9 % eller mer
- **Innebygd redundans** – data speilet mellom datasentre
- **Redusert vedlikeholdsansvar** – leverandøren tar seg av fysisk infrastruktur

**Ulemper:**
- **Avhengighet av internett** – ingen nett, ingen tilgang
- **Vendor lock-in** – vanskelig å bytte leverandør
- **Løpende kostnader** – kan bli dyrt over tid for store arbeidsbelastninger
- **GDPR og datasuverenitet** – se nedenfor

---

### FinOps – skyøkonomi i praksis

Sky-tjenester er fleksible, men kan føre til ukontrollerte kostnader hvis de ikke styres aktivt. **FinOps** (Cloud Financial Management) er en praksis for å forstå, kontrollere og optimalisere skykostnader i samarbeid mellom IT, finans og forretning.

Typiske tiltak:
- Slå av ubrukte ressurser automatisk (f.eks. test-servere om natten)
- Velg riktig størrelse (right-sizing) på virtuelle maskiner
- Bruk reserverte kapasiteter (Reserved Instances) for faste arbeidsbelastninger

---

### GDPR og datalagring i sky – norsk perspektiv

Personvernforordningen (GDPR) gjelder i Norge og stiller strenge krav til behandling og lagring av personopplysninger. Nøkkelspørsmål ved bruk av skytjenester:

- **Hvor lagres dataene?** EU/EØS-lagring er krav for personopplysninger uten spesielt grunnlag.
- **Hvem har tilgang?** Skyleverandøren og eventuelle underleverandører må behandle data i samsvar med GDPR.
- **Databehandleravtale** – det er lovpålagt å inngå en databehandleravtale med skyleverandøren.

Digdir (Digitaliseringsdirektoratet) anbefaler at offentlig sektor vurderer skytjenester, men alltid med en risikovurdering for personvern og datasuverenitet. Schrems II-dommen (2020) skapte usikkerhet rundt overføring av data til USA, noe som blant annet påvirket norske kommuners valg av skytjenester.

Både Microsoft Azure og AWS tilbyr europeiske datasentre (bl.a. i Norge, Sverige og Irland) og har inngått forpliktelser om å oppfylle GDPR. Se [[personvern]] for mer om GDPR-regelverket.

---

## Eksempel / lab

**Oppgave: Sammenlign tjenester i Azure og AWS**

1. Gå til [portal.azure.com](https://portal.azure.com) (eller bruk et gratis testabonnement).
2. Finn tjenesten «Virtual Machines» og noter hva du kan konfigurere.
3. Sammenlign med AWS EC2 på [aws.amazon.com/ec2](https://aws.amazon.com/ec2/).
4. Diskuter: Hva er likt? Hva er ulikt? Hvilken ville du valgt for en ny norsk skoleplattform og hvorfor?

**Tilleggsoppgave: Multi-sky og vendor lock-in**

Tenk deg at skolen bruker Microsoft 365 (SaaS), Azure Virtual Machines (IaaS) og Veeam Azure Backup. Diskuter: Hvilke av disse tjenestene er enklest å bytte til en annen leverandør? Hva er risikoene ved å «låse seg» til én leverandør?

---

## Study guide

### Kjerneinnhold

Skytjenester handler om å leie IT-ressurser over internett i stedet for å eie dem selv.

**De tre tjenestemodellene:**
- **IaaS** – leier infrastruktur; ansvarlig for OS og opp (Azure VMs, AWS EC2)
- **PaaS** – leverandøren håndterer OS; du fokuserer på applikasjoner (Azure App Service)
- **SaaS** – ferdig programvare; leverandøren håndterer alt (Microsoft 365, Zoom)

**Driftsmodeller:**
- **Public cloud** – delt ressurspool, billigst, minst kontroll
- **Private cloud** – dedikert, mer kontroll, dyrere
- **Hybrid** – kombinasjon, vanligst i Norge
- **Multi-cloud** – flere leverandører, reduserer vendor lock-in

**Nøkkelprinsipper:**
- Shared Responsibility Model: vet du hvem som er ansvarlig for hva i din løsning?
- GDPR og datasuverenitet: data om norske borgere bør ligge i EU/EØS
- Elastisitet og SLA: skyleverandørene garanterer 99,9 %+ oppetid
- FinOps: sky-kostnader må styres aktivt

**Husk:** Virksomheten er alltid ansvarlig for sine egne data – uansett om de ligger i IaaS, PaaS eller SaaS.

---

## FAQ

**Hva er egentlig forskjellen på IaaS, PaaS og SaaS i praksis?**
IaaS er som å leie en tomt og bygge huset selv. PaaS er som å leie et hus ferdig bygget, men du møblerer det selv. SaaS er som å leie et hotellrom – alt er klart, du bare sjekker inn. Jo høyere opp i modellen, jo mindre kontroll, men jo enklere å komme i gang.

**Hva betyr vendor lock-in og hvordan unngår man det?**
Vendor lock-in betyr at systemene er så tett integrert med én leverandørs plattform at det er svært kostbart å bytte. Man unngår det ved å bruke åpne standarder, containere (som kan kjøre hos alle leverandører), og multi-cloud-strategi.

**Er Microsoft 365 IaaS, PaaS eller SaaS?**
Microsoft 365 er SaaS. Du bruker ferdig programvare (Word, Teams, Exchange) over nett, og Microsoft håndterer alt fra servere til oppdateringer.

**Hva er en databehandleravtale og er den lovpålagt?**
Ja. Etter GDPR er det lovpålagt å inngå en databehandleravtale (DPA) med enhver tjenesteleverandør som behandler personopplysninger på din side. Alle store skyleverandører tilbyr standardiserte DPA-er.

**Kan vi bruke Azure eller AWS i en norsk skole?**
Ja, under forutsetning av at dataene lagres i EU/EØS (noe begge leverandørene tilbyr), at det er inngått databehandleravtale, og at det er gjort en personvernkonsekvensvurdering (DPIA) for sensitive data.

**Hva er serverless og er det praktisk for IT-drift?**
Serverless (f.eks. Azure Functions) er ikke at det ikke finnes servere – det er at du ikke trenger å tenke på dem. Du skriver en funksjon, og leverandøren kjører den og skalerer automatisk. Det er svært kostnadseffektivt for arbeidsoppgaver som kjøres av og til, ikke kontinuerlig.

---

## Quiz

<details><summary>Spørsmål 1: Hva skiller IaaS fra PaaS?</summary>

**Svar:** Ved IaaS leier du infrastruktur (servere, lagring, nettverk) og er selv ansvarlig for operativsystem og alt over. Ved PaaS håndterer leverandøren også operativsystem og mellomvare – du fokuserer kun på applikasjonsutvikling og data.

</details>

<details><summary>Spørsmål 2: Hva er Shared Responsibility Model?</summary>

**Svar:** En modell som beskriver ansvarsdelingen mellom skyleverandøren og kunden. Leverandøren er alltid ansvarlig for fysisk infrastruktur; kunden er alltid ansvarlig for data og tilgangsstyring. Alt imellom avhenger av tjenestemodell (IaaS/PaaS/SaaS).

</details>

<details><summary>Spørsmål 3: Hva er et SLA?</summary>

**Svar:** SLA (Service Level Agreement) er en avtale mellom leverandøren og kunden om hvilken tilgjengelighet og ytelse som garanteres. For eksempel kan en skyleverandør garantere 99,9 % oppetid per måned.

</details>

<details><summary>Spørsmål 4: Hvorfor er GDPR viktig å vurdere ved bruk av skytjenester?</summary>

**Svar:** GDPR stiller krav til behandling og lagring av personopplysninger. Virksomheter må sikre at data lagres i samsvar med loven (f.eks. innenfor EU/EØS), at det er inngått databehandleravtale med skyleverandøren, og at det er gjort risikovurdering for personvern.

</details>

<details><summary>Spørsmål 5: Hva er vendor lock-in, og hvorfor er det en ulempe med sky?</summary>

**Svar:** Vendor lock-in betyr at systemene er så tett integrert med én leverandørs teknologi at det blir kostbart og vanskelig å bytte. For eksempel kan en virksomhet som har investert mye i Azure-spesifikke tjenester ikke enkelt flytte til AWS uten stor innsats.

</details>

---

## Flashcards

IaaS :: Infrastructure as a Service – leie av virtuell infrastruktur (servere, lagring, nettverk). Kunden styrer OS og opp. Eksempel: AWS EC2, Azure Virtual Machines.

PaaS :: Platform as a Service – leverandøren håndterer OS og mellomvare. Kunden fokuserer på applikasjonsutvikling. Eksempel: Azure App Service.

SaaS :: Software as a Service – ferdig programvare levert over nett. Leverandøren håndterer alt. Eksempel: Microsoft 365, Google Workspace.

Offentlig sky :: Sky-ressurser delt mellom mange kunder hos leverandøren. Billigst og mest skalerbart. Eksempel: Azure, AWS.

Privat sky :: Dedikert sky for én organisasjon. Mer kontroll, men dyrere.

Hybridsky :: Kombinasjon av offentlig og privat sky (og/eller on-premise). Gir fleksibilitet.

Shared Responsibility Model :: Ansvarsmodell som fordeler sikkerhetsansvar mellom leverandøren og kunden avhengig av tjenestemodell.

SLA :: Service Level Agreement – avtale om garantert tilgjengelighet og ytelse. F.eks. 99,9 % oppetid.

GDPR :: Personvernforordningen – EU-lov som regulerer behandling av personopplysninger. Gjelder i Norge.

Databehandleravtale :: Lovpålagt avtale mellom virksomheten og skyleverandøren som regulerer behandling av personopplysninger.

Elastisitet :: Evnen til å skalere ressurser opp og ned etter behov – en nøkkelfordel med sky.

OPEX :: Operational Expenditure – løpende kostnader. Sky bruker OPEX-modell (betal for bruk).

Multi-sky (Multi-cloud) :: Bruk av flere offentlige skyleverandører for å unngå vendor lock-in og øke redundansen.

Serverless :: PaaS-variant der leverandøren automatisk tildeler ressurser basert på kodekjøring. Ingen serveradministrasjon. Eksempel: Azure Functions.

Hyperscalere :: De største skyleverandørene (AWS, Azure, Google Cloud) med enorm global infrastruktur og kapasitet.

Datasuverenitet :: Prinsippet om at data er underlagt lovene i landet der de lagres fysisk. Kritisk for GDPR-overholdelse.

FinOps :: Cloud Financial Management – praksis for å forstå og optimalisere skykostnader i samarbeid mellom IT og økonomi.

---

## Ressurser

- [AWS: What is cloud computing?](https://aws.amazon.com/what-is-cloud-computing/)
- [Microsoft Azure: Hva er IaaS?](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-iaas/)
- [Microsoft Learn AZ-900: PaaS](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/3-describe-platform-service)
- [Digdir: Skytjenester i offentlig sektor](https://www.digdir.no/nasjonal-arkitektur/skytjenester/2153)
- [NDLA: Hva er skytjenester? (video)](https://ndla.no/resource:46761)
- [[driftsarkitektur]]
- [[baerekraft]]
- [[personvern]]
- [[virtuelle-losninger]]
- [[backup-og-gjenoppretting]]
