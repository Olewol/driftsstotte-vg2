---
title: "Automation – Scheduled Tasks and IaC"
emne: skripting
kompetansemaal:

  - km-09

kilder:

  - ndla
  - <https://learn.microsoft.com/nb-no/powershell/scripting/overview>
  - <https://learn.microsoft.com/nb-no/powershell/scripting/>
  - <https://learnxinyminutes.com/docs/bash/>
  - <https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/>

video: <https://www.youtube.com/watch?v=j9MAMgyNpAU>
tags: []
flashcards: <https://notebooklm.google.com/notebook/15678f10-b24e-462c-b837-076df87bd4b7>
public: true
notebooklm: true
language: en
original: automatisering.md
---

## Introduction

WWriting a script is only half the job. The other half is making sure the script actually runs — at the right time, on
Wthe right machine, without anyone having to think about it. This is where**automation**truly shows its value.

IIn this article, we learn two basic mechanisms for scheduling and running scripts automatically:**Windows Task
IIScheduler**for Windows and**cron**for Linux. We also look at**Infrastructure as Code (IaC)**— the next step beyond
Iscripting, where entire IT infrastructures are described in code.

AAutomation builds directly on the skills from [[bash-grunnleggende-en|Bash basics]] and
AA[[powershell-grunnleggende-en|PowerShell basics]]. In larger operations environments, automation is closely linked to
AA[[backup-og-gjenoppretting-en|backup and recovery]], [[serverroller-en|server roles]], and [[skytjenester-en|cloud
Aservices]].

---

## Theory

### What is IT Automation?

AAutomation in IT means replacing manual, repetitive tasks with systems that perform them on their own.
AAA system administrator who manually logs into 50 servers to install updates spends hours.
AAA script that runs automatically via Task Scheduler or cron does the same thing in minutes — without human
Aintervention.

Typical tasks automated in operations:

-**Backup**— Copy data to secure storage every night.
-**Updates**— Install security updates weekly.
-**Log rotation**— Archive and delete old log files.
-**Monitoring**— Check service status every 5 minutes and send alerts on failure.
-**Reporting**— Generate and send user lists or system status reports.

Automation reduces human error, frees up time, and makes operations more predictable.

---

### Windows Task Scheduler

Task Scheduler is Windows' built-in system for scheduling and running programs and scripts automatically.

#### Concepts

A**task**in Task Scheduler consists of three parts:

1.**Trigger**— When should the task run? (time, system event, logon, etc.)
2.**Action**— What should run? (program, script, email)
3.**Conditions**— Additional requirements (e.g., "only if the computer is on AC power")

#### GUI — Create a Task Graphically

1. Open**Task Scheduler**(search in the Start menu).
2. Click**Create Basic Task**in the right panel.
3. Give the task a name and description.
4. Choose trigger:**Daily**, set the time to `02:00`.
5. Choose action:**Start a program**.
6. Browse to your script, e.g., `C:\Scripts\backup.ps1`.
   - Program: `powershell.exe`
   - Arguments: `-NonInteractive -File "C:\Scripts\backup.ps1"`
7.

#### Command Line with `schtasks`

`schtasks` is the command-line tool for Task Scheduler. It is useful for automated setup and scripting of tasks.

Basic commands:

|| Command | Description |
|| --- | --- |
|| `schtasks /create` | Create a new task |
|| `schtasks /query` | List tasks |
|| `schtasks /run` | Run a task immediately |
|| `schtasks /delete` | Delete a task |
|| `schtasks /change` | Modify an existing task |

*## Example — create a daily backup task at 02:00:

```cmd
schtasks /create ^
  /tn "DailyBackup" ^
  /tr "powershell.exe -NonInteractive -File C:\Scripts\backup.ps1" ^
  /sc DAILY ^
  /st 02:00 ^
  /ru SYSTEM ^
  /f
```

*## Parameter explanation:

