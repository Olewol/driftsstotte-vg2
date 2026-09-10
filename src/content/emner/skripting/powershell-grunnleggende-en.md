---
title: "PowerShell – Basic Scripting"
emne: skripting
kompetansemaal:
  - km-09
kilder:
  - ndla
  - https://ndla.no/subject:1:7852b71f-506e-41a4-849c-f9f30b910488/topic:1:43d5483f-0f66-4c4f-a492-c94488b0a99c/resource:155075
  - https://learn.microsoft.com/nb-no/powershell/scripting/overview
  - https://learn.microsoft.com/nb-no/powershell/scripting/
  - https://learnxinyminutes.com/docs/bash/
  - https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/
tags: []
flashcards: https://notebooklm.google.com/notebook/15678f10-b24e-462c-b837-076df87bd4b7
public: true
video: https://www.youtube.com/watch?v=FmJgD-r5U-w
notebooklm: true
language: en
original: powershell-grunnleggende.md
---

## Introduction

PowerShell is Microsoft's answer to Bash — a powerful shell language and scripting environment built into Windows. It fundamentally differs from Bash by operating with **.NET objects** instead of plain text. This means that when you retrieve information about a service, you get back an object with properties like `Name`, `Status`, and `StartType` — not just a text line you have to parse yourself.

Since PowerShell 7, it is also available on Linux and macOS, but it is primarily on Windows that it is indispensable: Active Directory, Azure, Task Scheduler, and Windows administration in general are managed efficiently via PowerShell.

PowerShell is the primary platform for managing [[active-directory]] and [[bruker-og-tilgangsstyring|user and access management]] in Windows environments. See [[automatisering|automation]] to learn how to schedule PowerShell scripts, and [[bash-grunnleggende|Bash basics]] for the Linux side of scripting.

---

## Theory

### What is PowerShell?

PowerShell is installed by default on all modern Windows versions. There are two main versions:

- **Windows PowerShell 5.1** — Built into Windows, runs only on Windows.
- **PowerShell 7+** — Open source, cross-platform, recommended for new projects.

To check which version you have:

```powershell
$PSVersionTable
```

To check and set execution policy (security policy for scripts):

```powershell
# Check current policy
Get-ExecutionPolicy

# Allow local scripts and signed scripts from the internet (recommended for operations)
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

`Restricted` is the default on Windows clients and blocks all scripts. `RemoteSigned` is a good compromise for operations environments.

### Cmdlets — Verb-Noun Convention

The basic building block in PowerShell is the **cmdlet** (pronounced "command-let"). All cmdlets follow the `Verb-Noun` pattern:

| Cmdlet | Description |
|---|---|
| `Get-Service` | Get information about services |
| `Start-Service` | Start a service |
| `Stop-Service` | Stop a service |
| `Get-Process` | List running processes |
| `Stop-Process` | Terminate a process |
| `Get-ChildItem` | List files and folders (equivalent to `ls`/`dir`) |
| `Copy-Item` | Copy file or folder |
| `Move-Item` | Move file or folder |
| `Remove-Item` | Delete file or folder |
| `New-Item` | Create new file or folder |
| `Get-Content` | Read the content of a file |
| `Set-Content` | Write content to a file |
| `Get-Help` | Display help for a cmdlet |
| `Get-Command` | Search for cmdlets |
| `Get-Member` | Display properties and methods of an object |

Approved verbs can be listed with `Get-Verb`. Following the convention makes scripts easier to read and understand.

### Pipeline and Objects

What makes PowerShell unique is that the pipeline (`|`) transfers **objects**, not text. Each object has properties and methods you can work with directly.

```powershell
# Get all services that are stopped
Get-Service | Where-Object Status -EQ "Stopped"

# Select only specific columns
Get-Service | Select-Object Name, Status, StartType

# Sort by name
Get-Service | Sort-Object Name

