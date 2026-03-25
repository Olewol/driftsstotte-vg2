---
title: "Serverroller"
emne: nettverk
kompetansemaal:
  - km-05
kilder:
  - ndla
  - https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/ad-ds-getting-started
tags: [server, ad, dns, dhcp, filserver, webserver, windows-server, serverrolle]
flashcards: https://notebooklm.google.com/notebook/f7e5ad6c-7082-40cf-abd5-7a41b540f8e1
public: true
video: https://www.youtube.com/watch?v=vVbrlNlqJP4
notebooklm: true
---

# Serverroller

## Introduksjon

En server er ikke bare en kraftig datamaskin — det er en maskin med spesifikke roller og ansvar i nettverket. I Windows Server installerer du tjenester som "serverroller" via Server Manager. Å kjenne de viktigste serverrollene, hva de gjør og hvilke protokoller de bruker, er essensielt for driftstøtte: du planlegger infrastrukturen, installerer tjenestene og holder dem i gang.

Serverroller er tett koblet til [[active-directory]], [[bruker-og-tilgangsstyring]] og [[filsystem]], og er en sentral del av [[driftsarkitektur]] i en bedrift. En domenekontroller er ikke én rolle, men en kombinasjon av AD DS, DNS og ofte DHCP som samarbeider.

## Teori

### Hva er en serverrolle?

En **serverrolle** er en tilleggsfunksjon man installerer i Windows Server via:
`Server Manager → Manage → Add Roles and Features`

Én fysisk server kan ha flere roller installert, men av ytelsesmessige og sikkerhetsmessige grunner anbefales det å holde rollene separate — spesielt i produksjon. I skolelab er det vanlig å ha AD DS, DNS og DHCP på samme domenekontroller.

### Oversikt over sentrale serverroller

| Rolle | Funksjon | Protokoll/port | Typisk bruk |
|-------|----------|----------------|-------------|
| AD DS | Sentralisert autentisering og katalog | Kerberos (88), LDAP (389) | Bedriftsnettverk med domene |
| DNS-server | Navneoppløsning | UDP/TCP 53 | Løse opp domenenavn til IP |
| DHCP-server | Automatisk IP-tildeling | UDP 67/68 | Klienter i nettverket |
| Webserver (IIS) | Betjene HTTP/HTTPS-forespørsler | TCP 80/443 | Internett/intranett-portal |
| Filserver | Dele mapper over nettverket | SMB (TCP 445), NFS | Felles lagring for ansatte |
| Printserver | Dele og administrere skrivere | TCP 9100, LPD (515) | Delte skrivere i nettverk |
| E-postserver | Sende og motta e-post | SMTP 25, IMAP 143, POP3 110 | Bedriftens e-posttjeneste |

---

### Active Directory Domain Services (AD DS)

AD DS er grunnmuren i et Windows-domenenettverk. En server med AD DS-rollen kalles en **domenekontroller** og administrerer:
- **Autentisering**: logger inn brukere med brukernavn og passord
- **Autorisasjon**: kontrollerer hva brukere har tilgang til
- **Katalog**: sentralt register over alle brukere, datamaskiner og ressurser

**AD DS** — Active Directory Domain Services — er altså en katalogtjeneste som sentraliserer administrasjon av brukere, grupper og datamaskiner i et nettverk.

#### AD-hierarkiet

```
Skog (Forest)
  └── Tre (Tree): firma.no
        └── Domene: firma.no
              ├── Underdomene: salg.firma.no
              └── OU: Ansatte
                    ├── OU: Oslo
                    └── OU: Bergen
```

- **Skog**: øverste nivå, inneholder ett eller flere trær
- **Tre**: domene med underdomener som deler et navnerom
- **Domene**: administrativ grense (f.eks. `lab.lan`)
- **OU (Organizational Unit)**: logisk mappe for organisering av objekter, støtter Group Policy
- **FQDN**: Fully Qualified Domain Name — f.eks. `pc01.lab.lan`

#### Brukere og grupper

- **Brukerkontoer**: tilordnes individuelt til ressurser, eller via gruppmedlemskap
- **Sikkerhetsgrupper**: en konto kan tilhøre flere grupper → skalerbar tilgangsstyring
- **OU vs. mappe**: OU støtter Group Policy Objects (GPO) og delegert administrasjon

Domenekontrolleren krever DNS — DNS-serverrollen installeres automatisk eller manuelt under AD DS-oppsett.

---

### DNS-server

DNS-serveren oversetter domenenavn til IP-adresser. I et AD-nettverk er domenekontrollerens DNS **autoritativ** for det lokale domenet og kjenner alle AD-objekter.

