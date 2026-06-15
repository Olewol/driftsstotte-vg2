---
title: "Active Directory"
emne: operativsystem
kompetansemaal:

  - km-04

kilder:

  - ndla
  - <https://learn.microsoft.com/nb-no/windows-server/identity/ad-ds/plan/active-directory-domain-services-logical-structure-design-guide>
  - <https://learn.microsoft.com/nb-no/windows-server/>
  - <https://documentation.ubuntu.com/server/>
  - <https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/>

video: <https://www.youtube.com/watch?v=85-bp7XxWDQ>
tags: []
flashcards: <https://notebooklm.google.com/notebook/70aa7fff-78f3-4825-aeed-bc879a29770f>
public: true
notebooklm: true
language: en
original: active-directory.md
---

## Introduction

***Active Directory (AD)**is Microsoft's directory service and the heart of Windows-based enterprise environments.
**AD centralizes the management of users, computers, groups, and policies across an entire organization.
*Instead of managing each machine separately, you control everything from one place — the domain controller.

IIn Norwegian schools and businesses, Active Directory Domain Services (AD DS) is the most common solution for user
IIadministration. This article covers its structure, components, and practical use.
IIAD is closely tied to [[dns-og-dhcp-en]] — without proper DNS, domain logon does not work.
IIAlso see [[serverroller-en]] for an overview of roles installed on a Windows Server, and
I[[bruker-og-tilgangsstyring-en]] for details on permissions and groups.

---

## Theory

### The AD Hierarchy

Active Directory is organized as a hierarchy with four levels:

```diff
Forest
└── Tree
    └── Domain
        └── Organizational Unit (OU)
```

*## Forest
TThe topmost level in AD. A forest can contain one or more trees. All domains in the same forest share a common schema
Tand global catalog. `Enterprise Admins` have control over the entire forest.

*## Tree
A collection of domains with a contiguous DNS namespace. Example: `school.no`with the subdomain`students.school.no`.

*## Domain
TThe fundamental unit in AD. A domain is a logical group of users, computers, and resources under common administration.
TIt is identified by a DNS name, e.g., `school.local`or`company.no`.

*## Organizational Unit (OU)
Logical containers within a domain. OUs are used to:

- Group objects by function, department, or geography
- Delegate administrative access (e.g., let the IT department manage only its own OU)
- Attach Group Policies (GPOs) to specific users or machines

Typical OU structure:

```javascript
school.local
├── OU=Users
│   ├── OU=Teachers
│   └── OU=Students
├── OU=Computers
│   ├── OU=Classrooms
│   └── OU=Administration
└── OU=Groups
```

### Domain Controller (DC)

A**domain controller**is a server with AD DS installed. The DC:

- Authenticates all logons in the domain
- Stores and replicates the AD database (`ntds.dit`)
- Runs DNS (typically) and the Kerberos authentication service

**Best practice**: Have at least two domain controllers. If one DC fails, the other takes over without downtime.

TThe first DC in a domain is also called the first domain-creating controller and holds special FSMO roles (*Flexible
TSingle Master Operation*).

### LDAP

***LDAP**(Lightweight Directory Access Protocol) is the protocol AD uses to provide access to directory data.
**When you search for a user in AD or an application authenticates against AD, LDAP is used.
*Encrypted LDAP is called LDAPS (LDAP over SSL/TLS, port 636).

### Kerberos Authentication

AD uses**Kerberos**as its default authentication protocol (instead of the older NTLM).

In short:

1. The user logs in and sends their username to the DC
2. The DC (KDC — Key Distribution Center) returns an encrypted**TGT**(Ticket Granting Ticket)
3. When the user wants to access a resource, the client uses the TGT to request a**service ticket**
4. The service ticket is presented to the resource — without the password ever being sent over the network

KKerberos is more secure than NTLM because the password is never transmitted, only encrypted tickets with a limited
Klifespan.

### Active Directory Users and Computers (ADUC)

**ADUC**(`dsa.msc`) is the graphical administration tool for AD. Here you can:

- Create, edit, and delete user accounts
- Create and manage groups
- Join computers to OUs
- Reset passwords and unlock accounts
- Create and move OUs

TThe default `Users`container holds the built-in accounts:`Administrator`, `Guest`, and `KRBTGT`.
TIt is best practice to create your own OUs and move accounts there.

### Group Policy (GPO)

***Group Policy Objects (GPO)**are among the most powerful features in AD. A GPO is a set of settings that are
*automatically distributed to users and machines in an OU, domain, or site.

GPOs can control:

- Password policies (length, complexity, lifetime)
- Security settings (disable USB, lock screen after X minutes)
- Software distribution (install MSI packages automatically)
- Drive mappings (connect network drives at logon)
- Desktop settings (wallpaper, start menu)

*## Example — Deny Domain Admins logon on client machines:

1. Open Group Policy Management Console (GPMC)
2. Create a new GPO on OU=Computers
3. Navigate to: `Computer Configuration → Windows Settings → Security Settings → Local Policies → User Rights Assignment`
4. Edit `Deny log on locally`— add`Domain Admins`

GGPOs are inherited through the hierarchy (forest → domain → OU). A GPO linked to an OU overrides a GPO at the domain
Glevel.

### Global Catalog

***Global Catalog (GC)**is a distributed storage that contains a copy of all objects in the entire AD forest — not just
*the local domain. It is used for:

- Fast cross-domain searches (e.g., finding a user in another domain)
- Logon with UPNs (User Principal Name, e.g., `user@company.no`)
- Universal group memberships

AAt least one domain controller should have the Global Catalog role enabled. In a single-domain environment (like most
Aschools), this is automatic.

### Planning and Naming Standards

Good planning is essential before setting up AD. Key decisions:
--**Domain name**: Use an internal name (e.g., `company.local`) or a subdomain of an external domain
-(`internal.company.no`). Avoid `.local` in new setups — it can conflict with mDNS.
--**Naming standard for users**: A consistent naming convention (`firstname.lastname`, `f.lastname`, etc.) simplifies
-administration and scripting with [[powershell-grunnleggende-en]].
--**OU structure**: Design the OU hierarchy based on organizational structure or geographic location — not by roles.
-The OU structure should be documented in [[dokumentasjon-og-planlegging-en]].

### Joining Client Machines to the Domain

When a Windows client joins the domain:

1. The machine is created as an object in AD (under `Computers` or a specified OU)
2. The client begins receiving GPOs from the domain
3. Domain users can log on to the machine
4. The user's local profile is created on first logon

---

## Example / Lab

### Windows Server Project: 7-Day Classroom Lab (Konnekt AS)

>**Source:**Classroom notes (2ITA)
>
> In this course, students work on a realistic case project where they set up a complete Windows Server solution for the fictional company Konnekt AS. The project is structured over 7 working days:
>
>**Day 1 – Installation and IP Plan:**Students design an IP plan for the `10.0.10.0/24` network (DC01 fixed address, client W11-KLIENT01, gateway, and DHCP pool). Windows Server 2022/2025 is installed in VirtualBox with two network cards: one internal (Internal Network) and one bridged (for Windows Update). A snapshot is taken after clean installation — "Clean install - Before AD".
>
>**Day 2 – Domain and AD DS:**The AD DS role is installed and the server is promoted to domain controller for `konnekt.local`. The client machine is joined to the domain after DNS is pointed to DC01. The OU structure is created in ADUC based on the departmental structure.
>
>**Day 3 – Users, Groups, and File Server:**Test users are created with the naming standard `firstname.lastname`. Security groups per department (`SG_SalesMarketing_Members`, `SG_AllEmployees`) are created. A file server with the folder `C:\Data`and subfolders per department is set up — share permissions open to`Everyone`, NTFS permissions strict per security group.
>
>**Day 4 – Group Policy (GPO):**Network drives are mapped automatically via GPO (F: for shared, department drive per group with security filtering). Verification with `gpupdate /force`and`gpresult /r`.
>
>**Day 5 – Security Hardening:**Default Domain Policy is adjusted with password policy (min. 12 characters, complexity requirements). GPO for automatic screen lock after 600 seconds. Access to Control Panel is blocked for standard users.

### Creating an OU in ADUC

1. Open**Active Directory Users and Computers**(`dsa.msc`)
2. Right-click the domain name (e.g., `school.local`)
3. Select**New → Organizational Unit**
4. Name the OU, e.g., `Students`
5. Keep "Protect container from accidental deletion" checked
6. Click**OK**

### Creating a Domain Account in ADUC

1. Navigate to the OU where the user should be created (e.g., `Students`)
2. Right-click →**New → User**
3. Fill in: First name, Last name, User logon name (e.g., `student01@school.local`)
4. Set password and choose options (e.g., "User must change password at next logon")
5. Click**Finish**

### Creating a User with PowerShell (AD module)

```powershell

# Import the AD module (requires RSAT)

Import-Module ActiveDirectory

## Create a domain account

New-ADUser `
    -Name "Student Studentsen" `
    -GivenName "Student" `
    -Surname "Studentsen" `
    -SamAccountName "student01" `
    -UserPrincipalName "student01@school.local" `
    -Path "OU=Students,DC=school,DC=local" `
    -AccountPassword (ConvertTo-SecureString "P@ssw0rd1" -AsPlainText -Force) `
    -Enabled $true `
    -ChangePasswordAtLogon $true
```

### Creating a GPO and Linking It to an OU

```powershell

## Create a new GPO

New-GPO -Name "Student-policy"

## Link GPO to OU

New-GPLink -Name "Student-policy" -Target "OU=Students,DC=school,DC=local"

