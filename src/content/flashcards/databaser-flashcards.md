# Database læringskort

## Card 1

**Q:**Hva er den grunnleggende definisjonen på en database?

**A:**En organisert samling av data som lagres elektronisk.

---

## Card 2

**Q:**Hva betyr begrepet 'persistens' i databasesammenheng?

**A:**At data overlever selv om systemet eller maskinen starter på nytt.

---

## Card 3

**Q:**Hva står forkortelsen DBMS for?

**A:**Database Management System (databasestyringssystem).

---

## Card 4

**Q:**Hva er rollen til et DBMS?

**A:**Programvare som administrerer lagring, sikkerhet og samtidig tilgang til data.

---

## Card 5

**Q:**Hva kalles strukturen som beskriver hvordan data er organisert i en database?

**A:**Et skjema (schema).

---

## Card 6

**Q:**Hva er Structured Query Language (SQL)?

**A:**Standardspråket som brukes for å kommunisere med relasjonsdatabaser.

---

## Card 7

**Q:**Hvilke to organisasjoner standardiserte SQL på 1980-tallet?

**A:**ANSI og ISO.

---

## Card 8

**Q:**Hvordan organiserer en relasjonsdatabase data?

**A:**I tabeller med rader og kolonner.

---

## Card 9

**Q:**Nevn tre alternative navn for en 'rad' i en databasetabell.

**A:**Post, record, tuppel, linje eller objekt.

---

## Card 10

**Q:**Hva kalles de navngitte verdiene som utgjør kolonnene i en tabell?

**A:**Attributter.

---

## Card 11

**Q:**Hva er formålet med en primærnøkkel (PRIMARY KEY)?

**A:**Å unikt identifisere hver enkelt rad i en tabell.

---

## Card 12

**Q:**Kan en primærnøkkel inneholde verdien NULL?

**A:**Nei, en primærnøkkel kan aldri være NULL.

---

## Card 13

**Q:**Hvor mange primærnøkler kan en enkelt tabell ha?

**A:**Maksimalt én.

---

## Card 14

**Q:**Hva er en fremmednøkkel (FOREIGN KEY)?

**A:**En kolonne som peker til primærnøkkelen i en annen tabell for å skape en relasjon.

---

## Card 15

**Q:**Kan en fremmednøkkel inneholde duplikate verdier?

**A:**Ja, en fremmednøkkel kan inneholde identiske verdier i flere rader.

---

## Card 16

**Q:**Hva kalles garantien for at en fremmednøkkel alltid peker til en eksisterende rad?

**A:**Referanseintegritet.

---

## Card 17

**Q:**Hva er en 'sammensatt primærnøkkel'?

**A:**En primærnøkkel som består av mer enn én kolonne.

---

## Card 18

**Q:**Hva er hovedforskjellen på SQL og NoSQL?

**A:**SQL er tabellbasert og strukturert, mens NoSQL er bedre egnet for ustrukturert eller varierende data.

---

## Card 19

**Q:**Hva står forkortelsen DDL for i SQL?

**A:**Data Definition Language.

---

## Card 20

**Q:**Hvilke tre hovedkommandoer tilhører DDL?

**A:**CREATE, ALTER og DROP.

---

## Card 21

**Q:**Hva står forkortelsen DML for i SQL?

**A:**Data Manipulation Language.

---

## Card 22

**Q:**Hvilke fire kommandoer utgjør CRUD-operasjonene i DML?

**A:**INSERT, SELECT, UPDATE og DELETE.

---

## Card 23

**Q:**Hva står forkortelsen DCL for?

**A:**Data Control Language.

---

## Card 24

**Q:**Hva brukes DCL-kommandoene GRANT og REVOKE til?

**A:**Administrasjon av brukertilganger og rettigheter.

---

## Card 25

**Q:**Hva skjer hvis man kjører kommandoen DELETE uten en WHERE-klausul?

**A:**Alle rader i tabellen blir slettet.

---

## Card 26

**Q:**Hvilken SQL-klausul brukes for å filtrere resultater basert på en betingelse?

**A:**WHERE.

---

## Card 27

**Q:**Hva gjør funksjonen AUTO_INCREMENT i MySQL?

**A:**Den tildeler automatisk neste ledige heltall som verdi for en primærnøkkel.

---

## Card 28

**Q:**Hva betyr begrensningen NOT NULL på en kolonne?

**A:**At feltet må inneholde en verdi og ikke kan stå tomt.

---

## Card 29

**Q:**Hva betyr det at en kolonne er markert som UNIQUE?

**A:**At alle verdiene i kolonnen må være forskjellige på tvers av alle rader.

---

## Card 30