Konfigurasjon i Windows Server:
- Soner (Zones): primærsone for `lab.lan` opprettes automatisk med AD DS
- Forwarders: oppslag utenfor `lab.lan` videresendes til ruter (f.eks. `192.168.1.1`) eller offentlig DNS (`8.8.8.8`)
- Dynamisk oppdatering: klienter registrerer seg automatisk i DNS ved domene-join

Se [[dns-og-dhcp]] for full gjennomgang av DNS.

---

### DHCP-server

DHCP-serveren tildeler automatisk IP-konfigurasjon til nettverksklienter. I domenemiljø overtar denne rollen fra ruterens innebygde DHCP.

Et **DHCP Scope** er et definert område med IP-adresser som DHCP-serveren kan tildele klienter på et bestemt subnett.

Viktige steg:
1. Deaktiver DHCP på ruteren
2. Installer DHCP Server-rollen i Windows Server
3. Opprett et scope (f.eks. `192.168.1.100`–`192.168.1.200`)
4. Konfigurer scope-alternativer: gateway, DNS-server, leasetid
5. Aktiver scope

Se [[dns-og-dhcp]] for full gjennomgang av DHCP.

---

### Webserver — IIS (Internet Information Services)

**IIS** (Internet Information Services) er Microsofts webserver-rolle som brukes til å hoste nettsider eller webapplikasjoner. Det er en serverrolle tilgjengelig i Windows Server.

**Funksjon**: betjener HTTP/HTTPS-forespørsler fra nettlesere. Brukes til:
- Interne portaler og intranett-sider
- Nettapplikasjoner (ASP.NET, PHP)
- Administratorgrensesnitt for andre tjenester

**Konkurrenter**:
- **Apache HTTP Server** — åpen kildekode, dominerende på Linux
- **Nginx** — åpen kildekode, kjent for høy ytelse og reverse proxy-bruk

**Oppsett av nettsted i IIS**:
1. Server Manager → Add Roles → Web Server (IIS)
2. IIS Manager → Sites → Add Website
3. Angi navn, fysisk mappe (f.eks. `C:\inetpub\wwwroot\minside`), port og eventuelt hostnavn
4. Bind domenenavn i DNS til serverens IP

---

### Filserver

En filserver gjør mapper tilgjengelig over nettverket slik at brukere kan lagre og hente filer fra en sentral plassering.

**SMB (Server Message Block)** er Windows-standarden for nettverksdeling, port 445.

**Sette opp en delt mappe (share)**:
1. Høyreklikk mappe → Properties → Sharing → Advanced Sharing
2. Hak av "Share this folder", gi sharenavn (f.eks. `Dokumenter`)
3. Sett delingsrettigheter (hvem kan lese/skrive via share)
4. Sett NTFS-rettigheter for finmasket tilgangskontroll

**NTFS-rettigheter** er filsystem-nivå rettigheter som bestemmer hvilken tilgang brukere og grupper har til filer og mapper på en filserver. De er mer granulære enn share-rettigheter og gjelder også ved lokal tilgang.

Tilgang fra klient:
```
\\servernavn\Dokumenter
```
Eller via "Map network drive" for å tilordne en stasjonsbokstav (f.eks. Z:).

**NFS (Network File System)**: Linux-/Unix-standard for fildeling. Brukes i hetrogene miljøer. Windows Server støtter NFS via "File Services"-rollen.

**NAS (Network Attached Storage)**: dedikert lagringsenhet med filserver-funksjonalitet (f.eks. TrueNAS, Synology). Alternativ til Windows-filserver for enklere oppsett og stor lagringskapasitet.

---

### E-postserver

En e-postserver håndterer sending og mottak av e-post for et domene.

| Komponent | Funksjon | Protokoll |
|-----------|----------|-----------|
| MTA (Mail Transfer Agent) | Sender og videresender e-post mellom servere | SMTP (port 25) |
| MDA (Mail Delivery Agent) | Leverer e-post til brukerens postboks | Intern |
| MUA (Mail User Agent) | Klientprogrammet (Outlook, Thunderbird) | IMAP/POP3 |

Eksempler på e-postserverløsninger: Microsoft Exchange Server (Windows), Postfix/Dovecot (Linux), hMailServer (enkel Windows-løsning).

---

### Printserver

En printserver deler én eller flere skrivere i nettverket slik at alle brukere kan skrive ut uten å koble fysisk til skriveren.

I Windows Server: Add Roles → Print and Document Services → Print Server.

Administrasjon via **Print Management**-konsollen: se køer, administrer drivere, overvåk status.

---

### Typisk serveroppsett i datalab (VG2)

```
[Windows Server 2022]
├── AD DS (domenekontroller for lab.lan)
├── DNS-server (autoritativ for lab.lan, forwarder: 192.168.1.1)
├── DHCP-server (scope: 192.168.1.100–200)
└── Filserver (share: \\server01\Elever)

[Klientmaskiner: Windows 10/11]
└── Domene-joined til lab.lan
    └── Pålogger med domenebrukere fra AD
    └── Får IP fra DHCP-serveren
    └── Løser opp lab.lan via DNS-serveren
```

