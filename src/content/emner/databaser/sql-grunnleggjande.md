---
title: SQL grunnleggende
public: true
emne: databaser
uke: [2, 3]
kompetansemaal: "opprette, drifte og administrere databaser"
tags: [sql, database, mysql, postgresql, relasjonsdatabase]
---

# SQL grunnleggende

SQL (Structured Query Language) er standardspråket for å arbeide med relasjonsdatabaser.

## Grunnleggende SQL-kommandoer

### Opprette og slette

```sql
-- Opprett database
CREATE DATABASE skule;

-- Opprett tabell
CREATE TABLE elevar (
  id     INT PRIMARY KEY AUTO_INCREMENT,
  namn   VARCHAR(100) NOT NULL,
  klasse VARCHAR(10),
  epost  VARCHAR(150) UNIQUE
);

-- Slett tabell
DROP TABLE elevar;
```

### Sette inn og oppdatere data

```sql
-- Sett inn rad
INSERT INTO elevar (namn, klasse, epost)
VALUES ('Ola Nordmann', 'VG2IT', 'ola@skule.no');

-- Oppdater rad
UPDATE elevar SET klasse = 'VG3IT' WHERE id = 1;

-- Slett rad
DELETE FROM elevar WHERE id = 1;
```

### Hente data

```sql
-- Hent alle
SELECT * FROM elevar;

-- Filtrer
SELECT namn, klasse FROM elevar WHERE klasse = 'VG2IT';

-- Sorter
SELECT * FROM elevar ORDER BY namn ASC;

-- Grupper
SELECT klasse, COUNT(*) AS tal FROM elevar GROUP BY klasse;
```

## Relasjoner mellom tabeller

```sql
-- Fremmednøkkel (foreign key)
CREATE TABLE karakterar (
  id       INT PRIMARY KEY AUTO_INCREMENT,
  elev_id  INT,
  fag      VARCHAR(50),
  karakter INT,
  FOREIGN KEY (elev_id) REFERENCES elevar(id)
);

-- JOIN — hent data fra flere tabeller
SELECT e.namn, k.fag, k.karakter
FROM elevar e
JOIN karakterar k ON e.id = k.elev_id;
```
