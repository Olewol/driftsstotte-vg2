---
title: "The TCP/IP Model"
emne: nettverk
competence_goals:

  - km-05

language: en
original: tcp-ip-modellen.md
kilder:

  - ndla
  - <https://ndla.no/nb/subject:1:430c00b5-773a-4933-9f2d-8647038e2f05/topic:2:183060/topic:2:183350/resource:1:115995>
  - <https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/>
  - <https://www.professormesser.com/network-plus/>
  - <https://www.cloudflare.com/learning/>
  - <https://learn.microsoft.com/en-us/training/paths/networking-fundamentals/>

tags: [tcp, ip, protocol, model, layers]
flashcards: <https://notebooklm.google.com/notebook/f7e5ad6c-7082-40cf-abd5-7a41b540f8e1>
public: true
video: <https://www.youtube.com/watch?v=6cG9qrKB9x0>
notebooklm: true
---

# The TCP/IP Model

## Introduction

The TCP/IP model is the practical framework that the internet and most modern networks are built upon. It describes how data is wrapped, sent through a network, and unpacked again at the receiving end. Understanding the model is key to understanding why network protocols are organized the way they are, and what happens "under the hood" when you open a website.

The TCP/IP model is closely related to the [[osi-modellen-en|OSI model]], which is the reference model for theory and troubleshooting. The specific protocols operating in the model are described in [[nettverksprotokoller-en|network protocols]], and services like [[dns-og-dhcp-en|DNS and DHCP]] and [[serverroller-en|server roles]] reside at the application layer.

## Theory

### The Layers of the TCP/IP Model

NDLA and many Norwegian textbooks use a**5-layer model**for TCP/IP. The classic internet model has 4 layers (where the bottom two are combined). Both variants are valid; the 5-layer model is more pedagogical and closer to OSI.

| Layer | Name | Function | Protocol Examples |
|-------|------|----------|------------------|
| 5 | Application | User-facing services and protocols | HTTP, HTTPS, DNS, SMTP, FTP, SSH |
| 4 | Transport | End-to-end communication, port numbers | TCP, UDP |
| 3 | Network (Internet) | Logical addressing and routing between networks | IP (v4/v6), ICMP |
| 2 | Data Link | Transmission within one network, MAC addresses | Ethernet, ARP, 802.11 (WiFi) |
| 1 | Physical | Actual bit transmission over medium | Fiber, copper (UTP), WiFi radio |

### What Each Layer Does

**Layer 1 — Physical Layer**
Responsible for the actual bit transmission: voltage levels on copper wire, light pulses in fiber, radio signals in WiFi. Protocols at this layer define connectors, cables, and signal standards (e.g. 10BASE-T, 1000BASE-T).

**Layer 2 — Data Link Layer**
Wraps bits into*frames*. Ethernet is dominant here. Each network card has a unique**MAC address**(48 bits, written as e.g. `00:1A:2B:3C:4D:5E`). A switch operates at layer 2 and forwards frames based on MAC addresses. ARP (Address Resolution Protocol) is used to find the MAC address for a known IP address.

A**MAC address**is a unique physical address at the data link layer (layer 2) that is burned into the network interface card for identification in a local network.

**Layer 3 — Network Layer**
Handles logical addressing with**IP addresses**and routing between different networks. A router operates at layer 3. IPv4 addresses are 32 bits (e.g. `192.168.1.10`), IPv6 addresses are 128 bits. ICMP is used for error messages and diagnostics (`ping`).

An**IP address**is a logical address at the network layer (layer 3) that uniquely identifies a device in a network and enables routing between networks.

**Layer 4 — Transport Layer**
Responsible for end-to-end communication between applications on two machines. Uses**port numbers**to identify which application the traffic belongs to.

A**port**is a numerical identifier at the transport layer used to direct traffic to the correct application or service on a machine.

-**TCP (Transmission Control Protocol)**: connection-oriented, guarantees delivery order and error correction. Used where reliability is important (websites, email, file transfer).
-**UDP (User Datagram Protocol)**: connectionless, fast but without guarantees. Used where speed is more important than accuracy (video streaming, VoIP, DNS lookups).

**Layer 5 — Application Layer**
This is where protocols that programs use directly reside: HTTP for web, SMTP for email, DNS for name resolution, etc. This layer "talks" to user applications (browser, email client, terminal program).

### Encapsulation

When data is sent down through the layers, each layer adds its own**header**with control information. This is called encapsulation:

```
Application:  [DATA]
Transport:    [TCP-header][DATA]
Network:      [IP-header][TCP-header][DATA]
Data Link:    [Ethernet-header][IP-header][TCP-header][DATA][Ethernet-trailer]
Physical:     bits over medium
```

At the receiving end, it is unpacked in reverse order — each layer reads and removes its own header. Relationship between hardware and layers: switches operate at layer 2, routers at layer 3. Layer 2 uses MAC addresses for local transmission; layer 3 uses IP addresses for routing between networks.

### Comparison: TCP/IP vs. OSI

| TCP/IP (5 layers) | OSI (7 layers) |
|-------------------|---------------|
| Application | Application (7) |
| Application | Presentation (6) |
| Application | Session (5) |
| Transport | Transport (4) |
| Network | Network (3) |
| Data Link | Data Link (2) |
| Physical | Physical (1) |

TCP/IP is the model the internet actually uses. OSI is the reference model used for theory and troubleshooting. See [[osi-modellen-en|the OSI model]] for a full description. Norwegian textbooks alternate between 4-layer and 5-layer TCP/IP — both are correct, but the 5-layer model is more pedagogical because it separates the physical layer from the data link layer.

## Example / Lab

### Packet Flow: What Happens When You Open ndla.no?

1. You type `<https://ndla.no`> in the browser.

