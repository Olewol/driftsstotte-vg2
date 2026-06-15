---
title: "Documentation and Planning"
emne: it-drift
competence_goals:

  - km-06

sources:

  - ndla
  - <https://www.digdir.no/nasjonal-arkitektur/referansearkitektur-for-datadeling/2131>
  - <https://learn.microsoft.com/en-us/azure/architecture/framework/>
  - <https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/>
  - <https://www.digdir.no/nasjonal-arkitektur/skytjenester/2153>
  - <https://snl.no/skytjeneste>

video: null
tags: []
flashcards: <https://notebooklm.google.com/notebook/bc9a5656-7a9b-4dc5-a59e-ef4a96aa8ccd>
public: true
notebooklm: true
language: en
original: dokumentasjon-og-planlegging.md
---

## Introduction

GGood documentation is the backbone of professional IT operations. Without up-to-date documentation, it is impossible to
Gtroubleshoot effectively, difficult to train new employees, and risky to make changes to the system.

DDocumentation and planning is about having an overview: of what exists, how things connect, what has been done, and what
DDneeds to be done. This is competence goal km-06 – one of the most practical parts of the subject.
DDA good IT department treats documentation as living resources that are continuously updated, not as something written
Donce and then left to gather dust.

---

## Theory

### Why Document?

Documentation serves several purposes in IT operations:

-**Troubleshooting**– if we know the normal configuration, it is easier to find deviations
-**Onboarding**– a new colleague or temp can take over without starting from scratch
-**Audits and compliance**– authorities and customers may require documentation (e.g., under GDPR)
-**Change management**– tracking what was changed, who changed it, and why
-**Continuity**– the organization is not dependent on one person carrying all knowledge in their head

Digdir emphasizes that good documentation is the foundation for interoperability in the Norwegian public sector.

---

### Network Topologies

A network topology describes how nodes (devices) are connected in a network.

#### Star Topology (most common)

AAll devices connect to a central switch or router. Easy to troubleshoot (isolate the cable to the faulty device) and
Aeasy to expand.

```text
      [PC]
       ||
[PC]--[Switch]--[PC]
       ||
      [Server]
```

- Advantages: simple, fault-tolerant (one device fails without affecting others), easy to expand
- Disadvantages: the switch is a single point of failure (mitigated with redundant switches)

#### Mesh Topology

AAll nodes are connected to all other nodes (full mesh) or to many others (partial mesh).
AUsed in WAN networks and robust critical systems.

```bash
[A]---[B]
 || \ / |
 || X |
 || / \ |
[C]---[D]
```

- Advantages: extremely robust – many alternative paths
- Disadvantages: expensive and complex

#### Bus Topology (historical)

AAll devices connected to one common cable (bus). No longer used in modern networks, but recognized from older Ethernet
Astandards.

---

### IP Address Plan

AAn IP address plan is a structured overview of all IP addresses, subnets, and related information in the network.
AAIt is a critical planning and operations document. See [[dns-og-dhcp-en]] and [[segmentering-og-vlan-en]] for related
Atopics.

#### Example: IP Address Plan for a School Network

**Network info:**192.168.1.0/24 (254 usable addresses)

|| VLAN | Name | Subnet | Network Address | Gateway | DNS | DHCP Range | Comment |
|| ------ | ------ | -------- | ----------------- | --------- | ----- | ------------- | --------- |
|| 10 | Administration | /26 | 192.168.1.0 | 192.168.1.1 | 192.168.1.10 | .20–.62 | 42 addresses for staff |
|| 20 | Students | /25 | 192.168.1.128 | 192.168.1.129 | 192.168.1.10 | .140–.253 | 114 addresses, BYOD |
|| 30 | Servers | /27 | 192.168.1.64 | 192.168.1.65 | 192.168.1.66 | Static | File server, AD, backup |
|| 40 | Guest/IoT | /27 | 192.168.1.96 | 192.168.1.97 | 8.8.8.8 | .100–.126 | Isolated, internet only |

*## Static addresses (selection):

|| Device | IP Address | MAC Address | Location |
|| -------- | ----------- | ------------- | ---------- |
|| Firewall (WAN interface) | 10.0.0.1 | – | Server Room |
|| Core Switch | 192.168.1.2 | aa:bb:cc:dd:ee:01 | Server Room |
|| Active Directory / DNS | 192.168.1.10 | aa:bb:cc:dd:ee:10 | Server Room |
|| File Server | 192.168.1.11 | aa:bb:cc:dd:ee:11 | Server Room |
|| NAS (backup) | 192.168.1.12 | aa:bb:cc:dd:ee:12 | Server Room |
|| Printer, 1st floor | 192.168.1.50 | aa:bb:cc:dd:ee:50 | Room 101 |

---

### Operations Log and Change Log

AAn operations log (change log) is a chronological record of all changes made to the IT environment.
AIt is perhaps the single most important document in an operations organization.

#### Format