# Count number
Get-Service | Where-Object Status -EQ "Running" | Measure-Object
```

The pipeline is evaluated from left to right. A good rule of thumb is **"filter left"** — filter as early as possible to avoid sending unnecessary objects through the pipeline.

To examine what kind of object you are working with:

```powershell
Get-Service | Get-Member
```

This shows all properties (`Property`) and methods (`Method`) available on the object.

### Variables

Variables in PowerShell always start with `$`:

```powershell
$name = "John Doe"
$age = 25
$active = $true
```

**String types:**
- Single quotes: `'Hello $name'` — interpreted literally, no variable expansion.
- Double quotes: `"Hello $name"` — variables are expanded to their value.
- For complex expressions inside a string: `"There are $($users.Count) users"`.

**Useful automatic variables:**

| Variable | Content |
|---|---|
| `$_` | Current object in the pipeline |
| `$PSVersionTable` | Info about the PowerShell version |
| `$env:COMPUTERNAME` | The computer name |
| `$env:USERNAME` | Logged-in user |
| `$true` / `$false` | Boolean values |
| `$null` | Represents no value |

### Arrays and Hashtables

**Array** (list of values):

```powershell
$servers = @("server01", "server02", "server03")
$servers[0]          # First element: "server01"
$servers.Count       # Number of elements: 3

foreach ($server in $servers) {
    Write-Host "Connecting to $server"
}
```

**Hashtable** (key-value pairs, equivalent to a dictionary):

```powershell
$user = @{
    Name   = "Jane Olsen"
    Age    = 30
    Department = "IT"
}

$user["Name"]      # "Jane Olsen"
$user.Department   # "IT"
```

### Functions

Functions in PowerShell should follow the verb-noun convention and use a `param` block for parameters:

```powershell
function Get-UserInfo {
    param(
        [Parameter(Mandatory)]
        [string]$Username
    )

    $user = Get-LocalUser -Name $Username
    return $user
}

Get-UserInfo -Username "jane.olsen"
```

- `[Parameter(Mandatory)]` makes the parameter required — PowerShell prompts the user if it is missing.
- `[string]` is a type annotation that ensures the value is a string.
- `[CmdletBinding()]` at the top of the function adds support for `-Verbose`, `-Debug`, and other common parameters.

### Modules

Modules are collections of cmdlets that can be loaded as needed:

```powershell
# Import a module
Import-Module ActiveDirectory

# List available cmdlets in the module
Get-Command -Module ActiveDirectory

# Install module from PowerShell Gallery
Install-Module -Name PSReadLine -Scope CurrentUser
```

Many Windows features (Active Directory, Exchange, Azure) are delivered as PowerShell modules.

### Write-Host vs Write-Output

A common source of confusion for beginners is the difference between these two:

| Cmdlet | What it does |
|---|---|
| `Write-Host` | Writes directly to the console — **not** to the pipeline. Cannot be captured by other cmdlets. |
| `Write-Output` | Sends the object to the pipeline. Other cmdlets can use it further. |

Example:

```powershell
# Write-Host: only displayed on screen
Write-Host "This does not go into the pipeline"

# Write-Output: can be used further in the pipeline
Write-Output "This can be piped further" | Out-File "log.txt"

# In functions: return with Write-Output (or just the value directly)
function Get-Double {
    param([int]$Number)
    Write-Output ($Number * 2)
}
$result = Get-Double -Number 5   # $result = 10
```

As a rule of thumb: use `Write-Host` only for messages to the user on screen. Use `Write-Output` (or return the value directly) when you want the function to produce data for the rest of the script.

### Error Handling

PowerShell uses `try/catch` for structured error handling:

```powershell
try {
    Get-Item "C:\doesnotexist.txt" -ErrorAction Stop
}
catch {
    Write-Host "Error occurred: $($_.Exception.Message)" -ForegroundColor Red
}
```

`-ErrorAction Stop` is necessary for the error to be caught by `catch`. The default error behavior in PowerShell is to continue.

---

## Example / Lab

### Lab: List Local Users and Save to CSV

We will write a script that retrieves all local user accounts, selects relevant properties, and exports them to a CSV file.

```powershell
# userlist.ps1 — Get and save local users
# Requires: Windows (local users do not exist on Linux/macOS)

# ─── Get users ────────────────────────────────────────────────
$users = Get-LocalUser | Select-Object Name, Enabled, LastLogon

# ─── Export to CSV ────────────────────────────────────────────
$users | Export-Csv -Path "C:\userlist.csv" -NoTypeInformation -Encoding UTF8

