---
title: "TCP/IP-modellen"
emne: nettverk
kompetansemaal:
  - km-05
kilder:
  - ndla
  - https://ndla.no/nb/subject:1:430c00b5-773a-4933-9f2d-8647038e2f05/topic:2:183060/topic:2:183350/resource:1:115995
tags: [tcp, ip, protokoll, modell, lag]
flashcards: https://notebooklm.google.com/notebook/f7e5ad6c-7082-40cf-abd5-7a41b540f8e1
public: true
video: https://www.youtube.com/watch?v=6cG9qrKB9x0
notebooklm: true
---

# TCP/IP-modellen

## Introduksjon

TCP/IP-modellen er det praktiske rammeverket som internett og de fleste moderne nettverk bygger på. Den beskriver hvordan data pakkes inn, sendes gjennom et nettverk og pakkes ut igjen på mottakersiden. Å forstå modellen er nøkkelen til å forstå hvorfor nettverksprotokoller er organisert slik de er, og hva som skjer "under panseret" når du åpner en nettside.

TCP/IP-modellen er nært beslektet med [[osi-modellen]], som er referansemodellen for teori og feilsøking. De konkrete protokollene som opererer i modellen beskrives i [[nettverksprotokoller]], og tjenester som [[dns-og-dhcp]] og [[serverroller]] befinner seg på applikasjonslaget.

## Teori

### Lagene i TCP/IP-modellen

NDLA og mange norske lærebøker bruker en **5-lagsmodell** for TCP/IP. Den klassiske internettmodellen har 4 lag (der de to nederste slås sammen). Begge variantene er gyldige; 5-lagsmodellen er mer pedagogisk og mer lik OSI.

| Lag | Navn | Funksjon | Protokolleksempler |
|-----|------|----------|--------------------|
| 5 | Applikasjonslaget | Brukervendte tjenester og protokoller | HTTP, HTTPS, DNS, SMTP, FTP, SSH |
| 4 | Transportlaget | Ende-til-ende-kommunikasjon, portnumre | TCP, UDP |
| 3 | Nettverkslaget (Internettlaget) | Logisk adressering og ruting mellom nettverk | IP (v4/v6), ICMP |
| 2 | Datalinklaget | Overføring innenfor ett nettverk, MAC-adresser | Ethernet, ARP, 802.11 (WiFi) |
| 1 | Fysisk lag | Faktisk bitsending over medium | Fiber, kobber (UTP), WiFi-radio |

### Hva gjør hvert lag?

**Lag 1 — Fysisk lag**
Ansvarlig for selve bitsendingen: spenningsnivåer på kobberledning, lyspulser i fiber, radiosignaler i WiFi. Protokoller på dette laget definerer kontakter, kabler og signalstandarder (f.eks. 10BASE-T, 1000BASE-T).

**Lag 2 — Datalinklaget**
Pakker biter inn i *frames* (rammer). Ethernet er dominerende her. Hvert nettverkskort har en unik **MAC-adresse** (48 bit, skrevet som f.eks. `00:1A:2B:3C:4D:5E`). En svitsj opererer på lag 2 og videresender frames basert på MAC-adresser. ARP (Address Resolution Protocol) brukes til å finne MAC-adressen til en kjent IP-adresse.

En **MAC-adresse** er en unik fysisk adresse på datalinklaget (lag 2) som er brent inn i nettverkskortet for identifikasjon i et lokalt nettverk.

**Lag 3 — Nettverkslaget**
Håndterer logisk adressering med **IP-adresser** og ruting mellom ulike nettverk. En ruter opererer på lag 3. IPv4-adresser er 32 bit (f.eks. `192.168.1.10`), IPv6-adresser er 128 bit. ICMP brukes til feilmeldinger og diagnostikk (`ping`).

En **IP-adresse** er en logisk adresse på nettverkslaget (lag 3) som identifiserer en enhet unikt i et nettverk og muliggjør ruting mellom nettverk.

