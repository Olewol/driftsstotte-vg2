---
title: "Brannmur og nettverkssikkerhet"
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

En brannmur (firewall) er det viktigste enkeltverktøyet for å kontrollere nettverkstrafikk. Den fungerer som en kontrollpost mellom nettverk: den inspiserer datapakker og bestemmer – basert på definerte regler – om de skal slippes gjennom eller blokkeres.

NSM Grunnprinsipper for IKT-sikkerhet peker på «kontroller dataflyt» som et sentralt prinsipp. En brannmur er primærverktøyet for dette, men den fungerer best som del av et helhetlig forsvar med nettverkssegmentering, IDS/IPS og logging.

---

## Teori

### Pakkefiltrering (stateless)

Den enkleste typen brannmur undersøker hver enkelt datapakke isolert og sammenligner den med et regelett:

- **Hva inspiseres:** kilde-IP, mål-IP, kilde-port, mål-port, protokoll (TCP/UDP/ICMP)
- **Fordel:** svært rask og lite ressurskrevende
- **Ulempe:** ingen kontekst – brannmuren vet ikke om en pakke er del av en etablert sesjon. En angriper kan forfølge returtrafikk

**Eksempel på en pakkefilter-regel:**
```
TILLAT  TCP  fra 192.168.1.0/24  til WHICH  port 443
BLOKKÉR TCP  fra ANY             til ANY    port 23   (Telnet er utdatert)
BLOKKÉR ALL  fra ANY             til ANY    (default-deny til slutt)
```

---

### Stateful inspection

En **stateful** brannmur husker tilstanden til aktive nettverksforbindelser. Den bygger opp en tilstandstabell og tillater automatisk returtrafikk for etablerte sesjoner.

- En PC initierer en HTTPS-tilkobling til en webserver
- Brannmuren registrerer at denne forbindelsen ble initiert innenfra og tillater returtrafikken
- En ekstern aktør som forsøker å initiere en tilkobling direkte inn blokkeres

**Fordeler vs. pakkefiltrering:**
- Kan skille mellom legitim returtrafikk og uønsket innkommende trafikk
- Vanskeligere å lure med forfalsket IP
- Standard i alle moderne hjemmeroutere og bedriftsbrannmurer

---

### Applikasjonsbrannmur (WAF / Layer 7)

En **WAF (Web Application Firewall)** opererer på applikasjonslaget og forstår protokoller som HTTP/HTTPS. Den kan:

- Inspisere innholdet i HTTP-forespørsler – ikke bare header
- Oppdage og blokkere **SQL-injeksjon**, **XSS (Cross-Site Scripting)** og andre OWASP Top 10-angrep
- Implementere ratebegrensning for å beskytte mot DDoS
- Maskere feilmeldinger som avslører serverteknologi

WAF er standardkomponent i skytjenester som Azure Application Gateway og Cloudflare. Viktig for alle organisasjoner som eksponerer webapplikasjoner mot internett.

---

### DMZ – Demilitarisert sone

En **DMZ** er et nettverk som befinner seg mellom det eksterne internett og det interne bedriftsnettverket. Servere som må være tilgjengelige fra internett (webserver, e-postserver, DNS) plasseres i DMZ.

```
Internett
    |
[Ytre brannmur]
    |
  [DMZ]
  ├── Webserver
  ├── E-postserver
  └── Reverse proxy
    |
[Indre brannmur]
    |
[Internt nettverk]
  ├── Filserver
  ├── AD-server
  └── Ansatt-PC-er
```

**Fordelen med DMZ:** Selv om en webserver i DMZ kompromitteres, stopper den indre brannmuren angriperen fra å bevege seg inn i det interne nettverket. Prinsippet heter **nettverkssegmentering**.

---

### Nettverkssegmentering

**Nettverkssegmentering** deler nettverket inn i separate soner med brannmurregler mellom. Målet er å begrense **lateral bevegelse** – angriperens evne til å spre seg i nettverket etter å ha kommet inn.

Implementeres via:
- **VLAN (Virtual LAN):** logisk separasjon på nettverksnivå. Ansatt-VLAN, gjeste-VLAN, server-VLAN og IoT-VLAN er typiske segmenter.
- **Brannmurregler mellom VLAN-ene:** definerer hvilken trafikk som er tillatt på tvers

NSM anbefaler segmentering som et av de viktigste forebyggende tiltakene. I Østre Toten-angrepet (2021) bidro mangel på segmentering til at ransomwaren spredte seg til hele nettverket.

---

### Default-deny prinsippet

Best practice for brannmurregler:

> **Blokkér alt, tillat kun det som er nødvendig**

Dette kalles *default-deny* eller *allowlist-tilnærming*. Alle porter og protokoller blokkeres som standard – kun eksplisitt tillatt trafikk slipper gjennom.

Motsetningen er *default-allow* (blokkliste): tillat alt, blokkér det kjente onde. Dette er ikke egnet for sikkerhetssensitive miljøer.

---

### IDS og IPS

| | **IDS** | **IPS** |
|---|---|---|
| **Navn** | Intrusion Detection System | Intrusion Prevention System |
| **Funksjon** | Overvåker trafikk og varsler ved mistenkelig aktivitet | Overvåker og **blokkerer** automatisk mistenkelig trafikk |
| **Plassering** | Kopierer trafikk (out-of-band) | Inline i trafikken |
| **Fordel** | Risiko for falskt positiv er begrenset til varsler | Automatisk respons – raskere enn manuell handling |
| **Ulempe** | Reagerer ikke – bare varsler | Falskt positiv kan blokkere legitim trafikk |

