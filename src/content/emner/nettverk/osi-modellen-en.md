---
title: "The OSI Model"
emne: nettverk
competence_goals:

  - km-05

language: en
original: osi-modellen.md
kilder:

  - ndla
  - <https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/>
  - <https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/>
  - <https://www.professormesser.com/network-plus/>
  - <https://www.cloudflare.com/learning/>
  - <https://learn.microsoft.com/en-us/training/paths/networking-fundamentals/>

tags: [osi, model, layer, protocol, network]
flashcards: <https://notebooklm.google.com/notebook/f7e5ad6c-7082-40cf-abd5-7a41b540f8e1>
public: true
video: <https://www.youtube.com/watch?v=vv4y_uOneC0>
notebooklm: true
---

# The OSI Model

## Introduction

TThe OSI model (Open Systems Interconnection) is a 7-layer reference model developed by ISO in the late 1970s.
TTIt never became the dominant implementation in practice — that was TCP/IP — but OSI has become the universal standard
TTfor*describing and understanding*network communication. In troubleshooting, asking "which layer is the problem at?" is
Tone of the most useful questions you can ask.

TThe OSI model is closely linked to the [[tcp-ip-modellen-en|TCP/IP model]], which is the framework the internet actually
TTuses in practice. Understanding OSI is key to understanding the protocols described in
TT[[nettverksprotokoller-en|network protocols]], as well as the services in [[dns-og-dhcp-en|DNS and DHCP]] and
T[[serverroller-en|server roles]].

## Theory

### The 7 Layers

|| Layer | Name | Function | Protocol Examples |
|| ------- | ------ | ---------- | ------------------ |
|| 7 | Application | User interface and application protocols | HTTP, HTTPS, FTP, SMTP, DNS |
|| 6 | Presentation | Formatting, encryption, compression | TLS/SSL, JPEG, ASCII, MPEG |
|| 5 | Session | Creating, maintaining, and ending sessions | NetBIOS, RPC, SQL |
|| 4 | Transport | End-to-end communication, segmentation | TCP, UDP |
|| 3 | Network | Logical addressing and routing | IP, ICMP, OSPF, BGP |
|| 2 | Data Link | Frames, MAC addresses, error detection | Ethernet, ARP, 802.11 |
|| 1 | Physical | Bit transmission over medium | UTP cable, fiber, WiFi radio |

### Detailed Description of Each Layer

*## Layer 1 — Physical Layer
TThe physical layer defines the electrical, optical, and wireless signals that represent bits (0 and 1).
TTIt includes connector types (RJ-45), cable types (Cat5e, Cat6, fiber), and transmission methods.
TNothing here knows about addresses or logical structure — it's just bits.

*## Layer 2 — Data Link Layer
Wraps bits into*frames*and handles transmission within one network segment. Divided into two sublayers:
-**MAC (Media Access Control)**: addressing with 48-bit MAC addresses, media access control
-**LLC (Logical Link Control)**: error detection, flow control

A switch operates at layer 2. Ethernet is the dominant layer 2 protocol in wired networks.

*## Layer 3 — Network Layer
IIntroduces logical addressing (IP addresses) and routing between networks. A router operates at layer 3.
IThe network layer determines the best path from source to destination through potentially many intermediate networks.

*## Layer 4 — Transport Layer
SSegments data from the application layer and handles end-to-end communication. TCP provides reliable delivery with
SSsequence numbers and acknowledgments (ACK). UDP is fast and simple without such guarantees.
SPort numbers identify which application the traffic belongs to.

*## Layer 5 — Session Layer
MManages*sessions*— persistent connections between applications. The session layer establishes, maintains, and terminates
MMthe dialogue between two systems. In practice, much of this functionality is integrated into application protocols in
MTCP/IP.

*## Layer 6 — Presentation Layer
Translates data between the application's format and the network's format. Responsible for:
-**Encryption/decryption**: TLS/SSL encrypts HTTP traffic to HTTPS
-**Compression**: reduces the amount of data being sent
-**Format conversion**: ensures character sets (UTF-8, ASCII) are interpreted the same on both sides

