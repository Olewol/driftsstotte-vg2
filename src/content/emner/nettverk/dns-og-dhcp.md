---
title: "DNS og DHCP"
emne: nettverk
kompetansemaal:
  - km-05
kilder:
  - ndla
  - https://learn.microsoft.com/nb-no/windows-server/networking/technologies/dhcp/dhcp-top
  - https://ndla.no/resource/130129
tags: [dns, dhcp, nettverkstjenester, ip, navneoppløsning]
flashcards: true
public: true
video: https://www.youtube.com/watch?v=S374jTRz4hU
notebooklm: true
---

# DNS og DHCP

## Introduksjon

Når du kobler en PC til et nettverk, skjer det to ting automatisk i bakgrunnen: maskinen får en IP-adresse (DHCP), og den lærer hvem den skal spørre når den trenger å finne ut hva `ndla.no` betyr i tall (DNS). Disse to tjenestene er usynlige for de fleste brukere — men uten dem ville ingenting fungere. Som driftstøtter er de to av de viktigste tjenestene du vil konfigurere og feilsøke. DNS og DHCP er ikke isolerte tjenester — de samarbeider tett med [[serverroller]] i et domenenettverk, og feil i én av dem er en av de vanligste årsakene til nettverksproblemer i bedriftsmiljøer. For å forstå hvilke protokoller og porter disse tjenestene bruker, se [[nettverksprotokoller]].

## Teori

### DHCP — Dynamic Host Configuration Protocol

DHCP automatiserer tildeling av IP-konfigurasjonen til klienter. Uten DHCP måtte en administrator manuelt konfigurere IP-adresse, subnettmaske, gateway og DNS på hver eneste maskin.

#### Hva DHCP deler ut

En DHCP-server tildeler klienter:
- **IP-adresse** (f.eks. `192.168.1.50`)
- **Subnettmaske** (f.eks. `255.255.255.0`)
- **Standard gateway** (f.eks. `192.168.1.1`)
- **DNS-serveradresse** (f.eks. `192.168.1.10`)
- **Leasetid** (hvor lenge klienten kan beholde adressen)

#### DORA-prosessen

DHCP bruker en fire-stegs prosess kalt DORA:

| Steg | Melding | Beskrivelse |
|------|---------|-------------|
| 1 | **D**iscover | Klienten sender broadcast: "Er det noen DHCP-server her?" |
| 2 | **O**ffer | DHCP-serveren svarer med et tilbud om en IP-adresse |
| 3 | **R**equest | Klienten aksepterer tilbudet: "Jeg vil ha denne adressen" |
| 4 | **A**cknowledge | Serveren bekrefter: "Adressen er din i X timer/dager" |

Steg 1 og 3 sendes som broadcast (til `255.255.255.255`) fordi klienten ikke har IP-adresse ennå.

#### Scope og leasing

Et **scope** er adresserommet DHCP-serveren administrerer — f.eks. `192.168.1.100`–`192.168.1.200`. Adresser utenfor dette kan tildeles statisk til servere og nettverksutstyr.

En **lease-tid** er tidsavtalen mellom DHCP-server og klient om at klienten bruker adressen en bestemt periode. Når leaseperioden nærmer seg slutten, forsøker klienten å fornye den. Standardleaseperiode i Windows Server er 8 dager.

#### Statisk vs. dynamisk tildeling

| Type | Beskrivelse | Brukes til |
|------|-------------|------------|
| Dynamisk | DHCP tildeler ledig adresse fra scope | Klientmaskiner |
| Statisk reservasjon | DHCP tildeler alltid samme adresse til bestemt MAC | Skrivere, servere i DHCP-miljø |
| Manuell/statisk | IP konfigureres direkte på enheten | Servere, rutere, svitsjer |

#### DHCP i bedriftsnettverk

I et enkelt hjemmenettverk kjører DHCP på ruteren. I et bedriftsnettverk med Windows Server bør DHCP flyttes til domenekontrolleren. Da må DHCP på ruteren **deaktiveres** for å unngå konflikter (to DHCP-servere på samme nett gir kaos).

