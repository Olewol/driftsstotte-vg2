---
title: "Firewalls and Network Security"
emne: sikkerhet
language: en
kompetansemaal:

  - km-10

kilder:

  - ndla
  - nsm
  - microsoft
  - <https://ndla.no/resource/224ac302-1aaa-43c7-9228-8b2f4bf402fc>
  - <https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/>
  - <https://www.cloudflare.com/learning/security/what-is-a-firewall/>
  - <https://owasp.org/www-project-top-ten/>
  - <https://learn.microsoft.com/en-us/azure/security/fundamentals/network-overview>

video: <https://www.youtube.com/watch?v=nS7fOofT-f4>
notebooklm: true
tags: []
flashcards: <https://notebooklm.google.com/notebook/3e72e53a-b0ca-4f05-a597-a8eea5ea7ea9>
public: true
original: brannmur.md
---

## Introduction

A**firewall**is the most important single tool for controlling network traffic [^1]. It acts as a checkpoint between networks: it inspects data packets and decides — based on defined rules — whether to allow or block them.

The Norwegian National Security Authority (NSM) identifies "control data flow" as a key principle [^2]. A firewall is the primary tool for this, but it works best as part of a layered defense with [[segmentering-og-vlan-en|network segmentation]], IDS/IPS, and logging [^3].

Firewalls operate at multiple levels: at the network level (routers/switches), in the cloud, and as host-based software on individual machines [^4].

---

## Theory

### Packet Filtering (Stateless)

The simplest type of firewall examines each data packet in isolation against a rule set [^5]:

-**What it inspects:**source IP, destination IP, source port, destination port, protocol (TCP/UDP/ICMP)
-**Advantage:**very fast and resource-light
-**Disadvantage:**no context — the firewall doesn't know if a packet is part of an established session

**Example packet filter rule:**

```
ALLOW  TCP  from 192.168.1.0/24  to ANY    port 443
DENY   TCP  from ANY             to ANY    port 23   (Telnet is outdated)
DENY   ALL  from ANY             to ANY    (default-deny at the end)
```

---

### Stateful Inspection

A**stateful**firewall remembers the state of active network connections [^5]. It builds a state table and automatically allows return traffic for established sessions.

- A PC initiates an HTTPS connection to a web server
- The firewall registers that this connection was initiated from inside and allows return traffic
- An external actor attempting to initiate a direct incoming connection is blocked

**Advantages over packet filtering:**

- Can distinguish legitimate return traffic from unwanted incoming traffic
- Harder to fool with spoofed IP addresses
- Standard in all modern home routers and enterprise firewalls

---

### Application Firewall (WAF / Layer 7)

A**WAF (Web Application Firewall)**operates at the application layer and understands protocols like HTTP/HTTPS [^6]. It can:

- Inspect the content of HTTP requests — not just headers
- Detect and block**SQL injection**,**XSS (Cross-Site Scripting)**, and other OWASP Top 10 attacks
- Implement rate limiting to protect against DDoS
- Mask error messages that reveal server technology

WAF is a standard component in cloud services such as Azure Application Gateway and Cloudflare [^4].

---

### DMZ — Demilitarized Zone

A**DMZ**is a network segment positioned between the external internet and the internal corporate network [^3]. Servers that must be accessible from the internet (web servers, email servers, DNS) are placed in the DMZ.

```
Internet
    |
[External Firewall]
    |
   [DMZ]
   ├── Web Server
   ├── Email Server
   └── Reverse Proxy
    |
[Internal Firewall]
    |
[Internal Network]
  ├── File Server
  ├── AD Server
  └── Employee PCs
```

**DMZ advantage:**Even if a web server in the DMZ is compromised, the internal firewall prevents the attacker from moving into the internal network [^2]. This is called**network segmentation**.

---

### Network Segmentation

**Network segmentation**divides the network into separate zones with firewall rules between them [^2]. The goal is to limit**lateral movement**— the attacker's ability to spread across the network after gaining initial access.

