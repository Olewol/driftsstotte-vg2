---
title: "Skytjenester"
emne: it-drift
kompetansemaal:
  - km-03
kilder:
  - ndla
tags: []
flashcards: true
public: true
---

## Introduksjon

Skyberegning (cloud computing) har endret måten virksomheter bygger og drifter IT-systemer. I stedet for å eie og vedlikeholde egne servere kan en virksomhet leie datakraft, lagring og programvare over internett – og betale kun for det de bruker.

AWS definerer det slik: *"Cloud computing is the on-demand delivery of IT resources over the Internet with pay-as-you-go pricing."*

I dag bruker de fleste virksomheter en eller annen form for skytjeneste, fra e-post og fillagring til fullstendige serverinfrastrukturer. Å forstå de ulike tjenestemodellene og driftsmodellene er en grunnleggende kompetanse i IT-faget.

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

---

### Shared Responsibility Model

En viktig del av å jobbe med skytjenester er å forstå hvem som er ansvarlig for hva. Dette kalles *Shared Responsibility Model*:

- **Leverandøren** er alltid ansvarlig for den fysiske infrastrukturen (bygninger, servere, nettverk).
- **Kunden** er alltid ansvarlig for sine egne data og tilgangsstyring.
- Alt imellom avhenger av om man bruker IaaS, PaaS eller SaaS (se tabellen over).

Misforståelse av ansvarsmodellen er en vanlig årsak til sikkerhetsproblemer i skymiljøer.

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

### GDPR og datalagring i sky – norsk perspektiv

Personvernforordningen (GDPR) gjelder i Norge og stiller strenge krav til behandling og lagring av personopplysninger. Nøkkelspørsmål ved bruk av skytjenester:

- **Hvor lagres dataene?** EU/EØS-lagring er krav for personopplysninger uten spesielt grunnlag.
- **Hvem har tilgang?** Skyleverandøren og eventuelle underleverandører må behandle data i samsvar med GDPR.
- **Databehandleravtale** – det er lovpålagt å inngå en databehandleravtale med skyleverandøren.

Digdir (Digitaliseringsdirektoratet) anbefaler at offentlig sektor vurderer skytjenester, men alltid med en risikovurdering for personvern og datasuverenitet. Schrems II-dommen (2020) skapte usikkerhet rundt overføring av data til USA, noe som blant annet påvirket norske kommuners valg av skytjenester.

Både Microsoft Azure og AWS tilbyr europeiske datasentre (bl.a. i Norge, Sverige og Irland) og har inngått forpliktelser om å oppfylle GDPR.

---

## Eksempel / lab

**Oppgave: Sammenlign tjenester i Azure og AWS**

1. Gå til [portal.azure.com](https://portal.azure.com) (eller bruk et gratis testabonnement).
2. Finn tjenesten «Virtual Machines» og noter hva du kan konfigurere.
3. Sammenlign med AWS EC2 på [aws.amazon.com/ec2](https://aws.amazon.com/ec2/).
4. Diskuter: Hva er likt? Hva er ulikt? Hvilken ville du valgt for en ny norsk skoleplattform og hvorfor?

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

---

## Ressurser

- [AWS: What is cloud computing?](https://aws.amazon.com/what-is-cloud-computing/)
- [Microsoft Azure: Hva er IaaS?](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-iaas/)
- [Microsoft Learn AZ-900: PaaS](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/3-describe-platform-service)
- [Digdir: Referansearkitektur for datadeling](https://www.digdir.no/nasjonal-arkitektur/referansearkitektur-for-datadeling/2131)
- [[driftsarkitektur]]
- [[baerekraft]]
