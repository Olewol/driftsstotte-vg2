---
title: "Backup og gjenoppretting"
emne: it-drift
kompetansemaal:
  - km-01
kilder:
  - ndla
  - https://nsm.no/fagomrader/digital-sikkerhet/grunnprinsipper-for-ikt-sikkerhet-2-0/oppdage-og-handtere-hendelser/sikre-og-gjenopprette-data/
video: https://www.youtube.com/watch?v=iL8Lp8w0UIs
tags: []
flashcards: https://notebooklm.google.com/notebook/bc9a5656-7a9b-4dc5-a59e-ef4a96aa8ccd
public: true
notebooklm: true
---

## Introduksjon

Data er en av de mest verdifulle ressursene en virksomhet har. Uten fungerende backup kan én hendelse – en harddisk som feiler, et ransomware-angrep eller en brann – føre til permanent tap av kritisk informasjon.

Backup handler ikke bare om å ta kopier. Det handler om å ha en strategi som sikrer at data kan gjenopprettes raskt nok og med lavt nok datatap til at virksomheten overlever hendelsen. En backup er kun verdifull hvis den faktisk kan gjenopprettes. I tillegg bør backup-strategien inkludere systemkonfigurasjoner og master-images, ikke bare rådata – slik at hele infrastrukturen kan gjenopprettes, ikke bare filene.

---

## Teori

### 3-2-1-regelen

3-2-1-regelen er den enkleste og mest anerkjente retningslinjen for backup-strategi:

- **3** – Ha minst 3 kopier av data (1 primær + 2 backup)
- **2** – Lagre på minst 2 ulike medietyper (f.eks. intern disk + ekstern disk eller NAS)
- **1** – Ha minst 1 kopi lagret offsite (utenfor bygningen – f.eks. i skyen eller i et annet lokale)

Offsite-kopien beskytter mot fysiske hendelser som brann, flom eller innbrudd som kan ødelegge alt lokalt utstyr.

#### Moderne utvidelse: 3-2-1-1-0

Veeam og andre eksperter anbefaler en utvidet versjon:

- **+1** – Ha én immutable (uforanderlig) eller air-gapped kopi som ikke kan slettes av ransomware
- **+0** – Null feil ved gjenopprettingstesting (automatisk verifisering av backup)

Immutable backup betyr at data er låst og ikke kan endres eller slettes i en periode. AWS S3 Object Lock er ett eksempel på dette. Air-gapped backup er isolert fra nettverket, slik at angripere ikke kan nå den.

---

### Backupstrategier

Det finnes tre hovedtyper backup. Valget avhenger av RPO, lagringskapasitet og gjenopprettingstid.

#### Full backup

En komplett kopi av alle valgte data. Tar lengst tid og krever mest lagringsplass, men er enklest å gjenopprette fra.

- Fordeler: enkel og rask gjenoppretting, fullstendig datasett
- Ulemper: krever mye lagringsplass og tid, uhensiktsmessig å kjøre daglig

#### Inkrementell backup

Tar kun en kopi av data som har endret seg siden **siste backup** (uansett type – full eller inkrementell).

- Fordeler: rask og lagringsvennlig, liten datastørrelse per backup
- Ulemper: gjenoppretting krever den siste fulle backup + alle påfølgende inkrementelle backuper – tidkrevende og sårbart for feil i kjeden

#### Differensiell backup

Tar en kopi av alt som har endret seg siden **siste fulle backup**.

- Fordeler: raskere gjenoppretting enn inkrementell (kun full backup + én differensiell)
- Ulemper: vokser i størrelse for hvert pass frem til neste fulle backup

| Type | Lagringsbruk | Backuptid | Gjenopprettingstid |
|------|-------------|-----------|-------------------|
| Full | Størst | Lengst | Kortest |
| Differensiell | Medium (vokser) | Medium | Medium |
| Inkrementell | Minst | Kortest | Lengst |

---

### RPO og RTO

To begreper er avgjørende for å designe en backup-strategi:

**RPO – Recovery Point Objective**
> "The maximum acceptable amount of data loss measured in time." – Microsoft Azure