|| Parameter | Explanation |
|| --- | --- |
|| `/tn "DailyBackup"` | Task Name — name of the task |
|| `/tr "powershell.exe ..."` | Task Run — the program/script to execute |
|| `/sc DAILY` | Schedule — run frequency (DAILY, WEEKLY, MONTHLY, ONCE, etc.) |
|| `/st 02:00` | Start Time — time of execution |
|| `/ru SYSTEM` | Run User — user account under which the task runs |
|| `/f` | Force — overwrite without confirmation if the task already exists |

*## Verify the task:

```cmd
schtasks /query /tn "DailyBackup" /fo LIST /v
```

*## Run the task manually for testing:

```cmd
schtasks /run /tn "DailyBackup"
```

---

### Linux Cron

***Cron**is the Linux daemon for running scheduled tasks. Tasks are defined in a**crontab**file (cron table) with a
*specific syntax.

#### Crontab Syntax

A crontab line consists of five time fields followed by the command:

```bash

# min  hour  day-of-month  month  day-of-week  command

  *****/path/to/script.sh
```

*## The fields:

|| Field | Value range | Description |
|| --- | --- | --- |
|| Minute | 0–59 | Minute of the hour |
|| Hour | 0–23 | Hour of the day (24-hour) |
|| Day of month | 1–31 | Day of the month |
|| Month | 1–12 | Month |
|| Day of week | 0–7 | Day of the week (0 and 7 are both Sunday) |

*## Special values:

|| Value | Meaning |
|| --- | --- |
|| `*` | All valid values |
|| `*/2` | Every two (e.g., every two minutes) |
|| `1,3,5` | Specific values (Monday, Wednesday, Friday) |
|| `1-5` | Range (Monday to Friday) |

*## Special strings (shortcuts):

|| String | Equivalent |
|| --- | --- |
|| `@reboot` | At system startup |
|| `@daily` | `0 0***` — midnight every day |
|| `@weekly` | `0 0**0` — Sunday midnight |
|| `@monthly` | `0 0 1**` — first day of the month |
|| `@hourly` | `0****` — every hour on the hour |

#### Managing Crontab

```bash

## Edit your crontab (opens in default text editor)

crontab -e

## List current crontab

crontab -l

## Delete your entire crontab

crontab -r
```

#### Practical Cron Examples

```bash

## Daily backup at 02:00

0 2***/home/user/backup.sh

## Weekly report every Sunday at 04:05

5 4**0 /opt/weekly-report.sh

## Log rotation on the first day of the month at 00:30

30 0 1**/usr/local/bin/rotate-logs.sh

## Check services every 5 minutes

*/5****/home/user/check-services.sh

## Restart web server every night at 03:00 (Monday–Friday)

0 3**1-5 systemctl restart nginx

## Run at system startup

@reboot /home/user/start-agent.sh
```

***Important:**Scripts run by cron have a limited environment (PATH is shorter than in your terminal).
*Always use**absolute paths**to programs and files in cron tasks:

```bash

## Wrong — cron may not find 'backup.sh'

*****backup.sh

## Correct — explicit path

0 2***/home/user/backup.sh

## Correct — also absolute path to the command itself

0 2***/bin/bash /home/user/backup.sh
```

*## Log cron output:

```bash

## Send output to log file (overwrites)

0 2***/home/user/backup.sh > /var/log/backup.log 2>&1

## Send output to log file (appends)

0 2***/home/user/backup.sh >> /var/log/backup.log 2>&1
```

`2>&1` redirects stderr (error messages) to the same file as stdout.

---

### Infrastructure as Code (IaC) — Introduction

SScripting is powerful, but it has limitations: a script describes*actions*(do this, then that), not*states*(the system
Sshould look like this). Infrastructure as Code is the next step in the automation journey.

***Definition:**IaC is the practice of defining and provisioning IT infrastructure through machine-readable configuration
*files rather than manual processes or interactive configuration tools.

#### Benefits of IaC

