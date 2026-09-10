---
title: "Sustainability in IT Operations"
emne: it-drift
competence_goals:
  - km-12
sources:
  - ndla
  - https://ndla.no/nb/subject:1:43a4e98f-ce79-42b3-9022-297e68266455/topic:1:94c5e317-0f9c-486a-8686-2678683519d5/resource:1:115939
  - https://www.nkom.no/aktuelt/digital-infrastruktur-og-miljo-hvordan-paivirker-vi-klimaet
  - https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/
  - https://www.digdir.no/nasjonal-arkitektur/skytjenester/2153
  - https://learn.microsoft.com/en-us/azure/architecture/framework/
  - https://snl.no/skytjeneste
video: https://www.youtube.com/watch?v=68D0v7Y-eIk
tags: []
flashcards: https://notebooklm.google.com/notebook/bc9a5656-7a9b-4dc5-a59e-ef4a96aa8ccd
public: true
notebooklm: true
language: en
original: baerekraft.md
---

## Introduction

The IT industry is not just digital – it is physical, energy-intensive, and resource-demanding. Servers, networks, and client equipment generate heat, consume electricity, and create waste. Understanding and reducing the environmental impact of IT operations is part of the professional competence in Driftsstøtte VG2.

Competence goal km-12 is about exploring the data industry's environmental footprint and evaluating measures for more sustainable IT operations. It is a rapidly evolving field, where the industry itself sets ambitious goals – and where much work remains. Choices regarding [[skytjenester]] and [[driftsarkitektur]] have a direct impact on the environmental footprint.

---

## Theory

### Data Center Energy Consumption

Data centers are the most energy-intensive single component of IT infrastructure.

**Globally:**
> "Estimated global data centre electricity consumption in 2022 was 240–340 TWh, or around 1–1.3% of global final electricity demand." – IEA (2023)

In addition, data transmission networks use 260–360 TWh per year. Together, this accounts for approximately 1–2.8% of global electricity consumption.

CO₂ emissions from the IT sector (including equipment production) are estimated at around **330 million tonnes of CO₂ equivalents in 2020**.

**Concentration example – Ireland:**
In 2022, data centers accounted for **18% of Ireland's total electricity consumption**. Ireland is an attractive country for large tech companies (low tax, favorable location) and has felt the strain on its power grid.

**Denmark** estimates a sixfold increase in data center consumption by 2030, potentially reaching up to 15% of the country's electricity consumption.

The big four – Amazon, Microsoft, Google, and Meta – collectively used over **72 TWh in 2021**.

---

### PUE – Power Usage Effectiveness

PUE is the industry's standard metric for data center energy efficiency:

$$\text{PUE} = \frac{\text{Total electricity consumption of the data center}}{\text{Electricity consumption of IT equipment}}$$

- **PUE = 1.0** is theoretically perfect – all power goes to IT equipment
- **PUE = 1.5** means 50% extra power is used for cooling, lighting, and other overheads
- **PUE = 2.0** means as much energy is wasted as is used productively

**Benchmarks:**
| Provider | PUE |
|----------|-----|
| Google | ~1.10 |
| Meta | ~1.10 |
| Microsoft Azure | ~1.12 |
| Industry average | ~1.50 |
| Older data center | 2.0+ |

The hyperscalers (Google, Meta, Microsoft, Amazon) are best in class with PUE around 1.1. Older and smaller data centers can have PUE above 2.0, indicating extremely poor efficiency.

**Example:** A data center with IT equipment using 1,000 kW and PUE = 1.5 uses a total of 1,500 kW. The 500 kW that is "wasted" largely goes to cooling.

---

### Dark Data

An underestimated environmental problem is **dark data** – data stored in data centers but never used. Studies estimate that up to 80% of all stored data is never accessed after it is created.

This is problematic because:
- Storing unused data requires power for servers and cooling
- Large organizations accumulate terabytes of duplicates, outdated files, and unused backups

Measures: regular data cleanup, clear retention and deletion policies, and data classification.