**Lag 4 — Transportlaget**
Ansvarlig for ende-til-ende-kommunikasjon mellom applikasjoner på to maskiner. Bruker **portnumre** for å identifisere hvilken applikasjon trafikken tilhører.

En **port** er et numerisk identifikasjonsnummer på transportlaget som brukes til å dirigere trafikk til riktig applikasjon eller tjeneste på en maskin.

- **TCP (Transmission Control Protocol)**: forbindelsesorientert, garanterer leveringsrekkefølge og feilretting. Brukes der pålitelighet er viktig (nettsider, e-post, filoverføring).
- **UDP (User Datagram Protocol)**: forbindelseløs, rask men uten garantier. Brukes der hastighet er viktigere enn nøyaktighet (videostrømming, VoIP, DNS-oppslag).

**Lag 5 — Applikasjonslaget**
Her befinner seg protokollene som programmer bruker direkte: HTTP for web, SMTP for e-post, DNS for navneoppløsning, osv. Dette laget "snakker" med brukernes applikasjoner (nettleser, e-postklient, terminalprogram).

### Innkapsling

Når data sendes nedover gjennom lagene, legger hvert lag til sin egen **header** (topptekst) med styringsinformasjon. Dette kalles innkapsling:

```
Applikasjon:  [DATA]
Transport:    [TCP-header][DATA]
Nettverk:     [IP-header][TCP-header][DATA]
Datalink:     [Ethernet-header][IP-header][TCP-header][DATA][Ethernet-trailer]
Fysisk:       biter over medium
```

På mottakersiden pakkes det ut i omvendt rekkefølge — hvert lag leser og fjerner sin egen header. Forholdet mellom maskinvare og lag: svitsjer opererer på lag 2, rutere på lag 3. Lag 2 bruker MAC-adresser for lokal overføring; lag 3 bruker IP-adresser for ruting mellom nettverk.

### Sammenligning: TCP/IP vs. OSI

| TCP/IP (5 lag) | OSI (7 lag) |
|----------------|-------------|
| Applikasjonslaget | Applikasjonslaget (7) |
| Applikasjonslaget | Presentasjonslaget (6) |
| Applikasjonslaget | Sesjonslaget (5) |
| Transportlaget | Transportlaget (4) |
| Nettverkslaget | Nettverkslaget (3) |
| Datalinklaget | Datalinklaget (2) |
| Fysisk lag | Fysisk lag (1) |

TCP/IP er den modellen internett faktisk bruker. OSI er referansemodellen som brukes til teori og feilsøking. Se [[osi-modellen]] for full beskrivelse. Norske lærebøker veksler mellom 4-lags og 5-lags TCP/IP — begge er korrekte, men 5-lagsmodellen er mer pedagogisk fordi den skiller mellom fysisk lag og datalink.

## Eksempel / lab

### Pakkeflyt: hva skjer når du åpner ndla.no?

1. Du skriver `https://ndla.no` i nettleseren.
2. **Applikasjonslaget**: Nettleseren lager en HTTP GET-forespørsel. Først må den løse opp domenenavnet — den sender et DNS-oppslag (UDP, port 53) og får tilbake IP-adressen til ndla.no (f.eks. `185.45.32.10`).
3. **Transportlaget**: TCP oppretter en forbindelse til port 443 (HTTPS) på serveren via en *three-way handshake* (SYN → SYN-ACK → ACK). HTTP-forespørselen pakkes inn i TCP-segmenter.
4. **Nettverkslaget**: Hvert TCP-segment pakkes inn i en IP-pakke med din IP-adresse som kilde og `185.45.32.10` som destinasjon.
5. **Datalinklaget**: IP-pakken pakkes inn i en Ethernet-frame med din MAC-adresse og ruterens MAC-adresse.
6. **Fysisk lag**: Biter sendes ut over kabelen eller WiFi til ruteren.
7. Ruteren (lag 3) leser IP-headeren, finner riktig rute, og sender pakken videre mot internett.
8. Prosessen gjentas gjennom flere rutere til pakken når NDLAs server.
9. Serveren pakker ut forespørselen, behandler den, og sender HTML-innholdet tilbake — gjennom de samme lagene i omvendt rekkefølge.

