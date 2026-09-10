# Skripting læringskort

## Card 1

**Q:** Hva er den fundamentale forskjellen på hvordan data sendes i en Bash-pipeline kontra en PowerShell-pipeline?

**A:** Bash sender ren tekst (strenger), mens PowerShell sender strukturerte .NET-objekter.

---

## Card 2

**Q:** Hvilket navngivningsmønster følger alle standard cmdlets i PowerShell?

**A:** Verb-Substantiv (for eksempel Get-Service).

---

## Card 3

**Q:** Hva kalles den første linjen i et Bash-skript (f.eks. #!/bin/bash) som forteller systemet hvilken tolk som skal brukes?

**A:** Shebang (eller hashbang).

---

## Card 4

**Q:** Hvilken PowerShell-cmdlet brukes for å se alle tilgjengelige egenskaper og metoder for et objekt i pipelinen?

**A:** Get-Member

---

## Card 5

**Q:** Hva er betydningen av en exit-kode på 0 i Unix- og Linux-systemer?

**A:** Det indikerer at kommandoen eller skriptet ble utført vellykket (suksess).

---

## Card 6

**Q:** Hva kalles prinsippet om at et skript kan kjøres flere ganger uten å endre resultatet etter den første vellykkede kjøringen?

**A:** Idempotens

---

## Card 7

**Q:** Hvilke fem tidsfelt inngår i en standard crontab-linje i Linux?

**A:** Minutt, time, dag i måneden, måned, og dag i uken.

---

## Card 8

**Q:** Hva er den primære funksjonen til PowerShell Execution Policy?

**A:** Det er en sikkerhetsinnstilling som bestemmer hvilke vilkår som må være oppfylt for at skript skal kunne kjøres.

---

## Card 9

**Q:** I Bash, hvilket tegn brukes for å referere til verdien av en variabel?

**A:** Dollartegnet ($).

---

## Card 10

**Q:** Hvilken omdirigering i Bash sender både standard utdata (stdout) og feilmeldinger (stderr) til samme fil?

**A:** 2>&1 (ofte brukt som >> fil.log 2>&1).

---

## Card 11

**Q:** Hva er forskjellen på 'imperativ' skripting og 'deklarativ' Infrastructure as Code (IaC)?

**A:** Imperativ beskriver stegene som skal gjøres, mens deklarativ beskriver den ønskede slutttilstanden.

---

## Card 12

**Q:** Nevn de tre delene en planlagt oppgave i Windows Task Scheduler består av.

**A:** Trigger (når), handling (hva), og betingelser (tilleggskrav).

---

## Card 13

**Q:** Hvilken PowerShell-cmdlet brukes for å finne hjelp og dokumentasjon om andre kommandoer?

**A:** Get-Help

---

## Card 14

**Q:** Hva gjør kommandoen 'chmod +x skript.sh' i Linux?

**A:** Den gir skriptfilen kjøretillatelse.

---

## Card 15

**Q:** I PowerShell, hva er forskjellen på Write-Host og Write-Output?

**A:** Write-Host skriver bare til skjermen, mens Write-Output sender objekter videre i pipelinen.

---

## Card 16

**Q:** Hvilken variabel i Bash inneholder exit-koden til den forrige kommandoen som ble kjørt?

**A:** $?

---

## Card 17

**Q:** Hvilket verktøy anbefales for å analysere Bash-skript for potensielle feil og dårlig praksis uten å kjøre dem?

**A:** Shellcheck

---

## Card 18

**Q:** Hva er formålet med 'try-catch-finally' blokker i PowerShell-skripting?

**A:** Å håndtere feil på en strukturert måte og sikre at opprydding skjer uavhengig av om en feil oppstår.

---

## Card 19

**Q:** I en crontab-fil, hva betyr verdien '*/15' i det første feltet?

**A:** At oppgaven skal kjøres hvert 15. minutt.

---

## Card 20

**Q:** Hvilket IaC-verktøy er kjent for å være 'agentfritt' og bruke YAML-filer kalt 'playbooks'?

**A:** Ansible

---

## Card 21

**Q:** Hva skjer i PowerShell hvis du bruker enkelthermetegn (' ') rundt en tekststreng som inneholder en variabel?

**A:** Variabelen blir ikke tolket, og teksten skrives ut nøyaktig slik den står (bokstavelig).

---

## Card 22

**Q:** Hvilken Bash-test brukes for å sjekke om en bestemt sti eksisterer og er en mappe?

**A:** [ -d STI ]

---

## Card 23

**Q:** Hvilken PowerShell-cmdlet tilsvarer Linux-kommandoen 'ls' for å liste innhold i en mappe?

**A:** Get-ChildItem

---

## Card 24

**Q:** Hva er formålet med 'set -e' i starten av et Bash-skript?

**A:** Det sørger for at skriptet avsluttes umiddelbart dersom en kommando returnerer en feilkode.

---

## Card 25

**Q:** Hva kalles Microsofts rammeverk for konfigurasjonsstyring som bruker konfigurasjon-som-kode?

**A:** PowerShell Desired State Configuration (DSC).

---

## Card 26

**Q:** I Bash, hva skjer hvis du har mellomrom rundt likhetstegnet ved tilordning av en variabel (f.eks. VAR = verdi)?

**A:** Det gir en feilmelding fordi skallet tolker variabelnavnet som en kommando.

---

## Card 27

**Q:** Hvilken PowerShell-variabel representerer det nåværende objektet som behandles i pipelinen?

**A:** $_ (eller $PSItem).

---

## Card 28

**Q:** I Linux, hvilken crontab-snarvei brukes for å kjøre en oppgave én gang ved systemoppstart?

**A:** @reboot

---

## Card 29

**Q:** Hva er hovedforskjellen mellom PowerShell ISE og VS Code med PowerShell-utvidelse?

**A:** PowerShell ISE støtter kun eldre Windows PowerShell, mens VS Code er det moderne verktøyet som støtter PowerShell 7+ og flere plattformer.

---

## Card 30

**Q:** Hvilken parameter til 'mkdir' i både Linux og PowerShell (New-Item) sørger for at foreldremapper opprettes uten feilmelding?

**A:** -p (Linux) eller -Force (PowerShell New-Item).

---

## Card 31

**Q:** Hva betyr 'RemoteSigned' som Execution Policy i PowerShell?

**A:** Lokale skript kan kjøres uten signatur, men skript lastet ned fra internett må være signert av en pålitelig utgiver.

---

## Card 32

**Q:** Hvordan defineres en funksjon i Bash?

**A:** Ved å skrive funksjonsnavn etterfulgt av parenteser og krøllparenteser: funksjon_navn() { ... }.

---

## Card 33

**Q:** Hva brukes 'Export-Csv' til i PowerShell?

**A:** Å konvertere objekter i pipelinen til en CSV-fil.

---

## Card 34

**Q:** I Bash-skripting, hva refererer variabelen $1 til inne i en funksjon?

**A:** Det første argumentet som ble sendt til funksjonen ved oppkall.

---

## Card 35

**Q:** Hvilken kommando i Linux brukes for å redigere gjeldende brukers planlagte oppgaver?

**A:** crontab -e

---

## Card 36

**Q:** Hva er fordelen med å bruke absolutte stier i automatiserte skript (som i cron)?

**A:** Det sikrer at skriptet finner riktige filer selv om miljøvariabelen PATH er begrenset eller annerledes.

---

## Card 37

**Q:** Hva er 'kommandosubstitusjon' i Bash, og hvilken syntaks brukes?

**A:** Det er å lagre utdata fra en kommando i en variabel ved å bruke syntaksen $(kommando).

---

## Card 38

**Q:** Hva gjør parameteren '-NoTypeInformation' når man eksporterer til CSV i PowerShell?

**A:** Den fjerner den øverste linjen i filen som spesifiserer .NET-objekttypen.

---

## Card 39

**Q:** Hvorfor bør man unngå interaktive dialoger (som Read-Host) i skript ment for automatisering?

**A:** Interaktive dialoger krever menneskelig inngripen, noe som stopper den automatiserte flyten.

---

## Card 40

**Q:** Hva brukes 'schtasks' kommandoen til i Windows?

**A:** Administrasjon av planlagte oppgaver (Task Scheduler) fra kommandolinjen.

---

## Card 41

**Q:** I Bash, hva er forskjellen på bruk av enkelte (') og doble (") anførselstegn rundt variabler?

**A:** Doble anførselstegn tillater variabeltolking, mens enkelte anførselstegn behandler alt som bokstavelig tekst.

---

## Card 42

**Q:** Hvilken PowerShell-cmdlet brukes for å filtrere objekter i pipelinen basert på en logisk betingelse?

**A:** Where-Object

---

## Card 43

**Q:** Hva er den viktigste fordelen med Infrastructure as Code (IaC) når det gjelder feilretting?

**A:** Det muliggjør versjonskontroll, slik at man enkelt kan rulle tilbake til en tidligere fungerende konfigurasjon.

---

## Card 44

**Q:** I Bash, hva sjekker testen '[ -f FIL ]'?

**A:** Om filen eksisterer og er en vanlig fil (ikke en mappe).

---

## Card 45

**Q:** Hvordan kan man skjule PowerShell-vinduet når et skript kjøres via Task Scheduler?

**A:** Ved å bruke argumentet '-WindowStyle Hidden'.

---

## Card 46

**Q:** Hva er 'local' nøkkelordet i en Bash-funksjon?

**A:** Det sørger for at variabelen kun er tilgjengelig inne i den spesifikke funksjonen (lokalt omfang).

---

## Card 47

**Q:** Hvilken PowerShell-cmdlet henter informasjon om alle kommandoer som er installert på systemet?

**A:** Get-Command

---

## Card 48

**Q:** Hva er 'jq' i en Bash-sammenheng?

**A:** Et eksternt verktøy som ofte brukes for å håndtere og filtrere strukturerte JSON-data.

---

## Card 49

**Q:** Hva er 'idempotens' i forbindelse med IaC-verktøy som Terraform?

**A:** Verktøyet sjekker nåværende tilstand og gjør bare endringer dersom det er nødvendig for å nå ønsket slutttilstand.

---

## Card 50

**Q:** Hva kalles metoden i PowerShell for å velge ut spesifikke kolonner eller egenskaper fra et objekt?

**A:** Select-Object

---

## Card 51

**Q:** I Bash, hvilken operator brukes for numerisk sammenligning av 'større enn'?

**A:** -gt

---

## Card 52

**Q:** Hvorfor er det god praksis å dokumentere skript med kommentarer?

**A:** For at andre (og deg selv i fremtiden) skal kunne forstå logikken og vedlikeholde koden.

---

## Card 53

**Q:** Hva skjer i Linux hvis en cron-jobb produserer utdata, men ingen omdirigering til fil er satt opp?

**A:** Utdataene sendes vanligvis som en e-post til den lokale systembrukeren.

---

## Card 54

**Q:** Hvilken PowerShell-modul må importeres for å administrere brukere i et Windows-domene?

**A:** ActiveDirectory-modulen.

---

## Card 55

**Q:** Hva er 'HCL' i forbindelse med Terraform?

**A:** HashiCorp Configuration Language, språket som brukes til å definere infrastruktur i Terraform.

---

## Card 56

**Q:** I PowerShell, hva gjør operatoren '-eq'?

**A:** Den sjekker om to verdier er like (equal).

---

## Card 57

**Q:** Hva er formålet med 'Set-Content' cmdleten?

**A:** Å skrive innhold til en fil (overskriver eksisterende innhold).

---

## Card 58

**Q:** I Bash, hvordan kan man omdirigere feilmeldinger (stderr) til en egen fil?

**A:** Ved å bruke operatoren '2> feil.log'.

---

## Card 59

**Q:** Hva er hovedforskjellen mellom Windows PowerShell 5.1 og PowerShell 7?

**A:** Windows PowerShell 5.1 er låst til Windows, mens PowerShell 7 er basert på .NET Core og er cross-platform.

---

## Card 60

**Q:** Nevn en vanlig bruk av 'hashtables' (@{ }) i PowerShell.

**A:** Lagring av data i nøkkel-verdi-par, for eksempel for konfigurasjonsinnstillinger.

---
