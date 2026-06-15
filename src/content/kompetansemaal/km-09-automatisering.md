---
title: "KM-09: Automatisering / Automation"
emne: kompetansemaal
kompetansemaal:
  - km-09
kilder:
  - https://www.udir.no/lk20/itk02-01/kompetansemaal-og-vurdering/kv372
  - https://learn.microsoft.com/en-us/powershell/
  - https://www.gnu.org/software/bash/
  - https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/
tags: [km-09, automatisering, bash, powershell, skripting]
flashcards: false
public: true
---

# KM-09: Automatisering / Automation

## 🎯 Mål / Competency Goal

**Norsk:** Forenkle og automatisere arbeidsprosesser i utvikling av IT-løsninger

**English:** Simplify and automate work processes in the development of IT solutions

---

## 📘 Forklaring / Explanation

### Norsk

Automatisering betyr å få datamaskiner til å gjøre repetitive oppgaver for deg — slik at du slipper å gjøre dem manuelt. I IT-drift er automatisering helt avgjørende for effektivitet og pålitelighet[^1][^2].

**Hvorfor automatisere?**

- **Tidsbesparelse** — En jobb som tar 1 time manuelt kan gjøres på 1 sekund med et skript
- **Færre feil** — Datamaskiner gjør samme operasjon likt hver gang
- **Dokumentasjon** — Skriptet i seg selv dokumenterer hva som ble gjort
- **Skalerbarhet** — Samme skript fungerer på 1 eller 1000 datamaskiner

**Verktøy for automatisering:**

- **Bash** — Linux/Unix shell-skripting, perfekt for filoperasjoner og systemadministrasjon
- **PowerShell** — Microsofts avanserte skriptspråk for Windows-serveradministrasjon
- **Ansible** — Konfigurasjonsstyringsverktøy (agentløst, bruker YAML)
- **Cron-jobb** — Planlagte oppgaver i Linux
- **Task Scheduler** — Planlagte oppgaver i Windows

### English

Automation means making computers do repetitive tasks for you — so you don't have to do them manually. In IT operations, automation is critical for efficiency and reliability[^1].

**Why automate?**

- **Saves time** — A 1-hour manual job takes 1 second with a script
- **Fewer errors** — Computers perform the same operation consistently
- **Documentation** — The script itself documents what was done
- **Scalability** — Same script works on 1 or 1000 computers

**Tools for automation:**

- **Bash** — Linux/Unix shell scripting, perfect for file operations and system administration
- **PowerShell** — Microsoft's advanced scripting language for Windows server administration
- **Ansible** — Configuration management tool (agentless, uses YAML playbooks)
- **Cron** — Scheduled tasks in Linux
- **Task Scheduler** — Scheduled tasks in Windows

---

## 💡 Eksempler / Examples

### Norsk

**Eksempel 1: Lage 100 brukere på 10 sekunder**
I stedet for å klikke i AD-brukergrensesnittet 100 ganger, skriver du et PowerShell-skript som oppretter alle brukerne fra en CSV-fil. Ferdig på 10 sekunder.

**Eksempel 2: Backup-skript i Bash**

```bash
#!/bin/bash
tar -czf /backup/hjemmeomrader-$(date +%Y%m%d).tar.gz /home/
```

Dette skriptet kan kjøres automatisk hver natt via cron.

### English

**Example 1: Create 100 Users in 10 Seconds**
Instead of clicking in the AD interface 100 times, you write a PowerShell script that creates all users from a CSV file. Done in 10 seconds.

**Example 2: Backup Script in Bash**

```bash
#!/bin/bash
tar -czf /backup/homes-$(date +%Y%m%d).tar.gz /home/
```

This script can run automatically every night via cron.

---

## 📝 Oppsummering / Summary

| Norsk | English |
|-------|---------|
| Automatisering = få datamaskiner til å gjøre repetitive oppgaver | Automation = making computers do repetitive tasks |
| Bash for Linux, PowerShell for Windows | Bash for Linux, PowerShell for Windows |
| Skripting sparer tid og reduserer feil | Scripting saves time and reduces errors |
| Planlagte oppgaver (cron/Task Scheduler) kjører skript automatisk | Scheduled tasks (cron/Task Scheduler) run scripts automatically |