---

### E-waste and the WEEE Directive

IT equipment has a limited lifespan. When it is replaced, it becomes **e-waste** (electrical and electronic waste).

E-waste is problematic because:
- IT equipment contains **rare earth metals** (e.g., neodymium, indium, dysprosium) that are difficult to extract and produce
- Equipment contains **toxic substances** such as lead, cadmium, and mercury
- Illegal dumping of e-waste is a global problem, particularly in West Africa and Southeast Asia

**The WEEE Directive** (Waste Electrical and Electronic Equipment) is EU legislation that also applies in Norway. The directive requires:
- Producers and importers are responsible for collecting and recycling e-waste
- Consumers and businesses must deliver equipment to approved collection points
- Certain materials (plastics, metals, glass) must be recovered

In Norway, e-waste is managed through **Elretur** and other approved return systems.

---

### Extending Equipment Lifespan

One of the most effective environmental measures is to use IT equipment longer:

- The production of a laptop typically accounts for **70–80% of its total carbon footprint** over its lifetime
- Extending the lifespan from 3 to 5 years can halve the annual environmental impact
- **Refurbished equipment** (used, renovated equipment) is a growing market that reduces the need for new production

Measures for lifespan extension:
- Upgrading RAM and storage instead of buying a new PC
- Using thin clients with long lifespans and simple administration
- Centralized systems (VDI, terminal servers) where clients are simple and durable

**Circular IT** is an operational model that prioritizes reuse, repair, and upgrading to keep hardware in use for as long as possible – in line with circular economy principles.

---

### Green IT Certifications

Organizations and products can be certified for energy efficiency:

**Energy Star**
American certification program for energy-efficient equipment (PCs, servers, monitors). Energy Star-labeled products typically use 25–50% less energy than uncertified products.

**EPEAT**
(Electronic Product Environmental Assessment Tool) – a global registry for environmentally friendly IT equipment. Assesses lifecycle, energy use, design for reuse, and manufacturing conditions. Used in public procurement in many countries, including Norway.

**ISO 50001**
International standard for energy management. Sets requirements for systematic energy work within the organization.

**TCO Certified**
International sustainability certification for IT equipment that assesses both environmental and social conditions in the production chain. Widely used in the Norwegian public sector.

---

### Green Measures in Organizations

Concrete measures IT managers can take:

1. **Consolidation and virtualization** – fewer physical servers mean lower energy consumption
2. **Turn off unused equipment** – automated power management
3. **Choose energy-efficient equipment** – look for Energy Star and EPEAT when purchasing
4. **Cloud migration** – large cloud providers have better PUE than most internal data centers
5. **Extend equipment lifespan** – do not replace before necessary
6. **Proper disposal** – use approved e-waste facilities (Elretur)
7. **Monitor and report energy consumption** – what is measured can be improved
8. **Clean up dark data** – regularly delete unused data and duplicates
9. **Heat recovery** – excess heat from server rooms can be used to heat buildings

Amazon, Microsoft, Meta, and Google have collectively entered into contracts for over **50 GW of renewable energy** – far more than any other single industry.

The IEA emphasizes that global emissions from data centers must be **halved by 2030** to meet net-zero goals.

---

### Norwegian Perspective

Norway is in a privileged position regarding sustainable IT:

**Renewable energy**
Approximately 90% of Norwegian electricity production comes from **hydropower** – making Norwegian data centers among the greenest in the world. Statkraft is Europe's largest producer of renewable energy.

**Natural cooling**
Norway's cold climate makes it possible to use **free cooling** (outside air cooling) for most of the year, reducing the need for energy-intensive cooling systems. Some data centers use seawater/fjord water for cooling.

**Green data center industry**
Data centers in the Nordics (Norway, Sweden, Finland) are marketed internationally as sustainable alternatives. Companies such as Green Mountain (Ryfylke) and Lefdal Mine Datacenter are examples of Norwegian players building on these advantages.