*## Layer 7 — Application Layer
TThe top layer is what the user interacts with. This is where protocols that applications use directly reside: HTTP for
Tweb browsing, SMTP for sending email, FTP for file transfer, DNS for name resolution.

### Encapsulation and PDU

WWhen data is sent down through the OSI layers, each layer adds its own control information (header).
WWThis process is called**encapsulation**. Each layer works with its own**PDU (Protocol Data Unit)**: at layer 4 it's
WWcalled a*Segment*, at layer 3 a*Packet*, and at layer 2 a*Frame*. At the receiving end, it's unpacked in reverse order
W— each layer reads and removes its header.

### Mnemonic

A popular mnemonic for the layers from bottom to top (layer 1 → 7):

>**P**lease**D**o**N**ot**T**hrow**S**ausage**P**izza**A**way
> (Physical, Data Link, Network, Transport, Session, Presentation, Application)

And top to bottom (layer 7 → 1):

>**A**ll**P**eople**S**eem**T**o**N**eed**D**ata**P**rocessing

### OSI vs. TCP/IP

|| OSI | Layer # | TCP/IP (5-layer) |
|| ----- | --------- | ----------------- |
|| Application | 7 | Application |
|| Presentation | 6 | Application |
|| Session | 5 | Application |
|| Transport | 4 | Transport |
|| Network | 3 | Network |
|| Data Link | 2 | Data Link |
|| Physical | 1 | Physical |

OOSI layers 5, 6, and 7 together correspond to the application layer in TCP/IP. In practice, the functions of the
Opresentation and session layers are implemented directly in application protocols or in TLS.

### OSI in Troubleshooting

The OSI model is especially useful for troubleshooting. Consider a scenario where a user can't reach the internet:

-**Layer 1**— Is the cable plugged in? Are link lights on?
-**Layer 2**— Does the switch see the MAC address? Wrong VLAN?
-**Layer 3**— Does the machine have the correct IP address and gateway? Can you ping the gateway?
-**Layer 4**— Is TCP port 443 blocked by a firewall?
-**Layer 7**— Browser configuration error? DNS works but HTTP fails?

By working systematically from the bottom up (or top down), you isolate the problem quickly.

## Example / Lab

### Identify the Layer

Determine which OSI layer each scenario belongs to:

|| Scenario | Layer |
|| ---------- | ------- |
|| Ethernet cable not plugged in | Layer 1 — Physical |
|| Wrong IP address configured | Layer 3 — Network |
|| HTTPS encryption (TLS) | Layer 6 — Presentation |
|| Switch forwards based on MAC | Layer 2 — Data Link |
|| TCP three-way handshake | Layer 4 — Transport |
|| DNS lookup fails | Layer 7 — Application |
|| WiFi signal too weak | Layer 1 — Physical |

### Troubleshooting Exercise

Scenario: A PC can ping `192.168.1.1`(gateway) but cannot open`<https://ndla.no`.>

Analysis:

- Layers 1–3 are working (ping to gateway works → physical connection, data link, and IP are OK)
- The problem is at layer 4 (TCP port blocked?), layer 6 (TLS error?) or layer 7 (DNS failing? HTTP error?)
- Test: `nslookup ndla.no` — if DNS doesn't respond, the problem is layer 7 (DNS service) or layer 3 (routing to DNS server)

## Study Guide

*## Purpose of the OSI Model
OOSI is a*reference model*, not an implementation. It is used as a common reference language for understanding and
OOtroubleshooting network communication. Each layer has a clear area of responsibility and only communicates with the
Olayer directly above and below.

*## Core Understanding Per Layer

- Layers 1–2 deal with physical and local transmission (cable, WiFi, switches, MAC addresses)
- Layer 3 introduces logical addressing and routing (IP, routers)
- Layer 4 handles end-to-end reliability and application identification (TCP/UDP, port numbers)
- Layers 5–7 are application-related (sessions, formatting, user protocols)

*## Common Exam Points

