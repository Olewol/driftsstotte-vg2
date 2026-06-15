---
title: "Linux – Fundamentals"
emne: operativsystem
kompetansemaal:

  - km-04

kilder:

  - ndla
  - <https://documentation.ubuntu.com/server/how-to/security/user-management/>
  - <https://learn.microsoft.com/nb-no/windows-server/>
  - <https://documentation.ubuntu.com/server/>
  - <https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/>

video: <https://www.youtube.com/watch?v=pkZEKIXe3u4>
tags: []
flashcards: <https://notebooklm.google.com/notebook/70aa7fff-78f3-4825-aeed-bc879a29770f>
public: true
notebooklm: true
language: en
original: linux-grunnleggende.md
---

## Introduction

LLinux is an open-source operating system widely used on servers, cloud platforms, and network devices.
LLFor IT operations technicians, basic Linux knowledge is essential — much of the infrastructure in professional
Lenvironments runs on Linux.

TThis article covers the Linux file structure, the file permission model (rwx), user administration, and the most
TTcommonly used commands. Comparisons with Windows equivalents are included where helpful.
TTThe ext4 file system that Linux typically uses is described in [[filsystem-en]], and Linux user administration is
TTclosely related to [[bruker-og-tilgangsstyring-en]]. For advanced scripting tasks in the Linux terminal, see
T[[bash-grunnleggende-en]].

---

## Theory

### Linux File Structure

LLinux has a single file tree rooted at `/`— there is no`C:\` drive like in Windows.
LEverything is mounted into this tree.

|| Directory | Contents and purpose |
|| --- | --- |
|| `/` | The root directory — the top of the entire file system |
|| `/etc` | Configuration files for the system and services (e.g.,`/etc/passwd`, `/etc/ssh/sshd_config`) |
|| `/home` | Home directories for regular users (e.g.,`/home/student01`) |
|| `/root` | The home directory of the root user (not under`/home`) |
|| `/var` | Variable data — log files (`/var/log`), spool files, databases |
|| `/bin` | Basic system commands available to all users (e.g.,`ls`, `cp`) |
|| `/usr/bin` | User programs and commands installed by the package manager |
|| `/sbin` | System administration commands (requires root, e.g.,`fdisk`, `iptables`) |
|| `/tmp` | Temporary files — cleared on reboot |
|| `/dev` | Device files (e.g.,`/dev/sda` for hard disk) |
|| `/proc` | Virtual file system with information about running processes |
|| `/mnt` | Temporary mount points for external drives |

### The rwx Permission Model

Each file and directory in Linux has three sets of permissions for three categories:

*## Categories:
-**User (u)**— the user who owns the file
-**Group (g)**— the group associated with the file
-**Others (o)**— all other users

*## Permissions:
|| Symbol | Number | File | Directory |
|| --- | --- | --- | --- |
|| r (read) | 4 | Read file contents | List files in the directory |
|| w (write) | 2 | Modify/delete the file | Create and delete files in the directory |
|| x (execute) | 1 | Run the file as a program | Enter the directory (`cd`) |

*## Interpreting `ls -l` output:

```bash
-rwxr-xr-- 1 student01 teachers 4096 Mar 20 10:00 script.sh
```

- `-`→ regular file (directory shown as`d`)
- `rwx` → owner (student01) has read, write, and execute
- `r-x` → group (teachers) has read and execute, not write
- `r--` → others have only read

*## Octal notation:
Each permission set is summed: r=4, w=2, x=1

```bash
rwxr-xr-x = 7  5  5 → chmod 755
rw-r--r-- = 6  4  4 → chmod 644
rwx------ = 7  0  0 → chmod 700
```

### chmod — Change Permissions

*## Octal notation:

```bash
chmod 755 directory/       # owner: rwx, group: r-x, others: r-x
chmod 644 document.txt     # owner: rw-, group: r--, others: r--
chmod 700 private/         # only owner has access
```

*## Symbolic notation:

```bash
chmod u+x script.sh    # add execute permission for owner
chmod g-w file.txt     # remove write permission for group
chmod o-r private.txt  # remove read permission for others
chmod a+r public       # all (everyone) gets read permission
```

*## Recursively (all files in directory):

```bash
chmod -R 755 /var/www/
```

### chown — Change Owner and Group

```bash
chown student01 file.txt              # change owner to student01
chown student01:teachers file.txt     # change owner AND group
chown :teachers file.txt              # change only group
chown -R student01:teachers /home/shared # recursively
```

Equivalent: `chgrp teachers file.txt` changes only the group.

### Sticky Bit

TThe sticky bit on a directory prevents users from deleting files they do not own, even if they have write permission to
Tthe directory. Typically used on `/tmp`.

```bash
chmod +t /shared/         # set sticky bit
ls -ld /shared/           # shown as 't' at the end: drwxrwxrwt
```

### sudo and root

***Root user**(UID 0) is the all-powerful superuser in Linux — equivalent to `Administrator` in Windows, but without any
*UAC-like restriction. Root can do anything.

**sudo**(Superuser Do) lets regular users run individual commands with root privileges:

```bash
sudo apt update           # run as root
sudo -i                   # open root shell (be careful)
sudo -u student01 command # run as another user
```

Who can use sudo is controlled by `/etc/sudoers`. Always edit with `visudo` (checks syntax before saving):

```bash
sudo visudo
```

On Ubuntu, users are added to the `sudo` group to grant them sudo access:

```bash
sudo usermod -aG sudo student01
```

### User Administration

*## Create user:

```bash
sudo useradd -m -s /bin/bash student01

