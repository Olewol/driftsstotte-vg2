---
title: "User and Access Management"
emne: operativsystem
kompetansemaal:
  - km-04
kilder:
  - ndla
  - https://learn.microsoft.com/nb-no/windows-server/identity/ad-ds/active-directory-domain-services
  - https://learn.microsoft.com/nb-no/windows-server/
  - https://documentation.ubuntu.com/server/
  - https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/
tags: []
flashcards: https://notebooklm.google.com/notebook/70aa7fff-78f3-4825-aeed-bc879a29770f
public: true
notebooklm: true
language: en
original: bruker-og-tilgangsstyring.md
---

## Introduction

User and access management is the core of km-04 and one of the most important tasks an IT operations technician performs. The goal is to ensure that **the right people have access to the right resources — and nothing more**. This is called the principle of least privilege.

This article covers Windows user administration (local and in a domain), security groups, access control, and the equivalent tools in Linux. User administration in domain environments requires knowledge of [[active-directory]]. For Linux commands, see [[linux-grunnleggende]], and for automating user creation, see [[powershell-grunnleggende]].

---

## Theory

### Local Accounts vs. Domain Accounts

| Feature | Local Account | Domain Account |
|---|---|---|
| Stored in | Local SAM database | Active Directory (DC) |
| Valid on | This machine only | All machines in the domain |
| Managed via | `lusrmgr.msc` / PowerShell | ADUC / PowerShell |
| Used for | Standalone machines | Enterprise environments with AD |
| Example | `.\\Administrator` | `SCHOOL\\Student01` |

### Built-in Default Accounts

**Administrator (SID …-500)**
The built-in administrator account created during Windows installation. Cannot be deleted. Has full control over the system. Best practice in production: rename the account and disable it — instead, create a named admin account.

**Guest (SID …-501)**
A restricted guest account. Disabled by default. Should remain disabled in all production environments.

**KRBTGT (domain)**
Internal domain account used by the Kerberos authentication service. Should never be used for interactive logon. The password should be rotated periodically as a security measure.

### Account Settings in Windows

When you create or edit a user account, you can control:

- **User must change password at next logon** — forces new employees to set their own password
- **User cannot change password** — for service accounts
- **Password never expires** — for service accounts (not for regular users)
- **Account is disabled** — used when someone leaves instead of deletion (preserves data and group membership)
- **Account is locked out** — set automatically after too many wrong passwords (can be unlocked manually)

### SID — Security Identifier

Every user account and group in Windows is assigned a unique **SID** (Security Identifier) at creation. The SID is what the operating system actually uses internally — not the username. This means:

- If you delete and recreate an account with the same name, it gets a new SID and loses all previous permissions
- Permissions in ACLs are stored as SIDs, not names

### The Principle of Least Privilege

Users and processes should only have the permissions that are absolutely necessary to perform their job. In practice:

- Don't give everyone Domain Admins
- Separate daily user accounts from admin accounts (administrators have two accounts)
- Remove permissions when they are no longer needed
- Use groups for access management — never assign permissions directly to individual users

### UAC — User Account Control

UAC is a security mechanism in Windows that prevents programs from running with administrative privileges without the user's explicit approval. Even if you are logged in as an administrator, programs run with standard user rights until UAC approves an elevation.

When a program requests administrator privileges, the UAC dialog is shown. A standard user must enter an admin password; an administrator simply clicks "Yes".

### Security Groups in Active Directory

Groups let you assign permissions to many users at once. Best practice: **always assign permissions to groups, never to individual users**.

**Group scope:**

| Scope | Can contain | Can be used for permissions in |
|---|---|---|
| Domain Local | Users and groups from all domains | Own domain only |
| Global | Users and groups from own domain | All domains in the forest |
| Universal | Users and groups from all domains | All domains in the forest |

**Built-in groups (examples):**

| Group | Rights |
|---|---|
| Domain Admins | Full administrative access to the domain |
| Enterprise Admins | Full access to the entire AD forest |
| Domain Users | Default for all domain users |
| Administrators (local) | Full local administrative access |
| Guests | Very limited access |

### The AAA Principle

Access control is built on three steps:

