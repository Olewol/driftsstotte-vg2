---
title: "Risk Analysis"
emne: sikkerhet
kompetansemaal:

  - km-08

kilder:

  - ndla
  - nsm
  - datatilsynet
  - <https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/vurdere-risiko-og-personvernkonsekvenser/risikovurdering/>
  - <https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/>
  - <https://www.datatilsynet.no/>
  - <https://owasp.org/www-project-top-ten/>
  - <https://www.digdir.no/informasjonssikkerhet/>

notebooklm: true
video: <https://www.youtube.com/watch?v=DejxGE91xJY>
tags: []
flashcards: <https://notebooklm.google.com/notebook/3e72e53a-b0ca-4f05-a597-a8eea5ea7ea9>
public: true
language: en
original: risikoanalyse.md
---

## Introduction

AA risk analysis is a structured tool for identifying what can go wrong with an IT system, how likely it is, and what the
AAconsequences will be. The purpose is not to eliminate all risk – that is impossible – but to understand the risk well
Aenough to prioritize the right measures.

NNSM's Fundamental Principles for ICT Security (v2.1, 2024) places "Identify and map" as the first and fundamental step.
NNGDPR Article 32 also requires that all organizations processing personal data conduct a risk assessment as the basis
Nfor their security measures.

RRisk analysis is the foundation that connects [[trusselbildet-en|the threat landscape]] (which threats exist?) to
RR[[it-losninger-med-sikkerhet-en|IT solutions with built-in security]] (which measures are appropriate?).
RRWithout risk analysis, you risk spending resources on the wrong problems. Remember also that GDPR Art.
R32 makes this a legal requirement where [[personvern-en|privacy]] is involved.

---

## Theory

### What is Risk?

**Risk**is defined as the product of probability and consequence:

>**Risk = Probability × Consequence**

-**Probability:**How likely is it that the event will occur? (very low / low / medium / high / very high)
--**Consequence:**What is the extent of damage if the event occurs? (negligible / minor / moderate / serious / very
-serious)

AAn event with low probability but catastrophic consequences can be just as important to address as an event that occurs
Afrequently but causes minor damage.

---

### 4-Step Risk Analysis Process

#### Step 1: Identify Assets and Threats

**Assets**are everything that has value and could be affected:

- Hardware (servers, network equipment, PCs)
- Software and systems
- Data (personal data, financial records, intellectual property)
- Services (email, ERP, website)
- Employees and competence

**Threats**are events that can harm the assets:

- Ransomware attacks
- Phishing targeting employees
- Fire or flooding in the server room
- Power outage
- Human error (accidentally deleting files)
- Insider threats

#### Step 2: Identify Vulnerabilities

A vulnerability is a weakness that allows a threat to materialize:

- Outdated software without patches
- Weak passwords or missing MFA
- Missing firewall
- No backup routine
- Employees not trained in phishing recognition

#### Step 3: Assess and Rank Risk

Use the**risk matrix**(5×5) to place and rank risk scenarios:

||  | **1 Negligible** | **2 Minor** | **3 Moderate** | **4 Serious** | **5 Very serious** |
|| --- | --- | --- | --- | --- | --- |
|| **5 Very high** | 5 | 10 | 15 | 20 | **25** |
|| **4 High** | 4 | 8 | 12 | **16** | **20** |
|| **3 Medium** | 3 | 6 | **9** | 12 | 15 |
|| **2 Low** | 2 | 4 | 6 | 8 | 10 |
|| **1 Very low** | 1 | 2 | 3 | 4 | 5 |

*Color code: 1–4 = low (green), 5–9 = medium (yellow), 10–19 = high (orange), 20–25 = critical (red)*

UUse the color codes actively when presenting the risk matrix – red risks must be prioritized immediately, yellow risks
Ushould be evaluated, green risks can be accepted with periodic review.

#### Step 4: Propose Measures and Accept Residual Risk

For each high or critically ranked risk scenario, the organization chooses one of four options:

|| Strategy | Explanation |
|| --- | --- |
|| **Reduce** | Implement measures that lower probability or consequence |
|| **Avoid** | Stop the activity that creates the risk |
|| **Transfer** | Insure against the risk (e.g., cyber insurance) |
|| **Accept** | Management approves that the risk is within an acceptable level |

***Residual risk**is the risk that remains after measures have been implemented. Management must formally accept the
**residual risk. The acceptable risk level should be defined in advance – this makes it clear to everyone when residual
*risk is "good enough."

