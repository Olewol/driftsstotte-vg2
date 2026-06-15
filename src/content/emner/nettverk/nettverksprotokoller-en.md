---
title: "Network Protocols"
emne: nettverk
competence_goals:

  - km-05

language: en
original: nettverksprotokoller.md
kilder:

  - ndla
  - <https://snl.no/protokoll_-_it>
  - <https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/>
  - <https://www.professormesser.com/network-plus/>
  - <https://www.cloudflare.com/learning/>
  - <https://learn.microsoft.com/en-us/training/paths/networking-fundamentals/>

tags: [protocols, http, ftp, ssh, smtp, dns, ports, tcp, udp]
flashcards: <https://notebooklm.google.com/notebook/f7e5ad6c-7082-40cf-abd5-7a41b540f8e1>
public: true
video: <https://www.youtube.com/watch?v=uwoD5YskPmc>
notebooklm: true
---

# Network Protocols

## Introduction

AA network protocol is a set of rules that defines how devices communicate. Without protocols, network communication
AAwould be like speaking two different languages — nobody would understand each other.
AAKnowing the most important protocols, what they are used for, and which port numbers they run on, is fundamental
Aknowledge for any IT support technician — both for configuration and troubleshooting.

PProtocols reside at different layers of the [[osi-modellen-en|OSI model]] and the [[tcp-ip-modellen-en|TCP/IP model]].
PPPort numbers and the transport protocols TCP and UDP are the foundation that all application protocols build upon.
PThe protocols for [[dns-og-dhcp-en|DNS and DHCP]] are central network services that use these mechanisms.

## Theory

### Transport Layer Protocols: TCP and UDP

All application protocols run either over TCP or UDP at the transport layer.

||  | TCP | UDP |
|| --- | --- | --- |
|| **Type** | Connection-oriented | Connectionless |
|| **Reliability** | Guaranteed delivery, ordering | No guarantee |
|| **Speed** | Slower (overhead for ack/retransmit) | Faster |
|| **Use case** | Web, email, file transfer, SSH | DNS, streaming, VoIP, gaming |

***TCP (Transmission Control Protocol)**is a connection-oriented and reliable protocol that ensures data arrives in the
*correct order and without errors through error checking and acknowledgments.

***UDP (User Datagram Protocol)**is a connectionless protocol that prioritizes speed over reliability; it sends data
*without confirming receipt, often used for streaming and gaming.

### Port Numbers

AA**port number**is a number from 0–65535 (16 bit) that identifies which service a network packet is intended for on a
Amachine. The IP address finds the machine; the port number finds the right service on the machine.

Categories:
-**Well-known ports (0–1023)**: standard ports for well-known services (HTTP, SMTP, DNS, etc.)
-**Registered ports (1024–49151)**: used by applications
-**Dynamic/ephemeral ports (49152–65535)**: temporarily assigned to client connections

AA**three-way handshake**is the process TCP uses to establish a stable connection between sender and receiver (SYN →
ASYN-ACK → ACK).

### Important Protocols

|| Protocol | Port(s) | Transport | Function | Security Level |
|| ---------- | --------- | ----------- | ---------- | ---------------- |
|| HTTP | 80 | TCP | Web pages, request/response | Unencrypted — don't use for sensitive data |
|| HTTPS | 443 | TCP | HTTP encrypted with TLS/SSL | Encrypted — standard today |
|| FTP | 20 (data), 21 (control) | TCP | File transfer | Unencrypted — passwords in plain text |
|| SFTP | 22 | TCP | Secure file transfer (over SSH) | Encrypted |
|| FTPS | 21 (explicit), 990 (implicit) | TCP | FTP with TLS encryption | Encrypted |
|| SSH | 22 | TCP | Secure remote terminal access | Encrypted |
|| RDP | 3389 | TCP | Graphical remote control of Windows | Encrypted (TLS in newer versions) |
|| SMTP | 25 (server-to-server), 587 (client-to-server) | TCP | Sending email | Port 587 uses STARTTLS |
|| IMAP | 143 (unencrypted), 993 (SSL/TLS) | TCP | Email synchronization | Port 993 encrypted |
|| POP3 | 110 (unencrypted), 995 (SSL/TLS) | TCP | Email download | Port 995 encrypted |
|| DNS | 53 | UDP (primary), TCP (zone transfer) | Name resolution | Unencrypted (DNS over HTTPS exists) |
|| DHCP | 67 (server), 68 (client) | UDP | Automatic IP assignment | No authentication |
|| SNMP | 161 (agent), 162 (trap) | UDP | Network monitoring and management | SNMPv3 is encrypted |

### Detailed Walkthrough

#### HTTP and HTTPS (port 80/443)