- The difference between a switch (layer 2) and a router (layer 3)
- TCP vs. UDP and when to use each
- The OSI layers from top to bottom vs. bottom to top
- Encapsulation: what happens to data as it travels down the stack

## FAQ

*## Why do we use the OSI model when TCP/IP is what's actually used?
OOSI gives us a precise, shared reference language for talking about network problems and protocols.
OOWhen a technician says "the problem is at layer 2," everyone understands what that means — even if the network is
Orunning TCP/IP.

*## What is the difference between layer 3 and layer 2 addresses?
LLayer 2 uses MAC addresses (physical, hard-coded) for communication within one network.
LLayer 3 uses IP addresses (logical, configurable) for communication between different networks.

*## What happens at layer 6 (Presentation) in practice?
EEncryption via TLS/SSL is the most common example. When you visit an HTTPS site, layer 6 encrypts the data.
ECompression (gzip) and character conversion (UTF-8) are other examples.

*## Can a single piece of hardware operate at multiple layers?
YYes. A "layer 3 switch" operates at both layer 2 and layer 3 — it can route between VLANs in addition to functioning as
Ya regular switch. Firewalls often operate at layers 3–7.

*## What is a PDU, and why is the term useful?
PPDU (Protocol Data Unit) is the name for the data unit at a given layer: Segment (layer 4), Packet (layer 3), Frame
P(layer 2), Bit (layer 1). It makes it easier to describe exactly what is being processed at each step.

*## What is encapsulation?
EEncapsulation is the process where data is wrapped in control information (headers) from each layer of the OSI model as
Eit travels down the stack. At the receiving end, it's unwrapped layer by layer.

*## Why is the session layer (layer 5) important?
TThe session layer manages the dialogue between applications — who speaks, in what order, and how to end cleanly.
TIn practice, this is often integrated into TLS and application protocols.

*## How do I actively use OSI in troubleshooting?
SStart at layer 1 and work up: check cable → switch → IP address → firewall ports → application settings.
SOr start at layer 7 and work down if you know the network is working.

## Quiz

<details>
<summary>Question 1: Which layers in OSI correspond to the application layer in TCP/IP?</summary>

***Answer:**Layers 5 (session), 6 (presentation), and 7 (application) in OSI together correspond to the application layer
*in the TCP/IP model.
</details>

<details>
<summary>Question 2: What is the task of the presentation layer (layer 6)?</summary>

***Answer:**The presentation layer handles formatting, encryption/decryption, and compression of data.
*TLS/SSL, which encrypts HTTP traffic to HTTPS, is an example of functionality from this layer.
</details>

<details>
<summary>Question 3: What is the difference between a switch and a router from the OSI model perspective?</summary>

***Answer:**A switch primarily operates at layer 2 (data link layer) and uses MAC addresses to forward frames within one
**network. A router operates at layer 3 (network layer) and uses IP addresses to route packets between different
*networks.
</details>

<details>
<summary>Question 4: What is the session layer (layer 5) responsible for?</summary>

***Answer:**The session layer manages the creation, maintenance, and termination of sessions (persistent connections)
*between applications on two systems.
</details>

<details>
<summary>Question 5: Describe the mnemonic for the OSI layers from bottom to top.</summary>

***Answer:**"Please Do Not Throw Sausage Pizza Away" — Physical, Data Link, Network, Transport, Session, Presentation,
*Application (layers 1 to 7).
</details>

## Resources

- [TCP/IP 5-layer model (mentions OSI) — NDLA](<https://ndla.no/nb/r/driftsstotte-im-itk-vg2/5-lags-tcpip-modell/9e31c212f6>)
- [OSI Model — Imperva](<https://www.imperva.com/learn/application-security/osi-model/>)
- [OSI Model — Cloudflare](<https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/>)
- [TCP/IP and OSI Comparison — Cisco Press](<https://www.ciscopress.com/articles/article.asp?p=1757634&seqNum=2>)
- [The OSI Model Explained | Animation — NetworkChuck (15 min)](<https://www.youtube.com/watch?v=vv4y_uOneC0>)
- [OSI Model — SNL (Norwegian)](<https://snl.no/OSI-modellen>)