The log should contain:
-**Date and time**– when was the change made?
-**Performed by**– who did it?
-**What was done**– concrete description of the change
-**Why**– reason/rationale
-**Result**– did it go as expected? Any issues?
-**Case number / ticket**– reference to the helpdesk case if relevant

#### Example of a Change Log

|| Date | Performed by | Change | Reason | Result |
|| ------ | -------------- | -------- | -------- | -------- |
|| 2025-11-12 08:30 | Erik H. | Updated Windows Server 2022 to KB5043050 | Monthly patch round | OK, server started normally |
|| 2025-11-14 14:00 | Sara L. | Added new PC (HP EliteBook) to AD, VLAN 20 | New student | Working, DHCP lease confirmed |
|| 2025-11-15 09:15 | Erik H. | Changed DHCP scope for VLAN 20: .140–.200 → .140–.253 | Capacity need | OK, new range active |

---

### Procedure Documentation

CCritical operations should be documented as step-by-step procedures. This ensures the operation can be performed by
Canyone on the team – not just the person who originally set it up.

*## Example: Procedure for Monthly Backup Test

```bash
Title: Monthly Recovery Test of File Server Backup
Responsible role: System Administrator
Frequency: Every 1st Monday of the month

Steps:

1. Log in to Veeam Backup & Replication.
2. Navigate to the latest full backup of FILESERVER01.
3. Right-click → "Instant Recovery" → select isolated test network.
4. Start recovery and wait until the VM is available (approx. 5 min).
5. Log in to the restored VM and verify:

   a. That services (fileshare, DNS) are running.
   b. That a randomly selected file from the last week is accessible and readable.

1. 
2. 

Expected result: VM starts, files accessible, no errors.
```

---

### Documentation Tools

|| Tool | Use Case |
|| ------ | ---------- |
|| **draw.io / Lucidchart** | Network topologies, architecture diagrams |
|| **Markdown / Obsidian** | Operations log, procedures, internal wiki |
|| **Confluence** | Team-based wiki, used in large IT departments |
|| **IT Glue** | Professional MSP tool for IT documentation. Integrates password management, device registry, and procedures. |
|| **CMDB** | Configuration Management Database – registry of all IT infrastructure (devices, configuration, relationships) |
|| **Excel/Google Sheets** | IP address plans and inventory lists (simple, but not scalable) |

---

### ITIL and Change Management

***ITIL**(IT Infrastructure Library) is a framework for good IT operations practice that is widely used in the Norwegian
**and international IT industry. Although you do not need to implement the entire ITIL at VG2 level, some concepts are
*central:

*## Change Management
A structured process for handling changes in the IT environment in a controlled manner:

1. The change is planned and documented
2. Risk assessment is performed
3. The change is approved (by the appropriate person/role)
4. The change is implemented in a specific time window
5. The result is verified and documented in the change log
6. A rollback plan is ready if something goes wrong

Without change management, uncontrolled changes can become the most frequent cause of operational disruptions.

---

### Planning IT Solutions

Good planning reduces risk and makes the project more predictable. A simple planning process can look like this:

1.**Needs assessment**– what does the organization want to achieve?
2.**Requirements specification**– technical and functional requirements
3.**Risk assessment (ROS analysis)**– what can go wrong, and what is the consequence?
4.**Solution proposals and selection**– evaluate alternatives
5.**Project plan**– timeline, responsibilities, milestones
6.**Implementation and testing**
7.**Documentation and handover**
8.**Evaluation**– were the requirements met?

See [[risikoanalyse-en]] for more on ROS analyses in an IT context.

---

## Example / Lab

### Systematic Troubleshooting in 5 Steps

>**Source:**Classroom notes (2ITA)
>
> When something stops working, do not panic. Go about it systematically with these steps:
>
> 1.**Observe**– What is happening (and what is not happening)? Read the entire error message, not just the first few words.
> 2.**Analyze**– What was the last thing that worked? What change was made just before the error? Often that is where the problem lies.
> 3.**Form hypotheses**– What does the computer need to do this? Test the hypothesis with concrete commands (e.g., `ping 8.8.8.8` to test network access).
> 4.**Use tools and read the error message**– Common patterns:
>    - `Permission denied`→ forgot`sudo`
>    - `Could not resolve host` → network or DNS problem
>    - `No such file or directory`→ wrong filename or wrong directory (check with`ls`)
> 5.**Search for knowledge**– Copy the entire error message (without usernames) into Google or an AI. Always provide context: OS version, what you are trying to do, and what is happening.
>
> Always document the solution in your log – it is worth its weight in gold the next time the same problem occurs.

*## Task: Create an IP Address Plan for a School Network

Given: A school with 80 students, 20 staff, 3 servers, 2 printers, and a guest network.

1. Choose a suitable private IP address space (e.g., 10.10.0.0/24 or 192.168.10.0/24).
2. Define at least 3 VLANs (e.g., staff, students, servers).
3. Calculate subnet sizes based on the number of devices.
4. Fill in a table with: VLAN number, name, subnet, gateway, DNS, DHCP range.
5. Specify static addresses for the servers.
6. Draw a simple topology in draw.io showing the VLAN structure.

