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
  - https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/2-2-etabler-en-sikker-ikt-infrastruktur/2-2-3-segmenter-virksomhetens-nettverk-basert-pa-risikoprofil/
  - https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/
  - https://www.datatilsynet.no/
  - https://owasp.org/www-project-top-ten/
  - https://www.digdir.no/informasjonssikkerhet/
video: https://www.youtube.com/watch?v=nS7fOofT-f4
notebooklm: true
tags: []
flashcards: https://notebooklm.google.com/notebook/3e72e53a-b0ca-4f05-a597-a8eea5ea7ea9
public: true
---

## Introduksjon

En brannmur (firewall) er det viktigste enkeltverktøyet for å kontrollere nettverkstrafikk [^1]. Den fungerer som en kontrollpost mellom nettverk: den inspiserer datapakker og bestemmer – basert på definerte regler – om de skal slippes gjennom eller blokkeres.

NSM Grunnprinsipper for IKT-sikkerhet peker på «kontroller dataflyt» som et sentralt prinsipp [^2]. En brannmur er primærverktøyet for dette, men den fungerer best som del av et helhetlig forsvar med [[segmentering-og-vlan|nettverkssegmentering]], IDS/IPS og logging [^3].

I praksis brukes brannmurer på flere nivåer: på nettverksnivå (ruter/switch), i skyen og som vertsbasert programvare på enkeltmaskiner [^4]. For å forstå brannmurens rolle fullt ut, er det nyttig å se den i sammenheng med [[it-losninger-med-sikkerhet|helhetlig IT-sikkerhet]] og Defense in Depth-prinsippet.

---

## Teori

### Pakkefiltrering (stateless)

Den enkleste typen brannmur undersøker hver enkelt datapakke isolert og sammenligner den med et regelett [^5]:

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

En **stateful** brannmur husker tilstanden til aktive nettverksforbindelser [^5]. Den bygger opp en tilstandstabell og tillater automatisk returtrafikk for etablerte sesjoner.

- En PC initierer en HTTPS-tilkobling til en webserver
- Brannmuren registrerer at denne forbindelsen ble initiert innenfra og tillater returtrafikken
- En ekstern aktør som forsøker å initiere en tilkobling direkte inn blokkeres

**Fordeler vs. pakkefiltrering:**
- Kan skille mellom legitim returtrafikk og uønsket innkommende trafikk
- Vanskeligere å lure med forfalsket IP
- Standard i alle moderne hjemmeroutere og bedriftsbrannmurer

---

### Applikasjonsbrannmur (WAF / Layer 7)

En **WAF (Web Application Firewall)** opererer på applikasjonslaget og forstår protokoller som HTTP/HTTPS [^6]. Den kan:

- Inspisere innholdet i HTTP-forespørsler – ikke bare header
- Oppdage og blokkere **SQL-injeksjon**, **XSS (Cross-Site Scripting)** og andre OWASP Top 10-angrep
- Implementere ratebegrensning for å beskytte mot DDoS
- Maskere feilmeldinger som avslører serverteknologi

WAF er standardkomponent i skytjenester som Azure Application Gateway og Cloudflare [^4]. Viktig for alle organisasjoner som eksponerer webapplikasjoner mot internett.

---

### DMZ – Demilitarisert sone

En **DMZ** er et nettverk som befinner seg mellom det eksterne internett og det interne bedriftsnettverket [^3]. Servere som må være tilgjengelige fra internett (webserver, e-postserver, DNS) plasseres i DMZ.

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

**Fordelen med DMZ:** Selv om en webserver i DMZ kompromitteres, stopper den indre brannmuren angriperen fra å bevege seg inn i det interne nettverket [^2]. Prinsippet heter **nettverkssegmentering**.

---

### Nettverkssegmentering

**Nettverkssegmentering** deler nettverket inn i separate soner med brannmurregler mellom [^2]. Målet er å begrense **lateral bevegelse** – angriperens evne til å spre seg i nettverket etter å ha kommet inn.

Implementeres via:
- **VLAN (Virtual LAN):** logisk separasjon på nettverksnivå. Ansatt-VLAN, gjeste-VLAN, server-VLAN og IoT-VLAN er typiske segmenter. Se [[segmentering-og-vlan]] for detaljer.
- **Brannmurregler mellom VLAN-ene:** definerer hvilken trafikk som er tillatt på tvers

NSM anbefaler segmentering som et av de viktigste forebyggende tiltakene [^2]. I Østre Toten-angrepet (2021) bidro mangel på segmentering til at ransomwaren spredte seg til hele nettverket [^7].

---

### Default-deny prinsippet

Best practice for brannmurregler [^3]:

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

Moderne systemer er gjerne kombinert (IDPS) [^8]. De bruker signaturer (kjente angrepsmønstre) og anomalideteksjon (avvik fra normalen) for å identifisere trusler.

