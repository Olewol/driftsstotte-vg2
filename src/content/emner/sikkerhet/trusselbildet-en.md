---
title: "The Threat Landscape"
emne: sikkerhet
kompetansemaal:

  - km-07

kilder:

  - ndla
  - nsm
  - owasp
  - <https://nsm.no/regelverk-og-hjelp/risiko-2024>
  - <https://owasp.org/www-project-top-ten/>
  - <https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/>
  - <https://www.datatilsynet.no/>
  - <https://www.digdir.no/informasjonssikkerhet/>

notebooklm: true
video: <https://www.youtube.com/watch?v=nG9v3RSSXTo>
tags: []
flashcards: <https://notebooklm.google.com/notebook/3e72e53a-b0ca-4f05-a597-a8eea5ea7ea9>
public: true
language: en
original: trusselbildet.md
---

## Introduction

TThe threat landscape in digital security changes rapidly. What were exotic attack methods ten years ago are now everyday
TToccurrences for Norwegian organizations and individuals. NSM (Norwegian National Security Authority) publishes an
TTannual threat report showing that Norwegian businesses, hospitals, municipalities, and critical infrastructure are
Tconstantly under pressure from digital attacks.

TTo work with IT security, you need to know the most common threats: what they are, how they work, and what impact they
Thave on society.

TTo move from knowledge about threats to concrete measures, it is necessary to conduct a structured
TT[[risikoanalyse-en|risk analysis]]. The threat landscape provides the raw material – risk analysis helps you
TTprioritize. [[it-losninger-med-sikkerhet-en|IT solutions with built-in security]] shows which technical and
Torganizational countermeasures exist.

---

## Theory

### Malware – Malicious Software

Malware is a collective term for software designed to damage, disrupt, or gain unauthorized access to systems.

*## Virus
AA virus copies itself by inserting itself into other files. It spreads when infected files are opened or shared.
AViruses require user action to spread.

*## Worm
AA worm spreads automatically over networks without requiring user action. It exploits vulnerabilities in network
AAprotocols. WannaCry (2017) was a worm that infected over 200,000 systems in 150 countries in a short time – including
Athe British NHS hospitals.

*## Trojan
AA trojan pretends to be useful software but contains hidden malicious code. Example: a free game that actually installs
Aspyware. Trojans often give the attacker backdoor access.

*## Ransomware
RRansomware encrypts the victim's files and demands payment for the decryption key.
RRThis is the dominant threat against Norwegian organizations according to NSM. In 2021, the Conti ransomware hit Østre
RRToten municipality and shut down all digital operations for weeks. The healthcare sector, municipalities, and
Rindustrial companies are frequent targets.

*## Spyware
SSpyware monitors user activity without consent – keystroke logging, screen capture, collection of passwords and banking
Sinformation. It can be part of commercial "stalkerware" products used for partner surveillance.

*## Rootkit
AA rootkit hides its own presence and the presence of other malware deep within the operating system.
AVery difficult to detect and remove. Often requires OS reinstallation.

---

### Phishing and Social Engineering

***Phishing**is an attempt to trick users into revealing sensitive information (passwords, credit card details) by posing
*as a legitimate entity – a bank, employer, the tax authorities, or postal service.

--**Spear phishing:**Targeted phishing against one specific person or organization, based on collected information about
-the victim. Far more effective than mass emails.
-**Vishing:**Voice phishing – fraud via phone. The attacker pretends to be IT support, a bank, or the police.
-**Smishing:**SMS phishing. Typical example: "Your package is on hold, click here to pay customs fees."
-**Pretexting:**The attacker constructs a believable false background story to manipulate the victim.

TThe human factor is the most common attack vector. Most successful cyber attacks start with social engineering, not
Ttechnical hacking.

---

### DDoS – Denial of Service Attacks

***DDoS (Distributed Denial of Service)**floods a service with so many requests that it cannot serve legitimate users.
*The attack is coordinated from thousands of compromised machines (a botnet).

NNSM and NCSC regularly warn about DDoS attacks against Norwegian critical infrastructure, particularly in the wake of
NNgeopolitical events. In 2022, following Norway's support for Ukraine, several Norwegian public websites were hit by
NDDoS attacks from pro-Russian hacker groups.

Consequences: online banking unavailable, public portals down, communication services disrupted.

---

### Zero-Day Vulnerabilities

AA**zero-day**is an unknown weakness in software that the vendor has not yet discovered or patched.
AThe attacker exploits the vulnerability*before*a patch exists – hence "zero days" of defense.