|| Benefit | Explanation |
|| --- | --- |
|| **Consistency** | All environments (development, test, production) are identically configured |
|| **Repeatability** | The same environment can be set up from scratch in minutes |
|| **Version control** | Infrastructure code is stored in Git — history, rollback, code review |
|| **Documentation** | The code documents itself — what runs and why |
|| **Scaling** | One configuration file can provision 1 or 1000 servers |

#### From Scripting to IaC

```bash
Manual operations → Scripting (Bash/PowerShell) → IaC (Ansible/Terraform)
```

-**Scripting**is*imperative*: "Create folder, copy file, start service."
--**IaC**is*declarative*: "The folder should exist, the file should be there, the service should run." The tool figures
-out what needs to be done.

#### Key IaC Tools

**Ansible**(Red Hat)

- Agentless: communicates via SSH, no software to install on target machines.
- Configuration is written in YAML files called**playbooks**.
- Suitable for configuration management and deploying applications.

```yaml

## Example Ansible playbook (YAML)

- name: Install and start nginx

  hosts: webservers
  tasks:

    - name: Install nginx

      apt:
        name: nginx
        state: present

    - name: Start nginx

      service:
        name: nginx
        state: started
```

**Terraform**(HashiCorp)

- Cloud-agnostic: works with AWS, Azure, Google Cloud, and many others.
- Configuration is written in**HCL**(HashiCorp Configuration Language).
- Suitable for provisioning cloud infrastructure (servers, networks, databases).

```hcl

## Example Terraform configuration (HCL)

resource "azurerm_virtual_machine" "webserver" {
  name     = "webserver-01"
  location = "norwayeast"
  size     = "Standard_B1s"
}
```

**PowerShell DSC**(Desired State Configuration)

- Microsoft's own IaC tool, integrated with Windows and Azure.
- Describes desired state for Windows configurations.

IIaC is an advanced topic that builds directly on scripting knowledge from this subject.
IBash and PowerShell are often used*inside*IaC tools for specific tasks.

#### Idempotence — A Key Principle

AAn important concept in automation and IaC is**idempotence**: an operation is idempotent if it can be run many times
AAwithout changing the result after the first successful run. Ansible and Terraform are idempotent — they always check
AAthe current state against the desired state and only make changes that are actually needed.
AAA simple Bash script run twice could create duplicates or overwrite data. Design your own scripts with idempotence in
Amind (e.g., check if the folder already exists before creating it).

#### Secure Handling of Secrets in Automated Scripts

SScripts that run automatically often need passwords, API keys, or certificates.**Never store secrets directly in script
Scode.**Good alternatives:

-**Environment variables**— Read the secret from the environment instead of hardcoding it.
-**Windows Credential Manager / Secret Store**— PowerShell module `Microsoft.PowerShell.SecretManagement`.
-**Vault solutions**— HashiCorp Vault or Azure Key Vault for production environments.

TThis is especially important when scripts are stored in [[dokumentasjon-og-planlegging-en|documentation and planning]]
Tor version control systems like Git.

---

## Example / Lab

### Lab: Set Up Automatic Backup with Task Scheduler

WWe will set up a Windows task that runs the PowerShell backup script (from [[powershell-grunnleggende-en|PowerShell
Wbasics]]) daily at 02:00.

**Prerequisite:**The backup script is located at `C:\Scripts\backup.ps1`.

*## Step 1 — Create the script folder and script:

```powershell

## Run in PowerShell as administrator

New-Item -ItemType Directory -Path "C:\Scripts" -Force

$scriptContent = @'

## backup.ps1

$source = "C:\Users\$env:USERNAME\Documents"
$target = "C:\Backup\$(Get-Date -Format 'yyyy-MM-dd')"
New-Item -ItemType Directory -Path $target -Force | Out-Null
Copy-Item -Path $source -Destination $target -Recurse -Force
Write-Host "Backup completed: $target"
'@

Set-Content -Path "C:\Scripts\backup.ps1" -Value $scriptContent -Encoding UTF8
```

