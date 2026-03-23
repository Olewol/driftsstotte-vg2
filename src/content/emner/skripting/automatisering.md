---
title: "Automatisering – planlagte oppgaver og IaC"
emne: skripting
kompetansemaal:
  - km-09
kilder:
  - ndla
  - https://learn.microsoft.com/nb-no/powershell/scripting/overview
tags: []
flashcards: true
public: true
notebooklm: true
---

## Introduksjon

Å skrive et skript er bare halve jobben. Det andre halvparten er å sørge for at skriptet faktisk kjøres — til riktig tid, på riktig maskin, uten at noen trenger å tenke på det. Det er her **automatisering** virkelig viser sin verdi.

I denne artikkelen lærer vi to grunnleggende mekanismer for å planlegge og kjøre skript automatisk: **Windows Task Scheduler** for Windows og **cron** for Linux. Vi ser også på **Infrastructure as Code (IaC)** — neste steg etter skripting, der hele IT-infrastrukturen beskrives i kode.

Automatisering bygger direkte på ferdighetene fra [[bash-grunnleggende]] og [[powershell-grunnleggende]]. I større driftsmiljøer henger automatisering tett sammen med [[backup-og-gjenoppretting]], [[serverroller]] og [[skytjenester]].

---

## Teori

### Hva er automatisering i IT?

Automatisering i IT betyr å erstatte manuelle, repeterende oppgaver med systemer som utfører dem av seg selv. En systemadministrator som manuelt logger inn på 50 servere for å installere oppdateringer bruker timevis. Et skript som kjøres automatisk via Task Scheduler eller cron gjør det samme på minutter — uten menneskelig intervensjon.

Typiske oppgaver som automatiseres i drift:

- **Backup** — Kopier data til sikker lagring hver natt.
- **Oppdateringer** — Installer sikkerhetsoppdateringer ukentlig.
- **Loggrotasjon** — Arkiver og slett gamle loggfiler.
- **Overvåking** — Sjekk tjenestestatus hvert 5. minutt og send varsel ved feil.
- **Rapportering** — Generer og send brukerlister eller systemstatus-rapporter.

Automatisering reduserer menneskelige feil, frigjør tid og gjør driften mer forutsigbar.

---

### Windows Task Scheduler

Task Scheduler (Oppgaveplanlegger) er Windows' innebygde system for å planlegge og kjøre programmer og skript automatisk.

#### Konsepter

En **oppgave** (task) i Task Scheduler består av tre deler:

1. **Trigger** — Når skal oppgaven kjøres? (tidspunkt, systemhendelse, pålogging, osv.)
2. **Handling** (Action) — Hva skal kjøres? (program, skript, e-post)
3. **Betingelser** — Tilleggskrav (f.eks. "bare hvis maskinen er på strøm")

#### GUI — opprett oppgave grafisk

1. Åpne **Task Scheduler** (søk i startmenyen).
2. Klikk **Create Basic Task** i høyre panel.
3. Gi oppgaven et navn og beskrivelse.
4. Velg trigger: **Daily**, sett klokkeslett til `02:00`.
5. Velg handling: **Start a program**.
6. Bla til skriptet ditt, f.eks. `C:\Scripts\backup.ps1`.
   - Program: `powershell.exe`
   - Argumenter: `-NonInteractive -File "C:\Scripts\backup.ps1"`
7. Klikk **Finish**.

#### Kommandolinje med `schtasks`

`schtasks` er kommandolinjeverktøyet for Task Scheduler. Det er nyttig for automatisk oppsett og scripting av oppgaver.

Grunnleggende kommandoer:

| Kommando | Beskrivelse |
|---|---|
| `schtasks /create` | Opprett ny oppgave |
| `schtasks /query` | List oppgaver |
| `schtasks /run` | Kjør oppgave umiddelbart |
| `schtasks /delete` | Slett oppgave |
| `schtasks /change` | Endre eksisterende oppgave |

**Eksempel — opprett daglig backup-oppgave kl. 02:00:**

```cmd
schtasks /create ^
  /tn "DagligBackup" ^
  /tr "powershell.exe -NonInteractive -File C:\Scripts\backup.ps1" ^
  /sc DAILY ^
  /st 02:00 ^
  /ru SYSTEM ^
  /f
```

