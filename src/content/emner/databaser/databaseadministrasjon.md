---
title: "Databaseadministrasjon"
emne: databaser
kompetansemaal:
  - km-04
kilder:
  - ndla
  - https://ndla.no/subject:1:7e101f30-891d-4076-a70e-1100f9156475/topic:1:a6e7039a-5e1a-4c92-b05b-439f72765366/resource:73797690-3486-444c-bc6d-62725e173e97
  - https://dev.mysql.com/doc/refman/8.0/en/optimization.html
video: https://www.youtube.com/watch?v=u96rS6Y236M
notebooklm: true
tags: []
flashcards: https://notebooklm.google.com/notebook/e9134332-9a2e-4991-9a72-2807660c7610
public: true
---

## Introduksjon

Databaseadministrasjon handler om å holde en databaseserver trygg, tilgjengelig og effektiv over tid. For en driftstøtter er dette daglig arbeid: du oppretter brukere, tildeler tilganger, tar backup, gjenoppretter data etter feil og sørger for at serveren ikke er for treg.

Denne artikkelen tar for seg tre kjerneområder i MySQL-administrasjon: **brukertilgang**, **backup og gjenoppretting**, og **ytelsesoptimalisering med indekser**. God databaseadministrasjon er tett koblet til [[bruker-og-tilgangsstyring]] generelt og er en forutsetning for solid [[backup-og-gjenoppretting]] av systemene du drifter.

---

## Teori

### Brukertilgang i MySQL

MySQL håndterer tilgangskontroll i to steg:

1. **Autentisering** — kan brukeren koble til serveren? (riktig brukernavn og passord)
2. **Autorisering** — hva har brukeren lov til å gjøre? (hvilke databaser, tabeller og operasjoner)

#### Brukeridentifikasjon

I MySQL identifiseres en bruker alltid med kombinasjonen `'brukernavn'@'host'`. Det betyr at `app_bruker@'localhost'` og `app_bruker@'192.168.1.10'` er to forskjellige brukere, selv om de har samme navn. Dette er viktig for sikkerhet: du kan begrense hvilke maskiner som får koble til.

```sql
-- Opprett en bruker som kun kan koble fra localhost
CREATE USER 'app_bruker'@'localhost' IDENTIFIED BY 'SterkPassord123!';

-- Opprett en bruker som kan koble fra et helt subnett
CREATE USER 'rapport_bruker'@'192.168.1.%' IDENTIFIED BY 'AnnetPassord456!';
```

#### Tildele rettigheter med GRANT

```sql
-- Gi alle rettigheter til én database
GRANT ALL PRIVILEGES ON it_inventar.* TO 'app_bruker'@'localhost';

-- Gi kun leserettighet (SELECT)
GRANT SELECT ON it_inventar.* TO 'rapport_bruker'@'192.168.1.%';

-- Gi SELECT og INSERT på én bestemt tabell
GRANT SELECT, INSERT ON it_inventar.utstyr TO 'lager_bruker'@'localhost';

-- Aktiver endringene umiddelbart
FLUSH PRIVILEGES;
```

Vanlige privilegier:

| Privilegium | Hva det tillater |
|---|---|
| `SELECT` | Lese data |
| `INSERT` | Legge inn nye rader |
| `UPDATE` | Endre eksisterende rader |
| `DELETE` | Slette rader |
| `CREATE` | Opprette tabeller og databaser |
| `DROP` | Slette tabeller og databaser |
| `ALTER` | Endre tabellstruktur |
| `ALL PRIVILEGES` | Alle rettigheter |

#### Trekke tilbake rettigheter med REVOKE

```sql
-- Fjern INSERT-rettighet
REVOKE INSERT ON it_inventar.utstyr FROM 'lager_bruker'@'localhost';

-- Fjern alle rettigheter til en database
REVOKE ALL PRIVILEGES ON it_inventar.* FROM 'rapport_bruker'@'192.168.1.%';

FLUSH PRIVILEGES;
```

#### Vis gjeldende rettigheter

```sql
SHOW GRANTS FOR 'app_bruker'@'localhost';
```

#### Slett en bruker

```sql
DROP USER 'rapport_bruker'@'192.168.1.%';
```

#### Roller (MySQL 8.0+)

Fra MySQL 8.0 kan du bruke **roller** for å gruppere rettigheter og tildele dem til mange brukere på én gang — tilsvarende rollebasert tilgangskontroll (RBAC).

