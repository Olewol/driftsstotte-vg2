---
title: Filsystem i Linux og Windows
public: true
emne: operativsystem
uke: [42]
kompetansemaal: "installere, konfigurere og drifte operativsystem"
tags: [filsystem, ext4, ntfs, linux, windows, partisjon]
---

# Filsystem

Et filsystem er metoden et operativsystem bruker for å organisere og lagre filer på en lagringsenhet.

## Linux filsystem

### Mappestruktur
```
/               Root — roten av hele filsystemet
├── /bin        Grunnleggende brukerprogram
├── /etc        Konfigurasjonsfiler
├── /home       Hjemmemapper for brukere
├── /var        Variable data (logger, databaser)
├── /tmp        Midlertidige filer
└── /usr        Brukerprogram og biblioteker
```

### Vanlige filsystemer i Linux
- **ext4** — Standard for de fleste Linux-distribusjoner
- **XFS** — Bra for store filer og høy ytelse
- **Btrfs** — Støtter snapshot og komprimering

## Windows filsystem

- **NTFS** — Standard i Windows, støtter rettigheter og kryptering
- **FAT32** — Eldre, kompatibelt med mange enheter
- **exFAT** — For USB-disker og minnekort

## Montering i Linux

```bash
# Vis monterte filsystemer
df -h

# Monter en partisjon
sudo mount /dev/sdb1 /mnt/data

# Automatisk montering via /etc/fstab
/dev/sdb1  /mnt/data  ext4  defaults  0  2
```
