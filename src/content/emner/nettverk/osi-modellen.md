---
title: OSI-modellen
public: true
emne: nettverk
uke: [38, 39]
kompetansemaal: "planlegge og konfigurere nettverk med ulike topologier"
tags: [osi, nettverk, protokoll, lag]
---

# OSI-modellen

OSI-modellen (Open Systems Interconnection) er en konseptuell modell som standardiserer kommunikasjonsfunksjonene i et nettverk.

## De sju lagene

1. **Fysisk lag** — Kabler, signal, bitoverføring
2. **Datalenkjelag** — MAC-adresser, rammer, svitsjer
3. **Nettverkslag** — IP-adresser, routing, rutere
4. **Transportlag** — TCP/UDP, porter, feilkorrigering
5. **Sesjonslag** — Oppretting og avslutning av sesjoner
6. **Presentasjonslag** — Kryptering, komprimering, formatkonvertering
7. **Applikasjonslag** — HTTP, FTP, DNS, SMTP

## OSI vs TCP/IP

OSI-modellen er en referansemodell med 7 lag, mens TCP/IP er den praktiske implementasjonen med 4 lag. I praksis bruker vi TCP/IP, men OSI-modellen er nyttig for feilsøking og forståelse.
