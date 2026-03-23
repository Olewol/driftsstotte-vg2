---
title: "PowerShell – grunnleggende skripting"
emne: skripting
kompetansemaal:
  - km-09
kilder:
  - ndla
tags: []
flashcards: true
public: true
---

## Introduksjon

PowerShell er Microsofts svar på Bash — et kraftig skallspråk og skriptmiljø innebygd i Windows. Det skiller seg fundamentalt fra Bash ved at det opererer med **.NET-objekter** i stedet for ren tekst. Det betyr at når du henter informasjon om en tjeneste, får du tilbake et objekt med egenskaper som `Name`, `Status` og `StartType` — ikke bare en tekstlinje du må tolke selv.

Siden PowerShell 7 er det også tilgjengelig på Linux og macOS, men det er primært på Windows det er uunnværlig: Active Directory, Azure, Task Scheduler og Windows-administrasjon generelt styres effektivt via PowerShell.

---

## Teori

### Hva er PowerShell?

PowerShell installeres som standard på alle moderne Windows-versjoner. Det finnes to hovedversjoner:

- **Windows PowerShell 5.1** — Innebygd i Windows, kjører kun på Windows.
- **PowerShell 7+** — Åpen kildekode, cross-platform, anbefalt for nye prosjekter.

For å sjekke hvilken versjon du har:

```powershell
$PSVersionTable
```

For å sjekke og sette execution policy (sikkerhetspolitikk for skript):

```powershell
# Sjekk gjeldende policy
Get-ExecutionPolicy

# Tillat lokale skript og signerte skript fra internett (anbefalt for drift)
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

`Restricted` er standard på Windows-klienter og blokkerer alle skript. `RemoteSigned` er et godt kompromiss for driftsmiljøer.

### Cmdlets — verb-substantiv-konvensjonen

Det grunnleggende byggeklossen i PowerShell er **cmdlet** (uttales "command-let"). Alle cmdlets følger mønsteret `Verb-Substantiv`:

| Cmdlet | Beskrivelse |
|---|---|
| `Get-Service` | Hent informasjon om tjenester |
| `Start-Service` | Start en tjeneste |
| `Stop-Service` | Stopp en tjeneste |
| `Get-Process` | List kjørende prosesser |
| `Stop-Process` | Avslutt en prosess |
| `Get-ChildItem` | List filer og mapper (tilsvarer `ls`/`dir`) |
| `Copy-Item` | Kopier fil eller mappe |
| `Move-Item` | Flytt fil eller mappe |
| `Remove-Item` | Slett fil eller mappe |
| `New-Item` | Opprett ny fil eller mappe |
| `Get-Content` | Les innholdet i en fil |
| `Set-Content` | Skriv innhold til en fil |
| `Get-Help` | Vis hjelp for en cmdlet |
| `Get-Command` | Søk etter cmdlets |
| `Get-Member` | Vis egenskaper og metoder for et objekt |

Godkjente verb kan listes med `Get-Verb`. Å følge konvensjonen gjør skript lettere å lese og forstå.

### Pipeline og objekter

Det som gjør PowerShell unikt er at pipelinen (`|`) overfører **objekter**, ikke tekst. Hvert objekt har egenskaper og metoder du kan jobbe med direkte.

```powershell
# Hent alle tjenester som er stoppet
Get-Service | Where-Object Status -EQ "Stopped"

# Velg bare bestemte kolonner
Get-Service | Select-Object Name, Status, StartType

# Sorter etter navn
Get-Service | Sort-Object Name

# Tell antall
Get-Service | Where-Object Status -EQ "Running" | Measure-Object
```

Pipelinen evalueres fra venstre til høyre. En god tommelfingerregel er **"filter left"** — filtrer så tidlig som mulig for å unngå å sende unødvendig mange objekter gjennom pipelinen.

For å undersøke hva slags objekt du jobber med:

```powershell
Get-Service | Get-Member
```

Dette viser alle egenskaper (`Property`) og metoder (`Method`) tilgjengelig på objektet.

### Variabler

Variabler i PowerShell starter alltid med `$`:

```powershell
$navn = "Ola Nordmann"
$alder = 25
$aktiv = $true
```

**Strengtyper:**
- Enkelthermetegn: `'Hei $navn'` — tolkes bokstavelig, ingen variabelekspansjon.
- Dobbelthermetegn: `"Hei $navn"` — variabler ekspanderes til sin verdi.
- For komplekse uttrykk inne i streng: `"Det er $($brukere.Count) brukere"`.

**Nyttige automatiske variabler:**

| Variabel | Innhold |
|---|---|
| `$_` | Gjeldende objekt i pipeline |
| `$PSVersionTable` | Info om PowerShell-versjonen |
| `$env:COMPUTERNAME` | Maskinnavnet |
| `$env:USERNAME` | Innlogget bruker |
| `$true` / `$false` | Boolske verdier |
| `$null` | Representerer ingen verdi |

### Arrays og hashtables

**Array** (liste med verdier):

```powershell
$servere = @("server01", "server02", "server03")
$servere[0]          # Første element: "server01"
$servere.Count       # Antall elementer: 3

