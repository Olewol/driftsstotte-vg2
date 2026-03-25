---
title: "Bash – grunnleggende skripting"
emne: skripting
kompetansemaal:
  - km-09
kilder:
  - ndla
  - https://ndla.no/nb/subject:1:89932061-799d-499d-948c-399738003791/topic:1:185333/resource:1:153844
  - https://learnxinyminutes.com/docs/bash/
tags: []
flashcards: https://notebooklm.google.com/notebook/15678f10-b24e-462c-b837-076df87bd4b7
public: true
video: https://www.youtube.com/watch?v=e7BufAVwgyM
notebooklm: true
---

## Introduksjon

Bash (Bourne Again SHell) er standardskallet på de fleste Linux-distribusjoner og macOS. Det er det første språket de fleste systemadministratorer lærer å skripte i, og med god grunn: Bash er tilgjengelig overalt på Linux, krever ingen installasjon og har direkte tilgang til alle systemverktøy.

I denne artikkelen lærer du de grunnleggende byggesteinene i Bash-skripting: shebang, variabler, betingede utsagn, løkker, funksjoner og filoperasjoner. Alt dette brukes i den praktiske laben der vi bygger et fullstendig backup-skript.

Bash er tett knyttet til [[linux-grunnleggende]] og brukes aktivt i [[automatisering]] av driftsoppgaver. Vil du sammenligne med Windows-siden, se [[powershell-grunnleggende]].

---

## Teori

### Shebang — `#!/bin/bash`

Den aller første linjen i et Bash-skript kalles **shebang** (eller hashbang). Den forteller operativsystemet hvilket program som skal tolke filen.

```bash
#!/bin/bash
```

- `#!` er et magisk prefiks som operativsystemet gjenkjenner.
- `/bin/bash` er stien til Bash-tolken.

Uten shebang vil skriptet kanskje kjøre, men man er avhengig av at skallet som kalte skriptet er Bash. Med shebang er det alltid eksplisitt.

For å gjøre filen kjørbar brukes `chmod`:

```bash
chmod +x miskript.sh
./miskript.sh
```

### Variabler

En variabel er en navngitt lagringsplass for data. I Bash deklareres variabler uten mellomrom rundt `=`:

```bash
NAVN="Ola Nordmann"
ALDER=25
```

For å lese verdien bruker man `$` foran navnet:

```bash
echo "Hei, $NAVN"
echo "Du er $ALDER år gammel"
```

**Viktige regler:**
- Ingen mellomrom rundt `=` ved tilordning (`VAR="verdi"`, ikke `VAR = "verdi"`).
- Bruk dobbelthermetegn `"..."` rundt variabler for å håndtere mellomrom i verdier.
- Enkelthermetegn `'...'` tolker ikke variabler — `'$NAVN'` gir ordrett `$NAVN`.

**Innebygde variabler** (miljøvariabler):

| Variabel | Innhold |
|---|---|
| `$HOME` | Hjemmemappen til brukeren |
| `$USER` | Brukernavnet |
| `$PATH` | Mapper der skallet søker etter programmer |
| `$0` | Navnet på skriptet |
| `$1`, `$2` ... | Argumenter gitt til skriptet |
| `$#` | Antall argumenter |
| `$?` | Exit-kode fra forrige kommando (0 = suksess) |
| `$$` | Prosess-ID (PID) til skriptet |

**Kommandosubstitusjon** — lagre utdata fra en kommando i en variabel:

```bash
DATO=$(date +%Y-%m-%d)
echo "I dag er det $DATO"
```

### Betingede utsagn — if/else

`if`-setningen lar skriptet ta valg basert på en betingelse.

```bash
if [ betingelse ]; then
    # kjøres hvis betingelsen er sann
elif [ annen_betingelse ]; then
    # kjøres hvis den andre betingelsen er sann
else
    # kjøres hvis ingen betingelse er sann
fi
```

Mellomrommene inne i `[ ]` er obligatoriske.

**Filtester:**

| Test | Beskrivelse |
|---|---|
| `[ -f FIL ]` | Filen eksisterer og er en vanlig fil |
| `[ -d MAPPE ]` | Mappen eksisterer |
| `[ -r FIL ]` | Filen er lesbar |
| `[ -x FIL ]` | Filen er kjørbar |
| `[ -e STI ]` | Stien eksisterer (fil eller mappe) |

**Strengsammenligninger:**

| Test | Beskrivelse |
|---|---|
| `[ "$A" == "$B" ]` | Strengene er like |
| `[ "$A" != "$B" ]` | Strengene er ulike |
| `[ -z "$A" ]` | Strengen er tom |
| `[ -n "$A" ]` | Strengen er ikke tom |

**Numeriske sammenligninger:**

