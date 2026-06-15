---
title: "IT Solutions with Built-in Security"
emne: sikkerhet
kompetansemaal:

  - km-10

kilder:

  - ndla
  - nsm
  - microsoft
  - <https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/>
  - <https://www.digdir.no/nasjonal-arkitektur/nulltillitsarkitektur/4054>
  - <https://www.datatilsynet.no/>
  - <https://owasp.org/www-project-top-ten/>
  - <https://www.digdir.no/informasjonssikkerhet/>

video: <https://www.youtube.com/watch?v=R9NCYvR3h3w>
notebooklm: true
tags: []
flashcards: <https://notebooklm.google.com/notebook/3e72e53a-b0ca-4f05-a597-a8eea5ea7ea9>
public: true
language: en
original: it-losninger-med-sikkerhet.md
---

## Introduction

Security is not something you add after a system is built. It is a design requirement that must be integrated from the first specification through ongoing operations. This article is about the principles and practices behind building and operating IT solutions where security is a natural part of the architecture — not an afterthought.

The Norwegian National Security Authority's (NSM) Fundamental Principles for ICT Security (v2.1, 2024) emphasize that good ICT security requires both technical and organizational measures throughout the entire lifecycle of a system. Here we look at the most important principles and methods.

The principles in this article are closely linked to [[brannmur-en|firewall and network security]], [[bruker-og-tilgangsstyring-en|user and access management]], and [[backup-og-gjenoppretting-en|backup and recovery]]. Good IT security is never a single measure – it is the sum of many overlapping layers.

---

## Theory

### Security by Design

**Security by Design**is the principle that security is integrated into all phases of system development and operations – from requirements specification, design, development, and testing, to production and decommissioning.

Microsoft's**SDL (Security Development Lifecycle)**is a reference model with these phases:

1. Training in secure coding
2. Requirements specification including security requirements
3. Threat modeling
4. Security-oriented design
5. Secure coding and code review
6. Security testing and penetration testing
7. Response and maintenance

The opposite – adding security after the system is built – is more expensive, harder, and yields weaker security. It's far easier to incorporate encryption and access control into a system from the start than to retrofit it into existing architecture.

---

### Zero Trust Model

**Zero Trust**is a security architecture based on the principle:

>**"Never trust, always verify"**

Traditional security thinking assumed that everything inside the corporate network was safe. Zero Trust rejects this assumption and treats all access as potentially dangerous – regardless of whether the user is inside or outside the corporate network.

**Three core principles (Microsoft Zero Trust):**

| Principle | What it means in practice |
|---|---|
|**Verify explicitly**| Authenticate based on all available data points: user identity, device, location, time |
|**Use least privilege**| Grant only the access that is strictly necessary. Use JIT (Just-In-Time) and JEA (Just-Enough-Access) |
|**Assume breach**| Design the system as if it is already compromised. Segment access, encrypt end-to-end, monitor actively |

**Practical Zero Trust measures:**

- MFA (multi-factor authentication) for all users – always
- Conditional Access: grant access only from approved devices with updated software
- Microsegmentation: limit which systems users and applications can reach
- No implicit trust in the corporate network – VPN alone is no longer enough

The Norwegian Digitalisation Directorate (Digdir) has published a Norwegian guide to zero trust architecture describing how Zero Trust is implemented in the public sector.

---

### Patch Management

Known vulnerabilities in software are one of the most common entry points for attackers. Patch management is the systematic process of keeping all software, firmware, and operating systems up to date.

**Patch cycle:**
1.**Identify:**map which systems and versions are in use (inventory list)
2.**Evaluate:**assess the severity of new patches (critical / important / moderate)
3.**Test:**test patches in a staging environment before production rollout
4.**Deploy:**distribute patches via management tools (WSUS, Intune, apt/yum)
5.**Verify:**confirm that patches are installed and systems are functioning

**Tools:**

- Windows:**WSUS**(Windows Server Update Services),**Microsoft Intune**
- Linux: `apt update && apt upgrade`(Debian/Ubuntu),`dnf update` (RHEL/Fedora)
- Network: vendor management portal for firmware

**NSM recommendation:**Critical patches should be installed within 24–72 hours. OWASP A06 (Vulnerable and Outdated Components) highlights that outdated components are one of the most common attack vectors.

Automating the patch process is key to reducing the vulnerability window – the shorter the time from a patch being available to it being installed, the less time attackers have to exploit known holes.

---

### Logging and SIEM

Logging is the recording of events in an IT system. Without logging, it is impossible to detect attacks, reconstruct event sequences, or investigate breaches.

**What should be logged:**

- Login attempts (successful and failed)
- Access changes (new users, modified permissions)
- System changes and configuration changes
- Firewall activity (blocked traffic)
- Application errors and security events

**SIEM (Security Information and Event Management):**
SIEM collects logs from all systems in a central location, correlates events, and alerts on suspicious activity.

-**Azure Monitor / Microsoft Sentinel:**cloud-based SIEM. Sentinel uses ML-based anomaly detection and can automatically trigger response.
-**Splunk, IBM QRadar:**commercial SIEM solutions
-**Wazuh, Graylog:**open-source alternatives

