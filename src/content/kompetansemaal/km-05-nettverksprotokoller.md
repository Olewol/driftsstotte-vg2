---
title: "KM-05: Nettverksprotokoller og serverroller / Network Protocols and Server Roles"
emne: kompetansemaal
kompetansemaal:
  - km-05
kilder:
  - https://www.udir.no/lk20/itk02-01/kompetansemaal-og-vurdering/kv372
  - https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/
  - https://www.professormesser.com/network-plus/
  - https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/
  - https://learn.microsoft.com/en-us/training/paths/networking-fundamentals/
tags: [km-05, nettverk, protokoller, dns, dhcp, serverroller]
flashcards: false
public: true
---

# KM-05: Nettverksprotokoller og serverroller / Network Protocols and Server Roles

## 🎯 Mål / Competency Goal

**Norsk:** Utforske og beskrive relevante nettverksprotokoller, nettverkstjenester og serverroller

**English:** Explore and describe relevant network protocols, network services and server roles

---

## 📘 Forklaring / Explanation

### Norsk
Nettverksprotokoller er «språkene» som datamaskiner bruker for å kommunisere. Uten protokoller kunne ikke en PC snakke med en webserver, sende e-post eller finne en skriver på nettverket[^1].

**Protokollene du må kjenne:**
| Protokoll | Port | Bruk |
|-----------|------|------|
| HTTP/HTTPS | 80/443 | Webtrafikk |
| DNS | 53 | Navneoppløsning (domenenavn → IP) |
| DHCP | 67/68 | Automatisk IP-tildeling |
| SSH | 22 | Sikker fjernpålogging |
| FTP/SFTP | 21/22 | Filoverføring |
| SMTP | 25 | E-postutsending |
| IMAP/POP3 | 143/110 | E-postmottak |

**Nettverksmodellene** forklarer hvordan protokollene er organisert:

- **OSI-modellen** (7 lag) — Referansemodell for forståelse av nettverkskommunikasjon
- **TCP/IP-modellen** (4–5 lag) — Den praktiske modellen internett bygger på

### English
Network protocols are the "languages" that computers use to communicate. Without protocols, a PC couldn't talk to a web server, send email, or find a printer on the network[^1].

**Key protocols you should know:**

| Protocol | Port | Use |
|----------|------|-----|
| HTTP/HTTPS | 80/443 | Web traffic |
| DNS | 53 | Name resolution (domain name → IP) |
| DHCP | 67/68 | Automatic IP assignment |
| SSH | 22 | Secure remote login |
| FTP/SFTP | 21/22 | File transfer |
| SMTP | 25 | Email sending |
| IMAP/POP3 | 143/110 | Email receiving |

**Network models** explain how protocols are organized:

- **OSI model** (7 layers) — Reference model for understanding network communication
- **TCP/IP model** (4–5 layers) — The practical model the internet is built on

---

## 💡 Eksempler / Examples

### Norsk

**Eksempel 1: Hva skjer når du åpner en nettside?**
1. DNS slår opp `nrk.no` → finner IP-adressen
2. DHCP har gitt PC-en din en ledig IP-adresse
3. HTTPS-protokollen sender en forespørsel til serveren
4. Serveren svarer med nettsiden

**Eksempel 2: En skoles servere**
Skolen har én server som er domenekontroller (AD DS), én som er filserver og én som er webserver for skolens hjemmeside. Hver rolle krever ulike protokoller og tjenester.

### English

**Example 1: What happens when you open a website?**
1. DNS looks up `nrk.no` → finds the IP address
2. DHCP gave your PC a free IP address
3. HTTPS sends a request to the server
4. The server responds with the webpage

**Example 2: A School's Servers**
The school has one server as domain controller (AD DS), one as file server, and one as web server for the school website. Each role needs different protocols and services.

---

## 📝 Oppsummering / Summary

| Norsk | English |
|-------|---------|
| Protokoller er språket enheter bruker for å kommunisere | Protocols are the language devices use to communicate |
| DNS oversetter domenenavn til IP-adresser | DNS translates domain names to IP addresses |
| DHCP gir enheter automatisk IP-konfigurasjon | DHCP automatically assigns IP configuration |
| Serverroller definerer en servers funksjon | Server roles define a server's function |