| Test | Beskrivelse |
|---|---|
| `[ $A -eq $B ]` | A er lik B |
| `[ $A -ne $B ]` | A er ikke lik B |
| `[ $A -lt $B ]` | A er mindre enn B |
| `[ $A -gt $B ]` | A er større enn B |
| `[ $A -le $B ]` | A er mindre enn eller lik B |
| `[ $A -ge $B ]` | A er større enn eller lik B |

Eksempel:

```bash
if [ -f "/etc/passwd" ]; then
    echo "Filen eksisterer"
else
    echo "Filen ble ikke funnet"
fi
```

### For-løkker

En `for`-løkke gjentar en blokk med kommandoer for hvert element i en liste.

```bash
for VARIABEL in element1 element2 element3; do
    echo "$VARIABEL"
done
```

Praktisk eksempel — iterer over filer i en mappe:

```bash
for FIL in /var/log/*.log; do
    echo "Behandler: $FIL"
done
```

Telle med en tallerekke:

```bash
for i in $(seq 1 5); do
    echo "Runde $i"
done
```

### While-løkker

En `while`-løkke kjøres så lenge betingelsen er sann.

```bash
TELLER=1
while [ $TELLER -le 5 ]; do
    echo "Iterasjon $TELLER"
    TELLER=$((TELLER + 1))
done
```

`$((uttrykk))` brukes for aritmetikk i Bash.

### Funksjoner

Funksjoner samler gjenbrukbar kode i navngitte blokker. De defineres øverst i skriptet og kalles ved navn.

```bash
function vis_hilsen {
    echo "Hei, $1!"
}

vis_hilsen "Ola"
vis_hilsen "Kari"
```

- `$1` inne i funksjonen refererer til første argument gitt til funksjonen (ikke skriptet).
- `local` brukes for variabler som kun skal eksistere inne i funksjonen:

```bash
function beregn_sum {
    local A=$1
    local B=$2
    echo $((A + B))
}

RESULTAT=$(beregn_sum 10 20)
echo "Summen er: $RESULTAT"
```

### Filoperasjoner

Bash har kraftige innebygde kommandoer for filhåndtering:

| Kommando | Beskrivelse |
|---|---|
| `mkdir -p STI` | Opprett mappe (og foreldre-mapper om nødvendig) |
| `cp -r KILDE MAL` | Kopier rekursivt (inkl. undermapper) |
| `mv KILDE MAL` | Flytt eller gi nytt navn |
| `rm -r MAPPE` | Slett mappe rekursivt |
| `ls -la` | List filer med detaljer |
| `find STI -name "*.log"` | Finn filer etter navn |

### Shellcheck — statisk analyse av skript

**Shellcheck** er et gratis verktøy som analyserer Bash-skript og peker på potensielle feil, dårlige vaner og sikkerhetsproblemer — uten at du trenger å kjøre skriptet.

```bash
# Installer på Ubuntu/Debian
sudo apt install shellcheck

# Analyser et skript
shellcheck backup.sh
```

Shellcheck vil for eksempel advare om manglende anførselstegn rundt variabler (`"$VAR"` i stedet for `$VAR`), noe som kan gi uventede feil når filnavn inneholder mellomrom. Det er god praksis å kjøre shellcheck på alle skript før de settes i produksjon.

### Feilhåndtering

Standardvariabelen `$?` inneholder exit-koden til forrige kommando. `0` betyr suksess, alt annet er en feil.

```bash
cp /viktig/fil /backup/
if [ $? -ne 0 ]; then
    echo "FEIL: Kopiering mislyktes!" >&2
    exit 1
fi
```

`>&2` sender feilmeldingen til stderr i stedet for stdout.

Et enklere alternativ er `set -e` øverst i skriptet — da stopper skriptet automatisk ved første feil:

```bash
#!/bin/bash
set -e
```

---

## Eksempel / lab

### Lab: Fullstendig backup-skript

Vi skal skrive et skript som:
1. Definerer kilde- og målmappe
2. Oppretter en datobasert backup-mappe
3. Kopierer innholdet
4. Bekrefter at det gikk bra

```bash
#!/bin/bash
# backup.sh — Daglig backup av dokumenter
# Bruk: ./backup.sh

set -e  # Stopp ved første feil

# ─── Konfigurasjon ───────────────────────────────────────────
KILDE="/home/bruker/dokumenter"
MAL="/backup/$(date +%Y-%m-%d)"

# ─── Sjekk at kildemappe eksisterer ─────────────────────────
if [ ! -d "$KILDE" ]; then
    echo "FEIL: Kildemappen '$KILDE' eksisterer ikke." >&2
    exit 1
fi

# ─── Opprett målmappe ────────────────────────────────────────
mkdir -p "$MAL"

# ─── Utfør kopiering ─────────────────────────────────────────
cp -r "$KILDE" "$MAL"

# ─── Bekreftelse ─────────────────────────────────────────────
echo "Backup fullført: $MAL"
```