OWASP identifies insufficient logging and monitoring (A09) as a critical vulnerability – without logs, you don't know you are being attacked.

---

### Access Control and IAM

**IAM (Identity and Access Management)**is about controlling who can do what in IT systems.

**Principle of least privilege:**
Users, applications, and services should only have the access rights that are strictly necessary for their job. No user should have domain administrator rights on a daily basis.

**Role-Based Access Control (RBAC):**
Permissions are tied to roles (e.g., "Helpdesk," "Accounting Staff," "IT Admin"), not to individual users. Users are assigned roles.

**Tools:**
-**Active Directory (AD):**user accounts, groups, and permissions management on-premises. See [[active-directory-en]].
-**Azure Entra ID (formerly Azure AD):**cloud-based IAM. Supports SSO (Single Sign-On), MFA, and Conditional Access.
-**MFA:**combines something you know (password), something you have (authenticator app/SMS), and/or something you are (biometrics). Blocks over 99% of account takeovers according to Microsoft.

See also [[bruker-og-tilgangsstyring-en|user and access management]] for a practical walkthrough of access management.

---

### Backup as a Security Measure

Backup is not just an operational routine – it is a security measure and the most important reactive measure against ransomware.

**The 3-2-1 rule:**
-**3**copies of the data

- on**2**different media (e.g., disk + tape or disk + cloud)
- with**1**offsite copy (physical or cloud-based)

**Practical:**

- Test recovery regularly – a backup is worthless if it cannot be restored
- Isolate backup systems from the production network (ransomware encrypts everything it can reach)
- Azure Backup: integrated cloud backup for virtual machines, databases, and file servers

See [[backup-og-gjenoppretting-en|backup and recovery]] for a detailed review of backup strategies and recovery plans.

---

### BCDR – Business Continuity and Disaster Recovery

**Business Continuity (BC)**is about maintaining critical functions during a crisis.
**Disaster Recovery (DR)**is about restoring IT systems after a catastrophic event.

Key terms:

| Term | Explanation |
|---|---|
|**RTO (Recovery Time Objective)**| Maximum acceptable downtime – how long does recovery take? |
|**RPO (Recovery Point Objective)**| Maximum acceptable data loss – how old can the latest backup be? |
|**Failover**| Automatic transition to a redundant system upon failure |
|**DR plan**| Documented recovery procedure – tested regularly |

Example: A hospital may have RTO = 4 hours and RPO = 1 hour for its patient records system. This requires data replication at intervals of no more than 1 hour and a tested recovery procedure that takes under 4 hours.

---

### Defense in Depth

**Defense in Depth**(layered defense) is the principle that no single security mechanism is sufficient – security is built in layers, so that even if one layer fails, the next layer stops the attacker.

```
Layer 7: Data          → Encryption, access control, DLP
Layer 6: Application   → WAF, secure coding, patch management
Layer 5: Identity      → MFA, Zero Trust, IAM, RBAC
Layer 4: Network       → Firewall, DMZ, segmentation, IPS
Layer 3: Computer      → Antivirus/EDR, host-based firewall, OS patches
Layer 2: Physical      → Server room access control, locked racks
Layer 1: Policies      → Security policies, training, procedures
```

Azure explicitly uses this model in its security documentation.

Microsegmentation is a concrete measure for implementing Defense in Depth at the network level: by limiting which systems and services can communicate with each other, the damage radius is dramatically reduced if one system is compromised.

---

## Example / Lab

**Scenario: Assess the security level of a fictional school network**

Solberg Upper Secondary School has the following IT infrastructure:

- Windows Server 2022 (AD, file server, WSUS)
- 350 Windows 11 clients managed via Intune
- Microsoft 365 with Entra ID and MFA enabled for employees
- Ubiquiti router with VLANs for staff, students, and guests
- Firewall with stateful inspection, default-deny
- Daily backup to Azure Backup with offsite copy

**Evaluate using the Defense in Depth model:**

| Layer | Present measures | Gaps |
|---|---|---|
| Policies | Security policy exists | No regular phishing training |
| Physical | Server room is locked | No access log |
| Network | VLAN segmentation, firewall | IDS/IPS missing |
| Computer | Windows Defender EDR | Student PCs lack Intune management |
| Identity | MFA for staff | MFA not enabled for students |
| Application | WSUS patching | Application software patched manually |
| Data | Azure Backup | Backup recovery not tested in the last 6 months |

**Conclusion:**Good basic security. Priority improvements: enable MFA for students, implement IDS, integrate student PCs into Intune, and plan quarterly DR testing.

---

## Study Guide

### IT Solutions with Built-in Security – Core Content

**Security by Design:**
Security must be built in from the start – in requirements specification, design, and development – not added as an afterthought. Microsoft's SDL is the reference model with seven phases from training to response.

**Zero Trust:**
The starting point is that no one – neither users, devices, nor networks – is automatically trusted. The three principles are: verify explicitly, use least privilege, and assume breach. MFA and Conditional Access are the most important practical measures.

