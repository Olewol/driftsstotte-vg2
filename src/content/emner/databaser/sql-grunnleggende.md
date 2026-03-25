---
title: "SQL – grunnleggende"
emne: databaser
kompetansemaal:
  - km-04
kilder:
  - ndla
  - https://www.w3schools.com/sql/default.asp
  - https://dev.mysql.com/doc/refman/8.0/en/tutorial.html
notebooklm: true
tags: []
flashcards: https://notebooklm.google.com/notebook/e9134332-9a2e-4991-9a72-2807660c7610
public: true
---

## Introduksjon

SQL (Structured Query Language) er standardspråket for å kommunisere med relasjonsdatabaser. Det ble standardisert av ANSI i 1986 og ISO i 1987, og brukes i dag i MySQL, PostgreSQL, SQLite, Microsoft SQL Server og mange andre systemer. Selv om dialektene varierer litt, er kjernesyntaksen den samme overalt.

SQL er delt inn i tre hoveddeler:

- **DDL** (Data Definition Language) — opprette og endre struktur: `CREATE`, `ALTER`, `DROP`
- **DML** (Data Manipulation Language) — jobbe med data: `SELECT`, `INSERT`, `UPDATE`, `DELETE`
- **DCL** (Data Control Language) — tilgangskontroll: `GRANT`, `REVOKE`

I denne artikkelen fokuserer vi på DDL og DML — det du trenger for å bygge og bruke databaser i praksis. De fire kjerneoperasjonene INSERT, SELECT, UPDATE og DELETE kalles samlet **CRUD** (Create, Read, Update, Delete). Tilgangskontroll med DCL er dekket i [[databaseadministrasjon]].

---

## Teori

### Tabeller, rader og kolonner

En SQL-database er bygd opp av tabeller. Hver tabell har et fast sett med **kolonner** (felt) som definerer strukturen, og varierende antall **rader** (records) som er selve dataene.

```sql
CREATE TABLE utstyr (
  id          INT PRIMARY KEY AUTO_INCREMENT,
  navn        VARCHAR(100) NOT NULL,
  type        VARCHAR(50),
  serienummer VARCHAR(50) UNIQUE,
  plassering  VARCHAR(100)
);
```

Her er `id` satt til `PRIMARY KEY` og `AUTO_INCREMENT`, noe som betyr at MySQL automatisk tildeler et unikt tall for hver ny rad. `NOT NULL` betyr at feltet er påkrevd. `UNIQUE` betyr at ingen to rader kan ha samme verdi i det feltet.

### Primærnøkkel og fremmednøkkel

En **primærnøkkel** (PRIMARY KEY) identifiserer én rad unikt i tabellen. Den kan ikke være NULL og kan ikke ha duplikater.

En **fremmednøkkel** (FOREIGN KEY) peker til primærnøkkelen i en annen tabell og skaper en relasjon mellom tabellene. Fremmednøkkelen sikrer **referanseintegritet** — du kan ikke legge inn en fremmednøkkelverdi som ikke finnes i kildetabellen.

```sql
CREATE TABLE rom (
  id   INT PRIMARY KEY AUTO_INCREMENT,
  navn VARCHAR(50) NOT NULL
);

CREATE TABLE utstyr (
  id          INT PRIMARY KEY AUTO_INCREMENT,
  navn        VARCHAR(100) NOT NULL,
  type        VARCHAR(50),
  serienummer VARCHAR(50) UNIQUE,
  rom_id      INT,
  FOREIGN KEY (rom_id) REFERENCES rom(id)
);
```

Viktig: når du setter inn data med fremmednøkkel, må **parent-tabellen** (`rom`) ha data før du kan sette inn i **child-tabellen** (`utstyr`).

### SELECT — hente data

`SELECT` er den mest brukte kommandoen i SQL. Dette er **R** i CRUD — lese (Read) data.

