---
title: "Databaser – oversikt"
emne: databaser
kompetansemaal: []
kilder:
  - ndla
tags: []
flashcards: false
public: true
---

## Introduksjon

En database er en organisert samling av data som lagres elektronisk og kan hentes frem, oppdateres og analyseres på en effektiv måte. I motsetning til å lagre informasjon i tekstfiler eller regneark gir en database strukturert og vedvarende lagring — data overlever selv om systemet starter på nytt. Dette kalles **persistens**.

I IT-drift møter du databaser overalt: brukerregistre, nettverksinventar, loggdata, billettingssystemer og konfigurasjonsdatabaser er alle eksempler. Å forstå hvordan databaser fungerer gir deg et solid grunnlag for å drifte, feilsøke og sikre tjenestene du er ansvarlig for.

---

## Teori

### Hva er en database?

En database består av:

- **Data** — selve informasjonen som lagres
- **Et databasesystem (DBMS)** — programvaren som administrerer databasen (MySQL, PostgreSQL, SQLite, MongoDB)
- **Et skjema (schema)** — strukturen som beskriver hvordan data er organisert

Et **DBMS** (Database Management System) håndterer lagring, sikkerhet, samtidig tilgang fra flere brukere, og sikrer at data er konsistente. Du kommuniserer med DBMS-et via et spørrespråk — for relasjonsdatabaser er det SQL.

### Relasjonsdatabaser (SQL)

Relasjonsdatabaser organiserer data i **tabeller** med rader og kolonner, inspirert av matematisk mengdelære (relasjoner). Tabeller kan knyttes sammen via **nøkler**.

Nøkkelbegreper:

| Begrep | Forklaring |
|---|---|
| **Tabell** | En samling rader med samme kolonnestruktur |
| **Rad (record)** | Én enkelt oppføring i tabellen |
| **Kolonne (felt)** | En bestemt type informasjon, f.eks. `navn` eller `ip_adresse` |
| **Primærnøkkel** | En kolonne som unikt identifiserer hver rad (f.eks. `id`) |
| **Fremmednøkkel** | En kolonne som peker til primærnøkkelen i en annen tabell |
| **Indeks** | En datastruktur som gjør oppslag raskere |

Relasjoner mellom tabeller kan være:
- **En-til-mange (1:N)** — én avdeling har mange ansatte
- **Mange-til-mange (M:N)** — en student kan ta mange kurs, et kurs kan ha mange studenter (løses med en koblingstabell)

### NoSQL

NoSQL-databaser bryter med den tabellbaserte strukturen og er bedre egnet når data er ustrukturert, varierende eller svært voluminøst. Vanlige typer:

| Type | Eksempel-system | Bruksområde |
|---|---|---|
| Dokument | MongoDB | JSON-lignende dokumenter, fleksibelt skjema |
| Nøkkel-verdi | Redis | Hurtigbuffer, sesjonsdata |
| Kolonnebasert | Apache Cassandra | Enorme datamengder, distribusjon |
| Graf | Neo4j | Sosiale nettverk, anbefalingssystemer |

### Populære systemer

| System | Type | Lisens | Typisk bruk |
|---|---|---|---|
| **MySQL** | Relasjonell | GPL / kommersiell | Webapplikasjoner, LAMP-stack |
| **PostgreSQL** | Relasjonell | BSD (fri) | Komplekse spørringer, geo-data, bedrift |
| **SQLite** | Relasjonell | Fri | Innebygd i applikasjoner, testing |
| **MongoDB** | NoSQL (dokument) | SSPL / kommersiell | Fleksible datamodeller, sky |
| **MariaDB** | Relasjonell | GPL | MySQL-kompatibel fork, ofte i Linux |

I norsk skole og næringsliv er MySQL og PostgreSQL de mest brukte. SQLite er praktisk for lokal testing siden det ikke krever noen serverinstallasjon — hele databasen er én fil.

### Databaser i IT-drift

Som driftstøtter vil du typisk:

- Administrere brukertilganger (hvem kan lese, skrive og slette)
- Ta backup og gjenopprette databaser
- Overvåke ytelse og diagnostisere trege spørringer
- Installere og konfigurere databaseservere
- Feilsøke tilkoblingsproblemer

Du trenger sjelden å designe store databaser fra bunnen, men du må kunne lese databasestruktur, kjøre vedlikeholdsoperasjoner og forstå hva som kan gå galt.

---

## Les videre

- [[sql-grunnleggende]] — SQL-spørringer, tabeller, nøkler og JOIN
- [[databaseadministrasjon]] — brukertilgang, backup, indekser og ytelse

---

## Ressurser

- [NDLA: Hva er en database?](https://ndla.no/r/konseptutvikling-og-programmering-im-ikm-vg1/hva-er-en-database/babda54d1b)
- [NDLA: Funksjoner i en database](https://ndla.no/r/konseptutvikling-og-programmering-im-ikm-vg1/funksjoner-i-en-database/75559ad075)
- [MySQL 8.0 offisiell tutorial](https://dev.mysql.com/doc/refman/8.0/en/tutorial.html)
- [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html)
