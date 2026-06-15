---
title: "KM-02: Segmenterte nettverk / Segmented Networks"
emne: kompetansemaal
kompetansemaal:

  - km-02

kilder:

  - <https://www.udir.no/lk20/itk02-01/kompetansemaal-og-vurdering/kv372>
  - <https://www.cloudflare.com/learning/network-layer/what-is-a-vlan/>
  - <https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/>
  - <https://learn.microsoft.com/en-us/training/modules/introduction-to-virtualization/>

tags: [km-02, nettverk, segmentering, vlan, virtualisering]
flashcards: false
public: true
---

# KM-02: Segmenterte nettverk / Segmented Networks

## 🎯 Mål / Competency Goal

**Norsk:**Planlegge, implementere og drifte fysiske og virtuelle løsninger med segmenterte nettverk

**English:**Plan, implement and operate physical and virtual solutions with segmented networks

---

## 📘 Forklaring / Explanation

### Norsk

SSegmenterte nettverk betyr å dele opp et større nettverk i mindre, isolerte deler (segmenter).
SDette gjøres for å forbedre sikkerhet, ytelse og oversiktlighet[^1][^4].

Hovedverktøyene for nettverkssegmentering:
-**VLAN (Virtual LAN)**— Logisk segmentering på svitsjnivå
-**Subnett**— IP-basert segmentering med CIDR-notasjon
-**Brannmurer**— Regelbasert trafikkontroll mellom segmenter

VVirtualisering spiller en nøkkelrolle: på én fysisk vert kan du kjøre flere virtuelle maskiner (VM-er) som hver har sitt
Veget virtuelle nettverkskort og kan plasseres i ulike VLAN.

### English

SSegmented networks means dividing a larger network into smaller, isolated parts (segments).
SThis improves security, performance, and manageability[^1].

Key tools for network segmentation:
-**VLAN (Virtual LAN)**— Logical segmentation at the switch level
-**Subnets**— IP-based segmentation using CIDR notation
-**Firewalls**— Rule-based traffic control between segments

VVirtualization plays a key role: on one physical host you can run multiple virtual machines (VMs), each with its own
Vvirtual network card placed in different VLANs.

---

## 💡 Eksempler / Examples

### Norsk (2)

*## Eksempel 1: Skole-nettverk med VLAN
EEn skole har tre avdelinger: administrasjon, undervisning og IT-drift. Med VLAN kan alle være på samme fysiske svitsjer,
Emen administrasjonens data kan ikke nås fra elevnettet. VLAN 10 = admin, VLAN 20 = undervisning, VLAN 30 = IT-drift.

*## Eksempel 2: DMZ i en bedrift
EEn bedrift har websereren i et eget segment (DMZ) slik at selv om den blir hacket, har angriperen ikke direkte tilgang
Etil interne dataserverer.

### English (2)

*## Example 1: School Network with VLANs
AA school has three departments: administration, teaching, and IT operations. With VLANs they can share the same physical
AAswitches, but administrative data can't be reached from the student network. VLAN 10 = admin, VLAN 20 = teaching, VLAN
A30 = IT operations.

*## Example 2: DMZ in a Company
AA company places its web server in a separate segment (DMZ) so even if it gets hacked, the attacker has no direct access
Ato internal database servers.

---

## 📝 Oppsummering / Summary

|| Norsk | English |
|| ------- | --------- |
|| Segmentering deler nettverk i isolerte soner | Segmentation divides networks into isolated zones |
|| VLAN er den vanligste metoden for logisk segmentering | VLAN is the most common method for logical segmentation |
|| Virtualisering gjør segmentering mer fleksibel | Virtualization makes segmentation more flexible |
|| God segmentering begrenser skade ved sikkerhetsbrudd | Good segmentation limits damage during security breaches |

---

## 🔧 Bridging Exercises / Praksisoppgaver

### Norsk — Praksisoppgaver