# -m: create home directory

## -s: set default shell
```

More complete:

```bash
sudo useradd -m -s /bin/bash -c "Student Studentsen" -G sudo student01
```

*## Set/change password:

```bash
sudo passwd student01
```

*## Modify user settings:

```bash
sudo usermod -aG teachers student01    # add to group
sudo usermod -s /bin/sh student01      # change shell
sudo usermod -L student01              # lock account
sudo usermod -U student01              # unlock account
```

*## Delete user:

```bash
sudo userdel student01               # delete account
sudo userdel -r student01            # delete account and home directory
```

*## Group commands:

```bash
sudo groupadd teachers              # create group
sudo gpasswd -a student01 teachers  # add user to group
sudo gpasswd -d student01 teachers  # remove user from group
```

### /etc/passwd and /etc/group

**/etc/passwd**— one line per user:

```bash
username:password:UID:GID:comment:home_directory:shell
student01:x:1001:1001:Student Studentsen:/home/student01:/bin/bash
root:x:0:0:root:/root:/bin/bash
```

- The password is `x`— the actual hash is stored in`/etc/shadow`
- UID 0 = root, 1–999 = system users, 1000+ = regular users

**/etc/group**— one line per group:

```bash
groupname:password:GID:members
sudo:x:27:student01,admin
teachers:x:1002:student01,student02
```

### Useful Commands for Access and Identity

```bash
whoami                   # show logged-in user
id                       # show UID, GID, and all groups
id student01             # show for a specific user
groups                   # list groups for the logged-in user
groups student01         # list groups for a specific user
ls -l file.txt           # show permissions, owner, and group
ls -ld directory/        # show permissions for the directory itself
stat file.txt            # detailed information including inode
```

### SUID and SGID — Special Permission Bits

In addition to the sticky bit, there are two other special permission bits you should know:

***SUID (Set User ID)**— when SUID is set on an executable file, the program runs with**the file owner's**privileges, not
**the logged-in user's. Used, for example, on the `passwd`command so regular users can change their own password (which
*requires writing to`/etc/shadow`).

```bash
ls -l /usr/bin/passwd

## -rwsr-xr-x  → 's' in the owner position means SUID

chmod u+s program       # set SUID
```

***SGID (Set Group ID)**— on a file: the program runs with the group's privileges. On a directory: new files and
*subdirectories inherit the directory's group instead of the creator's primary group. Useful for shared workspaces.

```bash
chmod g+s /shared/project   # set SGID on directory
ls -ld /shared/project

## drwxrwsr-x  → 's' in the group position means SGID
```

### System Logging in Linux

Linux logs system events to `/var/log/`. Important log files:

|| Log file | Contents |
|| --- | --- |
|| `/var/log/syslog` | General system messages (Ubuntu/Debian) |
|| `/var/log/auth.log` | Authentication events, sudo usage, SSH logins |
|| `/var/log/kern.log` | Kernel messages |
|| `/var/log/dpkg.log` | Package installation and updates |

Modern Linux uses**journald**(systemd) for logging. Queries via `journalctl`:

```bash
journalctl -u ssh          # logs for the SSH service
journalctl -n 50           # last 50 lines
journalctl --since today   # logs from today
journalctl -f              # follow logs live (like tail -f)
```

---

## Example / Lab

### Lab: Create User and Set Permissions

```bash

## 1. Create user with home directory

sudo useradd -m -s /bin/bash student01

## 2. Set password

sudo passwd student01

## 3. Create group

sudo groupadd class2a

## 4. Add user to group

sudo usermod -aG class2a student01

## 5. Verify

id student01

## 6. Create shared folder

sudo mkdir /shared/class2a
sudo chown :class2a /shared/class2a
sudo chmod 770 /shared/class2a

## Only owner and class2a group have access

## 7. Enable sticky bit (users cannot delete each other's files)

