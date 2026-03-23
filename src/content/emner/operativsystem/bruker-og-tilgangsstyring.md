---
title: "Bruker- og tilgangsstyring"
emne: operativsystem
kompetansemaal:
  - km-04
kilder:
  - ndla
  - https://learn.microsoft.com/nb-no/windows-server/identity/ad-ds/active-directory-domain-services
tags: []
flashcards: true
public: true
notebooklm: true
---

## Introduksjon

Bruker- og tilgangsstyring er kjernen i km-04 og én av de viktigste oppgavene en IT-driftsteknikker utfører. Målet er å sikre at **riktige personer har tilgang til riktige ressurser — og ikke mer**. Dette kalles prinsippet om minste privilegium (*Least Privilege*).

Denne artikkelen dekker Windows-brukeradministrasjon (lokalt og i domene), sikkerhetsgrupper, tilgangskontroll og tilsvarende verktøy i Linux. Brukeradministrasjon i domenemiljøer forutsetter kunnskap om [[active-directory]]. For Linux-kommandoer, se [[linux-grunnleggende]], og for automatisering av brukeropprettelse, se [[powershell-grunnleggende]].

---

## Teori

### Lokale kontoer vs. domenekontoer

| Egenskap | Lokal konto | Domenekonto |
|---|---|---|
| Lagret i | Lokal SAM-database | Active Directory (DC) |
| Gyldig på | Kun denne maskinen | Alle maskiner i domenet |
| Administreres via | `lusrmgr.msc` / PowerShell | ADUC / PowerShell |
| Brukes til | Frittstående maskiner | Bedriftsmiljøer med AD |
| Eksempel | `.\Administrator` | `SKOLE\Elev01` |

### Innebygde standardkontoer

**Administrator (SID …-500)**
Den innebygde administratorkontoen som opprettes ved Windows-installasjon. Kan ikke slettes. Har full kontroll over systemet. Best practice i produksjon: gi kontoen et annet navn og deaktiver den — opprett heller en navngitt adminkonto.

**Guest (SID …-501)**
Begrenset gjestekonto. Deaktivert som standard. Bør forbli deaktivert i alle produksjonsmiljøer.

**KRBTGT (domene)**
Intern domenekonto brukt av Kerberos-autentiseringstjenesten. Skal aldri logge inn interaktivt. Passordet bør roteres med jevne mellomrom som sikkerhetstiltak.

### Kontoinnstillinger i Windows

Når du oppretter eller redigerer en brukerkonto, kan du styre:

- **Bruker må endre passord ved neste pålogging** — tvinger nyansatte til å sette eget passord
- **Bruker kan ikke endre passord** — for tjenestekontoer
- **Passord utløper aldri** — for tjenestekontoer (ikke for vanlige brukere)
- **Konto deaktivert** — brukes ved oppsigelse i stedet for sletting (bevarer data og tilhørighet)
- **Konto er låst** — settes automatisk etter for mange feilpassord (kan manuelt låses opp)

### SID — Security Identifier

Hver brukerkonto og gruppe i Windows tildeles et unikt **SID** (Security Identifier) ved opprettelse. SID er det operativsystemet faktisk bruker internt — ikke brukernavnet. Dette betyr:

- Hvis du sletter og gjenoppretter en konto med samme navn, får den et nytt SID og mister alle tidligere tilganger
- Tillatelser i ACL-er lagres som SID-er, ikke navn

### Prinsippet om minste privilegium

Brukere og prosesser skal kun ha de rettighetene som er absolutt nødvendige for å utføre jobben sin. I praksis:

- Ikke gi alle Domain Admins
- Skill mellom daglig brukerkonto og adminkonto (administratorer har to kontoer)
- Fjern tilganger når de ikke lenger trengs
- Bruk grupper for tilgangsstyring — aldri tildel rettigheter direkte til enkeltbrukere

### UAC — User Account Control

UAC er en sikkerhetsmekanisme i Windows som hindrer programmer i å kjøre med administrative rettigheter uten brukerens eksplisitte godkjenning. Selv om du er logget inn som administrator, kjøres programmer med standard brukerrettigheter inntil UAC godkjenner en forhøyning (*elevation*).