---

## 🔧 Bridging Exercises / Praksisoppgaver

### Norsk — Praksisoppgaver

**Oppgave 1: PowerShell-skript for masseopprettelse av AD-brukere**
IT-avdelingen skal opprette 30 nye elevkontoer ved skolestart.

- Lag en CSV-fil med kolonner: Fornavn, Etternavn, Klasse, Brukernavn
- Skriv et PowerShell-skript som:
  - Leser CSV-filen
  - Oppretter hver bruker i Active Directory
  - Plasserer brukeren i riktig OU basert på klasse
  - Setter midlertidig passord (f.eks. Skole2026!)
  - Tvinger passordendring ved første pålogging
  - Logger alle operasjoner til en tidsstemplet loggfil
- Test med 3 testbrukere før du kjører på alle 30
- Bonus: Legg til feilhåndtering (hva skjer om brukeren allerede finnes?)

**Oppgave 2: Bash-skript for backup med cron-jobb**
Skolen trenger automatisert backup av hjemmeområdene.

- Skriv et Bash-skript som:
  - Tar en komprimert tar-arkiv-backup av `/home/`
  - Lagrer til `/backup/` med dato i filnavnet (f.eks. backup-20260608.tar.gz)
  - Sletter backup eldre enn 14 dager
  - Logger suksess/feil til `/var/log/backup.log`
  - Sender e-post til IT ved feil (bonus)
- Gjør skriptet kjørbart (`chmod +x`)
- Sett opp cron-jobb som kjører skriptet hver natt kl 02:00
- Verifiser at cron-jobben kjører og at backup-filen opprettes

**Veiledning / Solution Guidelines:**

- Oppgave 1 (PowerShell): `Import-Csv .\elever.csv | ForEach-Object { New-ADUser ... }`. OU: `OU=$($_.Klasse),OU=Elever,DC=skole,DC=local`. Logging: `Add-Content -Path .\logg.txt -Value "$(Get-Date) - Opprettet $($_.Brukernavn)"`. Feilhåndtering: `try { New-ADUser ... } catch { Write-Warning ... }`.
- Oppgave 2 (Bash): `tar -czf /backup/backup-$(date +%Y%m%d).tar.gz /home/`. Sletting: `find /backup/ -name "backup-*.tar.gz" -mtime +14 -delete`. Cron: `0 2 * * * /usr/local/bin/backup.sh`. Verifiser: `ls -la /backup/` og `cat /var/log/backup.log`.

### English — Practical Exercises

**Exercise 1: PowerShell Script for Bulk AD User Creation**
The IT department needs to create 30 new student accounts.

- Create a CSV with columns: FirstName, LastName, Class, Username
- Write a PowerShell script that reads the CSV, creates users in AD, places them in correct OUs, sets temporary password, forces password change at first login, logs all operations
- Test with 3 users first
- Bonus: Add error handling

**Exercise 2: Bash Backup Script with Cron**
Create an automated backup solution:

- Bash script: compressed tar archive of /home/, date-stamped filenames, delete backups older than 14 days, log to /var/log/backup.log
- Make it executable, set up cron job for nightly 02:00
- Verify the backup file is created

**Solution Guidelines:**

- Exercise 1 (PowerShell): `Import-Csv | ForEach-Object { New-ADUser ... }`. Error handling with try/catch.
- Exercise 2 (Bash): `tar -czf`, `find ... -mtime +14 -delete`, cron: `0 2 * * *`.

## 🔗 Relevante artikler / Related Articles

- [[automatisering]] — Automatisering av IT-arbeidsprosesser
- [[bash-grunnleggende]] — Bash-skripting for Linux-administrasjon
- [[powershell-grunnleggende]] — PowerShell-skripting for Windows-administrasjon

## 📚 Kilder / Sources

[^1]: Udir (2020). Læreplan i Vg2 informasjonsteknologi. <https://www.udir.no/lk20/itk02-01/>
[^2]: NDLA. Fagstoff for driftsstøtte VG2. <https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/>