Moderne systemer er gjerne kombinert (IDPS). De bruker signaturer (kjente angrepsmønstre) og anomalideteksjon (avvik fra normalen) for å identifisere trusler.

---

### Windows Defender Firewall

På Windows-maskiner er den innebygde brannmuren et vertsbasert (host-based) tillegg til nettverksbrannmuren. Den kontrollerer trafikk inn og ut av den individuelle maskinen.

**Konfigurasjon via GUI:**
1. Søk etter «Windows Defender Firewall with Advanced Security» i Start-menyen
2. Inngående regler (*Inbound Rules*): kontrollerer hva som kan koble til maskinen
3. Utgående regler (*Outbound Rules*): kontrollerer hva maskinen kan koble til
4. Profiler: Domene (skole/jobb), Privat (hjemme), Offentlig (kafé/hotspot)

**To brannmurer = bedre forsvar:**
En bedrifts forsvar bør ha både en nettverksbrannmur (på ruternivå) og vertsbaserte brannmurer på alle maskiner. Selv om nettverksbrannmuren omgås, stopper den vertsbaserte angrepet.

---

## Eksempel / lab

### Praktisk: Windows Defender Firewall-regler

**Oppgave:** Blokker inngående ping (ICMP Echo Request) på en Windows-maskin

1. Åpne **Windows Defender Firewall with Advanced Security**
2. Klikk **Inbound Rules** → **New Rule**
3. Velg **Custom** → **Next**
4. Program: **All programs** → **Next**
5. Protokoll: **ICMPv4** → velg «Specific ICMP types» → huk av «Echo Request» → **Next**
6. Scope: behold standardverdier → **Next**
7. Action: **Block the connection** → **Next**
8. Profile: velg **Public** og **Private** → **Next**
9. Gi regelen et navn: «Blokker ICMP ping» → **Finish**

**Test:** Forsøk å pinge maskinen fra en annen maskin i nettverket – du skal ikke få svar.

---

## Quiz

<details><summary>Spørsmål 1: Hva er forskjellen på stateless og stateful brannmur?</summary>

**Svar:** En stateless brannmur (pakkefiltrering) inspiserer hver pakke isolert uten kontekst. En stateful brannmur husker tilstanden til aktive forbindelser og kan skille mellom ønsket returtrafikk og uønsket innkommende trafikk.

</details>

<details><summary>Spørsmål 2: Hva er hensikten med en DMZ?</summary>

**Svar:** DMZ er et nettverkssegment mellom internett og det interne nettverket der internett-eksponerte servere plasseres. Selv om en server i DMZ kompromitteres, hindrer den indre brannmuren angriperen i å nå det interne nettverket.

</details>

<details><summary>Spørsmål 3: Hva betyr default-deny, og hvorfor er det best practice?</summary>

**Svar:** Default-deny betyr at all trafikk blokkeres som standard, og kun eksplisitt tillatt trafikk slipper gjennom. Det er best practice fordi det minimerer angrepsflaten – kun det nødvendige åpnes, ikke det kjente farlige.

</details>

<details><summary>Spørsmål 4: Hva er forskjellen mellom IDS og IPS?</summary>

**Svar:** IDS (Intrusion Detection System) overvåker trafikk og varsler ved mistenkelig aktivitet, men griper ikke inn. IPS (Intrusion Prevention System) varsler og blokkerer automatisk mistenkelig trafikk inline.

</details>

<details><summary>Spørsmål 5: Hva er nettverkssegmentering, og hvorfor er det viktig?</summary>

**Svar:** Nettverkssegmentering deler nettverket i separate soner med brannmurregler mellom. Det begrenser angriperens mulighet til lateral bevegelse – selv om én sone kompromitteres, stopper brannmuren spredning til resten av nettverket.

</details>

---

## Flashcards

Pakkefiltrering :: Stateless brannmur som inspiserer kilde/mål-IP, port og protokoll for hver pakke isolert
Stateful inspection :: Brannmur som husker tilstanden til aktive forbindelser og tillater returtrafikk automatisk
WAF :: Web Application Firewall – applikasjonsbrannmur som inspiserer HTTP-innhold og stopper SQL-injeksjon og XSS
DMZ :: Demilitarisert sone – nettverk mellom internett og internt nett der internett-eksponerte servere plasseres
Nettverkssegmentering :: Deling av nettverk i VLAN-soner med brannmurregler mellom for å begrense lateral bevegelse
Default-deny :: Brannmurprinsipp: blokker alt, tillat kun eksplisitt godkjent trafikk
IDS :: Intrusion Detection System – overvåker trafikk og varsler ved mistenkelig aktivitet, men blokkerer ikke
IPS :: Intrusion Prevention System – overvåker trafikk og blokkerer automatisk mistenkelig aktivitet inline
Lateral bevegelse :: Angriperens evne til å bevege seg mellom systemer etter å ha fått innledende tilgang
Vertsbasert brannmur :: Brannmur som kjører på selve maskinen (f.eks. Windows Defender Firewall), i tillegg til nettverksbrannmuren

---

## Ressurser

- [NDLA – Brannmur (Driftsstøtte VG2)](https://ndla.no/r/driftsstotte-im-itk-vg2/brannmur/2aad28ca4e)
- [NSM Grunnprinsipper – Kontroller dataflyt](https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/)
- [Microsoft – Azure Network Security](https://learn.microsoft.com/en-us/azure/security/fundamentals/network-overview)
