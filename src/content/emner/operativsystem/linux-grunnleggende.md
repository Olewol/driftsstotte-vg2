---
title: "Linux – grunnleggende"
emne: operativsystem
kompetansemaal:
  - km-04
kilder:
  - ndla
  - https://documentation.ubuntu.com/server/how-to/security/user-management/
tags: []
flashcards: true
public: true
notebooklm: true
---

## Introduksjon

Linux er et åpen kildekode-operativsystem som brukes i stort omfang på servere, skyplattformer og nettverksenheter. For IT-driftsteknikere er grunnleggende Linux-kunnskap nødvendig — mye av infrastrukturen i profesjonelle miljøer kjøres på Linux.

Denne artikkelen dekker Linux-filstrukturen, filrettighetsmodellen (rwx), brukeradministrasjon og de mest brukte kommandoene. Sammenligninger med Windows-ekvivalenter er inkludert der det er nyttig. Filsystemet ext4 som Linux typisk bruker er beskrevet i [[filsystem]], og Linux-brukeradministrasjon henger tett sammen med [[bruker-og-tilgangsstyring]]. For viderekomne skriptoppgaver i Linux-terminalen, se [[bash-grunnleggende]].

---

## Teori

### Linux-filstruktur

Linux har én enkelt filtre med rot i `/` — det finnes ingen `C:\`-stasjon slik som i Windows. Alt er montert inn i dette treet.

| Katalog | Innhold og formål |
|---|---|
| `/` | Rotkatalogen — toppen av hele filsystemet |
| `/etc` | Konfigurasjonsfiler for systemet og tjenester (f.eks. `/etc/passwd`, `/etc/ssh/sshd_config`) |
| `/home` | Hjemmemapper for vanlige brukere (f.eks. `/home/elev01`) |
| `/root` | Hjemmemappen til root-brukeren (ikke under `/home`) |
| `/var` | Variable data — loggfiler (`/var/log`), spool-filer, databaser |
| `/bin` | Grunnleggende systemkommandoer tilgjengelig for alle brukere (f.eks. `ls`, `cp`) |
| `/usr/bin` | Brukerprogrammer og kommandoer installert av pakkebehandleren |
| `/sbin` | Systemadministrasjonskommandoer (krever root, f.eks. `fdisk`, `iptables`) |
| `/tmp` | Midlertidige filer — tømmes ved omstart |
| `/dev` | Enhetsfiler (f.eks. `/dev/sda` for harddisk) |
| `/proc` | Virtuelt filsystem med informasjon om kjørende prosesser |
| `/mnt` | Midlertidige monteringspunkter for eksterne disker |

### rwx-tillatelsesmodellen

Hver fil og mappe i Linux har tre sett med tillatelser for tre kategorier:

**Kategorier:**
- **Eier (user/u)** — brukeren som eier filen
- **Gruppe (group/g)** — gruppen som er tilknyttet filen
- **Andre (other/o)** — alle andre brukere

**Tillatelser:**
| Symbol | Tall | Fil | Mappe |
|---|---|---|---|
| r (read) | 4 | Les filinnhold | List opp filer i mappen |
| w (write) | 2 | Endre/slette filen | Opprette og slette filer i mappen |
| x (execute) | 1 | Kjør filen som program | Gå inn i mappen (`cd`) |

**Tolke `ls -l`-output:**

```
-rwxr-xr-- 1 elev01 lærere 4096 mars 20 10:00 skript.sh
```

- `-` → vanlig fil (mappe vises som `d`)
- `rwx` → eier (elev01) har les, skriv og kjør
- `r-x` → gruppe (lærere) har les og kjør, ikke skriv
- `r--` → andre har kun les

**Oktaltallsnotasjon:**
Hvert tillatelsessett summeres: r=4, w=2, x=1

```
rwxr-xr-x = 7  5  5 → chmod 755
rw-r--r-- = 6  4  4 → chmod 644
rwx------ = 7  0  0 → chmod 700
```

### chmod — endre tillatelser

**Oktalnotasjon:**
```bash
chmod 755 mappe/       # eier: rwx, gruppe: r-x, andre: r-x
chmod 644 dokument.txt # eier: rw-, gruppe: r--, andre: r--
chmod 700 privat/      # kun eier har tilgang
```

**Symbolsk notasjon:**
```bash
chmod u+x skript.sh    # legg til kjøretillatelse for eier
chmod g-w fil.txt      # fjern skrivetillatelse for gruppe
chmod o-r privat.txt   # fjern lesetillatelse for andre
chmod a+r offentlig    # alle (all) får lesetillatelse
```

**Rekursivt (alle filer i mappen):**
```bash
chmod -R 755 /var/www/
```

### chown — endre eier og gruppe

```bash
chown elev01 fil.txt              # endre eier til elev01
chown elev01:lærere fil.txt       # endre eier OG gruppe
chown :lærere fil.txt             # endre kun gruppe
chown -R elev01:lærere /home/delt # rekursivt
```

Tilsvarende: `chgrp lærere fil.txt` endrer kun gruppe.

### Sticky bit

Sticky bit på en mappe hindrer at brukere sletter filer de ikke eier, selv om de har skrivetillatelse til mappen. Brukes typisk på `/tmp`.

```bash
chmod +t /felles/         # sett sticky bit
ls -ld /felles/           # vises som 't' på slutten: drwxrwxrwt
```

### sudo og root

**Root-brukeren** (UID 0) er den allmektige superbrukeren i Linux — tilsvarer `Administrator` i Windows, men uten noen UAC-lignende begrensning. Root kan gjøre alt.

**sudo** (Superuser Do) lar vanlige brukere kjøre enkeltkommandoer med root-rettigheter:
```bash
sudo apt update           # kjør som root
sudo -i                   # åpne root-shell (vær forsiktig)
sudo -u elev01 kommando   # kjør som en annen bruker
```

Hvem som kan bruke sudo styres av `/etc/sudoers`. Redigeres alltid med `visudo` (kontrollerer syntaks før lagring):
```bash
sudo visudo
```

På Ubuntu legges brukere til i `sudo`-gruppen for å gi dem sudo-tilgang:
```bash
sudo usermod -aG sudo elev01
```

### Brukeradministrasjon

**Opprett bruker:**
```bash
sudo useradd -m -s /bin/bash elev01
# -m: opprett hjemmemappe
# -s: sett standard shell
```

Mer komplett:
```bash
sudo useradd -m -s /bin/bash -c "Elev Elevsen" -G sudo elev01
```

**Sett/endre passord:**
```bash
sudo passwd elev01
```

**Endre brukerinnstillinger:**
```bash
sudo usermod -aG lærere elev01    # legg til i gruppe
sudo usermod -s /bin/sh elev01    # endre shell
sudo usermod -L elev01            # lås konto (Lock)
sudo usermod -U elev01            # lås opp konto (Unlock)
```

**Slett bruker:**
```bash
sudo userdel elev01               # slett konto
sudo userdel -r elev01            # slett konto og hjemmemappe
```

**Gruppekommandoer:**
```bash
sudo groupadd lærere              # opprett gruppe
sudo gpasswd -a elev01 lærere    # legg bruker til i gruppe
sudo gpasswd -d elev01 lærere    # fjern bruker fra gruppe
```

### /etc/passwd og /etc/group

**/etc/passwd** — én linje per bruker:
```
brukernavn:passord:UID:GID:kommentar:hjemmemappe:shell
elev01:x:1001:1001:Elev Elevsen:/home/elev01:/bin/bash
root:x:0:0:root:/root:/bin/bash
```
- Passordet er `x` — faktisk hash lagres i `/etc/shadow`
- UID 0 = root, 1–999 = systembrukere, 1000+ = vanlige brukere

**/etc/group** — én linje per gruppe:
```
gruppenavn:passord:GID:medlemmer
sudo:x:27:elev01,admin
lærere:x:1002:elev01,elev02
```

### Nyttige kommandoer for tilgang og identitet

```bash
whoami                   # vis innlogget bruker
id                       # vis UID, GID og alle grupper
id elev01                # vis for spesifikk bruker
groups                   # list grupper for innlogget bruker
groups elev01            # list grupper for spesifikk bruker
ls -l fil.txt            # vis tillatelser, eier og gruppe
ls -ld mappe/            # vis tillatelser for selve mappen
stat fil.txt             # detaljert informasjon inkl. inode
```

### SUID og SGID — spesielle tillatelsesbit

I tillegg til sticky bit finnes to andre spesielle tillatelsesbit som er viktige å kjenne til:

**SUID (Set User ID)** — når SUID er satt på en kjørbar fil, kjøres programmet med **filens eiers** rettigheter, ikke den innloggede brukerens. Brukes f.eks. på `passwd`-kommandoen slik at vanlige brukere kan endre sitt eget passord (som krever skriving til `/etc/shadow`).

```bash
ls -l /usr/bin/passwd
# -rwsr-xr-x  → 's' i eierposisjonen betyr SUID
chmod u+s program       # sett SUID
```

**SGID (Set Group ID)** — på en fil: programmet kjøres med gruppens rettigheter. På en mappe: nye filer og undermapper i mappen arver mappens gruppe i stedet for oppretterens primærgruppe. Nyttig for delte arbeidsmapper.

```bash
chmod g+s /felles/prosjekt   # sett SGID på mappe
ls -ld /felles/prosjekt
# drwxrwsr-x  → 's' i gruppeposisjonen betyr SGID
```

### Systemlogging i Linux

Linux logger systemhendelser til `/var/log/`. Viktige loggfiler:

| Loggfil | Innhold |
|---|---|
| `/var/log/syslog` | Generelle systemmeldinger (Ubuntu/Debian) |
| `/var/log/auth.log` | Autentiseringshendelser, sudo-bruk, SSH-pålogginger |
| `/var/log/kern.log` | Kjernemeldinger |
| `/var/log/dpkg.log` | Pakkeinstallasjon og -oppdatering |

Moderne Linux bruker **journald** (systemd) for logging. Spørringer via `journalctl`:

```bash
journalctl -u ssh          # logg for SSH-tjenesten
journalctl -n 50           # siste 50 linjer
journalctl --since today   # logg fra i dag
journalctl -f              # følg logg live (tilsvarende tail -f)
```

---

## Eksempel / lab

### Lab: Opprett bruker og sett tillatelser

```bash
# 1. Opprett bruker med hjemmemappe
sudo useradd -m -s /bin/bash elev01

