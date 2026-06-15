---
title: "DNS and DHCP"
emne: nettverk
competence_goals:
  - km-05
language: en
original: dns-og-dhcp.md
kilder:
  - ndla
  - https://learn.microsoft.com/nb-no/windows-server/networking/technologies/dhcp/dhcp-top
  - https://ndla.no/resource/130129
  - https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/
  - https://www.professormesser.com/network-plus/
  - https://www.cloudflare.com/learning/
  - https://learn.microsoft.com/en-us/training/paths/networking-fundamentals/
tags: [dns, dhcp, network services, ip, name resolution]
flashcards: https://notebooklm.google.com/notebook/f7e5ad6c-7082-40cf-abd5-7a41b540f8e1
public: true
video: https://www.youtube.com/watch?v=S374jTRz4hU
notebooklm: true
---

# DNS and DHCP

## Introduction

When you connect a PC to a network, two things happen automatically in the background: the machine gets an IP address (DHCP), and it learns who to ask when it needs to find out what `ndla.no` means in numbers (DNS). These two services are invisible to most users — but without them, nothing would work. As an IT support technician, they are among the most important services you will configure and troubleshoot. DNS and DHCP are not isolated services — they work closely with [[serverroller-en|server roles]] in a domain network, and errors in either are among the most common causes of network problems in business environments. To understand which protocols and ports these services use, see [[nettverksprotokoller-en|network protocols]].

## Theory

### DHCP — Dynamic Host Configuration Protocol

DHCP automates the assignment of IP configuration to clients. Without DHCP, an administrator would have to manually configure IP address, subnet mask, gateway, and DNS on every single machine.

#### What DHCP Distributes

A DHCP server assigns clients:
- **IP address** (e.g. `192.168.1.50`)
- **Subnet mask** (e.g. `255.255.255.0`)
- **Default gateway** (e.g. `192.168.1.1`)
- **DNS server address** (e.g. `192.168.1.10`)
- **Lease time** (how long the client can keep the address)

#### The DORA Process

DHCP uses a four-step process called DORA:

| Step | Message | Description |
|------|---------|-------------|
| 1 | **D**iscover | Client sends broadcast: "Is there a DHCP server here?" |
| 2 | **O**ffer | DHCP server replies with an IP address offer |
| 3 | **R**equest | Client accepts the offer: "I want this address" |
| 4 | **A**cknowledge | Server confirms: "The address is yours for X hours/days" |

Steps 1 and 3 are sent as broadcasts (to `255.255.255.255`) because the client does not yet have an IP address.

#### Scope and Leasing

A **scope** is the address range the DHCP server manages — e.g. `192.168.1.100`–`192.168.1.200`. Addresses outside this range can be assigned statically to servers and network equipment.

A **lease time** is the time agreement between the DHCP server and client that the client may use the address for a specific period. When the lease period nears its end, the client tries to renew it. The default lease period in Windows Server is 8 days.

#### Static vs. Dynamic Assignment

| Type | Description | Used for |
|------|-------------|----------|
| Dynamic | DHCP assigns available address from scope | Client machines |
| Static reservation | DHCP always assigns the same address to a specific MAC | Printers, servers in DHCP environment |
| Manual/static | IP is configured directly on the device | Servers, routers, switches |

#### DHCP in Business Networks

In a simple home network, DHCP runs on the router. In a business network with Windows Server, DHCP should be moved to the domain controller. The DHCP on the router must then be **disabled** to avoid conflicts (two DHCP servers on the same network creates chaos).

Check current IP configuration from the client:
```cmd
ipconfig /all
```

---

### DNS — Domain Name System

DNS is the internet's "phone book." It translates human-friendly domain names like `ndla.no` into machine-friendly IP addresses like `185.45.32.10`. Without DNS, you'd have to remember the IP address of every website you visit.

#### Hierarchical Structure

DNS is organized in a tree hierarchy:

```
                    . (root)
                   / \
                .no   .com
               /         \
           ndla.no     google.com
           /
    www.ndla.no
```

