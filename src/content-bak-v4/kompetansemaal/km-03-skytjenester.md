---
title: "KM-03: Skytjenester og virtuelle tjenester / Cloud and Virtual Services"
emne: kompetansemaal
kompetansemaal:
  - km-03
kilder:
  - https://www.udir.no/lk20/itk02-01/kompetansemaal-og-vurdering/kv372
  - https://www.cloudflare.com/learning/cloud/what-is-the-cloud/
  - https://learn.microsoft.com/en-us/training/azure/
  - https://aws.amazon.com/what-is-cloud-computing/
  - https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/
tags: [km-03, sky, cloud, virtualisering, tjenester]
flashcards: false
public: true
---

# KM-03: Skytjenester og virtuelle tjenester / Cloud and Virtual Services

## 🎯 Mål / Competency Goal

**Norsk:** Gjøre rede for prinsipper og strukturer for skytjenester og virtuelle tjenester

**English:** Explain principles and structures for cloud services and virtual services

---

## 📘 Forklaring / Explanation

### Norsk
Skytjenester (cloud services) betyr at IT-ressurser som servere, lagring, databaser og programvare leveres over internett — i stedet for å være fysisk installert hos deg[^1][^5]. Du betaler for det du bruker, og slipper å drifte maskinvaren selv.

**Tre hovedtyper skytjenester:**
- **IaaS (Infrastructure as a Service)** — Virtuelle maskiner, lagring, nettverk (f.eks. Azure VM, AWS EC2)
- **PaaS (Platform as a Service)** — Plattform for å utvikle og kjøre apper (f.eks. Azure App Services, Heroku)
- **SaaS (Software as a Service)** — Ferdige programmer (f.eks. Office 365, Google Workspace)

**Skydistribusjonsmodeller:**
- **Public Cloud** — Delt infrastruktur, lavere kostnad
- **Private Cloud** — Dedikert til én organisasjon, høyere sikkerhet
- **Hybrid Cloud** — Kombinasjon av public og private sky

Virtuelle tjenester bygger på hypervisor-teknologi (f.eks. Hyper-V, VMware, KVM) som gjør at én fysisk maskin kan kjøre flere virtuelle maskiner samtidig[^2].

### English
Cloud services means IT resources like servers, storage, databases, and software are delivered over the internet — instead of being physically installed at your location[^1]. You pay for what you use and don't have to maintain the hardware yourself.

**Three main cloud service types:**
- **IaaS** — Virtual machines, storage, networking (e.g., Azure VM, AWS EC2)
- **PaaS** — Platform to develop and run apps (e.g., Azure App Services, Heroku)
- **SaaS** — Ready-made applications (e.g., Office 365, Google Workspace)

**Cloud deployment models:**
- **Public Cloud** — Shared infrastructure, lower cost
- **Private Cloud** — Dedicated to one organization, higher security
- **Hybrid Cloud** — Combination of public and private cloud

Virtual services are built on hypervisor technology (e.g., Hyper-V, VMware, KVM) that lets one physical machine run multiple virtual machines simultaneously[^2].

---

## 💡 Eksempler / Examples

### Norsk

**Eksempel 1: Skole som flytter til skyen**
En skole bytter fra lokal e-postserver til Office 365. Elevene får tilgang fra hvor som helst, IT-avdelingen trenger ikke lenger vedlikeholde servermaskinvaren.

**Eksempel 2: Nettbutikk på AWS**
En nettbutikk kjører webserveren på en EC2-instans (IaaS) og databasen i RDS (PaaS). Når Black Friday kommer, skalerer de automatisk opp antall servere.

### English

**Example 1: School Moving to the Cloud**
A school switches from a local email server to Office 365. Students get access from anywhere, and IT no longer needs to maintain server hardware.

**Example 2: Online Store on AWS**
An online store runs its web server on EC2 (IaaS) and the database in RDS (PaaS). When Black Friday arrives, they automatically scale up the number of servers.

---

## 📝 Oppsummering / Summary

| Norsk | English |
|-------|---------|
| Skyen = IT-ressurser over internett | Cloud = IT resources over the internet |
| IaaS/PaaS/SaaS er de tre tjenestemodellene | IaaS/PaaS/SaaS are the three service models |
| Public/private/hybrid er distribusjonsmodeller | Public/private/hybrid are deployment models |
| Virtualisering er teknologien bak skytjenester | Virtualization is the technology behind cloud services |