**Parameter-forklaring:**

| Parameter | Forklaring |
|---|---|
| `/tn "DagligBackup"` | Task Name — navn på oppgaven |
| `/tr "powershell.exe ..."` | Task Run — programmet/skriptet som skal kjøres |
| `/sc DAILY` | Schedule — kjørefrekvens (DAILY, WEEKLY, MONTHLY, ONCE, osv.) |
| `/st 02:00` | Start Time — klokkeslettet for kjøring |
| `/ru SYSTEM` | Run User — brukerkontoen som oppgaven kjøres under |
| `/f` | Force — overskriv uten bekreftelse hvis oppgaven allerede finnes |

**Verifiser oppgaven:**

```cmd
schtasks /query /tn "DagligBackup" /fo LIST /v
```

**Kjør oppgaven manuelt for testing:**

```cmd
schtasks /run /tn "DagligBackup"
```

---

### Linux Cron

**Cron** er Linux' daemon for å kjøre planlagte oppgaver. Oppgavene defineres i en **crontab**-fil (cron table) med en spesifikk syntaks.

#### Crontab-syntaks

En crontab-linje består av fem tidsfelt etterfulgt av kommandoen:

```
# min  time  dag-i-mnd  måned  dag-i-uke  kommando
  *    *     *          *      *          /sti/til/skript.sh
```

**Feltene:**

| Felt | Verdiområde | Beskrivelse |
|---|---|---|
| Minutt | 0–59 | Minutt i timen |
| Time | 0–23 | Time på dagen (24-timers) |
| Dag i måned | 1–31 | Dag i måneden |
| Måned | 1–12 | Måneden |
| Dag i uke | 0–7 | Ukedag (0 og 7 er begge søndag) |

**Spesialverdier:**

| Verdi | Betydning |
|---|---|
| `*` | Alle gyldige verdier |
| `*/2` | Hvert andre (f.eks. hvert andre minutt) |
| `1,3,5` | Spesifikke verdier (mandag, onsdag, fredag) |
| `1-5` | Område (mandag til fredag) |

**Spesialstrenger (snarveier):**

| Streng | Tilsvarer |
|---|---|
| `@reboot` | Ved oppstart av systemet |
| `@daily` | `0 0 * * *` — midnatt hver dag |
| `@weekly` | `0 0 * * 0` — søndag midnatt |
| `@monthly` | `0 0 1 * *` — første dag i måneden |
| `@hourly` | `0 * * * *` — hvert hele time |

#### Administrere crontab

```bash
# Rediger din crontab (åpner i standard tekstbehandler)
crontab -e

# List gjeldende crontab
crontab -l

# Slett all din crontab
crontab -r
```

#### Praktiske cron-eksempler

```bash
# Daglig backup kl. 02:00
0 2 * * * /home/bruker/backup.sh

# Ukentlig rapport hver søndag kl. 04:05
5 4 * * 0 /opt/ukentlig-rapport.sh

# Loggrotasjon første dag i måneden kl. 00:30
30 0 1 * * /usr/local/bin/roter-logger.sh

# Sjekk tjenester hvert 5. minutt
*/5 * * * * /home/bruker/sjekk-tjenester.sh

# Restart webserver hver natt kl. 03:00 (mandag–fredag)
0 3 * * 1-5 systemctl restart nginx

# Kjør ved systemoppstart
@reboot /home/bruker/start-agent.sh
```

**Viktig:** Skript som kjøres av cron har et begrenset miljø (PATH er kortere enn i terminalen din). Bruk alltid **absolutte stier** til programmer og filer i cron-oppgaver:

```bash
# Feil — cron finner kanskje ikke 'backup.sh'
* * * * * backup.sh

# Riktig — eksplisitt sti
0 2 * * * /home/bruker/backup.sh

# Riktig — også absolutt sti til selve kommandoen
0 2 * * * /bin/bash /home/bruker/backup.sh
```

**Logg cron-utdata:**

```bash
# Send utdata til loggfil (overskriver)
0 2 * * * /home/bruker/backup.sh > /var/log/backup.log 2>&1

# Send utdata til loggfil (legger til)
0 2 * * * /home/bruker/backup.sh >> /var/log/backup.log 2>&1
```

