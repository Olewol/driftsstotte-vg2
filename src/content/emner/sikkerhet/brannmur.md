---
title: "Brannmur og nettverkssikkerhet"
emne: sikkerhet
kompetansemaal:
  - km-10
kilder:
  - ndla
  - nsm
  - microsoft
  - https://ndla.no/resource/224ac302-1aaa-43c7-9228-8b2f4bf402fc
  - https://nsm.no/fagomrader/digital-sikkerhet/grunnprinsipper-for-ikt-sikkerhet/beskytte-og-opprettholde/2-2-etabler-en-sikker-ikt-infrastruktur/2-2-3-segmenter-virksomhetens-nettverk-basert-pa-risikoprofil/
video: https://www.youtube.com/watch?v=nS7fOofT-f4
notebooklm: true
tags: []
flashcards: true
public: true
---

## Introduksjon

En brannmur (firewall) er det viktigste enkeltverktøyet for å kontrollere nettverkstrafikk. Den fungerer som en kontrollpost mellom nettverk: den inspiserer datapakker og bestemmer – basert på definerte regler – om de skal slippes gjennom eller blokkeres.

NSM Grunnprinsipper for IKT-sikkerhet peker på «kontroller dataflyt» som et sentralt prinsipp. En brannmur er primærverktøyet for dette, men den fungerer best som del av et helhetlig forsvar med [[segmentering-og-vlan|nettverkssegmentering]], IDS/IPS og logging.

I praksis brukes brannmurer på flere nivåer: på nettverksnivå (ruter/switch), i skyen og som vertsbasert programvare på enkeltmaskiner. For å forstå brannmurens rolle fullt ut, er det nyttig å se den i sammenheng med [[it-losninger-med-sikkerhet|helhetlig IT-sikkerhet]] og Defense in Depth-prinsippet.

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
- **VLAN (Virtual LAN):** logisk separasjon på nettverksnivå. Ansatt-VLAN, gjeste-VLAN, server-VLAN og IoT-VLAN er typiske segmenter. Se [[segmentering-og-vlan]] for detaljer.
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

### Next-Generation Firewall (NGFW)

En **Next-Generation Firewall** kombinerer tradisjonell stateful inspection med dypere applikasjons-bevissthet. NGFW kan identifisere og kontrollere trafikk basert på applikasjon (ikke bare port), brukeridentitet og innhold. Eksempler: Palo Alto Networks, Fortinet FortiGate, Cisco Firepower. NGFW er i dag standarden i bedriftsmiljøer fordi enkle pakkefiltre og stateful inspection ikke er tilstrekkelig mot moderne trusler.

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

## Study guide

### Brannmur og nettverkssikkerhet – kjerneinnhold

**Hva er en brannmur?**
En brannmur kontrollerer nettverkstrafikk basert på forhåndsdefinerte regler. Den inspiserer datapakker og beslutter om de skal tillates eller blokkeres. Det finnes tre hovednivåer: pakkefiltrering (stateless), stateful inspection og applikasjonsbrannmur (WAF/Layer 7).

**Stateless vs. stateful:**
Stateless brannmurer vurderer hver pakke isolert – de er raske men har ingen hukommelse. Stateful brannmurer holder oversikt over aktive forbindelser og kan skille mellom legitim returtrafikk og forsøk på innbrudd utenfra. Moderne brannmurer er alltid stateful.

**Default-deny:**
Grunnprinsippet er å blokkere alt som standard og kun eksplisitt tillate nødvendig trafikk. Dette minimerer angrepsflaten dramatisk sammenlignet med default-allow.

**DMZ og segmentering:**
DMZ plasserer internett-eksponerte servere i et isolert segment. Intern nettverkssegmentering via VLAN begrenser lateral bevegelse etter et innbrudd. NSM peker på segmentering som ett av de viktigste forebyggende tiltakene.

**IDS/IPS:**
IDS oppdager og varsler om mistenkelig aktivitet. IPS gjør det samme men blokkerer automatisk. Begge bruker signaturer (kjente mønstre) og anomalideteksjon. Kombinert kalles de IDPS.

**Lagdelt forsvar:**
Brannmuren er ett lag i et helhetlig forsvar (Defense in Depth). Nettverksbrannmur + vertsbasert brannmur + segmentering + logging gir overlappende beskyttelse slik at svikt i ett lag ikke er fatalt.