- **Root servers** (13 globally): know about all top-level domains
- **Top-Level Domain servers (TLD)**: `.no`, `.com`, `.org`, etc.
- **Authoritative name servers**: responsible for specific domains
- **Recursive resolvers**: do the work for clients (typically your ISP or Google 8.8.8.8)

#### DNS Record Types

| Record | Name | Function | Example |
|--------|------|----------|---------|
| A | Address | Name → IPv4 address | `ndla.no → 185.45.32.10` |
| AAAA | IPv6 Address | Name → IPv6 address | `ndla.no → 2001:db8::1` |
| CNAME | Canonical Name | Alias → another name | `www.ndla.no → ndla.no` |
| MX | Mail Exchanger | Domain → mail server | `ndla.no → mail.ndla.no` |
| PTR | Pointer | IP → name (reverse lookup) | `10.1.168.192.in-addr.arpa → pc01.lab.lan` |
| NS | Name Server | Which servers are authoritative | `ndla.no → ns1.domeneshop.no` |
| SOA | Start of Authority | Zone metadata | Primary name server, serial number |

An **A Record** connects a hostname to a specific IPv4 address — this is the most common and important DNS record type.

#### DNS in Active Directory

In an AD network, DNS is installed on the domain controller. This DNS server is **authoritative** for the local domain (e.g. `lab.lan`) and knows all machines that are joined to the domain.

For lookups outside the local domain (e.g. `google.com`), **forwarders** are used: the DNS server sends unresolved lookups to the router's IP or an external DNS server (e.g. `8.8.8.8`).

#### Port and Protocol

DNS primarily uses **UDP on port 53** for regular lookups (fast, low overhead). For zone transfers between DNS servers, it uses **TCP on port 53**.

#### Security: DNS Spoofing and DHCP Snooping

DNS spoofing is an attack where an attacker sends fake DNS responses to redirect users to malicious websites. DNSSEC (DNS Security Extensions) can be used to protect against this. On switches, **DHCP snooping** is used to prevent rogue DHCP servers: the switch blocks DHCP responses from ports that are not configured as trusted.

## Example / Lab

### Lab: nslookup Commands

`nslookup` is a command-line tool for DNS troubleshooting. Run from CMD or PowerShell:

```cmd
# Look up IP address for a domain
nslookup ndla.no

# Specify a particular DNS server for the lookup
nslookup ndla.no 8.8.8.8

# Look up MX record (mail server)
nslookup -type=MX ndla.no

# Reverse lookup (IP to name)
nslookup 185.45.32.10

# Interactive mode
nslookup
> set type=A
> google.com
> exit
```

Example output from `nslookup ndla.no`:
```
Server:  UnKnown
Address:  192.168.1.1

Non-authoritative answer:
Name:    ndla.no
Addresses:  185.45.32.10
```

"Non-authoritative answer" means the response came from cache, not directly from an authoritative server.

### Lab: DHCP Check

```cmd
# View full IP configuration including DHCP server and lease time
ipconfig /all

# Release DHCP lease
ipconfig /release

# Get new DHCP lease
ipconfig /renew

# Flush DNS cache on the client
ipconfig /flushdns
```

### Practical Troubleshooting

Common problems and solutions:
- **No IP address**: client hasn't reached the DHCP server (check if scope is active, if DHCP on router is off, if there are enough available addresses)
- **Can't reach ndla.no**: check with `nslookup ndla.no` — if the DNS lookup fails, the problem is DNS. If DNS responds but the page won't open, the problem is the network connection.
- **169.254.x.x address**: APIPA address — client didn't get a response from the DHCP server

## Study Guide

**DHCP — Core Understanding**
DHCP automates IP configuration. The DORA process (Discover → Offer → Request → Acknowledge) is the mechanism that happens in the background. A scope defines the address space. Lease time controls how long an address is held by a client.

**DNS — Core Understanding**
DNS is hierarchical (root → TLD → domain → hostname). The A record is the most important. CNAME is used for aliases. MX points to the mail server. PTR is used for reverse lookups. In AD, the DNS server is authoritative for the local domain.

