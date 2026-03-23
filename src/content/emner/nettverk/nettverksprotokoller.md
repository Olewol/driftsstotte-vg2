---
title: "Nettverksprotokoller"
emne: nettverk
kompetansemaal:
  - km-05
kilder:
  - ndla
tags: [protokoller, http, ftp, ssh, smtp, dns, porter, tcp, udp]
flashcards: true
public: true
---

# Nettverksprotokoller

## Introduksjon

En nettverksprotokoll er et sett med regler som definerer hvordan enheter kommuniserer. Uten protokoller ville nettverkskommunikasjon være som å snakke to forskjellige språk — ingen ville forstå hverandre. Å kjenne de viktigste protokollene, hva de brukes til og hvilke portnumre de kjører på, er grunnleggende kunnskap for enhver driftstøtter — både for konfigurasjon og feilsøking.

## Teori

### Transportlagsprotokoller: TCP og UDP

Alle applikasjonsprotokoller kjører enten over TCP eller UDP på transportlaget.

| | TCP | UDP |
|---|---|---|
| **Type** | Forbindelsesorientert | Forbindelseløs |
| **Pålitelighet** | Garantert levering, rekkefølge | Ingen garanti |
| **Hastighet** | Tregere (overhead for ack/retransmit) | Raskere |
| **Bruksområde** | Web, e-post, filoverføring, SSH | DNS, streaming, VoIP, spill |

### Portnumre

Et **portnummer** er et tall fra 0–65535 (16 bit) som identifiserer hvilken tjeneste en nettverkspakke er ment for på en maskin. IP-adressen finner maskinen; portnummeret finner riktig tjeneste på maskinen.

Kategorier:
- **Well-known ports (0–1023)**: standardporter for kjente tjenester (HTTP, SMTP, DNS, osv.)
- **Registered ports (1024–49151)**: brukt av applikasjoner
- **Dynamic/ephemeral ports (49152–65535)**: tildeles midlertidig til klientforbindelser

### Viktige protokoller

| Protokoll | Port(er) | Transport | Funksjon | Sikkerhetsnivå |
|-----------|----------|-----------|----------|----------------|
| HTTP | 80 | TCP | Webbsider, forespørsel/svar | Ukryptert — ikke bruk for sensitiv data |
| HTTPS | 443 | TCP | HTTP kryptert med TLS/SSL | Kryptert — standard i dag |
| FTP | 20 (data), 21 (kontroll) | TCP | Filoverføring | Ukryptert — passord i klartekst |
| SFTP | 22 | TCP | Sikker filoverføring (over SSH) | Kryptert |
| FTPS | 21 (eksplisitt), 990 (implisitt) | TCP | FTP med TLS-kryptering | Kryptert |
| SSH | 22 | TCP | Sikker fjerntilgang til terminal | Kryptert |
| RDP | 3389 | TCP | Grafisk fjernstyring av Windows | Kryptert (TLS i nyere versjoner) |
| SMTP | 25 (server-til-server), 587 (klient-til-server) | TCP | Sending av e-post | Port 587 bruker STARTTLS |
| IMAP | 143 (ukryptert), 993 (SSL/TLS) | TCP | Synkronisering av e-post | Port 993 kryptert |
| POP3 | 110 (ukryptert), 995 (SSL/TLS) | TCP | Nedlasting av e-post | Port 995 kryptert |
| DNS | 53 | UDP (primært), TCP (soneoverføring) | Navneoppløsning | Ukryptert (DNS over HTTPS finnes) |
| DHCP | 67 (server), 68 (klient) | UDP | Automatisk IP-tildeling | Ingen autentisering |
| SNMP | 161 (agent), 162 (trap) | UDP | Nettverksovervåking og -administrasjon | SNMPv3 er kryptert |

### Detaljert gjennomgang

#### HTTP og HTTPS (port 80/443)

HTTP (Hypertext Transfer Protocol) er grunnlaget for webkommunikasjon. Protokollen bruker en **forespørsel/svar-modell**:

```
Klient → Server:
GET /index.html HTTP/1.1
Host: ndla.no

Server → Klient:
HTTP/1.1 200 OK
Content-Type: text/html
...
```

**HTTP-metoder**: GET (hent ressurs), POST (send data), PUT (oppdater), DELETE (slett)

**HTTP-statuskoder**:
- 2xx Suksess: `200 OK`, `201 Created`
- 3xx Omdirigering: `301 Moved Permanently`, `302 Found`
- 4xx Klientfeil: `400 Bad Request`, `403 Forbidden`, `404 Not Found`
- 5xx Serverfeil: `500 Internal Server Error`, `503 Service Unavailable`

**HTTPS** = HTTP + TLS. Forbindelsen krypteres med TLS (Transport Layer Security) — det er dette hengelåsikonet i nettleseren betyr. All moderne webtrafikk bør bruke HTTPS.

#### FTP og SFTP (port 21/22)

FTP (File Transfer Protocol) bruker to separate forbindelser: **kontrollkanal** (port 21) for kommandoer og **datakanal** (port 20) for selve filoverføringen. FTP er ukryptert — brukernavn og passord sendes i klartekst.

**SFTP** (SSH File Transfer Protocol) er en komplett erstatning som kjører over SSH (port 22) og er kryptert fra start til slutt. SFTP er standarden i dag.

Verktøy: FileZilla (grafisk klient for FTP/SFTP), WinSCP (Windows), scp-kommandoen (Linux/terminal).

#### SSH (port 22)

SSH (Secure Shell) gir sikker fjerntilgang til en kommandolinje — primært på Linux/Unix-servere, men også nettverksutstyr som svitsjer og rutere.

```bash
# Koble til server via SSH
ssh brukernavn@192.168.30.10

# Kopiere fil sikkert (SCP over SSH)
scp fil.txt brukernavn@192.168.30.10:/home/brukernavn/
```

SSH bruker asymmetrisk kryptografi: server og klient utveksler nøkler, og all kommunikasjon krypteres. Mye tryggere enn Telnet (port 23) som var forgjengeren.

#### E-postprotokoller (SMTP/IMAP/POP3)

E-postsystemet bruker forskjellige protokoller for sending og mottak:

```
[Avsender-klient] --SMTP(587)-→ [Avsenders mailserver] --SMTP(25)-→ [Mottakers mailserver]
                                                                              ↓
                                                               [Mottaker-klient] ←--IMAP(993)--
```

- **SMTP** sender e-post (klient til server og mellom servere)
- **IMAP** synkroniserer e-post — e-posten forblir på serveren (anbefalt)
- **POP3** laster ned og sletter fra server — gammel løsning, brukes sjelden

#### SNMP (port 161/162)

SNMP (Simple Network Management Protocol) brukes til å overvåke og administrere nettverksenheter (svitsjer, rutere, servere). En SNMP-**agent** kjører på hver enhet og rapporterer tilstand. En **NMS** (Network Management Station) poller agentene på port 161. Agenter kan sende alarmer (**traps**) til NMS på port 162 ved hendelser.

SNMPv1 og v2c bruker "community strings" (passord i klartekst). **SNMPv3** er den sikre versjonen med kryptering og autentisering.

### Sikkerhet og porter

Kjente portnumre er også kjente angrepsmål. SSH (port 22) og RDP (port 3389) utsettes konstant for automatiserte innloggingsforsøk (brute force). Tiltak:
- Bruk VPN — bare tillat RDP/SSH fra internt nett eller VPN
- Begrens med IP-restriksjoner i brannmur
- Bruk nøkkelbasert autentisering for SSH (ikke passord)
- Aktiver kontosperring etter X feil forsøk

## Eksempel / lab

### Test protokoller fra kommandolinje

```cmd
# Test HTTP-tilgang med curl
curl -I http://ndla.no

# Test om en port er åpen (PowerShell)
Test-NetConnection -ComputerName ndla.no -Port 443

# Test om en port er åpen (CMD/nmap)
nmap -p 80,443,22 192.168.1.10

# Vis aktive forbindelser og porter
netstat -an

# Koble til SSH (fra Windows Terminal/PowerShell)
ssh admin@192.168.1.1
```

