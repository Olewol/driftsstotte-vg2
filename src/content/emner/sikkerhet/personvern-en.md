---
title: "Privacy and GDPR"
emne: sikkerhet
kompetansemaal:
  - km-11
kilder:
  - ndla
  - datatilsynet
  - https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/
  - https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/
  - https://www.datatilsynet.no/
  - https://owasp.org/www-project-top-ten/
  - https://www.digdir.no/informasjonssikkerhet/
video: https://www.youtube.com/watch?v=u6p_G7w89Uo
notebooklm: true
tags: []
flashcards: https://notebooklm.google.com/notebook/3e72e53a-b0ca-4f05-a597-a8eea5ea7ea9
public: true
language: en
original: personvern.md
---

## Introduction

Privacy is about an individual's right to control information about themselves. In our digital everyday lives – where apps, services, and organizations collect enormous amounts of data about us – privacy is both a fundamental right and a legal requirement.

In the EU and Norway, privacy is regulated by **GDPR** (General Data Protection Regulation), an EU regulation that came into force in May 2018. GDPR applies in Norway through the EEA Agreement and is implemented in Norwegian law via the **Personal Data Act**. For those working in IT operations, privacy is not something the legal department handles alone – technical choices like database structure, access control, logging, and backup have direct privacy implications.

As an IT operations professional, you will encounter privacy in connection with [[kryptering-en|encryption]] (GDPR requires encryption of personal data), [[bruker-og-tilgangsstyring-en|user and access management]] (who has access to personal data?), and [[risikoanalyse-en|risk analysis]] (GDPR Art. 32 requires risk assessment as a basis for security measures). Privacy is not isolated legal theory – it is technical practice.

---

## Theory

### The 7 Privacy Principles (GDPR Art. 5)

GDPR Article 5 establishes seven fundamental principles for processing personal data. All organizations that process personal data are required to follow these:

| No | Principle | Brief explanation |
|---|---|---|
| 1 | **Lawfulness, fairness and transparency** | Processing must have a legal basis and be transparent to the data subjects |
| 2 | **Purpose limitation** | Data is collected for a specific purpose and cannot be used for anything else without a new legal basis |
| 3 | **Data minimization** | Only the data necessary for the purpose should be collected |
| 4 | **Accuracy** | Personal data must be correct and kept up to date |
| 5 | **Storage limitation** | Data must be deleted when it is no longer necessary for the purpose |
| 6 | **Integrity and confidentiality** | Appropriate technical and organizational measures must secure data against unauthorized access and loss |
| 7 | **Accountability** | The organization must be able to demonstrate compliance with all principles |

---

### Legal Basis for Processing (GDPR Art. 6)

To process personal data lawfully, you always need a **legal basis**. GDPR Art. 6 lists six valid bases:

1. **Consent** – The data subject has given explicit, informed consent. Can be withdrawn at any time.
2. **Contract** – Processing is necessary to fulfill a contract with the data subject
3. **Legal obligation** – The organization is legally required to process the data (e.g., tax records)
4. **Vital interests** – Necessary to protect the data subject's life
5. **Public interest** – Necessary to perform a task in the public interest
6. **Legitimate interest** – The organization's interest outweighs the data subject's privacy interest

For special categories of personal data (health information, political opinions, ethnic origin, etc.), stricter rules apply (GDPR Art. 9).

---

### Data Subject Rights

GDPR gives individuals a number of rights that organizations are obligated to fulfill:

| Right | Explanation |
|---|---|
| **Access (Art. 15)** | Right to know what information is being processed about you |
| **Rectification (Art. 16)** | Right to correct inaccurate information |
| **Erasure (Art. 17)** | "Right to be forgotten" – deletion of data when it is no longer necessary |
| **Data portability (Art. 20)** | Right to receive your data in a machine-readable format and transfer it to another provider |
| **Objection (Art. 21)** | Right to object to processing based on legitimate interest |
| **Restriction (Art. 18)** | Right to demand that processing be restricted in certain situations |

---

### Privacy by Design

**Privacy by Design** is the principle that privacy must be integrated into system design from the start, not added afterward. This is codified in GDPR Art. 25.

Practical examples:
- Encrypt all data storage from day one – not as an afterthought
- Only collect necessary fields in registration forms (data minimization)
- Implement access control so that only authorized users see sensitive data
- Automatically delete data after a specified period (storage limitation)
- Pseudonymization: replace direct identifiers with pseudonyms in test databases

Privacy by Design is the sister principle to Security by Design – both are about security (and privacy) being a design requirement, not an afterthought. See [[it-losninger-med-sikkerhet-en|IT solutions with built-in security]] for Security by Design in a broader context.

---

### Controller and Processor

A key distinction in GDPR is the roles in the processing chain:

