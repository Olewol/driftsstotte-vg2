---
title: "Driftsarkitektur"
emne: it-drift
kompetansemaal:
  - km-01
  - km-03
kilder:
  - ndla
  - https://ndla.no/nb/subject:1:34375b6a-9a99-4d64-884d-2a3164a27521/topic:2:183915/resource:1:160358
  - https://snl.no/skytjeneste
video: https://www.youtube.com/watch?v=mxT23V-pS0I
tags: []
flashcards: https://notebooklm.google.com/notebook/bc9a5656-7a9b-4dc5-a59e-ef4a96aa8ccd
public: true
notebooklm: true
---

## Introduksjon

En driftsarkitektur beskriver hvordan en virksomhets IT-infrastruktur er bygget opp – hvilke komponenter som finnes, hvordan de henger sammen, og hvor de er plassert. En gjennomtenkt arkitektur gjør systemet stabilt, sikkert og skalerbart.

I dag finnes tre hovedmodeller: lokal infrastruktur (on-premise), skybasert infrastruktur, og en kombinasjon av begge (hybrid). Valget avhenger av krav til kontroll, kostnad, fleksibilitet og lovpålegg. En god driftsarkitektur tar alltid hensyn til hvem som er ansvarlig for hva – noe som er særlig viktig når tjenester flyttes til skyen (se [[skytjenester]] for Shared Responsibility Model).

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

Virtualisering gir bedre ressursutnyttelse, enklere administrasjon og raskere utrulling av nye servere. Se [[virtuelle-losninger]] for en dypere gjennomgang av virtualiseringsteknologi.

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

Se [[brannmur]] og [[segmentering-og-vlan]] for mer om disse komponentene.

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

### Infrastruktur som kode (IaC)

Moderne driftsarkitektur handler ikke bare om hvilke komponenter som finnes – det handler også om hvordan de konfigureres og vedlikeholdes. **Infrastruktur som kode (IaC)** er en metode der IT-infrastruktur beskrives og styres via maskinlesbare konfigurasjonsfiler i stedet for manuell konfigurering.

Fordeler med IaC:
- Reproduserbar infrastruktur – samme konfigurasjon gir alltid samme resultat
- Versjonskontroll – endringer spores som kode
- Automatisert utrulling – raskere og mer pålitelig enn manuelt arbeid

Verktøy: Terraform (infrastruktur), Ansible (konfigurasjon), Azure ARM-maler. Se [[automatisering]] for mer.

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

I tillegg kan noen tjenester ligge i skyen (f.eks. e-post via Microsoft 365, backup til Azure), noe som gir en hybrid arkitektur. God [[dokumentasjon-og-planlegging]] sikrer at alle komponenter er kartlagt og at endringer spores.

---

## Eksempel / lab

**Oppgave: Kartlegg arkitekturen på skolen**

1. Finn ut hvilke nettverkskomponenter som finnes på skolen (svitsj, ruter, brannmur).
2. Er det noen tjenester som kjøres i skyen? (f.eks. Microsoft 365, Google Workspace)
3. Tegn en forenklet arkitekturskisse i draw.io eller på papir.
4. Identifiser hvilken type lagring som brukes for filserveren (DAS, NAS eller SAN).

**Tilleggsoppgave: Vurder IaC**

Se på et eksempel på en Azure ARM-mal eller Terraform-konfigurasjon (finnes mange åpne eksempler på GitHub). Diskuter: Hva er fordelen med å beskrive infrastruktur som kode kontra å konfigurere manuelt i et webgrensesnitt?

---

## Study guide

### Kjerneinnhold

Driftsarkitektur handler om hvordan IT-systemer er bygget opp og hvilke valg som tas for plassering, skalering og sikring av infrastruktur.

**De tre modellene:**
- **On-premise** – full kontroll, høy CAPEX, ingen avhengighet av internett
- **Public cloud** – elastisk, OPEX-modell, avhengig av leverandør
- **Hybrid** – kombinasjon, mest utbredt i norske virksomheter

**Servere og virtualisering:**
- Hypervisor muliggjør flere VM-er på én fysisk server (VMware, Hyper-V, KVM)
- Containere (Docker/Kubernetes) er lettere enn VM-er og deler OS-kjernen
- IaC automatiserer og versjonskontrollerer infrastrukturoppsettet

