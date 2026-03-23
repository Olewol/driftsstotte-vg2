---
title: "SQL – grunnleggende"
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

SQL (Structured Query Language) er standardspråket for å kommunisere med relasjonsdatabaser. Det ble standardisert av ANSI i 1986 og ISO i 1987, og brukes i dag i MySQL, PostgreSQL, SQLite, Microsoft SQL Server og mange andre systemer. Selv om dialektene varierer litt, er kjernesyntaksen den samme overalt.

SQL er delt inn i tre hoveddeler:

- **DDL** (Data Definition Language) — opprette og endre struktur: `CREATE`, `ALTER`, `DROP`
- **DML** (Data Manipulation Language) — jobbe med data: `SELECT`, `INSERT`, `UPDATE`, `DELETE`
- **DCL** (Data Control Language) — tilgangskontroll: `GRANT`, `REVOKE`

I denne artikkelen fokuserer vi på DDL og DML — det du trenger for å bygge og bruke databaser i praksis.

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

`SELECT` er den mest brukte kommandoen i SQL.

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

---

## Ressurser

- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/default.asp)
- [W3Schools: SQL JOIN](https://www.w3schools.com/sql/sql_join.asp)
- [MySQL 8.0 offisiell tutorial](https://dev.mysql.com/doc/refman/8.0/en/tutorial.html)
- [NDLA: Legge inn data i en database](https://ndla.no/r/konseptutvikling-og-programmering-im-ikm-vg1/legge-inn-data-i-en-database/22e4bdf1fd)
