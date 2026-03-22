---
title: Bash-skripting grunnleggende
public: true
emne: skripting
uke: [44, 45]
kompetansemaal: "bruke skript for å automatisere driftsoppgåver"
tags: [bash, shell, skripting, automatisering, linux]
---

# Bash-skripting

Bash (Bourne Again Shell) er standardskallet i de fleste Linux-distribusjoner og et kraftig verktøy for automatisering av driftsoppgaver.

## Et enkelt skript

```bash
#!/bin/bash
# Dette er en kommentar

echo "Hei, verden!"

# Variabler
NAVN="Driftsstøtte"
echo "Velkommen til $NAVN"
```

Lagre filen som `hei.sh`, sett kjøringsrettighet og kjør:
```bash
chmod +x hei.sh
./hei.sh
```

## Variabler og brukerinput

```bash
#!/bin/bash
read -p "Skriv inn navnet ditt: " BRUKER
echo "Hei, $BRUKER!"
```

## Kontrollstrukturer

```bash
# if-setning
if [ "$BRUKER" = "admin" ]; then
  echo "Velkommen, administrator!"
else
  echo "Tilgang nektet."
fi

# for-løkke
for FIL in /var/log/*.log; do
  echo "Prosesserer: $FIL"
done
```

## Nyttige enlinjeskript

```bash
# Sikkerhetskopier alle .conf-filer
cp /etc/*.conf /backup/

# Finn alle filer større enn 100MB
find /home -size +100M -type f

# Overvåk prosesser i sanntid
watch -n 2 'ps aux | grep nginx'
```