```sql
-- Hent alle kolonner fra utstyr
SELECT * FROM utstyr;

-- Hent kun navn og plassering
SELECT navn, plassering FROM utstyr;

-- Filtrer med WHERE
SELECT * FROM utstyr WHERE type = 'PC';

-- Sorter resultatet
SELECT * FROM utstyr ORDER BY navn ASC;

-- Begrens antall rader
SELECT * FROM utstyr LIMIT 10;

-- Kombiner betingelser
SELECT * FROM utstyr
WHERE type = 'PC'
  AND plassering = 'Rom 201'
ORDER BY navn ASC
LIMIT 5;
```

`WHERE` støtter sammenligningsoperatorer (`=`, `<>`, `<`, `>`, `<=`, `>=`), logiske operatorer (`AND`, `OR`, `NOT`), og mønstersøk med `LIKE`:

```sql
-- Finn alt utstyr med serienummer som starter med 'SN'
SELECT * FROM utstyr WHERE serienummer LIKE 'SN%';

-- Finn utstyr uten registrert plassering
SELECT * FROM utstyr WHERE plassering IS NULL;
```

**Tips:** Unngå `SELECT *` i produksjon og applikasjoner — spesifiser alltid kolonnenavn for bedre ytelse og forutsigbarhet. Se [[databaseadministrasjon]] for mer om ytelsesoptimalisering.

### INSERT — legge inn data

```sql
INSERT INTO utstyr (navn, type, serienummer, plassering)
VALUES ('Dell OptiPlex 7090', 'PC', 'SN123456', 'Rom 201');

-- Sett inn flere rader på én gang
INSERT INTO utstyr (navn, type, serienummer, plassering)
VALUES
  ('HP LaserJet Pro', 'Skriver', 'SN789012', 'Rom 201'),
  ('Cisco Switch 2960', 'Nettverksutstyr', 'SN345678', 'Serverrom');
```

### UPDATE — oppdatere data

```sql
-- Oppdater plasseringen for ett bestemt utstyr
UPDATE utstyr
SET plassering = 'Rom 202'
WHERE id = 1;

-- Oppdater flere felter samtidig
UPDATE utstyr
SET plassering = 'Rom 301', type = 'Stasjonær PC'
WHERE serienummer = 'SN123456';
```

**Advarsel:** Alltid bruk `WHERE` med `UPDATE`. Uten `WHERE` oppdateres alle rader i tabellen.

### DELETE — slette data

```sql
-- Slett én rad
DELETE FROM utstyr WHERE id = 3;

-- Slett alle PC-er fra ett rom
DELETE FROM utstyr
WHERE type = 'PC' AND plassering = 'Rom 201';
```

**Advarsel:** Også her — `DELETE` uten `WHERE` sletter alle rader i tabellen.

### Tabell-aliaser for lesbarhet

Når du jobber med JOIN og lange tabellnavn, er det god praksis å bruke aliaser for å gjøre SQL-koden kortere og mer oversiktlig:

```sql
-- Uten alias (verbose)
SELECT utstyr.navn, utstyr.type, rom.navn AS rom_navn
FROM utstyr INNER JOIN rom ON utstyr.rom_id = rom.id;

-- Med alias (ryddigere)
SELECT u.navn, u.type, r.navn AS rom_navn
FROM utstyr AS u
INNER JOIN rom AS r ON u.rom_id = r.id;
```

### JOIN — kombinere tabeller

JOIN brukes til å hente data fra to eller flere tabeller basert på en relasjon mellom dem.

#### INNER JOIN

Returnerer kun rader som har treff i **begge** tabeller.

```sql
SELECT utstyr.navn, utstyr.type, rom.navn AS rom_navn
FROM utstyr
INNER JOIN rom ON utstyr.rom_id = rom.id;
```

Resultat: kun utstyr som er koblet til et rom.

#### LEFT JOIN

Returnerer **alle rader fra venstre tabell**, pluss matchende rader fra høyre. Rader uten match får `NULL` i høyre kolonne.

```sql
SELECT utstyr.navn, utstyr.type, rom.navn AS rom_navn
FROM utstyr
LEFT JOIN rom ON utstyr.rom_id = rom.id;
```