---

## 🔧 Bridging Exercises / Praksisoppgaver

### Norsk — Praksisoppgaver

**Oppgave 1: Fang og analyser nettverkstrafikk med Wireshark**
Eleven bruker Wireshark til å fange nettverkstrafikk og identifisere protokoller.
- Start Wireshark og fang trafikk på nettverkskortet
- Åpne en nettside (f.eks. nrk.no)
- Stopp fangsten og filtrer på:
  - `dns` — Se DNS-spørringer (domenenavn → IP)
  - `http` — Se HTTP-forespørsler og svar
  - `tls` — Se TLS-håndtrykk (kryptert kommunikasjon)
- Identifiser for hver: Kilde-IP, Destinasjons-IP, portnumre, protokoll
- Skjermbilde av hver filtervisning + forklaring

**Oppgave 2: Sett opp en DNS-server**
Bruk Windows Server (DNS-rolle) eller Linux (BIND9):
- Installer DNS-server-rollen / `sudo apt install bind9`
- Opprett en foroverslåingssone for `skole.local`
- Legg til A-poster: `www.skole.local` → `10.0.0.10`, `mail.skole.local` → `10.0.0.11`
- Legg til CNAME: `files.skole.local` → `www.skole.local`
- Konfigurer en klient til å bruke denne DNS-serveren
- Test med `nslookup www.skole.local` og `ping www.skole.local`
- Utfordring: Sett opp omvendt oppslagsone (PTR-poster)

**Veiledning / Solution Guidelines:**
- Oppgave 1: Wireshark-filtre: `dns` viser DNS-spørringer på port 53. `http` viser ubeskyttet webtrafikk (påminn elevene om at de fleste nettsider nå bruker HTTPS/TLS). `tls` viser TLS-håndtrykket (Client Hello, Server Hello, sertifikatutveksling).
- Oppgave 2 (BIND9): `sudo apt install bind9`. Konfigurasjon i `/etc/bind/named.conf.local`. Sonefil: `www IN A 10.0.0.10`. `sudo systemctl restart bind9`. Test: `nslookup www.skole.local 127.0.0.1`.

### English — Practical Exercises

**Exercise 1: Capture and Analyze Network Traffic with Wireshark**
- Start Wireshark capture on the network interface
- Open a webpage (e.g., nrk.no)
- Stop capture and filter on: dns, http, tls
- Identify: source/destination IPs, port numbers, protocols
- Screenshot each filter view + explanation

**Exercise 2: Set Up a DNS Server**
Windows Server (DNS role) or Linux (BIND9):
- Install DNS server / `sudo apt install bind9`
- Create forward lookup zone for `school.local`
- Add A records, CNAME records
- Test with `nslookup` and `ping`
- Challenge: Set up reverse lookup zone (PTR records)

**Solution Guidelines:**
- Exercise 1: `dns` filter shows port 53 queries. `http` shows unencrypted web traffic. `tls` shows the TLS handshake (Client Hello, Server Hello, Certificate Exchange).
- Exercise 2 (BIND9): Install, configure zone in `named.conf.local`, create zone file, restart service, test with nslookup.

## 🔗 Relevante artikler / Related Articles

- [[nettverksprotokoller]] — Viktige protokoller og portnumre
- [[dns-og-dhcp]] — Navneoppløsning og automatisk IP-tildeling
- [[serverroller]] — Serverroller i Windows Server
- [[tcp-ip-modellen]] — TCP/IP-modellens lag
- [[osi-modellen]] — OSI-modellens 7 lag

## 📚 Kilder / Sources

[^1]: Udir (2020). Læreplan i Vg2 informasjonsteknologi. https://www.udir.no/lk20/itk02-01/
[^2]: Cloudflare. What is a network protocol? https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/
[^3]: Professor Messer. Network+ Study Guide. https://www.professormesser.com/network-plus/
[^4]: Microsoft Learn. Networking fundamentals. https://learn.microsoft.com/en-us/training/paths/networking-fundamentals/