2.**Application Layer**: The browser creates an HTTP GET request. First, it must resolve the domain name — it sends a DNS lookup (UDP, port 53) and receives the IP address of ndla.no back (e.g. `185.45.32.10`).
3.**Transport Layer**: TCP establishes a connection to port 443 (HTTPS) on the server via a*three-way handshake*(SYN → SYN-ACK → ACK). The HTTP request is wrapped in TCP segments.
4.**Network Layer**: Each TCP segment is wrapped in an IP packet with your IP address as source and `185.45.32.10` as destination.
5.**Data Link Layer**: The IP packet is wrapped in an Ethernet frame with your MAC address and the router's MAC address.
6.**Physical Layer**: Bits are sent out over the cable or WiFi to the router.

1. 
2. 
3. 

## Study Guide

**Core Understanding Per Layer**

- Layer 1: bits and signals (cable, WiFi, fiber)
- Layer 2: frames and MAC addresses (switches, Ethernet)
- Layer 3: IP addresses and routing (routers, IPv4/IPv6)
- Layer 4: TCP/UDP and ports (end-to-end reliability)
- Layer 5: application protocols (HTTP, DNS, SMTP, SSH)

**Encapsulation**
Understand that each layer adds its own header. Data from the application layer is payload for the transport layer, which is payload for the network layer, and so on. On the receiving end, it is unpacked in reverse order.

**4-layer vs. 5-layer Model**
The 4-layer model merges layers 1 and 2 into a "Network Access Layer." The 5-layer model separates them and is pedagogically closer to OSI. Both are correct.

**Common Exam Points**

- Which layer is responsible for what (IP = layer 3, MAC = layer 2, TCP = layer 4, HTTP = layer 5)
- Encapsulation: what is added at each layer
- The difference between TCP and UDP
- What ARP does (IP → MAC at layer 2)

## FAQ

**What is the difference between TCP and UDP?**
TCP is connection-oriented and guarantees that data is delivered in the correct order without loss. UDP is connectionless and fast, but gives no delivery guarantees. TCP is used where reliability is important (web, email), UDP where speed is more important (streaming, DNS).

**Which layer is responsible for IP addressing and routing?**
Layer 3 — the Network layer (also called the Internet layer in the classic 4-layer model).

**What is meant by encapsulation in TCP/IP?**
Encapsulation means that each layer adds its own header with control information as data is sent down through the layers. On the receiving end, it is unpacked in reverse order.

**What are MAC addresses used for, and at which layer do we find them?**
MAC addresses uniquely identify network cards and are used for addressing within a local network. They are found at layer 2 (data link layer). A switch uses MAC addresses to forward frames to the correct port.

**Why is the TCP/IP model organized in layers?**
Layering allows each layer to be developed and updated independently of the others. For example, you can switch from IPv4 to IPv6 at layer 3 without changing TCP at layer 4 or HTTP at layer 5. It also simplifies troubleshooting — you can isolate a problem to a single layer.

**What is ARP and why do we need it?**
ARP (Address Resolution Protocol) translates a known IP address to the corresponding MAC address on the local network. Layer 3 knows the IP address of the destination, but layer 2 needs the MAC address to send an Ethernet frame to the correct port on the switch.

**What is the difference between the 4-layer and 5-layer TCP/IP model?**
The classic internet model has 4 layers where the lowest layer ("Network Access") combines physical and data link. Norwegian textbooks (and NDLA) use a 5-layer model where these are separate — more like OSI and pedagogically clearer.

**What is ICMP and ping?**
ICMP (Internet Control Message Protocol) is a protocol at layer 3 used for error messages and diagnostics. The `ping` command sends ICMP Echo Request and waits for ICMP Echo Reply — a simple tool to test if a device is reachable.

## Quiz

<details>
<summary>Question 1: What is the difference between TCP and UDP?</summary>

**Answer:**TCP is connection-oriented and guarantees that data is delivered in the correct order without loss. UDP is connectionless and fast, but gives no delivery guarantees. TCP is used where reliability is important (web, email), UDP where speed is more important (streaming, DNS).
</details>

<details>
<summary>Question 2: Which layer is responsible for IP addressing and routing?</summary>

**Answer:**Layer 3 — the Network layer (also called the Internet layer in the classic 4-layer model).
</details>

<details>
<summary>Question 3: What is meant by encapsulation in TCP/IP?</summary>

**Answer:**Encapsulation means that each layer adds its own header with control information as data is sent down through the layers. On the receiving end, it is unpacked in reverse order.
</details>

<details>
<summary>Question 4: What are MAC addresses used for, and at which layer do we find them?</summary>

**Answer:**MAC addresses uniquely identify network cards and are used for addressing within a local network. They are found at layer 2 (data link layer). A switch uses MAC addresses to forward frames to the correct port.
</details>

<details>
<summary>Question 5: Why is the TCP/IP model organized in layers?</summary>

**Answer:**Layering allows each layer to be developed and updated independently of the others. For example, you can switch from IPv4 to IPv6 at layer 3 without changing TCP at layer 4 or HTTP at layer 5. It also simplifies troubleshooting — you can isolate a problem to a single layer.
</details>

## Resources

- [TCP/IP 5-layer Model — NDLA](<https://ndla.no/nb/r/driftsstotte-im-itk-vg2/5-lags-tcpip-modell/9e31c212f6>)
- [TCP, UDP and Ports — NDLA](<https://ndla.no/nb/r/driftsstotte-im-itk-vg2/tcp-udp-og-porter/d7acb2196e>)
- [Transport Layer TCP and UDP — windowsnett.no](<http://windowsnett.no/leksjoner/L08/8b%20Transportlaget%20TCP%20og%20UDP%20skjerm.pdf>)
