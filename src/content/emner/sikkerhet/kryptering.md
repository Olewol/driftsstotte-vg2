---
title: Kryptering
public: true
emne: sikkerhet
uke: [46, 47]
kompetansemaal: "planlegge og implementere sikkerhetstiltak"
tags: [kryptering, symmetrisk, asymmetrisk, ssl, tls]
---

# Kryptering

Kryptering er prosessen med å gjøre lesbar informasjon om til et ulesbart format for å beskytte data mot uautorisert tilgang.

## Symmetrisk kryptering

Bruker samme nøkkel for kryptering og dekryptering.

- **Fordel:** Rask og effektiv
- **Ulempe:** Nøkkelen må deles sikkert
- **Eksempel:** AES (Advanced Encryption Standard)

## Asymmetrisk kryptering

Bruker et nøkkelpar — en offentlig og en privat nøkkel.

- **Offentlig nøkkel:** Kan deles fritt, brukes til kryptering
- **Privat nøkkel:** Holdes hemmelig, brukes til dekryptering
- **Eksempel:** RSA, ECC

## TLS/SSL

Transport Layer Security (TLS) beskytter kommunikasjon over internett ved å kombinere symmetrisk og asymmetrisk kryptering. HTTPS bruker TLS.
