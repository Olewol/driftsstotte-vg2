---
title: "Server Roles"
emne: nettverk
competence_goals:

  - km-05

language: en
original: serverroller.md
kilder:

  - ndla
  - <https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/ad-ds-getting-started>
  - <https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/>
  - <https://www.professormesser.com/network-plus/>
  - <https://www.cloudflare.com/learning/>
  - <https://learn.microsoft.com/en-us/training/paths/networking-fundamentals/>

tags: [server, ad, dns, dhcp, file server, web server, windows-server, server role]
flashcards: <https://notebooklm.google.com/notebook/f7e5ad6c-7082-40cf-abd5-7a41b540f8e1>
public: true
video: <https://www.youtube.com/watch?v=vVbrlNlqJP4>
notebooklm: true
---

# Server Roles

## Introduction

AA server is not just a powerful computer — it's a machine with specific roles and responsibilities in the network.
AAIn Windows Server, you install services as "server roles" via Server Manager. Knowing the most important server roles,
AAwhat they do, and which protocols they use, is essential for IT support: you plan the infrastructure, install the
Aservices, and keep them running.

SServer roles are closely tied to [[active-directory-en]], [[bruker-og-tilgangsstyring-en|user and access management]]
SSand [[filsystem-en|file system]], and are a central part of [[driftsarkitektur-en|operations architecture]] in a
Sbusiness. A domain controller is not one role, but a combination of AD DS, DNS, and often DHCP working together.

## Theory

### What is a Server Role?

A**server role**is an additional function you install in Windows Server via:
`Server Manager → Manage → Add Roles and Features`

OOne physical server can have multiple roles installed, but for performance and security reasons, it's recommended to
OOkeep roles separate — especially in production. In a school lab, it's common to have AD DS, DNS, and DHCP on the same
Odomain controller.

### Overview of Key Server Roles

|| Role | Function | Protocol/port | Typical Use |
|| ------ | ---------- | -------------- | ------------- |
|| AD DS | Centralized authentication and directory | Kerberos (88), LDAP (389) | Business network with domain |
|| DNS Server | Name resolution | UDP/TCP 53 | Resolve domain names to IP |
|| DHCP Server | Automatic IP assignment | UDP 67/68 | Clients in the network |
|| Web Server (IIS) | Serve HTTP/HTTPS requests | TCP 80/443 | Internet/intranet portal |
|| File Server | Share folders over the network | SMB (TCP 445), NFS | Shared storage for employees |
|| Print Server | Share and manage printers | TCP 9100, LPD (515) | Shared printers in network |
|| Mail Server | Send and receive email | SMTP 25, IMAP 143, POP3 110 | Company email service |

---

### Active Directory Domain Services (AD DS)

AAD DS is the foundation of a Windows domain network. A server with the AD DS role is called a**domain controller**and
Amanages:
-**Authentication**: logs in users with username and password
-**Authorization**: controls what users have access to
-**Directory**: central registry of all users, computers, and resources

***AD DS**— Active Directory Domain Services — is a directory service that centralizes the administration of users,
*groups, and computers in a network.

#### AD Hierarchy

```bash
Forest
  └── Tree: company.no
        └── Domain: company.no
              ├── Subdomain: sales.company.no
              └── OU: Employees
                    ├── OU: Oslo
                    └── OU: Bergen
```

-**Forest**: top level, contains one or more trees
-**Tree**: domain with subdomains that share a namespace
-**Domain**: administrative boundary (e.g. `lab.lan`)
-**OU (Organizational Unit)**: logical folder for organizing objects, supports Group Policy
-**FQDN**: Fully Qualified Domain Name — e.g. `pc01.lab.lan`

#### Users and Groups

-**User accounts**: assigned individually to resources, or via group membership
-**Security groups**: an account can belong to multiple groups → scalable access management
-**OU vs. folder**: OU supports Group Policy Objects (GPO) and delegated administration

The domain controller requires DNS — the DNS server role is installed automatically or manually during AD DS setup.

---

### DNS Server

TThe DNS server translates domain names to IP addresses. In an AD network, the domain controller's DNS
Tis**authoritative**for the local domain and knows all AD objects.

Configuration in Windows Server:

- Zones: primary zone for `lab.lan` is created automatically with AD DS
- Forwarders: lookups outside `lab.lan`are forwarded to router (e.g.`192.168.1.1`) or public DNS (`8.8.8.8`)
- Dynamic update: clients register automatically in DNS when joining the domain

See [[dns-og-dhcp-en|DNS and DHCP]] for a full review of DNS.

---

### DHCP Server

TThe DHCP server automatically assigns IP configuration to network clients. In a domain environment, this role takes over
Tfrom the router's built-in DHCP.

A**DHCP Scope**is a defined range of IP addresses that the DHCP server can assign to clients on a particular subnet.

Important steps:

1. Disable DHCP on the router
2. Install the DHCP Server role in Windows Server
3. Create a scope (e.g. `192.168.1.100`–`192.168.1.200`)
4. Configure scope options: gateway, DNS server, lease time
5. Activate the scope