Statisk IP på server: `192.168.1.10/24`, gateway `192.168.1.1`, DNS `192.168.1.10` (seg selv).

## Eksempel / lab

### Lab: Installer AD DS og koble en klient til domenet

1. **Installer AD DS-rollen** på Windows Server:
   - Server Manager → Add Roles → Active Directory Domain Services
   - Etterpå: Promote this server to a domain controller
   - Velg "Add a new forest", domenenavn: `lab.lan`
   - Sett DSRM-passord, fullfør veiviseren, start om

2. **Koble en Windows-klient til domenet**:
   - Klientmaskin → Settings → System → About → Join a domain
   - Skriv inn `lab.lan`, oppgi domenekontrollerens administrator-legitimasjon
   - Restart klienten
   - Logg inn med domenebrukernavn: `lab\brukernavn`

3. **Opprett en bruker i AD**:
   - Server Manager → Tools → Active Directory Users and Computers
   - Naviger til ønsket OU → New → User
   - Fyll inn fornavn, etternavn og påloggingsnavn

## Study guide

**Serverroller — kjerneforståelse**
En Windows Server er en plattform for å kjøre tjenester ("roller"). De viktigste å kjenne for VG2 er: AD DS (domene og autentisering), DNS (navneoppløsning), DHCP (IP-tildeling), IIS (webserver) og Filserver (SMB-deling).

**AD DS — det viktigste å forstå**
AD DS er fundamentet. Det samler brukerkontoer, datamaskiner og policyer i ett sentralt system. En domenekontroller er en server med AD DS-rollen. OU-er strukturerer AD og er ankerpunktet for Group Policy. DNS er en forutsetning for AD.

**Filserver og tilgangskontroll**
NTFS-rettigheter gjelder alltid, share-rettigheter gjelder kun ved nettverkstilgang. Når begge er satt, er det den mest restriktive kombinasjonen som gjelder. Mappestruktur og rettigheter henger tett sammen med [[bruker-og-tilgangsstyring]].

**Vanlige eksamenspoeng**
- Forskjellen mellom OU og en vanlig mappe i AD
- Hva FQDN betyr og eksempel
- Stegene for å koble en klient til et domene
- Hvilke protokoller/porter de ulike serverrollene bruker

## FAQ

**Hva er forskjellen mellom en OU og en mappe i Active Directory?**
En OU (Organizational Unit) er en logisk container i AD som støtter delegert administrasjon og Group Policy Objects (GPO). En vanlig mappe støtter ikke dette. OU-er brukes til å strukturere AD og styre policyer for grupper av brukere eller datamaskiner.

**Hvilken protokoll bruker en Windows-filserver for nettverksdeling, og hvilken port?**
SMB (Server Message Block), port 445 (TCP). Eldre versjoner brukte port 139 (via NetBIOS).

**Hva er forskjellen mellom IIS, Apache og Nginx?**
Alle tre er webservere. IIS er Microsofts løsning for Windows Server. Apache er den mest brukte åpen kildekode-webserveren, primært på Linux. Nginx er kjent for høy ytelse og brukes mye som reverse proxy og lastbalanserer, i tillegg til webserver. IIS er integrert med Windows-autentisering og .NET.

**Hva er et FQDN, og gi et eksempel?**
FQDN (Fully Qualified Domain Name) er det fullstendige domenenavnet til en enhet, inkludert alle ledd frem til roten. Eksempel: `pc01.lab.lan` — her er `pc01` maskinnavnet, `lab` er domenet og `lan` er toppdomenet.

**Hvorfor trenger en domenekontroller DNS-serverrollen?**
Active Directory er avhengig av DNS for at klienter skal finne domenekontrolleren (via SRV-poster i DNS). Uten DNS kan klienter ikke logge inn, finne AD-tjenester eller kommunisere med domenet. DNS-rollen installeres derfor alltid i kombinasjon med AD DS.

**Hva er DHCP Scope og hvorfor er det viktig å konfigurere det riktig?**
Et DHCP Scope er adresserommet serveren deler ut fra. Feil konfigurasjon (for lite adresser, feil gateway eller DNS) betyr at klienter ikke kan nå nettverket. Scope-alternativer som gateway og DNS-server er like viktige som adressene selv.

**Hva er AD DS og hvorfor er det sentralt i bedriftsnettverk?**
AD DS er katalogtjenesten som samler alle nettverksobjekter (brukere, grupper, maskiner) i ett sted. I stedet for at hver bruker har lokale kontoer på hver maskin, logger alle inn med sin AD-konto — og tilganger styres sentralt via grupper og policyer.