**Nøkkelbegreper å beherske:**
Pakkefiltrering, stateful inspection, WAF, DMZ, nettverkssegmentering, default-deny, VLAN, IDS, IPS, lateral bevegelse, vertsbasert brannmur, NGFW.

---

## FAQ

**Hva er forskjellen mellom en brannmur og antivirus?**
En brannmur kontrollerer nettverkstrafikk basert på IP-adresser, porter og protokoller – den bestemmer hva som får lov til å kommunisere. Antivirus/EDR analyserer filer og programkjøring for ondsinnet kode på selve maskinen. Begge er nødvendige og utfyller hverandre.

**Kan en brannmur stoppe all malware?**
Nei. En brannmur stopper uautorisert nettverkstrafikk, men en bruker kan for eksempel laste ned malware via en tillatt HTTPS-tilkobling. Brannmuren er ett lag – ikke en fullstendig løsning alene.

**Hvorfor er DMZ viktig for webservere?**
Webservere må være tilgjengelige fra internett og er dermed eksponert for angrep. Ved å plassere dem i DMZ sikrer man at selv om en webserver kompromitteres, kan angriperen ikke bevege seg direkte inn i det interne nettverket.

**Hva er forskjellen mellom VLAN-segmentering og DMZ?**
DMZ er typisk for internett-eksponerte servere og er plassert mellom to brannmurer. VLAN-segmentering deler det interne nettverket i logiske soner (ansatte, elever, gjester, IoT) med brannmurregler mellom. Begge er former for nettverkssegmentering.

**Hva betyr «falskt positiv» i sammenheng med IPS?**
Et falskt positiv er når IPS feilaktig identifiserer legitim trafikk som en trussel og blokkerer den. Dette kan forstyrre driften, for eksempel at et forretningssystem ikke lenger fungerer. Derfor krever IPS nøye kalibrering og overvåkning.

**Når bør man bruke WAF fremfor vanlig brannmur?**
WAF brukes i tillegg til vanlig brannmur når du eksponerer webapplikasjoner mot internett. En vanlig brannmur ser ikke innholdet i HTTPS-trafikk, men en WAF dekrypterer og inspekterer HTTP-forespørsler for å oppdage SQL-injeksjon, XSS og andre applikasjonsangrep.

**Hva er en NGFW og hvorfor er den bedre enn tradisjonell brannmur?**
En Next-Generation Firewall kombinerer stateful inspection med applikasjonsidentifisering, brukeridentitet og innholdsinspeksjon. Den kan for eksempel tillate Zoom men blokkere andre videostrømmingstjenester, og den kan identifisere trafikk uavhengig av port.

**Hva skjer i praksis uten default-deny?**
Med default-allow tillates all trafikk som ikke eksplisitt er blokkert. Angripere trenger bare å finne én port eller protokoll som ikke er i blokklisten – noe som er enkelt. Med default-deny er utgangspunktet null tilgang, og kun dokumentert nødvendig trafikk åpnes.

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
NGFW :: Next-Generation Firewall – kombinerer stateful inspection med applikasjonsidentifisering og brukeridentitet for dypere trafikkanalyse

---

## Ressurser

- [NDLA – Brannmur (Driftsstøtte VG2)](https://ndla.no/r/driftsstotte-im-itk-vg2/brannmur/2aad28ca4e)
- [NSM Grunnprinsipper – Kontroller dataflyt](https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/)
- [Microsoft – Azure Network Security](https://learn.microsoft.com/en-us/azure/security/fundamentals/network-overview)
- [NDLA – Brannmur og pakkefiltrering](https://ndla.no/resource/224ac302-1aaa-43c7-9228-8b2f4bf402fc)
- [NSM – Nettverkssegmentering](https://nsm.no/fagomrader/digital-sikkerhet/grunnprinsipper-for-ikt-sikkerhet/beskytte-og-opprettholde/2-2-etabler-en-sikker-ikt-infrastruktur/2-2-3-segmenter-virksomhetens-nettverk-basert-pa-risikoprofil/)
- [YouTube: What is a DMZ? (PowerCert Animated Videos, 6 min)](https://www.youtube.com/watch?v=nS7fOofT-f4)
