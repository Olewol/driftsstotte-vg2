---
title: "File Systems"
emne: operativsystem
kompetansemaal:
  - km-04
kilder:
  - ndla
  - https://snl.no/filsystem
  - https://learn.microsoft.com/nb-no/windows-server/
  - https://documentation.ubuntu.com/server/
  - https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/
tags: []
flashcards: https://notebooklm.google.com/notebook/70aa7fff-78f3-4825-aeed-bc879a29770f
public: true
notebooklm: true
language: en
original: filsystem.md
---

## Introduction

A **file system** determines how data is stored and organized on a disk. For IT operations technicians, choosing a file system is directly linked to security and access control — only NTFS, for example, supports user-based permissions in Windows. Knowledge of file systems is necessary to manage rights, set up quotas, and understand the limitations of different storage media. NTFS permissions are closely related to [[bruker-og-tilgangsstyring]], and the Linux ext4 file system is covered in connection with [[linux-grunnleggende]]. File system choices are also relevant for [[backup-og-gjenoppretting]] since not all backup solutions support every file system.

---

## Theory

### NTFS (New Technology File System)

NTFS is the standard file system for Windows and Windows Server. It is the only option when you need file-level access control in Windows.

**Key features:**

- **Access Control Lists (ACL)**: Each file and folder has an ACL that lists which users and groups have which permissions. This is the engine behind Windows access control.
- **Permission inheritance**: Permissions are inherited by default from the parent folder. If you grant the `Students` group read access to `C:\Shared`, all subfolders automatically inherit this permission. Inheritance can be disabled per object.
- **Disk quotas**: Administrators can set limits on how much storage space individual users can use on a volume.
- **Journaling (transaction log)**: NTFS logs all file operations to a journal. If the system crashes mid-write, the journal can be used to restore consistency on the next boot.
- **Encryption and compression**: Supports EFS (Encrypting File System) and transparent compression.
- **Max volume**: Up to 8 petabytes with 2 MB cluster size (Windows Server 2019).

**NTFS permission levels:**

| Permission | What the user can do |
|---|---|
| Full control | Everything — including changing permissions and taking ownership |
| Modify | Read, write, delete files and subfolders |
| Read & execute | View contents and run programs |
| List folder contents | See filenames in the folder (not open files) |
| Read | Open and read files |
| Write | Create new files and folders, write to existing ones |

> **Note**: NTFS permissions apply both locally and over the network. When a user accesses a shared folder, NTFS permissions are combined with Share Permissions — the most restrictive combination wins.

### FAT32 (File Allocation Table 32)

FAT32 is an older file system supported by practically all operating systems and devices. It is primarily used on USB flash drives and memory cards.

**Characteristics:**
- **No access control** — anyone who can read the disk can read all files
- **Max file size: 4 GB − 1 byte** (4,294,967,295 bytes) — cannot store individual files of 4 GB or more (e.g., large ISO files or video files)
- **Max volume size: 2 TB**
- Supported by Windows, macOS, and Linux without extra drivers
- **Not** used for Windows Server volumes

### exFAT (Extended FAT)

exFAT is a successor to FAT32 designed for flash storage. It removes the 4 GB limit, supports files up to 16 exabytes, and works across platforms. No access control. Common on SD cards and USB drives that need to be shared between Windows and macOS.

### ext4 (Fourth Extended Filesystem)

ext4 is the standard file system on modern Linux distributions such as Ubuntu, Debian, and RHEL.

**Characteristics:**
- **Journaling**: Similar to NTFS — logs operations to ensure consistency after power failure.
- **Inodes**: Each file has an inode that stores metadata (owner, group, permissions, timestamps). The filename itself is a pointer to the inode.
- **Permission model**: rwx for owner, group, and others (see [[linux-grunnleggende]]).
- **POSIX ACL**: For more granular control, similar to NTFS ACL.
- Supports volume sizes up to 1 exabyte and files up to 16 TB.

### Comparison

| Feature | NTFS | FAT32 | exFAT | ext4 |
|---|---|---|---|---|
| OS | Windows | All | Windows/macOS | Linux |
| Max file size | 8 PB (volume) | 4 GB | 16 EB | 16 TB |
| Access control | Yes (ACL) | No | No | Yes (rwx + POSIX ACL) |
| Journaling | Yes | No | No | Yes |
| Encryption | Yes (EFS) | No | No | Via dm-crypt/LUKS |
| Quotas | Yes | No | No | Yes |
| Use case | Windows systems | USB/memory cards | USB/memory cards | Linux systems |

