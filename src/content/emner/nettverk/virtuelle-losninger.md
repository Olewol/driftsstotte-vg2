---
title: "Virtuelle løsninger"
emne: nettverk
kompetansemaal:
  - km-02
kilder:
  - ndla
  - https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/hyper-v-technology-overview
tags: [virtualisering, hyper-v, virtualbox, hypervisor, vm, nettverk]
flashcards: https://notebooklm.google.com/notebook/f7e5ad6c-7082-40cf-abd5-7a41b540f8e1
public: true
video: https://www.youtube.com/watch?v=GidreS70z0U
notebooklm: true
---

# Virtuelle løsninger

## Introduksjon

Virtualisering er en av de mest transformative teknologiene i moderne IT-drift. I stedet for å kjøpe én fysisk server per tjeneste, kan man kjøre ti, tjue eller hundre virtuelle servere på én fysisk maskin — med full isolasjon mellom dem. For driftstøtter er virtualisering grunnleggende: det er slik de fleste bedriftsservere og nettverksinfrastrukturer i dag er bygd opp.

Virtuelle løsninger henger tett sammen med [[segmentering-og-vlan]], siden virtuelle svitsjer støtter VLAN-tagging (IEEE 802.1Q) for å integrere VM-er i segmenterte nettverk. I større produksjonsmiljøer inngår virtualisering som et sentralt element i [[driftsarkitektur]].

## Teori

### Hva er virtualisering?

Virtualisering er teknologien som lar en fysisk datamaskin kjøre flere isolerte virtuelle maskiner (VM-er) samtidig. Hver VM kjører sitt eget operativsystem og sine egne applikasjoner, og "tror" at den er en selvstendig fysisk maskin.

En **hypervisor** er programvaren som administrerer de virtuelle maskinene og fordeler fysiske ressurser (CPU, RAM, disk, nettverk) mellom dem.

### Type 1 vs. Type 2 hypervisorer

| | Type 1 (Bare Metal) | Type 2 (Hosted) |
|---|---|---|
| **Kjører på** | Direkte på maskinvaren | Oppå et vertsoperativsystem |
| **Ytelse** | Høy (ingen OS-overhead) | Lavere (OS-lag i veien) |
| **Bruksområde** | Produksjonsservere, datasentre | Utvikling, testing, undervisning |
| **Eksempler** | Hyper-V, VMware ESXi, Proxmox | VirtualBox, VMware Workstation |
| **Administrasjon** | Via nettgrensesnitt eller mgmt-verktøy | Fra vertsoperativsystemet |

#### Type 1: Microsoft Hyper-V

Hyper-V er Microsofts Type 1-hypervisor og er tilgjengelig som en serverrolle i Windows Server. Den kan også aktiveres som funksjon i Windows 10/11 Pro.

Nøkkelbegreper i Hyper-V:
- **Root partition**: Windows Server-installasjonen med tilgang til faktisk maskinvare
- **Child partition (Guest VM)**: Den virtuelle maskinen som kun ser emulert/virtuell maskinvare
- **Generation 1 vs. Generation 2**: Gen 2 støtter UEFI og Secure Boot, anbefalt for moderne OS

#### Type 2: Oracle VirtualBox

VirtualBox er gratis og plattformuavhengig (Windows, macOS, Linux). Godt egnet for laboratorieøvelser der man ikke har dedikert serverhardware.

### Virtuelle maskiner — egenskaper

Hver VM har:
- **Virtuell CPU** (vCPU) — én eller flere kjerner
- **Virtuelt RAM** — allokert fra fysisk RAM
- **Virtuell harddisk** — lagret som en fil (.vhd, .vhdx, .vmdk) på fysisk disk
- **Virtuelt nettverkskort** — koblet til en virtuell svitsj

Fordeler med VM-er:
- **Isolasjon**: feil eller kompromittering i én VM påvirker ikke andre
- **Ressurseffektivitet**: unngår "én server per tjeneste"-overforbruk
- **Portabilitet**: en VM kan eksporteres og importeres på annen hardware
- **Snapshots**: ta øyeblikksbilde av tilstanden — rull tilbake ved feil
- **Skalerbarhet**: enkel å klone og skalere opp
- **Bærekraft**: serverkonsolidering reduserer strømforbruk og behov for fysisk maskinvare

**Isolasjon** er prinsippet om at en virtuell maskin er separert fra andre maskiner og vertssystemet, slik at feil eller virus i én VM ikke sprer seg til resten av infrastrukturen.

### Virtuelle nettverk