## Force policy update on client

gpupdate /force
```

---

## Study Guide

***Active Directory**is Microsoft's centralized directory service for Windows domains.
**It is organized in a hierarchy:**Forest → Tree → Domain → OU**. A**domain controller (DC)**is the server that runs the
*AD DS role and authenticates all logons.

Core components you need to know:
-**ADUC**(`dsa.msc`) — the graphical tool for creating and managing users, groups, computers, and OUs
--**GPO (Group Policy Object)**— automatic settings distributed to users and machines in an OU; inherited hierarchically,
-the closest OU wins
--**Kerberos**— the authentication protocol AD uses; the password is never sent over the network, only encrypted tickets
-(TGT)
-**LDAP**— the protocol programs use to search and update the AD directory
-**Global Catalog**— cross-domain search service; required for UPN logon

Important relationships:

- AD is dependent on**DNS**— the client must be able to resolve the domain controller via DNS to log on

-**FSMO roles**are specialized DC tasks that only one DC can hold at a time (e.g., PDC Emulator, RID Master)

- Access control is done via**security groups**linked to NTFS permissions — never assign access directly to individual users

Best practices:

- Always have at least two domain controllers (redundancy)
- Give administrators two accounts: a daily user account and a separate admin account
- Use GPOs to enforce password policies and security requirements automatically

---

## FAQ

*## What is the difference between AD DS and Azure AD?
AAD DS is the classic on-premises directory service that requires a Windows Server and domain controller in your own
AAnetwork. Azure AD (now called Microsoft Entra ID) is Microsoft's cloud-based directory service for Microsoft 365 and
Acloud services. They can be synchronized via Azure AD Connect.

*## Can a user log on to any machine in the domain?
YYes — that is the whole point of a domain. The domain user exists in AD, not on the individual machine.
YGPOs can still restrict which users can log on to specific machines.

*## What happens if the domain controller goes down?
WWith a single DC, no one will be able to log on with domain accounts. Users already logged on can continue working
Wlocally for a while (cached credentials). That is why you should always have at least two DCs.

*## What is the difference between Domain Admins and Enterprise Admins?
DDomain Admins have full control within one domain. Enterprise Admins have control over the entire AD forest (all
Ddomains). Enterprise Admins should only be used for forest-level operations.

*## Why should I use groups instead of assigning access directly to users?
WWith groups, you only need to change group membership when a user changes roles — not go through all resources manually.
WIt is easier to audit (who has access to what) and reduces the risk of errors.

*## What are FSMO roles and why are they important?
FFlexible Single Master Operation roles are specialized AD tasks that only one DC can perform at a time (e.g., issuing
FFnew SIDs). If the DC holding an FSMO role fails, certain operations can stop until the role is transferred to another
FDC.

*## Can I change the domain name after installation?
TTechnically yes, but it is complicated and risky. All GPOs, profiles, and service connections are tied to the domain
Tname. It is recommended to plan the domain name thoroughly before installation.

---

## Quiz

<details><summary>Question 1: What is a domain controller?</summary>

***Answer:**A domain controller is a server with Active Directory Domain Services (AD DS) installed.
*It authenticates all logons in the domain, stores the AD database, and distributes group policies.

</details>

<details><summary>Question 2: What is the difference between an OU and a security group?</summary>

***Answer:**An OU (Organizational Unit) is a logical container for organizing objects in AD and linking GPOs to.
**A security group gathers users to assign them common access rights and permissions.
*OUs are used for administration; groups are used for access control.

</details>

<details><summary>Question 3: What is a GPO and what can it be used for?</summary>

***Answer:**A Group Policy Object is a set of settings automatically distributed to users and machines in AD.
*It can control password policies, security settings, software distribution, network drives, and much more.

</details>

<details><summary>Question 4: Why should you have at least two domain controllers?</summary>

***Answer:**For redundancy. If one domain controller fails, the other can continue authenticating users without downtime.
*With only one DC, the entire domain will stop working in the event of a failure.

</details>

<details><summary>Question 5: What is LDAP?</summary>

***Answer:**Lightweight Directory Access Protocol — the protocol used to query and update directory data in Active
*Directory.

</details>

---

## Resources

- [Microsoft Learn: AD Default Accounts](<https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-default-user-accounts>)
- [Microsoft Learn: AD Security Groups](<https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups>)
- [Microsoft Learn: Active Directory Users and Computers](<https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc754217(v=ws.11>))
- [NDLA: Datalab with Windows Server and Generic Network](<https://ndla.no/nb/r/driftsstotte-im-itk-vg2/datalab-med-windows-server-og-generisk-nettverk/6fbbe0f727>)
- [Microsoft Learn: Logical Structure Design for AD DS](<https://learn.microsoft.com/nb-no/windows-server/identity/ad-ds/plan/active-directory-domain-services-logical-structure-design-guide>)
