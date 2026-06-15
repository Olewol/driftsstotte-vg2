---
title: "Backup and Recovery"
emne: it-drift
competence_goals:
  - km-01
sources:
  - ndla
  - https://nsm.no/fagomrader/digital-sikkerhet/grunnprinsipper-for-ikt-sikkerhet-2-0/oppdage-og-handtere-hendelser/sikre-og-gjenopprette-data/
  - https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/
  - https://www.digdir.no/nasjonal-arkitektur/skytjenester/2153
  - https://learn.microsoft.com/en-us/azure/architecture/framework/
  - https://snl.no/skytjeneste
video: https://www.youtube.com/watch?v=iL8Lp8w0UIs
tags: []
flashcards: https://notebooklm.google.com/notebook/bc9a5656-7a9b-4dc5-a59e-ef4a96aa8ccd
public: true
notebooklm: true
language: en
original: backup-og-gjenoppretting.md
---

## Introduction

Data is one of the most valuable resources an organization has. Without a working backup, a single event – a failing hard drive, a ransomware attack, or a fire – can lead to permanent loss of critical information.

Backup is not just about making copies. It is about having a strategy that ensures data can be restored quickly enough and with low enough data loss for the organization to survive the incident. A backup is only valuable if it can actually be restored. In addition, the backup strategy should include system configurations and master images, not just raw data – so that the entire infrastructure can be restored, not just the files.

---

## Theory

### The 3-2-1 Rule

The 3-2-1 rule is the simplest and most recognized guideline for backup strategy:

- **3** – Keep at least 3 copies of data (1 primary + 2 backups)
- **2** – Store on at least 2 different media types (e.g., internal disk + external disk or NAS)
- **1** – Keep at least 1 copy stored offsite (outside the building – e.g., in the cloud or another location)

The offsite copy protects against physical events such as fire, flood, or burglary that could destroy all local equipment.

#### Modern extension: 3-2-1-1-0

Veeam and other experts recommend an extended version:

- **+1** – Have one immutable or air-gapped copy that cannot be deleted by ransomware
- **+0** – Zero errors in recovery testing (automatic verification of backups)

Immutable backup means data is locked and cannot be changed or deleted for a period of time. AWS S3 Object Lock is one example. Air-gapped backup is isolated from the network, so attackers cannot reach it.

---

### Backup Strategies

There are three main types of backup. The choice depends on RPO, storage capacity, and recovery time.

#### Full Backup

A complete copy of all selected data. Takes the longest time and requires the most storage space, but is easiest to restore from.

- Advantages: simple and fast recovery, complete dataset
- Disadvantages: requires a lot of storage space and time, impractical to run daily

#### Incremental Backup

Only copies data that has changed since the **last backup** (regardless of type – full or incremental).

- Advantages: fast and storage-friendly, small data size per backup
- Disadvantages: restoration requires the last full backup plus all subsequent incremental backups – time-consuming and vulnerable to chain errors

#### Differential Backup

Copies everything that has changed since the **last full backup**.

- Advantages: faster recovery than incremental (only full backup + one differential)
- Disadvantages: grows in size with each pass until the next full backup

| Type | Storage Usage | Backup Time | Recovery Time |
|------|-------------|-----------|-------------------|
| Full | Highest | Longest | Shortest |
| Differential | Medium (grows) | Medium | Medium |
| Incremental | Lowest | Shortest | Longest |

---

### RPO and RTO

Two concepts are essential for designing a backup strategy:

**RPO – Recovery Point Objective**
> "The maximum acceptable amount of data loss measured in time." – Microsoft Azure

RPO answers: *How much data can we afford to lose?*

Example: If an organization has an RPO of 4 hours, it means data from the last 4 hours can be lost without it being critical. Backups must then run at least every 4 hours.

**RTO – Recovery Time Objective**
> "The maximum acceptable time to restore business operations after a disaster occurs." – Microsoft Azure