Resultat: alt utstyr vises, også utstyr som ikke er koblet til noe rom (`rom_navn` blir da `NULL`).

**Tommelfingerregel:** Bruk `INNER JOIN` når du kun vil ha komplette relasjoner. Bruk `LEFT JOIN` når du vil beholde alle rader fra én tabell selv om det ikke finnes en match.

---

## Eksempel / lab

### Lab: Bygg en IT-inventardatabase

I denne labben lager du en enkel database for å holde oversikt over IT-utstyr på skolen.

**Steg 1: Opprett databasen og velg den**

```sql
CREATE DATABASE it_inventar;
USE it_inventar;
```

**Steg 2: Opprett tabellen for rom**

```sql
CREATE TABLE rom (
  id   INT PRIMARY KEY AUTO_INCREMENT,
  navn VARCHAR(50) NOT NULL
);
```

**Steg 3: Opprett utstyr-tabellen med fremmednøkkel**

```sql
CREATE TABLE utstyr (
  id          INT PRIMARY KEY AUTO_INCREMENT,
  navn        VARCHAR(100) NOT NULL,
  type        VARCHAR(50),
  serienummer VARCHAR(50) UNIQUE,
  plassering  VARCHAR(100),
  rom_id      INT,
  FOREIGN KEY (rom_id) REFERENCES rom(id)
);
```

**Steg 4: Legg inn testdata**

```sql
INSERT INTO rom (navn) VALUES ('Rom 201'), ('Rom 202'), ('Serverrom');

INSERT INTO utstyr (navn, type, serienummer, plassering, rom_id)
VALUES
  ('Dell OptiPlex 7090', 'PC', 'SN123456', 'Rom 201', 1),
  ('HP LaserJet Pro', 'Skriver', 'SN789012', 'Rom 201', 1),
  ('Cisco Switch 2960', 'Nettverksutstyr', 'SN345678', 'Serverrom', 3),
  ('Lenovo ThinkPad E15', 'Laptop', 'SN901234', 'Rom 202', 2),
  ('Dell OptiPlex 3090', 'PC', 'SN567890', 'Rom 202', 2);
```

**Steg 5: Kjør spørringer**

```sql
-- Vis alt PC-utstyr
SELECT * FROM utstyr WHERE type = 'PC';

-- Vis utstyr med romnavn (INNER JOIN)
SELECT utstyr.navn, utstyr.type, utstyr.serienummer, rom.navn AS rom_navn
FROM utstyr
INNER JOIN rom ON utstyr.rom_id = rom.id
ORDER BY rom.navn, utstyr.navn;

-- Tell antall enheter per type
SELECT type, COUNT(*) AS antall
FROM utstyr
GROUP BY type
ORDER BY antall DESC;

-- Vis alt utstyr, inkludert utstyr uten rom (LEFT JOIN)
SELECT utstyr.navn, utstyr.type, rom.navn AS rom_navn
FROM utstyr
LEFT JOIN rom ON utstyr.rom_id = rom.id;
```

**Steg 6: Oppdater og rydd**

```sql
-- Flytt en laptop til serverrommet
UPDATE utstyr SET rom_id = 3, plassering = 'Serverrom'
WHERE serienummer = 'SN901234';

-- Slett et gammelt utstyr
DELETE FROM utstyr WHERE serienummer = 'SN567890';
```

---

## Study guide

### SQL grunnleggende — kjerneinnhold

SQL er standardspråket for relasjonsdatabaser og deles i tre kategorier: DDL (struktur), DML (data) og DCL (tilgang). VG2 IT fokuserer primært på DDL og DML.

**Tabellstruktur og nøkler**
Tabeller består av kolonner (struktur) og rader (data). Primærnøkkelen identifiserer hver rad unikt og kan ikke være NULL. Fremmednøkkelen kobler tabeller sammen og sikrer referanseintegritet — du kan ikke peke til en rad som ikke finnes. `AUTO_INCREMENT` gjør at MySQL tildeler primærnøkkelverdi automatisk.

