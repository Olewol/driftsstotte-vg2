---
title: "Driftsarkitektur"
emne: it-drift
kompetansemaal:
  - km-01
  - km-03
kilder:
  - ndla
tags: []
flashcards: true
public: true
---

## Introduksjon

En driftsarkitektur beskriver hvordan en virksomhets IT-infrastruktur er bygget opp – hvilke komponenter som finnes, hvordan de henger sammen, og hvor de er plassert. En gjennomtenkt arkitektur gjør systemet stabilt, sikkert og skalerbart.

I dag finnes tre hovedmodeller: lokal infrastruktur (on-premise), skybasert infrastruktur, og en kombinasjon av begge (hybrid). Valget avhenger av krav til kontroll, kostnad, fleksibilitet og lovpålegg.

---

## Teori

### On-premise, sky og hybrid

**On-premise** betyr at all infrastruktur er plassert lokalt – i virksomhetens egne rom eller leide serverrom. Virksomheten eier og drifter alt selv: servere, nettverk, lagring og programvare.

- Fordeler: full kontroll, forutsigbare kostnader over tid, ingen avhengighet av internettforbindelse
- Ulemper: høye investeringskostnader (CAPEX), krever kompetanse internt, skalering tar tid

**Skybasert infrastruktur (public cloud)** betyr at ressurser leies av en ekstern skyleverandør (Microsoft Azure, Amazon Web Services, Google Cloud). Virksomheten betaler for det den bruker (OPEX-modell).

- Fordeler: elastisk skalering, betaler kun for bruk, lavt vedlikeholdsansvar
- Ulemper: løpende kostnader, avhengighet av leverandør og internett, spørsmål om datalagring og GDPR

**Hybrid sky** kombinerer on-premise og sky. Kritiske data og tjenester kan ligge lokalt, mens variable arbeidsbelastninger kjøres i skyen. Dette er den vanligste modellen for mellomstore og store norske virksomheter i dag.

> Koblingen til km-03: Skytjenester er en integrert del av moderne driftsarkitektur. IaaS (Infrastructure as a Service) er i praksis en forlengelse av on-premise – man leier virtuelle maskiner og nettverk i stedet for å eie fysisk utstyr. Se [[skytjenester]] for en fullstendig gjennomgang.

---

### Servere: fysiske og virtuelle

En **fysisk server** er dedikert maskinvare som kjører ett eller flere operativsystemer. I et datasenter plasseres servere i **rack** (metallstativer), og mange rack samles i en serversal.

**Virtualisering** gjør det mulig å kjøre flere virtuelle maskiner (VM-er) på én fysisk server. En **hypervisor** er programvaren som administrerer VM-ene. De vanligste hypervisorene er:

- **VMware ESXi** – industristandard, mye brukt i bedrifter
- **Microsoft Hyper-V** – innebygget i Windows Server
- **KVM** – åpen kildekode, brukt i Linux-miljøer

Virtualisering gir bedre ressursutnyttelse, enklere administrasjon og raskere utrulling av nye servere.

**Containere** (f.eks. Docker) er en lettere form for virtualisering som deler operativsystemkjernen mellom applikasjoner. Kubernetes brukes til å orkestrere containere i stor skala.

---

### Nettverkskomponenter

Et lokalt nettverk (LAN) består av flere nøkkelkomponenter:

| Komponent | Funksjon |
|-----------|----------|
| **Svitsj (switch)** | Kobler enheter i et lokalt nettverk. Opererer på lag 2 (MAC-adresser). |
| **Ruter** | Kobler ulike nettverk. Opererer på lag 3 (IP-adresser). Sender trafikk mellom LAN og WAN. |
| **Brannmur** | Kontrollerer og filtrerer nettverkstrafikk basert på regler. Første forsvarslinje mot angrep. |
| **DMZ** | Demilitarisert sone – et isolert nettverkssegment for tjenester som er tilgjengelige fra internett (f.eks. webserver). |
| **VLAN** | Logisk segmentering av nettverket uten fysisk separasjon. Brukes for sikkerhet og ytelse. |
| **Trådløst aksesspunkt (AP)** | Gir Wi-Fi-tilgang til nettverket. |

---

### Lagringstyper

Lagring er en kritisk del av driftsarkitekturen. De tre hovedtypene er:

**DAS – Direct Attached Storage**
Lagring som er koblet direkte til én server (f.eks. intern harddisk eller ekstern disk over USB/SAS). Enkel og rask, men kan ikke deles mellom servere.

**NAS – Network Attached Storage**
En dedikert lagringsenhet tilkoblet nettverket. Alle servere og klienter i nettverket kan nå filer via protokoller som SMB (Windows) eller NFS (Linux). Typisk brukt til fildeling og backup.

**SAN – Storage Area Network**
Et dedikert høyhastighetsnettverk for lagring, separat fra det vanlige datanettverket. Bruker protokoller som Fibre Channel eller iSCSI. Gir svært rask tilgang og brukes i virksomheter med høye ytelseskrav (f.eks. databaser).

**Objektlagring i sky**
Lagring i skyen (f.eks. Azure Blob Storage, AWS S3) egner seg for store mengder ustrukturerte data som bilder, videoer og backup. Svært skalerbart og kostnadseffektivt.

---

### Klientutstyr

Sluttbrukernes utstyr kalles klientutstyr og inkluderer:
- PC-er og bærbare datamaskiner
- Nettbrett og mobiltelefoner (BYOD – Bring Your Own Device)
- Tynne klienter (thin clients) – billige enheter som kobler til en terminalserver

---

### UPS og redundans

**UPS (Uninterruptible Power Supply)** er et batterisystem som gir strøm ved strømbrudd. Det sikrer at servere og nettverksutstyr kan slå seg ned kontrollert – eller fortsette å kjøre – når strømmen går.