**Hva er forskjellen mellom NTFS-rettigheter og share-rettigheter?**
Share-rettigheter gjelder kun når man kobler til mappen via nettverket. NTFS-rettigheter gjelder alltid — også ved lokal tilgang. Beste praksis er å sette share til "Everyone - Full Control" og bruke NTFS-rettigheter for den faktiske tilgangskontrollen.

## Quiz

<details>
<summary>Spørsmål 1: Hva er forskjellen mellom en OU og en mappe i Active Directory?</summary>

**Svar:** En OU (Organizational Unit) er en logisk container i AD som støtter delegert administrasjon og Group Policy Objects (GPO). En vanlig mappe støtter ikke dette. OU-er brukes til å strukturere AD og styre policyer for grupper av brukere eller datamaskiner.
</details>

<details>
<summary>Spørsmål 2: Hvilken protokoll bruker en Windows-filserver for nettverksdeling, og hvilken port?</summary>

**Svar:** SMB (Server Message Block), port 445 (TCP). Eldre versjoner brukte port 139 (via NetBIOS).
</details>

<details>
<summary>Spørsmål 3: Hva er forskjellen mellom IIS, Apache og Nginx?</summary>

**Svar:** Alle tre er webservere. IIS er Microsofts løsning for Windows Server. Apache er den mest brukte åpen kildekode-webserveren, primært på Linux. Nginx er kjent for høy ytelse og brukes mye som reverse proxy og lastbalanserer, i tillegg til webserver. IIS er integrert med Windows-autentisering og .NET.
</details>

<details>
<summary>Spørsmål 4: Hva er et FQDN, og gi et eksempel?</summary>

**Svar:** FQDN (Fully Qualified Domain Name) er det fullstendige domenenavnet til en enhet, inkludert alle ledd frem til roten. Eksempel: `pc01.lab.lan` — her er `pc01` maskinnavnet, `lab` er domenet og `lan` er toppdomenet.
</details>

<details>
<summary>Spørsmål 5: Hvorfor trenger en domenekontroller DNS-serverrollen?</summary>

**Svar:** Active Directory er avhengig av DNS for at klienter skal finne domenekontrolleren (via SRV-poster i DNS). Uten DNS kan klienter ikke logge inn, finne AD-tjenester eller kommunisere med domenet. DNS-rollen installeres derfor alltid i kombinasjon med AD DS.
</details>

## Flashcards

Serverrolle :: Tilleggsfunksjon installert i Windows Server via Server Manager (f.eks. AD DS, DNS, DHCP, IIS)
AD DS :: Active Directory Domain Services — domenekontrollerrolle som sentraliserer autentisering og katalogtjenester
Domenekontroller :: Server med AD DS-rollen som administrerer brukere, grupper og policyer i et domene
OU :: Organizational Unit — logisk container i AD som støtter Group Policy og delegert administrasjon
IIS :: Internet Information Services — Microsofts webserver for Windows Server, betjener HTTP/HTTPS
SMB :: Server Message Block — Windows-protokollen for nettverksdeling av mapper og filer (port 445)
FQDN :: Fully Qualified Domain Name — fullstendig domenenavn f.eks. pc01.lab.lan
MTA :: Mail Transfer Agent — serverprogramvare som sender og videresender e-post via SMTP
GPO :: Group Policy Object — policysett i AD som distribuerer innstillinger til brukere og maskiner
NAS :: Network Attached Storage — dedikert lagringsenhet med filserverfunksjonalitet
DHCP Scope :: Et definert område med IP-adresser som DHCP-serveren kan tildele klienter på et bestemt subnett
NTFS-rettigheter :: Filsystem-nivå rettigheter som bestemmer hvilken tilgang brukere og grupper har til filer og mapper på en filserver

## Ressurser

- [Brukerkontoer, grupper og struktur i AD — NDLA](https://ndla.no/r/driftsstotte-im-itk-vg2/brukerkontoer-grupper-og-struktur-i-active-directory/2c7a25f92e)
- [Domener og hierarkiet i Active Directory — NDLA](https://ndla.no/en/r/driftsstotte-im-itk-vg2/domener-og-hierarkiet-i-active-directory/db58e9da66)
- [Koble opp share i Windows 10 — NDLA](https://ndla.no/en/r/driftsstotte-im-itk-vg2/koble-opp-share-i-windows-10/5a04d2403d)
- [HTTP og IIS — windowsnett.no](http://www.windowsnett.no/leksjoner/L09/Leksjon%209%20beskrivelse.htm)
- [windowsnett.no — leksjon 5–7: AD, grupper, delte mapper](https://www.windowsnett.no/)
- [Active Directory, DNS & DHCP Roles Installation & Configuration on Server 2022 — PowerUser (15 min)](https://www.youtube.com/watch?v=vVbrlNlqJP4)
- [Getting Started with AD DS — Microsoft Learn](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/ad-ds-getting-started)