foreach ($server in $servere) {
    Write-Host "Kobler til $server"
}
```

**Hashtable** (nøkkel-verdi-par, tilsvarer dictionary):

```powershell
$bruker = @{
    Navn     = "Kari Olsen"
    Alder    = 30
    Avdeling = "IT"
}

$bruker["Navn"]      # "Kari Olsen"
$bruker.Avdeling     # "IT"
```

### Funksjoner

Funksjoner i PowerShell bør følge verb-substantiv-konvensjonen og bruke en `param`-blokk for parametere:

```powershell
function Get-BrukerInfo {
    param(
        [Parameter(Mandatory)]
        [string]$Brukernavn
    )

    $bruker = Get-LocalUser -Name $Brukernavn
    return $bruker
}

Get-BrukerInfo -Brukernavn "ola.nordmann"
```

- `[Parameter(Mandatory)]` gjør parameteren obligatorisk — PowerShell spør brukeren om den mangler.
- `[string]` er typeannotering som sikrer at verdien er en streng.
- `[CmdletBinding()]` øverst i funksjonen legger til støtte for `-Verbose`, `-Debug` og andre felles parametere.

### Moduler

Moduler er samlinger av cmdlets som kan lastes inn ved behov:

```powershell
# Importer en modul
Import-Module ActiveDirectory

# List tilgjengelige cmdlets i modulen
Get-Command -Module ActiveDirectory

# Installer modul fra PowerShell Gallery
Install-Module -Name PSReadLine -Scope CurrentUser
```

Mange Windows-funksjoner (Active Directory, Exchange, Azure) leveres som PowerShell-moduler.

### Feilhåndtering

PowerShell bruker `try/catch` for strukturert feilhåndtering:

```powershell
try {
    Get-Item "C:\finnesikke.txt" -ErrorAction Stop
}
catch {
    Write-Host "Feil oppstod: $($_.Exception.Message)" -ForegroundColor Red
}
```

`-ErrorAction Stop` er nødvendig for at feilen skal fanges av `catch`. Standard feiloppførsel i PowerShell er å fortsette.

---

## Eksempel / lab

### Lab: List lokale brukere og lagre til CSV

Vi skal skrive et skript som henter alle lokale brukerkontoer, velger relevante egenskaper og eksporterer til en CSV-fil.

```powershell
# brukerliste.ps1 — Hent og lagre lokale brukere
# Krever: Windows (lokale brukere finnes ikke på Linux/macOS)

# ─── Hent brukere ────────────────────────────────────────────
$brukere = Get-LocalUser | Select-Object Name, Enabled, LastLogon

# ─── Eksporter til CSV ───────────────────────────────────────
$brukere | Export-Csv -Path "C:\brukerliste.csv" -NoTypeInformation -Encoding UTF8

# ─── Bekreftelse ─────────────────────────────────────────────
Write-Host "Lagret $($brukere.Count) brukere til brukerliste.csv"
```

**Linje-for-linje forklaring:**

| Linje | Forklaring |
|---|---|
| `Get-LocalUser` | Henter alle lokale brukerkontoer på maskinen som .NET-objekter |
| `Select-Object Name, Enabled, LastLogon` | Velger kun tre egenskaper fra hvert brukerobjekt — reduserer datamengden |
| `$brukere = ...` | Lagrer listen med brukerobjekter i variabelen `$brukere` |
| `Export-Csv -Path "C:\brukerliste.csv"` | Skriver objektene til en CSV-fil på angitt sti |
| `-NoTypeInformation` | Fjerner den første linjen i CSV-filen som ellers inneholder .NET-typeinfo |
| `-Encoding UTF8` | Sikrer at norske tegn (æ, ø, å) lagres korrekt |
| `$($brukere.Count)` | Subexpression som henter antall elementer i arrayen og setter det inn i strengen |
| `Write-Host` | Skriver ut melding til konsollet (ikke til pipeline) |

**Kjør skriptet:**

```powershell
# Åpne PowerShell som administrator
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# Naviger til mappen der skriptet ligger
cd C:\Scripts

# Kjør skriptet
.\brukerliste.ps1