RTO answers: *How long can we have downtime?*

Example: If the RTO is 2 hours, the IT team must have the systems back up within 2 hours after an incident.

#### Practical Example

A school stores student data and grade systems:
- **RPO: 24 hours** – grades cannot be re-entered further back than one day
- **RTO: 8 hours** – the system must be back up within one working day

Solution: daily full backup stored locally and in the cloud, with a clear recovery procedure documented and tested.

---

### Backup Tools

**Windows Server Backup**
Built-in tool in Windows Server. Adequate for simple backup setups, but limited functionality for complex environments.

**Veeam Backup & Replication**
Industry standard for virtualized environments (VMware, Hyper-V). Supports incremental backup, verification, and recovery down to individual files. Widely used in Norwegian businesses.

**Azure Backup**
Microsoft's cloud-based backup service. Easy to set up for Azure VMs and Windows Server. Naturally supports offsite storage.

**AWS S3 + Glacier**
Amazon S3 is used for active backup storage; Glacier is a cheaper archival storage option for data that is rarely needed but must be preserved.

---

### Backup Automation

Manual backup is prone to human error – the person who is sick on the day the backup should run, forgets it, or skips it "just this once." Automated backup routines eliminate this risk.

Good practices for automated backup:
- Schedule backup jobs outside working hours (e.g., at 02:00) for low impact on systems
- Configure automatic alerts on backup job failures
- Use script-based backup (e.g., [[powershell-grunnleggende-en]]) for custom needs
- Log all backup results and store logs separately from the backup system

---

### Recovery Testing

A backup that has never been tested is a backup you cannot rely on. Recovery testing should:

- Be carried out regularly (monthly or quarterly)
- Include actual restoration to a test environment – not just checking that files exist
- Be documented with result, date, and who performed the test
- Verify that the system works after recovery (not just that data is in place)

Veeam and Azure Backup support automatic verification (SureBackup / Instant Restore) as part of the backup process.

---

### Disaster Recovery

Disaster Recovery (DR) is a broader plan for what happens when large parts of the infrastructure fail. DR strategy includes:

- **Cold standby** – backup infrastructure that is set up manually when needed. Cheap, but long RTO.
- **Warm standby** – a partially pre-configured environment that can be activated quickly.
- **Hot standby / active-passive** – a fully parallel environment that is always ready. Lowest RTO, but most expensive.

The DR plan should be documented and practiced regularly. See [[dokumentasjon-og-planlegging-en]] for templates and procedure documentation.

---

## Example / Lab

**Task: Create a backup plan for a fictional school**

Given: A school with 500 students, grade system, file server, and email.

1. Define RPO and RTO for each of the systems (grade system, file server, email).
2. Choose backup strategy (full/incremental/differential) and frequency for each system.
3. Describe where backups are stored (local, NAS, cloud) – consider the 3-2-1 rule.
4. Create a simple recovery procedure for the file server (step-by-step).

**Additional task: Assess what should be included in the backup**

Discuss: Should a backup only contain data files, or should it also include system configuration, user lists, and network settings? What is the advantage of a complete system image versus a file-by-file backup?

---

## Study Guide

### Core Content

Backup and recovery is about ensuring that data can be restored in the event of loss or failure – and that this actually works in practice.

**The 3-2-1 rule (and 3-2-1-1-0):**
- 3 copies, 2 media, 1 offsite
- +1 immutable/air-gapped, +0 errors in testing
- Protects against physical events AND ransomware

**Backup strategies:**
- Full: largest, easiest to restore
- Incremental: smallest, fastest to run, complex to restore
- Differential: in between – simple recovery (full + one diff)

**RPO and RTO:**
- RPO = maximum acceptable data loss in time (determines backup frequency)
- RTO = maximum acceptable downtime (determines recovery speed requirements)

**DR strategies:**
- Cold standby (cheapest, longest RTO) → Warm standby → Hot standby (most expensive, shortest RTO)

