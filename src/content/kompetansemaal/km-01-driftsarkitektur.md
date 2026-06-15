---
title: "KM-01: Driftsarkitektur / IT Operations Architecture"
emne: kompetansemaal
kompetansemaal:
  - km-01
kilder:
  - https://www.udir.no/lk20/itk02-01/kompetansemaal-og-vurdering/kv372
  - https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/
  - https://www.cloudflare.com/learning/
  - https://learn.microsoft.com/en-us/training/
tags: [km-01, driftsarkitektur, arkitektur]
flashcards: false
public: true
---

# KM-01: Driftsarkitektur / IT Operations Architecture

## 🎯 Mål / Competency Goal

**Norsk:** Utforske og beskrive komponenter i en driftsarkitektur

**English:** Explore and describe components of an IT operations architecture

---

## 📘 Forklaring / Explanation

### Norsk
Driftsarkitektur er «skjelettet» i en IT-organisasjon. Det handler om å forstå hvordan ulike komponenter — servere, lagring, nettverk, programvare, backup-løsninger — henger sammen og samspiller for å levere pålitelige IT-tjenester[^1][^4].

En driftsarkitekt må kunne:
- Identifisere fysiske og logiske komponenter i en infrastruktur
- Beskrive hvordan komponentene kommuniserer
- Forstå avhengigheter mellom systemer
- Dokumentere arkitekturen slik at andre kan forstå den

### English
IT operations architecture is the "skeleton" of an IT organization. It's about understanding how different components — servers, storage, networks, software, backup solutions — interconnect and interact to deliver reliable IT services[^1].

An operations architect must be able to:
- Identify physical and logical components in an infrastructure
- Describe how components communicate
- Understand dependencies between systems
- Document the architecture so others can understand it

---

## 💡 Eksempler / Examples

### Norsk

**Eksempel 1: Skole-nettverk**
En skole har 200 PC-er, 10 servere, svitsjer, rutere og trådløse aksesspunkt. Driftsarkitekturen beskriver hvordan disse henger sammen: elevene kobler seg til via WiFi, trafikken går gjennom en brannmur, og serverene håndterer pålogging, filer og printertjenester.

**Eksempel 2: Netthandel**
En nettbutikk har web-servere, databaseservere, betalingssystem og lagerstyring. Arkitekturen må vise hvordan en kunde klikker «Kjøp» og data flyter gjennom hele systemet.

### English

**Example 1: School Network**
A school has 200 PCs, 10 servers, switches, routers, and wireless access points. The operations architecture describes how these connect: students connect via WiFi, traffic goes through a firewall, and servers handle login, files, and printing services.

**Example 2: E-commerce**
An online store has web servers, database servers, payment systems, and inventory management. The architecture must show how a customer clicks "Buy" and data flows through the entire system.

---

## 📝 Oppsummering / Summary

| Norsk | English |
|-------|---------|
| Driftsarkitektur er hvordan IT-komponenter henger sammen | Operations architecture is how IT components interconnect |
| Viktige komponenter: servere, nettverk, lagring, programvare | Key components: servers, networks, storage, software |
| Dokumentasjon er avgjørende for å forstå helheten | Documentation is essential for understanding the big picture |
| God arkitektur gir pålitelige og sikre tjenester | Good architecture delivers reliable and secure services |

---

## 🔧 Bridging Exercises / Praksisoppgaver

### Norsk — Praksisoppgaver

**Oppgave 1: Tegn skolens driftsarkitektur**
Eleven får en beskrivelse av skolens IT-system: 200 klient-PCer, 3 servere (domenekontroller, filserver, webserver), 6 svitsjer, 2 rutere, 10 WiFi-aksesspunkt, brannmur, og en nettverkskriver.
- Tegn en arkitekturskisse som viser hvordan komponentene henger sammen
- Merk av alle fysiske og logiske komponenter
- Beskriv dataflyten når en elev logger på skolens system
- Identifiser single points of failure / enkeltpunkter for feil

**Oppgave 2: Design en arkitektur for en liten bedrift**
En bedrift med 15 ansatte trenger ny IT-infrastruktur. Krav:
- Fildeling mellom ansatte
- E-post og kalender (krever internetttilgang)
- Enkel webside for markedsføring
- Backup-løsning
- Trådløst nett for gjester
Lever: arkitekturskisse + begrunnelse for hver komponent.

**Veiledning / Solution Guidelines:**
- Oppgave 1: Skissen bør inneholde klienter → svitsj → ruter → brannmur → internett, med servere på et eget segment. Eleven bør identifisere at én enkelt brannmur eller én server kan være SPOF.
- Oppgave 2: En god løsning kan være skytjenester (SaaS) for e-post/Office, lokal filserver (eller sky), nettsted hos webhotell. Backup bør følge 3-2-1-regelen. Gjestenett bør være VLAN-isolert.

### English — Practical Exercises

**Exercise 1: Draw the School's Operations Architecture**
Students receive a description of the school's IT system: 200 client PCs, 3 servers (domain controller, file server, web server), 6 switches, 2 routers, 10 WiFi access points, firewall, and a network printer.
- Draw an architecture diagram showing how components are connected
- Label all physical and logical components
- Describe the data flow when a student logs into the school system
- Identify single points of failure

**Exercise 2: Design an Architecture for a Small Business**
A company with 15 employees needs new IT infrastructure. Requirements:
- File sharing between employees
- Email and calendar (requires internet access)
- Simple marketing website
- Backup solution
- Guest wireless network
Deliver: architecture sketch + justification for each component.

**Solution Guidelines:**
- Exercise 1: The sketch should show clients → switch → router → firewall → internet, with servers on a separate segment. Identify that a single firewall or single server can be a SPOF.
- Exercise 2: A good solution: cloud services (SaaS) for email/Office, local file server (or cloud), website with web hosting. Backup should follow 3-2-1 rule. Guest network VLAN-isolated.

## 🔗 Relevante artikler / Related Articles

- [[driftsarkitektur]] — Innføring i driftsarkitektur
- [[backup-og-gjenoppretting]] — Backup og gjenoppretting som del av arkitekturen
- [[dokumentasjon-og-planlegging]] — Hvordan dokumentere en driftsarkitektur

## 📚 Kilder / Sources

[^1]: Udir (2020). Læreplan i Vg2 informasjonsteknologi, kompetansemål etter driftsstøtte. https://www.udir.no/lk20/itk02-01/
[^2]: Cloudflare Learning Center. What is network architecture? https://www.cloudflare.com/learning/
[^3]: Microsoft Learn. Introduction to IT infrastructure. https://learn.microsoft.com/en-us/training/
[^4]: NDLA. Fagstoff for driftsstøtte VG2. https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/
