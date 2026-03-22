---
title: Brannmur og pakkefiltrering
public: true
emne: sikkerhet
uke: [48, 49]
kompetansemaal: "planlegge og implementere sikkerhetstiltak"
tags: [brannmur, firewall, pakkefiltrering, acl, nettverkssikkerhet]
---

# Brannmur og pakkefiltrering

En brannmur er et sikkerhetssystem som overvåker og kontrollerer inn- og utgående nettverkstrafikk basert på definerte regler.

## Typer brannmurer

### Pakkefiltrering
Den enkleste formen. Analyserer hver nettverkspakke og bestemmer om den skal slippes gjennom eller blokkeres basert på:
- Kilde- og destinasjons-IP-adresse
- Portnummer
- Protokoll (TCP/UDP)

### Stateful inspection
Holder styr på aktive tilkoblinger og bestemmer om pakkene tilhører en etablert sesjon.

### Application-layer firewall (WAF)
Analyserer trafikk helt opp til applikasjonslaget og kan forstå protokoller som HTTP og DNS.

## Regler og ACL

Access Control Lists (ACL) er settet av regler som definerer hvilken trafikk som er tillatt. Reglene evalueres i rekkefølge — første treff vinner.

```
# Eksempel på iptables-regel (Linux)
iptables -A INPUT -p tcp --dport 22 -j ACCEPT   # Tillat SSH
iptables -A INPUT -p tcp --dport 80 -j ACCEPT   # Tillat HTTP
iptables -A INPUT -j DROP                        # Blokker alt annet
```
