---
title: "Bash – Basic Scripting"
emne: skripting
kompetansemaal:
  - km-09
kilder:
  - ndla
  - https://ndla.no/nb/subject:1:89932061-799d-499d-948c-399738003791/topic:1:185333/resource:1:153844
  - https://learnxinyminutes.com/docs/bash/
  - https://learn.microsoft.com/nb-no/powershell/scripting/
  - https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/
tags: []
flashcards: https://notebooklm.google.com/notebook/15678f10-b24e-462c-b837-076df87bd4b7
public: true
video: https://www.youtube.com/watch?v=e7BufAVwgyM
notebooklm: true
language: en
original: bash-grunnleggende.md
---

## Introduction

Bash (Bourne Again SHell) is the standard shell on most Linux distributions and macOS. It is the first language most system administrators learn to script in, and for good reason: Bash is available everywhere on Linux, requires no installation, and has direct access to all system tools.

In this article, you will learn the basic building blocks of Bash scripting: shebang, variables, conditional statements, loops, functions, and file operations. All of this is used in the practical lab where we build a complete backup script.

Bash is closely tied to [[linux-grunnleggende-en|Linux basics]] and is actively used in [[automatisering-en|automation]] of operations tasks. To compare with the Windows side, see [[powershell-grunnleggende-en|PowerShell basics]].

---

## Theory

### Shebang — `#!/bin/bash`

The very first line of a Bash script is called the **shebang** (or hashbang). It tells the operating system which program should interpret the file.

```bash
#!/bin/bash
```

- `#!` is a magic prefix that the operating system recognizes.
- `/bin/bash` is the path to the Bash interpreter.

Without the shebang, the script might still run, but it depends on the shell that called the script being Bash. With the shebang, it is always explicit.

To make the file executable, use `chmod`:

```bash
chmod +x myscript.sh
./myscript.sh
```

### Variables

A variable is a named storage location for data. In Bash, variables are declared without spaces around `=`:

```bash
NAME="John Doe"
AGE=25
```

To read the value, use `$` before the name:

```bash
echo "Hello, $NAME"
echo "You are $AGE years old"
```

**Important rules:**

- No spaces around `=` when assigning (`VAR="value"`, not `VAR = "value"`).
- Use double quotes `"..."` around variables to handle spaces in values.
- Single quotes `'...'` do not interpret variables — `'$NAME'` gives the literal `$NAME`.

**Built-in variables** (environment variables):

| Variable | Content |
|---|---|
| `$HOME` | The user's home directory |
| `$USER` | The username |
| `$PATH` | Directories where the shell searches for programs |
| `$0` | The name of the script |
| `$1`, `$2` ... | Arguments given to the script |
| `$#` | Number of arguments |
| `$?` | Exit code from the previous command (0 = success) |
| `$$` | Process ID (PID) of the script |

**Command substitution** — store the output of a command in a variable:

```bash
DATE=$(date +%Y-%m-%d)
echo "Today is $DATE"
```

### Conditional Statements — if/else

The `if` statement allows the script to make decisions based on a condition.

```bash
if [ condition ]; then
    # runs if condition is true
elif [ other_condition ]; then
    # runs if the other condition is true
else
    # runs if no condition is true
fi
```

Spaces inside `[ ]` are mandatory.

**File tests:**

| Test | Description |
|---|---|
| `[ -f FILE ]` | File exists and is a regular file |
| `[ -d FOLDER ]` | Folder exists |
| `[ -r FILE ]` | File is readable |
| `[ -x FILE ]` | File is executable |
| `[ -e PATH ]` | Path exists (file or folder) |

**String comparisons:**

| Test | Description |
|---|---|
| `[ "$A" == "$B" ]` | Strings are equal |
| `[ "$A" != "$B" ]` | Strings are not equal |
| `[ -z "$A" ]` | String is empty |
| `[ -n "$A" ]` | String is not empty |

**Numeric comparisons:**

| Test | Description |
|---|---|
| `[ $A -eq $B ]` | A equals B |
| `[ $A -ne $B ]` | A does not equal B |
| `[ $A -lt $B ]` | A is less than B |
| `[ $A -gt $B ]` | A is greater than B |
| `[ $A -le $B ]` | A is less than or equal to B |
| `[ $A -ge $B ]` | A is greater than or equal to B |

Example:

```bash
if [ -f "/etc/passwd" ]; then
    echo "The file exists"
else
    echo "The file was not found"
fi
```

### For Loops

A `for` loop repeats a block of commands for each element in a list.

```bash
for VARIABLE in element1 element2 element3; do
    echo "$VARIABLE"
done
```

Practical example — iterate over files in a folder:

```bash
for FILE in /var/log/*.log; do
    echo "Processing: $FILE"
done
```

Counting with a number sequence:

```bash
for i in $(seq 1 5); do
    echo "Round $i"
done
```