## Study guide

**Kjerneforståelse per lag**
- Lag 1: bits og signaler (kabel, WiFi, fiber)
- Lag 2: frames og MAC-adresser (svitsjer, Ethernet)
- Lag 3: IP-adresser og ruting (rutere, IPv4/IPv6)
- Lag 4: TCP/UDP og porter (ende-til-ende pålitelighet)
- Lag 5: applikasjonsprotokoller (HTTP, DNS, SMTP, SSH)

**Innkapsling**
Forstå at hvert lag legger til sin header. Data fra applikasjonslaget er payload for transportlaget, som er payload for nettverkslaget, osv. Ved mottak pakkes det ut i omvendt rekkefølge.

**4-lags vs. 5-lags modell**
4-lagsmodellen slår sammen lag 1 og 2 til "Network Access Layer". 5-lagsmodellen skiller disse og er pedagogisk mer lik OSI. Begge er korrekte.

**Vanlige eksamenspoeng**
- Hvilket lag er ansvarlig for hva (IP = lag 3, MAC = lag 2, TCP = lag 4, HTTP = lag 5)
- Innkapsling: hva legges til på hvert lag
- Forskjellen mellom TCP og UDP
- Hva ARP gjør (IP → MAC på lag 2)

## FAQ

**Hva er forskjellen mellom TCP og UDP?**
TCP er forbindelsesorientert og garanterer at data leveres i riktig rekkefølge uten tap. UDP er forbindelseløs og rask, men gir ingen garantier for levering. TCP brukes der pålitelighet er viktig (web, e-post), UDP der hastighet er viktigere (streaming, DNS).

**Hvilket lag er ansvarlig for IP-adressering og ruting?**
Lag 3 — Nettverkslaget (også kalt internetlaget i klassisk 4-lagsmodell).

**Hva menes med innkapsling i TCP/IP?**
Innkapsling betyr at hvert lag legger til sin egen header med styringsinformasjon når data sendes nedover gjennom lagene. Ved mottak pakkes det ut i omvendt rekkefølge.

**Hva brukes MAC-adresser til, og på hvilket lag finner vi dem?**
MAC-adresser identifiserer nettverkskort unikt og brukes til adressering innenfor ett lokalt nettverk. De finnes på lag 2 (datalinklaget). En svitsj bruker MAC-adresser til å videresende frames til riktig port.

**Hvorfor er TCP/IP-modellen organisert i lag?**
Lagdeling gjør at hvert lag kan utvikles og oppdateres uavhengig av de andre. F.eks. kan man bytte fra IPv4 til IPv6 på lag 3 uten å endre TCP på lag 4 eller HTTP på lag 5. Det forenkler også feilsøking — man kan isolere problemet til ett lag.

**Hva er ARP og hvorfor trenger vi det?**
ARP (Address Resolution Protocol) oversetter en kjent IP-adresse til den tilhørende MAC-adressen på det lokale nettverket. Lag 3 kjenner IP-adressen til destinasjonen, men lag 2 trenger MAC-adressen for å sende en Ethernet-frame til riktig port på svitsjen.

**Hva er forskjellen mellom 4-lags og 5-lags TCP/IP?**
Den klassiske internettmodellen har 4 lag der det laveste laget ("Network Access") kombinerer fysisk og datalink. Norske lærebøker (og NDLA) bruker en 5-lagsmodell der disse er separate — mer lik OSI og pedagogisk klarere.