**Redundans** betyr at kritiske komponenter finnes i duplikat, slik at systemet fortsetter å fungere om én komponent feiler:
- Redundante strømforsyninger i servere
- Redundante nettverkskoblinger (bonding/failover)
- RAID (Redundant Array of Independent Disks) for lagring
- Redundante internettforbindelser fra ulike leverandører

---

### Typisk arkitektur for en SMB

En liten til mellomstor bedrift (SMB – Small and Medium Business) kan ha en slik arkitektur:

```
[Internett]
     |
[Brannmur/ruter]
     |
[Kjernesvitsj]
  /       \
[Server-VLAN]   [Klient-VLAN]
  |               |
[Virtuelle     [PC-er, bærbare,
 servere,       printere]
 NAS, UPS]
```

I tillegg kan noen tjenester ligge i skyen (f.eks. e-post via Microsoft 365, backup til Azure), noe som gir en hybrid arkitektur.

---

## Eksempel / lab

**Oppgave: Kartlegg arkitekturen på skolen**

1. Finn ut hvilke nettverkskomponenter som finnes på skolen (svitsj, ruter, brannmur).
2. Er det noen tjenester som kjøres i skyen? (f.eks. Microsoft 365, Google Workspace)
3. Tegn en forenklet arkitekturskisse i draw.io eller på papir.
4. Identifiser hvilken type lagring som brukes for filserveren (DAS, NAS eller SAN).

---

## Quiz

<details><summary>Spørsmål 1: Hva er forskjellen på CAPEX og OPEX i forbindelse med IT-drift?</summary>

**Svar:** CAPEX (Capital Expenditure) er store engangsutgifter til kjøp av utstyr og infrastruktur, typisk for on-premise. OPEX (Operational Expenditure) er løpende driftsutgifter, typisk for sky-tjenester der man betaler månedlig for det man bruker.

</details>

<details><summary>Spørsmål 2: Hva gjør en hypervisor?</summary>

**Svar:** En hypervisor er programvare som lar én fysisk server kjøre flere virtuelle maskiner (VM-er) samtidig. Den fordeler ressurser (CPU, minne, lagring) mellom VM-ene og isolerer dem fra hverandre.

</details>

<details><summary>Spørsmål 3: Hva er forskjellen på NAS og SAN?</summary>

**Svar:** NAS (Network Attached Storage) er en filserver tilkoblet det vanlige nettverket og tilbyr fildeling via SMB/NFS. SAN (Storage Area Network) er et dedikert høyhastighetsnettverk for lagring som gir serverne blokkbasert tilgang – som om disken var lokalt montert. SAN er raskere og brukes til ytelseskrevende applikasjoner.

</details>

<details><summary>Spørsmål 4: Hva er en DMZ i nettverksarkitektur?</summary>

**Svar:** DMZ (Demilitarisert sone) er et isolert nettverkssegment mellom internett og det interne nettverket. Tjenester som skal være tilgjengelige fra internett (f.eks. webservere) plasseres her, slik at et angrep mot disse ikke gir direkte tilgang til det interne nettverket.

</details>

<details><summary>Spørsmål 5: Hva er hybridsky og hvorfor er det vanlig i norske virksomheter?</summary>

**Svar:** Hybridsky kombinerer lokal on-premise infrastruktur med offentlige skytjenester. Det er vanlig fordi det gir fleksibilitet: sensitive data og systemer med strenge GDPR-krav kan ligge lokalt, mens skalerbare tjenester og backup kan ligge i skyen. Det gir også kostnadsoptimalisering.

</details>

---

## Flashcards

On-premise :: Lokal IT-infrastruktur eid og driftet av virksomheten selv, med full kontroll men høye investeringskostnader (CAPEX).

Hybridsky :: En driftsmodell som kombinerer lokal (on-premise) infrastruktur med skytjenester.

Hypervisor :: Programvare som lar én fysisk server kjøre flere virtuelle maskiner (VM-er) samtidig. Eksempler: VMware ESXi, Hyper-V.

VM (virtuell maskin) :: En programvarebasert server som oppfører seg som en fysisk maskin, men kjører på delt fysisk maskinvare.

NAS :: Network Attached Storage – lagringsenhet tilkoblet nettverket for fildeling. Tilgjengelig for alle enheter i nettverket.

SAN :: Storage Area Network – dedikert høyhastighetsnettverk for lagring. Gir servere blokkbasert tilgang til lagring.

DAS :: Direct Attached Storage – lagring koblet direkte til én server. Enkel og rask, men ikke delt.

Svitsj :: Nettverkskomponent som kobler enheter i et lokalt nettverk (LAN) ved hjelp av MAC-adresser.

Brannmur :: Nettverkssikkerhetskomponent som filtrerer trafikk inn og ut av nettverket basert på regler.

VLAN :: Virtual LAN – logisk segmentering av et nettverk uten fysisk separasjon, brukt for sikkerhet og ytelse.

UPS :: Uninterruptible Power Supply – batterisystem som sikrer strøm ved strømbrudd og beskytter mot uplanlagt nedstengning.

CAPEX :: Capital Expenditure – engangsutgifter til kjøp av utstyr. Typisk for on-premise infrastruktur.

OPEX :: Operational Expenditure – løpende driftsutgifter. Typisk for skytjenester med abonnementsmodell.

---

## Ressurser

- [Microsoft Azure: Hva er IaaS?](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-iaas/)
- [Microsoft Learn AZ-900: IaaS](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/2-describe-infrastructure-service)
- [AWS: What is cloud computing?](https://aws.amazon.com/what-is-cloud-computing/)
- [[skytjenester]]
- [[backup-og-gjenoppretting]]
- [[dokumentasjon-og-planlegging]]