Hypervisorer tilbyr virtuelle svitsjer (virtual switches / vSwitch) som kobler VM-er sammen og mot fysiske nettverk.

En **virtuell svitsj (vSwitch)** er en programvarebasert nettverkssvitsj som lar virtuelle maskiner kommunisere med hverandre og fysiske nettverk via VLAN.

#### Hyper-V Virtual Switch — tre typer

| Type | Beskrivelse | Bruksscenario |
|------|-------------|---------------|
| **Ekstern** | Koblet til fysisk nettverkskort — VM-er når det fysiske nettverket | Produksjon, lab mot reelt nett |
| **Intern** | Kommunikasjon mellom host og VM-er — ikke ut på fysisk nettverk | Host administrerer VM-er, delt nett |
| **Privat** | Kun mellom VM-er — host har ikke tilgang | Isolerte testmiljøer |

#### VirtualBox nettverksmodi

| Modus | VM ser | VM nås fra | Typisk bruk |
|-------|--------|-----------|-------------|
| **NAT** | Internett via host | Kun host (port-forward) | Enkel internett-tilgang fra VM |
| **Bridged** | Fysisk nettverk direkte | Andre maskiner på nettverket | VM oppfører seg som fysisk maskin |
| **Host-only** | Kun host og andre VM-er | Kun host | Isolert lab-nettverk |
| **Internal Network** | Kun andre VM-er | Ingen | Fullstendig isolerte VM-er |

### VLAN i virtuelle nettverk

Virtuelle svitsjer støtter VLAN-tagging. En VM kan tilordnes et bestemt VLAN-ID, slik at den logisk befinner seg i det samme VLAN-et som fysiske maskiner i samme segment. Dette er nøkkelen til kompetansemål km-02: virtuelle løsninger integreres i de segmenterte nettverkene.

Eksempel: En Windows Server-VM med AD DS tilordnes VLAN 30 (Servere), mens klient-VM-er tilordnes VLAN 10 (Ansatte) — nøyaktig slik fysiske maskiner ville vært plassert.

### Praktisk bruk i VG2

**Opprette VM i Hyper-V (forenklet):**
1. Hyper-V Manager → Action → New → Virtual Machine
2. Gi VM-en et navn (f.eks. `WinServer01`)
3. Velg Generasjon (Gen 2 for Windows Server 2019/2022)
4. Tildel RAM (minimum 2 GB, anbefalt 4 GB)
5. Koble til virtuell svitsj
6. Opprett virtuell harddisk (f.eks. 60 GB dynamisk)
7. Velg installasjons-ISO
8. Fullfør og start VM-en

**Snapshots/kontrollpunkter:**
- Høyreklikk VM → Checkpoint (tar øyeblikksbilde)
- Rull tilbake: høyreklikk checkpoint → Apply
- Slett foreldede checkpoints for å frigjøre diskplass

## Eksempel / lab

### Lab: Todelt tjenestearkitektur med Linux (WebServer + DBServer)

> **Kilde:** Klasseromsnotater (2ITA)
>
> I undervisningen setter elevene opp en todelt tjenestearkitektur med to Ubuntu Server-VM-er i VirtualBox. Målet er å få ticketsystemet osTicket til å kjøre med webserver og database på separate maskiner.
>
> **VM-oppsett:** Begge VM-er (WebServer og DBServer) konfigureres med min. 4 GB RAM, 2 CPU-er og 25 GB disk. Nettverksmodus settes til **Bridged Adapter** slik at VM-ene får egne IP-adresser på skolenettverket.
>
> **Statisk IP med Netplan (Ubuntu Server):**
> ```yaml
> network:
>   ethernets:
>     enp0s3:
>       dhcp4: no
>       addresses:
>         - 192.168.52.100/24
>       routes:
>         - to: default
>           via: 192.168.52.5
>       nameservers:
>         addresses: [192.168.52.5, 8.8.8.8]
>   version: 2
> ```
> Aktiver med `sudo netplan apply`.
>
> **WebServer:** Apache installeres (`sudo apt install apache2 -y`) og PHP-moduler som kreves av osTicket. osTicket lastes ned og legges i `/var/www/html/`.
>
> **DBServer:** MariaDB installeres (`sudo apt install mariadb-server -y`). For at WebServer skal nå databasen må `bind-address` i `/etc/mysql/mariadb.conf.d/50-server.cnf` endres fra `127.0.0.1` til `0.0.0.0`, etterfulgt av `sudo systemctl restart mariadb`.

### Lab-scenario: To VM-er på isolert nettverk

Mål: Sett opp en Windows Server-VM og en Windows-klient-VM som kommuniserer kun med hverandre (isolert fra internett).