### NTFS vs. Share Permissions

A common point of confusion in IT support is the difference between **NTFS permissions** and **Share permissions**:

- **NTFS permissions** always apply — whether you access the file locally or over the network. They are granular (7 levels) and inherited.
- **Share permissions** only apply when you access a resource over the network (via `\\server\share`). They only have three levels: Read, Change, and Full Control.

When both are active, the **most restrictive combination** wins. Best practice is to set Share permissions to "Full Control" for `Everyone` and manage all access via NTFS permissions. This gives full control and avoids confusion.

### POSIX ACL in Linux

The standard rwx model in Linux gives three permission sets (owner, group, others). For more granular control — for example, giving a specific user access without changing group membership — **POSIX ACL** is used:

```bash
# Give user student02 read access to a folder
setfacl -m u:student02:r-x /shared/class2a

# View current ACL
getfacl /shared/class2a
```

POSIX ACL is equivalent to NTFS ACL but is used less frequently in practice. It is supported by ext4 and most modern Linux file systems.

---

## Example / Lab

### Setting NTFS Permissions in Windows

1. Right-click the folder → **Properties** → **Security** tab
2. Click **Edit** → **Add** → enter the user or group name
3. Choose the desired permission level and click **OK**

### Checking Inheritance

1. Properties → Security → **Advanced**
2. Under "Inherited from" you can see which permissions are inherited
3. To break inheritance: click **Disable inheritance** — choose whether existing inherited permissions should be converted to explicit permissions or removed

### View File System Type in PowerShell

```powershell
Get-Volume
```

Example output:
```
DriveLetter FriendlyName FileSystemType SizeRemaining    Size
----------- ------------ -------------- -------------    ----
C           Windows      NTFS            45.2 GB   237.4 GB
D           Data         NTFS           120.0 GB   500.0 GB
```

### Setting NTFS Permissions with icacls (Command Line)

`icacls` is the command-line tool for NTFS permissions in Windows:

```powershell
# View permissions for a folder
icacls C:\Data\Sales

# Grant group SG_Sales modify access recursively
icacls C:\Data\Sales /grant SG_Sales:(OI)(CI)M /T

# Remove access for a user
icacls C:\Data\Sales /remove student01

# (OI) = object inherit, (CI) = container inherit, M = Modify
```

---

## Study Guide

**File systems** determine how data is stored, organized, and protected on a disk. The choice of file system is critical for security, performance, and compatibility.

The four file systems you need to know:
- **NTFS** — standard for Windows and Windows Server; supports ACL, journaling, quotas, and encryption (EFS). The only option for Windows servers with access control.
- **FAT32** — universally compatible; used on USB and memory cards. No access control. Max file size 4 GB — a classic pitfall.
- **exFAT** — FAT32 without the 4 GB limit; used on larger USB devices and SD cards. No access control.
- **ext4** — standard Linux file system; supports journaling, inodes, rwx permissions, and POSIX ACL.

Critical to understand for NTFS:
- **ACL (Access Control List)** is the list of who has access to a file/folder and what they can do
- **Permission inheritance** — subfolders automatically inherit permissions from the parent; can be disabled per object
- **NTFS vs. Share Permissions**: both apply when accessing over the network — the most restrictive wins. Best practice: set Share to "Full Control"/"Everyone" and manage via NTFS.
- Permission levels from least to most: Read → List folder contents → Read & execute → Write → Modify → Full control

For Linux: the rwx model gives three permission sets (owner, group, others). POSIX ACL provides more granular control where standard rwx is insufficient.

---

## FAQ

**Can I move a disk with NTFS permissions to another Windows machine and keep the permissions?**
The permissions move with the disk, but they are stored as SIDs. If you connect the disk to a machine in a different domain or with different local users, the SIDs will no longer match any user — and you will typically not have access. You can take ownership with `takeown` and `icacls` to regain access.