Implemented via:
-**VLAN (Virtual LAN):**logical separation at the network level. Employee VLAN, guest VLAN, server VLAN, and IoT VLAN are typical segments.
-**Firewall rules between VLANs:**define which traffic is allowed across

---

### Default-Deny Principle

Best practice for firewall rules [^3]:

>**Block everything, allow only what is necessary**

This is called*default-deny*or*allowlist approach*. All ports and protocols are blocked by default — only explicitly permitted traffic gets through.

The opposite is*default-allow*(blocklist): allow everything, block the known bad. This is not suitable for security-sensitive environments.

---

### IDS and IPS

| |**IDS**|**IPS**|
|---|---|---|
|**Name**| Intrusion Detection System | Intrusion Prevention System |
|**Function**| Monitors traffic and alerts on suspicious activity | Monitors and**automatically blocks**suspicious traffic |
|**Placement**| Copies traffic (out-of-band) | Inline in the traffic path |
|**Advantage**| False positive risk limited to alerts | Automatic response — faster than manual action |
|**Disadvantage**| Doesn't react — only alerts | False positive can block legitimate traffic |

Modern systems are typically combined (IDPS) [^8]. They use signatures (known attack patterns) and anomaly detection (deviations from normal behavior).

---

### Next-Generation Firewall (NGFW)

A**Next-Generation Firewall**combines traditional stateful inspection with deeper application awareness [^9]. NGFW can identify and control traffic based on application (not just port), user identity, and content. Examples: Palo Alto Networks, Fortinet FortiGate, Cisco Firepower. NGFW is now the standard in enterprise environments [^3].

---

### Windows Defender Firewall

On Windows machines, the built-in firewall is a host-based addition to the network firewall [^10]. It controls traffic in and out of the individual machine.

**GUI configuration:**

1. Search for "Windows Defender Firewall with Advanced Security" in the Start menu

2.**Inbound Rules:**control what can connect to the machine
3.**Outbound Rules:**control what the machine can connect to

1. 

**Two firewalls = better defense:**
An enterprise defense should include both a network firewall (at router level) and host-based firewalls on all machines. Even if the network firewall is bypassed, the host-based firewall stops the attack [^3].

---

## Lab Example

### Practical: Block Inbound Ping (ICMP Echo Request) on Windows

1. Open**Windows Defender Firewall with Advanced Security**
2. Click**Inbound Rules**→**New Rule**
3. Select**Custom**→**Next**
4. Program:**All programs**→**Next**
5. Protocol:**ICMPv4**→ select "Specific ICMP types" → check "Echo Request" →**Next**
6. Scope: keep defaults →**Next**
7. Action:**Block the connection**→**Next**
8. Profile: select**Public**and**Private**→**Next**
9. Name the rule: "Block ICMP Ping" →**Finish**

**Test:**Try pinging the machine from another machine on the network — you should receive no response.

---

## Study Guide

### Firewall and Network Security — Core Content

**What is a firewall?**
A firewall controls network traffic based on predefined rules [^1]. Three main levels: packet filtering (stateless), stateful inspection, and application firewall (WAF/Layer 7) [^5].

**Stateless vs. stateful:**
Stateless firewalls evaluate each packet in isolation — fast but no memory. Stateful firewalls track active connections and distinguish legitimate return traffic from intrusion attempts [^5].

**Default-deny:**
Block everything by default, explicitly allow only necessary traffic [^3]. Minimizes attack surface dramatically compared to default-allow.

**DMZ and segmentation:**
DMZ isolates internet-exposed servers in a separate segment [^3]. Internal network segmentation via VLAN limits lateral movement after a breach.

**IDS/IPS:**
IDS detects and alerts [^8]. IPS detects and automatically blocks. Both use signatures and anomaly detection.

**Layered defense:**
Firewall is one layer in Defense in Depth. Network firewall + host-based firewall + segmentation + logging provides overlapping protection [^3].

**Key terms:**Packet filtering, stateful inspection, WAF, DMZ, network segmentation, default-deny, VLAN, IDS, IPS, lateral movement, host-based firewall, NGFW.