**Linje-for-linje forklaring:**

| Linje | Forklaring |
|---|---|
| `#!/bin/bash` | Shebang — kjør med Bash |
| `set -e` | Stopp skriptet umiddelbart hvis en kommando feiler |
| `KILDE=...` | Variabel for kildemappen som skal sikkerhetskopieres |
| `MAL=...` | Variabel for målmappen; `$(date +%Y-%m-%d)` gir dagens dato som mappe-navn |
| `if [ ! -d "$KILDE" ]` | Sjekk at kildemappen faktisk finnes (`!` betyr IKKE, `-d` sjekker mappe) |
| `exit 1` | Avslutt skriptet med feilkode 1 (indikerer feil) |
| `mkdir -p "$MAL"` | Opprett målmappen; `-p` lager også foreldremapper uten feil hvis de finnes |
| `cp -r "$KILDE" "$MAL"` | Kopier rekursivt fra kilde til mål |
| `echo "Backup fullført: $MAL"` | Skriv ut bekreftelsesmelding med stien til backup-mappen |

**Slik tester du skriptet:**

```bash
# Gi kjørerettigheter
chmod +x backup.sh

# Test med en trygg kildemappe
KILDE="/tmp/testdokumenter"
mkdir -p "$KILDE"
echo "testinnhold" > "$KILDE/test.txt"

# Kjør skriptet
./backup.sh
```

---

## Study guide

### Bash – grunnleggende skripting

Bash er skallspråket du møter på alle Linux-systemer. Et Bash-skript er en tekstfil med kommandoer som kjøres linje for linje av Bash-tolken.

**Struktur i et skript:**
1. **Shebang** (`#!/bin/bash`) — alltid første linje, peker på tolken.
2. **Variabler** — lagrer data. Tilordnes uten mellomrom (`NAVN="verdi"`), leses med `$NAVN`.
3. **Betingede utsagn** — `if [ betingelse ]; then ... fi` styrer flyten. Bruk filtester (`-f`, `-d`) og sammenligninger (`-eq`, `==`).
4. **Løkker** — `for`-løkken itererer over lister; `while`-løkken kjører så lenge en betingelse er sann.
5. **Funksjoner** — navngitte blokker med gjenbrukbar kode. Argumenter hentes med `$1`, `$2` osv. Bruk `local` for lokale variabler.
6. **Filoperasjoner** — `mkdir -p`, `cp -r`, `mv`, `rm -r`, `find`.
7. **Feilhåndtering** — `$?` er exit-kode (0 = ok). `set -e` stopper skriptet ved første feil. `>&2` sender feilmeldinger til stderr.

**Gode vaner:**
- Bruk alltid `"$VAR"` (dobbelthermetegn) rundt variabler — beskytter mot mellomrom i verdier.
- Kjør `shellcheck skript.sh` for å finne feil før kjøring.
- Bruk absolutte stier i skript som kalles av cron eller automatiserte systemer.
- Kommandosubstitusjon `$(kommando)` lagrer utdata fra en kommando i en variabel.

**Typiske bruksområder i drift:** backup-skript, loggrotasjon, brukeroppretting, systemovervåking — se [[automatisering]] for hvordan slike skript planlegges.

---

## FAQ

**Hva er forskjellen på `[ ]` og `[[ ]]` i Bash?**
`[ ]` er den POSIX-kompatible testen som fungerer i alle Unix-skall. `[[ ]]` er en Bash-utvidelse som gir ekstra funksjoner som mønstermatching med `=~` og logiske operatorer uten behov for `&&`/`||` inni. For VG2-nivå er `[ ]` tilstrekkelig, men det er greit å vite at `[[ ]]` er tryggere mot edge cases.

**Hva skjer hvis jeg glemmer mellomrom inne i `[ ]`?**
Det feiler. `[$VARIABEL -eq 5]` gir syntaksfeil fordi `[` er en kommando som krever mellomrom rundt alle argumentene. Riktig form er `[ $VARIABEL -eq 5 ]`.

**Kan jeg kjøre et Bash-skript uten `chmod +x`?**
Ja, ved å kalle tolken eksplisitt: `bash miskript.sh`. Du trenger da ikke kjørerettigheter. `chmod +x` er nødvendig bare hvis du vil kjøre skriptet direkte med `./miskript.sh`.

**Hva betyr `>&2` i en feilmelding?**
`2` er filbeskriveren for stderr (standardfeil), og `>&2` omdirigerer output til stderr. Det gjør at feilmeldinger kan skilles fra normal output når skriptet kjøres i automatiserte systemer.