```sql
-- Opprett en rolle
CREATE ROLE 'les_inventar';

-- Tildel rettigheter til rollen
GRANT SELECT ON it_inventar.* TO 'les_inventar';

-- Tildel rollen til en bruker
GRANT 'les_inventar' TO 'vikar_bruker'@'localhost';

-- Aktiver rollen for brukeren
SET DEFAULT ROLE 'les_inventar' TO 'vikar_bruker'@'localhost';
```

Roller gjør det mye enklere å administrere tilganger når mange brukere skal ha samme rettigheter.

**Prinsippet om minste privilegium (Least Privilege):** Gi alltid brukere kun de rettighetene de absolutt trenger for å utføre sin oppgave. En applikasjonsbruker som kun leser data trenger ikke `DELETE` eller `DROP`. Dette begrenser skadeomfanget ved feil eller kompromittering.

---

### Backup med mysqldump

`mysqldump` er det enkleste verktøyet for å ta **logisk backup** av MySQL-databaser. Det eksporterer databasestrukturen og dataene som SQL-setninger som kan kjøres på nytt for å gjenopprette databasen.

Logisk backup er bærbar: du kan gjenopprette til en annen maskin, et annet operativsystem, eller en nyere versjon av MySQL.

#### Ta backup

```bash
# Backup av én database
mysqldump -u root -p it_inventar > it_inventar_backup.sql

# Backup med dato i filnavnet
mysqldump -u root -p it_inventar > "it_inventar_$(date +%Y-%m-%d).sql"

# Backup av alle databaser på serveren
mysqldump -u root -p --all-databases > alle_databaser_backup.sql

# Backup med komprimering (sparer diskplass)
mysqldump -u root -p it_inventar | gzip > it_inventar_backup.sql.gz
```

#### Gjenopprette fra backup

```bash
# Gjenopprett til en eksisterende database
mysql -u root -p it_inventar < it_inventar_backup.sql

# Opprett ny database og gjenopprett
mysql -u root -p -e "CREATE DATABASE it_inventar_restore;"
mysql -u root -p it_inventar_restore < it_inventar_backup.sql

# Gjenopprett fra komprimert backup
gunzip < it_inventar_backup.sql.gz | mysql -u root -p it_inventar
```

#### Planlegge automatisk backup med cron (Linux)

```bash
# Åpne crontab
crontab -e

# Kjør backup hver dag klokken 02:00
0 2 * * * mysqldump -u root -pDittPassord it_inventar > /backup/it_inventar_$(date +\%Y-\%m-\%d).sql
```

Backup-filer bør lagres på en separat disk eller ekstern lokasjon — en backup på samme disk som databasen er ikke en ekte backup.

**Test alltid gjenoppretting (Recovery Testing).** En backup du aldri har testet er ikke en backup du kan stole på. Sett av tid regelmessig til å gjenopprette til en testdatabase og verifiser at dataene er intakte. Se [[backup-og-gjenoppretting]] for generelle prinsipper som gjelder på tvers av systemer.

---

### Indekser og ytelsesoptimalisering

#### Hva er en indeks?

En indeks er en datastruktur (typisk et B-tre) som gjør oppslag i en kolonne raskere, på bekostning av litt mer diskplass og litt tregere innsetting/oppdatering. Primærnøkler og kolonner med `UNIQUE` får automatisk en indeks. Andre kolonner som brukes mye i `WHERE`-setninger bør du legge til manuelt.

```sql
-- Opprett en indeks på type-kolonnen
CREATE INDEX idx_type ON utstyr(type);

-- Opprett en indeks på to kolonner (sammensatt indeks)
CREATE INDEX idx_type_plassering ON utstyr(type, plassering);

-- Vis alle indekser på en tabell
SHOW INDEX FROM utstyr;

-- Slett en indeks
DROP INDEX idx_type ON utstyr;
```

#### EXPLAIN — analyser spørringer

`EXPLAIN` viser deg hvordan MySQL planlegger å utføre en spørring. Det er det viktigste verktøyet for å finne flaskehalser. Bruk alltid `EXPLAIN` før du legger til nye indekser — det hjelper deg forstå om en indeks faktisk trengs.

```sql
EXPLAIN SELECT * FROM utstyr WHERE type = 'PC';
```

Viktige kolonner i EXPLAIN-output:

| Kolonne | Hva det betyr |
|---|---|
| `type` | Typen oppslag: `ALL` = full tabellscan (dårlig), `ref`/`eq_ref` = indeksoppslag (bra) |
| `key` | Hvilken indeks som brukes (NULL betyr ingen indeks) |
| `rows` | Estimert antall rader MySQL må lese |
| `Extra` | Tilleggsinformasjon, f.eks. `Using filesort` (trenger sortering) eller `Using index` (bra) |

