---
title: "OSI-modellen"
emne: nettverk
kompetansemaal:
  - km-05
kilder:
  - ndla
  - https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/
tags: [osi, modell, lag, protokoll, nettverk]
flashcards: true
public: true
video: https://www.youtube.com/watch?v=vv4y_uOneC0
notebooklm: true
---

# OSI-modellen

## Introduksjon

OSI-modellen (Open Systems Interconnection) er en 7-lags referansemodell utviklet av ISO på slutten av 1970-tallet. Den ble aldri den dominerende implementasjonen i praksis — det ble TCP/IP — men OSI er blitt den universelle standarden for å *beskrive og forstå* nettverkskommunikasjon. I feilsøking er spørsmålet "på hvilket lag oppstår problemet?" en av de mest nyttige du kan stille.

OSI-modellen er tett knyttet til [[tcp-ip-modellen]], som er det rammeverket internett faktisk bruker i praksis. Å forstå OSI er nøkkelen til å forstå protokoller som [[nettverksprotokoller]] beskriver, samt tjenestene i [[dns-og-dhcp]] og [[serverroller]].

## Teori

### De 7 lagene

| Lag | Navn | Norsk | Funksjon | Protokolleksempler |
|-----|------|-------|----------|--------------------|
| 7 | Application | Applikasjonslaget | Brukergrensesnitt og applikasjonsprotokoller | HTTP, HTTPS, FTP, SMTP, DNS |
| 6 | Presentation | Presentasjonslaget | Formatering, kryptering, komprimering | TLS/SSL, JPEG, ASCII, MPEG |
| 5 | Session | Sesjonslaget | Oppretting, vedlikehold og avslutning av sesjoner | NetBIOS, RPC, SQL |
| 4 | Transport | Transportlaget | Ende-til-ende-kommunikasjon, segmentering | TCP, UDP |
| 3 | Network | Nettverkslaget | Logisk adressering og ruting | IP, ICMP, OSPF, BGP |
| 2 | Data Link | Datalinklaget | Frames, MAC-adresser, feildeteksjon | Ethernet, ARP, 802.11 |
| 1 | Physical | Fysisk lag | Bitsending over medium | UTP-kabel, fiber, WiFi-radio |

### Detaljert beskrivelse av hvert lag

**Lag 1 — Fysisk lag**
Det fysiske laget definerer de elektriske, optiske og trådløse signalene som representerer biter (0 og 1). Det inkluderer kontakttyper (RJ-45), kabeltyper (Cat5e, Cat6, fiber), og overføringsmetoder. Ingenting her kjenner til adresser eller logisk struktur — det er bare bits.

**Lag 2 — Datalinklaget**
Pakker biter inn i *frames* og håndterer overføring innenfor ett nettverkssegment. Delt i to underlag:
- **MAC (Media Access Control)**: adressering med 48-bits MAC-adresser, kontroll av tilgang til mediet
- **LLC (Logical Link Control)**: feildeteksjon, flomstyring

En svitsj opererer på lag 2. Ethernet er den dominerende lag 2-protokollen i kablede nettverk.

**Lag 3 — Nettverkslaget**
Introduserer logisk adressering (IP-adresser) og ruting mellom nettverk. En ruter opererer på lag 3. Nettverkslaget bestemmer den beste veien fra kilde til destinasjon gjennom potensielt mange mellomliggende nettverk.

**Lag 4 — Transportlaget**
Segmenterer data fra applikasjonslaget og håndterer ende-til-ende-kommunikasjon. TCP gir pålitelig levering med sekvensnumre og bekreftelser (ACK). UDP er rask og enkel uten slike garantier. Portnumre identifiserer hvilken applikasjon trafikken tilhører.

**Lag 5 — Sesjonslaget**
Administrerer *sesjoner* — vedvarende forbindelser mellom applikasjoner. Sesjonslaget oppretter, vedlikeholder og avslutter dialogen mellom to systemer. I praksis er mye av denne funksjonaliteten integrert i applikasjonsprotokoller i TCP/IP.