### While Loops

A `while` loop runs as long as the condition is true.

```bash
COUNTER=1
while [ $COUNTER -le 5 ]; do
    echo "Iteration $COUNTER"
    COUNTER=$((COUNTER + 1))
done
```

`$((expression))` is used for arithmetic in Bash.

### Functions

Functions group reusable code into named blocks. They are defined at the top of the script and called by name.

```bash
function say_hello {
    echo "Hello, $1!"
}

say_hello "John"
say_hello "Jane"
```

- `$1` inside the function refers to the first argument given to the function (not the script).
- `local` is used for variables that should only exist inside the function:

```bash
function calculate_sum {
    local A=$1
    local B=$2
    echo $((A + B))
}

RESULT=$(calculate_sum 10 20)
echo "The sum is: $RESULT"
```

### File Operations

Bash has powerful built-in commands for file handling:

| Command | Description |
|---|---|
| `mkdir -p PATH` | Create folder (and parent folders if necessary) |
| `cp -r SOURCE DEST` | Copy recursively (including subfolders) |
| `mv SOURCE DEST` | Move or rename |
| `rm -r FOLDER` | Delete folder recursively |
| `ls -la` | List files with details |
| `find PATH -name "*.log"` | Find files by name |

### Shellcheck — Static Analysis of Scripts

**Shellcheck** is a free tool that analyzes Bash scripts and points out potential bugs, bad practices, and security issues — without you needing to run the script.

```bash
# Install on Ubuntu/Debian
sudo apt install shellcheck

# Analyze a script
shellcheck backup.sh
```

Shellcheck will, for example, warn about missing quotation marks around variables (`"$VAR"` instead of `$VAR`), which can cause unexpected errors when filenames contain spaces. It is good practice to run shellcheck on all scripts before putting them into production.

### Error Handling

The special variable `$?` contains the exit code of the previous command. `0` means success, anything else is an error.

```bash
cp /important/file /backup/
if [ $? -ne 0 ]; then
    echo "ERROR: Copy failed!" >&2
    exit 1
fi
```

`>&2` sends the error message to stderr instead of stdout.

A simpler alternative is `set -e` at the top of the script — then the script automatically stops at the first error:

```bash
#!/bin/bash
set -e
```

---

## Example / Lab

### Lab: Complete Backup Script

We will write a script that:

1. Defines source and destination folders
2. Creates a date-based backup folder
3. Copies the content
4. Confirms success

```bash
#!/bin/bash
# backup.sh — Daily backup of documents
# Usage: ./backup.sh

set -e  # Stop on first error

# ─── Configuration ───────────────────────────────────────────
SOURCE="/home/user/documents"
TARGET="/backup/$(date +%Y-%m-%d)"

# ─── Check that source folder exists ─────────────────────────
if [ ! -d "$SOURCE" ]; then
    echo "ERROR: Source folder '$SOURCE' does not exist." >&2
    exit 1
fi

# ─── Create destination folder ────────────────────────────────
mkdir -p "$TARGET"

# ─── Perform copy ─────────────────────────────────────────────
cp -r "$SOURCE" "$TARGET"

# ─── Confirmation ─────────────────────────────────────────────
echo "Backup completed: $TARGET"
```

**Line-by-line explanation:**

| Line | Explanation |
|---|---|
| `#!/bin/bash` | Shebang — run with Bash |
| `set -e` | Stop the script immediately if a command fails |
| `SOURCE=...` | Variable for the source folder to be backed up |
| `TARGET=...` | Variable for the destination folder; `$(date +%Y-%m-%d)` gives today's date as folder name |
| `if [ ! -d "$SOURCE" ]` | Check that the source folder actually exists (`!` means NOT, `-d` checks for directory) |
| `exit 1` | Exit the script with error code 1 (indicates error) |
| `mkdir -p "$TARGET"` | Create the destination folder; `-p` also creates parent folders without error if they exist |
| `cp -r "$SOURCE" "$TARGET"` | Copy recursively from source to destination |
| `echo "Backup completed: $TARGET"` | Print confirmation message with the path to the backup folder |

**How to test the script:**

```bash
# Give execute permissions
chmod +x backup.sh

# Test with a safe source folder
SOURCE="/tmp/testdocuments"
mkdir -p "$SOURCE"
echo "testcontent" > "$SOURCE/test.txt"

# Run the script
./backup.sh
```

---

## Study Guide

### Bash – Basic Scripting

Bash is the shell language you encounter on all Linux systems. A Bash script is a text file with commands that are executed line by line by the Bash interpreter.

**Structure of a script:**