---

## 🔧 Bridging Exercises / Praksisoppgaver

### Norsk — Praksisoppgaver

**Oppgave 1: Sett opp en virtuell maskin i skyen**
Eleven oppretter en gratis Azure- eller AWS-konto (eller bruker skolens lab-miljø).
- Opprett en VM (f.eks. Ubuntu Server 22.04 LTS)
- Velg riktig størrelse basert på bruksområde (webserver: 2 vCPU, 4 GB RAM)
- Konfigurer SSH-nøkkel for pålogging
- Logg inn og installer en webserver (Apache/Nginx)
- Åpne port 80/443 i nettverkssikkerhetsgruppen
- Verifiser at nettsiden er tilgjengelig fra internett
- Reflekter: Hvilket skytjeneste-modell (IaaS/PaaS/SaaS) brukte du?

**Oppgave 2: Klassifiser IT-tjenester som IaaS/PaaS/SaaS**
Eleven får 6 scenarioer og skal klassifisere hver:
1. Skolen bruker Office 365 for e-post og dokumenter
2. IT-avdelingen setter opp en virtuell Windows Server i Azure
3. Utvikleren deployer kode til Azure App Services uten å tenke på servere
4. Eleven logger på ItsLearning for å levere oppgaver
5. Skolen kjører egne servere i et serverrom
6. En bedrift bruker AWS RDS for database uten å administrere OS
- For hver: begrunn valget og forklar hvordan ansvarsfordelingen er

**Veiledning / Solution Guidelines:**
- Oppgave 1: Azure VM (B1s/B2s) eller AWS t2.micro (free tier). SSH: `ssh -i nokkel.pem ubuntu@<public-ip>`. Installere Apache: `sudo apt update && sudo apt install apache2 -y`. Dette er IaaS fordi vi administrerer OS og programvare selv.
- Oppgave 2: IaaS = du styrer OS og apper (mest fleksibelt, mest ansvar). PaaS = du styrer appen, leverandøren styrer OS/plattform. SaaS = ferdig programvare, brukeren styrer ingenting teknisk.

### English — Practical Exercises

**Exercise 1: Set Up a Virtual Machine in the Cloud**
Create a free Azure or AWS account (or use school lab).
- Create a VM (e.g., Ubuntu Server 22.04 LTS)
- Choose appropriate size (web server: 2 vCPU, 4 GB RAM)
- Configure SSH key for login
- SSH in and install a web server (Apache/Nginx)
- Open port 80/443 in the network security group
- Verify the website is accessible from the internet
- Reflect: Which cloud service model (IaaS/PaaS/SaaS) did you use?

**Exercise 2: Classify IT Services as IaaS/PaaS/SaaS**
Classify 6 scenarios and justify each choice:
1. School uses Office 365 for email and documents
2. IT sets up a virtual Windows Server in Azure
3. Developer deploys code to Azure App Services
4. Student logs into ItsLearning to submit assignments
5. School runs physical servers in a server room
6. Company uses AWS RDS for database without managing the OS

**Solution Guidelines:**
- Exercise 1: Azure B1s/B2s or AWS t2.micro (free tier). SSH + Apache install. This is IaaS because you manage the OS and software yourself.
- Exercise 2: IaaS = you manage OS + apps. PaaS = you manage the app, provider manages OS/platform. SaaS = ready-made software, user manages nothing technical.

## 🔗 Relevante artikler / Related Articles

- [[skytjenester]] — Ulike skytjenester og deres bruk
- [[driftsarkitektur]] — Hvordan skyen passer inn i driftsarkitekturen
- [[virtuelle-losninger]] — Hypervisorer og VM-er

## 📚 Kilder / Sources

[^1]: Udir (2020). Læreplan i Vg2 informasjonsteknologi. https://www.udir.no/lk20/itk02-01/
[^2]: Cloudflare. What is the cloud? https://www.cloudflare.com/learning/cloud/what-is-the-cloud/
[^3]: AWS. What is cloud computing? https://aws.amazon.com/what-is-cloud-computing/
[^4]: Microsoft Learn. Azure fundamentals. https://learn.microsoft.com/en-us/training/azure/
[^5]: NDLA. Fagstoff for driftsstøtte VG2. https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/