**CRUD — de fire kjerneoperasjonene**
- `INSERT` — legg til nye rader (Create)
- `SELECT` — hent og filtrer data (Read)
- `UPDATE` — endre eksisterende rader (Update)
- `DELETE` — fjern rader (Delete)

Kritisk regel for `UPDATE` og `DELETE`: bruk alltid `WHERE`. Uten `WHERE` påvirkes alle rader i tabellen — en vanlig og farlig feil.

**SELECT og filtrering**
`WHERE` filtrerer rader med sammenligningsoperatorer, `AND`/`OR`/`NOT`, og `LIKE` for mønstersøk. `ORDER BY` sorterer, `LIMIT` begrenser antall rader. Unngå `SELECT *` — spesifiser kolonner eksplisitt.

**JOIN — kombinere tabeller**
`INNER JOIN` gir kun rader med treff i begge tabeller. `LEFT JOIN` gir alle rader fra venstre tabell, med `NULL` der høyre tabell mangler treff. Bruk aliaser (`AS u`, `AS r`) for mer lesbar kode ved JOIN med mange tabeller.

**Sammenheng med andre emner**
SQL-kunnskapene fra denne artikkelen brukes aktivt i [[databaseadministrasjon]] der du optimaliserer spørringer med indekser og `EXPLAIN`. DCL-delen av SQL (GRANT, REVOKE) er dekket der.

---

## FAQ

**Hva betyr CRUD?**
Create, Read, Update, Delete — de fire grunnleggende operasjonene for datamanipulering. I SQL tilsvarer dette INSERT, SELECT, UPDATE og DELETE.

**Hva er forskjellen på en primærnøkkel og en fremmednøkkel?**
En primærnøkkel identifiserer én rad unikt i sin egen tabell og kan ikke være NULL. En fremmednøkkel er en kolonne i én tabell som peker til primærnøkkelen i en annen tabell, og brukes til å knytte tabeller sammen.

**Hva skjer hvis du kjører UPDATE eller DELETE uten WHERE?**
Alle rader i tabellen påvirkes. Ved `UPDATE` endres alle rader til den nye verdien. Ved `DELETE` slettes alle rader. Bruk alltid `WHERE` for å begrense hvilke rader som endres — dette er en av de vanligste og farligste feilene i SQL.

**Hva er forskjellen på INNER JOIN og LEFT JOIN?**
`INNER JOIN` returnerer kun rader som har treff i begge tabeller. `LEFT JOIN` returnerer alle rader fra venstre tabell og fyller inn `NULL` for kolonner fra høyre tabell der det ikke finnes et treff.

**Hva betyr AUTO_INCREMENT i en kolonnedefinisjon?**
MySQL tildeler automatisk neste ledige heltall som verdi når en ny rad settes inn, uten at du trenger å angi verdien manuelt. Brukes typisk på primærnøkkelkolonner av typen INT.

**Hvorfor må du sette inn data i parent-tabellen før child-tabellen ved bruk av fremmednøkler?**
Fremmednøkkelen sikrer referanseintegritet — verdien i fremmednøkkelkolonnen må finnes som primærnøkkel i parent-tabellen. Hvis parent-raden ikke eksisterer, vil MySQL avvise innsettingen med en feilmelding.

**Hva er tabell-aliaser, og hvorfor bør jeg bruke dem?**
Aliaser (`FROM utstyr AS u`) gir tabeller kortere navn i en spørring. De gjør SQL-koden mer lesbar og mindre feilutsatt, spesielt ved JOIN med flere tabeller der du ellers må skrive fullt tabellnavn mange ganger.

**Hva er en spørring (query)?**
En forespørsel skrevet i SQL for å hente, filtrere eller endre spesifikke data i databasesystemet. `SELECT * FROM utstyr WHERE type = 'PC'` er et eksempel på en spørring som henter alle PC-er fra utstyr-tabellen.

---

## Quiz

<details><summary>Spørsmål 1: Hva er forskjellen på en primærnøkkel og en fremmednøkkel?</summary>