1. **Shebang** (`#!/bin/bash`) — always the first line, points to the interpreter.
2. **Variables** — store data. Assigned without spaces (`NAME="value"`), read with `$NAME`.
3. **Conditional statements** — `if [ condition ]; then ... fi` controls flow. Use file tests (`-f`, `-d`) and comparisons (`-eq`, `==`).
4. **Loops** — `for` loop iterates over lists; `while` loop runs as long as a condition is true.
5. **Functions** — named blocks of reusable code. Arguments are accessed with `$1`, `$2`, etc. Use `local` for local variables.
6. **File operations** — `mkdir -p`, `cp -r`, `mv`, `rm -r`, `find`.
7. **Error handling** — `$?` is the exit code (0 = ok). `set -e` stops the script at the first error. `>&2` sends error messages to stderr.

**Good practices:**

- Always use `"$VAR"` (double quotes) around variables — protects against spaces in values.
- Run `shellcheck script.sh` to find errors before execution.
- Use absolute paths in scripts called by cron or automated systems.
- Command substitution `$(command)` stores output from a command in a variable.

**Typical use cases in operations:** backup scripts, log rotation, user creation, system monitoring — see [[automatisering-en|automation]] for how such scripts are scheduled.

---

## FAQ

**What is the difference between `[ ]` and `[[ ]]` in Bash?**
`[ ]` is the POSIX-compatible test that works in all Unix shells. `[[ ]]` is a Bash extension that provides additional features like pattern matching with `=~` and logical operators without needing `&&`/`||` inside. For VG2 level, `[ ]` is sufficient, but it is good to know that `[[ ]]` is safer against edge cases.

**What happens if I forget spaces inside `[ ]`?**
It fails. `[$VARIABLE -eq 5]` gives a syntax error because `[` is a command that requires spaces around all arguments. The correct form is `[ $VARIABLE -eq 5 ]`.

**Can I run a Bash script without `chmod +x`?**
Yes, by calling the interpreter explicitly: `bash myscript.sh`. You do not need execute permissions then. `chmod +x` is only necessary if you want to run the script directly with `./myscript.sh`.

**What does `>&2` mean in an error message?**
`2` is the file descriptor for stderr (standard error), and `>&2` redirects output to stderr. This allows error messages to be separated from normal output when the script runs in automated systems.

**What is an exit code and why is 0 success?**
An exit code is a number (0–255) that a program returns when it terminates. The convention in Unix is that 0 means "everything went well" and anything else means some form of error. Bash scripts can read the previous command's exit code with `$?`.

**How do I stop a script immediately on error?**
Add `set -e` at the top (after the shebang). The script will then automatically exit with an error if a command returns a non-zero exit code — instead of continuing with a failed state.

**What is command substitution and when is it used?**
`$(command)` runs the command and inserts the output in place of the substitution itself. Typical use: `DATE=$(date +%Y-%m-%d)` stores today's date in a variable, which is used in filenames for backup folders.

---

## Quiz

<details><summary>Question 1: What does the shebang line `#!/bin/bash` at the top of a script do?</summary>

**Answer:** It tells the operating system that the file should be interpreted by the program `/bin/bash`. Without the shebang, the script may be run by the wrong interpreter or not at all.

</details>

<details><summary>Question 2: What is the value of `$?` after a command that succeeded?</summary>

**Answer:** `0`. In Bash (and Unix in general), exit code `0` means success. All other values indicate an error.

</details>

<details><summary>Question 3: Why do we use `mkdir -p` instead of just `mkdir`?</summary>

**Answer:** `-p` (parents) also creates any missing parent folders in the path, and does not give an error if the folder already exists. `mkdir /backup/2024-01-01` would fail if `/backup` does not exist, but `mkdir -p /backup/2024-01-01` works regardless.

</details>

<details><summary>Question 4: What is the difference between `$1` in the script's main part and `$1` inside a function?</summary>

**Answer:** In the script's main part, `$1` refers to the first argument given to the *script* when it runs (e.g., `./script.sh argument1`). Inside a function, `$1` refers to the first argument given to the *function* when called.

</details>

<details><summary>Question 5: What does `set -e` do at the top of a Bash script?</summary>

**Answer:** It makes the script abort immediately if a command returns a non-zero exit code (i.e., an error). This prevents the script from continuing in a partially failed state.

</details>

---

## Resources

- [TLDP Bash Beginners Guide](https://tldp.org/LDP/Bash-Beginners-Guide/html/index.html)
- [TLDP – Bash if/else syntax](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_01.html)
- [SS64 – Bash A–Z reference](https://ss64.com/bash/)
- [NDLA – Bash and Linux scripting](https://ndla.no/nb/subject:1:89932061-799d-499d-948c-399738003791/topic:1:185333/resource:1:153844)
- [Learn X in Y Minutes – Bash](https://learnxinyminutes.com/docs/bash/) — compact syntax overview
- [YouTube – You need to learn Bash Scripting RIGHT NOW!! (NetworkChuck, ~21 min)](https://www.youtube.com/watch?v=e7BufAVwgyM)
