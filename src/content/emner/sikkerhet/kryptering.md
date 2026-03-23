---
title: "Kryptering"
emne: sikkerhet
kompetansemaal:
  - km-10
kilder:
  - ndla
  - nsm
  - microsoft
tags: []
flashcards: true
public: true
---

## Introduksjon

Kryptering er teknologien som gjør at informasjon forblir konfidensielt selv om den havner i feil hender. Uten kryptering ville alt du sender over internett – passord, bankdetaljer, helseinformasjon, private meldinger – være leselig for hvem som helst som avlytter nettverkstrafikken.

NSM anbefaler i sine grunnprinsipper å «beskytte data i ro og under overføring», og kryptering er det primære verktøyet for dette. For en IT-drifter er det essensielt å forstå hvordan kryptering fungerer, hvilke standarder som er aktuelle i dag, og hvordan man verifiserer at kryptering faktisk er på plass.

---

## Teori

### Symmetrisk kryptering

Ved symmetrisk kryptering brukes **samme nøkkel** til å kryptere og dekryptere data.

- Fordel: svært rask – egnet for å kryptere store datamengder
- Ulempe: **nøkkeldistribusjonsproblemet** – nøkkelen må deles trygt mellom sender og mottaker, noe som er utfordrende over åpne nettverk
- Eksempel: **AES-256** (Advanced Encryption Standard med 256-bits nøkkel) – regnes som uknekket og er industristandarden for kryptering av data i ro (filsystemer, databaser, backuper)

**Illustrasjon:**
```
Avsender: Klartekst → [AES-nøkkel] → Chiffertekst
Mottaker: Chiffertekst → [AES-nøkkel] → Klartekst
```

---

### Asymmetrisk kryptering

Asymmetrisk kryptering bruker et **nøkkelpar**: en offentlig nøkkel (public key) og en privat nøkkel (private key). Det som krypteres med den ene nøkkelen, kan bare dekrypteres med den andre.

- **Offentlig nøkkel:** kan deles fritt med hvem som helst
- **Privat nøkkel:** holdes hemmelig av eieren – må aldri deles

Brukes til to formål:
1. **Kryptering:** Avsender krypterer med mottakerens offentlige nøkkel → bare mottakeren kan dekryptere med sin private nøkkel
2. **Digital signatur:** Avsenderen signerer med sin private nøkkel → hvem som helst kan verifisere signaturen med avsenderens offentlige nøkkel

- Eksempler: **RSA** (2048 eller 4096-bits nøkler), **ECC** (Elliptic Curve Cryptography – kortere nøkler, samme sikkerhet)
- Ulempe: mye tregere enn symmetrisk kryptering – egner seg dårlig for store datamengder

---

### Hybrid kryptering

Hybrid kryptering kombinerer det beste fra begge metoder:

1. **Asymmetrisk kryptering** brukes til å utveksle en midlertidig symmetrisk nøkkel (sesjonsnøkkel) trygt
2. **Symmetrisk kryptering** (AES) brukes for selve datakommunikasjonen – effektiv og rask

Dette er modellen TLS (og dermed HTTPS) bruker. Nesten all sikker kommunikasjon på internett er basert på hybrid kryptering.

---

### TLS 1.3 og HTTPS

**TLS (Transport Layer Security)** er protokollen som sikrer kommunikasjon over internett. TLS 1.3 (2018) er gjeldende standard og har erstattet de sårbare SSL og eldre TLS-versjoner.

**TLS 1.3 handshake (forenklet):**

```
1. Klienten sender støttede cipher suites og en tilfeldig verdi
2. Serveren sender valgt cipher suite, sertifikat og en tilfeldig verdi
3. Klienten verifiserer serverens sertifikat mot en CA (Certificate Authority)
4. Begge parter beregner en felles sesjonsnøkkel (via ECDHE)
5. Kryptert kommunikasjon begynner
```

Forbedringer i TLS 1.3 vs 1.2:
- Raskere handshake (1 round-trip i stedet for 2)
- Alle utdaterte cipher suites fjernet (ingen RC4, DES, 3DES, MD5)
- Forward secrecy er obligatorisk – gamle sesjoner kan ikke dekrypteres selv om nøkkelen later kompromitteres

---

### PKI – Public Key Infrastructure

**PKI** er infrastrukturen som gjør asymmetrisk kryptering praktisk brukbar i stor skala. Problemet PKI løser: Hvordan vet du at en offentlig nøkkel faktisk tilhører den den utgir seg for å være?

**Sertifikater (X.509):**
Et digitalt sertifikat binder en offentlig nøkkel til en identitet (f.eks. et domenenavn). Sertifikatet er signert av en **Certificate Authority (CA)**.

**CA-hierarki (tillitskjede):**
```
Root CA (selvsignert, innebygget i OS/nettleser)
    └── Intermediate CA (signert av Root CA)
            └── Serverens sertifikat (signert av Intermediate CA)
```

Nettleseren verifiserer at serverens sertifikat er signert av en CA den stoler på. Hvis sertifikatet er ugyldig, utløpt eller selvsignert, vises en sikkerhetsadvarsel.

Kjente CA-er: DigiCert, Let's Encrypt (gratis, automatisert), Sectigo, GlobalSign.

---

### Hashing

Hashing er en **enveisfunksjon** – du kan lage en hash fra data, men ikke rekonstruere dataene fra hashen. Hashing brukes ikke til kryptering, men til **integritetskontroll**.

| Algoritme | Hash-lengde | Status |
|---|---|---|
| MD5 | 128 bit | **Utdatert** – kollisjoner er funnet |
| SHA-1 | 160 bit | **Utdatert** – ikke lenger anbefalt |
| SHA-256 | 256 bit | **Anbefalt** – brukes i TLS, sertifikater, Git |
| bcrypt / Argon2 | variabel | **Anbefalt for passord** – langsom med vilje |