# Se resultatet
Import-Csv "C:\brukerliste.csv" | Format-Table
```

**Utvidet versjon — legg til feilhåndtering:**

```powershell
# brukerliste-utvidet.ps1

$utFil = "C:\brukerliste.csv"

try {
    $brukere = Get-LocalUser | Select-Object Name, Enabled, LastLogon
    $brukere | Export-Csv -Path $utFil -NoTypeInformation -Encoding UTF8
    Write-Host "Lagret $($brukere.Count) brukere til $utFil" -ForegroundColor Green
}
catch {
    Write-Host "FEIL: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}
```

---

## Quiz

<details><summary>Spørsmål 1: Hva er den fundamentale forskjellen mellom PowerShell-pipeline og Bash-pipeline?</summary>

**Svar:** PowerShell sender **.NET-objekter** gjennom pipelinen — du jobber med strukturerte data med egenskaper og metoder. Bash sender **tekst** (strenger), som du må tolke og parse selv med verktøy som `grep`, `awk` og `cut`.

</details>

<details><summary>Spørsmål 2: Hva gjør `Where-Object` i en pipeline?</summary>

**Svar:** `Where-Object` filtrerer objekter i pipelinen og slipper bare gjennom de som oppfyller en betingelse. For eksempel: `Get-Service | Where-Object Status -EQ "Running"` viser bare tjenester som kjører.

</details>

<details><summary>Spørsmål 3: Hvorfor bruker man `-NoTypeInformation` ved `Export-Csv`?</summary>

**Svar:** Uten `-NoTypeInformation` legger PowerShell til en ekstra første linje i CSV-filen med .NET-typenavnet til objektet (f.eks. `#TYPE Microsoft.PowerShell.Commands.LocalUser`). Denne linjen er unødvendig og kan forvirre andre programmer som leser CSV-filen.

</details>

<details><summary>Spørsmål 4: Hva er forskjellen på enkelthermetegn og dobbelthermetegn i PowerShell?</summary>

**Svar:** Enkelthermetegn (`'...'`) er statiske strenger — ingenting tolkes, variabelnavn skrives ut bokstavelig. Dobbelthermetegn (`"..."`) ekspanderer variabler og subexpressions. For eksempel: `'$navn'` gir teksten `$navn`, mens `"$navn"` gir verdien av variabelen `$navn`.

</details>

<details><summary>Spørsmål 5: Hva må til for at en feil skal fanges av `catch` i PowerShell?</summary>

**Svar:** Man må legge til `-ErrorAction Stop` på cmdleten som kan feile. Som standard er PowerShell-cmdlets satt til å fortsette selv ved feil (`-ErrorAction Continue`), og da kastes ikke en unntaksfeil som `catch` kan fange.

</details>

---

## Flashcards

Cmdlet :: Grunnleggende kommandoenhet i PowerShell, følger Verb-Substantiv-mønster (f.eks. Get-Service)
`$_` :: Automatisk variabel i PowerShell som representerer gjeldende objekt i en pipeline
`Get-Member` :: Cmdlet som viser alle egenskaper og metoder for objektene som sendes inn
`Where-Object` :: Cmdlet som filtrerer pipeline-objekter basert på en betingelse
`Select-Object` :: Cmdlet som velger bestemte egenskaper fra pipeline-objekter
`Export-Csv` :: Cmdlet som skriver pipeline-objekter til en CSV-fil
`Import-Module` :: Laster inn en PowerShell-modul med tilhørende cmdlets
`param`-blokk :: Deklarerer parametere til en PowerShell-funksjon med type og validering
`[Parameter(Mandatory)]` :: Attributt som gjør en funksjonsparameter obligatorisk
`-ErrorAction Stop` :: Gjør at en cmdlet kaster et unntak ved feil, slik at `catch` kan fange det
Execution Policy :: Sikkerhetspolitikk som bestemmer hvilke PowerShell-skript som kan kjøres
`$env:COMPUTERNAME` :: Automatisk miljøvariabel med maskinens navn

---

## Ressurser

- [Microsoft Learn – PowerShell 101: Komme i gang](https://learn.microsoft.com/en-us/powershell/scripting/learn/ps101/01-getting-started)
- [Microsoft Learn – PowerShell 101: Pipeline](https://learn.microsoft.com/en-us/powershell/scripting/learn/ps101/04-pipelines)
- [Microsoft Learn – PowerShell 101: Funksjoner](https://learn.microsoft.com/en-us/powershell/scripting/learn/ps101/09-functions)
- [SS64 – PowerShell cmdlet-referanse](https://ss64.com/ps/)
