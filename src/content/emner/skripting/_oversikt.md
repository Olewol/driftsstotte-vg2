---
title: "Skripting og automatisering – oversikt"
emne: skripting
kompetansemaal:

  - km-09

kilder:

  - ndla
  - <https://learn.microsoft.com/nb-no/powershell/scripting/>
  - <https://learnxinyminutes.com/docs/bash/>
  - <https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/>

tags: []
flashcards: false
public: true
---

## Introduksjon

II IT-drift bruker vi kommandolinjen daglig for å utføre oppgaver: kopiere filer, sjekke tjenester, opprette brukere.
IINår de samme oppgavene skal gjøres om igjen, er det bortkastet tid å taste dem inn manuelt hver eneste gang.
IDet er her**skripting**kommer inn.

EEt skript er en tekstfil med en rekke kommandoer som kjøres i sekvens. I stedet for å taste ti kommandoer manuelt kan du
EEkjøre én fil og la maskinen gjøre jobben. Dette er kjernen i kompetansemål km-09: å forenkle og automatisere
Earbeidsprosesser i utvikling av IT-løsninger.

---

## Teori

### Hva er skripting?

SSkripting handler om å skrive instruksjoner til et skall (shell) eller en skriptmotor.
SSSkriptet tolkes linje for linje av et program — for eksempel Bash eller PowerShell — uten å kompileres til maskinkode
Sslik tradisjonelle programmeringsspråk gjør.

Forskjellen på en interaktiv kommandolinje og et skript er enkel:

|| Interaktiv | Skript |
|| --- | --- |
|| Én kommando av gangen | Mange kommandoer i rekkefølge |
|| Resultatet forsvinner | Gjenbrukbart og delerbart |
|| Manuell kjøring | Kan planlegges og automatiseres |

### Hvorfor automatisere?

II driftssammenheng er manuell gjentakelse av oppgaver en av de vanligste kildene til feil og tidstap.
IAutomatisering løser dette ved å:

-**Spare tid**— En oppgave som tar 20 minutter manuelt, tar 2 sekunder som skript.
-**Redusere menneskelige feil**— En maskin gjør alltid akkurat det som er skrevet. En person kan glemme et steg.
-**Sikre konsistens**— Alle servere konfigureres likt, uavhengig av hvem som gjør jobben.
-**Muliggjøre skalering**— Med skript kan du gjøre det samme mot 1 eller 1 000 maskiner.

Typiske automatiseringsscenarier i IT-drift:

-**Backup**— Kopier viktige mapper til en backup-lokasjon hver natt.
-**Brukeradministrasjon**— Opprett og slett Active Directory-brukere basert på en liste.
-**Logganalyse**— Søk gjennom systemlogger og send varsel ved feil.
-**Overvåking**— Sjekk om tjenester kjører og start dem på nytt ved behov.
-**Oppdateringer**— Installer sikkerhetsoppdateringer på alle maskiner automatisk.

### Bash vs. PowerShell

DDe to dominerende skriptspråkene i IT-drift er**Bash**og**PowerShell**. De er laget for ulike plattformer og tenker
Dforskjellig på data.

|| Egenskap | Bash | PowerShell |
|| --- | --- | --- |
|| Primær plattform | Linux, macOS | Windows (også Linux/macOS via PS 7) |
|| Hva sendes i pipeline | Tekst (strenger) | .NET-objekter |
|| Filendelse | `.sh` | `.ps1` |
|| Typisk bruk | Serveradmin, DevOps, CI/CD | Windows-administrasjon, Azure |
|| Kursrelevans | Backup, cron, systemer | Active Directory, Task Scheduler |

BBash er standard på alle Linux-distribusjoner og macOS. PowerShell er innebygd i Windows og har siden versjon 7 blitt
Bcross-platform. I VG2 IT lærer vi begge — Bash for Linux-oppgaver og PowerShell for Windows-administrasjon.

DDet finnes også Python, som er et fullverdig programmeringsspråk brukt mye til automatisering, men det dekkes ikke i
Ddette emnet.

### Skriptets livssyklus

Et godt skript utvikles i faser:

1.**Planlegging**— Hva skal automatiseres? Hvilke steg inngår?
2.**Koding**— Skriv skriptet, test delene underveis.
3.**Testing**— Kjør skriptet i et trygt miljø. Sjekk at feil håndteres.
4.**Planlegging/kjøring**— Sett opp automatisk kjøring via cron eller Task Scheduler.
5.**Vedlikehold**— Oppdater skriptet når miljøet endrer seg.

### Skripting og DevOps / IaC

SSkripting er grunnmuren under moderne DevOps og Infrastructure as Code (IaC). Verktøy som Ansible, Terraform og Docker
SSbruker alle konfigurasjonsfiler som likner på skript. Når du forstår Bash og PowerShell, er veien kort til å lære disse
Sverktøyene.

---

## Artikler i dette emnet

- [[bash-grunnleggende]] — Variabler, if/else, løkker, funksjoner og backup-skript i Bash
- [[powershell-grunnleggende]] — Cmdlets, pipeline, objekter og brukeradministrasjon i PowerShell
- [[automatisering]] — Task Scheduler, cron og introduksjon til Infrastructure as Code

---

## Ressurser

- [TLDP Bash Beginners Guide](<https://tldp.org/LDP/Bash-Beginners-Guide/html/index.html>)
- [Microsoft Learn – PowerShell 101](<https://learn.microsoft.com/en-us/powershell/scripting/learn/ps101/01-getting-started>)
- [SS64 – Bash referanse](<https://ss64.com/bash/>)
- [SS64 – PowerShell referanse](<https://ss64.com/ps/>)