`2>&1` videresender stderr (feilmeldinger) til samme fil som stdout.

---

### Infrastructure as Code (IaC) — introduksjon

Skripting er kraftig, men har begrensninger: et skript beskriver *handlinger* (gjør dette, så det), ikke *tilstander* (systemet skal se slik ut). Infrastructure as Code er neste steg i automatiseringsreisen.

**Definisjon:** IaC er praksis med å definere og provisjonere IT-infrastruktur gjennom maskinlesbare konfigurasjonsfiler i stedet for manuelle prosesser eller interaktive konfigurasjonsverktøy.

#### Fordeler med IaC

| Fordel | Forklaring |
|---|---|
| **Konsistens** | Alle miljøer (utvikling, test, produksjon) er identisk konfigurert |
| **Repeterbarhet** | Samme miljø kan settes opp igjen fra bunnen av på minutter |
| **Versjonskontroll** | Infrastruktur-kode lagres i Git — historikk, rollback, code review |
| **Dokumentasjon** | Koden dokumenterer seg selv — hva som kjører og hvorfor |
| **Skalering** | Én konfigurasjonsfil kan provisjonere 1 eller 1000 servere |

#### Fra skripting til IaC

```
Manuell drift → Skripting (Bash/PowerShell) → IaC (Ansible/Terraform)
```

- **Skripting** er *imperativt*: "Opprett mappe, kopier fil, start tjeneste."
- **IaC** er *deklarativt*: "Mappen skal eksistere, filen skal være der, tjenesten skal kjøre." Verktøyet finner selv ut hva som må gjøres.

#### Sentrale IaC-verktøy

**Ansible** (Red Hat)
- Agentfri: kommuniserer via SSH, ingen programvare å installere på målmaskiner.
- Konfigurasjon skrives i YAML-filer kalt **playbooks**.
- Egnet for konfigurasjonsstyring og deploying av applikasjoner.

```yaml
# Eksempel på Ansible-playbook (YAML)
- name: Installer og start nginx
  hosts: webservere
  tasks:
    - name: Installer nginx
      apt:
        name: nginx
        state: present
    - name: Start nginx
      service:
        name: nginx
        state: started
```

**Terraform** (HashiCorp)
- Sky-agnostisk: fungerer med AWS, Azure, Google Cloud og mange andre.
- Konfigurasjon skrives i **HCL** (HashiCorp Configuration Language).
- Egnet for å provisjonere skyinfrastruktur (servere, nettverk, databaser).

```hcl
# Eksempel på Terraform-konfigurasjon (HCL)
resource "azurerm_virtual_machine" "webserver" {
  name     = "webserver-01"
  location = "norwayeast"
  size     = "Standard_B1s"
}
```

**PowerShell DSC** (Desired State Configuration)
- Microsofts eget IaC-verktøy, integrert med Windows og Azure.
- Beskriver ønsket tilstand for Windows-konfigurasjoner.

IaC er et avansert emne som bygger direkte på skripting-kunnskapen fra dette emnet. Bash og PowerShell er ofte brukt *inne i* IaC-verktøy for spesifikke oppgaver.

#### Idempotens — et sentralt prinsipp

Et viktig begrep i automatisering og IaC er **idempotens**: en operasjon er idempotent hvis den kan kjøres mange ganger uten at resultatet endrer seg etter den første vellykkede kjøringen. Ansible og Terraform er idempotente — de sjekker alltid gjeldende tilstand mot ønsket tilstand og gjør bare det som faktisk trengs. Et enkelt Bash-skript som kjøres to ganger kan derimot opprette duplikater eller overskrive data. Design egne skript med idempotens i tankene (f.eks. sjekk om mappen allerede finnes før du oppretter den).

#### Sikker håndtering av hemmeligheter i automatiserte skript

Skript som kjøres automatisk trenger ofte passord, API-nøkler eller sertifikater. **Lagre aldri hemmeligheter direkte i skriptkoden.** Gode alternativer:

- **Miljøvariabler** — Les hemmeligheten fra miljøet i stedet for å hardkode den.
- **Windows Credential Manager / Secret Store** — PowerShell-modul `Microsoft.PowerShell.SecretManagement`.
- **Vault-løsninger** — HashiCorp Vault eller Azure Key Vault for produksjonsmiljøer.