*## Additional task: Write a procedure

CChoose one critical IT operation (e.g., adding a new user in Active Directory, or performing a backup).
CDocument the operation as a step-by-step procedure with title, responsible role, frequency, and expected result.

---

## Study Guide

### Core Content

DDocumentation and planning is about creating and maintaining an overview of the IT environment – so that operations,
Dtroubleshooting, and changes can be done in a controlled and efficient manner.

*## Types of documentation:
-**IP address plan**– overview of VLANs, subnets, gateway, DNS, DHCP, and static addresses
-**Network topology**– visual map of network components and connections (draw.io)
-**Operations log / change log**– chronological register of all changes
-**Procedure documentation**– step-by-step instructions for critical operations
-**CMDB**– register of all infrastructure

*## Network topologies:

- Star (most common): centralized switch, easy to troubleshoot
- Mesh: all connected to all, robust but complex
- Bus: historical, not used in modern networks

*## Planning process:
NNeeds assessment → Requirements → ROS analysis → Solution selection → Project plan → Implementation → Documentation →
NEvaluation

*## ITIL change management:
All changes are planned, risk-assessed, approved, implemented, documented. Rollback plan always ready.

***Remember:**Without documentation, the IT department depends on individuals' memory.
*Good documentation is a collective insurance policy.

---

## FAQ

*## Why is the change log more important than people think?
WWhen something stops working, the first question is always: "What did we change last?" The change log provides the
Wanswer immediately. Without it, you have to guess – which can take hours or days.

*## What is the difference between an operations log and a change log?
IIn practice, the terms are used interchangeably, but a change log specifically focuses on changes made (patching,
Iconfiguration, new user), while an operations log can include events, errors, and status more generally.

*## What is CMDB and is it necessary for a small school?
CCMDB (Configuration Management Database) is a detailed register of all IT infrastructure.
CCFor a small school, a simple Excel sheet or Markdown document is sufficient. Large organizations use dedicated CMDB
Ctools (e.g., ServiceNow) because the number of components is too large for manual tracking.

*## What is ITIL and do we need it?
IITIL is a framework of best practices for IT operations, originally developed for large organizations.
IIThe principles (change management, incident management, service management) are relevant at all scales, even if you do
Inot implement the entire framework. Having a change log and rollback process is ITIL thinking in its simplest form.

*## What is a ROS analysis in IT planning?
RROS (Risk and Vulnerability) analysis maps what can go wrong with a planned IT solution, how likely it is, and what the
Rconsequence would be. It provides a basis for prioritizing measures. See [[risikoanalyse-en]] for method and templates.

*## What makes draw.io a good documentation tool?
ddraw.io is free, web-based, and saves diagrams as XML files that can be version-controlled with git.
ddIt has specific symbol libraries for network topologies. The result is visual, easy-to-read diagrams that can be shared
dand updated easily.

---

## Quiz

<details><summary>Question 1: Why is a change log important in IT operations?</summary>

***Answer:**The change log provides a history of all changes made to the system. This is indispensable for
**troubleshooting (what did we change right before the problem occurred?), audits, onboarding new colleagues, and
*maintaining continuity when people leave.

</details>

<details><summary>Question 2: What is a star topology and what is its weakness?</summary>

***Answer:**A star topology connects all devices to a central switch. It is easy to troubleshoot and expand.
**The weakness is that the switch is a single point of failure – if the switch fails, all devices lose connectivity.
*This is mitigated with redundant switches.

</details>

<details><summary>Question 3: What should an IP address plan contain?</summary>

***Answer:**An IP address plan should at minimum contain: network address and subnet mask, gateway address, DNS
**server(s), DHCP range, and an overview of static addresses (servers, printers, network equipment).
*It can also include VLAN information and MAC addresses.

</details>

<details><summary>Question 4: What is CMDB?</summary>

***Answer:**CMDB (Configuration Management Database) is a register of all IT infrastructure in an organization: devices,
**software, configurations, and the relationships between them. It is the foundation for good change management and
*troubleshooting.

</details>

<<details><summary>Question 5: Name two tools used for network documentation and describe what they are used
<for.</summary>

***Answer:**draw.io is used to draw network topologies and architecture diagrams – visual and free.
**IT Glue is a professional documentation tool used by managed service providers (MSPs) that consolidates everything from
*password management to procedures and device registry in one system.

</details>

---

## Resources

- [Digdir: Referansearkitektur for datadeling](<https://www.digdir.no/nasjonal-arkitektur/referansearkitektur-for-datadeling/2131>)
- [Microsoft Azure Well-Architected Framework](<https://learn.microsoft.com/en-us/azure/architecture/framework/>)
- [draw.io (diagram drawing)](<https://app.diagrams.net/>)
- [[driftsarkitektur-en]]
- [[backup-og-gjenoppretting-en]]
- [[risikoanalyse-en]]
- [[dns-og-dhcp-en]]
- [[segmentering-og-vlan-en]]
