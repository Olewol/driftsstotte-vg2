---
title: "Dokumentasjon og planlegging"
emne: it-drift
kompetansemaal:
  - km-06
kilder:
  - ndla
tags: []
flashcards: true
public: true
---

## Introduksjon

God dokumentasjon er ryggraden i profesjonell IT-drift. Uten oppdatert dokumentasjon er det umulig å feilsøke effektivt, vanskelig å lære opp nye medarbeidere, og risikabelt å gjøre endringer i systemet.

Dokumentasjon og planlegging handler om å ha oversikt: over hva som finnes, hvordan det henger sammen, hva som er gjort, og hva som skal gjøres. Dette er kompetansemål km-06 – en av de mest praktiske delene av faget.

---

## Teori

### Hvorfor dokumentere?

Dokumentasjon tjener flere formål i IT-drift:

- **Feilsøking** – vet vi hva som er normal konfigurasjon, er det lettere å finne avvik
- **Onboarding** – ny kollega eller vikar kan ta over uten å starte fra null
- **Revisjoner og compliance** – myndigheter og kunder kan kreve dokumentasjon (f.eks. etter GDPR)
- **Endringstyring** – sporing av hva som er endret, hvem som endret det og hvorfor
- **Kontinuitet** – virksomheten er ikke avhengig av én person som bærer all kunnskap i hodet

Digdir understreker at god dokumentasjon er grunnlaget for interoperabilitet i norsk offentlig sektor.

---

### Nettverkstopologier

En nettverkstopologi beskriver hvordan noder (enheter) er koblet sammen i et nettverk.

#### Stjernetopologi (vanligst)

Alle enheter kobler seg til en sentral svitsj eller ruter. Enkel å feilsøke (isoler kabelen til den defekte enheten) og enkel å utvide.

```
      [PC]
       |
[PC]--[Svitsj]--[PC]
       |
      [Server]
```

- Fordeler: enkel, feiltolerант (én enhet feiler uten å påvirke andre), lett å utvide
- Ulemper: svitsjen er et single point of failure (avhjelpes med redundante svitsjer)

#### Mesh-topologi

Alle noder er koblet til alle andre noder (full mesh) eller til mange andre (partial mesh). Brukes i WAN-nett og robuste kritiske systemer.

```
[A]---[B]
 | \ / |
 | X  |
 |/ \ |
[C]---[D]
```

- Fordeler: ekstremt robust – mange alternative veier
- Ulemper: dyr og kompleks

#### Busstopologi (historisk)

Alle enheter koblet til én felles kabel (bus). Brukes ikke lenger i moderne nettverk, men kjennes igjen fra eldre Ethernet-standarder.

---

### IP-adresseplan

En IP-adresseplan er en strukturert oversikt over alle IP-adresser, subnett og tilhørende informasjon i nettverket. Den er et kritisk planleggings- og driftsdokument.

#### Eksempel: IP-adresseplan for et skolenettverk

**Nettverksinfo:** 192.168.1.0/24 (254 brukbare adresser)

| VLAN | Navn | Subnett | Nettadresse | Gateway | DNS | DHCP-område | Kommentar |
|------|------|---------|-------------|---------|-----|-------------|-----------|
| 10 | Administrasjon | /26 | 192.168.1.0 | 192.168.1.1 | 192.168.1.10 | .20–.62 | 42 adresser til ansatte |
| 20 | Elever | /25 | 192.168.1.128 | 192.168.1.129 | 192.168.1.10 | .140–.253 | 114 adresser, BYOD |
| 30 | Servere | /27 | 192.168.1.64 | 192.168.1.65 | 192.168.1.66 | Statisk | Filserver, AD, backup |
| 40 | Gjest/IoT | /27 | 192.168.1.96 | 192.168.1.97 | 8.8.8.8 | .100–.126 | Isolert, kun internett |

**Statiske adresser (utvalg):**

| Enhet | IP-adresse | MAC-adresse | Lokasjon |
|-------|-----------|-------------|----------|
| Brannmur (WAN-grensesnitt) | 10.0.0.1 | – | Server-rom |
| Kjernesvitsj | 192.168.1.2 | aa:bb:cc:dd:ee:01 | Server-rom |
| Active Directory / DNS | 192.168.1.10 | aa:bb:cc:dd:ee:10 | Server-rom |
| Filserver | 192.168.1.11 | aa:bb:cc:dd:ee:11 | Server-rom |
| NAS (backup) | 192.168.1.12 | aa:bb:cc:dd:ee:12 | Server-rom |
| Printer, 1. etasje | 192.168.1.50 | aa:bb:cc:dd:ee:50 | Rom 101 |

---

### Driftslogg og endringslogg

En driftslogg (change log) er en kronologisk registrering av alle endringer som er gjort i IT-miljøet. Det er kanskje det viktigste enkeltdokumentet i en driftsorganisasjon.