Eksempel på dårlig spørring (full scan):

```
type: ALL, key: NULL, rows: 10000
```

Etter å ha lagt til en indeks:

```
type: ref, key: idx_type, rows: 42
```

#### Sakte spørringslogg (Slow Query Log)

MySQL kan loggføre alle spørringer som tar lengre tid enn en definert grense. Dette er et verdifullt verktøy for å identifisere ytelsesflaskehalser i produksjonsmiljøer.

```sql
-- Se om slow query log er aktivert
SHOW VARIABLES LIKE 'slow_query_log%';

-- Aktiver i MySQL-konfigurasjon (/etc/mysql/my.cnf):
-- slow_query_log = 1
-- slow_query_log_file = /var/log/mysql/slow.log
-- long_query_time = 2
```

#### Praktiske ytelsestips

**Bruk riktige datatyper.** En `INT` er raskere enn en `VARCHAR` å søke i. Bruk `DATE` for datoer, ikke `VARCHAR`.

```sql
-- Dårlig: lagre datoer som tekst
ALTER TABLE utstyr ADD COLUMN kjopt_dato VARCHAR(20);

-- Bra: bruk DATE
ALTER TABLE utstyr ADD COLUMN kjopt_dato DATE;
```

**Unngå SELECT \* i produksjon.** Hent bare kolonnene du faktisk trenger.

```sql
-- Tregere: henter alle kolonner
SELECT * FROM utstyr WHERE type = 'PC';

-- Raskere: henter kun det som trengs
SELECT id, navn, serienummer FROM utstyr WHERE type = 'PC';
```

**Begrens resultatsett med LIMIT.**

```sql
SELECT * FROM logg ORDER BY tidspunkt DESC LIMIT 100;
```

**Indekser kolonner brukt i WHERE, JOIN og ORDER BY.** Disse er de vanligste flaskehalsene.

---

## Eksempel / lab

### Lab: Administrer brukertilgang og ta backup

**Steg 1: Opprett brukere med ulike rettigheter**

```sql
-- Driftspersonell: full tilgang
CREATE USER 'drifts_admin'@'localhost' IDENTIFIED BY 'Admin2024!';
GRANT ALL PRIVILEGES ON it_inventar.* TO 'drifts_admin'@'localhost';

-- Lærere: kun lese
CREATE USER 'laerer'@'localhost' IDENTIFIED BY 'Laerer2024!';
GRANT SELECT ON it_inventar.* TO 'laerer'@'localhost';

-- Applikasjonsbruker: lese og oppdatere, ikke slette
CREATE USER 'app'@'localhost' IDENTIFIED BY 'App2024!';
GRANT SELECT, INSERT, UPDATE ON it_inventar.* TO 'app'@'localhost';

FLUSH PRIVILEGES;
```

**Steg 2: Verifiser rettighetene**

```sql
SHOW GRANTS FOR 'laerer'@'localhost';
SHOW GRANTS FOR 'app'@'localhost';
```

**Steg 3: Ta backup fra terminalen**

```bash
mysqldump -u root -p it_inventar > it_inventar_backup.sql
```

**Steg 4: Sjekk at backup-filen inneholder SQL**

```bash
head -30 it_inventar_backup.sql
```

Du skal se CREATE TABLE- og INSERT-setninger.

**Steg 5: Test gjenoppretting**

```bash
mysql -u root -p -e "CREATE DATABASE it_inventar_test;"
mysql -u root -p it_inventar_test < it_inventar_backup.sql
mysql -u root -p -e "USE it_inventar_test; SELECT * FROM utstyr;"
```

**Steg 6: Legg til en indeks og bruk EXPLAIN**

```sql
-- Kjør EXPLAIN uten indeks
EXPLAIN SELECT * FROM utstyr WHERE type = 'PC';

-- Legg til indeks
CREATE INDEX idx_type ON utstyr(type);

-- Kjør EXPLAIN igjen og sammenlign
EXPLAIN SELECT * FROM utstyr WHERE type = 'PC';
```

---

## Study guide

### Databaseadministrasjon — kjerneinnhold

Databaseadministrasjon i MySQL handler om tre overordnede ansvarsområder som en driftstøtter møter i hverdagen.

**Brukertilgang og sikkerhet**
MySQL identifiserer brukere med kombinasjonen `'brukernavn'@'host'`, noe som gir finkornet kontroll over hvem som kobler til fra hvilken maskin. Tilgangskontroll skjer i to steg: autentisering (er det riktig bruker?) og autorisering (hva har de lov til?). Prinsippet om minste privilegium er avgjørende: gi aldri mer enn det som trengs. Fra MySQL 8.0 kan roller (RBAC) brukes til å forenkle administrasjon der mange brukere trenger samme rettigheter.