**Lag 6 — Presentasjonslaget**
Oversetter data mellom applikasjonens format og nettverkets format. Ansvarlig for:
- **Kryptering/dekryptering**: TLS/SSL krypterer HTTP-trafikk til HTTPS
- **Komprimering**: reduserer datamengden som sendes
- **Formatkonvertering**: sikrer at f.eks. tegnsett (UTF-8, ASCII) tolkes likt på begge sider

**Lag 7 — Applikasjonslaget**
Det øverste laget er det brukeren møter. Her befinner seg protokollene som applikasjoner bruker direkte: HTTP for nettlesing, SMTP for e-postsending, FTP for filoverføring, DNS for navneoppløsning.

### Innkapsling og PDU

Når data sendes nedover gjennom OSI-lagene, legger hvert lag til sin egen kontrollinformasjon (header). Denne prosessen kalles **innkapsling (encapsulation)**. Hvert lag opererer med sin egen **PDU (Protocol Data Unit)**: på lag 4 kalles den *Segment*, på lag 3 *Pakke*, og på lag 2 *Ramme*. Ved mottak pakkes det ut i omvendt rekkefølge — hvert lag leser og fjerner sin header.

### Huskeregel

En populær huskeregel for lagene nedenfra og opp (lag 1 → 7):

> **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way
> (Physical, Data Link, Network, Transport, Session, Presentation, Application)

Og ovenfra og ned (lag 7 → 1):

> **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing

### OSI vs. TCP/IP

| OSI | Lag nr. | TCP/IP (5-lag) |
|-----|---------|----------------|
| Applikasjonslaget | 7 | Applikasjonslaget |
| Presentasjonslaget | 6 | Applikasjonslaget |
| Sesjonslaget | 5 | Applikasjonslaget |
| Transportlaget | 4 | Transportlaget |
| Nettverkslaget | 3 | Nettverkslaget |
| Datalinklaget | 2 | Datalinklaget |
| Fysisk lag | 1 | Fysisk lag |

OSI-modellens lag 5, 6 og 7 tilsvarer samlet applikasjonslaget i TCP/IP. I praksis er funksjonene fra presentasjons- og sesjonslaget implementert direkte i applikasjonsprotokoller eller i TLS.

### OSI i feilsøking

OSI-modellen er særlig nyttig ved feilsøking. Tenk deg et problem der en bruker ikke kommer på internett:

- **Lag 1** — Er kabelen plugget inn? Lyser linklys?
- **Lag 2** — Svitsjen ser MAC-adressen? Feil VLAN?
- **Lag 3** — Har maskinen riktig IP-adresse og gateway? Kan du pinge gateway?
- **Lag 4** — Blokkeres TCP-port 443 av brannmur?
- **Lag 7** — Feil i nettleserens konfigurasjon? DNS fungerer men HTTP feiler?

Ved å jobbe systematisk nedenfra og opp (eller ovenfra og ned) isolerer du problemet raskt.

## Eksempel / lab

### Identifiser laget

Avgjør hvilket OSI-lag hvert scenario tilhører:

| Scenario | Lag |
|----------|-----|
| Ethernet-kabel ikke plugget inn | Lag 1 — Fysisk |
| Feil IP-adresse konfigurert | Lag 3 — Nettverk |
| HTTPS-kryptering (TLS) | Lag 6 — Presentasjon |
| Svitsj videresender basert på MAC | Lag 2 — Datalink |
| TCP three-way handshake | Lag 4 — Transport |
| DNS-oppslag feiler | Lag 7 — Applikasjon |
| WiFi-signal for svakt | Lag 1 — Fysisk |

### Feilsøkingsøvelse

Scenario: En PC kan pinge `192.168.1.1` (gateway) men ikke åpne `https://ndla.no`.