---

### Types of Measures

|| Type | Description | Example |
|| --- | --- | --- |
|| **Preventive** | Prevents the event from occurring | Patches, MFA, firewall |
|| **Detective** | Detects that something is happening | Logging, IDS, antivirus monitoring |
|| **Reactive (corrective)** | Limits damage after the event | Backup, incident response plan, DR plan |

GGood security practice combines all three types – you cannot only prevent; you must also detect and react.
GOrganizational measures (training, routines, policies) are just as important as technical measures.

---

### GDPR Article 32 and Risk Assessment

GGDPR Article 32 requires organizations that process personal data to implement "appropriate technical and organizational
Gsecurity measures" based on a risk assessment. The assessment must take into account:

- The nature, scope, context, and purpose of the processing
- The likelihood and severity of the risk to the rights of data subjects

TThis means risk analysis is not just good practice – it is a legal requirement if you process personal data.
TTThe Norwegian Data Protection Authority (Datatilsynet) has published a specific guide for risk assessment of personal
Tdata.

---

## Example / Lab

### Risk Analysis for Bakke Upper Secondary School – School Network

***Scenario:**Bakke vgs has a school network with the following components: Active Directory server, file server with
*student work, wireless guest network, 350 student computers, and staff PCs.

*## Step 1 – Identify assets and threats:

|| Asset | Threat |
|| --- | --- |
|| AD server | Ransomware, password attacks |
|| File server with student work | Ransomware, accidental deletion, fire |
|| Wireless guest network | Unauthorized access, sniffing attacks |
|| Staff PCs | Phishing, malware via USB |

*## Step 2 – Identify vulnerabilities:

- AD server runs Windows Server 2016 without automatic patching
- Staff use simple passwords without MFA
- Guest network has no VLAN isolation from the internet
- No backup routine is tested regularly

*## Step 3 – Risk matrix (selection):

|| Scenario | Probability | Consequence | Risk value |
|| --- | --- | --- | --- |
|| Ransomware against file server | 3 (medium) | 5 (very serious) | **15 – high** |
|| Phishing targeting staff | 4 (high) | 3 (moderate) | **12 – high** |
|| Fire in server room | 1 (very low) | 5 (very serious) | **5 – medium** |
|| Student connects malware via USB | 3 (medium) | 2 (minor) | **6 – medium** |

*## Step 4 – Measures:

|| Risk | Measure | Type |
|| --- | --- | --- |
|| Ransomware against file server | Implement automatic patching, install backup with offsite copy | Preventive + reactive |
|| Phishing targeting staff | Mandatory phishing training, enable MFA on all accounts | Preventive |
|| Fire in server room | Fire suppression system, offsite backup, DR plan | Preventive + reactive |
|| USB use | Disable USB ports via GPO, only allow approved devices | Preventive |

***Residual risk:**The ransomware risk is reduced from 15 to approximately 6 (medium) after measures.
*Management accepts the residual risk.

---

### Classroom Case: Risk Assessment for MediaHuset AS

>**Source:**Classroom notes (2ITA)
>
> In class, students conduct a risk assessment for a fictional Dark Web lab that investigative journalists at "MediaHuset AS" plan to use. The case illustrates structured risk management:
>
>**Three assets to protect:**
> - The company's main network
> - Source protection / journalist anonymity
> - Company reputation
>
>**Three identified threats:**
> - Journalist downloads malware that spreads to the corporate network
> - Journalist logs into personal Facebook via Tor and is exposed (breaking anonymity)
> - Cleaner inserts an infected USB drive into the lab machine
>
>**Assessment:**For each threat, probability and consequence are evaluated (Low/Medium/High). The most dangerous combination (typically malware spread with High consequence) requires a concrete measure – for example, physically disconnecting the lab machine from the corporate network and using a dedicated 4G router.
>
>**The point of the case:**Risk management is not gut feeling, but a structured process: define assets → identify threats → assess probability and consequence → propose measures.

---

## Study Guide

### Risk Analysis – Core Content

*## The basic formula:
RRisk = Probability × Consequence. Both are typically assessed on a scale of 1–5. A risk value of 1–4 is low (green), 5–9
Rmedium (yellow), 10–19 high (orange), 20–25 critical (red).

*## The 4-step model:

1. Identify assets and threats – what is worth protecting, and what could harm it?
2. Identify vulnerabilities – what weaknesses make the threats possible?
3. Assess and rank risk – use the risk matrix
4. Propose measures and accept residual risk – choose reduce/avoid/transfer/accept

*## Three types of measures:
PPreventive (stops the event), detective (reveals that something is happening), reactive (limits damage afterward).
PAll three are necessary – they complement each other.

*## Residual risk:
NNot all risk can be eliminated. Management formally accepts the risk that remains after measures.
NAn acceptable risk level should be set in advance.

*## GDPR Art. 32:
RRisk assessment is a legal requirement for anyone processing personal data. Measures must be proportionate to the risk
Rto data subjects' rights.

*## Practical advice:

- Always include organizational measures (training, routines), not just technical ones
- Document the analysis and measures – accountability requires documentation
- Review and update the analysis regularly, not just once

---

## FAQ

*## What is the difference between a threat and a vulnerability?
AA threat is a potential event that can harm your assets, e.g., ransomware or fire.
AAA vulnerability is a weakness that allows the threat to materialize, e.g., missing backup or outdated software.
AThe threat exists regardless – the vulnerability determines whether it actually affects you.

*## Why is it important to involve management in the risk analysis?
MManagement are the only ones who can accept residual risk on behalf of the organization.
MMThey also decide resources for security measures. A risk analysis that does not reach management rarely leads to actual
Mimprovements.

*## What is a ROS analysis?
RROS (Risk and Vulnerability Analysis) is the Norwegian term for risk analysis. It follows the same 4-step model, but the
Rterm is particularly used in Norwegian public sector and in NVE's requirements for critical infrastructure.

*## Can residual risk always be accepted?
NNot always. Some risks are too high to accept – then you must either reduce them further, avoid the activity entirely,
NNor transfer the risk (e.g., through cyber insurance). If residual risk is still critical (20–25) after all measures,
Nthe activity should be reconsidered.

*## What is the difference between preventive and reactive measures?
PPreventive measures stop the event from occurring (e.g., MFA, patches, firewall). Reactive measures come into effect
PPafter the event has occurred and limit the damage (e.g., backup recovery, incident response plan).
PYou need both – prevention reduces probability, reactive measures reduce consequence.

*## What does it mean that a measure is "appropriate" under GDPR Art. 32?
AAppropriateness is assessed against the risk. A hospital processing sensitive health data requires stricter measures
AAthan a restaurant storing contact information. Measures must be proportionate to the likelihood and severity of the
Arisk to data subjects.

*## How often should the risk analysis be updated?
AAt least once a year, and always after significant changes in the IT environment (new software, new vendor, new
Aequipment) or after a security incident. The threat landscape changes – the analysis must keep pace.

---

## Quiz

<details><summary>Question 1: What is the formula for risk?</summary>

**Answer:**Risk = Probability × Consequence. Both factors are typically assessed on a scale from 1 to 5.

</details>

<details><summary>Question 2: What are the four steps in a risk analysis process?</summary>

*## Answer:

1. Identify assets and threats
2. Identify vulnerabilities
3. Assess and rank risk (risk matrix)
4. Propose measures and accept residual risk

</details>

<details><summary>Question 3: What is the difference between preventive, detective, and reactive measures?</summary>

***Answer:**Preventive measures stop the event from occurring (e.g., firewall, MFA).
**Detective measures reveal that something is happening (e.g., logging, IDS). Reactive measures limit damage after the
*event (e.g., backup, incident response plan).

</details>

<details><summary>Question 4: What does GDPR Article 32 require?</summary>

***Answer:**GDPR Article 32 requires organizations that process personal data to conduct a risk assessment and implement
*appropriate technical and organizational security measures based on that assessment.

</details>

<details><summary>Question 5: What is residual risk?</summary>

***Answer:**Residual risk is the risk that remains after measures have been implemented.
*It is not possible to eliminate all risk – management must formally accept the remaining risk.

</details>

---

## Resources

- [NSM Fundamental Principles for ICT Security (Norwegian)](<https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/>)
- [Datatilsynet – Risk Assessment and Privacy (Norwegian)](<https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/risikovurdering/>)
- [NDLA – Risk Assessment for Office Administration (Norwegian)](<https://ndla.no>)
- [Datatilsynet – Guide for Risk Assessment of Personal Data (Norwegian)](<https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/vurdere-risiko-og-personvernkonsekvenser/risikovurdering/>)