*## Step 2 — Create the Task Scheduler task:

```powershell

## Define action (what to run)

$action = New-ScheduledTaskAction `
    -Execute "powershell.exe" `
    -Argument "-NonInteractive -WindowStyle Hidden -File C:\Scripts\backup.ps1"

## Define trigger (when to run)

$trigger = New-ScheduledTaskTrigger `
    -Daily `
    -At "02:00"

## Define settings

$settings = New-ScheduledTaskSettingsSet `
    -ExecutionTimeLimit (New-TimeSpan -Hours 1) `
    -RestartCount 3 `
    -RestartInterval (New-TimeSpan -Minutes 5)

## Register the task

Register-ScheduledTask `
    -TaskName "DailyBackup" `
    -Action $action `
    -Trigger $trigger `
    -Settings $settings `
    -RunLevel Highest `
    -Force
```

*## Line-by-line explanation:

|| Command | Explanation |
|| --- | --- |
|| `New-ScheduledTaskAction` | Defines what to run — here PowerShell with the backup script |
|| `-NonInteractive` | The script should not show user interfaces or wait for input |
|| `-WindowStyle Hidden` | Hide the PowerShell window during execution |
|| `New-ScheduledTaskTrigger -Daily -At "02:00"` | The task runs daily at 02:00 |
|| `New-ScheduledTaskSettingsSet` | Extra settings: time limit and automatic restart on failure |
|| `Register-ScheduledTask` | Registers (saves) the task in Task Scheduler |
|| `-RunLevel Highest` | Run with elevated privileges (administrator) |

*## Step 3 — Verify and test:

```powershell

## See the task

Get-ScheduledTask -TaskName "DailyBackup"

## Run the task manually to test

Start-ScheduledTask -TaskName "DailyBackup"

## Check if the backup folder was created