Analyser:
- Lag 1–3 fungerer (ping til gateway virker → fysisk forbindelse, datalink og IP er OK)
- Problemet er på lag 4 (TCP-port blokkert?), lag 6 (TLS-feil?) eller lag 7 (DNS feiler? HTTP-feil?)
- Test: `nslookup ndla.no` — hvis DNS ikke svarer er problemet lag 7 (DNS-tjenesten) eller lag 3 (ruting mot DNS-server)

## Study guide

**OSI-modellens formål**
OSI er en *referansemodell*, ikke en implementasjon. Den brukes som felles referansespråk for å forstå og feilsøke nettverkskommunikasjon. Hvert lag har et klart ansvarsområde og kommuniserer kun med laget direkte over og under.

**Kjerneforståelse per lag**
- Lag 1–2 handler om fysisk og lokal overføring (kabel, WiFi, svitsjer, MAC-adresser)
- Lag 3 introduserer logisk adressering og ruting (IP, rutere)
- Lag 4 håndterer ende-til-ende pålitelighet og applikasjonsidentifikasjon (TCP/UDP, portnumre)
- Lag 5–7 er applikasjonsrelaterte (sesjoner, formatering, brukerprotokoller)

**Vanlige eksamenspoeng**
- Forskjellen mellom svitsj (lag 2) og ruter (lag 3)
- TCP vs. UDP og når man bruker hva
- OSI-lagene ovenfra og ned vs. nedenfra og opp
- Innkapsling: hva skjer med data når det sendes nedover i stakken

## FAQ

**Hvorfor bruker vi OSI-modellen når TCP/IP er det som faktisk brukes?**
OSI gir oss et presist og delt referansespråk for å snakke om nettverksproblemer og protokoller. Når en teknikker sier "problemet er på lag 2", forstår alle hva det betyr — selv om nettverket kjører TCP/IP.

**Hva er forskjellen mellom lag 3 og lag 2-adresser?**
Lag 2 bruker MAC-adresser (fysiske, hardkodede) for kommunikasjon innenfor ett nettverk. Lag 3 bruker IP-adresser (logiske, konfigurerbare) for kommunikasjon mellom ulike nettverk.

**Hva skjer på lag 6 (presentasjonslaget) i praksis?**
Kryptering via TLS/SSL er det vanligste eksemplet. Når du besøker en HTTPS-side, krypterer lag 6 dataene. Komprimering (gzip) og tegnkonvertering (UTF-8) er andre eksempler.

**Kan ett stykke maskinvare operere på flere lag?**
Ja. En "lag 3-svitsj" opererer på både lag 2 og lag 3 — den kan route mellom VLAN-er i tillegg til å fungere som vanlig svitsj. Brannmurer opererer ofte på lag 3–7.

**Hva er PDU, og hvorfor er begrepet nyttig?**
PDU (Protocol Data Unit) er betegnelsen på dataenheten på et gitt lag: Segment (lag 4), Pakke (lag 3), Ramme (lag 2), Bit (lag 1). Det gjør det enklere å beskrive nøyaktig hva som behandles på hvert trinn.

**Hva er innkapsling?**
Innkapsling er prosessen der data pakkes inn i kontrollinformasjon (headers) fra hvert lag i OSI-modellen når de sendes nedover i stakken. På mottakersiden pakkes det ut lag for lag.

**Hvorfor er sesjonslaget (lag 5) viktig?**
Sesjonslaget administrerer dialogen mellom applikasjoner — hvem snakker, i hvilken rekkefølge, og hvordan avslutter man ryddig. I praksis er dette ofte integrert i TLS og applikasjonsprotokoller.

**Hvordan bruker jeg OSI aktivt i feilsøking?**
Start fra lag 1 og jobb oppover: sjekk kabel → svitsj → IP-adresse → brannmur-porter → applikasjonsinnstillinger. Eller start fra lag 7 og jobb nedover hvis du vet at nettverket fungerer.

## Quiz

<details>
<summary>Spørsmål 1: Hvilke lag i OSI tilsvarer applikasjonslaget i TCP/IP?</summary>