HHTTP (Hypertext Transfer Protocol) is the foundation of web communication. The protocol uses a**request/response
Hmodel**:

```text
Client → Server:
GET /index.html HTTP/1.1
Host: ndla.no

Server → Client:
HTTP/1.1 200 OK
Content-Type: text/html
...
```

**HTTP methods**: GET (get resource), POST (send data), PUT (update), DELETE (delete)

**HTTP status codes**:

- 2xx Success: `200 OK`, `201 Created`
- 3xx Redirection: `301 Moved Permanently`, `302 Found`
- 4xx Client Error: `400 Bad Request`, `403 Forbidden`, `404 Not Found`
- 5xx Server Error: `500 Internal Server Error`, `503 Service Unavailable`

***HTTPS**= HTTP + TLS. The connection is encrypted with TLS (Transport Layer Security) — this is what the padlock icon
*in the browser means. All modern web traffic should use HTTPS.

#### FTP and SFTP (port 21/22)

FFTP (File Transfer Protocol) uses two separate connections: a**control channel**(port 21) for commands and a**data
Fchannel**(port 20) for the actual file transfer. FTP is unencrypted — usernames and passwords are sent in plain text.

***SFTP**(SSH File Transfer Protocol) is a complete replacement that runs over SSH (port 22) and is encrypted from start
*to finish. SFTP is the standard today.

Tools: FileZilla (graphical FTP/SFTP client), WinSCP (Windows), scp command (Linux/terminal).

#### SSH (port 22)

SSSH (Secure Shell) provides secure remote access to a command line — primarily on Linux/Unix servers, but also on
Snetwork equipment like switches and routers.

```bash

## Connect to server via SSH

ssh username@192.168.30.10

## Copy file securely (SCP over SSH)

scp file.txt username@192.168.30.10:/home/username/
```

SSSH uses asymmetric cryptography: server and client exchange keys, and all communication is encrypted.
SMuch more secure than Telnet (port 23), which was its predecessor.

#### Email Protocols (SMTP/IMAP/POP3)

The email system uses different protocols for sending and receiving:

```bash
[Sender client] --SMTP(587)-→ [Sender's mail server] --SMTP(25)-→ [Recipient's mail server]
                                                                              ↓
                                                               [Recipient client] ←--IMAP(993)--
```

-**SMTP**sends email (client to server and between servers)
-**IMAP**synchronizes email — emails remain on the server (recommended)
-**POP3**downloads and deletes from server — old solution, rarely used

#### SNMP (port 161/162)

SSNMP (Simple Network Management Protocol) is used to monitor and manage network devices (switches, routers, servers).
SSAn SNMP**agent**runs on each device and reports status. An**NMS**(Network Management Station) polls agents on port 161.
SAgents can send alerts (**traps**) to the NMS on port 162 when events occur.

SSNMPv1 and v2c use "community strings" (passwords in plain text).**SNMPv3**is the secure version with encryption and
Sauthentication.

### Security and Ports

WWell-known port numbers are also well-known attack targets. SSH (port 22) and RDP (port 3389) are constantly subjected
Wto automated login attempts (brute force). Countermeasures:

- Use VPN — only allow RDP/SSH from internal network or VPN
- Restrict with IP restrictions in firewall
- Use key-based authentication for SSH (not passwords)
- Enable account locking after X failed attempts

## Example / Lab

### Test Protocols from the Command Line

```cmd

## Test HTTP access with curl

curl -I <http://ndla.no>

## Test if a port is open (PowerShell)

Test-NetConnection -ComputerName ndla.no -Port 443

## Test if a port is open (CMD/nmap)

nmap -p 80,443,22 192.168.1.10

## Show active connections and ports

netstat -an

## Connect via SSH (from Windows Terminal/PowerShell)

ssh admin@192.168.1.1
```

### Identify Protocol from Port

|| Port | Protocol | Service |
|| ------ | ---------- | --------- |
|| 22 | ? | ? |
|| 80 | ? | ? |
|| 443 | ? | ? |
|| 3389 | ? | ? |
|| 25 | ? | ? |

Answer: SSH/SFTP, HTTP, HTTPS, RDP, SMTP

### Analyze Packets with Wireshark

Wireshark is a network analysis tool that lets you see actual network traffic. Start a capture and filter by protocol:

- `http` — see HTTP requests
- `dns` — see DNS lookups
- `tcp.port == 443` — see HTTPS traffic (encrypted content, but metadata visible)

This provides concrete understanding of the protocols in action and is valuable for troubleshooting.

## Study Guide

*## TCP vs. UDP — Core Understanding
TTCP is reliable and connection-oriented (three-way handshake, ACK). UDP is fast and connectionless.
TTChoose TCP when you need accuracy (web, email, file transfer). Choose UDP when you need speed (streaming, DNS lookups,
TVoIP).