RPO svarer på: *Hvor mye data har vi råd til å miste?*

Eksempel: Hvis en virksomhet har RPO på 4 timer, betyr det at data fra de siste 4 timene kan gå tapt uten at det er kritisk. Backup må da kjøres minst hvert 4. time.

**RTO – Recovery Time Objective**
> "The maximum acceptable time to restore business operations after a disaster occurs." – Microsoft Azure

RTO svarer på: *Hvor lenge kan vi ha nedetid?*

Eksempel: Dersom RTO er 2 timer, må IT-teamet ha systemene oppe igjen innen 2 timer etter en hendelse.

#### Praktisk eksempel

En skole lagrer elevdata og karaktersystemer:
- **RPO: 24 timer** – karakterer kan ikke mates inn på nytt lenger tilbake enn én dag
- **RTO: 8 timer** – systemet må være oppe igjen innen én arbeidsdag

Løsning: daglig full backup lagret lokalt og i sky, med klart gjenopprettingsprosedyre dokumentert og testet.

---

### Backup-verktøy

**Windows Server Backup**
Innebygget verktøy i Windows Server. Greit for enkle backupoppsett, men begrenset funksjonalitet for komplekse miljøer.

**Veeam Backup & Replication**
Industristandard for virtualiserte miljøer (VMware, Hyper-V). Støtter inkrementell backup, verifisering og gjenoppretting ned til enkeltfiler. Mye brukt i norske bedrifter.

**Azure Backup**
Microsofts skybaserte backup-tjeneste. Enkel å sette opp for Azure VM-er og Windows Server. Støtter offsite-lagring naturlig.

**AWS S3 + Glacier**
Amazon S3 brukes for aktiv backup-lagring; Glacier er et billigere arkivlagringsalternativ for data som sjelden trengs men må bevares.

---

### Automatisering av backup

Manuell backup er utsatt for menneskelig svikt – den som er syk den dagen backupen skal kjøres, glemmer det, eller hopper over det «for én gangs skyld». Automatiserte backup-rutiner eliminerer denne risikoen.

Gode praksiser for automatisert backup:
- Planlegg backup-jobber utenfor arbeidstid (f.eks. kl. 02:00) for lavt påvirkning på systemer
- Konfigurer automatisk varsling ved feil i backup-jobben
- Bruk skriptbasert backup (f.eks. [[powershell-grunnleggende]]) for tilpassede behov
- Logg alle backup-resultater og oppbevar loggene separat fra backup-systemet

---

### Gjenopprettingstesting

En backup som aldri er testet, er en backup man ikke kan stole på. Gjenopprettingstesting bør:

- Gjennomføres regelmessig (månedlig eller kvartalsvis)
- Inkludere faktisk gjenoppretting til et testmiljø – ikke bare sjekk av at filene finnes
- Dokumenteres med resultat, dato og hvem som utførte testen
- Verifisere at systemet fungerer etter gjenoppretting (ikke bare at data er på plass)

Veeam og Azure Backup støtter automatisk verifisering (SureBackup / Instant Restore) som del av backup-prosessen.

---

### Katastrofegjenoppretting (Disaster Recovery)

Disaster Recovery (DR) er en bredere plan for hva som skjer hvis store deler av infrastrukturen feiler. DR-strategi inkluderer:

- **Cold standby** – backup-infrastruktur som settes opp manuelt ved behov. Billig, men lang RTO.
- **Warm standby** – et delvis ferdigkonfigurert miljø som kan aktiveres raskt.
- **Hot standby / active-passive** – et fullstendig parallelt miljø som alltid er klart. Laveste RTO, men dyrest.

DR-planen skal dokumenteres og øves regelmessig. Se [[dokumentasjon-og-planlegging]] for maler og prosedyredokumentasjon.

---

## Eksempel / lab

**Oppgave: Lag en backup-plan for en fiktiv skole**

Gitt: En skole med 500 elever, karaktersystem, filserver og e-post.

