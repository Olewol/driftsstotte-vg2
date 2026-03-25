---
title: "Kryptering"
emne: sikkerhet
kompetansemaal:
  - km-10
kilder:
  - ndla
  - nsm
  - microsoft
  - https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/informasjonssikkerhet-internkontroll/kryptering/
video: https://www.youtube.com/watch?v=N6Tf1_27n0A
notebooklm: true
tags: []
flashcards: https://notebooklm.google.com/notebook/3e72e53a-b0ca-4f05-a597-a8eea5ea7ea9
public: true
---

## Introduksjon

Kryptering er teknologien som gjør at informasjon forblir konfidensielt selv om den havner i feil hender. Uten kryptering ville alt du sender over internett – passord, bankdetaljer, helseinformasjon, private meldinger – være leselig for hvem som helst som avlytter nettverkstrafikken.

NSM anbefaler i sine grunnprinsipper å «beskytte data i ro og under overføring», og kryptering er det primære verktøyet for dette. For en IT-drifter er det essensielt å forstå hvordan kryptering fungerer, hvilke standarder som er aktuelle i dag, og hvordan man verifiserer at kryptering faktisk er på plass.

Kryptering er tett knyttet til [[personvern]] – GDPR krever at personopplysninger beskyttes med egnede tekniske tiltak, og kryptering er det mest sentrale av disse. Datatilsynet gir konkrete råd om når og hvordan kryptering bør brukes i norske virksomheter.

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

Hashing er en enveisprosess – i motsetning til kryptering kan man ikke reversere en hash til originaldata. Dette skiller hashing fra kryptering: kryptering er toveis (reversibel med riktig nøkkel), hashing er enveis.

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

E2EE er spesielt relevant for [[personvern]] – selv om serveren hackes, er innholdet uleselig. For sensitive kommunikasjonskanaler i virksomheter er E2EE derfor et viktig krav.

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

## Study guide

### Kryptering – kjerneinnhold

**To grunnleggende typer:**
Symmetrisk kryptering bruker samme nøkkel begge veier – rask, men nøkkeldistribusjon er utfordrende. Asymmetrisk kryptering bruker nøkkelpar (offentlig/privat) – løser nøkkeldistribusjonsproblemet, men er tregere. I praksis kombineres de i hybrid kryptering.

**Hybrid kryptering og TLS:**
TLS (og HTTPS) bruker asymmetrisk kryptering kun til nøkkelutveksling, deretter symmetrisk AES for selve dataoverføringen. TLS 1.3 er gjeldende standard med obligatorisk forward secrecy.

**PKI og sertifikater:**
PKI løser tillitsproblemet: en Certificate Authority (CA) signerer sertifikater og bekrefter at en offentlig nøkkel tilhører riktig identitet. Nettlesere stoler på CA-er som er forhåndsinstallert. Let's Encrypt har gjort gratis, automatiserte sertifikater standard.

**Hashing vs. kryptering:**
Hashing er en enveisprosess og brukes til integritetskontroll og passordlagring – ikke til å skjule data. Kryptering er toveis. SHA-256 er anbefalt for integritet, bcrypt/Argon2 for passord. MD5 og SHA-1 er utdaterte og skal ikke brukes.

**E2EE:**
Ende-til-ende-kryptering sikrer at kun avsender og mottaker kan lese innholdet – ikke tjenesteleverandøren. Kritisk for personvern i kommunikasjonstjenester.

**Praktisk sjekkliste:**
- Alltid HTTPS på nettsider (TLS 1.3 foretrukket)
- AES-256 for data i ro (filer, databaser, backuper)
- Aldri lagre passord i klartekst – bruk bcrypt/Argon2 med salt
- Sjekk sertifikatstatus i nettleser for å verifisere HTTPS

---

## FAQ

**Hva er forskjellen mellom kryptering og hashing?**
Kryptering er en toveis operasjon: data krypteres og kan dekrypteres igjen med riktig nøkkel. Hashing er en enveisprosess: du lager et fingeravtrykk av data, men kan ikke rekonstruere originaldata fra fingeravtrykket. Kryptering brukes til å skjule innhold, hashing til å verifisere integritet.

**Hvorfor er ikke MD5 lenger trygt?**
MD5-algoritmen har en kjent svakhet: det er mulig å finne to forskjellige inndata som produserer samme hash (kollisjon). Dette gjør det mulig å forfalske digitale signaturer og filer. Bruk SHA-256 eller nyere.

**Hva skjer hvis sertifikatet til en nettside er utløpt?**
Nettleseren viser en sikkerhetsadvarsel. Dette betyr ikke nødvendigvis at siden er farlig, men at TLS-forbindelsen ikke kan verifiseres. For brukere er det en rød flagg. For driftsansvarlige er det et tegn på dårlig vedlikehold – sertifikater bør fornyes automatisk (f.eks. med Let's Encrypt og certbot).

**Hva er forward secrecy og hvorfor er det viktig?**
Forward secrecy betyr at sesjonsnøkler slettes etter bruk og ikke kan avledes fra langtidsnøkkelen. Selv om en angripere registrerer all kryptert trafikk nå og later stjeler serverens private nøkkel, kan de ikke dekryptere den gamle trafikken. TLS 1.3 krever dette obligatorisk.

**Kan kvantecomputere knekke krypteringen vi bruker i dag?**
Kvantecomputere er en fremtidig trussel mot RSA og ECC (asymmetrisk kryptering). Symmetrisk AES-256 er langt mer motstandsdyktig. NIST jobber med å standardisere post-kvante-krypteringsalgoritmer. For VG2-nivå er det viktig å vite at fremtidssikker kryptering er et aktivt forskningsfelt.

**Hva er en CA, og hvem kan bli det?**
En Certificate Authority (CA) er en betrodd tredjepart som utsteder digitale sertifikater. Å bli en rot-CA krever strenge revisjonskrav og godkjenning fra nettleserprodusentene (Apple, Google, Mozilla, Microsoft). Let's Encrypt er en non-profit CA som tilbyr gratis, automatiserte sertifikater og har revolusjonert utbredelsen av HTTPS.

**Hvorfor trenger passord «salt»?**
Salt er en tilfeldig verdi som legges til passordet før hashing. Uten salt vil to brukere med samme passord få identiske hashes – og en angripere med en ferdigberegnet «rainbow table» kan knekke dem raskt. Med salt er hver hash unik, og rainbow tables er ubrukelige.

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
Salt :: Tilfeldig verdi som legges til et passord før hashing for å forhindre rainbow table-angrep og gjøre identiske passord unike
AES-256 :: Advanced Encryption Standard med 256-bits nøkkel – industristandarden for symmetrisk kryptering av data i ro

---

## Ressurser

- [NDLA – Kryptering](https://ndla.no)
- [NSM Grunnprinsipper – Beskytt data i ro og under overføring](https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/)
- [Mozilla – TLS 1.3 forklart (engelsk)](https://hacks.mozilla.org/2018/03/introducing-the-new-firefox-63/)
- [Azure kryptering og nøkkelhåndtering](https://learn.microsoft.com/en-us/azure/security/fundamentals/encryption-overview)
- [Datatilsynet – Kryptering av personopplysninger](https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/informasjonssikkerhet-internkontroll/kryptering/)
- [YouTube: Kryptering (NDLA, 6 min)](https://www.youtube.com/watch?v=N6Tf1_27n0A)