**Hva er en exit-kode og hvorfor er 0 suksess?**
En exit-kode er et tall (0–255) et program returnerer når det avsluttes. Konvensjonen i Unix er at 0 betyr "alt gikk bra" og alt annet betyr en form for feil. Bash-skript kan lese forrige kommandos exit-kode med `$?`.

**Hvordan stopper jeg et skript umiddelbart ved feil?**
Legg til `set -e` øverst (etter shebang). Da avsluttes skriptet automatisk med feil hvis en kommando returnerer ikke-null exit-kode — i stedet for å fortsette med feil tilstand.

**Hva er kommandosubstitusjon og når brukes det?**
`$(kommando)` kjører kommandoen og setter inn utdataene i stedet for selve substitusjonen. Typisk bruk: `DATO=$(date +%Y-%m-%d)` lagrer dagens dato i en variabel, som brukes i filnavn for backup-mapper.

---

## Quiz

<details><summary>Spørsmål 1: Hva gjør shebang-linjen `#!/bin/bash` øverst i et skript?</summary>

**Svar:** Den forteller operativsystemet at filen skal tolkes av programmet `/bin/bash`. Uten shebang kan skriptet kjøres av feil tolk eller ikke i det hele tatt.

</details>

<details><summary>Spørsmål 2: Hva er verdien av `$?` etter en kommando som lyktes?</summary>

**Svar:** `0`. I Bash (og Unix generelt) betyr exit-kode `0` suksess. Alle andre verdier indikerer en feil.

</details>

<details><summary>Spørsmål 3: Hvorfor bruker vi `mkdir -p` i stedet for bare `mkdir`?</summary>

**Svar:** `-p` (parents) oppretter også alle manglende foreldremapper i stien, og gir ikke feilmelding hvis mappen allerede eksisterer. `mkdir /backup/2024-01-01` ville feilet hvis `/backup` ikke finnes, men `mkdir -p /backup/2024-01-01` fungerer uansett.

</details>

<details><summary>Spørsmål 4: Hva er forskjellen på `$1` i skriptets hoveddel og `$1` inne i en funksjon?</summary>

**Svar:** I skriptets hoveddel refererer `$1` til første argument gitt til *skriptet* når det kjøres (f.eks. `./skript.sh argument1`). Inne i en funksjon refererer `$1` til første argument gitt til *funksjonen* ved kall.

</details>

<details><summary>Spørsmål 5: Hva gjør `set -e` øverst i et Bash-skript?</summary>

**Svar:** Det gjør at skriptet avbrytes umiddelbart dersom en kommando returnerer en ikke-null exit-kode (dvs. en feil). Dette hindrer at skriptet fortsetter med delvis mislykket tilstand.

</details>

---

## Flashcards

Shebang :: Den første linjen i et skript (`#!/bin/bash`) som forteller OS hvilken tolk som skal brukes
`$?` :: Spesialvariabel som inneholder exit-koden til forrige kommando (0 = suksess)
`$1`, `$2` :: Posisjonelle parametere — argumenter gitt til skriptet eller funksjonen
`set -e` :: Bash-innstilling som avbryter skriptet ved første feil
`$(kommando)` :: Kommandosubstitusjon — kjører kommandoen og setter inn utdataene
`mkdir -p` :: Oppretter mappe og alle manglende foreldremapper, uten feil ved eksisterende mappe
`chmod +x` :: Gir kjørerettigheter til en fil slik at den kan kjøres direkte
`local` :: Nøkkelord i Bash-funksjoner som begrenser variabelens levetid til funksjonsblokken
`[ -d STI ]` :: Bash-test som er sann dersom stien eksisterer og er en mappe
`[ -f STI ]` :: Bash-test som er sann dersom stien eksisterer og er en vanlig fil
Shellcheck :: Statisk analyseverktøy for Bash-skript som finner feil og foreslår beste praksis uten å kjøre skriptet
Exit-kode :: Statuskode (0–255) som returneres av en kommando; 0 = suksess, alt annet = feil
Kommandosubstitusjon :: Teknikk (`$(kommando)`) som kjører en kommando og setter inn resultatet direkte i en variabel

---

## Ressurser

- [TLDP Bash Beginners Guide](https://tldp.org/LDP/Bash-Beginners-Guide/html/index.html)
- [TLDP – Bash if/else syntaks](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_01.html)
- [SS64 – Bash A–Z referanse](https://ss64.com/bash/)
- [NDLA – Bash og Linux-skripting](https://ndla.no/nb/subject:1:89932061-799d-499d-948c-399738003791/topic:1:185333/resource:1:153844)
- [Learn X in Y Minutes – Bash](https://learnxinyminutes.com/docs/bash/) — kompakt syntaks-oversikt
- [YouTube – You need to learn Bash Scripting RIGHT NOW!! (NetworkChuck, ~21 min)](https://www.youtube.com/watch?v=e7BufAVwgyM)