**Nettverkskomponenter:**
- Svitsj (lag 2), ruter (lag 3), brannmur (filtrering), VLAN (segmentering), DMZ (offentlige tjenester)
- Redundans og UPS sikrer kontinuitet ved feil

**Lagring:**
- DAS (direkte tilkoblet, kun én server), NAS (nettverksdeling, SMB/NFS), SAN (høyhastighets blokklagring, Fibre Channel/iSCSI)
- Objektlagring i sky for ustrukturerte data og backup

**Husk:** CAPEX vs. OPEX er ikke bare en kostnadsbeslutning – det er en strategisk beslutning om kontroll, fleksibilitet og risiko. Hybridsky er en bevisst kombinasjon, ikke en kompromissløsning.

---

## FAQ

**Hva er egentlig forskjellen på en svitsj og en ruter?**
En svitsj kobler enheter innenfor samme nettverk ved hjelp av MAC-adresser (lag 2). En ruter kobler ulike nettverk og sender trafikk basert på IP-adresser (lag 3). I praksis: svitsjen kobler PC-er i klasserommet, ruteren sender trafikk fra klasserommet ut på internett.

**Hvorfor velger mange virksomheter hybrid sky i stedet for kun sky eller kun on-premise?**
Hybrid sky gir fleksibilitet: sensitive data og systemer med strenge GDPR-krav kan ligge lokalt, mens skalerbare og variable tjenester kan kjøre i skyen. Det er også enklere å migrere gradvis enn å flytte alt på én gang.

**Hva er RAID og hva beskytter det mot?**
RAID (Redundant Array of Independent Disks) er en teknologi som sprer data over flere harddisker for redundans og/eller ytelse. RAID 1 speiler data (én disk kan feile uten tap). RAID 5/6 kombinerer ytelse og feiltoleranse. RAID er ikke en backup – det beskytter mot diskfeil, ikke mot feil sletting eller ransomware.

**Hva menes med «latens» og hvorfor er det viktig i arkitekturvalg?**
Latens er forsinkelsen i kommunikasjon mellom klient og server. En applikasjon som krever rask respons (f.eks. et lagersystem i sanntid) bør ha lav latens – noe som kan tale for lokal hosting fremfor sky. Valg av skyregion (nærhet til brukerne) reduserer latens.

**Hva er IaC og er det relevant for VG2-nivå?**
Infrastruktur som kode (IaC) er å beskrive serveroppsett og nettverkskonfigurasjon i tekstfiler som kan versjonskontrolleres og kjøres automatisk. Det er relevant fordi det er standarden i moderne IT-drift – selv om man ikke koder selv, er det viktig å forstå prinsippet og se at «manuell klikking» er på vei ut.

**Hva er DMZ og hvorfor er det viktig?**
DMZ (Demilitarisert sone) er et isolert nettverk mellom internett og det interne nettverket. Tjenester som webservere og e-postservere, som skal være tilgjengelige fra internett, plasseres her. Slik er et kompromiss av en DMZ-server ikke automatisk inngangsbillett til det interne nettverket.

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

Infrastruktur som kode (IaC) :: Metode for å styre IT-infrastruktur via maskinlesbare konfigurasjonsfiler i stedet for manuell konfigurering. Gir reproduserbarhet og versjonskontroll.

Redundans :: Dublering av kritiske komponenter i et system for å sikre drift hvis én del svikter.

Latens :: Forsinkelsen i kommunikasjon mellom klient og server. Lav latens er kritisk for sanntidssystemer.

---

## Ressurser

- [Microsoft Azure: Hva er IaaS?](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-iaas/)
- [Microsoft Learn AZ-900: IaaS](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/2-describe-infrastructure-service)
- [AWS: What is cloud computing?](https://aws.amazon.com/what-is-cloud-computing/)
- [NDLA: Driftsarkitektur](https://ndla.no/nb/subject:1:34375b6a-9a99-4d64-884d-2a3164a27521/topic:2:183915/resource:1:160358)
- [SNL: Skytjeneste](https://snl.no/skytjeneste)
- [YouTube: What is Cloud Computing? – Amazon Web Services](https://www.youtube.com/watch?v=mxT23V-pS0I)
- [[skytjenester]]
- [[backup-og-gjenoppretting]]
- [[dokumentasjon-og-planlegging]]