*## Oppgave 1: Konfigurer VLAN på en svitsj
Bruk Cisco Packet Tracer (eller en fysisk svitsj) til å sette opp:

- VLAN 10 — Administrasjon (4 PC-er)
- VLAN 20 — Undervisning (10 PC-er)
- VLAN 30 — Gjestenett (trådløst, 5 enheter)
- VLAN 40 — Serversegment (3 servere)
- Konfigurer trunk-port mellom svitsjer
- Verifiser at PC-er i ulike VLAN IKKE kan pinge hverandre
- Sett opp en ruter på stilk (router-on-a-stick) for inter-VLAN-ruting

*## Oppgave 2: Design et segmentert nettverk for en videregående skole
Skolens IT-sjef har bedt deg om å tegne en segmenteringsplan:

- 3 undervisningsavdelinger: IT, Helse, Elektro
- Administrasjon med 10 ansatte
- Serverrom med 4 fysiske servere
- Gjestenett for besøkende
- Hvert segment skal ha egen DHCP-sone og brannmurregler

Lever: VLAN-tabell, IP-adresseområder, og brannmurregel-sett.

*## Veiledning / Solution Guidelines:

- Oppgave 1: VLAN-konfigurasjon: `vlan 10`, `name Admin`, `interface range f0/1-4`, `switchport access vlan 10`. Trunk: `interface f0/24`, `switchport mode trunk`. Router-on-a-stick: subinterfaces med 802.1Q-innkapsling.
- Oppgave 2: Eksempel: VLAN 10-19 for undervisning, VLAN 20 for administrasjon, VLAN 30 for servere, VLAN 40 for gjester. Hvert segment /24-nett. Brannmurregler: gjestenett kun internett, administrasjon tilgang til servere, undervisning begrenset tilgang.

### English — Practical Exercises

*## Exercise 1: Configure VLANs on a Switch
Using Cisco Packet Tracer (or physical switch), set up:

- VLAN 10 — Administration (4 PCs)
- VLAN 20 — Teaching (10 PCs)
- VLAN 30 — Guest network (5 wireless devices)
- VLAN 40 — Server segment (3 servers)
- Configure trunk ports between switches
- Verify that PCs in different VLANs CANNOT ping each other
- Set up router-on-a-stick for inter-VLAN routing

*## Exercise 2: Design a Segmented Network for a High School
The school's IT manager asks you to design a segmentation plan:

- 3 teaching departments: IT, Health, Electrical
- Administration with 10 employees
- Server room with 4 physical servers
- Guest network for visitors

Deliver: VLAN table, IP address ranges, and firewall rule set.

*## Solution Guidelines:

- Exercise 1: VLAN config: `vlan 10`, `name Admin`, `interface range f0/1-4`, `switchport access vlan 10`. Trunk: `interface f0/24`, `switchport mode trunk`. Router-on-a-stick: subinterfaces with 802.1Q encapsulation.
- Exercise 2: Example: VLAN 10-19 for teaching, VLAN 20 for admin, VLAN 30 for servers, VLAN 40 for guests. Each segment /24 network. Firewall rules: guest network internet-only, admin has server access, teaching limited access.

## 🔗 Relevante artikler / Related Articles

- [[segmentering-og-vlan]] — VLAN, subnetting og CIDR
- [[virtuelle-losninger]] — Hypervisorer, VM-er og virtuelle nettverk
- [[brannmur]] — Brannmurer og DMZ

## 📚 Kilder / Sources

[^1]: Udir (2020). Læreplan i Vg2 informasjonsteknologi. <https://www.udir.no/lk20/itk02-01/>
[^2]: Cloudflare. What is a VLAN? <https://www.cloudflare.com/learning/network-layer/what-is-a-vlan/>
[^3]: Microsoft Learn. Introduction to virtualization. <https://learn.microsoft.com/en-us/training/modules/introduction-to-virtualization/>
[^4]: NDLA. Fagstoff for driftsstøtte VG2. <https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/>