**Common Exam Points**
- The DORA process step by step
- What the different DNS record types do (A, AAAA, CNAME, MX, PTR)
- The difference between authoritative DNS server and recursive resolver
- What a forwarder is
- The commands ipconfig, nslookup

## FAQ

**What does the abbreviation DORA stand for in DHCP context?**
DORA stands for Discover, Offer, Request, Acknowledge — the four messages in the DHCP process where the client finds a server, receives an offer, accepts it, and the server confirms the assignment.

**What is a DNS A record?**
An A record (Address) is a DNS record that connects a domain name to an IPv4 address. E.g. `ndla.no → 185.45.32.10`.

**Why is DHCP Discover sent as a broadcast?**
Because the client does not yet have an IP address and does not know the DHCP server's address. Broadcast (`255.255.255.255`) reaches all devices on the local network, including the DHCP server.

**What is a DNS forwarder?**
A forwarder is a configuration on the DNS server that says: "Lookups I cannot answer myself, I send on to this other DNS server." In AD networks, the forwarder typically points to the router's IP to resolve internet addresses.

**What is the difference between a PTR record and an A record in DNS?**
An A record translates name to IP (forward lookup). A PTR record (Pointer) does the opposite — it translates an IP address to a name (reverse lookup). PTR records are used by email servers and logs among other things.

**What are scope and lease in DHCP?**
Scope is the address range the DHCP server can distribute from. Lease is the time agreement — the client "borrows" the address for a specific period. When the lease period nears its end, it is automatically renewed.

**What happens if there are two DHCP servers on the same network?**
It causes IP address conflicts. Both servers can assign the same address to different clients, creating chaos. In domain networks, DHCP on the router is always disabled when Windows Server DHCP is configured.

**What are DHCP snooping and DNS spoofing?**
DNS spoofing is an attack where fake DNS responses redirect users to malicious websites. DHCP snooping is a switch feature that blocks rogue DHCP servers by only allowing DHCP responses from trusted ports.

## Quiz

<details>
<summary>Question 1: What does the abbreviation DORA stand for in DHCP context?</summary>

**Answer:** DORA stands for Discover, Offer, Request, Acknowledge — the four messages in the DHCP process where the client finds a server, receives an offer, accepts it, and the server confirms the assignment.
</details>

<details>
<summary>Question 2: What is a DNS A record?</summary>

**Answer:** An A record (Address) is a DNS record that connects a domain name to an IPv4 address. E.g. `ndla.no → 185.45.32.10`.
</details>

<details>
<summary>Question 3: Why is DHCP Discover sent as a broadcast?</summary>

**Answer:** Because the client does not yet have an IP address and does not know the DHCP server's address. Broadcast (`255.255.255.255`) reaches all devices on the local network, including the DHCP server.
</details>

<details>
<summary>Question 4: What is a DNS forwarder?</summary>

**Answer:** A forwarder is a configuration on the DNS server that says: "Lookups I cannot answer myself, I send on to this other DNS server." In AD networks, the forwarder typically points to the router's IP to resolve internet addresses.
</details>

<details>
<summary>Question 5: What is the difference between a PTR record and an A record in DNS?</summary>

**Answer:** An A record translates name to IP (forward lookup). A PTR record (Pointer) does the opposite — it translates an IP address to a name (reverse lookup). PTR records are used by email servers and logs among other things.
</details>

## Resources

- [Deactivate existing DHCP server — NDLA](https://ndla.no/nb/r/driftsstotte-im-itk-vg2/deaktivere-eksisterende-dhcp-server/9d5c1dedc7)
- [DNS Server Installation — NDLA](https://ndla.no/nn/r/driftsstotte-im-itk-vg2/installasjon-av-dns-server/4246401a38)
- [windowsnett.no — lesson 11: DHCP and DNS](https://www.windowsnett.no/)
- [DHCP Overview — Microsoft Learn](https://learn.microsoft.com/nb-no/windows-server/networking/technologies/dhcp/dhcp-top)