---

### Next-Generation Firewall (NGFW)

En **Next-Generation Firewall** kombinerer tradisjonell stateful inspection med dypere applikasjons-bevissthet [^9]. NGFW kan identifisere og kontrollere trafikk basert på applikasjon (ikke bare port), brukeridentitet og innhold. Eksempler: Palo Alto Networks, Fortinet FortiGate, Cisco Firepower. NGFW er i dag standarden i bedriftsmiljøer fordi enkle pakkefiltre og stateful inspection ikke er tilstrekkelig mot moderne trusler [^3].

---

### Windows Defender Firewall

På Windows-maskiner er den innebygde brannmuren et vertsbasert (host-based) tillegg til nettverksbrannmuren [^10]. Den kontrollerer trafikk inn og ut av den individuelle maskinen.

**Konfigurasjon via GUI:**
1. Søk etter «Windows Defender Firewall with Advanced Security» i Start-menyen
2. Inngående regler (*Inbound Rules*): kontrollerer hva som kan koble til maskinen
3. Utgående regler (*Outbound Rules*): kontrollerer hva maskinen kan koble til
4. Profiler: Domene (skole/jobb), Privat (hjemme), Offentlig (kafé/hotspot)

**To brannmurer = bedre forsvar:**
En bedrifts forsvar bør ha både en nettverksbrannmur (på ruternivå) og vertsbaserte brannmurer på alle maskiner. Selv om nettverksbrannmuren omgås, stopper den vertsbaserte angrepet [^3].

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
En brannmur kontrollerer nettverkstrafikk basert på forhåndsdefinerte regler [^1]. Den inspiserer datapakker og beslutter om de skal tillates eller blokkeres. Det finnes tre hovednivåer: pakkefiltrering (stateless), stateful inspection og applikasjonsbrannmur (WAF/Layer 7) [^5].

**Stateless vs. stateful:**
Stateless brannmurer vurderer hver pakke isolert – de er raske men har ingen hukommelse. Stateful brannmurer holder oversikt over aktive forbindelser og kan skille mellom legitim returtrafikk og forsøk på innbrudd utenfra. Moderne brannmurer er alltid stateful [^5].

**Default-deny:**
Grunnprinsippet er å blokkere alt som standard og kun eksplisitt tillate nødvendig trafikk [^3]. Dette minimerer angrepsflaten dramatisk sammenlignet med default-allow.

**DMZ og segmentering:**
DMZ plasserer internett-eksponerte servere i et isolert segment [^3]. Intern nettverkssegmentering via VLAN begrenser lateral bevegelse etter et innbrudd. NSM peker på segmentering som ett av de viktigste forebyggende tiltakene [^2].

**IDS/IPS:**
IDS oppdager og varsler om mistenkelig aktivitet [^8]. IPS gjør det samme men blokkerer automatisk. Begge bruker signaturer (kjente mønstre) og anomalideteksjon. Kombinert kalles de IDPS.

**Lagdelt forsvar:**
Brannmuren er ett lag i et helhetlig forsvar (Defense in Depth). Nettverksbrannmur + vertsbasert brannmur + segmentering + logging gir overlappende beskyttelse slik at svikt i ett lag ikke er fatalt [^3].

**Nøkkelbegreper å beherske:**
Pakkefiltrering, stateful inspection, WAF, DMZ, nettverkssegmentering, default-deny, VLAN, IDS, IPS, lateral bevegelse, vertsbasert brannmur, NGFW.

---

## FAQ

**Hva er forskjellen mellom en brannmur og antivirus?**
En brannmur kontrollerer nettverkstrafikk basert på IP-adresser, porter og protokoller – den bestemmer hva som får lov til å kommunisere. Antivirus/EDR analyserer filer og programkjøring for ondsinnet kode på selve maskinen. Begge er nødvendige og utfyller hverandre [^3].

**Kan en brannmur stoppe all malware?**
Nei. En brannmur stopper uautorisert nettverkstrafikk, men en bruker kan for eksempel laste ned malware via en tillatt HTTPS-tilkobling. Brannmuren er ett lag – ikke en fullstendig løsning alene [^3].

**Hvorfor er DMZ viktig for webservere?**
Webservere må være tilgjengelige fra internett og er dermed eksponert for angrep. Ved å plassere dem i DMZ sikrer man at selv om en webserver kompromitteres, kan angriperen ikke bevege seg direkte inn i det interne nettverket [^2].

**Hva er forskjellen mellom VLAN-segmentering og DMZ?**
DMZ er typisk for internett-eksponerte servere og er plassert mellom to brannmurer. VLAN-segmentering deler det interne nettverket i logiske soner (ansatte, elever, gjester, IoT) med brannmurregler mellom. Begge er former for nettverkssegmentering.