#### Format

Loggen bør inneholde:
- **Dato og klokkeslett** – når ble endringen gjort?
- **Utført av** – hvem gjorde det?
- **Hva ble gjort** – konkret beskrivelse av endringen
- **Hvorfor** – årsak/begrunnelse
- **Resultat** – ble det som forventet? Noen problemer?
- **Saksnummer / ticket** – referanse til helpdesk-saken om det er relevant

#### Eksempel på endringslogg

| Dato | Utført av | Endring | Årsak | Resultat |
|------|-----------|---------|-------|---------|
| 2025-11-12 08:30 | Erik H. | Oppdaterte Windows Server 2022 til KB5043050 | Månedlig patchrunde | OK, server startet normalt |
| 2025-11-14 14:00 | Sara L. | Lagt til ny PC (HP EliteBook) i AD, VLAN 20 | Ny elev | Funger, DHCP-leie bekreftet |
| 2025-11-15 09:15 | Erik H. | Endret DHCP-område for VLAN 20: .140–.200 → .140–.253 | Kapasitetsbehov | OK, ny rekkevidde aktiv |

---

### Prosedyredokumentasjon

Kritiske operasjoner bør dokumenteres som steg-for-steg prosedyrer. Dette sikrer at operasjonen kan utføres av hvem som helst i teamet – ikke bare den som opprinnelig satte det opp.

**Eksempel: Prosedyre for månedlig backup-test**

```
Tittel: Månedlig gjenopprettingstest av filserver-backup
Ansvarlig rolle: Systemadministrator
Frekvens: Hver 1. mandag i måneden

Steg:
1. Logg inn på Veeam Backup & Replication.
2. Naviger til siste fulle backup av FILESERVER01.
3. Høyreklikk → «Instant Recovery» → velg isolert test-nettverk.
4. Start gjenoppretting og vent til VM er tilgjengelig (ca. 5 min).
5. Logg inn på den gjenopprettede VM og verifiser:
   a. At tjenestene (fileshare, DNS) kjører.
   b. At en tilfeldig valgt fil fra siste uke er tilgjengelig og lesbar.
6. Dokumenter resultatet i driftsloggen.
7. Slå av test-VM.

Forventet resultat: VM starter, filer tilgjengelige, ingen feil.
```

---

### Verktøy for dokumentasjon

| Verktøy | Bruksområde |
|---------|-------------|
| **draw.io / Lucidchart** | Nettverkstopologier, arkitekturdiagrammer |
| **Markdown / Obsidian** | Driftslogg, prosedyrer, intern wiki |
| **Confluence** | Teambasert wiki, brukt i store IT-avdelinger |
| **IT Glue** | Profesjonelt MSP-verktøy for IT-dokumentasjon. Integrerer passordhåndtering, enhetsregister og prosedyrer. |
| **CMDB** | Configuration Management Database – register over all IT-infrastruktur (enheter, konfigurasjon, relasjoner) |
| **Excel/Google Sheets** | IP-adresseplaner og inventarlister (enkel, men ikke skalerbar) |

---

### Planlegging av IT-løsninger

God planlegging reduserer risiko og gjør prosjektet mer forutsigbart. En enkel planleggingsprosess kan se slik ut:

1. **Behovskartlegging** – hva ønsker virksomheten å oppnå?
2. **Kravspesifikasjon** – tekniske og funksjonelle krav
3. **Risikovurdering (ROS-analyse)** – hva kan gå galt, og hva er konsekvensen?
4. **Løsningsforslag og valg** – vurder alternativer
5. **Prosjektplan** – tidsplan, ansvar, milepæler
6. **Implementering og testing**
7. **Dokumentasjon og overlevering**
8. **Evaluering** – ble kravene oppfylt?

---

## Eksempel / lab

### Systematisk feilsøking i 5 steg

> **Kilde:** Klasseromsnotater (2ITA)
>
> Når noe stopper opp, ikke få panikk. Gå systematisk til verks med disse stegene:
>
> 1. **Observer** – Hva skjer (og hva skjer ikke)? Les hele feilmeldingen, ikke bare de første ordene.
> 2. **Analyser** – Hva var det siste som fungerte? Hvilken endring ble gjort rett før feilen? Ofte ligger feilen der.
> 3. **Still hypoteser** – Hva trenger datamaskinen for å gjøre dette? Test hypotesen med konkrete kommandoer (f.eks. `ping 8.8.8.8` for å teste nettverkstilgang).
> 4. **Bruk verktøy og les feilmeldingen** – Vanlige mønstre:
>    - `Permission denied` → glemt `sudo`
>    - `Could not resolve host` → nettverk eller DNS-problem
>    - `No such file or directory` → feil filnavn eller feil mappe (sjekk med `ls`)
> 5. **Søk etter kunnskap** – Kopier hele feilmeldingen (uten brukernavn) til Google eller en AI. Gi alltid kontekst: OS-versjon, hva du prøver å gjøre, og hva som skjer.
>
> Dokumenter alltid løsningen i loggen din — det er gull verdt neste gang samme problem oppstår.