sudo chmod +t /shared/class2a
```

### Comparison: Windows vs. Linux Access Control

|| Task | Windows | Linux |
|| --- | --- | --- |
|| Create user | `New-LocalUser` | `useradd` |
|| Set password | (part of New-LocalUser) | `passwd` |
|| Add to group | `Add-LocalGroupMember` | `usermod -aG` |
|| View user info | `Get-LocalUser` | `id`, `cat /etc/passwd` |
|| Change permissions | NTFS Properties / `icacls` | `chmod` |
|| Change owner | `takeown` | `chown` |
|| Admin rights | UAC / Administrator | `sudo` / root |

---

## Study Guide

***Linux**is an open-source operating system based on Unix. It is dominant on servers, in the cloud, and on network
*devices. As an IT operations technician, you use Linux via the terminal.

**File structure**is a single tree rooted at `/`. Important directories:

- `/etc`— configuration files (including`/etc/passwd`, `/etc/shadow`, `/etc/sudoers`)
- `/home` — home directories for regular users
- `/var/log` — log files from the system and services
- `/tmp` — temporary files, cleared on reboot
- `/bin`and`/usr/bin` — commands and programs

**Permission model (rwx)**gives three sets of three permissions:
-**r**(read=4),**w**(write=2),**x**(execute=1)

- For**owner**,**group**, and**others**
- Octal sum: `rwx = 7`, `r-x = 5`, `rw- = 6`
- Common patterns: `755`(directories/programs),`644`(regular files),`700` (private files)

*## User administration:

- `useradd -m -s /bin/bash student01` — create user
- `passwd student01` — set password
- `usermod -aG sudo student01` — grant sudo access
- `userdel -r student01` — delete user and home directory

***Sudo and root**: Root (UID 0) is all-powerful. Never log in as root directly — use `sudo`for individual administrative
*commands.`/etc/sudoers`controls who can use sudo; always edit with`visudo`.

SSpecial permission bits:**sticky bit**(prevents deleting others' files in shared directories),**SUID**(program runs with
Sthe file owner's privileges),**SGID**(files inherit the directory's group).

---

## FAQ

*## What is the difference between `useradd`and`adduser`?
``useradd`is the low-level system tool available on all Linux distributions.`adduser`is a more user-friendly script
``(available on Debian/Ubuntu) that asks questions interactively and sets up the home directory and password
`automatically. In scripts, use`useradd`.

*## Why do system users start at UID 1–999 and regular users at UID 1000?
SSystem users (UID 1–999) are accounts created for services and processes, not for people logging in (e.g., `www-data`for
SSApache,`postgres` for the database service). They are separated from regular users for security and administrative
Spurposes.

*## What happens if I forget `-a`in`usermod -aG`?
WWithout `-a`, `usermod -G sudo student01`will replace all existing group memberships with only`sudo`.
WThe user loses all other groups they were a member of. Always use `-aG` to add.

*## Can I set a password for root and log in directly?
TTechnically yes, but it is strongly not recommended in production environments. SSH should be configured to deny root
Tlogin (`PermitRootLogin no`in`/etc/ssh/sshd_config`). Always use sudo from a regular user account.

*## What does 'd' mean at the beginning of `ls -l` output?
TThe first character indicates the file type: `-`= regular file,`d`= directory,`l`= symbolic link,`b`= block device,`c` =
Tcharacter device.

*## What is the difference between `/bin`and`/usr/bin`?
``/bin`contains basic system commands that must be available early in the boot process and during system recovery
``(e.g.,`ls`, `cp`, `bash`). `/usr/bin`contains programs installed by the package manager.
`On modern Linux,`/bin`is often a symbolic link to`/usr/bin`.

*## What is `journalctl` and why is it better than reading log files directly?
``journalctl`is the command for reading logs from systemd's journald. Benefits: structured logs with metadata, easy
``filtering by service and time range, binary format that is more efficient than text files.
`Older systems still use text files in`/var/log/`.

---

## Quiz

<details><summary>Question 1: What does the permission code `chmod 755` mean?</summary>

***Answer:**Owner gets rwx (7 = 4+2+1), group gets r-x (5 = 4+0+1), others get r-x (5 = 4+0+1).
*The owner can read, write, and execute; group and others can read and execute, but not write.

</details>

<details><summary>Question 2: What is stored in /etc/shadow?</summary>

***Answer:**Encrypted (hashed) passwords for all users. The file is only readable by root, unlike `/etc/passwd` which is
*readable by everyone.

</details>

<details><summary>Question 3: What is the difference between `useradd`and`usermod`?</summary>

***Answer:**`useradd`creates a new user account.`usermod` modifies settings on an existing account (e.g., adds group
*memberships, changes shell, or locks the account).

</details>

<details><summary>Question 4: What does the sticky bit do on a directory?</summary>

***Answer:**The sticky bit prevents users from deleting files in the directory that they do not own, even if they have
*write permission to the directory. Typically used on `/tmp` and shared directories.

</details>

<details><summary>Question 5: What is the /etc directory used for?</summary>

***Answer:**`/etc`contains configuration files for the system and installed services, including`/etc/passwd`(user
*accounts),`/etc/group`(groups),`/etc/hosts`(hostnames), and`/etc/ssh/sshd_config` (SSH configuration).

</details>

---

## Resources

- [Ubuntu Community Wiki: FilePermissions](<https://help.ubuntu.com/community/FilePermissions>)
- [Ubuntu Community Wiki: POSIX ACL](<https://help.ubuntu.com/community/FilePermissionsACLs>)
- [Ubuntu Server: User Management](<https://documentation.ubuntu.com/server/how-to/security/user-management/>)