---

## FAQ

**What's the difference between a firewall and antivirus?**
A firewall controls network traffic. Antivirus/EDR analyzes files and program execution on the machine itself. Both are necessary and complement each other [^3].

**Can a firewall stop all malware?**
No. A firewall stops unauthorized network traffic, but a user can download malware over an allowed HTTPS connection [^3].

**Why is DMZ important for web servers?**
Web servers must be accessible from the internet. Placing them in a DMZ ensures that even if compromised, the attacker cannot directly reach the internal network [^2].

**What's the difference between VLAN segmentation and DMZ?**
DMZ is for internet-exposed servers between two firewalls. VLAN segmentation divides the internal network into logical zones with firewall rules between them.

**What does "false positive" mean for IPS?**
An IPS falsely identifying legitimate traffic as a threat and blocking it. This can disrupt operations and requires careful calibration [^8].

**When should you use WAF instead of a regular firewall?**
WAF is used in addition to a regular firewall when exposing web applications to the internet [^6]. A regular firewall cannot inspect HTTPS content, but a WAF decrypts and inspects HTTP requests.

---

## Quiz

<details><summary>Question 1: What is the difference between stateless and stateful firewalls?</summary>

**Answer:**A stateless firewall (packet filtering) inspects each packet in isolation without context. A stateful firewall remembers the state of active connections and can distinguish legitimate return traffic from unwanted incoming traffic [^5].

</details>

<details><summary>Question 2: What is the purpose of a DMZ?</summary>

**Answer:**A DMZ is a network segment between the internet and the internal network where internet-exposed servers are placed. If a server in the DMZ is compromised, the internal firewall prevents the attacker from reaching the internal network [^3].

</details>

<details><summary>Question 3: What does default-deny mean, and why is it best practice?</summary>

**Answer:**Default-deny means all traffic is blocked by default, and only explicitly permitted traffic is allowed. It minimizes the attack surface — only what's necessary is opened [^3].

</details>

<details><summary>Question 4: What is the difference between IDS and IPS?</summary>

**Answer:**IDS (Intrusion Detection System) monitors traffic and alerts on suspicious activity but doesn't intervene. IPS (Intrusion Prevention System) alerts and automatically blocks suspicious traffic inline [^8].

</details>

<details><summary>Question 5: What is network segmentation, and why is it important?</summary>

**Answer:**Network segmentation divides the network into separate zones with firewall rules between them. It limits an attacker's ability for lateral movement — even if one zone is compromised, the firewall prevents spread [^2].

</details>

---

## Sources

[^1]: NDLA. (2024).*Firewall (Driftsstøtte VG2)*. <https://ndla.no/r/driftsstotte-im-itk-vg2/brannmur/2aad28ca4e>
[^2]: NSM. (2025).*Basic Principles for ICT Security 2.0*. <https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/>
[^3]: Microsoft. (2025).*Azure Network Security Overview*. <https://learn.microsoft.com/en-us/azure/security/fundamentals/network-overview>
[^4]: Cloudflare. (2025).*What is a firewall?*<https://www.cloudflare.com/learning/security/what-is-a-firewall/>
[^5]: PowerCert Animated Videos. (2022).*Stateful vs Stateless Firewall*. YouTube. <https://www.youtube.com/watch?v=nS7fOofT-f4>
[^6]: OWASP. (2025).*Web Application Firewall*. <https://owasp.org/www-community/Web_Application_Firewall>
[^7]: SANS Institute. (2024).*IDS vs IPS: What's the Difference?*<https://www.sans.org/blog/ids-vs-ips/>
[^8]: Palo Alto Networks. (2025).*What is a Next-Generation Firewall?*<https://www.paloaltonetworks.com/cyberpedia/what-is-a-next-generation-firewall>
[^9]: Microsoft. (2025).*Windows Defender Firewall with Advanced Security*. <https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-firewall/windows-firewall-with-advanced-security>