1. I VirtualBox: opprett to VM-er
2. Begge VM-er: nettverksmodus = "Internal Network", samme nettverksnavn (f.eks. "labnet")
3. Windows Server: sett statisk IP `192.168.10.1/24`
4. Windows-klient: sett statisk IP `192.168.10.2/24`, gateway `192.168.10.1`
5. Test: `ping 192.168.10.1` fra klienten
6. Installer DHCP-rollen på serveren og endre klienten til dynamisk IP

Dette simulerer et produksjonsmiljø uten risiko for det fysiske nettverket.

## Study guide

**Kjerneforståelse: hypervisorer**
Type 1 (bare metal) kjører direkte på maskinvaren — høy ytelse, brukes i produksjon (Hyper-V, ESXi, Proxmox). Type 2 kjører oppå et OS — enklere, brukes i lab og utvikling (VirtualBox, VMware Workstation).

**Nettverksmodi i VirtualBox**
NAT: VM deler hostens IP, ikke synlig utenfra. Bridged: VM får egen IP, oppfører seg som fysisk maskin. Host-only: kun mellom host og VM-er. Internal Network: kun mellom VM-er.

**VLAN i virtuelle miljøer**
Virtuelle svitsjer støtter VLAN-tagging. En VM kan tilhøre et VLAN akkurat som en fysisk maskin. Dette er sentralt for å integrere virtuelle servere i segmenterte nettverksarkitekturer.

**Vanlige eksamenspoeng**
- Forskjellen mellom Type 1 og Type 2 hypervisor
- Hva et snapshot er og når man bruker det
- Forskjellen mellom NAT og Bridged i VirtualBox
- Fordeler med virtualisering (isolasjon, effektivitet, portabilitet, bærekraft)

## FAQ

**Hva er forskjellen mellom en Type 1 og Type 2 hypervisor?**
En Type 1-hypervisor (bare metal) kjører direkte på maskinvaren uten underliggende OS, noe som gir bedre ytelse. Den brukes i produksjon (Hyper-V, VMware ESXi). En Type 2-hypervisor kjører som et program oppå et vertsoperativsystem (VirtualBox, VMware Workstation) — enklere å sette opp, men med noe dårligere ytelse.

**Hva er et snapshot/kontrollpunkt i en VM, og hvorfor er det nyttig?**
Et snapshot (kontrollpunkt) er et øyeblikksbilde av en VM-s tilstand på et bestemt tidspunkt. Det lar deg rulle VM-en tilbake til den tilstanden hvis noe går galt — f.eks. etter en mislykket oppdatering eller feilkonfigurasjon. Uunnværlig i lab-miljøer.

**Hva er forskjellen mellom NAT og Bridged nettverksmodus i VirtualBox?**
I NAT-modus deler VM-en hostmaskinens IP-adresse og når internett gjennom den — men er ikke direkte synlig fra andre maskiner på nettverket. I Bridged-modus kobles VM-en direkte til det fysiske nettverket og får sin egen IP-adresse, som om den var en fysisk maskin.

**Hvilke tre typer virtuelle svitsjer finnes i Hyper-V?**
Ekstern (kobler VM-er til det fysiske nettverket via vertsmaskinens nettverkskort), Intern (kommunikasjon mellom host og VM-er, ikke ut på fysisk nett) og Privat (kun mellom VM-er, host har ikke tilgang).

**Nevn tre fordeler med virtualisering i IT-drift.**
(Velg tre av): Ressurseffektivitet (færre fysiske servere), isolasjon mellom tjenester, portabilitet (eksport/import av VM-er), snapshots for enkel feilretting, enkel skalering, raskere utrulling av nye servere.

**Hva er en virtuell svitsj (vSwitch)?**
En programvarebasert nettverkssvitsj som lar virtuelle maskiner kommunisere med hverandre og med fysiske nettverk. Virtuelle svitsjer støtter VLAN-tagging slik at VM-er kan plasseres i logiske nettverkssegmenter på samme måte som fysiske maskiner.

**Hvordan bidrar virtualisering til bærekraft?**
Serverkonsolidering lar én fysisk server erstatte mange separate maskiner. Dette reduserer strømforbruk, kjølebehov og mengden fysisk maskinvare som må produseres og kasseres — direkte bidrag til redusert miljøbelastning i IT-drift.

**Hva betyr isolasjon i virtualisering?**
Isolasjon betyr at en VM er separert fra andre VM-er og fra vertssystemet. Hvis en VM kompromitteres av malware, sprer det seg ikke automatisk til andre VM-er. Dette er en av de viktigste sikkerhetsfordelene med virtualisering.