- **Controller:** The organization or person that determines the purpose of processing personal data and which tools to use. The controller has the overall legal responsibility.
- **Processor:** An external party (e.g., a cloud service) that processes personal data on behalf of the controller.

This distinction is crucial for who is responsible if something goes wrong, and it governs which agreements are required between the parties.

---

### Data Protection Officer (DPO)

Some organizations are required to have a **Data Protection Officer (DPO)**. This applies to:
- Public authorities (all Norwegian municipalities, agencies, etc.)
- Organizations that carry out systematic monitoring of individuals on a large scale
- Organizations that process special categories of personal data on a large scale

The DPO serves as an internal expert and point of contact for the Data Protection Authority (Datatilsynet).

---

### Data Processing Agreement (GDPR Art. 28)

When an organization uses a third party to process personal data on its behalf (e.g., a cloud solution, a payroll system, an email service), a **data processing agreement** is required. The agreement regulates what the processor can do with the data and ensures it is only used for the specified purpose.

Example: A Norwegian school uses Microsoft 365. The school is the **controller**, Microsoft is the **processor**, and a data processing agreement must be in place.

An important practical task for IT managers is to maintain an overview of all subcontractors and cloud services that process personal data on behalf of the organization and ensure that valid data processing agreements are in place for all of them.

---

### Personal Data Breach and Notification Obligation

If personal data is compromised (unauthorized access, data loss, incorrect disclosure), a **personal data breach** has occurred.

**GDPR Art. 33 – The 72-hour rule:**
Breaches that pose a risk to data subjects must be notified to the Data Protection Authority (Datatilsynet) within **72 hours** of the organization becoming aware of the breach. The notification must include:
- Description of the breach (what happened)
- Categories and approximate number of affected individuals
- Possible consequences
- Measures taken or proposed

**GDPR Art. 34:** Breaches that pose a high risk to data subjects must also be communicated directly to the affected individuals without undue delay.

Incident management – the routines for detecting, stopping, and reporting breaches – is a requirement GDPR places on all organizations. IT operations staff are often the first to discover a breach.

---

### Datatilsynet and Sanctions

**Datatilsynet** is the Norwegian supervisory authority for privacy. Datatilsynet:
- Enforces GDPR and the Personal Data Act
- Provides guidance to organizations and individuals
- Can impose administrative fines

**Sanctions under GDPR:**
- Up to **€10 million** or 2% of global annual turnover for technical breaches (Art. 83.4)
- Up to **€20 million** or 4% of global annual turnover for fundamental breaches (Art. 83.5)

*Example: Meta was fined €1.2 billion by the Irish Data Protection Commission in 2023 for unlawfully transferring European users' data to the United States.*

---

### Consequences of Personal Data Breaches

**For individuals:**
- Identity theft and fraud (leaked ID numbers, account numbers)
- Psychological harm and loss of control over one's own life
- Discrimination (leaked information about health, sexuality, political beliefs)
- Stalking and harassment (leaked address or location data)

**For organizations:**
- Multi-million euro fines from the Data Protection Authority
- Damaged reputation and loss of customer trust
- Lawsuits from affected parties
- Loss of public sector contracts

**For society:**
- Reduced trust in digital services
- Increased resistance to necessary digitalization
- Potential misuse of personal data in political campaigns (Cambridge Analytica scandal)
- Threat to freedom of expression when people know they are being monitored

---

## Example / Lab

**Scenario: Assess privacy implications**

You are the IT manager at Solberg Middle School. The school is considering implementing a new system that uses facial recognition to automatically register student attendance.

Consider the following:

1. **Legal basis:** What is the basis for processing biometric data? Consent from students? From guardians? Is this sufficient for biometric data (Art. 9)?

2. **Data minimization:** Is facial recognition necessary for attendance registration, or could this be achieved with simpler methods?

3. **Privacy by Design:** If the school proceeds – what technical measures should be integrated from the start? (encryption of biometric database, restricted access, automatic deletion at the end of the school year)

4. **Notification:** If the biometric database is leaked – who do you notify, within what deadline, and what do you write?

**Conclusion:** Such a system would almost certainly require a DPIA (Data Protection Impact Assessment, GDPR Art. 35) because it involves systematic processing of biometric data about children.

---

## Study Guide

### Privacy and GDPR – Core Content

**What is GDPR?**
GDPR is the EU's privacy regulation, applicable in Norway through the EEA Agreement. It gives individuals rights over their personal data and sets requirements for all organizations that process such data. Datatilsynet is the Norwegian supervisory authority.

**The 7 principles (GDPR Art. 5):**
Lawfulness/fairness/transparency, purpose limitation, data minimization, accuracy, storage limitation, integrity/confidentiality, accountability. All are mandatory.

**Legal basis (GDPR Art. 6):**
You always need a basis to process personal data: consent, contract, legal obligation, vital interests, public interest, or legitimate interest. Without a basis, the processing is unlawful.