Sjekk nåværende IP-konfigurasjon fra klienten:
```cmd
ipconfig /all
```

---

### DNS — Domain Name System

DNS er internettets "telefonbok". Det oversetter menneskevennlige domenenavn som `ndla.no` til maskineslige IP-adresser som `185.45.32.10`. Uten DNS måtte du huske IP-adressen til hvert nettsted du besøker.

#### Hierarkisk struktur

DNS er organisert i et tre-hierarki:

```
                    . (rot)
                   / \
                .no   .com
               /         \
           ndla.no     google.com
           /
    www.ndla.no
```

- **Rotservere** (13 stk. globalt): vet om alle toppdomener
- **Toppdomeneservere (TLD)**: `.no`, `.com`, `.org` osv.
- **Autoritative navneservere**: ansvarlige for spesifikke domener
- **Rekursive resolvere**: gjør jobben for klientene (typisk din ISP eller Google 8.8.8.8)

#### DNS-posttyper

| Post | Navn | Funksjon | Eksempel |
|------|------|----------|---------|
| A | Address | Navn → IPv4-adresse | `ndla.no → 185.45.32.10` |
| AAAA | IPv6 Address | Navn → IPv6-adresse | `ndla.no → 2001:db8::1` |
| CNAME | Canonical Name | Alias → annet navn | `www.ndla.no → ndla.no` |
| MX | Mail Exchanger | Domene → e-postserver | `ndla.no → mail.ndla.no` |
| PTR | Pointer | IP → navn (omvendt oppslag) | `10.1.168.192.in-addr.arpa → pc01.lab.lan` |
| NS | Name Server | Hvilke servere er autoritative | `ndla.no → ns1.domeneshop.no` |
| SOA | Start of Authority | Metadata om sonen | Primær navneserver, serienummer |

En **A-Record** (A-post) kobler altså et vertsnavn til en spesifikk IPv4-adresse — dette er den vanligste og viktigste DNS-posttypen.

#### DNS i Active Directory

I et AD-nettverk installeres DNS på domenekontrolleren. Denne DNS-serveren er **autoritativ** for det lokale domenet (f.eks. `lab.lan`) og kjenner alle maskiner som er innmeldt i domenet.

For oppslag utenfor lokalt domene (f.eks. `google.com`) brukes **forwarders**: DNS-serveren sender uløste oppslag videre til ruterens IP eller en ekstern DNS-server (f.eks. `8.8.8.8`).

#### Port og protokoll

DNS bruker primært **UDP på port 53** for vanlige oppslag (rask, liten overhead). For soneoverføringer mellom DNS-servere brukes **TCP på port 53**.

#### Sikkerhet: DNS-spoofing og DHCP-snooping

DNS-spoofing er et angrep der en angriper sender falske DNS-svar for å omdirigere brukere til ondsinnede nettsteder. DNSSEC (DNS Security Extensions) kan brukes til å beskytte mot dette. I svitsjer brukes **DHCP snooping** for å hindre falske DHCP-servere: svitsjen blokkerer DHCP-svar fra porter som ikke er konfigurert som betrodde.

## Eksempel / lab

### Lab: nslookup-kommandoer

`nslookup` er et kommandolinjeverktøy for DNS-feilsøking. Kjør fra CMD eller PowerShell:

```cmd
# Slå opp IP-adresse for et domene
nslookup ndla.no

# Angi en bestemt DNS-server for oppslaget
nslookup ndla.no 8.8.8.8

# Slå opp MX-post (e-postserver)
nslookup -type=MX ndla.no

# Omvendt oppslag (IP til navn)
nslookup 185.45.32.10

# Interaktiv modus
nslookup
> set type=A
> google.com
> exit
```

Eksempel på output fra `nslookup ndla.no`:
```
Server:  UnKnown
Address:  192.168.1.1

Non-authoritative answer:
Name:    ndla.no
Addresses:  185.45.32.10
```