**Patch Management:**
A structured process: identify → evaluate → test → deploy → verify. Critical patches should be installed within 72 hours. OWASP A06 highlights that outdated components are one of the most common attack vectors.

**Logging and SIEM:**
Logging is the prerequisite for detecting attacks. SIEM collects logs centrally and correlates them. OWASP A09 covers insufficient logging. Microsoft Sentinel is a cloud-based SIEM with ML-driven anomaly detection.

**IAM and Least Privilege:**
Users only get the access they actually need. RBAC ties permissions to roles, not individuals. Active Directory on-premises and Azure Entra ID in the cloud are the primary tools.

**Backup and BCDR:**
The 3-2-1 rule is the standard. RTO defines maximum downtime, RPO defines maximum data loss. Backup is worthless without tested recovery. Isolation from the production network is critical against ransomware.

**Defense in Depth:**
Security in layers – policies, physical, network, computer, identity, application, data. No single mechanism is sufficient alone.

---

## FAQ

**What is the difference between Security by Design and Privacy by Design?**
Security by Design is about integrating information security in general into all phases of system development. Privacy by Design (GDPR Art. 25) is specifically about integrating privacy considerations from the start. They overlap significantly, but Privacy by Design is a legal requirement, while Security by Design is a professional best practice.

**Why is VPN no longer sufficient with Zero Trust?**
Traditional VPN gives full access to the corporate network once connected. Zero Trust replaces this with conditional access: even authenticated users inside the network must be continuously verified, and they only get access to the specific resources they need.

**What are JIT and JEA?**
JIT (Just-In-Time) grants temporary, time-limited access to sensitive systems – only when necessary. JEA (Just-Enough-Access) ensures the access is minimized to exactly what is needed. Both reduce the attack surface if an account is compromised.

**Why is it important to test backup recovery?**
A backup that cannot be restored is worthless. Files can become corrupted, the backup process can fail silently, or the recovery procedure may take much longer than the RTO allows. Regular testing reveals these issues before they become critical.

**What is the difference between RTO and RPO?**
RTO (Recovery Time Objective) is the maximum acceptable downtime – how long it can take to restore the system. RPO (Recovery Point Objective) is the maximum acceptable data loss – how old the latest backup can be. A hospital may have RTO = 4 hours and RPO = 1 hour, while a blog may accept RTO = 24 hours and RPO = 7 days.

**What is meant by microsegmentation?**
Microsegmentation divides the network into very fine-grained zones – down to individual application or server level – with firewall rules between them. This drastically limits lateral movement: even if a server is compromised, the attacker cannot move freely to other systems.

**How do SIEM and logging relate to threat detection?**
Logging alone gives you raw data – you cannot manually read through millions of log lines. SIEM automates analysis, correlates events across systems (e.g., failed login + new user created + large file download = alarm), and alerts on patterns that indicate attacks.

---

## Quiz

<details><summary>Question 1: What are the three core principles of Zero Trust?</summary>

**Answer:**Verify explicitly, Use least privilege, and Assume breach. Together, this means no user, device, or network is automatically trusted – all access is verified and limited.

</details>

<details><summary>Question 2: What is the 3-2-1 rule for backup?</summary>

**Answer:**3 copies of the data, on 2 different media, with 1 offsite copy. The offsite copy ensures that backups survive local disasters such as fire or ransomware attacks.

</details>

<details><summary>Question 3: What is the difference between RTO and RPO?</summary>

**Answer:**RTO (Recovery Time Objective) is the maximum acceptable downtime – how long recovery can take. RPO (Recovery Point Objective) is the maximum acceptable data loss – how old the latest backup can be.

</details>

<details><summary>Question 4: Why is patch management important for security?</summary>

**Answer:**Known vulnerabilities in software are one of the most common attack vectors. Patches close these vulnerabilities. Outdated components (OWASP A06) are consistently among the most frequent causes of compromises.

</details>

<details><summary>Question 5: What is SIEM, and which vulnerability does OWASP associate with insufficient logging?</summary>

**Answer:**SIEM (Security Information and Event Management) collects logs from all systems centrally, correlates events, and alerts on suspicious activity. OWASP Top 10 A09 identifies insufficient logging and monitoring as a critical vulnerability – without logs, you cannot detect attacks.

</details>

---

## Resources

- [Microsoft – Zero Trust Overview](<https://learn.microsoft.com/en-us/security/zero-trust/zero-trust-overview>)
- [Microsoft – Azure Security Overview](<https://learn.microsoft.com/en-us/azure/security/fundamentals/overview>)
- [NSM Fundamental Principles – Protect and Maintain](<https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/>)
- [NDLA – Updating Linux with APT](<https://ndla.no>)
- [NDLA – User Accounts in Active Directory](<https://ndla.no>)
- [NSM – Fundamental Principles for ICT Security (full version)](<https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/>)
- [Digdir – Zero Trust Architecture (Norwegian)](<https://www.digdir.no/nasjonal-arkitektur/nulltillitsarkitektur/4054>)
- [YouTube: What is Zero Trust? (IBM Technology, 6 min)](<https://www.youtube.com/watch?v=R9NCYvR3h3w>)
