---
title: "Sikkerhet – oversikt"
emne: sikkerhet
kompetansemaal:
  - km-07
  - km-08
  - km-10
  - km-11
kilder:
  - ndla
  - nsm
  - datatilsynet
tags: []
flashcards: false
public: true
---

## Hva er informasjonssikkerhet?

Informasjonssikkerhet handler om å beskytte informasjon og IT-systemer mot uautorisert tilgang, endring, ødeleggelse eller avbrudd. Det er ikke bare et teknisk fagfelt – det omfatter også organisatoriske rutiner og juridiske rammer.

I faget Driftsstøtte (ITK02-01) er sikkerhet gjennomgående: du skal forstå trusler, gjennomføre risikoanalyse, implementere sikkerhetstiltak og kjenne til personvernregelverket.

---

## CIA-triaden

CIA-triaden er grunnmuren i all informasjonssikkerhet. Den består av tre egenskaper som et system eller en informasjonsressurs skal ha:

| Egenskap | Norsk | Betydning |
|---|---|---|
| **Confidentiality** | Konfidensialitet | Kun autoriserte personer får tilgang til informasjonen |
| **Integrity** | Integritet | Informasjonen er korrekt og ikke manipulert |
| **Availability** | Tilgjengelighet | Systemer og data er tilgjengelige når de trengs |

Et angrep retter seg alltid mot én eller flere av disse egenskapene:
- **Ransomware** rammer tilgjengelighet (filer krypteres) og konfidensialitet (data stjeles)
- **Datamanipulering** rammer integritet
- **DDoS** rammer tilgjengelighet

---

## Sikkerhetsemner i dette faget

Dette fagområdet dekker sju artikler:

### Trusler og trusselbilde
- [[trusselbildet]] – Malware, phishing, DDoS, APT og samfunnspåvirkning *(km-07)*

### Analyse og planlegging
- [[risikoanalyse]] – Risikovurderingsprosessen, risikomatrise og tiltak *(km-08)*

### Tekniske sikkerhetstiltak
- [[kryptering]] – Symmetrisk/asymmetrisk kryptering, TLS, PKI og hashing *(km-10)*
- [[brannmur]] – Pakkefiltrering, stateful inspection, DMZ og IDS/IPS *(km-10)*

### Systemer med innebygd sikkerhet
- [[it-losninger-med-sikkerhet]] – Security by Design, Zero Trust, patching, SIEM og BCDR *(km-10)*

### Personvern og juridisk rammeverk
- [[personvern]] – GDPR, rettigheter, bruddvarsling og samfunnskonsekvenser *(km-10, km-11)*

---

## Norske aktører innen sikkerhet

**NSM – Nasjonal sikkerhetsmyndighet**
Norges ekspertorgan for informasjons- og objektsikkerhet. Utgir *Grunnprinsipper for IKT-sikkerhet* (v2.1, 2024) – en praktisk veileder for sikker drift. NSM har fire kategorier av grunnprinsipper:
1. Identifiser og kartlegg
2. Beskytt og oppretthold
3. Oppdag
4. Håndter og gjenopprett

**NCSC – Norwegian Cyber Security Centre**
Opereres av NSM. Tilbyr 24/7 hendelseshåndtering og varsling. Kontakt: cert@ncsc.no

**Datatilsynet**
Norsk tilsynsmyndighet for personvern. Håndhever GDPR og personopplysningsloven. Ressurser for unge: [dubestemmer.no](https://dubestemmer.no) og [slettmeg.no](https://slettmeg.no).

---

## Relevante standarder og rammeverk

| Standard/rammeverk | Beskrivelse |
|---|---|
| **ISO 27001** | Internasjonal standard for styringssystem for informasjonssikkerhet (ISMS) |
| **NSM Grunnprinsipper v2.1** | Norsk veileder for sikker IKT-drift, tilpasset offentlig sektor og kritisk infrastruktur |
| **OWASP Top 10** | De ti vanligste sikkerhetsfeilene i webapplikasjoner (2021-versjon er gjeldende) |
| **GDPR** | EUs personvernforordning, gjeldende i Norge via EØS og personopplysningsloven |
| **Zero Trust** | Arkitekturmodell: «Aldri stol, alltid verifiser» (Microsoft-implementasjon er vanligst) |

---

## Sammenheng mellom emnene

```
Trusler (km-07)
     ↓
Risikoanalyse (km-08) ← identifiserer hvilke trusler som er relevante
     ↓
Tiltak (km-10):
  - Kryptering
  - Brannmur
  - IT-løsninger med sikkerhet
     ↓
Personvern (km-11) ← juridisk og etisk perspektiv på sikkerhet
```

God sikkerhet starter med å forstå trusselbildet, fortsetter med systematisk risikoanalyse og avsluttes med målrettede tiltak – alt innenfor rammen av gjeldende personvernlovgivning.