**Oppgave: Lag IP-adresseplan for et skolenettverk**

Gitt: Skole med 80 elever, 20 ansatte, 3 servere, 2 printere og et gjestenettverk.

1. Velg et passende privat IP-adresserom (f.eks. 10.10.0.0/24 eller 192.168.10.0/24).
2. Definer minst 3 VLAN (f.eks. ansatte, elever, servere).
3. Beregn subnett-størrelser basert på antall enheter.
4. Fyll inn en tabell med: VLAN-nr, navn, subnett, gateway, DNS, DHCP-område.
5. Angi statiske adresser for servrene.
6. Tegn en enkel topologi i draw.io som viser VLAN-strukturen.

---

## Quiz

<details><summary>Spørsmål 1: Hvorfor er en endringslogg viktig i IT-drift?</summary>

**Svar:** Endringsloggen gir en historikk over alle endringer som er gjort i systemet. Dette er uunnværlig ved feilsøking (hva endret vi rett før problemet oppsto?), revisjoner, onboarding av ny kollega og for å opprettholde kontinuitet når folk slutter.

</details>

<details><summary>Spørsmål 2: Hva er en stjernetopologi og hva er dens svakhet?</summary>

**Svar:** En stjernetopologi kobler alle enheter til en sentral svitsj. Det er enkelt å feilsøke og utvide. Svakheten er at svitsjen er et single point of failure – feiler svitsjen, mister alle enheter kontakten. Dette avhjelpes med redundante svitsjer.

</details>

<details><summary>Spørsmål 3: Hva skal en IP-adresseplan inneholde?</summary>

**Svar:** En IP-adresseplan skal minst inneholde: nettverksadresse og subnettmaske, gateway-adresse, DNS-server(e), DHCP-område, og oversikt over statiske adresser (servere, printere, nettverksutstyr). Den kan også inkludere VLAN-informasjon og MAC-adresser.

</details>

<details><summary>Spørsmål 4: Hva er CMDB?</summary>

**Svar:** CMDB (Configuration Management Database) er et register over all IT-infrastruktur i en virksomhet: enheter, programvare, konfigurasjoner og relasjonene mellom dem. Det er grunnlaget for god endringstyring og feilsøking.

</details>

<details><summary>Spørsmål 5: Nevn to verktøy som brukes til nettverksdokumentasjon og beskriv hva de brukes til.</summary>

**Svar:** draw.io brukes til å tegne nettverkstopologier og arkitekturdiagrammer – visuelt og gratis. IT Glue er et profesjonelt dokumentasjonsverktøy brukt av driftsselskaper (MSP-er) som samler alt fra passordhåndtering til prosedyrer og enhetsregister i ett system.

</details>

---

## Flashcards

Nettverkstopologi :: Beskrivelse av hvordan noder er koblet sammen i et nettverk. Eksempler: stjerne, mesh, buss.

Stjernetopologi :: Alle enheter koblet til en sentral svitsj. Enkel og vanligst i moderne nettverk.

IP-adresseplan :: Strukturert oversikt over IP-adresser, subnett, gateway og DNS i et nettverk.

Subnett :: En del av et IP-nettverk adskilt ved hjelp av subnettmaske. Brukes for VLAN-segmentering og adressering.

VLAN :: Virtual LAN – logisk nettverksegmentering. Enheter i samme VLAN kommuniserer som om de er på samme fysiske nettverk.

Driftslogg :: Kronologisk logg over alle endringer i IT-miljøet. Brukes til feilsøking, revisjon og kontinuitet.

CMDB :: Configuration Management Database – register over all IT-infrastruktur og konfigurasjoner.

draw.io :: Gratis, nettbasert verktøy for tegning av nettverkstopologier og arkitekturdiagrammer.

IT Glue :: Profesjonelt dokumentasjonsverktøy for IT-driftsselskaper. Samler dokumentasjon, passord og enhetsinformasjon.

Prosedyredokumentasjon :: Steg-for-steg instrukser for kritiske IT-operasjoner. Sikrer at hvem som helst kan utføre oppgaven.

ROS-analyse :: Risiko- og sårbarhetsanalyse. Brukes i planleggingsfasen for å identifisere og vurdere risiko.

---

## Ressurser

- [Digdir: Referansearkitektur for datadeling](https://www.digdir.no/nasjonal-arkitektur/referansearkitektur-for-datadeling/2131)
- [draw.io (diagramtegning)](https://app.diagrams.net/)
- [[driftsarkitektur]]
- [[backup-og-gjenoppretting]]