**Key principle:** Backups that are not regularly tested are not reliable. Test, document, repeat.

---

## FAQ

**What is the difference between backup and archive?**
Backup is copies of active data that you want to be able to restore quickly. Archive is data that is no longer in active use but must be preserved for a long time (e.g., for legal requirements). AWS Glacier is an archival storage product – it is not suitable as a primary backup.

**Can we use RAID as backup?**
No. RAID protects against disk failure, not against accidental deletion, ransomware, or fire. RAID is redundancy, not backup. Both are needed in a complete strategy.

**What is an immutable backup in practice?**
It is backup data that is locked by the system so that no one can modify or delete it for a defined period (e.g., 30 days). AWS S3 Object Lock and Azure Immutable Blob Storage are examples. Even if a ransomware attacker gains access to the backup system, they cannot delete or encrypt immutable data.

**What is air-gap and is it practical in a school?**
Air-gap means the backup medium is physically disconnected from the network. An offline hard drive or tape medium in another room is air-gapped. It is practical and affordable for schools – but requires routines for regular updating.

**How often should we test backups?**
At least quarterly for a complete recovery test. Many choose monthly for critical systems. Most importantly, the test should actually verify that the system works after recovery – not just that the files are accessible.

**What is the difference between RPO and RTO with an example?**
RPO: "We can afford to lose a maximum of 4 hours of data." – Backup must run at least every 4 hours. RTO: "The system must be back up within 2 hours." – The recovery process and infrastructure must be dimensioned accordingly. A school grade system might have RPO 24h and RTO 8h; an online banking system might have RPO 0 (no loss) and RTO 15 min.

---

## Quiz

<details><summary>Question 1: What does the 3-2-1 rule mean?</summary>

**Answer:** 3 copies of data, stored on 2 different media types, with 1 copy offsite (outside the building). Protects against local disasters and media failure.

</details>

<details><summary>Question 2: What is the difference between RPO and RTO?</summary>

**Answer:** RPO (Recovery Point Objective) is the maximum acceptable data loss measured in time – i.e., how old a restored backup can be. RTO (Recovery Time Objective) is the maximum acceptable downtime – i.e., how long it takes to restore the system.

</details>

<details><summary>Question 3: What is the difference between incremental and differential backup?</summary>

**Answer:** Incremental backup only takes changes since the last backup (regardless of type). Differential backup takes all changes since the last full backup. Incremental is more storage-efficient, but recovery is more complex. Differential is easier to restore from.

</details>

<details><summary>Question 4: What is an immutable backup and why is it important against ransomware?</summary>

**Answer:** An immutable backup is locked and cannot be modified or deleted for a defined period. This means ransomware cannot encrypt or delete the backup data, even if attackers gain access to the backup system.

</details>

<details><summary>Question 5: Why is it important to test backups regularly?</summary>

**Answer:** A backup guarantees nothing until it is tested. Files can be corrupt, backup software can have errors, or the recovery process can take longer than the RTO allows. Regular testing uncovers these problems before they occur in a real crisis situation.

</details>

---

## Resources

- [Veeam: 3-2-1 Backup Rule](https://www.veeam.com/blog/321-backup-rule.html)
- [Microsoft Azure Well-Architected: Disaster Recovery](https://learn.microsoft.com/en-us/azure/well-architected/reliability/disaster-recovery)
- [NSM: Sikre og gjenopprette data](https://nsm.no/fagomrader/digital-sikkerhet/grunnprinsipper-for-ikt-sikkerhet-2-0/oppdage-og-handtere-hendelser/sikre-og-gjenopprette-data/)
- [YouTube: 3-2-1-regelen for backup – NetNordic](https://www.youtube.com/watch?v=iL8Lp8w0UIs)
- [[driftsarkitektur-en]]
- [[dokumentasjon-og-planlegging-en]]