1. Definer RPO og RTO for hvert av systemene (karaktersystem, filserver, e-post).
2. Velg backup-strategi (full/inkrementell/differensiell) og frekvens for hvert system.
3. Beskriv hvor backupene lagres (lokalt, NAS, sky) – vurder 3-2-1-regelen.
4. Lag en enkel gjenopprettingsprosedyre for filserveren (steg-for-steg).

**Tilleggsoppgave: Vurder hva som inngår i backup**

Diskuter: Bør en backup kun inneholde datafiler, eller bør den også inkludere systemkonfigurasjon, brukerlister og nettverksinnstillinger? Hva er fordelen med et fullstendig system-image kontra en fil-for-fil-backup?

---

## Study guide

### Kjerneinnhold

Backup og gjenoppretting handler om å sikre at data kan gjenopprettes ved tap eller feil – og at dette faktisk fungerer i praksis.

**3-2-1-regelen (og 3-2-1-1-0):**
- 3 kopier, 2 medier, 1 offsite
- + 1 immutable/air-gapped, + 0 feil i testing
- Beskytter mot fysiske hendelser OG ransomware

**Backupstrategier:**
- Full: størst, enklest å gjenopprette
- Inkrementell: minst, raskest å kjøre, kompleks å gjenopprette
- Differensiell: midt imellom – enkel gjenoppretting (full + én diff)

**RPO og RTO:**
- RPO = maks akseptabelt datatap i tid (bestemmer backup-frekvens)
- RTO = maks akseptabel nedetid (bestemmer krav til gjenopprettingshastighet)

**DR-strategier:**
- Cold standby (billigst, lengst RTO) → Warm standby → Hot standby (dyrest, korteste RTO)

**Nøkkelprinsipp:** Backup som ikke testes jevnlig er ikke pålitelig. Test, dokumenter, repeter.

---

## FAQ

**Hva er forskjellen på backup og archive?**
Backup er kopier av aktive data som du vil kunne gjenopprette raskt. Archive (arkiv) er data som ikke lenger er i aktiv bruk, men som må bevares over lang tid (f.eks. for lovkrav). AWS Glacier er et arkivlagringsprodukt – det er ikke egnet som primær backup.

**Kan vi bruke RAID som backup?**
Nei. RAID beskytter mot diskfeil, ikke mot feil sletting, ransomware eller brann. RAID er redundans, ikke backup. Begge deler trengs i en komplett strategi.

**Hva er en immutable backup i praksis?**
Det er backup-data som er låst av systemet slik at ingen kan endre eller slette den i en definert periode (f.eks. 30 dager). AWS S3 Object Lock og Azure Immutable Blob Storage er eksempler. Selv om en ransomware-angriper får tilgang til backup-systemet, kan de ikke slette eller kryptere immutable data.

**Hva er air-gap og er det praktisk i en skole?**
Air-gap betyr at backup-mediet er fysisk frakoblet nettverket. En offline harddisk eller et tapemedium i et annet rom er air-gapped. Det er praktisk og rimelig for skoler – men krever rutiner for regelmessig oppdatering.

**Hvor ofte bør vi teste backup?**
Minimum kvartalsvis for fullstendig gjenopprettingstest. Mange velger månedlig for kritiske systemer. Viktigst er at testen faktisk verifiserer at systemet fungerer etter gjenoppretting – ikke bare at filene er tilgjengelige.

**Hva er forskjellen på RPO og RTO med et eksempel?**
RPO: "Vi tåler å miste maks 4 timers data." – Backup må kjøres minst hvert 4. time. RTO: "Systemet må være oppe igjen innen 2 timer." – Gjenopprettingsprosessen og infrastrukturen må dimensjoneres for dette. Et karaktersystem for en skole kan ha RPO 24t og RTO 8t; et nettbanksystem kan ha RPO 0 (ingen tap) og RTO 15 min.

---

## Quiz

<details><summary>Spørsmål 1: Hva betyr 3-2-1-regelen?</summary>

**Svar:** 3 kopier av data, lagret på 2 ulike medietyper, der 1 kopi er offsite (utenfor bygningen). Sikrer mot lokale katastrofer og mediesvikt.

