---
title: Backup og katastrofegjenoppretting
public: true
emne: it-drift
uke: [13, 14]
kompetansemaal: "planlegge og dokumentere IT-driftsoppgaver"
tags: [backup, gjenoppretting, disaster-recovery, rto, rpo]
---

# Backup og katastrofegjenoppretting

Backup er en kopi av data som kan brukes til å gjenopprette informasjon ved tap, korrupsjon eller katastrofe.

## 3-2-1-regelen

Den gyldne regelen for backup:

- **3** kopier av data
- **2** ulike lagringsmedier
- **1** kopi offsite (utenfor bygget)

## Typer backup

| Type | Forklaring | Tid | Plass |
|------|-----------|-----|-------|
| **Full** | Komplett kopi av alt | Lang | Mye |
| **Inkrementell** | Bare endringer siden siste backup | Kort | Lite |
| **Differensiell** | Endringer siden siste fulle backup | Medium | Medium |

## Viktige begreper

- **RTO** (Recovery Time Objective) — Hvor lenge systemet kan være nede
- **RPO** (Recovery Point Objective) — Hvor mye data man kan tape (tid siden siste backup)

## Backup med rsync

```bash
# Enkel backup av hjemmemappen
rsync -avz /home/bruker/ /backup/bruker/

# Backup til fjernserver
rsync -avz -e ssh /var/www/ bruker@backupserver:/backup/www/

# Inkrementell backup med tidsstempel
rsync -avz --backup --backup-dir=/backup/$(date +%Y-%m-%d) /data/ /backup/current/
```

## Teste backup

En backup som ikke er testet er ikke en backup. Test gjenoppretting jevnlig!