Get-ChildItem "C:\Backup"
```

*## Equivalent with schtasks (command line):

```cmd
schtasks /create /tn "DailyBackup" /tr "powershell.exe -NonInteractive -File C:\Scripts\backup.ps1" /sc DAILY /st 02:00 /ru SYSTEM /f
```

---

## Study Guide

### Automation – Scheduled Tasks and IaC

AAutomation is about letting systems perform tasks on their own — at the right time, with the right permissions, without
Ahuman intervention.

*## Two platforms for scheduling:

||  | Windows | Linux |
|| --- | --- | --- |
|| Tool | Task Scheduler / `schtasks` | cron /`crontab -e` |
|| Syntax | GUI or command line | 5 time fields + command |
|| Example | `schtasks /create /sc DAILY /st 02:00` | `0 2***/path/to/script.sh` |

**Cron syntax mnemonic**(5 fields): `minute hour day-of-month month day-of-week`

- `*`= all values,`*/5`= every five,`1-5`= Monday–Friday,`@daily` = shortcut for midnight every day.
- Always use absolute paths in cron — the PATH environment is minimal.
- Always log output: `>> /var/log/script.log 2>&1`

*## Task Scheduler — three parts of a task:
1.**Trigger**— when (time, event, logon)
2.**Action**— what (program, script)
3.**Conditions**— additional requirements (power, network)

*## From scripting to IaC:

- Scripting is*imperative*: "do A, B, C in sequence."
- IaC is*declarative*: "the system should look like this — the tool handles the rest."
- Ansible (YAML playbooks via SSH) → configuration management
- Terraform (HCL) → cloud infrastructure
- PowerShell DSC → Windows state management

***Key principles:**idempotence (safe to run multiple times), secure secret management (never passwords in code), version
*control of scripts.

CConnect to [[backup-og-gjenoppretting-en|backup and recovery]] for examples of what is automated, and
C[[skytjenester-en|cloud services]] for cloud-based IaC.

---

## FAQ

*## What happens if a cron job fails — will I be notified?
BBy default, cron sends the error message via email to the system user. In practice, it is better to log explicitly: `0
B2***/path/script.sh >> /var/log/backup.log 2>&1`. Then you can check the log manually or with a monitoring tool.

*## Can I run Task Scheduler tasks without being logged in?
YYes, if you set the user account to `SYSTEM` or a service account and check "Run whether user is logged on or not." The
Ytask then runs in the background regardless of logon status.

*## How do I test a cron job without waiting for the scheduled time?
RRun the script manually in the terminal with the same user that cron would use: `sudo -u www-data /path/to/script.sh`.
RThis simulates the cron environment well. For Task Scheduler: `schtasks /run /tn "TaskName"`.

*## What is idempotence and why is it important in automation?
IIdempotence means that an operation can be run many times without changing the result after the first successful run.
IIA script that always checks `if [ ! -d "$FOLDER" ]; then mkdir "$FOLDER"; fi` is idempotent — it only creates the
Ifolder if it doesn't exist. This is crucial for reliable automation.

*## What is the difference between Ansible and Terraform?
AAnsible is primarily used for configuration management — installing packages, starting services, editing configuration
AAfiles on existing servers. Terraform is primarily used to*provision*infrastructure — creating VMs, networks, and
AAdatabases in the cloud. In practice, they are often used together: Terraform creates the infrastructure, Ansible
Aconfigures it.

*## Can a PowerShell script in Task Scheduler run without opening a window?
YYes, add `-WindowStyle Hidden`to the arguments:`-NonInteractive -WindowStyle Hidden -File C:\Scripts\script.ps1`.
YThe script then runs in the background without a visible window.

*## Why should secrets never be hardcoded in scripts?
SScripts are often stored in version control (Git), log files, or shared with colleagues.
SSHardcoded passwords or API keys are then exposed uncontrollably. Use environment variables, Windows Credential Manager,
Sor a dedicated vault solution for sensitive information.

---

## Quiz

<details><summary>Question 1: What are the three main parts of a Task Scheduler task?</summary>

***Answer:**A task consists of (1)**Trigger**— when the task should run, (2)**Action**— what should run, and
*(3)**Conditions**— any additional requirements that must be met.

</details>

<details><summary>Question 2: What does `*/5` mean in crontab syntax?</summary>

***Answer:**`*/5`means "every five" of the relevant time unit. In the minute field,`*/5` means every 5th minute (0, 5,
*10, 15, ...). In the hour field, it would mean every 5th hour.

</details>

<details><summary>Question 3: Why should you always use absolute paths in cron tasks?</summary>

***Answer:**Cron runs with a minimal environment where the `PATH`variable is much shorter than in an interactive
**terminal. Commands that work normally in the terminal may not be found by cron. With absolute paths
*(e.g.,`/bin/bash`and`/home/user/backup.sh`), there is no ambiguity about which file is meant.

</details>

<<details><summary>Question 4: What is the fundamental difference between imperative scripting and declarative
<IaC?</summary>

***Answer:**Imperative scripting describes the*actions*to be performed in sequence ("do A, then B, then C").
**Declarative IaC describes the*desired end state*("the system should look like this"), and the tool determines which
*actions are needed to reach that state.

</details>

<details><summary>Question 5: What does `2>&1` at the end of a cron command mean?</summary>

***Answer:**It redirects**stderr**(file descriptor 2) to**stdout**(file descriptor 1).
**When combined with `>> /var/log/backup.log`, it means both normal output and error messages are written to the same log
*file.

</details>

---

## Resources

- [Microsoft Learn – Task Scheduler](<https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page>)
- [Microsoft Learn – schtasks command reference](<https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/schtasks>)
- [man7.org – crontab(5)](<https://man7.org/linux/man-pages/man5/crontab.5.html>)
- [IBM – What is Infrastructure as Code?](<https://www.ibm.com/topics/infrastructure-as-code>)
- [Microsoft Learn – PowerShell in Norwegian](<https://learn.microsoft.com/nb-no/powershell/scripting/overview>)