**Svar:** En primærnøkkel identifiserer én rad unikt i sin egen tabell og kan ikke være NULL. En fremmednøkkel er en kolonne i én tabell som peker til primærnøkkelen i en annen tabell, og brukes til å knytte tabeller sammen.

</details>

<details><summary>Spørsmål 2: Hva skjer hvis du kjører UPDATE uten WHERE?</summary>

**Svar:** Alle rader i tabellen oppdateres med den nye verdien. Dette er en vanlig og farlig feil — bruk alltid WHERE for å begrense hvilke rader som endres.

</details>

<details><summary>Spørsmål 3: Hva er forskjellen på INNER JOIN og LEFT JOIN?</summary>

**Svar:** INNER JOIN returnerer kun rader som har treff i begge tabeller. LEFT JOIN returnerer alle rader fra venstre tabell, og fyller inn NULL for kolonner fra høyre tabell der det ikke finnes et treff.

</details>

<details><summary>Spørsmål 4: Hva betyr AUTO_INCREMENT i en kolonnedefinisjon?</summary>

**Svar:** MySQL tildeler automatisk neste ledige heltall som verdi når en ny rad settes inn, uten at du trenger å angi verdien manuelt. Brukes typisk på primærnøkkelkolonner av typen INT.

</details>

<details><summary>Spørsmål 5: Hvorfor må du sette inn data i parent-tabellen før child-tabellen ved bruk av fremmednøkler?</summary>

**Svar:** Fremmednøkkelen sikrer referanseintegritet — verdien i fremmednøkkelkolonnen må finnes som primærnøkkel i parent-tabellen. Hvis parent-raden ikke eksisterer, vil MySQL avvise innsettingen med en feilmelding.

</details>

---

## Flashcards

SQL :: Standardspråk for å kommunisere med relasjonsdatabaser (ANSI 1986, ISO 1987)
DDL :: Data Definition Language — kommandoer som CREATE, ALTER og DROP som endrer databasestruktur
DML :: Data Manipulation Language — kommandoer som SELECT, INSERT, UPDATE og DELETE som jobber med data
Primærnøkkel :: En kolonne (eller kombinasjon) som unikt identifiserer hver rad i en tabell — kan ikke være NULL
Fremmednøkkel :: En kolonne som peker til primærnøkkelen i en annen tabell og skaper en relasjon mellom tabellene
Referanseintegritet :: Garantien om at en fremmednøkkelverdi alltid peker til en eksisterende rad i den refererte tabellen
AUTO_INCREMENT :: MySQL-funksjon som automatisk tildeler neste ledige heltall til en kolonne ved innsetting
INNER JOIN :: Kombinerer rader fra to tabeller der det finnes treff i begge — rader uten treff ekskluderes
LEFT JOIN :: Returnerer alle rader fra venstre tabell og matchende rader fra høyre — NULL der det ikke er treff
WHERE :: Klausul som filtrerer hvilke rader som påvirkes av en SELECT, UPDATE eller DELETE
ORDER BY :: Klausul som sorterer resultatet av en SELECT, ASC = stigende, DESC = synkende
LIMIT :: Klausul som begrenser antall rader returnert av en SELECT
CRUD :: Create, Read, Update, Delete — de fire grunnleggende dataoperasjonene, tilsvarer INSERT, SELECT, UPDATE, DELETE i SQL
Spørring (Query) :: En forespørsel i SQL for å hente, filtrere eller endre data i databasesystemet
Tabell-alias :: Kortform for et tabellnavn i en spørring (f.eks. FROM utstyr AS u) — gjør JOIN-kode mer lesbar

---

## Ressurser

- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/default.asp)
- [W3Schools: SQL JOIN](https://www.w3schools.com/sql/sql_join.asp)
- [MySQL 8.0 offisiell tutorial](https://dev.mysql.com/doc/refman/8.0/en/tutorial.html)
- [NDLA: Legge inn data i en database](https://ndla.no/r/konseptutvikling-og-programmering-im-ikm-vg1/legge-inn-data-i-en-database/22e4bdf1fd)
