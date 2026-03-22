---
title: Linux grunnleggende
public: true
emne: operativsystem
uke: [40, 41]
kompetansemaal: "installere, konfigurere og drifte operativsystem"
tags: [linux, terminal, kommandolinje, bash, cli]
---

# Linux grunnleggende

Linux er et åpen kildekode-operativsystem som er svært utbredt i servermiljøer og IT-drift.

## Viktige kommandoer

| Kommando | Forklaring |
|----------|-----------|
| `ls` | List filer og mapper |
| `cd` | Endre katalog |
| `pwd` | Vis gjeldende katalog |
| `mkdir` | Opprett ny mappe |
| `rm` | Slett fil eller mappe |
| `cp` | Kopier fil |
| `mv` | Flytt eller gi nytt navn til fil |
| `cat` | Vis innhold i fil |
| `man` | Vis hjelpeside for kommando |

## Filrettigheter

Linux bruker et rettighetssystem med tre nivåer: eier, gruppe og andre.

```bash
# Vis rettigheter
ls -l filnavn.txt
# -rw-r--r-- 1 bruker gruppe 1024 jan 1 12:00 filnavn.txt

# Endre rettigheter
chmod 755 skript.sh   # rwxr-xr-x
chmod +x skript.sh    # Legg til kjøringsrettighet
```

## Pakkehåndtering

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install pakkenavn

# CentOS/RHEL
sudo dnf install pakkenavn
```