ZZero-day exploits are highly valuable and traded on criminal markets. State-sponsored actors have the resources to
Zpurchase or develop such tools themselves.

---

### Insider Threats

Not all threats come from outside.**Insider threats**can be:

--**Unintentional:**An employee clicks a phishing link, uses a weak password, or sends confidential documents to the
-wrong email address.
-**Intentional:**A disgruntled employee sabotages systems, steals data for competitors, or sells access to criminals.

MMeasures: principle of least privilege, logging of user activity, access management, and background checks for employees
Min sensitive roles.

---

### APT – Advanced Persistent Threats

***APT**are long-term, sophisticated attacks carried out by resourceful actors – typically state-sponsored hacker groups.
*Characteristics:

- Planned over months
- Uses tailored tools and zero-days
- The goal is espionage, sabotage, or destabilization, not quick profit
- The attacker can remain hidden in a network for years

NNSM points to state actors linked to Russia, China, and North Korea as active threats against Norwegian interests.
NAPT29 (Cozy Bear) and APT28 (Fancy Bear) are well-known Russian groups that have attacked Norwegian targets.

CContinuous monitoring and log analysis are crucial for detecting APT activity. An attacker who has had access for years
Cwithout being discovered can exfiltrate enormous amounts of data.

---

### OWASP Top 10 – Web Application Vulnerabilities

OOWASP (Open Web Application Security Project) publishes a list of the ten most common security flaws in web
Oapplications. The 2021 version is current:

|| No | Category |
|| --- | --- |
|| A01 | Broken Access Control |
|| A02 | Cryptographic Failures |
|| A03 | Injection – SQL injection and similar |
|| A04 | Insecure Design |
|| A05 | Security Misconfiguration |
|| A06 | Vulnerable and Outdated Components |
|| A07 | Identification and Authentication Failures |
|| A08 | Software and Data Integrity Failures |
|| A09 | Security Logging and Monitoring Failures |
|| A10 | Server-Side Request Forgery (SSRF) |

---

### Societal Impact and Democracy

Digital threats do not stop at organizations. They affect democracy and public discourse:

***Disinformation campaigns:**State-sponsored actors spread fake news via social media to sow doubt, polarize
**populations, and undermine trust in institutions. Election interference in the US (2016), France (2017), and alleged
*influence on Norwegian public opinion are documented examples.

***Attacks on critical infrastructure:**Power, water, healthcare, and communications depend on IT systems.
*A successful attack on the power grid or hospital systems can cost lives.

***Psychological warfare:**Threatening or debilitating cyber attacks can be used as leverage in diplomatic conflicts
*without a single soldier crossing a border.

NNSM emphasizes that digital security is national security. This is why ICT competence is a societal need, not just a
Nvocational field.

---

## Example / Lab

*## Scenario: Recognize phishing emails

You receive the following emails. Assess which ones are phishing and why:

11.*"Dear customer, your account has been temporarily blocked. Click here to verify your identity:
1www.dnb-sikkerhet.net"*
   → Suspicious: the domain is not dnb.no. Urgency appeal. Link to unknown website.

2.*"Hi Kari, here are the minutes from yesterday's meeting. See attached PDF."*– sender is <colleague@company.no>
   → Could be legitimate, but: check if the attachment is expected, and whether the sender address matches exactly.

3.*"You have won an iPhone 15. Enter your credit card info to pay shipping."*
   → Classic scam. No legitimate prize requires paying shipping with a credit card in advance.

*## Phishing defense measures:

- Use MFA (multi-factor authentication) – even if the password is stolen, login is blocked
- Email filtering with SPF, DKIM, and DMARC
- Security awareness training for employees

---

## Study Guide

### The Threat Landscape – Core Content

*## Malware types and characteristics:
VVirus (requires user action), worm (self-spreads over networks), trojan (hidden malicious code in seemingly useful
VVsoftware), ransomware (encrypts files and demands payment), spyware (silently monitors), rootkit (hides deep in the
VOS).

*## Phishing and social engineering:
PPhishing is the most common attack vector – most successful attacks start here. Variants include spear phishing
PP(targeted), vishing (phone), smishing (SMS), and pretexting (false background story).
PDefense: MFA, email filtering, training.

*## DDoS:
FFlooding with traffic from a botnet. Affects availability, not confidentiality. Typically used as geopolitical leverage
For against online banking. Countermeasures: CDN, rate limiting, scrubbing centers.

*## Zero-day:
UUnknown vulnerability with no available patch. Highly valuable to attackers. The only defense is Defense in Depth –
Ulimit the damage even if one layer fails.

