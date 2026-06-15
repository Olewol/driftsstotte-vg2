---
title: "IT-drift – oversikt"
emne: it-drift
kompetansemaal:

  - km-01
  - km-03
  - km-06
  - km-12

kilder:

  - ndla
  - <https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/>
  - <https://www.digdir.no/nasjonal-arkitektur/skytjenester/2153>
  - <https://learn.microsoft.com/en-us/azure/architecture/framework/>
  - <https://snl.no/skytjeneste>

tags: []
flashcards: false
public: true
---

## Introduksjon

IIT-drift handler om å forvalte, vedlikeholde og sikre at IT-systemer, nettverk og infrastruktur fungerer stabilt og
IIeffektivt over tid. Det er den daglige driften som holder en virksomhet i gang – fra at servere er oppe og kjører, til
Iat brukerne får tilgang til programmene de trenger.

II faget Driftsstøtte VG2 (ITK02-01) lærer du å forstå og jobbe med de viktigste delene av IT-drift: hvordan
IIinfrastruktur er bygget opp, hva skytjenester er, hvordan data beskyttes, hvordan man dokumenterer arbeid, og hva
Ibransjen gjør for å bli mer bærekraftig.

---

## Hva er IT-drift?

IIT-drift (på engelsk:*IT operations*eller*ITOps*) er alle aktiviteter som sikrer at IT-miljøet i en virksomhet fungerer
Isom det skal. Typiske arbeidsoppgaver inkluderer:

-**Overvåking**– sjekke at servere, nettverk og tjenester er tilgjengelige
-**Oppdateringer og patchhåndtering**– holde programvare og operativsystemer oppdatert
-**Feilsøking og brukerstøtte**– løse problemer når noe går galt
-**Sikkerhetskopiering**– ta regelmessige backup og verifisere at de kan gjenopprettes
-**Kapasitetsplanlegging**– vurdere om ressursene (lagring, prosessorkraft, båndbredde) er tilstrekkelige
-**Dokumentasjon og endringslogging**– holde oversikt over hva som er gjort og hvorfor

EEt driftsteam kan bestå av systemadministratorer, nettverksteknikere, sikkerhetsspesialister og brukerstøtte.
EI mindre virksomheter kan én person ha alle disse rollene.

---

## Emner i dette faget

Dette emnet er delt inn i fem fagartikler som bygger på hverandre:

|| Artikkel | Tema | Kompetansemål |
|| ---------- | ------ | --------------- |
|| [[driftsarkitektur]] | Infrastruktur, servere, nettverk, sky | km-01, km-03 |
|| [[skytjenester]] | IaaS, PaaS, SaaS, skyleverandører | km-03 |
|| [[backup-og-gjenoppretting]] | 3-2-1, RPO/RTO, gjenoppretting | km-01 |
|| [[dokumentasjon-og-planlegging]] | IP-plan, topologi, driftslogg | km-06 |
|| [[baerekraft]] | Energiforbruk, PUE, e-avfall | km-12 |

### Sammenheng mellom emnene

EEn god driftsarkitektur ([[driftsarkitektur]]) er grunnmuren – den definerer hvilke fysiske og virtuelle komponenter
EEvirksomheten bruker. Skytjenester ([[skytjenester]]) er en sentral del av moderne arkitektur og endrer måten vi tenker
EEpå infrastruktur. Backup og gjenoppretting ([[backup-og-gjenoppretting]]) sørger for at data overlever feil og angrep.
EEAlt dette forutsetter god dokumentasjon ([[dokumentasjon-og-planlegging]]) for at teamet skal kunne jobbe effektivt og
EEstrukturert. Til slutt ser vi på hva IT-bransjen gjør – og bør gjøre – for å redusere miljøpåvirkningen
E([[baerekraft]]).

---

## Kobling til kompetansemålene

*## km-01 – Utforske og beskrive komponenter i en driftsarkitektur
HHandler om å forstå hva en IT-infrastruktur består av: servere, nettverk, lagring, klientutstyr og hvordan disse henger
Hsammen. Se [[driftsarkitektur]] og [[backup-og-gjenoppretting]].

*## km-03 – Gjøre rede for prinsipper og strukturer for skytjenester og virtuelle tjenester
HHandler om å forstå sky-modellene IaaS, PaaS og SaaS, og hva virtualisering er. Se [[skytjenester]] og
H[[driftsarkitektur]].

*## km-06 – Planlegge og dokumentere arbeidsprosesser og IT-løsninger
HHandler om å lage IP-planer, nettverkstopologier, driftslogs og prosedyredokumentasjon.
HSe [[dokumentasjon-og-planlegging]].

*## km-12 – Utforske dataindustriens miljøavtrykk og vurdere bærekraftige tiltak
Handler om energiforbruk i datasentre, PUE, e-avfall og tiltak for grønnere IT. Se [[baerekraft]].

---

## Norsk kontekst

II Norge er IT-drift regulert av blant annet personvernlovgivningen (GDPR), Nasjonal sikkerhetsmyndighets (NSM)
IIanbefalinger, og Digitaliseringsdirektoratets (Digdir) retningslinjer. Digdir har utarbeidet referansearkitektur for
Idatadeling som gjelder offentlig sektor og setter krav til dokumentasjon og interoperabilitet.

NNorske virksomheter bruker både lokale datasentre og internasjonale skyleverandører som Microsoft Azure og Amazon Web
NServices. Valget av løsning avhenger av krav til ytelse, kostnad, lovpålegg og bærekraft.

---

## Ressurser

- [AWS: What is cloud computing?](<https://aws.amazon.com/what-is-cloud-computing/>)
- [Digdir: Referansearkitektur for datadeling](<https://www.digdir.no/nasjonal-arkitektur/referansearkitektur-for-datadeling/2131>)
- [[driftsarkitektur]]
- [[skytjenester]]
- [[backup-og-gjenoppretting]]
- [[dokumentasjon-og-planlegging]]
- [[baerekraft]]