*## Ports to Memorize
Create a table: HTTP=80, HTTPS=443, SSH=22, FTP=21/20, SMTP=25/587, IMAP=143/993, DNS=53, RDP=3389, DHCP=67/68.

*## Common Exam Points

- Identify which protocol and port is used for a given task
- The difference between FTP and SFTP (security)
- What HTTP status codes mean (2xx, 4xx, 5xx)
- Why RDP exposed to the internet is a security risk

## FAQ

*## Which port does HTTPS use, and what does it mean that a connection is HTTPS?
HHTTPS uses port 443. It means that the HTTP traffic is encrypted with TLS (Transport Layer Security).
HThe content cannot be read by anyone eavesdropping on the connection.

*## What is the difference between FTP and SFTP?
FFTP (port 21) transfers files without encryption — usernames, passwords, and files are sent in plain text and can be
Fintercepted. SFTP is secure file transfer over SSH (port 22) where everything is encrypted. SFTP is the standard today.

*## Explain the difference between SMTP and IMAP.
SSMTP is used to*send*email (from client to server and between servers). IMAP is used to*retrieve and synchronize*email
Sfrom server to client — the email remains on the server so you can read it from multiple devices.

*## What is an HTTP 404 error?
HHTTP 404 Not Found means the server received the request but did not find the requested resource (e.g., the page or file
Hdoes not exist at that address). It is a client error (4xx).

*## Why is it a security risk to have RDP (port 3389) open to the internet?
RRDP is a popular attack target. Automated tools constantly scan the internet for open port 3389 and attempt brute force
RRlogin. If successful, the attacker gets graphical access to the Windows machine. The solution is to only allow RDP from
RVPN or the IP addresses of administrators.

*## What is the difference between TCP and UDP?
TTCP is connection-oriented and guarantees delivery in the correct order. UDP is connectionless and prioritizes speed.
TTCP is used where reliability is important; UDP where speed is more important than accuracy.

*## What is the three-way handshake?
TThe three-way handshake is the process TCP uses to establish a connection: the client sends SYN, the server responds
TSYN-ACK, the client confirms with ACK. After this, the connection is established.

*## What are well-known ports?
WWell-known ports are port numbers 0–1023 that are reserved for standardized services by IANA.
WE.g., HTTP=80, HTTPS=443, SSH=22. These ports are known attack targets and should be protected with firewall rules.

## Quiz

<details>
<summary>Question 1: Which port does HTTPS use, and what does it mean that a connection is HTTPS?</summary>

***Answer:**HTTPS uses port 443. It means that the HTTP traffic is encrypted with TLS (Transport Layer Security).
*The content cannot be read by anyone eavesdropping on the connection.
</details>

<details>
<summary>Question 2: What is the difference between FTP and SFTP?</summary>

***Answer:**FTP (port 21) transfers files without encryption — usernames, passwords, and files are sent in plain text and
**can be intercepted. SFTP is secure file transfer over SSH (port 22) where everything is encrypted.
*SFTP is the standard today.
</details>

<details>
<summary>Question 3: Explain the difference between SMTP and IMAP.</summary>

***Answer:**SMTP is used to*send*email (from client to server and between servers).
**IMAP is used to*retrieve and synchronize*email from server to client — the email remains on the server so you can read
*it from multiple devices.
</details>

<details>
<summary>Question 4: What is an HTTP 404 error?</summary>

***Answer:**HTTP 404 Not Found means the server received the request but did not find the requested resource (e.g., the
*page or file does not exist at that address). It is a client error (4xx).
</details>

<details>
<summary>Question 5: Why is it a security risk to have RDP (port 3389) open to the internet?</summary>

***Answer:**RDP is a popular attack target. Automated tools constantly scan the internet for open port 3389 and attempt
**brute force login. If successful, the attacker gets graphical access to the Windows machine.
*The solution is to only allow RDP from VPN or the IP addresses of administrators.
</details>

## Resources

- [TCP, UDP and Ports — NDLA](<https://ndla.no/nb/r/driftsstotte-im-itk-vg2/tcp-udp-og-porter/d7acb2196e>)
- [SSH — NDLA](<https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/topic:6e8a2eaf-4983-4d42-a9b0-911b5921b44a/resource:db7b7d9d-9894-418a-8458-74a5cfec1e60>)
- [Transport Layer TCP and UDP — windowsnett.no](<http://windowsnett.no/leksjoner/L08/8b%20Transportlaget%20TCP%20og%20UDP%20skjerm.pdf>)
- [HTTP and IIS — windowsnett.no](<http://www.windowsnett.no/leksjoner/L09/Leksjon%209%20beskrivelse.htm>)
- [Protocol — SNL](<https://snl.no/protokoll_-_it>)