See [[dns-og-dhcp-en|DNS and DHCP]] for a full review of DHCP.

---

### Web Server — IIS (Internet Information Services)

***IIS**(Internet Information Services) is Microsoft's web server role used to host websites or web applications.
*It is a server role available in Windows Server.

**Function**: serves HTTP/HTTPS requests from browsers. Used for:

- Internal portals and intranet pages
- Web applications (ASP.NET, PHP)
- Administrative interfaces for other services

**Competitors**:
-**Apache HTTP Server**— open source, dominant on Linux
-**Nginx**— open source, known for high performance and reverse proxy use

**Setting up a website in IIS**:

1. Server Manager → Add Roles → Web Server (IIS)
2. IIS Manager → Sites → Add Website
3. Specify name, physical path (e.g. `C:\inetpub\wwwroot\mysite`), port, and optionally hostname
4. Bind domain name in DNS to the server's IP

---

### File Server

A file server makes folders available over the network so users can store and retrieve files from a central location.

**SMB (Server Message Block)**is the Windows standard for network sharing, port 445.

**Setting up a shared folder (share)**:

1. Right-click folder → Properties → Sharing → Advanced Sharing
2. Check "Share this folder", give share name (e.g. `Documents`)
3. Set share permissions (who can read/write via the share)
4. Set NTFS permissions for granular access control

***NTFS permissions**are file system-level permissions that determine what access users and groups have to files and
*folders on a file server. They are more granular than share permissions and also apply to local access.

Access from client:

```sql
\\servername\Documents
```

Or via "Map network drive" to assign a drive letter (e.g. Z:).

***NFS (Network File System)**: Linux/Unix standard for file sharing. Used in heterogeneous environments.
*Windows Server supports NFS via the "File Services" role.

***NAS (Network Attached Storage)**: dedicated storage device with file server functionality (e.g. TrueNAS, Synology).
*Alternative to Windows file server for simpler setup and large storage capacity.

---

### Mail Server

A mail server handles sending and receiving email for a domain.

|| Component | Function | Protocol |
|| ----------- | ---------- | ---------- |
|| MTA (Mail Transfer Agent) | Sends and forwards email between servers | SMTP (port 25) |
|| MDA (Mail Delivery Agent) | Delivers email to user's mailbox | Internal |
|| MUA (Mail User Agent) | Client program (Outlook, Thunderbird) | IMAP/POP3 |

EExamples of mail server solutions: Microsoft Exchange Server (Windows), Postfix/Dovecot (Linux), hMailServer (simple
EWindows solution).

---

### Print Server

AA print server shares one or more printers on the network so all users can print without physically connecting to the
Aprinter.

In Windows Server: Add Roles → Print and Document Services → Print Server.

Administration via**Print Management**console: view queues, manage drivers, monitor status.

---

### Typical Server Setup in Data Lab (VG2)

```bash
[Windows Server 2022]
├── AD DS (domain controller for lab.lan)
├── DNS server (authoritative for lab.lan, forwarder: 192.168.1.1)
├── DHCP server (scope: 192.168.1.100–200)
└── File server (share: \\server01\Students)

[Client machines: Windows 10/11]
└── Domain-joined to lab.lan
    └── Log in with domain users from AD
    └── Get IP from DHCP server
    └── Resolve lab.lan via DNS server
```

Static IP on server: `192.168.1.10/24`, gateway `192.168.1.1`, DNS `192.168.1.10` (itself).

## Example / Lab

### Lab: Install AD DS and Join a Client to the Domain

1.**Install the AD DS role**on Windows Server:

   - Server Manager → Add Roles → Active Directory Domain Services
   - After: Promote this server to a domain controller
   - Choose "Add a new forest", domain name: `lab.lan`
   - Set DSRM password, complete the wizard, restart

2.**Join a Windows client to the domain**:

   - Client machine → Settings → System → About → Join a domain
   - Type `lab.lan`, provide domain controller administrator credentials
   - Restart the client
   - Log in with domain username: `lab\username`

3.**Create a user in AD**:

   - Server Manager → Tools → Active Directory Users and Computers
   - Navigate to desired OU → New → User
   - Fill in first name, last name, and logon name

## Study Guide

*## Server Roles — Core Understanding
AA Windows Server is a platform for running services ("roles"). The most important ones to know for VG2 are: AD DS
AA(domain and authentication), DNS (name resolution), DHCP (IP assignment), IIS (web server) and File Server (SMB
Asharing).

*## AD DS — The Most Important Thing to Understand
AAD DS is the foundation. It collects user accounts, computers, and policies in one central system.
AAA domain controller is a server with the AD DS role. OUs structure AD and are the anchor point for Group Policy.
ADNS is a prerequisite for AD.

*## File Server and Access Control
NNTFS permissions always apply, share permissions only apply during network access.
NNWhen both are set, the most restrictive combination takes effect. Folder structure and permissions are closely tied to
N[[bruker-og-tilgangsstyring-en|user and access management]].

*## Common Exam Points

