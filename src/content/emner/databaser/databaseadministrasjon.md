---
title: "Databaseadministrasjon"
emne: databaser
kompetansemaal:
  - km-04
kilder:
  - ndla
tags: []
flashcards: true
public: true
---

## Introduksjon

Databaseadministrasjon handler om å holde en databaseserver trygg, tilgjengelig og effektiv over tid. For en driftstøtter er dette daglig arbeid: du oppretter brukere, tildeler tilganger, tar backup, gjenoppretter data etter feil og sørger for at serveren ikke er for treg.

Denne artikkelen tar for seg tre kjerneområder i MySQL-administrasjon: **brukertilgang**, **backup og gjenoppretting**, og **ytelsesoptimalisering med indekser**.

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

`EXPLAIN` viser deg hvordan MySQL planlegger å utføre en spørring. Det er det viktigste verktøyet for å finne flaskehalser.

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

-- Applikasjonsbru ker: lese og oppdatere, ikke slette
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

---

## Ressurser

- [MySQL 8.0: Access Control](https://dev.mysql.com/doc/refman/8.0/en/access-control.html)
- [MySQL 8.0: Backup og recovery](https://dev.mysql.com/doc/refman/8.0/en/backup-and-recovery.html)
- [MySQL 8.0: Optimering](https://dev.mysql.com/doc/refman/8.0/en/optimization.html)
- [PostgreSQL: Backup og restore](https://www.postgresql.org/docs/current/backup.html)