**Q:**Hvilken operator brukes i SQL for mønstersøk i tekst (pattern matching)?

**A:**LIKE.

---

## Card 31

**Q:**Hvordan sorterer man et resultatsett i synkende rekkefølge?

**A:**Ved å legge til DESC etter kolonnenavnet i ORDER BY-klausulen.

---

## Card 32

**Q:**Hva er formålet med LIMIT-klausulen i en SELECT-spørring?

**A:**Å begrense antall rader som blir returnert i resultatet.

---

## Card 33

**Q:**Hva er forskjellen på INNER JOIN og LEFT JOIN?

**A:**INNER JOIN krever treff i begge tabeller, mens LEFT JOIN tar med alt fra venstre tabell uansett treff.

---

## Card 34

**Q:**Hva kalles det når man gir en tabell et midlertidig kortere navn i en spørring?

**A:**Tabell-alias (bruker nøkkelordet AS).

---

## Card 35

**Q:**Hvilken datatype brukes for tekst med fast lengde, som for eksempel et registreringsnummer?

**A:**CHAR.

---

## Card 36

**Q:**Hva er forskjellen på CHAR(n) og VARCHAR(n)?

**A:**CHAR bruker alltid fast plass (n tegn), mens VARCHAR bruker kun plassen teksten faktisk tar opptil maksgrensen n.

---

## Card 37

**Q:**Hvilken datatype brukes for å lagre store binære filer som bilder eller lyd i databasen?

**A:**BLOB (Binary Large Object).

---

## Card 38

**Q:**Hva er standardformatet for datatypen DATE i de fleste SQL-systemer?

**A:**ÅÅÅÅ-MM-DD.

---

## Card 39

**Q:**Beskriv en en-til-mange-relasjon (1:N) med et eksempel.

**A:**Én avdeling kan ha mange ansatte, men hver ansatt tilhører kun én avdeling.

---

## Card 40

**Q:**Hvordan løser man teknisk en mange-til-mange-relasjon (M:N) i en relasjonsdatabase?

**A:**Ved å bruke en koblingstabell med fremmednøkler til begge de involverte tabellene.

---

## Card 41

**Q:**Nevn et populært databasesystem som er dokumentbasert (NoSQL).

**A:**MongoDB.

---

## Card 42

**Q:**Hva er spesielt med databasesystemet SQLite sammenlignet med MySQL?

**A:**SQLite er serverløst og lagrer hele databasen som én enkelt fil.

---

## Card 43

**Q:**Hva er forskjellen på autentisering og autorisering?

**A:**Autentisering bekrefter hvem du er, mens autorisering bestemmer hva du har lov til å gjøre.

---

## Card 44

**Q:**Hvordan identifiseres en bruker i MySQL (format)?

**A:**'brukernavn'@'host' (f.eks. 'admin'@'localhost').

---

## Card 45

**Q:**Hva betyr 'Prinsippet om minste privilegium'?

**A:**At brukere kun skal tildeles de rettighetene de absolutt trenger for å utføre oppgaven sin.

---

## Card 46

**Q:**Hva er fordelen med å bruke 'Roller' (RBAC) i MySQL 8.0+?

**A:**Det gjør administrasjon enklere ved at man kan tildele rettigheter til en gruppe brukere samtidig.

---

## Card 47

**Q:**Hva er 'mysqldump'?

**A:**Et kommandolinjeverktøy som brukes til å ta logisk backup av en database.

---

## Card 48

**Q:**Hva kjennetegner en 'logisk backup'?

**A:**Dataene eksporteres som SQL-setninger som er portable og lesbare.

---

## Card 49

**Q:**Hva er en 'fysisk backup'?

**A:**En direkte kopi av databasens faktiske filer på harddisken.

---

## Card 50

**Q:**Hvorfor er det kritisk å utføre 'Recovery Testing'?

**A:**For å verifisere at backup-filene faktisk fungerer og kan brukes til gjenoppretting ved en krise.

---

## Card 51

**Q:**Hva er hovedformålet med å legge til en indeks på en tabell?

**A:**Å gjøre søk og oppslag i spesifikke kolonner betydelig raskere.

---

## Card 52

**Q:**Hva er den største ulempen med å ha for mange indekser?

**A:**Innsetting (INSERT) og oppdatering (UPDATE) av data går tregere fordi indeksen også må oppdateres.

---

## Card 53

**Q:**Hvilken datastruktur brukes vanligvis for indekser i MySQL?

**A:**B-tre (B-tree).

---

## Card 54

**Q:**Hva brukes SQL-kommandoen EXPLAIN til?

**A:**Å analysere hvordan MySQL planlegger å utføre en spørring for å finne ytelsesproblemer.

---

## Card 55