**APT:**
LLong-term state-sponsored attacks. Characteristics: tailored tools, stays hidden for years, goal is espionage/sabotage.
LDetected through good logging and SIEM.

*## OWASP Top 10:
TThe most common web application vulnerabilities: broken access control (A01), cryptographic failures (A02), injection
T(A03), and insufficient logging (A09) are the most important to know.

*## Societal perspective:
DDigital security = national security. Disinformation, attacks on critical infrastructure, and psychological warfare are
Dreal threats to democracy and societal functions.

---

## FAQ

*## What is the difference between ransomware and a regular virus?
AA virus copies itself and can damage files or systems, but its primary purpose is spreading.
AARansomware is optimized for making money: it encrypts the victim's data and demands payment for the decryption key.
ARansomware is currently the most profitable form of cybercrime.

*## Why is phishing so effective?
PPhishing exploits human psychology – trust in familiar senders, urgency appeals ("your account will be closed in 24
PPhours"), curiosity, and fear. Technical security is strong enough that it is easier to trick a human than to hack a
Psystem. Spear phishing is especially effective because it is tailored with real information about the victim.

*## Can you protect against zero-day attacks?
NNot directly – there is no patch for unknown vulnerabilities. Defense relies on Defense in Depth: segmentation limits
NNthe spread, logging detects abnormal activity, and rapid response limits the damage.
NRegular patching reduces the number of known vulnerabilities and makes zero-days harder to combine.

*## What is a botnet?
AA botnet is a network of compromised machines ("bots" or "zombies") controlled by an attacker without the owners'
AAknowledge. Botnets are used for DDoS attacks, spam distribution, and cryptocurrency mining.
AMachines can become part of a botnet via malware downloaded from insecure websites or email attachments.

*## What is the difference between APT and "regular" hacking?
RRegular hacking is often opportunistic – the attacker looks for easily accessible targets.
RRAPT is targeted, planned over time, and carried out by resourceful actors (typically state-sponsored).
RThe APT actor is patient, hides themselves, and has a long-term strategic goal – not just quick profit.

*## What does Broken Access Control (OWASP A01) mean?
IIt means the application does not enforce access control correctly – users can do things they should not have access to.
IIExample: a regular user can edit the URL and gain access to another user's data. It is consistently ranked as the most
Icommon web application vulnerability.

*## How can disinformation threaten democracy?
SState-sponsored actors can use social media to systematically spread fake news, amplify polarization, and undermine
SStrust in media, politicians, and institutions. When citizens cannot distinguish between fact and lies, the foundation
SSfor informed decisions is weakened. The Cambridge Analytica scandal showed that personal data combined with targeted
Sdisinformation can influence election results.

---

## Quiz

<details><summary>Question 1: What distinguishes a worm from a virus?</summary>

***Answer:**A worm spreads automatically over networks without user action, while a virus requires an infected file to be
*opened or shared to spread.

</details>

<details><summary>Question 2: What is spear phishing?</summary>

***Answer:**Spear phishing is targeted phishing against a specific person or organization, based on collected information
*about the victim. It is far more effective than general mass emails.

</details>

<details><summary>Question 3: What is meant by a zero-day vulnerability?</summary>

***Answer:**A zero-day is an unknown weakness in software that the vendor has not yet discovered or created a patch for.
*The attacker can exploit the vulnerability without the defender having the ability to patch.

</details>

<details><summary>Question 4: What is APT, and who typically stands behind it?</summary>

***Answer:**APT (Advanced Persistent Threat) refers to long-term, sophisticated attacks carried out by resourceful actors
**– typically state-sponsored hacker groups. They use advanced tools and can remain hidden in a network for months or
*years.

</details>

<details><summary>Question 5: How can disinformation campaigns threaten democracy?</summary>

***Answer:**State-sponsored actors can spread fake news via social media to polarize populations, undermine trust in
**democratic institutions, and influence elections. This is a form of digital warfare that does not require traditional
*military means.

</details>

---

## Resources

- [NSM – Digital Security (Norwegian)](<https://nsm.no/fagomrader/digital-sikkerhet/>)
- [NCSC – Norwegian Notification Center for Digital Infrastructure](<https://nsm.no/ncsc>)
- [OWASP Top 10:2021](<https://owasp.org/Top10/>)
- [NDLA – Information Security (Norwegian)](<https://ndla.no>)
- [NSM – Risk Assessment 2024 (annual report, Norwegian)](<https://nsm.no/regelverk-og-hjelp/risiko-2024>)
- [OWASP – Top 10 Project Page (full documentation)](<https://owasp.org/www-project-top-ten/>)