**What is the difference between journaling and backup?**
Journaling protects against corruption when the system crashes mid-write — it is not a backup. The journal logs what was planned, so the file system can complete or roll back the operation at the next boot. Journaling does not replace [[backup-og-gjenoppretting]].

**Why can't I copy a 5 GB ISO file to a USB drive formatted as FAT32?**
FAT32 has an absolute limit of 4 GB − 1 byte per file. A 5 GB file exceeds this limit. Solution: format the USB drive as exFAT (retains compatibility) or NTFS (Windows only without extra drivers on Mac/Linux).

**What is an inode in Linux?**
An inode is a data structure that stores metadata about a file: owner, group, permissions, size, timestamps, and pointers to the disk blocks containing the actual data. The filename is not stored in the inode — it is a pointer from the directory to the inode. Two files can share the same inode (hard link).

**What happens to permissions on a file when I copy it vs. move it in NTFS?**
Copying to another folder: the file inherits the destination folder's permissions. Moving within the same volume: the file retains its explicit permissions. Moving to a different volume works like copying — the file inherits the destination folder's permissions.

**What does "the most restrictive combination" of NTFS and Share Permissions mean?**
Example: NTFS says "Read", Share says "Full Control". The user gets only read access because the NTFS permission is most restrictive. Another example: NTFS says "Full Control", Share says "Read" — the user gets only read access. The system takes the lowest common denominator.

---

## Quiz

<details><summary>Question 1: What is the biggest limitation of FAT32?</summary>

**Answer:** The maximum file size is 4 GB − 1 byte (4,294,967,295 bytes). Files of 4 GB or larger cannot be stored on a FAT32 volume.

</details>

<details><summary>Question 2: What is an ACL?</summary>

**Answer:** An Access Control List is a list attached to a file or folder that specifies which users and groups have which permissions. NTFS uses ACL for all access control.

</details>

<details><summary>Question 3: What happens if NTFS permissions say "Read" but Share permissions say "Full Control"?</summary>

**Answer:** The user gets only read access. When NTFS and Share permissions are combined, the most restrictive permission always applies.

</details>

<details><summary>Question 4: What is journaling and why is it important?</summary>

**Answer:** Journaling is a mechanism where the file system logs all planned operations before they are executed. If the system crashes mid-operation, the journal can be used to restore file system consistency without data loss.

</details>

<details><summary>Question 5: Which file system is standard on Ubuntu Linux?</summary>

**Answer:** ext4 (Fourth Extended Filesystem).

</details>

---

## Flashcards

NTFS :: Standard Windows file system with support for ACL, quotas, journaling, and encryption
ACL :: Access Control List — list of users/groups and their permissions on a file or folder
Permission inheritance :: Mechanism in NTFS where subfolders automatically adopt the permissions of the parent folder
FAT32 :: Older file system without access control; max file size 4 GB − 1 byte (4,294,967,295 bytes)
exFAT :: Modern FAT-based file system without the 4 GB limit; used on USB/SD
ext4 :: Standard Linux file system with journaling, inodes, and rwx permission model
Inode :: Data structure in Linux file systems that stores metadata about a file (owner, permissions, timestamp)
Journaling :: File system transaction log that ensures consistency after a system crash
Disk quota :: Limit on how much storage space a user can use on a volume
Full control :: Highest NTFS permission level — includes the right to change permissions and take ownership
POSIX ACL :: Extended access control in Linux beyond standard rwx; provides per-user and per-group permissions with `setfacl`/`getfacl`
icacls :: Windows command-line tool for viewing and changing NTFS permissions
Share Permissions :: Permissions that only apply when accessing a shared resource over the network; combined with NTFS permissions (most restrictive wins)
EFS :: Encrypting File System — NTFS feature for transparent file encryption tied to the user's certificate

---

## Resources

- [Microsoft Learn: NTFS Overview](https://learn.microsoft.com/en-us/windows-server/storage/file-server/ntfs-overview)
- [Microsoft Learn: Configuring Share and NTFS Permissions](https://learn.microsoft.com/en-us/iis/web-hosting/configuring-servers-in-the-windows-web-platform/configuring-share-and-ntfs-permissions)
- [Ubuntu Community Wiki: FilePermissions](https://help.ubuntu.com/community/FilePermissions)
- [Store Norske Leksikon: File system](https://snl.no/filsystem)