Typiske bruksområder:
- Passordlagring: aldri lagre klartekstpassord – lagre hashen (med salt)
- Filintegritet: SHA-256-sum av en fil avslører om filen er endret
- Digital signatur: man signerer hashen av dokumentet, ikke selve dokumentet

---

### Ende-til-ende-kryptering (E2EE)

Med ende-til-ende-kryptering er meldinger kryptert på avsenderens enhet og dekryptert kun hos mottakeren. Tjenesten i midten (serveren) kan ikke lese innholdet. Eksempler: Signal, WhatsApp (E2EE for meldinger, men ikke backuper som standard).

E2EE er spesielt relevant for personvern – selv om serveren hackes, er innholdet uleselig.

---

## Eksempel / lab

### Sjekk HTTPS-sertifikat i nettleser (Chrome/Edge)

1. Gå til en nettside, f.eks. [https://www.nav.no](https://www.nav.no)
2. Klikk på låseikonet (eller informasjonsikonet) til venstre i adresselinjen
3. Velg **«Tilkoblingen er sikker»** → **«Sertifikatet er gyldig»**

Sjekk følgende i sertifikatet:
- **Utstedt til:** bekrefter at domenet stemmer
- **Utstedt av:** hvilken CA som har signert sertifikatet
- **Gyldig fra / til:** sertifikater utløper (typisk 1 år for kommersielle, 90 dager for Let's Encrypt)
- **SHA-256 fingeravtrykk:** unik identifikator for sertifikatet

**Bonus:** Åpne nettleserens utviklerverktøy (F12) → Sikkerhet-fanen for å se hvilken TLS-versjon og cipher suite som brukes.

---

## Quiz

<details><summary>Spørsmål 1: Hva er nøkkeldistribusjonsproblemet ved symmetrisk kryptering?</summary>

**Svar:** Nøkkeldistribusjonsproblemet er at sender og mottaker må dele nøkkelen trygt på forhånd. Over åpne nettverk er dette vanskelig – hvis nøkkelen avlyttes under utveksling, er krypteringen kompromittert.

</details>

<details><summary>Spørsmål 2: Hva brukes den private nøkkelen til i asymmetrisk kryptering?</summary>

**Svar:** Den private nøkkelen brukes til to ting: (1) å dekryptere meldinger som er kryptert med din offentlige nøkkel, og (2) å signere meldinger digitalt slik at andre kan verifisere at de kom fra deg.

</details>

<details><summary>Spørsmål 3: Hvorfor bruker TLS hybrid kryptering i stedet for kun asymmetrisk?</summary>

**Svar:** Asymmetrisk kryptering er svært treg og egner seg dårlig for store datamengder. TLS bruker asymmetrisk kryptering bare til nøkkelutveksling (for å dele en sesjonsnøkkel trygt), deretter brukes den raske symmetriske AES-krypteringen for selve datatrafikken.

</details>

<details><summary>Spørsmål 4: Hva er hensikten med hashing av passord?</summary>

**Svar:** Passord lagres aldri i klartekst. I stedet lagres en hash av passordet (gjerne med salt). Når brukeren logger inn, hashes det oppgitte passordet og sammenlignes med den lagrede hashen. Selv om databasen stjeles, kan ikke passordene leses direkte.

</details>

<details><summary>Spørsmål 5: Hva er en Certificate Authority (CA)?</summary>

**Svar:** En CA er en betrodd tredjepart som utsteder og signerer digitale sertifikater. CA-en bekrefter at en offentlig nøkkel faktisk tilhører den identiteten (f.eks. det domenet) den utgir seg for å representere. Nettlesere stoler på CA-er som er forhåndsinstallert i operativsystemet.

</details>

---

## Flashcards

Symmetrisk kryptering :: Kryptering der samme nøkkel brukes til både kryptering og dekryptering. Rask, men nøkkeldistribusjon er utfordrende. Eks: AES-256
Asymmetrisk kryptering :: Kryptering med nøkkelpar: offentlig nøkkel (deles fritt) og privat nøkkel (holdes hemmelig). Eks: RSA, ECC
Hybrid kryptering :: Kombinerer asymmetrisk nøkkelutveksling med symmetrisk datakryptering – modellen TLS og HTTPS bruker
TLS :: Transport Layer Security – protokoll som sikrer kommunikasjon over internett. TLS 1.3 er gjeldende standard
PKI :: Public Key Infrastructure – system av sertifikater og CA-er som gjør asymmetrisk kryptering praktisk i stor skala
Certificate Authority (CA) :: Betrodd tredjepart som utsteder og signerer digitale sertifikater, bekrefter eierskap til offentlige nøkler
SHA-256 :: Kryptografisk hashfunksjon som produserer et 256-bits fingeravtrykk. Anbefalt standard (erstatter MD5 og SHA-1)
Hashing :: Enveisfunksjon som lager et unikt fingeravtrykk av data. Brukes til integritetskontroll og passordlagring
Ende-til-ende-kryptering :: Kryptering der bare avsender og mottaker kan lese innholdet – ikke serveren eller tredjeparter
Forward secrecy :: Egenskap ved TLS 1.3: selv om langtidsnøkkelen kompromitteres, kan tidligere sesjoner ikke dekrypteres

---

## Ressurser

- [NDLA – Kryptering](https://ndla.no)
- [NSM Grunnprinsipper – Beskytt data i ro og under overføring](https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/)
- [Mozilla – TLS 1.3 forklart (engelsk)](https://hacks.mozilla.org/2018/03/introducing-the-new-firefox-63/)
- [Azure kryptering og nøkkelhåndtering](https://learn.microsoft.com/en-us/azure/security/fundamentals/encryption-overview)
