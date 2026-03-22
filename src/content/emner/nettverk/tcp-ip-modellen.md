---
title: TCP/IP-modellen
public: true
emne: nettverk
uke: [36, 37]
kompetansemaal: "Planlegge og konfigurere nettverk med ulike topologiar"
tags: [tcp, ip, protokoll, nettverk]
relatert:
  - osi-modellen
  - ip-adressering
ressursar:
  - type: lenke
    tittel: "Cloudflare: What is TCP/IP?"
    url: "https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/"
  - type: video
    tittel: "Nettverkslag visualisert (8 min)"
    lengde: "8 min"
oppgaaver:
  - "Teikn og forklar dei fire laga i TCP/IP-modellen"
  - "Samanlikn TCP/IP og [[nettverk/osi-modellen|OSI-modellen]]"
---

TCP/IP er den grunnleggjande protokollstabelen som internett byggjer på. Modellen beskriv korleis data pakkas, adresserast, overførast og mottakast mellom einingar i eit nettverk.

## Dei fire laga

| Lag | Namn | Protokollar |
|---|---|---|
| 4 | Applikasjon | HTTP, FTP, DNS, SMTP |
| 3 | Transport | TCP, UDP |
| 2 | Internett | IP, ICMP, ARP |
| 1 | Nettverkstilgang | Ethernet, Wi-Fi |

For å forstå IP-adressering og subnetting er det naudsynt å ha kontroll på internettlaget. Samanlikn gjerne med [[nettverk/osi-modellen|OSI-modellen]] som har sju lag.
