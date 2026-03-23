---
title: "Nettverk — oversikt"
emne: nettverk
kompetansemaal:
  - km-02
  - km-05
kilder:
  - ndla
tags: []
flashcards: false
public: true
---

# Nettverk — oversikt

## Hva er et datanettverk?

Et datanettverk er et system der to eller flere enheter er koblet sammen for å dele ressurser og kommunisere. I driftsstøtte-faget er nettverksforståelse fundamentalt — du kan ikke drifte det du ikke forstår.

Nettverk deles gjerne inn etter størrelse:
- **LAN (Local Area Network)** — lokalt nettverk, f.eks. i et klasserom eller kontorbygg
- **WAN (Wide Area Network)** — nettverk over store geografiske avstander, f.eks. internett
- **WLAN (Wireless LAN)** — trådløst lokalnettverk (WiFi)

## Nettverkskomponenter

| Komponent | Funksjon | OSI-lag |
|-----------|----------|---------|
| Svitsj | Kobler enheter i et LAN, bruker MAC-adresser | Lag 2 |
| Ruter | Kobler nettverk sammen, videresender pakker | Lag 3 |
| Aksesspunkt | Gir trådløs tilgang til nettverket | Lag 1–2 |
| Kabel (UTP/fiber) | Fysisk medium for dataoverføring | Lag 1 |
| Brannmur | Filtrerer trafikk etter regler | Lag 3–7 |

## Logisk vs. fysisk struktur

Den **fysiske strukturen** beskriver hvordan kabler og utstyr er koblet sammen. Den **logiske strukturen** beskriver hvordan datatrafikken flyter og hvordan nettverk er segmentert — f.eks. med VLAN.

En god driftstøtter behersker begge.

## Nettverksmodellene

For å forstå kommunikasjon i nettverk bruker vi to referansemodeller:

- **[[tcp-ip-modellen]]** — den praktiske modellen med 4–5 lag som internett faktisk bygger på
- **[[osi-modellen]]** — ISO-standardmodellen med 7 lag, brukt som referanse og ved feilsøking

## Segmentering og VLAN

Segmentering handler om å dele nettverket opp i logiske soner. Dette gir:
- Bedre **sikkerhet** (angrep sprer seg ikke på tvers av segmenter)
- Bedre **ytelse** (mindre broadcast-trafikk)
- Enklere **administrasjon**

Les mer: [[segmentering-og-vlan]]

## Virtuelle løsninger

Virtualisering gjør det mulig å kjøre flere servere og nettverk på én fysisk maskin. I skolen bruker vi Hyper-V og VirtualBox til laboratorieøvelser.

Les mer: [[virtuelle-losninger]]

## Protokoller og tjenester

Nettverksprotokoller er "språket" enhetene bruker for å kommunisere. Sentrale tjenester inkluderer:

- **DNS** og **DHCP** — navneoppløsning og automatisk IP-tildeling: [[dns-og-dhcp]]
- **HTTP, FTP, SSH, SMTP** og mange flere: [[nettverksprotokoller]]
- **Serverroller** som webserver, filserver og domenekontroller: [[serverroller]]

## Kobling til kompetansemål

| Kompetansemål | Artikler |
|---------------|---------|
| **km-02** — Planlegge, implementere og drifte fysiske og virtuelle løsninger med segmenterte nettverk | [[segmentering-og-vlan]], [[virtuelle-losninger]] |
| **km-05** — Utforske og beskrive relevante nettverksprotokoller, nettverkstjenester og serverroller | [[tcp-ip-modellen]], [[osi-modellen]], [[dns-og-dhcp]], [[nettverksprotokoller]], [[serverroller]] |

## Alle artikler i dette emnet

- [[tcp-ip-modellen]] — TCP/IP-modellens lag og pakkeflyt
- [[osi-modellen]] — OSI-modellens 7 lag og bruk ved feilsøking
- [[dns-og-dhcp]] — Navneoppløsning og automatisk IP-tildeling
- [[segmentering-og-vlan]] — Subnetting, CIDR og VLAN
- [[virtuelle-losninger]] — Hypervisorer og virtuelle nettverk
- [[nettverksprotokoller]] — Viktige protokoller og portnumre
- [[serverroller]] — Serverroller i Windows Server og AD DS