# ─── Confirmation ─────────────────────────────────────────────
Write-Host "Saved $($users.Count) users to userlist.csv"
```

**Line-by-line explanation:**

| Line | Explanation |
|---|---|
| `Get-LocalUser` | Retrieves all local user accounts on the machine as .NET objects |
| `Select-Object Name, Enabled, LastLogon` | Selects only three properties from each user object — reduces data size |
| `$users = ...` | Stores the list of user objects in the variable `$users` |
| `Export-Csv -Path "C:\userlist.csv"` | Writes the objects to a CSV file at the specified path |
| `-NoTypeInformation` | Removes the first line in the CSV file that otherwise contains .NET type info |
| `-Encoding UTF8` | Ensures that Norwegian characters (æ, ø, å) are saved correctly |
| `$($users.Count)` | Subexpression that gets the number of elements in the array and inserts it into the string |
| `Write-Host` | Writes output message to the console (not to the pipeline) |

**Run the script:**

```powershell
# Open PowerShell as administrator
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# Navigate to the folder where the script is located
cd C:\Scripts

# Run the script
.\userlist.ps1

# See the result
Import-Csv "C:\userlist.csv" | Format-Table
```

**Extended version — add error handling:**

```powershell
# userlist-extended.ps1

$outputFile = "C:\userlist.csv"