Når et program ber om administratorrettigheter, vises UAC-dialogen. Standardbruker må taste inn adminpassord; administrator klikker bare «Ja».

### Sikkerhetsgrupper i Active Directory

Grupper lar deg tildele tilganger til mange brukere på én gang. Best practice: **tildel alltid tillatelser til grupper, aldri til enkeltbrukere**.

**Gruppeomfang (scope):**

| Omfang | Kan inneholde | Kan brukes til tillatelser i |
|---|---|---|
| Domenelokal | Brukere, grupper fra alle domener | Kun eget domene |
| Global | Brukere og grupper fra eget domene | Alle domener i skogen |
| Universell | Brukere og grupper fra alle domener | Alle domener i skogen |

**Innebygde grupper (eksempler):**

| Gruppe | Rettigheter |
|---|---|
| Domain Admins | Full administrasjonstilgang til domenet |
| Enterprise Admins | Full tilgang til hele AD-skogen |
| Domain Users | Standard for alle domenebrukere |
| Administrators (lokal) | Full lokal administrasjonstilgang |
| Guests | Svært begrenset tilgang |

### AAA-prinsippet

Tilgangskontroll bygger på tre steg:

1. **Autentisering** — Hvem er du? (brukernavn + passord, MFA, smartkort)
2. **Autorisasjon** — Hva har du lov til? (grupper, ACL-er, rettigheter)
3. **Revisjon** — Hva har du gjort? (hendelseslogger, sikkerhetssporing)

### RBAC — Rollebasert tilgangsstyring

**Rollebasert tilgangsstyring (RBAC)** er en utvidelse av prinsippet om minste privilegium. I stedet for å tildele rettigheter direkte til enkeltbrukere, knyttes tillatelser til **roller** (f.eks. «Regnskapsfører», «IT-administrator», «Elev»). Brukere tildeles deretter roller.

Fordeler med RBAC:
- Enklere å administrere ved store brukermengder
- Enklere revisjon («hvem har rollen X?» er ett spørsmål, ikke mange)
- Lavere risiko for feilkonfigurering — nye brukere arver rollen automatisk

I Windows AD implementeres RBAC i praksis ved hjelp av sikkerhetsgrupper: én gruppe per rolle, rettigheter tildeles gruppen.

### Integrasjon mellom Windows og Linux

I større miljøer er det ønskelig at Linux-klienter kan logge inn mot Windows-domenet. Dette gjøres typisk med:
- **SSSD** (System Security Services Daemon) — lar Linux autentisere mot AD
- **Samba/Winbind** — alternativ løsning for domeneintegrasjon

Dette er avansert stoff, men konseptet er viktig: ett sentralt brukersystem (AD) for både Windows og Linux.

---

## Eksempel / lab

### Administrere lokale brukere med PowerShell

**Opprett ny lokal bruker:**
```powershell
New-LocalUser -Name "Elev01" -Password (ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force) -FullName "Elev Elevsen" -Description "Testkonto"
```

**Legg brukeren til i en gruppe:**
```powershell
Add-LocalGroupMember -Group "Users" -Member "Elev01"
```

**List alle lokale brukere:**
```powershell
Get-LocalUser
```

**Deaktiver en konto:**
```powershell
Disable-LocalUser -Name "Elev01"
```

**Fjern bruker fra gruppe:**
```powershell
Remove-LocalGroupMember -Group "Users" -Member "Elev01"
```

### Linux-ekvivalenter

**Opprett bruker:**
```bash
sudo useradd -m -s /bin/bash elev01
```
Flaggene `-m` oppretter hjemmemappe og `-s` setter standard shell.

**Sett passord:**
```bash
sudo passwd elev01
```

**Legg bruker til i gruppe (f.eks. sudo):**
```bash
sudo usermod -aG sudo elev01
```

**Vis brukerens grupper:**
```bash
groups elev01
id elev01
```

**Deaktiver konto (lås passord):**
```bash
sudo passwd -l elev01
```

### Strukturen i /etc/passwd

Hver linje i `/etc/passwd` har sju felt separert med kolon:
```
brukernavn:x:UID:GID:GECOS:hjemmemappe:shell
elev01:x:1001:1001:Elev Elevsen:/home/elev01:/bin/bash
```