**Svar:** Lag 5 (sesjon), lag 6 (presentasjon) og lag 7 (applikasjon) i OSI tilsvarer samlet applikasjonslaget i TCP/IP-modellen.
</details>

<details>
<summary>Spørsmål 2: Hva er presentasjonslagets (lag 6) oppgave?</summary>

**Svar:** Presentasjonslaget håndterer formatering, kryptering/dekryptering og komprimering av data. TLS/SSL som krypterer HTTP-trafikk til HTTPS er et eksempel på funksjonalitet fra dette laget.
</details>

<details>
<summary>Spørsmål 3: Hva er forskjellen mellom en svitsj og en ruter sett fra OSI-modellen?</summary>

**Svar:** En svitsj opererer primært på lag 2 (datalinklaget) og bruker MAC-adresser for å videresende frames innenfor ett nettverk. En ruter opererer på lag 3 (nettverkslaget) og bruker IP-adresser for å rute pakker mellom ulike nettverk.
</details>

<details>
<summary>Spørsmål 4: Hva er sesjonslaget (lag 5) ansvarlig for?</summary>

**Svar:** Sesjonslaget administrerer opprettelse, vedlikehold og avslutning av sesjoner (vedvarende forbindelser) mellom applikasjoner på to systemer.
</details>

<details>
<summary>Spørsmål 5: Beskriv huskeregelen for OSI-lagene nedenfra og opp.</summary>

**Svar:** "Please Do Not Throw Sausage Pizza Away" — Physical, Data Link, Network, Transport, Session, Presentation, Application (lag 1 til 7).
</details>

## Flashcards

OSI-modellen :: ISO-standardens 7-lags referansemodell for nettverkskommunikasjon
Fysisk lag (OSI 1) :: Bitsending over fysisk medium (kabel, fiber, WiFi-radio)
Datalinklaget (OSI 2) :: Frames og MAC-adressering innenfor ett nettverkssegment
Nettverkslaget (OSI 3) :: IP-adressering og ruting mellom ulike nettverk
Transportlaget (OSI 4) :: Ende-til-ende-kommunikasjon med TCP eller UDP og portnumre
Sesjonslaget (OSI 5) :: Oppretting, vedlikehold og avslutning av applikasjonssesjoner
Presentasjonslaget (OSI 6) :: Formatering, kryptering (TLS) og komprimering av data
Applikasjonslaget (OSI 7) :: Brukervendte protokoller som HTTP, FTP, SMTP og DNS
OSI vs TCP/IP :: OSI har 7 lag og er referansemodell; TCP/IP har 4–5 lag og er det internett faktisk bruker
Innkapsling (Encapsulation) :: Prosessen der data pakkes inn i kontrollinformasjon (headers) fra hvert lag i OSI-modellen når de sendes nedover i stakken
PDU (Protocol Data Unit) :: Betegnelsen på informasjonsenheten på et spesifikt lag: Segment (lag 4), Pakke (lag 3), Ramme (lag 2)
Lag (Layers) :: De syv logiske nivåene i OSI-modellen som deler opp oppgavene i nettverkskommunikasjon for å sikre standardisering og forenkle feilsøking
Referansemodell :: Et teoretisk rammeverk som brukes for å forstå og beskrive hvordan komplekse prosesser som nettverkskommunikasjon fungerer

## Ressurser

- [TCP/IP 5-lagsmodell (nevner OSI) — NDLA](https://ndla.no/nb/r/driftsstotte-im-itk-vg2/5-lags-tcpip-modell/9e31c212f6)
- [OSI-modellen — Imperva](https://www.imperva.com/learn/application-security/osi-model/)
- [OSI-modellen — Cloudflare](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/)
- [TCP/IP og OSI sammenligning — Cisco Press](https://www.ciscopress.com/articles/article.asp?p=1757634&seqNum=2)
- [The OSI Model Explained | Animation — NetworkChuck (15 min)](https://www.youtube.com/watch?v=vv4y_uOneC0)
- [OSI-modellen — SNL](https://snl.no/OSI-modellen)