Sentrale kommandoer: `CREATE USER`, `GRANT`, `REVOKE`, `FLUSH PRIVILEGES`, `SHOW GRANTS`, `DROP USER`, `CREATE ROLE`.

**Backup og gjenoppretting**
`mysqldump` lager en logisk backup som SQL-setninger — portabel, leserbar og versjonsuavhengig. Backup bør automatiseres med cron og lagres utenfor databaseserveren. Like viktig som å ta backup er å *teste gjenoppretting* jevnlig. En utestet backup er ikke en pålitelig backup.

**Ytelsesoptimalisering**
Indekser (B-tre-strukturer) gjør oppslag dramatisk raskere i store tabeller, men koster litt ved innsetting og oppdatering. `EXPLAIN` er det primære verktøyet for å analysere spørringsplaner og finne manglende indekser. Full tabellscan (`type: ALL`) er tegn på at en indeks mangler. Slow Query Log hjelper deg oppdage flaskehalser i produksjon. Gode vaner: riktige datatyper, unngå `SELECT *`, bruk `LIMIT`.

**Sammenheng med andre emner**
Databaseadministrasjon bygger på prinsipper fra [[bruker-og-tilgangsstyring]] og er en del av det totale [[backup-og-gjenoppretting]]-ansvaret i en driftsorganisasjon. [[sql-grunnleggende]] gir grunnlaget for å forstå spørringene du optimaliserer.

---

## FAQ

**Hva er de to stadiene i MySQL sin tilgangskontroll?**
Autentisering (er brukernavn og passord riktig?) og autorisering (hva har denne brukeren lov til å gjøre?). Begge må godkjennes for at en operasjon skal gå gjennom.

**Hvorfor er formatet `'bruker'@'host'` viktig i MySQL?**
Fordi samme brukernavn fra ulike maskiner kan ha helt forskjellige rettigheter. `admin@localhost` og `admin@'192.168.1.5'` er separate kontoer. Dette gir presis kontroll over nettverkstilgang til databasen.

**Hva er prinsippet om minste privilegium, og hvorfor gjelder det databaser?**
Gi brukere kun de rettighetene de trenger for sin oppgave — ikke mer. En rapportbruker trenger `SELECT`, ikke `DELETE`. Hvis en konto kompromitteres eller en feil begås, begrenses skaden.

**Hva er forskjellen på logisk og fysisk backup?**
Logisk backup (mysqldump) eksporterer data som SQL-setninger — portabel og leserbar, men tregere å gjenopprette for store databaser. Fysisk backup kopierer de faktiske datafiler på disk — raskere gjenoppretting, men ikke nødvendigvis kompatibel på tvers av MySQL-versjoner.

**Hvorfor bør jeg teste gjenoppretting, ikke bare ta backup?**
En backup-fil kan være korrupt, ufullstendig eller skrevet feil. Hvis du aldri tester gjenoppretting, vet du ikke om den faktisk fungerer — det finner du ut i verste øyeblikk under en reell hendelse.

**Hva forteller `EXPLAIN` meg, og når bruker jeg det?**
EXPLAIN viser MySQL sin plan for å kjøre en spørring: hvilken indeks som brukes, antall estimerte rader som leses, og om det er full tabellscan. Bruk det når en spørring er treg, eller før du legger til en indeks, for å forstå hva som faktisk skjer.

**Hva er en sakte spørringslogg (Slow Query Log)?**
En MySQL-funksjon som logger alle spørringer som tar lengre tid enn en definert grense (f.eks. 2 sekunder). Uunnværlig i produksjon for å finne ytelsesflaskehalser uten å måtte overvåke manuelt.

**Hva er RBAC, og hvordan støtter MySQL det?**
Rollebasert tilgangskontroll (RBAC) betyr at rettigheter tildeles roller, og roller tildeles brukere — ikke rettigheter direkte til hver bruker. Fra MySQL 8.0 brukes `CREATE ROLE` og `GRANT rolle TO bruker`. Gjør det mye enklere å administrere mange brukere med like tilgangsbehov.

---

## Quiz

<details><summary>Spørsmål 1: Hva er de to stadiene i MySQL sin tilgangskontroll?</summary>

**Svar:** Autentisering (verifiserer hvem brukeren er — brukernavn og passord) og autorisering (bestemmer hva brukeren har lov til å gjøre — hvilke databaser, tabeller og operasjoner).