try {
    $users = Get-LocalUser | Select-Object Name, Enabled, LastLogon
    $users | Export-Csv -Path $outputFile -NoTypeInformation -Encoding UTF8
    Write-Host "Saved $($users.Count) users to $outputFile" -ForegroundColor Green
}
catch {
    Write-Host "ERROR: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}
```

---

## Study Guide

### PowerShell – Basic Scripting

PowerShell differs from traditional shell languages by working with **.NET objects** instead of plain text. This makes it easier to filter, sort, and export data without parsing text strings.

**Core concepts:**

1. **Cmdlets** always follow the `Verb-Noun` pattern (e.g., `Get-Service`, `Stop-Process`). This makes it easy to guess commands.
2. **The pipeline (`|`)** sends objects forward — not text. Use `Where-Object` for filtering, `Select-Object` to choose properties, `Sort-Object` for sorting.
3. **Variables** always start with `$`. Single quotes are literal, double quotes expand variables.
4. **Arrays** (`@(...)`) and **hashtables** (`@{...}`) are basic data structures for collecting and organizing data.
5. **Functions** use a `param` block for parameters and should follow the verb-noun convention.
6. **Modules** extend PowerShell with new cmdlets — `Import-Module ActiveDirectory` for AD administration.
7. **Error handling** with `try/catch` requires `-ErrorAction Stop` to catch errors from cmdlets.

**Important distinctions:**
- `Write-Host` displays to screen; `Write-Output` sends to the pipeline — use correctly in functions.
- Execution Policy controls which scripts can run; `RemoteSigned` is a good choice in operations environments.
- `Get-Member` is your best friend: shows all properties and methods of an object in the pipeline.

**Typical operations tasks with PowerShell:** user administration in [[active-directory]], export of user lists, service monitoring, and file management. Combine with [[automatisering|automation]] to schedule scripts.

---

## FAQ

**What is the most important difference between PowerShell and Command Prompt (cmd.exe)?**
Command Prompt runs old DOS commands and works only with text. PowerShell runs cmdlets and works with .NET objects — that means structured data with properties you can filter and sort directly, without manually parsing text strings.

**Why do I get the error message "running scripts is disabled on this system"?**
The Execution Policy is set to `Restricted` (default on Windows clients). Run `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` to allow local scripts. This is a security setting that prevents malicious scripts from running automatically.

**What does `Get-Member` do and why is it useful?**
`Get-Member` shows all properties (Property) and methods (Method) on the objects passed in via the pipeline. Write e.g., `Get-Service | Get-Member` to see what kind of data you can work with. Indispensable for discovering which properties exist on an unknown object.

**What is the difference between `Select-Object` and `Where-Object`?**
`Select-Object` chooses which *columns* (properties) to display — used to reduce data volume. `Where-Object` filters which *rows* (objects) pass through based on a condition. They are often used together: `Get-Service | Where-Object Status -EQ "Running" | Select-Object Name, Status`.

**Can I use PowerShell on Linux?**
Yes, PowerShell 7+ is open source and can be installed on Linux and macOS. However, many Windows-specific cmdlets (such as `Get-LocalUser` and `Import-Module ActiveDirectory`) are only available on Windows. For Linux scripting, [[bash-grunnleggende|Bash basics]] is more natural.

**What does `[Parameter(Mandatory)]` mean in a function?**
It is an attribute that makes the parameter mandatory. If the user calls the function without providing that parameter, PowerShell stops and asks for the value interactively. This is better than letting the script fail with a cryptic error message.

**What is ISE and should I use it?**
ISE (Integrated Scripting Environment) is a built-in graphical tool for writing and testing PowerShell scripts. For newer projects, **VS Code** with the PowerShell extension is recommended — it is faster, has better debugging, and supports PowerShell 7+.

---

## Quiz

<details><summary>Question 1: What is the fundamental difference between the PowerShell pipeline and the Bash pipeline?</summary>

**Answer:** PowerShell sends **.NET objects** through the pipeline — you work with structured data that has properties and methods. Bash sends **text** (strings), which you have to parse yourself with tools like `grep`, `awk`, and `cut`.

</details>

<details><summary>Question 2: What does `Where-Object` do in a pipeline?</summary>

**Answer:** `Where-Object` filters objects in the pipeline and only passes through those that meet a condition. For example: `Get-Service | Where-Object Status -EQ "Running"` shows only services that are running.

</details>

<details><summary>Question 3: Why do you use `-NoTypeInformation` with `Export-Csv`?</summary>

**Answer:** Without `-NoTypeInformation`, PowerShell adds an extra first line to the CSV file with the .NET type name of the object (e.g., `#TYPE Microsoft.PowerShell.Commands.LocalUser`). This line is unnecessary and can confuse other programs reading the CSV file.

</details>

<details><summary>Question 4: What is the difference between single quotes and double quotes in PowerShell?</summary>

**Answer:** Single quotes (`'...'`) are static strings — nothing is interpreted, variable names are written literally. Double quotes (`"..."`) expand variables and subexpressions. For example: `'$name'` produces the text `$name`, while `"$name"` produces the value of the variable `$name`.

</details>

<details><summary>Question 5: What is needed for an error to be caught by `catch` in PowerShell?</summary>

**Answer:** You must add `-ErrorAction Stop` to the cmdlet that might fail. By default, PowerShell cmdlets are set to continue even on error (`-ErrorAction Continue`), and then an exception error that `catch` can catch is not thrown.

</details>

---

## Flashcards

Cmdlet :: Basic command unit in PowerShell, follows Verb-Noun pattern (e.g., Get-Service)
`$_` :: Automatic variable in PowerShell that represents the current object in a pipeline
`Get-Member` :: Cmdlet that shows all properties and methods of the objects passed in
`Where-Object` :: Cmdlet that filters pipeline objects based on a condition
`Select-Object` :: Cmdlet that selects specific properties from pipeline objects
`Export-Csv` :: Cmdlet that writes pipeline objects to a CSV file
`Import-Module` :: Loads a PowerShell module with its associated cmdlets
`param` block :: Declares parameters for a PowerShell function with type and validation
`[Parameter(Mandatory)]` :: Attribute that makes a function parameter mandatory
`-ErrorAction Stop` :: Makes a cmdlet throw an exception on error, so `catch` can handle it
Execution Policy :: Security policy that determines which PowerShell scripts can run
`$env:COMPUTERNAME` :: Automatic environment variable with the machine's name
`Write-Host` :: Writes directly to the console — not sent to the pipeline and cannot be captured by other cmdlets
`Write-Output` :: Sends the value to the pipeline so it can be processed further by other cmdlets
ISE (Integrated Scripting Environment) :: Built-in graphical tool in Windows for writing and testing PowerShell scripts

---

## Resources

- [Microsoft Learn – PowerShell 101: Getting Started](https://learn.microsoft.com/en-us/powershell/scripting/learn/ps101/01-getting-started)
- [Microsoft Learn – PowerShell 101: Pipeline](https://learn.microsoft.com/en-us/powershell/scripting/learn/ps101/04-pipelines)
- [Microsoft Learn – PowerShell 101: Functions](https://learn.microsoft.com/en-us/powershell/scripting/learn/ps101/09-functions)
- [SS64 – PowerShell cmdlet reference](https://ss64.com/ps/)
- [Microsoft Learn – PowerShell in Norwegian (overview)](https://learn.microsoft.com/nb-no/powershell/scripting/overview)
- [NDLA – PowerShell and scripting for VG2 IT](https://ndla.no/subject:1:7852b71f-506e-41a4-849c-f9f30b910488/topic:1:43d5483f-0f66-4c4f-a492-c94488b0a99c/resource:155075)
- [YouTube – PowerShell in Norwegian – Basics (norskADMIN, ~12 min)](https://www.youtube.com/watch?v=FmJgD-r5U-w)