**Hva betyr «falskt positiv» i sammenheng med IPS?**
Et falskt positiv er når IPS feilaktig identifiserer legitim trafikk som en trussel og blokkerer den. Dette kan forstyrre driften, for eksempel at et forretningssystem ikke lenger fungerer. Derfor krever IPS nøye kalibrering og overvåkning [^8].

**Når bør man bruke WAF fremfor vanlig brannmur?**
WAF brukes i tillegg til vanlig brannmur når du eksponerer webapplikasjoner mot internett [^6]. En vanlig brannmur ser ikke innholdet i HTTPS-trafikk, men en WAF dekrypterer og inspekterer HTTP-forespørsler for å oppdage SQL-injeksjon, XSS og andre applikasjonsangrep.

**Hva er en NGFW og hvorfor er den bedre enn tradisjonell brannmur?**
En Next-Generation Firewall kombinerer stateful inspection med applikasjonsidentifisering, brukeridentitet og innholdsinspeksjon [^9]. Den kan for eksempel tillate Zoom men blokkere andre videostrømmingstjenester, og den kan identifisere trafikk uavhengig av port.

**Hva skjer i praksis uten default-deny?**
Med default-allow tillates all trafikk som ikke eksplisitt er blokkert. Angripere trenger bare å finne én port eller protokoll som ikke er i blokklisten – noe som er enkelt. Med default-deny er utgangspunktet null tilgang, og kun dokumentert nødvendig trafikk åpnes [^3].

---

## Quiz

<details><summary>Spørsmål 1: Hva er forskjellen på stateless og stateful brannmur?</summary>

**Svar:** En stateless brannmur (pakkefiltrering) inspiserer hver pakke isolert uten kontekst. En stateful brannmur husker tilstanden til aktive forbindelser og kan skille mellom ønsket returtrafikk og uønsket innkommende trafikk [^5].

</details>

<details><summary>Spørsmål 2: Hva er hensikten med en DMZ?</summary>

**Svar:** DMZ er et nettverkssegment mellom internett og det interne nettverket der internett-eksponerte servere plasseres. Selv om en server i DMZ kompromitteres, hindrer den indre brannmuren angriperen i å nå det interne nettverket [^3].

</details>

<details><summary>Spørsmål 3: Hva betyr default-deny, og hvorfor er det best practice?</summary>

**Svar:** Default-deny betyr at all trafikk blokkeres som standard, og kun eksplisitt tillatt trafikk slipper gjennom. Det er best practice fordi det minimerer angrepsflaten – kun det nødvendige åpnes, ikke det kjente farlige [^3].

</details>

<details><summary>Spørsmål 4: Hva er forskjellen mellom IDS og IPS?</summary>

**Svar:** IDS (Intrusion Detection System) overvåker trafikk og varsler ved mistenkelig aktivitet, men griper ikke inn. IPS (Intrusion Prevention System) varsler og blokkerer automatisk mistenkelig trafikk inline [^8].

</details>

<details><summary>Spørsmål 5: Hva er nettverkssegmentering, og hvorfor er det viktig?</summary>

**Svar:** Nettverkssegmentering deler nettverket i separate soner med brannmurregler mellom. Det begrenser angriperens mulighet til lateral bevegelse – selv om én sone kompromitteres, stopper brannmuren spredning til resten av nettverket [^2].

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

## Kilder

[^1]: NDLA. (2024). *Brannmur (Driftsstøtte VG2)*. https://ndla.no/r/driftsstotte-im-itk-vg2/brannmur/2aad28ca4e
[^2]: NSM. (2025). *Grunnprinsipper for IKT-sikkerhet 2.0 – Kontroller dataflyt og segmenter nettverk*. https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/
[^3]: Microsoft. (2025). *Azure Network Security Overview*. https://learn.microsoft.com/en-us/azure/security/fundamentals/network-overview
[^4]: Cloudflare. (2025). *What is a firewall?* https://www.cloudflare.com/learning/security/what-is-a-firewall/
[^5]: PowerCert Animated Videos. (2022). *Stateful vs Stateless Firewall*. YouTube. https://www.youtube.com/watch?v=nS7fOofT-f4
[^6]: OWASP. (2025). *Web Application Firewall*. https://owasp.org/www-community/Web_Application_Firewall
[^7]: Østre Toten kommune. (2021). *Ransomware-angrepet – evalueringsrapport*. https://www.regjeringen.no/no/aktuelt/erfaringer-fra-ostre-toten/id2880806/
[^8]: SANS Institute. (2024). *IDS vs IPS: What's the Difference?* https://www.sans.org/blog/ids-vs-ips/
[^9]: Palo Alto Networks. (2025). *What is a Next-Generation Firewall?* https://www.paloaltonetworks.com/cyberpedia/what-is-a-next-generation-firewall
[^10]: Microsoft. (2025). *Windows Defender Firewall with Advanced Security*. https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-firewall/windows-firewall-with-advanced-security
