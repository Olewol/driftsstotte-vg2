---
title: "KM-06: Dokumentasjon og planlegging / Documentation and Planning"
emne: kompetansemaal
kompetansemaal:
  - km-06
kilder:
  - https://www.udir.no/lk20/itk02-01/kompetansemaal-og-vurdering/kv372
  - https://www.digdir.no/informasjonssikkerhet/
  - https://www.itil.org/
  - https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/
tags: [km-06, dokumentasjon, planlegging, arbeidsprosesser]
flashcards: false
public: true
---

# KM-06: Dokumentasjon og planlegging / Documentation and Planning

## 🎯 Mål / Competency Goal

**Norsk:** Planlegge og dokumentere arbeidsprosesser og IT-løsninger

**English:** Plan and document work processes and IT solutions

---

## 📘 Forklaring / Explanation

### Norsk
Dokumentasjon er «bruksanvisningen» for IT-systemer. Uten dokumentasjon blir systemer avhengige av enkeltpersoners kunnskap — det kalles «bus factor» (hva skjer om den ene personen blir borte?)[^1][^2].

**God dokumentasjon bør inneholde:**
- **Systemoversikt** — Hvilke systemer finnes og hvordan henger de sammen?
- **Installasjonsveiledning** — Hvordan settes systemet opp?
- **Driftsrutiner** — Hvordan starte, stoppe og overvåke?
- **Feilsøkingsguide** — Hva gjør vi når noe går galt?
- **Nedetidsplan** — Hva gjør vi ved strømbrudd, brann eller cyberangrep?

**Planleggingsmetodikk:**[^4]
- **ITIL** — Beste praksis for IT-tjenestehåndtering
- **PDCA (Plan-Do-Check-Act)** — Sirkulær forbedringsprosess
- **Tidsestimering** — Å kunne anslå hvor lang tid oppgaver tar

### English
Documentation is the "instruction manual" for IT systems. Without documentation, systems depend on individual knowledge — this is called the "bus factor" (what happens if that one person leaves?)[^1][^2].

**Good documentation should include:**
- **System overview** — What systems exist and how do they connect?
- **Installation guide** — How is the system set up?
- **Operations procedures** — How to start, stop, and monitor?
- **Troubleshooting guide** — What do we do when something goes wrong?
- **Disaster recovery plan** — What do we do during power outages, fires, or cyberattacks?

**Planning methodology:**[^4]
- **ITIL** — Best practice for IT service management
- **PDCA (Plan-Do-Check-Act)** — Continuous improvement cycle
- **Time estimation** — Being able to estimate how long tasks will take

---

## 💡 Eksempler / Examples

### Norsk

**Eksempel 1: Planlegge ny server**
IT-avdelingen skal sette opp en ny filserver. De lager en plan: kravspesifikasjon → velge maskinvare → installere OS → konfigurere delinger → teste → dokumentere. Hvert steg dokumenteres.

**Eksempel 2: Driftshåndbok**
En skole har en driftshåndbok med instrukser for daglig oppstart av servere, ukentlig backup-sjekk, og hva lærere skal gjøre når projektoren ikke virker. Håndboken oppdateres hvert år.

### English

**Example 1: Planning a New Server**
IT plans to set up a new file server. They create a plan: requirements specification → choose hardware → install OS → configure shares → test → document. Each step is documented.

**Example 2: Operations Manual**
A school has an operations manual with instructions for daily server startup, weekly backup checks, and what teachers should do when the projector doesn't work. The manual is updated yearly.

---

## 📝 Oppsummering / Summary

| Norsk | English |
|-------|---------|
| Dokumentasjon er «bruksanvisningen» for IT | Documentation is the "instruction manual" for IT |
| Planlegging reduserer feil og sparer tid | Planning reduces errors and saves time |
| God dokumentasjon gjør systemet uavhengig av enkeltpersoner | Good documentation makes systems independent of individuals |
| ITIL er bransjestandard for IT-tjenestehåndtering | ITIL is the industry standard for IT service management |

---

## 🔧 Bridging Exercises / Praksisoppgaver