"Non-authoritative answer" betyr at svaret kom fra cache, ikke direkte fra autoritativ server.

### Lab: DHCP-sjekk

```cmd
# Vis full IP-konfigurasjon inkl. DHCP-server og leasetid
ipconfig /all

# Frigjør DHCP-lease
ipconfig /release

# Hent ny DHCP-lease
ipconfig /renew

# Tøm DNS-cache på klienten
ipconfig /flushdns
```

### Praktisk feilsøking

Vanlige problemer og tiltak:
- **Ingen IP-adresse**: klienten har ikke nådd DHCP-serveren (sjekk om scope er aktivt, om DHCP på ruter er av, om det er nok ledige adresser)
- **Kan ikke nå ndla.no**: sjekk med `nslookup ndla.no` — hvis DNS-oppslaget feiler, er problemet DNS. Hvis DNS gir svar men siden ikke åpner, er problemet i nettverksforbindelsen.
- **169.254.x.x-adresse**: APIPA-adresse — klienten fikk ikke svar fra DHCP-server

## Study guide

**DHCP — kjerneforståelse**
DHCP automatiserer IP-konfigurasjonen. DORA-prosessen (Discover → Offer → Request → Acknowledge) er den mekanismen som skjer i bakgrunnen. Et scope definerer adresserommet. Leasetid styrer hvor lenge en adresse holdes av en klient.

**DNS — kjerneforståelse**
DNS er hierarkisk (rot → TLD → domene → vertsnavn). A-posten er den viktigste. CNAME brukes til alias. MX peker til e-postserver. PTR brukes til omvendt oppslag. I AD er DNS-serveren autoritativ for det lokale domenet.

**Vanlige eksamenspoeng**
- DORA-prosessen steg for steg
- Hva de ulike DNS-posttypene gjør (A, AAAA, CNAME, MX, PTR)
- Forskjellen mellom autoritativ DNS-server og rekursiv resolver
- Hva en forwarder er
- Kommandoene ipconfig, nslookup

## FAQ

**Hva betyr forkortelsen DORA i DHCP-sammenheng?**
DORA står for Discover, Offer, Request, Acknowledge — de fire meldingene i DHCP-prosessen der klienten finner en server, mottar et tilbud, aksepterer det og serveren bekrefter tildelingen.

**Hva er en DNS A-post?**
En A-post (Address) er en DNS-post som kobler et domenenavn til en IPv4-adresse. F.eks. `ndla.no → 185.45.32.10`.

**Hvorfor sendes DHCP Discover som broadcast?**
Fordi klienten ikke har en IP-adresse ennå og ikke vet hvilken adresse DHCP-serveren har. Broadcast (`255.255.255.255`) når alle enheter på det lokale nettverket, inkludert DHCP-serveren.

**Hva er en DNS forwarder?**
En forwarder er en konfigurasjon på DNS-serveren som sier: "Oppslag jeg ikke kan besvare selv, sender jeg videre til denne andre DNS-serveren." I AD-nettverk peker forwarderen typisk mot ruterens IP for å løse opp internettadresser.

**Hva er forskjellen mellom en PTR-post og en A-post i DNS?**
En A-post oversetter navn til IP (fremover-oppslag). En PTR-post (Pointer) gjør det motsatte — den oversetter IP-adresse til navn (omvendt oppslag/reverse lookup). PTR-poster brukes bl.a. av e-postservere og logger.

**Hva er scope og lease i DHCP?**
Scope er adresserommet DHCP-serveren kan dele ut. Lease er tidsavtalen — klienten "låner" adressen for en bestemt periode. Når leaseperioden nærmer seg slutten, fornyes den automatisk.

**Hva skjer hvis det er to DHCP-servere på samme nettverk?**
Det gir IP-adressekonflikter. Begge serverne kan tildele samme adresse til ulike klienter, noe som skaper kaos. I domenenettverk deaktiveres alltid DHCP på ruteren når Windows Server-DHCP er konfigurert.