**Hva er ICMP og ping?**
ICMP (Internet Control Message Protocol) er en protokoll på lag 3 som brukes til feilmeldinger og diagnostikk. Kommandoen `ping` sender ICMP Echo Request og venter på ICMP Echo Reply — et enkelt verktøy for å teste om en enhet er nåbar.

## Quiz

<details>
<summary>Spørsmål 1: Hva er forskjellen mellom TCP og UDP?</summary>

**Svar:** TCP er forbindelsesorientert og garanterer at data leveres i riktig rekkefølge uten tap. UDP er forbindelseløs og rask, men gir ingen garantier for levering. TCP brukes der pålitelighet er viktig (web, e-post), UDP der hastighet er viktigere (streaming, DNS).
</details>

<details>
<summary>Spørsmål 2: Hvilket lag er ansvarlig for IP-adressering og ruting?</summary>

**Svar:** Lag 3 — Nettverkslaget (også kalt internetlaget i klassisk 4-lagsmodell).
</details>

<details>
<summary>Spørsmål 3: Hva menes med innkapsling i TCP/IP?</summary>

**Svar:** Innkapsling betyr at hvert lag legger til sin egen header med styringsinformasjon når data sendes nedover gjennom lagene. Ved mottak pakkes det ut i omvendt rekkefølge.
</details>

<details>
<summary>Spørsmål 4: Hva brukes MAC-adresser til, og på hvilket lag finner vi dem?</summary>

**Svar:** MAC-adresser identifiserer nettverkskort unikt og brukes til adressering innenfor ett lokalt nettverk. De finnes på lag 2 (datalinklaget). En svitsj bruker MAC-adresser til å videresende frames til riktig port.
</details>

<details>
<summary>Spørsmål 5: Hvorfor er TCP/IP-modellen organisert i lag?</summary>

**Svar:** Lagdeling gjør at hvert lag kan utvikles og oppdateres uavhengig av de andre. F.eks. kan man bytte fra IPv4 til IPv6 på lag 3 uten å endre TCP på lag 4 eller HTTP på lag 5. Det forenkler også feilsøking — man kan isolere problemet til ett lag.
</details>

## Flashcards

TCP :: Forbindelsesorientert transportprotokoll som garanterer levering og rekkefølge
UDP :: Forbindelseløs transportprotokoll som er rask men uten leveringsgarantier
IP-adresse :: Logisk adresse på lag 3 som identifiserer en enhet i et nettverk (IPv4: 32 bit)
MAC-adresse :: Fysisk adresse på lag 2 som identifiserer et nettverkskort (48 bit, f.eks. 00:1A:2B:3C:4D:5E)
Innkapsling :: Prosessen der hvert lag legger til sin header når data sendes nedover gjennom TCP/IP-lagene
Port :: Tall (1–65535) som identifiserer hvilken applikasjon/tjeneste en nettverkspakke er ment for
ARP :: Address Resolution Protocol — oversetter IP-adresse til MAC-adresse på samme nettverk
ICMP :: Internet Control Message Protocol — brukes til feilmeldinger og diagnostikk (ping)
Three-way handshake :: TCP-prosessen for å opprette en forbindelse: SYN → SYN-ACK → ACK
Ruter :: Nettverksenhet som opererer på lag 3 og videresender pakker mellom ulike nettverk
TCP (Transmission Control Protocol) :: En forbindelsesorientert protokoll på transportlaget som garanterer feilfri levering og riktig rekkefølge på datapakker

## Ressurser

- [TCP/IP 5-lagsmodell — NDLA](https://ndla.no/nb/r/driftsstotte-im-itk-vg2/5-lags-tcpip-modell/9e31c212f6)
- [TCP, UDP og porter — NDLA](https://ndla.no/nb/r/driftsstotte-im-itk-vg2/tcp-udp-og-porter/d7acb2196e)
- [Transportlaget TCP og UDP — windowsnett.no](http://windowsnett.no/leksjoner/L08/8b%20Transportlaget%20TCP%20og%20UDP%20skjerm.pdf)