- `x` betyr at passordet er lagret i `/etc/shadow` (kryptert)
- UID 0 = root, UID 1–999 = systembrukere, UID 1000+ = vanlige brukere

### Strukturen i /etc/group

```
gruppenavn:x:GID:medlemmer
sudo:x:27:elev01,admin
```

---

## Study guide

**Bruker- og tilgangsstyring** handler om å sikre at riktige personer har tilgang til riktige ressurser. Kjerneprinsippet er **minste privilegium**: gi aldri mer tilgang enn nødvendig.

To kontotyper å skille mellom:
- **Lokale kontoer** lagres i maskinens SAM-database og gjelder kun lokalt
- **Domenekontoer** lagres i Active Directory og fungerer på alle domene-tilknyttede maskiner

Viktige Windows-konsepter:
- **SID** — Windows bruker ikke brukernavn internt, men SID. Sletter du og gjenoppretter en konto med samme navn, mister den alle tilganger
- **UAC** — hindrer programmer i å eskalere til adminrettigheter uten eksplisitt bekreftelse
- **Sikkerhetsgrupper** — tildel alltid tillatelser til grupper, aldri enkeltbrukere
- **Gruppeomfang** — domenelokale grupper for tillatelser lokalt, globale grupper for å samle brukere, universelle grupper for skog-nivå

AAA-rammeverket oppsummerer tilgangskontroll: **Autentisering** (hvem er du?), **Autorisasjon** (hva har du lov til?), **Revisjon** (hva har du gjort?).

Linux-ekvivalenter:
- Brukere opprettes med `useradd`, endres med `usermod`, slettes med `userdel`
- Grupper administreres med `groupadd` og `gpasswd`
- `/etc/passwd` inneholder brukerinfo; `/etc/shadow` inneholder krypterte passord (kun root kan lese)
- Tilgangsrettigheter styres av rwx-modellen — se [[linux-grunnleggende]] for detaljer

---

## FAQ

**Hvorfor bør man ikke bruke Administrator-kontoen til daglig bruk?**
Administrator-kontoen (SID ...-500) har ubegrenset tilgang og kan ikke deaktiveres permanent. Daglig bruk øker risikoen for at skadelig programvare eller menneskelige feil gjør permanent skade. Bruk en navngitt brukerkonto med begrenset tilgang, og en separat adminkonto kun når nødvendig.

**Hva skjer med tilganger hvis jeg sletter og gjenoppretter en bruker med samme navn?**
Den nye kontoen får et nytt SID. Alle NTFS-tillatelser, gruppemedlemskap og ressurskoblinger er knyttet til det gamle SID-et og må settes opp på nytt. Bruk derfor deaktivering fremfor sletting ved oppsigelser.

**Hva er forskjellen mellom global, domenelokal og universell gruppe?**
Global gruppe samler brukere fra eget domene og kan brukes til tillatelser i alle domener i skogen. Domenelokal gruppe brukes til tillatelser lokalt og kan inneholde brukere fra alle domener. Universell gruppe kan inneholde brukere fra hele skogen og brukes i skog-nivå-scenarier.

**Hva gjør `-aG` i `usermod -aG sudo elev01`?**
`-a` (append) legger brukeren til i gruppen uten å fjerne eksisterende gruppemedlemskap. Uten `-a` ville kommandoen erstatte alle eksisterende gruppemedlemskap med kun `sudo`.

**Hva er RBAC og hvorfor brukes det?**
Rollebasert tilgangsstyring knytter rettigheter til roller fremfor enkeltpersoner. Det forenkler administrasjon: nye ansatte tildeles en rolle og får automatisk riktig tilgang. Det reduserer også feil og gjør revisjon enklere.

**Hva er forskjellen mellom autentisering og autorisasjon?**
Autentisering verifiserer identiteten din (du er den du utgir deg for å være). Autorisasjon bestemmer hva du har lov til å gjøre etter du er autentisert. Et system kan autentisere deg uten å gi deg tilgang til noe som helst.

---

## Quiz

<details><summary>Spørsmål 1: Hva er forskjellen mellom en lokal konto og en domenekonto?</summary>