1. **Authentication** — Who are you? (username + password, MFA, smart card)
2. **Authorization** — What are you allowed to do? (groups, ACLs, rights)
3. **Accounting/Auditing** — What have you done? (event logs, security auditing)

### RBAC — Role-Based Access Control

**Role-based access control (RBAC)** is an extension of the principle of least privilege. Instead of assigning permissions directly to individual users, permissions are linked to **roles** (e.g., "Accountant", "IT Administrator", "Student"). Users are then assigned roles.

Benefits of RBAC:
- Easier to manage with large numbers of users
- Easier to audit ("who has role X?" is one question, not many)
- Lower risk of misconfiguration — new users inherit the role automatically

In Windows AD, RBAC is practically implemented using security groups: one group per role, permissions are assigned to the group.

### Windows and Linux Integration

In larger environments, it is desirable for Linux clients to be able to log on against the Windows domain. This is typically done with:
- **SSSD** (System Security Services Daemon) — lets Linux authenticate against AD
- **Samba/Winbind** — alternative solution for domain integration

This is advanced material, but the concept is important: one central user system (AD) for both Windows and Linux.

---

## Example / Lab

### Managing Local Users with PowerShell

**Create a new local user:**
```powershell
New-LocalUser -Name "Student01" -Password (ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force) -FullName "Student Studentsen" -Description "Test account"
```

**Add the user to a group:**
```powershell
Add-LocalGroupMember -Group "Users" -Member "Student01"
```

**List all local users:**
```powershell
Get-LocalUser
```

**Disable an account:**
```powershell
Disable-LocalUser -Name "Student01"
```

**Remove user from group:**
```powershell
Remove-LocalGroupMember -Group "Users" -Member "Student01"
```

### Linux Equivalents

**Create user:**
```bash
sudo useradd -m -s /bin/bash student01
```
The flags `-m` create a home directory and `-s` sets the default shell.

**Set password:**
```bash
sudo passwd student01
```

**Add user to a group (e.g., sudo):**
```bash
sudo usermod -aG sudo student01
```

**View user's groups:**
```bash
groups student01
id student01
```

**Disable account (lock password):**
```bash
sudo passwd -l student01
```

### Structure of /etc/passwd

Each line in `/etc/passwd` has seven fields separated by colons:
```
username:x:UID:GID:GECOS:home_directory:shell
student01:x:1001:1001:Student Studentsen:/home/student01:/bin/bash
```

- `x` means the password is stored in `/etc/shadow` (encrypted)
- UID 0 = root, UID 1–999 = system users, UID 1000+ = regular users

### Structure of /etc/group

```
groupname:x:GID:members
sudo:x:27:student01,admin
```

---

## Study Guide

**User and access management** is about ensuring the right people have access to the right resources. The core principle is **least privilege**: never give more access than necessary.

Two account types to distinguish:
- **Local accounts** are stored in the machine's SAM database and apply only locally
- **Domain accounts** are stored in Active Directory and work on all domain-joined machines

Important Windows concepts:
- **SID** — Windows does not use usernames internally, but SIDs. If you delete and recreate an account with the same name, it loses all permissions
- **UAC** — prevents programs from escalating to admin rights without explicit confirmation
- **Security groups** — always assign permissions to groups, never to individual users
- **Group scope** — domain local groups for local permissions, global groups to collect users, universal groups for forest-level access

The AAA framework summarizes access control: **Authentication** (who are you?), **Authorization** (what are you allowed to do?), **Accounting/Auditing** (what have you done?).

Linux equivalents:
- Users are created with `useradd`, modified with `usermod`, deleted with `userdel`
- Groups are managed with `groupadd` and `gpasswd`
- `/etc/passwd` contains user info; `/etc/shadow` contains encrypted passwords (only root can read)
- Access rights are controlled by the rwx model — see [[linux-grunnleggende]] for details

---

## FAQ

**Why should you not use the Administrator account for daily work?**
The Administrator account (SID ...-500) has unlimited access and cannot be permanently disabled. Daily use increases the risk that malicious software or human error causes permanent damage. Use a named user account with limited access, and a separate admin account only when necessary.

**What happens to permissions if I delete and recreate a user with the same name?**
The new account receives a new SID. All NTFS permissions, group memberships, and resource connections are tied to the old SID and must be set up again. Therefore, use deactivation rather than deletion when an employee leaves.