Dette er spesielt viktig når skript lagres i [[dokumentasjon-og-planlegging]] eller versjonskontrollsystemer som Git.

---

## Eksempel / lab

### Lab: Sett opp automatisk backup med Task Scheduler

Vi setter opp en Windows-oppgave som kjører PowerShell-backup-skriptet (fra [[powershell-grunnleggende]]) daglig kl. 02:00.

**Forutsetning:** Backup-skriptet ligger på `C:\Scripts\backup.ps1`.

**Steg 1 — Opprett scriptmappen og skriptet:**

```powershell
# Kjøres i PowerShell som administrator
New-Item -ItemType Directory -Path "C:\Scripts" -Force

$skriptinnhold = @'
# backup.ps1
$kilde = "C:\Users\$env:USERNAME\Documents"
$mal = "C:\Backup\$(Get-Date -Format 'yyyy-MM-dd')"
New-Item -ItemType Directory -Path $mal -Force | Out-Null
Copy-Item -Path $kilde -Destination $mal -Recurse -Force
Write-Host "Backup fullfort: $mal"
'@

Set-Content -Path "C:\Scripts\backup.ps1" -Value $skriptinnhold -Encoding UTF8
```

**Steg 2 — Opprett Task Scheduler-oppgaven:**

```powershell
# Definer handling (hva som skal kjøres)
$handling = New-ScheduledTaskAction `
    -Execute "powershell.exe" `
    -Argument "-NonInteractive -WindowStyle Hidden -File C:\Scripts\backup.ps1"

# Definer trigger (når det skal kjøres)
$trigger = New-ScheduledTaskTrigger `
    -Daily `
    -At "02:00"

# Definer innstillinger
$innstillinger = New-ScheduledTaskSettingsSet `
    -ExecutionTimeLimit (New-TimeSpan -Hours 1) `
    -RestartCount 3 `
    -RestartInterval (New-TimeSpan -Minutes 5)

# Registrer oppgaven
Register-ScheduledTask `
    -TaskName "DagligBackup" `
    -Action $handling `
    -Trigger $trigger `
    -Settings $innstillinger `
    -RunLevel Highest `
    -Force
```

**Linje-for-linje forklaring:**

| Kommando | Forklaring |
|---|---|
| `New-ScheduledTaskAction` | Definerer hva som skal kjøres — her PowerShell med backup-skriptet |
| `-NonInteractive` | Skriptet skal ikke vise brukergrensesnitt eller vente på input |
| `-WindowStyle Hidden` | Skjul PowerShell-vinduet under kjøring |
| `New-ScheduledTaskTrigger -Daily -At "02:00"` | Oppgaven kjøres daglig kl. 02:00 |
| `New-ScheduledTaskSettingsSet` | Ekstra innstillinger: tidsbegrensning og automatisk restart ved feil |
| `Register-ScheduledTask` | Registrerer (lagrer) oppgaven i Task Scheduler |
| `-RunLevel Highest` | Kjør med forhøyede rettigheter (administrator) |

**Steg 3 — Verifiser og test:**

```powershell
# Se oppgaven
Get-ScheduledTask -TaskName "DagligBackup"

# Kjør oppgaven manuelt for å teste
Start-ScheduledTask -TaskName "DagligBackup"