**Svar:** En lokal konto er lagret i maskinens SAM-database og gjelder kun på den maskinen. En domenekonto er lagret i Active Directory og kan brukes til å logge inn på alle maskiner i domenet.

</details>

<details><summary>Spørsmål 2: Hva er SID og hvorfor er det viktig?</summary>

**Svar:** SID (Security Identifier) er en unik identifikator Windows tildeler hver konto. Operativsystemet bruker SID internt i stedet for brukernavnet. Hvis en konto slettes og gjenopprettes med samme navn, får den et nytt SID og mister alle tidligere tilganger.

</details>

<details><summary>Spørsmål 3: Hva betyr prinsippet om minste privilegium?</summary>

**Svar:** Brukere og prosesser skal kun ha de rettighetene som er absolutt nødvendige for å utføre jobben sin — ikke mer. Dette begrenser skadeomfanget ved kompromitterte kontoer.

</details>

<details><summary>Spørsmål 4: Hva er UAC og hva beskytter det mot?</summary>

**Svar:** User Account Control er en sikkerhetsmekanisme som hindrer programmer i å kjøre med administrative rettigheter uten eksplisitt godkjenning. Det beskytter mot at skadelig programvare stille i bakgrunnen får adminrettigheter selv når brukeren er logget inn som administrator.

</details>

<details><summary>Spørsmål 5: Hvilken PowerShell-kommando legger brukeren "Elev01" til i gruppen "Users"?</summary>

**Svar:** `Add-LocalGroupMember -Group "Users" -Member "Elev01"`

</details>

<details><summary>Spørsmål 6: Hva gjør kommandoen `usermod -aG sudo elev01` i Linux?</summary>

**Svar:** Den legger brukeren `elev01` til i gruppen `sudo` uten å fjerne brukeren fra andre grupper (`-a` = append, `-G` = supplementary groups). Dette gir brukeren mulighet til å kjøre kommandoer med root-rettigheter via `sudo`.

</details>

---

## Flashcards

Lokal konto :: Brukerkonto lagret i maskinens SAM-database, gyldig kun på denne maskinen
Domenekonto :: Brukerkonto lagret i Active Directory, gyldig på alle maskiner i domenet
SID :: Security Identifier — unik numerisk identifikator Windows tildeler hver konto og gruppe
Prinsippet om minste privilegium :: Brukere skal kun ha de rettighetene de trenger for jobben sin
UAC :: User Account Control — Windows-mekanisme som krever eksplisitt godkjenning for administrative operasjoner
Domain Admins :: Innebygd AD-gruppe med full administrasjonstilgang til domenet
Sikkerhetsgruppe :: AD-objekt som samler brukere for felles tilgangsstyring
Domenelokal gruppe :: Gruppe som kan brukes til tillatelser kun i eget domene
Global gruppe :: Gruppe fra eget domene som kan brukes til tillatelser i alle domener i skogen
AAA :: Autentisering, Autorisasjon og Revisjon — grunnprinsippene for tilgangskontroll
useradd :: Linux-kommando for å opprette en ny brukerkonto
usermod -aG :: Linux-kommando for å legge en bruker til i en tilleggsgruppe uten å fjerne eksisterende gruppemedlemskap
/etc/shadow :: Linux-fil som lagrer krypterte passord (kun root kan lese)
RBAC :: Rollebasert tilgangsstyring — rettigheter knyttes til roller, ikke enkeltpersoner
Sudoers :: Konfigurasjonsfil i Linux (`/etc/sudoers`) som definerer hvem som kan kjøre kommandoer med root-rettigheter
SSSD :: System Security Services Daemon — lar Linux-klienter autentisere mot Active Directory

---

## Ressurser

- [Microsoft Learn: AD-standardkontoer](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-default-user-accounts)
- [Microsoft Learn: AD-sikkerhetsgrupper](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups)
- [Microsoft Learn: Administrere brukerkontoer i Windows Server](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage-user-accounts-in-windows-server)
- [Ubuntu Server: Brukerhåndtering](https://documentation.ubuntu.com/server/how-to/security/user-management/)
- [Microsoft Learn: Active Directory Domain Services](https://learn.microsoft.com/nb-no/windows-server/identity/ad-ds/active-directory-domain-services)