**Norwegian regulations**
Nkom (Norwegian Communications Authority) and the Norwegian Environment Agency regulate e-waste and the ICT sector. Public procurement in Norway can require environmental certification (EPEAT) when purchasing IT equipment.

---

## Example / Lab

**Task: Calculate PUE and assess measures**

A school has a server room with the following measurements:
- Total power meter (all equipment in the room): 12 kW
- Power meter for servers and network equipment only: 8 kW

1. Calculate the PUE for the server room.
2. Compare with the industry average (~1.5) and hyperscalers (~1.1).
3. What are the "extra" kW used for? (Hint: cooling, lighting, UPS losses)
4. Suggest at least two measures to improve PUE.
5. Discuss: Should the school consider moving services to a cloud provider with better PUE? What factors determine this?

**Additional task: Lifecycle of a laptop**

Map the environmental footprint of a laptop throughout its entire lifecycle: raw material production, manufacturing, use phase, and disposal. Where in the cycle is the environmental impact greatest? What choices can you as an IT manager make to reduce it?

---

## Study Guide

### Core Content

Sustainability in IT operations is about understanding and reducing the IT sector's environmental impact – from energy consumption in data centers to disposal of old equipment.

**Energy consumption:**
- Data centers use 1–1.3% of global electricity consumption (IEA 2022)
- PUE measures energy efficiency: 1.0 is perfect, 1.5 is industry average
- Hyperscalers (Google, Microsoft, AWS) achieve ~1.1

**E-waste:**
- 70–80% of a PC's carbon footprint occurs during manufacturing
- The WEEE Directive imposes producer responsibility and recycling requirements
- Elretur handles e-waste in Norway

**Measures (in order of impact):**
1. Extend equipment lifespan (greatest impact per krone)
2. Virtualize and consolidate servers
3. Choose certified equipment (Energy Star, EPEAT)
4. Migrate to energy-efficient cloud providers
5. Clean up dark data

**Norway's unique position:** hydropower + cold climate = low carbon footprint for Norwegian data centers.

---

## FAQ

**Is IT a major source of greenhouse gases?**
The IT sector accounts for approximately 2–4% of global CO₂ emissions – roughly the same as aviation. This includes equipment production, data center operations, and data transmission. It is not huge, but it is growing rapidly alongside digitalization.

**Is cloud-based operations always more environmentally friendly than on-premise?**
Not necessarily, but large cloud providers (Google, Microsoft, AWS) have PUE values around 1.1 and invest massively in renewable energy. An older internal data center with PUE 2.0 and coal power can have a much higher carbon footprint than using a large cloud provider with renewable energy.

**What is dark data and how does it become a problem?**
Dark data is data that is stored but never used – duplicates, outdated files, forgotten backups. They consume storage space that requires electricity. Regular cleanup and clear data retention policies reduce the problem.

**What is TCO Certified and is it better than Energy Star?**
TCO Certified assesses the entire lifecycle and includes social conditions in the production chain (work environment, chemicals), while Energy Star primarily focuses on energy use during the operational phase. They are complementary, and the Norwegian public sector uses both.

**What is "circular IT"?**
Circular IT is an operational model based on circular economy principles: equipment is kept in use for as long as possible through upgrading, repair, and refurbishment. When equipment is eventually discarded, materials are recovered. It counteracts the linear "produce – use – dispose" pattern.

**What makes Norway especially suitable for green data centers?**
Three factors: nearly 100% renewable electricity from hydropower, cold climate enabling natural cooling for most of the year, and access to fjord water for cooling. This gives very low PUE and near-zero CO₂ from electricity. Lefdal Mine Datacenter in a Norwegian mountainside is a concrete example.

---

## Quiz

<details><summary>Question 1: What is PUE and what does a PUE of 1.0 mean?</summary>

**Answer:** PUE (Power Usage Effectiveness) is a measure of energy efficiency in data centers. PUE = total electricity consumption / electricity consumption of IT equipment. A PUE of 1.0 is theoretically perfect – all power goes to IT equipment. In practice, the best data centers achieve PUE around 1.1.