# Sjekk om backup-mappen ble opprettet
Get-ChildItem "C:\Backup"
```

**Tilsvarende med schtasks (kommandolinje):**

```cmd
schtasks /create /tn "DagligBackup" /tr "powershell.exe -NonInteractive -File C:\Scripts\backup.ps1" /sc DAILY /st 02:00 /ru SYSTEM /f
```

---

## Study guide

### Automatisering – planlagte oppgaver og IaC

Automatisering handler om å la systemer utføre oppgaver av seg selv — til riktig tid, med riktige rettigheter, uten menneskelig inngripen.

**To plattformer for planlegging:**

| | Windows | Linux |
|---|---|---|
| Verktøy | Task Scheduler / `schtasks` | cron / `crontab -e` |
| Syntaks | GUI eller kommandolinje | 5 tidsfelt + kommando |
| Eksempel | `schtasks /create /sc DAILY /st 02:00` | `0 2 * * * /sti/til/skript.sh` |

**Cron-syntaks huskeregel** (5 felt): `minutt time dag-i-mnd måned dag-i-uke`
- `*` = alle verdier, `*/5` = hvert femte, `1-5` = mandag–fredag, `@daily` = snarvei for midnatt hver dag.
- Alltid absolutte stier i cron — PATH-miljøet er minimalt.
- Logg alltid output: `>> /var/log/skript.log 2>&1`

**Task Scheduler — tre deler i en oppgave:**
1. **Trigger** — når (tid, hendelse, pålogging)
2. **Handling** — hva (program, skript)
3. **Betingelser** — tilleggskrav (strøm, nettverk)

**Fra skripting til IaC:**
- Skripting er *imperativt*: "gjør A, B, C i rekkefølge."
- IaC er *deklarativt*: "systemet skal se slik ut — verktøyet ordner resten."
- Ansible (YAML-playbooks via SSH) → konfigurasjonsstyring
- Terraform (HCL) → skyinfrastruktur
- PowerShell DSC → Windows-tilstandsstyring

**Nøkkelprinsipper:** idempotens (trygt å kjøre flere ganger), sikker hemmelighets-håndtering (aldri passord i kode), versjonskontroll av skript.

Koble til [[backup-og-gjenoppretting]] for eksempler på hva som automatiseres, og [[skytjenester]] for sky-basert IaC.

---

## FAQ

**Hva skjer hvis en cron-jobb feiler — får jeg beskjed?**
Som standard sender cron feilmeldingen på e-post til systembrukeren. I praksis er det bedre å logge eksplisitt: `0 2 * * * /sti/skript.sh >> /var/log/backup.log 2>&1`. Da kan du sjekke loggen manuelt eller med et overvåkingsverktøy.

**Kan jeg kjøre Task Scheduler-oppgaver uten å være logget inn?**
Ja, hvis du setter brukerkontoen til `SYSTEM` eller en servicekonto og krysser av for "Run whether user is logged on or not". Da kjøres oppgaven i bakgrunnen uavhengig av påloggingsstatus.

**Hvordan tester jeg en cron-jobb uten å vente til riktig tidspunkt?**
Kjør skriptet manuelt direkte i terminalen med samme bruker som cron ville brukt: `sudo -u www-data /sti/til/skript.sh`. Dette simulerer cron-miljøet godt. For Task Scheduler: `schtasks /run /tn "OppgaveNavn"`.

**Hva er idempotens og hvorfor er det viktig i automatisering?**
Idempotens betyr at en operasjon kan kjøres mange ganger uten at resultatet endrer seg etter første vellykkede kjøring. Et skript som alltid sjekker `if [ ! -d "$MAPPE" ]; then mkdir "$MAPPE"; fi` er idempotent — det oppretter mappen kun hvis den ikke finnes. Dette er avgjørende for pålitelig automatisering.

**Hva er forskjellen på Ansible og Terraform?**
Ansible brukes primært til konfigurasjonsstyring — installere pakker, starte tjenester, redigere konfigurasjonsfiler på eksisterende servere. Terraform brukes primært til å *provisjonere* infrastruktur — opprette VM-er, nettverk og databaser i skyen. I praksis brukes de ofte sammen: Terraform oppretter infrastrukturen, Ansible konfigurerer den.

**Kan et PowerShell-skript i Task Scheduler kjøre uten å åpne et vindu?**
Ja, legg til `-WindowStyle Hidden` i argumentene: `-NonInteractive -WindowStyle Hidden -File C:\Scripts\skript.ps1`. Da kjøres skriptet i bakgrunnen uten synlig vindu.

**Hvorfor bør hemmeligheter aldri hardkodes i skript?**
Skript lagres gjerne i versjonskontroll (Git), loggfiler eller deles med kolleger. Hardkodede passord eller API-nøkler eksponeres da ukontrollert. Bruk miljøvariabler, Windows Credential Manager eller en dedikert vault-løsning for sensitiv informasjon.

---

## Quiz

<details><summary>Spørsmål 1: Hva er de tre hoveddelene i en Task Scheduler-oppgave?</summary>

**Svar:** En oppgave består av (1) **Trigger** — når oppgaven skal kjøres, (2) **Handling (Action)** — hva som skal kjøres, og (3) **Betingelser** — eventuelle tilleggskrav som må oppfylles.

</details>

<details><summary>Spørsmål 2: Hva betyr `*/5` i crontab-syntaksen?</summary>

**Svar:** `*/5` betyr "hvert femte" av den aktuelle tidsenheten. I minutt-feltet betyr `*/5` hvert 5. minutt (0, 5, 10, 15, ...). I time-feltet ville det betydd hver 5. time.

</details>

<details><summary>Spørsmål 3: Hvorfor skal man alltid bruke absolutte stier i cron-oppgaver?</summary>

**Svar:** Cron kjører med et minimalt miljø der `PATH`-variabelen er mye kortere enn i et interaktivt terminal. Kommandoer som fungerer normalt i terminalen kan derfor ikke finnes av cron. Med absolutte stier (f.eks. `/bin/bash` og `/home/bruker/backup.sh`) er det ingen tvil om hvilken fil som menes.

</details>

<details><summary>Spørsmål 4: Hva er den grunnleggende forskjellen på imperativ skripting og deklarativ IaC?</summary>

**Svar:** Imperativ skripting beskriver *handlingene* som skal utføres i rekkefølge ("gjør A, så B, så C"). Deklarativ IaC beskriver *ønsket sluttilstand* ("systemet skal se slik ut"), og verktøyet bestemmer selv hvilke handlinger som trengs for å nå den tilstanden.

</details>

<details><summary>Spørsmål 5: Hva betyr `2>&1` på slutten av en cron-kommando?</summary>

**Svar:** Det videresender **stderr** (filbeskriver 2) til **stdout** (filbeskriver 1). Når dette kombineres med `>> /var/log/backup.log`, betyr det at både vanlig utdata og feilmeldinger skrives til samme loggfil.

</details>

---

## Flashcards

Crontab :: Konfigurasjonsfil i Linux som definerer planlagte oppgaver for cron-daemonen
Cron-syntaks :: Fem felt (min time dag mnd ukedag) etterfulgt av kommandoen som skal kjøres
`@reboot` :: Cron-spesialstreng som kjører kommandoen ved systemoppstart
`crontab -e` :: Kommando for å redigere brukerens crontab i standardeditoren
`schtasks /create` :: Windows-kommandolinjeverktøy for å opprette planlagte oppgaver
Task Scheduler-trigger :: Betingelsen som starter en oppgave (tid, hendelse, pålogging osv.)
Infrastructure as Code (IaC) :: Praksis med å definere IT-infrastruktur i maskinlesbare konfigurasjonsfiler
Ansible :: Agentfritt IaC-verktøy (Red Hat) som bruker YAML-playbooks via SSH
Terraform :: Sky-agnostisk IaC-verktøy (HashiCorp) som bruker HCL for å provisjonere infrastruktur
Deklarativ konfigurasjon :: Beskriver ønsket sluttilstand — verktøyet bestemmer selv hvilke steg som trengs
`2>&1` :: Shell-omdirigering som sender stderr til samme sted som stdout
`Register-ScheduledTask` :: PowerShell-cmdlet som registrerer en planlagt oppgave i Windows Task Scheduler
Idempotens :: Prinsipp i automatisering der en operasjon kan kjøres mange ganger uten at resultatet endrer seg etter første vellykkede kjøring
Planlagte oppgaver :: Bruk av Task Scheduler (Windows) eller cron (Linux) for å kjøre skript automatisk på gitte tidspunkter eller hendelser
Imperativ skripting :: Skript som beskriver handlingene som skal utføres steg for steg ("gjør A, så B")
Deklarativ IaC :: Konfigurasjon som beskriver ønsket sluttilstand, ikke fremgangsmåten for å nå den

---

## Ressurser

- [Microsoft Learn – Task Scheduler](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page)
- [Microsoft Learn – schtasks kommandoreferanse](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/schtasks)
- [man7.org – crontab(5)](https://man7.org/linux/man-pages/man5/crontab.5.html)
- [IBM – Hva er Infrastructure as Code?](https://www.ibm.com/topics/infrastructure-as-code)
- [Microsoft Learn – PowerShell på norsk](https://learn.microsoft.com/nb-no/powershell/scripting/overview)