</details>

<details><summary>Spørsmål 2: Hvorfor bruker MySQL formatet 'brukernavn'@'host' for å identifisere brukere?</summary>

**Svar:** Fordi samme brukernavn fra ulike maskiner kan ha ulike rettigheter. `admin@'localhost'` og `admin@'192.168.1.5'` er to separate brukere med potensielt helt forskjellige tilganger. Dette gir finkornet kontroll over hvem som kan koble til fra hvor.

</details>

<details><summary>Spørsmål 3: Hva er forskjellen på logisk og fysisk backup?</summary>

**Svar:** Logisk backup (som mysqldump) eksporterer data som SQL-setninger — bærbar, leserbar og versjonsuavhengig. Fysisk backup kopierer de faktiske datafilene på disk — raskere å gjenopprette for store databaser, men ikke nødvendigvis kompatibel på tvers av versjoner.

</details>

<details><summary>Spørsmål 4: Hva forteller EXPLAIN deg, og når bruker du det?</summary>

**Svar:** EXPLAIN viser MySQL sin plan for å utføre en spørring — hvilken indeks som brukes, hvor mange rader som estimeres lest, og om det er full tabellscan. Du bruker det når en spørring er treg, for å finne ut om en indeks mangler eller om spørringen kan skrives mer effektivt.

</details>

<details><summary>Spørsmål 5: Hva skjer med eksisterende data hvis du gjenoppretter en mysqldump-backup til en database som allerede har tabeller?</summary>

**Svar:** mysqldump inkluderer som standard DROP TABLE IF EXISTS før CREATE TABLE, så eksisterende tabeller slettes og erstattes. Du mister data som var i databasen fra før. Bruk alltid en tom database eller en dedikert gjenopprettingsdatabase hvis du vil beholde eksisterende data.

</details>

---

## Flashcards

Autentisering :: Verifiserer hvem brukeren er — brukernavn og passord — første steg i MySQL-tilgangskontroll
Autorisering :: Bestemmer hva den autentiserte brukeren har lov til å gjøre — andre steg i MySQL-tilgangskontroll
GRANT :: MySQL-kommando for å tildele rettigheter til en bruker eller rolle
REVOKE :: MySQL-kommando for å fjerne rettigheter fra en bruker eller rolle
FLUSH PRIVILEGES :: Tvinger MySQL til å laste inn rettighetstabellene på nytt slik at endringer trer i kraft
mysqldump :: Kommandolinjeverktøy for logisk backup av MySQL-databaser — eksporterer SQL-setninger
Logisk backup :: Backup lagret som SQL-setninger (f.eks. mysqldump) — bærbar på tvers av versjoner og systemer
Indeks :: Datastruktur (typisk B-tre) som gjør oppslag i en kolonne raskere — opprettes med CREATE INDEX
EXPLAIN :: MySQL-kommando som viser spørringsplanen — brukes for å diagnostisere trege spørringer
RBAC :: Rollebasert tilgangskontroll — rettigheter tildeles roller, roller tildeles brukere
CREATE ROLE :: MySQL 8.0-kommando for å opprette en rolle som kan samle rettigheter
Full tabellscan :: MySQL leser alle rader i tabellen for å finne treff — indikert med type=ALL i EXPLAIN, unngås med indekser
Minste privilegium :: Sikkerhetsprinsipp — gi brukere kun de rettighetene de absolutt trenger for sin oppgave
Sakte spørringslogg :: MySQL-funksjon som logger spørringer over definert tidsgrense — brukes til å identifisere ytelsesflaskehalser
Indeksering :: Opprettelse av en datastruktur som fungerer som hurtigvei for søk og forbedrer ytelse ved store datamengder

---

## Ressurser

- [MySQL 8.0: Access Control](https://dev.mysql.com/doc/refman/8.0/en/access-control.html)
- [MySQL 8.0: Backup og recovery](https://dev.mysql.com/doc/refman/8.0/en/backup-and-recovery.html)
- [MySQL 8.0: Optimering](https://dev.mysql.com/doc/refman/8.0/en/optimization.html)
- [PostgreSQL: Backup og restore](https://www.postgresql.org/docs/current/backup.html)
- [NDLA: Databaseadministrasjon](https://ndla.no/subject:1:7e101f30-891d-4076-a70e-1100f9156475/topic:1:a6e7039a-5e1a-4c92-b05b-439f72765366/resource:73797690-3486-444c-bc6d-62725e173e97)
- [YouTube: MySQL Administration and User Management — Database Star (12 min)](https://www.youtube.com/watch?v=u96rS6Y236M)