**Hva er DHCP-snooping og DNS-spoofing?**
DNS-spoofing er et angrep der falske DNS-svar omdirigerer brukere til ondsinnede nettsteder. DHCP-snooping er en svitsjefunksjon som blokkerer falske DHCP-servere ved å godkjenne DHCP-svar kun fra betrodde porter.

## Quiz

<details>
<summary>Spørsmål 1: Hva betyr forkortelsen DORA i DHCP-sammenheng?</summary>

**Svar:** DORA står for Discover, Offer, Request, Acknowledge — de fire meldingene i DHCP-prosessen der klienten finner en server, mottar et tilbud, aksepterer det og serveren bekrefter tildelingen.
</details>

<details>
<summary>Spørsmål 2: Hva er en DNS A-post?</summary>

**Svar:** En A-post (Address) er en DNS-post som kobler et domenenavn til en IPv4-adresse. F.eks. `ndla.no → 185.45.32.10`.
</details>

<details>
<summary>Spørsmål 3: Hvorfor sendes DHCP Discover som broadcast?</summary>

**Svar:** Fordi klienten ikke har en IP-adresse ennå og ikke vet hvilken adresse DHCP-serveren har. Broadcast (`255.255.255.255`) når alle enheter på det lokale nettverket, inkludert DHCP-serveren.
</details>

<details>
<summary>Spørsmål 4: Hva er en DNS forwarder?</summary>

**Svar:** En forwarder er en konfigurasjon på DNS-serveren som sier: "Oppslag jeg ikke kan besvare selv, sender jeg videre til denne andre DNS-serveren." I AD-nettverk peker forwarderen typisk mot ruterens IP for å løse opp internettadresser.
</details>

<details>
<summary>Spørsmål 5: Hva er forskjellen mellom en PTR-post og en A-post i DNS?</summary>

**Svar:** En A-post oversetter navn til IP (fremover-oppslag). En PTR-post (Pointer) gjør det motsatte — den oversetter IP-adresse til navn (omvendt oppslag/reverse lookup). PTR-poster brukes bl.a. av e-postservere og logger.
</details>

## Flashcards

DHCP :: Dynamic Host Configuration Protocol — tildeler automatisk IP-konfigurasjon til klienter
DORA :: De fire stegene i DHCP: Discover, Offer, Request, Acknowledge
DNS :: Domain Name System — oversetter domenenavn til IP-adresser
DNS A-post :: DNS-post som kobler domenenavn til IPv4-adresse
DNS CNAME :: DNS-post som lager et alias/peker til et annet domenenavn
DNS MX-post :: DNS-post som angir hvilken server som håndterer e-post for domenet
DNS PTR-post :: DNS-post for omvendt oppslag: IP-adresse → domenenavn
DHCP scope :: Adresserommet DHCP-serveren administrerer og tildeler fra
DHCP lease :: Tidsavtalen mellom DHCP-server og klient om bruk av en IP-adresse
Forwarder :: DNS-konfigurasjon som videresender uløste oppslag til en annen DNS-server
Lease-tid :: Tiden en klient får beholde en tildelt IP-adresse før den må be om fornyelse fra DHCP-serveren
A-Record :: En ressurs-oppføring i DNS som kobler et vertsnavn til en spesifikk IPv4-adresse

## Ressurser

- [Deaktivere eksisterende DHCP-server — NDLA](https://ndla.no/nb/r/driftsstotte-im-itk-vg2/deaktivere-eksisterende-dhcp-server/9d5c1dedc7)
- [Installasjon av DNS-server — NDLA](https://ndla.no/nn/r/driftsstotte-im-itk-vg2/installasjon-av-dns-server/4246401a38)
- [windowsnett.no — leksjon 11: DHCP og DNS](https://www.windowsnett.no/)
- [DHCP Overview — Microsoft Learn](https://learn.microsoft.com/nb-no/windows-server/networking/technologies/dhcp/dhcp-top)