### Norsk — Praksisoppgaver

**Oppgave 1: Lag en feilsøkingsguide for skolens IT**
Eleven skal dokumentere en feilsøkingsguide for 5 vanlige IT-problemer på skolen:
1. Eleven får ikke logget på PC-en (glemt passord / konto låst)
2. Projektoren viser ikke bilde (kabel / kildevalg / driver)
3. Skriveren fungerer ikke (tomt blekk / papirstopp / driver)
4. Trådløst nettverk fungerer ikke (feil passord / signal / AP nede)
5. Nettverksstasjonen (hjemmeområde) er utilgjengelig
- For hvert problem: Symptomer → Mulige årsaker → Trinn-for-trinn feilsøking → Løsning → Når kontakte IT-avdelingen
- Skriv i et format som en lærer uten IT-bakgrunn kan følge

**Oppgave 2: Planlegg en serverflytting**
Skolen skal flytte en filserver fra serverrommet til et datasenter.
- Lag en prosjektplan med følgende faser:
  1. Kartlegging (hva kjører på serveren, avhengigheter, kapasitet)
  2. Planlegging (ny maskinvare/skytjeneste, tidslinje, risikoanalyse)
  3. Forberedelse (backup, testmiljø, kommunikasjon til brukere)
  4. Migrering (nedetidsvindu, datakopiering, testing)
  5. Etterarbeid (verifisering, dokumentasjon, dekommisjonering)
- For hver fase: beskriv oppgaver, ansvarlig, tidsestimat, risiko, kvalitetskontroll
- Inkluder en rollback-plan hvis migreringen feiler

**Veiledning / Solution Guidelines:**
- Oppgave 1: God feilsøkingsguide har trinn i logisk rekkefølge, konkrete handlinger ("Trykk Ctrl+Alt+Del"), sjekkpunkter ("Lyser det grønt på projektoren?"), og tydelige stoppunkter ("Hvis ikke løst etter disse stegene, kontakt IT").
- Oppgave 2: God plan inkluderer tidslinje (Gantt), avhengigheter, risikohåndtering ("hva gjør vi hvis..."). Rollback: ta full backup først, test at backup kan gjenopprettes, ha gammel maskinvare klar til å starte på nytt.

### English — Practical Exercises

**Exercise 1: Create a Troubleshooting Guide for School IT**
Document a guide for 5 common school IT problems:
1. Can't log in (forgot password / locked account)
2. Projector shows no image (cable / source / driver)
3. Printer not working (empty ink / paper jam / driver)
4. WiFi not working (wrong password / signal / AP down)
5. Network drive unavailable
- For each: Symptoms → Possible causes → Step-by-step → Solution → When to escalate
- Write in a format a non-IT teacher can follow

**Exercise 2: Plan a Server Migration**
Plan moving a file server from the server room to a data center:
- Create a project plan with phases: Assessment, Planning, Preparation, Migration, Post-work
- Include tasks, responsible person, time estimate, risk, quality control
- Include a rollback plan

**Solution Guidelines:**
- Exercise 1: Steps in logical order, concrete actions ("Press Ctrl+Alt+Del"), checkpoints ("Is the projector green light on?"), clear escalation criteria.
- Exercise 2: Timeline (Gantt), dependencies, risk management ("what if..."). Rollback: full backup first, test restore, keep old hardware ready.

## 🔗 Relevante artikler / Related Articles

- [[dokumentasjon-og-planlegging]] — Hvordan dokumentere og planlegge IT-arbeid
- [[driftsarkitektur]] — Hvordan arkitektur påvirker dokumentasjonsbehov (KM-01)

## 📚 Kilder / Sources

[^1]: Udir (2020). Læreplan i Vg2 informasjonsteknologi. https://www.udir.no/lk20/itk02-01/
[^2]: NDLA. Fagstoff for driftsstøtte VG2. https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/
[^3]: AXELOS. ITIL Foundation. https://www.itil.org/

[^4]: Digdir. Informasjonssikkerhet. https://www.digdir.no/informasjonssikkerhet/
