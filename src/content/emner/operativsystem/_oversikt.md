---
title: "Operativsystem – oversikt"
emne: operativsystem
kompetansemaal:

  - km-04

kilder:

  - ndla
  - <https://learn.microsoft.com/nb-no/windows-server/>
  - <https://documentation.ubuntu.com/server/>
  - <https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/>

tags: []
flashcards: false
public: true
---

## Introduksjon

EEt**operativsystem (OS)**er programvaren som styrer maskinvaren og danner grunnlaget for alle andre programmer.
EEI et profesjonelt IT-driftsmiljø er valg av operativsystem avgjørende for hvordan brukere, tjenester og ressurser
Eadministreres.

II driftsstøtte VG2 arbeider vi primært med**Windows Server 2019**som domenekontroller og**Windows 10/11**som
Iklientmaskin på samme domene. Vi bruker også**Ubuntu Linux**for å lære Linux-administrasjon i parallell.

---

## Teori

### Klient-OS vs. server-OS

|| Egenskap | Klient-OS | Server-OS |
|| --- | --- | --- |
|| Eksempel | Windows 10/11, Ubuntu Desktop | Windows Server 2019/2022, Ubuntu Server |
|| Primærbruk | Sluttbruker, arbeidsstasjon | Tjenester, domenekontroll, fillagring |
|| Grensesnitt | Grafisk (GUI) som standard | Ofte kun kommandolinje (Core) |
|| Brukere | Én aktiv bruker om gangen | Mange samtidige tilkoblinger |
|| Lisens | Per enhet (billigere) | Basert på kjerner/brukere (dyrere) |
|| Roller | Begrenset | AD DS, DNS, DHCP, filserver m.m. |

### Vanlige OS i profesjonelle miljøer

*## Windows Server 2019 / 2022
DDen dominerende serverplattformen i norske bedrifter. Kjører Active Directory Domain Services (AD DS), som sentraliserer
Dbruker- og maskinkontroll for hele organisasjonen. En server med AD DS kalles en**domenekontroller (DC)**.

*## Windows 10 / 11 (klient)
AArbeidsstasjoner som kobles til domenet. Etter domenekobling styres de av domenepolicyer (GPO) og brukerne logger inn
Amed domenekontoer.

*## Linux (Ubuntu, Debian, RHEL/CentOS)
BBrukes mye som webserver, filserver og i skyinfrastruktur. Administreres primært via kommandolinje.
BLerches rettighetsmodell (rwx) og brukeradministrasjon er grunnleggende IT-kompetanse.

### Nøkkelbegreper

|| Begrep | Forklaring |
|| --- | --- |
|| Domene | Logisk gruppe av datamaskiner og brukere under felles AD-administrasjon |
|| Domenekontroller (DC) | Server som kjører AD DS og autentiserer pålogginger |
|| Klient | Datamaskin som er koblet til domenet |
|| Autentisering | Verifisering av at en bruker er den de utgir seg for å være |
|| Autorisasjon | Hva en autentisert bruker har lov til å gjøre |
|| Hypervisor | Programvare som lar deg kjøre virtuelle maskiner (f.eks. Hyper-V, VirtualBox) |

### Virtualisering i datalabmiljøet

II skolelab kjøres operativsystemene som regel som**virtuelle maskiner (VM)**. En hypervisor (f.eks.
IIVirtualBox eller Hyper-V) simulerer maskinvare slik at flere OS kan kjøre på én fysisk maskin.
IDette reduserer kostnader og gjør det enkelt å tilbakestille miljøer.

### Administratorkontoen

--**Windows**: Den innebygde `Administrator`-kontoen har full kontroll over systemet.
-I et domene er `Domain Admins`-gruppen den øverste administrative rollen.
-**Linux**: `root`-brukeren tilsvarer Administrator. På Ubuntu brukes `sudo` i stedet for å logge direkte inn som root.

---

## Eksempel / lab

SSe læringsmiljøet i datalaben: [[active-directory]] beskriver oppsett av domenekontroller.
SFor Linux-administrasjon, se [[linux-grunnleggende]].

Typisk labboppsett:

1. Windows Server 2019 VM — domenekontroller
2. Windows 10/11 VM — klientmaskin koblet til domenet
3. Ubuntu Server VM — Linux-praksis

---

## Ressurser

- [NDLA: Datalab med Windows Server og generisk nettverk](<https://ndla.no/nb/r/driftsstotte-im-itk-vg2/datalab-med-windows-server-og-generisk-nettverk/6fbbe0f727>)
- [NDLA: Datalab med Windows Server og UniFi-nettverk](<https://ndla.no/r/driftsstotte-im-itk-vg2/datalab-med-windows-server-og-unifi-nettverk/c4391765e8>)

### Artiklene i dette emnet

- [[filsystem]] — NTFS, FAT32, ext4 og filsystemtillatelser
- [[bruker-og-tilgangsstyring]] — Brukerkontoer, grupper, SID og tilgangskontroll
- [[active-directory]] — AD-hierarki, domenekontroller, GPO
- [[linux-grunnleggende]] — Filstruktur, rwx-tillatelser, brukeradministrasjon