## Quiz

<details>
<summary>Spørsmål 1: Hva er forskjellen mellom en Type 1 og Type 2 hypervisor?</summary>

**Svar:** En Type 1-hypervisor (bare metal) kjører direkte på maskinvaren uten underliggende OS, noe som gir bedre ytelse. Den brukes i produksjon (Hyper-V, VMware ESXi). En Type 2-hypervisor kjører som et program oppå et vertsoperativsystem (VirtualBox, VMware Workstation) — enklere å sette opp, men med noe dårligere ytelse.
</details>

<details>
<summary>Spørsmål 2: Hva er et snapshot/kontrollpunkt i en VM, og hvorfor er det nyttig?</summary>

**Svar:** Et snapshot (kontrollpunkt) er et øyeblikksbilde av en VM-s tilstand på et bestemt tidspunkt. Det lar deg rulle VM-en tilbake til den tilstanden hvis noe går galt — f.eks. etter en mislykket oppdatering eller feilkonfigurasjon. Uunnværlig i lab-miljøer.
</details>

<details>
<summary>Spørsmål 3: Hva er forskjellen mellom NAT og Bridged nettverksmodus i VirtualBox?</summary>

**Svar:** I NAT-modus deler VM-en hostmaskinens IP-adresse og når internett gjennom den — men er ikke direkte synlig fra andre maskiner på nettverket. I Bridged-modus kobles VM-en direkte til det fysiske nettverket og får sin egen IP-adresse, som om den var en fysisk maskin.
</details>

<details>
<summary>Spørsmål 4: Hvilke tre typer virtuelle svitsjer finnes i Hyper-V?</summary>

**Svar:** Ekstern (kobler VM-er til det fysiske nettverket via vertsmaskinens nettverkskort), Intern (kommunikasjon mellom host og VM-er, ikke ut på fysisk nett) og Privat (kun mellom VM-er, host har ikke tilgang).
</details>

<details>
<summary>Spørsmål 5: Nevn tre fordeler med virtualisering i IT-drift.</summary>

**Svar:** (Velg tre av): Ressurseffektivitet (færre fysiske servere), isolasjon mellom tjenester, portabilitet (eksport/import av VM-er), snapshots for enkel feilretting, enkel skalering, raskere utrulling av nye servere.
</details>

## Flashcards

Hypervisor :: Programvare som administrerer virtuelle maskiner og fordeler fysiske ressurser mellom dem
Type 1 hypervisor :: Hypervisor som kjører direkte på maskinvare (bare metal): Hyper-V, VMware ESXi, Proxmox
Type 2 hypervisor :: Hypervisor som kjører oppå et vertsoperativsystem: VirtualBox, VMware Workstation
VM (virtuell maskin) :: Isolert programvaresimulert datamaskin som kjører eget OS på en hypervisor
Snapshot :: Øyeblikksbilde av en VM-s tilstand som kan brukes til å rulle tilbake endringer
Hyper-V ekstern svitsj :: Virtuell svitsj koblet til fysisk nettverkskort — gir VM-er tilgang til det fysiske nettverket
NAT (VM-nettverk) :: VM deler hostens IP og når internett, men er ikke direkte synlig utenfra
Bridged (VM-nettverk) :: VM kobles direkte til fysisk nettverk og får egen IP-adresse
Root partition :: Hyper-V-terminologi for Windows Server-installasjonen med tilgang til fysisk maskinvare
Child partition :: Hyper-V-terminologi for en gjeste-VM som kun ser virtuell/emulert maskinvare
Virtuell Svitsj (vSwitch) :: En programvarebasert nettverkssvitsj som lar virtuelle maskiner kommunisere med hverandre og fysiske nettverk via VLAN
Isolasjon :: Prinsippet om at en virtuell maskin er separert fra andre maskiner og vertssystemet, slik at feil eller virus i én VM ikke sprer seg

## Ressurser

- [Virtualisering i Windows Server — NDLA](https://ndla.no/nb/r/teknologiforstaelse-im-ikm-vg1/virtualisering-i-windows-server/5f000530eb)
- [Opprett virtuell maskin i Hyper-V — NDLA](https://ndla.no/nb/r/yrkesfaglig-fordypning-im-ikm-vg1/opprett-virtuell-maskin-i-hyper-v/23c398aac8)
- [windowsnett.no — leksjon 1: virtualisering og Windows Server](https://www.windowsnett.no/)
- [Hyper-V Technology Overview — Microsoft Learn](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/hyper-v-technology-overview)