**What is the difference between global, domain local, and universal groups?**
A global group collects users from the same domain and can be used for permissions in all domains in the forest. A domain local group is used for permissions locally and can contain users from all domains. A universal group can contain users from the entire forest and is used in forest-level scenarios.

**What does `-aG` do in `usermod -aG sudo student01`?**
`-a` (append) adds the user to the group without removing existing group memberships. Without `-a`, the command would replace all existing group memberships with only `sudo`.

**What is RBAC and why is it used?**
Role-based access control links permissions to roles rather than individuals. It simplifies administration: new employees are assigned a role and automatically get the correct access. It also reduces errors and makes auditing easier.

**What is the difference between authentication and authorization?**
Authentication verifies your identity (you are who you claim to be). Authorization determines what you are allowed to do after you are authenticated. A system can authenticate you without giving you access to anything at all.

---

## Quiz

<details><summary>Question 1: What is the difference between a local account and a domain account?</summary>

**Answer:** A local account is stored in the machine's SAM database and is only valid on that machine. A domain account is stored in Active Directory and can be used to log on to all machines in the domain.

</details>

<details><summary>Question 2: What is a SID and why is it important?</summary>

**Answer:** SID (Security Identifier) is a unique identifier Windows assigns to each account. The operating system uses SID internally instead of the username. If an account is deleted and recreated with the same name, it gets a new SID and loses all previous permissions.

</details>

<details><summary>Question 3: What does the principle of least privilege mean?</summary>

**Answer:** Users and processes should only have the permissions that are absolutely necessary to perform their job — no more. This limits the damage scope in the event of compromised accounts.

</details>

<details><summary>Question 4: What is UAC and what does it protect against?</summary>

**Answer:** User Account Control is a security mechanism that prevents programs from running with administrative privileges without explicit approval. It protects against malicious software silently gaining admin rights in the background, even when the user is logged in as an administrator.

</details>

<details><summary>Question 5: Which PowerShell command adds user "Student01" to the group "Users"?</summary>

**Answer:** `Add-LocalGroupMember -Group "Users" -Member "Student01"`

</details>

<details><summary>Question 6: What does the command `usermod -aG sudo student01` do in Linux?</summary>

**Answer:** It adds the user `student01` to the `sudo` group without removing the user from other groups (`-a` = append, `-G` = supplementary groups). This gives the user the ability to run commands with root privileges via `sudo`.

</details>

---

## Flashcards

Local account :: User account stored in the machine's SAM database, valid only on that machine
Domain account :: User account stored in Active Directory, valid on all machines in the domain
SID :: Security Identifier — unique numeric identifier Windows assigns to each account and group
Principle of least privilege :: Users should only have the permissions they need for their job
UAC :: User Account Control — Windows mechanism that requires explicit approval for administrative operations
Domain Admins :: Built-in AD group with full administrative access to the domain
Security group :: AD object that gathers users for shared access management
Domain local group :: Group that can be used for permissions only in its own domain
Global group :: Group from the same domain that can be used for permissions in all domains in the forest
AAA :: Authentication, Authorization, and Accounting — the core principles of access control
useradd :: Linux command to create a new user account
usermod -aG :: Linux command to add a user to a supplementary group without removing existing group memberships
/etc/shadow :: Linux file that stores encrypted passwords (only root can read)
RBAC :: Role-based access control — permissions are linked to roles, not individuals
Sudoers :: Configuration file in Linux (`/etc/sudoers`) that defines who can run commands with root privileges
SSSD :: System Security Services Daemon — lets Linux clients authenticate against Active Directory

---

## Resources

- [Microsoft Learn: AD Default Accounts](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-default-user-accounts)
- [Microsoft Learn: AD Security Groups](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups)
- [Microsoft Learn: Managing User Accounts in Windows Server](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage-user-accounts-in-windows-server)
- [Ubuntu Server: User Management](https://documentation.ubuntu.com/server/how-to/security/user-management/)
- [Microsoft Learn: Active Directory Domain Services](https://learn.microsoft.com/nb-no/windows-server/identity/ad-ds/active-directory-domain-services)
