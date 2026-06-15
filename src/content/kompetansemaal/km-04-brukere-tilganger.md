---
title: "KM-04: Brukere, tilganger og rettigheter / Users, Access and Permissions"
emne: kompetansemaal
kompetansemaal:
  - km-04
kilder:
  - https://www.udir.no/lk20/itk02-01/kompetansemaal-og-vurdering/kv372
  - https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/active-directory-domain-services
  - https://learn.microsoft.com/en-us/training/modules/implement-user-group-management/
  - https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/
tags: [km-04, brukere, tilgangsstyring, active-directory, linux]
flashcards: false
public: true
---

# KM-04: Brukere, tilganger og rettigheter / Users, Access and Permissions

## 🎯 Mål / Competency Goal

**Norsk:** Administrere brukere, tilganger og rettigheter i relevante systemer

**English:** Administer users, access rights and permissions in relevant systems

---

## 📘 Forklaring / Explanation

### Norsk
Brukeradministrasjon handler om å opprette, endre og slette brukerkontoer, og å gi hver bruker akkurat de tilgangene de trenger — verken mer eller mindre. Dette kalles **least privilege principle** (minsterettighetsprinsippet)[^1].

**Hvem styrer hva?**
- **Active Directory (AD DS)** — Microsofts katalogtjeneste for å administrere brukere, datamaskiner og grupper i et Windows-domenenettverk
- **Linux-brukere** — Lokale brukere på Linux-systemer, styrt via `/etc/passwd` og `/etc/sudoers`
- **Databaser** — Egne brukere og tilganger i SQL Server, MySQL, PostgreSQL
- **Filsystem** — NTFS-tillatelser (Windows) og `chmod`/`chown` (Linux)

**Prinsipper:**
- **Least privilege** — Minst nødvendig tilgang for å utføre jobben
- **Role-Based Access Control (RBAC)** — Tilganger gis basert på rolle, ikke enkeltperson
- **Separation of duties** — Ingen skal ha fullmakt alene til kritiske oppgaver

### English
User administration is about creating, modifying, and deleting user accounts, and giving each user exactly the access they need — no more, no less. This is called the **least privilege principle**[^1].

**What controls what?**
- **Active Directory (AD DS)** — Microsoft's directory service for managing users, computers, and groups in a Windows domain network
- **Linux users** — Local users on Linux systems, managed via `/etc/passwd` and `/etc/sudoers`
- **Databases** — Own users and permissions in SQL Server, MySQL, PostgreSQL
- **File systems** — NTFS permissions (Windows) and `chmod`/`chown` (Linux)

**Principles:**
- **Least privilege** — Minimum necessary access to do the job
- **Role-Based Access Control (RBAC)** — Permissions given based on role, not individual
- **Separation of duties** — No one should have sole authority over critical tasks

---

## 💡 Eksempler / Examples

### Norsk

**Eksempel 1: Ny elev**
En ny elev begynner på skolen. IT-administratoren oppretter en bruker i Active Directory, legger eleven i rett elevgruppe, og eleven får automatisk tilgang til trådløst nettverk, hjemmeområde og skriver.

**Eksempel 2: Læreren får flere rettigheter**
En lærer trenger tilgang til å installere programvare på klasseroms-PC-ene. IT legger læreren i gruppen "Lokal administrator" via AD, uten å gi dem domeneadministrator-rettigheter.

### English

**Example 1: New Student**
A new student joins the school. The IT administrator creates a user in Active Directory, places the student in the correct group, and they automatically get access to WiFi, home folder, and printer.

**Example 2: Teacher Gets Elevated Rights**
A teacher needs to install software on classroom PCs. IT adds the teacher to the "Local Administrator" group via AD, without giving them domain admin rights.

---

## 📝 Oppsummering / Summary

| Norsk | English |
|-------|---------|
| Brukeradministrasjon = opprette, endre, slette kontoer | User admin = create, modify, delete accounts |
| Least privilege = gi minimum nødvendig tilgang | Least privilege = give minimum necessary access |
| Active Directory er hovedverktøyet i Windows-miljøer | Active Directory is the main tool in Windows environments |
| Linux bruker egne verktøy (passwd, sudo, chmod) | Linux uses its own tools (passwd, sudo, chmod) |