**Q:**Hva betyr det hvis EXPLAIN viser 'type: ALL'?

**A:**At MySQL må utføre en full tabellscan (lese alle rader), noe som er ineffektivt.

---

## Card 56

**Q:**Hva er en 'Slow Query Log'?

**A:**En funksjon som logger alle spørringer som tar lengre tid enn en spesifisert tidsgrense.

---

## Card 57

**Q:**Hva er formålet med normalisering i databasedesign?

**A:**Å organisere data for å unngå dobbeltlagring og sikre logisk struktur.

---

## Card 58

**Q:**Hva står ER-diagram for?

**A:**Entity Relationship-diagram.

---

## Card 59

**Q:**Hvilken lagringsmotor er standard i moderne MySQL og støtter transaksjoner?

**A:**InnoDB.

---

## Card 60

**Q:**Hva gjør kommandoen FLUSH PRIVILEGES?

**A:**Den tvinger MySQL til å laste inn rettighetstabellene på nytt umiddelbart.

---

## Card 61

**Q:**Hvorfor bør man unngå 'SELECT*' i produksjonssystemer?

**A:**Det kan gi dårligere ytelse og gjøre applikasjonen sårbar for endringer i tabellstrukturen.

---

## Card 62

**Q:**Hva betyr begrepet 'atomiske attributter' i relasjonsmodellen?

**A:**At hver kolonne i en rad kun skal inneholde én udelelig verdi.

---

## Card 63

**Q:**Hva er forskjellen på 'parent-tabell' og 'child-tabell' i en relasjon?

**A:**Parent-tabellen inneholder primærnøkkelen som child-tabellens fremmednøkkel peker til.

---

## Card 64

**Q:**Hvilken SQL-kommando brukes for å endre strukturen på en eksisterende tabell?

**A:**ALTER TABLE.

---

## Card 65

**Q:**Hva er MySQL Workbench?

**A:**Et visuelt verktøy for databasemodellering, SQL-utvikling og administrasjon.

---

## Card 66

**Q:**Nevn en vanlig NoSQL-databasetype som brukes til hurtigbuffer (caching).

**A:**Nøkkel-verdi-database (f.eks. Redis).

---

## Card 67

**Q:**Hva er 'MySQL Community Server'?

**A:**Gratisversjonen av MySQL med åpen kildekode.

---

## Card 68

**Q:**Hvorfor er formatet 'brukernavn'@'host' viktig for sikkerhet?

**A:**Det gjør det mulig å begrense tilgang slik at en bruker kun kan koble til fra en bestemt IP-adresse.

---

## Card 69

**Q:**I SQL-syntaks, hva skiller en kommando fra en annen dersom man kjører flere samtidig?

**A:**Semikolon (;).

---

## Card 70

**Q:**Hva er en 'transaksjon' i databasesammenheng?

**A:**En serie operasjoner som utføres som én udelelig enhet (enten blir alt utført, eller ingenting).

---

## Card 71

**Q:**Hvilken datatype ville du valgt for et felt som skal lagre prisen på en vare?

**A:**FLOAT eller DECIMAL.

---

## Card 72

**Q:**Hva kalles det når man planlegger en automatisk backup i Linux?

**A:**Cron-jobb.

---

## Card 73

**Q:**Hva er hovedformålet med å bruke SQL-aliaser (AS)?

**A:**Å gjøre kolonnenavn eller tabellnavn mer lesbare i resultatet eller spørringen.

---

## Card 74

**Q:**Hvilken SQL-kommando brukes for å fjerne en hel tabell og all dens data permanent?

**A:**DROP TABLE.

---

## Card 75

**Q:**Hva er den største fordelen med logisk backup (mysqldump) sammenlignet med fysisk kopi?

**A:**Den er uavhengig av operativsystem og MySQL-versjon (portabel).

---

## Card 76

**Q:**Hvilken klausul brukes for å gruppere rader som har samme verdier i spesifiserte kolonner?

**A:**GROUP BY.

---

## Card 77

**Q:**Hva er 'referanseintegritet' i praksis?

**A:**Det hindrer sletting av en rad i en overordnet tabell dersom det finnes rader i andre tabeller som peker til den.

---

## Card 78

**Q:**Hva kalles databasemotoren som ofte brukes for innebygde applikasjoner og mobilapper?

**A:**SQLite.

---

## Card 79

**Q:**Hva er forskjellen mellom 'NULL' og en tom streng ('') i en database?

**A:**NULL betyr at verdien er ukjent eller mangler, mens en tom streng er en kjent verdi med lengde null.

---

## Card 80

**Q:**Hvilken SQL-kommando brukes for å tildele rettigheter til en databasebruker?

**A:**GRANT.

---