- The difference between an OU and a regular folder in AD
- What FQDN means, with an example
- The steps to join a client to a domain
- Which protocols/ports the different server roles use

## FAQ

*## What is the difference between an OU and a folder in Active Directory?
AAn OU (Organizational Unit) is a logical container in AD that supports delegated administration and Group Policy Objects
AA(GPO). A regular folder does not support this. OUs are used to structure AD and manage policies for groups of users or
Acomputers.

*## Which protocol does a Windows file server use for network sharing, and on which port?
SMB (Server Message Block), port 445 (TCP). Older versions used port 139 (via NetBIOS).

*## What is the difference between IIS, Apache, and Nginx?
AAll three are web servers. IIS is Microsoft's solution for Windows Server. Apache is the most widely used open source
AAweb server, primarily on Linux. Nginx is known for high performance and is widely used as a reverse proxy and load
Abalancer, in addition to being a web server. IIS is integrated with Windows authentication and .NET.

*## What is an FQDN, and give an example?
FFQDN (Fully Qualified Domain Name) is the complete domain name of a device, including all parts up to the root.
FExample: `pc01.lab.lan`— here`pc01`is the machine name,`lab`is the domain, and`lan` is the top-level domain.

*## Why does a domain controller need the DNS server role?
AActive Directory relies on DNS for clients to find the domain controller (via SRV records in DNS).
AAWithout DNS, clients cannot log in, find AD services, or communicate with the domain.
AThe DNS role is therefore always installed in combination with AD DS.

*## What is a DHCP Scope and why is it important to configure it correctly?
AA DHCP Scope is the address range the server distributes from. Incorrect configuration (too few addresses, wrong gateway
AAor DNS) means clients cannot reach the network. Scope options like gateway and DNS server are just as important as the
Aaddresses themselves.

*## What is AD DS and why is it central in business networks?
AAD DS is the directory service that collects all network objects (users, groups, machines) in one place.
AAInstead of each user having local accounts on each machine, everyone logs in with their AD account — and access is
Amanaged centrally via groups and policies.

*## What is the difference between NTFS permissions and share permissions?
SShare permissions only apply when connecting to the folder via the network. NTFS permissions always apply — including
SSlocal access. Best practice is to set the share to "Everyone — Full Control" and use NTFS permissions for the actual
Saccess control.

## Quiz

<details>
<summary>Question 1: What is the difference between an OU and a folder in Active Directory?</summary>

***Answer:**An OU (Organizational Unit) is a logical container in AD that supports delegated administration and Group
**Policy Objects (GPO). A regular folder does not support this. OUs are used to structure AD and manage policies for
*groups of users or computers.
</details>

<details>
<summary>Question 2: Which protocol does a Windows file server use for network sharing, and on which port?</summary>

**Answer:**SMB (Server Message Block), port 445 (TCP). Older versions used port 139 (via NetBIOS).
</details>

<details>
<summary>Question 3: What is the difference between IIS, Apache, and Nginx?</summary>

***Answer:**All three are web servers. IIS is Microsoft's solution for Windows Server.
**Apache is the most widely used open source web server, primarily on Linux. Nginx is known for high performance and is
**widely used as a reverse proxy and load balancer, in addition to being a web server.
*IIS is integrated with Windows authentication and .NET.
</details>

<details>
<summary>Question 4: What is an FQDN, and give an example?</summary>

***Answer:**FQDN (Fully Qualified Domain Name) is the complete domain name of a device, including all parts up to the
*root. Example: `pc01.lab.lan`— here`pc01`is the machine name,`lab`is the domain, and`lan` is the top-level domain.
</details>

<details>
<summary>Question 5: Why does a domain controller need the DNS server role?</summary>

***Answer:**Active Directory relies on DNS for clients to find the domain controller (via SRV records in DNS).
**Without DNS, clients cannot log in, find AD services, or communicate with the domain.
*The DNS role is therefore always installed in combination with AD DS.
</details>

## Resources

- [User Accounts, Groups, and Structure in AD — NDLA](<https://ndla.no/r/driftsstotte-im-itk-vg2/brukerkontoer-grupper-og-struktur-i-active-directory/2c7a25f92e>)
- [Domains and Hierarchy in Active Directory — NDLA](<https://ndla.no/en/r/driftsstotte-im-itk-vg2/domener-og-hierarkiet-i-active-directory/db58e9da66>)
- [Connect to Share in Windows 10 — NDLA](<https://ndla.no/en/r/driftsstotte-im-itk-vg2/koble-opp-share-i-windows-10/5a04d2403d>)
- [HTTP and IIS — windowsnett.no](<http://www.windowsnett.no/leksjoner/L09/Leksjon%209%20beskrivelse.htm>)
- [windowsnett.no — lessons 5–7: AD, groups, shared folders](<https://www.windowsnett.no/>)
- [Active Directory, DNS & DHCP Roles Installation & Configuration on Server 2022 — PowerUser (15 min)](<https://www.youtube.com/watch?v=vVbrlNlqJP4>)
- [Getting Started with AD DS — Microsoft Learn](<https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/ad-ds-getting-started>)