---

## 🔧 Bridging Exercises / Praksisoppgaver

### Norsk — Praksisoppgaver

**Oppgave 1: Opprett brukere i Active Directory**
Bruk en Windows Server-lab (eller virtuell maskin med AD DS).
- Opprett 5 brukere i riktig OU-struktur:
  - `elev1`-`elev3` i OU=Elever
  - `larer1` i OU=Laerere
  - `admin1` i OU=IT-avdeling
- Opprett 3 sikkerhetsgrupper: G\_Elever, G\_Laerere, G\_IT
- Plasser brukere i riktige grupper
- Del en mappe som fellesområde med NTFS-tillatelser:
  - Elever: lese/skrive i `\\server\felles\elever`
  - Lærere: lese/skrive i `\\server\felles\laerere`
  - IT: full kontroll på alt
- Test at tilgangene fungerer korrekt

**Oppgave 2: Linux-brukeradministrasjon**
Gjennomfør følgende på en Ubuntu-server:
- Opprett brukerne: `ole`, `kari`, `per` med `useradd -m -s /bin/bash`
- Sett passord med `passwd`
- Opprett gruppene: `utviklere` og `operatorer`
- Legg Ole i utviklere, Kari og Per i operatorer
- Opprett mappen `/opt/prosjekt` med:
  - Eier: root, gruppe: utviklere
  - Tillatelser: 775 (rwxrwxr-x)
- Dokumenter alle kommandoer i en rapport

**Veiledning / Solution Guidelines:**
- Oppgave 1 (AD): `New-ADUser -Name "elev1" -Path "OU=Elever,DC=skole,DC=local"`. NTFS: Properties → Security → Add gruppe → velg tillatelser. Test: logg inn som elev1, prøv å skrive til lærermappe — skal feile.
- Oppgave 2 (Linux): `sudo useradd -m -s /bin/bash ole`. `sudo groupadd utviklere`. `sudo usermod -aG utviklere ole`. `sudo chmod 775 /opt/prosjekt`. `sudo chown root:utviklere /opt/prosjekt`.

### English — Practical Exercises

**Exercise 1: Create Users in Active Directory**
Using a Windows Server lab (or VM with AD DS):
- Create 5 users in proper OU structure: 3 students, 1 teacher, 1 admin
- Create 3 security groups
- Share a folder with correct NTFS permissions
- Test access restrictions

**Exercise 2: Linux User Administration**
On an Ubuntu server:
- Create users: `ole`, `kari`, `per`
- Create groups: `developers` and `operators`
- Set up directory `/opt/project` with permissions 775
- Document all commands in a report

**Solution Guidelines:**
- Exercise 1 (AD): `New-ADUser`, `New-ADGroup`, NTFS security tab testing. Students should not be able to write to teacher folders.
- Exercise 2 (Linux): `useradd -m -s /bin/bash`, `groupadd`, `usermod -aG`, `chmod 775`, `chown root:developers /opt/project`.

## 🔗 Relevante artikler / Related Articles

- [[active-directory]] — Active Directory Domain Services
- [[bruker-og-tilgangsstyring]] — Brukeradministrasjon i AD og lokalt
- [[filsystem]] — NTFS-tillatelser og Linux-filtillatelser
- [[linux-grunnleggende]] — Linux-brukeradministrasjon
- [[databaseadministrasjon]] — Database-brukere og tilganger
- [[sql-grunnleggende]] — SQL-tilgangsstyring

## 📚 Kilder / Sources

[^1]: Udir (2020). Læreplan i Vg2 informasjonsteknologi. https://www.udir.no/lk20/itk02-01/
[^2]: Microsoft Learn. Active Directory Domain Services overview. https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/
[^3]: Microsoft Learn. Implement user and group management. https://learn.microsoft.com/en-us/training/modules/implement-user-group-management/