### Identifiser protokoll fra port

| Port | Protokoll | Tjeneste |
|------|-----------|---------|
| 22 | ? | ? |
| 80 | ? | ? |
| 443 | ? | ? |
| 3389 | ? | ? |
| 25 | ? | ? |

Svar: SSH/SFTP, HTTP, HTTPS, RDP, SMTP

## Quiz

<details>
<summary>Spørsmål 1: Hvilken port bruker HTTPS, og hva betyr det at en forbindelse er HTTPS?</summary>

**Svar:** HTTPS bruker port 443. Det betyr at HTTP-trafikken er kryptert med TLS (Transport Layer Security). Innholdet kan ikke leses av noen som avlytter forbindelsen.
</details>

<details>
<summary>Spørsmål 2: Hva er forskjellen mellom FTP og SFTP?</summary>

**Svar:** FTP (port 21) overfører filer uten kryptering — brukernavn, passord og filer sendes i klartekst og kan avlyttes. SFTP er sikker filoverføring over SSH (port 22) der alt krypteres. SFTP er standarden i dag.
</details>

<details>
<summary>Spørsmål 3: Forklar forskjellen mellom SMTP og IMAP.</summary>

**Svar:** SMTP brukes til å *sende* e-post (fra klient til server og mellom servere). IMAP brukes til å *hente og synkronisere* e-post fra server til klient — e-posten forblir på serveren slik at du kan lese den fra flere enheter.
</details>

<details>
<summary>Spørsmål 4: Hva er en HTTP 404-feil?</summary>

**Svar:** HTTP 404 Not Found betyr at serveren mottok forespørselen, men ikke fant den etterspurte ressursen (f.eks. siden eller filen finnes ikke på den adressen). Det er en klientfeil (4xx).
</details>

<details>
<summary>Spørsmål 5: Hvorfor er det en sikkerhetsrisiko å ha RDP (port 3389) åpen mot internett?</summary>

**Svar:** RDP er et populært angrepsmål. Automatiserte verktøy skanner konstant internett etter åpen port 3389 og forsøker brute force-innlogging. Dersom det lykkes, får angriperen grafisk tilgang til Windows-maskinen. Løsningen er å bare tillate RDP fra VPN eller IP-adressen til administratorer.
</details>

## Flashcards

HTTP :: Hypertext Transfer Protocol — ukryptert nettprotokoll på port 80
HTTPS :: HTTP over TLS — kryptert nettprotokoll på port 443
FTP :: File Transfer Protocol — ukryptert filoverføring på port 21 (kontroll) og 20 (data)
SFTP :: Sikker filoverføring over SSH på port 22 — kryptert erstatning for FTP
SSH :: Secure Shell — kryptert fjerntilgang til terminal/kommandolinje på port 22
RDP :: Remote Desktop Protocol — grafisk Windows-fjernstyring på port 3389
SMTP :: Simple Mail Transfer Protocol — sending av e-post, port 25 (server-server) / 587 (klient-server)
IMAP :: Internet Message Access Protocol — synkronisering av e-post fra server, port 143 / 993 (TLS)
POP3 :: Post Office Protocol 3 — nedlasting av e-post fra server, port 110 / 995 (TLS)
SNMP :: Simple Network Management Protocol — overvåking av nettverksenheter på port 161/162

## Ressurser

- [TCP, UDP og porter — NDLA](https://ndla.no/nb/r/driftsstotte-im-itk-vg2/tcp-udp-og-porter/d7acb2196e)
- [SSH — NDLA](https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/topic:6e8a2eaf-4983-4d42-a9b0-911b5921b44a/resource:db7b7d9d-9894-418a-8458-74a5cfec1e60)
- [Transportlaget TCP og UDP — windowsnett.no](http://windowsnett.no/leksjoner/L08/8b%20Transportlaget%20TCP%20og%20UDP%20skjerm.pdf)
- [HTTP og IIS — windowsnett.no](http://www.windowsnett.no/leksjoner/L09/Leksjon%209%20beskrivelse.htm)