</details>

<details><summary>Spørsmål 2: Hva er forskjellen på RPO og RTO?</summary>

**Svar:** RPO (Recovery Point Objective) er maksimalt akseptabelt datatap målt i tid – altså hvor gammel en gjenopprettet backup kan være. RTO (Recovery Time Objective) er maksimalt akseptabel nedetid – altså hvor lang tid det tar å gjenopprette systemet.

</details>

<details><summary>Spørsmål 3: Hva er forskjellen på inkrementell og differensiell backup?</summary>

**Svar:** Inkrementell backup tar kun endringer siden forrige backup (uansett type). Differensiell backup tar alle endringer siden siste fulle backup. Inkrementell er mer lagringseffektiv, men gjenoppretting er mer kompleks. Differensiell er enklere å gjenopprette fra.

</details>

<details><summary>Spørsmål 4: Hva er en immutable backup og hvorfor er den viktig mot ransomware?</summary>

**Svar:** En immutable backup er låst og kan ikke endres eller slettes i en definert periode. Dette gjør at ransomware ikke kan kryptere eller slette backup-dataene, selv om angriperne får tilgang til backup-systemet.

</details>

<details><summary>Spørsmål 5: Hvorfor er det viktig å teste backup regelmessig?</summary>

**Svar:** En backup garanterer ingenting før den er testet. Filer kan være korrupte, backup-programvaren kan ha feil, eller gjenopprettingsprosessen kan ta lengre tid enn RTO tillater. Regelmessig testing avdekker disse problemene før de oppstår i en reell krisesituasjon.

</details>

---

## Flashcards

3-2-1-regelen :: 3 kopier av data, 2 ulike lagringsmedier, 1 offsite-kopi. Standard minstekrav for backup-strategi.

RPO :: Recovery Point Objective – maksimalt akseptabelt datatap målt i tid. Bestemmer backup-frekvens.

RTO :: Recovery Time Objective – maksimalt akseptabel nedetid. Bestemmer krav til gjenopprettingshastighet.

Full backup :: Komplett kopi av alle valgte data. Størst lagringsbruk, raskest å gjenopprette.

Inkrementell backup :: Kopi av endringer siden siste backup (uansett type). Liten og rask, men kompleks gjenoppretting.

Differensiell backup :: Kopi av alle endringer siden siste fulle backup. Middels størrelse og gjenopprettingstid.

Immutable backup :: Backup-data som er låst og ikke kan endres eller slettes. Beskytter mot ransomware.

Air-gapped backup :: Backup isolert fra nettverket. Angripere kan ikke nå den digitalt.

Disaster Recovery (DR) :: Helhetlig plan for å gjenopprette IT-systemer etter en større katastrofe.

Veeam :: Ledende backup-programvare for virtualiserte miljøer. Støtter VMware, Hyper-V og skybackup.

Cold standby :: DR-strategi der backup-infrastruktur settes opp manuelt ved behov. Billigst, lengst RTO.

Hot standby :: DR-strategi med fullstendig parallelt miljø klart hele tiden. Kortest RTO, dyrest.

System-image :: Komplett kopi av et operativsystem med konfigurasjon og programvare. Raskere totalrestaurering enn fil-for-fil.

---

## Ressurser

- [Veeam: 3-2-1 Backup Rule](https://www.veeam.com/blog/321-backup-rule.html)
- [Microsoft Azure Well-Architected: Disaster Recovery](https://learn.microsoft.com/en-us/azure/well-architected/reliability/disaster-recovery)
- [NSM: Sikre og gjenopprette data](https://nsm.no/fagomrader/digital-sikkerhet/grunnprinsipper-for-ikt-sikkerhet-2-0/oppdage-og-handtere-hendelser/sikre-og-gjenopprette-data/)
- [YouTube: 3-2-1-regelen for backup – NetNordic](https://www.youtube.com/watch?v=iL8Lp8w0UIs)
- [[driftsarkitektur]]
- [[dokumentasjon-og-planlegging]]