**Data subject rights:**
Access, rectification, erasure ("right to be forgotten"), data portability, objection, and restriction. Organizations are obligated to fulfill these rights within specified deadlines.

**Privacy by Design:**
Privacy is integrated from the start of system development – not added afterward. Encryption, data minimization, automatic deletion, and access control are technical measures implemented from day one.

**The 72-hour rule:**
Personal data breaches posing a risk to data subjects must be notified to Datatilsynet within 72 hours. High-risk breaches must also be communicated directly to affected individuals.

**Sanctions:**
Up to €20 million or 4% of global annual turnover for serious breaches. Privacy is not just ethical – it is a legal requirement with dramatic consequences for non-compliance.

---

## FAQ

**What is the difference between a controller and a processor?**
The controller determines the purpose of processing and has the overall legal responsibility. The processor (e.g., a cloud service) processes data on behalf of the controller according to instructions. A school is the controller; Microsoft is the processor for Microsoft 365.

**Do you always need to obtain consent to process personal data?**
No. Consent is only one of six legal bases. An employer does not need consent to process salary information – it is necessary to fulfill a contract. Many public authorities process personal data based on legal obligation.

**What is a DPIA?**
DPIA (Data Protection Impact Assessment) is a privacy impact assessment required by GDPR Art. 35 when processing is likely to result in high risk to individuals. Examples: systematic monitoring, processing of biometric data, or new technology with unknown privacy implications.

**What are pseudonymization and anonymization?**
Pseudonymization replaces direct identifiers (name, ID number) with a pseudonym – data can still be linked back to the person with additional information. Anonymization removes all possibility of identification – the data then falls outside GDPR scope. Pseudonymization is a GDPR measure; anonymization removes GDPR requirements.

**What does "right to be forgotten" mean in practice?**
Individuals can demand that organizations delete personal data about them when the data is no longer necessary, consent is withdrawn, or there is no other legal basis. The right is not absolute – it can be overridden by statutory retention requirements (e.g., accounting data).

**What must the notification to Datatilsynet contain?**
A description of the breach, categories and approximate number of affected persons and personal data records, possible consequences for data subjects, and measures taken or proposed to address the breach and mitigate harm.

**How does GDPR distinguish between regular and special category personal data?**
GDPR Art. 9 defines special categories (sensitive data): health information, biometric data, genetic data, ethnic origin, political opinions, religious beliefs, trade union membership, and sexual orientation. These require a stricter legal basis and additional security measures.

---

## Quiz

<details><summary>Question 1: What are the seven privacy principles in GDPR Article 5?</summary>

**Answer:** Lawfulness, fairness and transparency / Purpose limitation / Data minimization / Accuracy / Storage limitation / Integrity and confidentiality / Accountability.

</details>

<details><summary>Question 2: What is the 72-hour rule in GDPR?</summary>

**Answer:** GDPR Art. 33 requires that personal data breaches posing a risk to data subjects must be notified to the Data Protection Authority within 72 hours of the organization becoming aware of the breach.

</details>

<details><summary>Question 3: What is Privacy by Design?</summary>

**Answer:** Privacy by Design is the principle that privacy must be integrated into system design from the start, not added afterward. It is codified in GDPR Art. 25 and involves measures such as encryption, data minimization, and access control from day one.

</details>

<details><summary>Question 4: What is a data processing agreement, and when is it required?</summary>

**Answer:** A data processing agreement (GDPR Art. 28) is required when an organization uses a third party to process personal data on its behalf. The agreement regulates what the third party can do with the data. Example: a school using Microsoft 365 must have a data processing agreement with Microsoft.

</details>

<details><summary>Question 5: What consequences can a personal data breach have for individuals?</summary>

**Answer:** Identity theft, fraud, psychological harm, discrimination, stalking/harassment, and loss of control over one's own life. Breaches involving sensitive categories (health, sexuality, politics) can have particularly serious consequences.

</details>

---

## Resources

- [Datatilsynet – The Privacy Principles (Norwegian)](https://www.datatilsynet.no/rettigheter-og-plikter/personvernprinsippene/)
- [Datatilsynet – Rights and Obligations (Norwegian)](https://www.datatilsynet.no/rettigheter-og-plikter/)
- [dubestemmer.no – Privacy for Youth (Norwegian)](https://www.dubestemmer.no)
- [slettmeg.no – Help to Delete Content Online (Norwegian)](https://www.slettmeg.no)
- [NDLA – Privacy by Design (Norwegian)](https://ndla.no)
- [Datatilsynet – Organizational Obligations (full overview, Norwegian)](https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/)
- [YouTube: Privacy and GDPR – What Does It Mean for You? (Simployer, 10 min)](https://www.youtube.com/watch?v=u6p_G7w89Uo)