# 2. Sett passord
sudo passwd elev01

# 3. Opprett gruppe
sudo groupadd klasse2a

# 4. Legg bruker til i gruppe
sudo usermod -aG klasse2a elev01

# 5. Verifiser
id elev01

# 6. Opprett delt mappe
sudo mkdir /felles/klasse2a
sudo chown :klasse2a /felles/klasse2a
sudo chmod 770 /felles/klasse2a
# Kun eier og klasse2a-gruppen har tilgang

# 7. Aktiver sticky bit (brukere kan ikke slette andres filer)
sudo chmod +t /felles/klasse2a
```

### Sammenligning: Windows vs. Linux tilgangskontroll

| Oppgave | Windows | Linux |
|---|---|---|
| Opprett bruker | `New-LocalUser` | `useradd` |
| Sett passord | (del av New-LocalUser) | `passwd` |
| Legg til gruppe | `Add-LocalGroupMember` | `usermod -aG` |
| Vis brukerinfo | `Get-LocalUser` | `id`, `cat /etc/passwd` |
| Endre tillatelser | NTFS-egenskaper / `icacls` | `chmod` |
| Endre eier | `takeown` | `chown` |
| Admin-rettigheter | UAC / Administrator | `sudo` / root |

---

## Study guide

**Linux** er et åpen kildekode-operativsystem basert på Unix. Det er dominerende på servere, i sky og på nettverksenheter. Som IT-driftsteknikker bruker du Linux via terminalen.

**Filstrukturen** er ett enkelt tre med rot i `/`. Viktige kataloger:
- `/etc` — konfigurasjonsfiler (inkl. `/etc/passwd`, `/etc/shadow`, `/etc/sudoers`)
- `/home` — hjemmemapper for vanlige brukere
- `/var/log` — loggfiler fra systemet og tjenester
- `/tmp` — midlertidige filer, tømmes ved omstart
- `/bin` og `/usr/bin` — kommandoer og programmer

**Tillatelsesmodellen (rwx)** gir tre sett av tre tillatelser:
- **r** (read=4), **w** (write=2), **x** (execute=1)
- For **eier**, **gruppe** og **andre**
- Oktalsummering: `rwx = 7`, `r-x = 5`, `rw- = 6`
- Vanlige mønstre: `755` (mapper/programmer), `644` (vanlige filer), `700` (private filer)

**Brukeradministrasjon**:
- `useradd -m -s /bin/bash elev01` — opprett bruker
- `passwd elev01` — sett passord
- `usermod -aG sudo elev01` — gi sudo-tilgang
- `userdel -r elev01` — slett bruker og hjemmemappe

**Sudo og root**: Root (UID 0) er allmektig. Aldri logg inn som root direkte — bruk `sudo` for enkeltstående administrative kommandoer. `/etc/sudoers` styrer hvem som kan bruke sudo; redigeres alltid med `visudo`.

Spesielle tillatelsesbit: **sticky bit** (hindrer sletting av andres filer i delt mappe), **SUID** (programmet kjøres med filens eiers rettigheter), **SGID** (filer arver mappens gruppe).

---

## FAQ

**Hva er forskjellen mellom `useradd` og `adduser`?**
`useradd` er det lave systemverktøyet tilgjengelig på alle Linux-distribusjoner. `adduser` er et mer brukervennlig skript (tilgjengelig på Debian/Ubuntu) som stiller spørsmål interaktivt og setter opp hjemmemappe og passord automatisk. I skript brukes `useradd`.

**Hvorfor starter systembrukere på UID 1–999 og vanlige brukere på UID 1000?**
Systembrukere (UID 1–999) er kontoer opprettet for tjenester og prosesser, ikke for mennesker som logger inn (f.eks. `www-data` for Apache, `postgres` for databasetjenesten). De separeres fra vanlige brukere for sikkerhets- og administrasjonsformål.

**Hva skjer hvis jeg glemmer `-a` i `usermod -aG`?**
Uten `-a` vil `usermod -G sudo elev01` erstatte alle eksisterende gruppemedlemskap med kun `sudo`. Brukeren mister alle andre grupper de var medlem av. Bruk alltid `-aG` for å legge til.

**Kan jeg sette passord for root og logge inn direkte?**
Teknisk ja, men det anbefales sterkt ikke i produksjonsmiljøer. SSH bør konfigureres til å nekte root-pålogging (`PermitRootLogin no` i `/etc/ssh/sshd_config`). Bruk alltid sudo fra en vanlig brukerkonto.

**Hva betyr 'd' fremst i `ls -l` output?**
Det første tegnet angir filtypen: `-` = vanlig fil, `d` = katalog (directory), `l` = symbolsk lenke, `b` = blokkenhetsf il, `c` = tegnenhetsfil.

**Hva er forskjellen mellom `/bin` og `/usr/bin`?**
`/bin` inneholder grunnleggende systemkommandoer som må være tilgjengelige tidlig i oppstartsprosessen og ved systemgjenoppretting (f.eks. `ls`, `cp`, `bash`). `/usr/bin` inneholder programmer installert av pakkebehandleren. På moderne Linux er `/bin` ofte en symbolsk lenke til `/usr/bin`.

**Hva er `journalctl` og hvorfor er det bedre enn å lese loggfiler direkte?**
`journalctl` er kommandoen for å lese loggene fra systemd's journald. Fordeler: strukturerte logger med metadata, enkel filtrering per tjeneste og tidsrom, binært format som er mer effektivt enn tekstfiler. For eldre systemer brukes fortsatt tekstfiler i `/var/log/`.

---

## Quiz

<details><summary>Spørsmål 1: Hva betyr tillatelseskoden `chmod 755`?</summary>

**Svar:** Eier får rwx (7 = 4+2+1), gruppe får r-x (5 = 4+0+1), andre får r-x (5 = 4+0+1). Eieren kan lese, skrive og kjøre; gruppe og andre kan lese og kjøre, men ikke skrive.

</details>

<details><summary>Spørsmål 2: Hva lagres i /etc/shadow?</summary>

**Svar:** Krypterte (hashede) passord for alle brukere. Filen er kun lesbar av root, i motsetning til `/etc/passwd` som er lesbar for alle.

</details>

<details><summary>Spørsmål 3: Hva er forskjellen mellom `useradd` og `usermod`?</summary>

**Svar:** `useradd` oppretter en ny brukerkonto. `usermod` endrer innstillingene på en eksisterende konto (f.eks. legger til gruppemedlemskap, endrer shell eller låser kontoen).

</details>

<details><summary>Spørsmål 4: Hva gjør sticky bit på en mappe?</summary>

**Svar:** Sticky bit hindrer at brukere kan slette filer i mappen de ikke selv eier, selv om de har skrivetillatelse til mappen. Brukes typisk på `/tmp` og delte mapper.

</details>

<details><summary>Spørsmål 5: Hva er katalogen /etc brukt til?</summary>

**Svar:** `/etc` inneholder konfigurasjonsfiler for systemet og installerte tjenester, bl.a. `/etc/passwd` (brukerkontoer), `/etc/group` (grupper), `/etc/hosts` (vertsnavn) og `/etc/ssh/sshd_config` (SSH-konfigurasjon).

</details>

---

## Flashcards

/ :: Rotkatalogen i Linux — toppen av hele filsystemet
/etc :: Katalog med konfigurasjonsfiler for system og tjenester
/home :: Katalog med hjemmemapper for vanlige brukere
/var/log :: Katalog med loggfiler fra systemet og tjenester
chmod :: Linux-kommando for å endre filrettigheter (rwx)
chown :: Linux-kommando for å endre eier og/eller gruppe for en fil
sudo :: Kommando som lar en vanlig bruker kjøre en kommando med root-rettigheter
root :: Superbrukeren i Linux (UID 0) med ubegrenset tilgang til systemet
rwx :: Les (r=4), skriv (w=2), kjør (x=1) — de tre tillatelsene i Linux
chmod 755 :: eier: rwx, gruppe: r-x, andre: r-x — typisk for websider og mapper
chmod 644 :: eier: rw-, gruppe: r--, andre: r-- — typisk for vanlige filer
sticky bit :: Forhindrer brukere fra å slette filer i en delt mappe de ikke eier
/etc/passwd :: Fil med brukerkontoer — inneholder brukernavn, UID, GID, hjemmemappe og shell
/etc/shadow :: Fil med krypterte passord — kun lesbar av root
/etc/group :: Fil med gruppedefinisjoner og gruppemedlemskap
useradd -m :: Opprett ny Linux-bruker med hjemmemappe
usermod -aG :: Legg bruker til i tilleggsgruppe uten å fjerne eksisterende gruppemedlemskap
visudo :: Sikker måte å redigere /etc/sudoers på — kontrollerer syntaks før lagring
SUID :: Set User ID — spesiell tillatelsesbit som gjør at en kjørbar fil kjøres med filens eiers rettigheter
SGID :: Set Group ID — på mappe: nye filer arver mappens gruppe i stedet for oppretterens primærgruppe
journalctl :: Kommando for å lese systemlogger fra systemd journald; støtter filtrering per tjeneste og tid
/var/log/auth.log :: Linux-loggfil for autentiseringshendelser, sudo-bruk og SSH-pålogginger
UID :: User ID — numerisk identifikator for en Linux-bruker (root=0, systembrukere 1–999, vanlige brukere 1000+)
GID :: Group ID — numerisk identifikator for en Linux-gruppe

---

## Ressurser

- [Ubuntu Community Wiki: Filrettigheter](https://help.ubuntu.com/community/FilePermissions)
- [Ubuntu Community Wiki: POSIX ACL](https://help.ubuntu.com/community/FilePermissionsACLs)
- [Ubuntu Server: Brukerhåndtering](https://documentation.ubuntu.com/server/how-to/security/user-management/)