</details>

<details><summary>Question 2: How much electricity did data centers use globally in 2022, and what share of global consumption did it represent?</summary>

**Answer:** According to the IEA, data centers used 240–340 TWh in 2022, corresponding to approximately 1–1.3% of global electricity consumption.

</details>

<details><summary>Question 3: What is the WEEE Directive?</summary>

**Answer:** WEEE is the EU directive on electrical and electronic waste. It imposes producer responsibility for the collection and recycling of e-waste, and requires businesses and consumers to deliver equipment to approved facilities. It applies in Norway through the EEA.

</details>

<details><summary>Question 4: Why is Norway favorable for green data centers?</summary>

**Answer:** Norway has approximately 90% renewable electricity production from hydropower, low electricity prices, a cold climate enabling natural cooling, and access to sea/fjord water for cooling. This gives very low CO₂ emissions and low PUE for Norwegian data centers.

</details>

<details><summary>Question 5: What is the single most effective measure to reduce the environmental impact of client equipment?</summary>

**Answer:** Extending the lifespan of the equipment. The production of a PC accounts for 70–80% of the total carbon footprint over its lifetime. Using the equipment for 5 years instead of 3 years almost halves the annual environmental impact. Refurbished equipment is a related approach.

</details>

---

## Flashcards

PUE :: Power Usage Effectiveness – measure of energy efficiency in data centers. PUE = total consumption / IT consumption. 1.0 is perfect; industry average ~1.5.

E-waste :: Electrical and electronic waste. Contains rare earth metals and toxic substances. Must be delivered to approved facilities.

WEEE Directive :: EU directive on electrical and electronic waste. Producer responsibility and recycling requirements. Applies in Norway.

Energy Star :: Certification program for energy-efficient IT equipment. Products typically use 25–50% less energy.

EPEAT :: Electronic Product Environmental Assessment Tool – global certification for environmentally friendly IT equipment. Used in public procurement.

Lifespan extension :: Measures to use IT equipment longer. One of the most effective environmental measures since production is the greatest environmental burden.

Free cooling :: Use of cold outside air or water to cool data centers. Reduces the need for energy-intensive cooling machines.

Hyperscaler :: The largest cloud providers (Google, Microsoft, Amazon, Meta). Have the best PUE values (~1.1) and largest renewable energy contracts.

Refurbished equipment :: Used IT equipment that is renovated and resold. Reduces the need for new production and environmental impact.

Statkraft :: Norwegian state-owned energy company and Europe's largest producer of renewable energy. Important for Norway's position in green IT.

IEA :: International Energy Agency – international organization that monitors global energy use. Authoritative source for data center statistics.

Circular IT :: Operational model that prioritizes reuse, repair, and upgrading to keep hardware in use as long as possible.

Dark Data :: Data stored in data centers but never used. Leads to unnecessary energy consumption for storage and cooling.

TCO Certified :: International sustainability certification for IT equipment assessing both environmental and social conditions in the production chain.

EE-waste :: Electrical and electronic waste containing environmental toxins and valuable metals requiring specialized recycling.

---

## Resources

- [IEA: Data Centres and Data Transmission Networks](https://www.iea.org/energy-system/buildings/data-centres-and-data-transmission-networks)
- [NDLA: Bærekraft og IT-utstyr](https://ndla.no/nb/subject:1:43a4e98f-ce79-42b3-9022-297e68266455/topic:1:94c5e317-0f9c-486a-8686-2678683519d5/resource:1:115939)
- [Nkom: Digital infrastruktur og miljø](https://www.nkom.no/aktuelt/digital-infrastruktur-og-miljo-hvordan-paivirker-vi-klimaet)
- [Elretur: E-avfall i Norge](https://www.elretur.no/)
- [YouTube: The life cycle of a smartphone – TED-Ed](https://www.youtube.com/watch?v=68D0v7Y-eIk)
- [[driftsarkitektur]]
- [[skytjenester]]
