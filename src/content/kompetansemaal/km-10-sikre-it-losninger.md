---
title: "KM-10: Sikre IT-løsninger / Secure IT Solutions"
emne: kompetansemaal
kompetansemaal:
  - km-10
kilder:
  - https://www.udir.no/lk20/itk02-01/kompetansemaal-og-vurdering/kv372
  - https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/
  - https://www.cloudflare.com/learning/security/glossary/
  - https://gdpr.eu/
  - https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/
tags: [km-10, sikkerhet, kryptering, brannmur, personvern, it-sikkerhet]
flashcards: false
public: true
---

# KM-10: Sikre IT-løsninger / Secure IT Solutions

## 🎯 Mål / Competency Goal

**Norsk:** Planlegge, drifte og implementere IT-løsninger som ivaretar informasjonssikkerhet og gjeldende regelverk for personvern

**English:** Plan, operate and implement IT solutions that maintain information security and comply with current privacy regulations

---

## 📘 Forklaring / Explanation

### Norsk
Å bygge sikre IT-løsninger handler om å tenke sikkerhet fra starten — ikke som en ettertanke. Dette kalles **Security by Design**[^1].

**Sentrale sikkerhetstiltak:**

- **Kryptering** — Gjør data uleselig for uautoriserte. Brukes både for data i transit (TLS/HTTPS) og data i ro (BitLocker, FileVault)
- **Brannmur** — Kontrollerer trafikk inn og ut av nettverket basert på regler. Kan være maskinvarebasert eller programvarebasert
- **Tilgangskontroll** — Hvem får tilgang til hva? Styres med RBAC, AD-grupper og NTFS-tillatelser
- **Patching** — Holde programvare oppdatert for å tette sikkerhetshull
- **Logging og overvåking (SIEM)** — Oppdage angrep ved å analysere logger

**Personvern (GDPR):** Alle IT-løsninger som behandler personopplysninger må følge personvernforordningen. Det betyr blant annet at data skal lagres sikkert, ikke oppbevares lenger enn nødvendig, og brukere skal ha innsyn i egne data.

### English
Building secure IT solutions means thinking about security from the start — not as an afterthought. This is called **Security by Design**[^1].

**Key security measures:**
- **Encryption** — Makes data unreadable to unauthorized users. Used for data in transit (TLS/HTTPS) and data at rest (BitLocker, FileVault)
- **Firewall** — Controls traffic in and out of the network based on rules. Can be hardware-based or software-based
- **Access control** — Who gets access to what? Managed with RBAC (role-based access control), Active Directory groups, and NTFS permissions
- **Patching** — Keeping software updated to close security vulnerabilities
- **Logging and monitoring (SIEM)** — Detecting attacks by analyzing security logs from multiple sources

**Privacy (GDPR):** All IT solutions that process personal data must comply with the General Data Protection Regulation. This means data must be stored securely, kept no longer than necessary, and users must have the right to access their own data.

---

## 💡 Eksempler / Examples

### Norsk

**Eksempel 1: Sikker nettside for skolen**
Skolens nettside bruker HTTPS (TLS-kryptering) slik at all trafikk mellom eleven og serveren er kryptert. En Web Application Firewall (WAF) blokkerer angrep.

**Eksempel 2: Kryptert harddisk**
En lærer mister bærbar-PC-en. Fordi harddisken var kryptert med BitLocker, kan ingen lese dataene på den — selv om de fjerner harddisken og setter den i en annen PC.

### English

**Example 1: Secure School Website**
The school's website uses HTTPS (TLS encryption) so all traffic between student and server is encrypted. A Web Application Firewall (WAF) blocks attacks.

**Example 2: Encrypted Hard Drive**
A teacher loses their laptop. Because the hard drive was encrypted with BitLocker, no one can read the data — even if they remove the drive and put it in another PC.

---

## 📝 Oppsummering / Summary

| Norsk | English |
|-------|---------|
| Security by Design = sikkerhet fra starten | Security by Design = security from the start |
| Kryptering, brannmur og tilgangskontroll er grunnleggende tiltak | Encryption, firewalls, and access control are basic measures |
| Regelmessig patching er avgjørende for sikkerhet | Regular patching is critical for security |
| IT-løsninger må følge personvernregelverket (GDPR) | IT solutions must comply with privacy regulations (GDPR) |

---

## 🔧 Bridging Exercises / Praksisoppgaver

### Norsk — Praksisoppgaver

**Oppgave 1: Konfigurer en brannmur for skolens nettverk**
Bruk en brannmursimulator (f.eks. pfSense VM eller iptables på Linux).
Scenario: Skolen har tre soner — LAN (elever/lærere), DMZ (webserver), WAN (internett).
- Sett opp NAT slik at LAN har tilgang til internett
- Opprett brannmurregler:
  - Tillat HTTP/HTTPS (80/443) fra LAN til internett
  - Tillat HTTP/HTTPS fra internett til webserver i DMZ
  - Tillat SSH (22) fra LAN til DMZ (kun IT-ansatte)
  - Blokker alt annet fra internett inn til LAN
  - Tillat ping (ICMP) kun fra LAN
- Test reglene ved å prøve forbindelser som skal tillates og blokkeres
- Dokumenter regelsettet med begrunnelse for hver regel

**Oppgave 2: Sett opp HTTPS på en webserver**
Eleven har en Apache/Nginx-webserver (fra KM-03 lab'en).
- Generer et selvsignert SSL-sertifikat med OpenSSL
- Konfigurer Apache/Nginx til å bruke sertifikatet
- Tving omdirigering fra HTTP (80) til HTTPS (443)
- Verifiser: Åpne `https://server-ip` i nettleser — se hengelåsikonet
- Bonus: Konfigurer HSTS (HTTP Strict Transport Security)
- Refleksjon: Hvorfor er HTTPS viktig for personvernet?

**Veiledning / Solution Guidelines:**
- Oppgave 1 (iptables): `iptables -A FORWARD -i lan -o wan -p tcp --dport 80 -j ACCEPT`. Standard policy: DROP på inngående fra WAN. Test med curl/wget fra ulike soner. Dokumentasjon: tegn et regelsett-diagram.
- Oppgave 2 (Apache): `a2enmod ssl`, konfigurer VirtualHost med `SSLEngine on`, `SSLCertificateFile`, `SSLCertificateKeyFile`. Redirect: `Redirect permanent / https://server/`. HSTS: `Header always set Strict-Transport-Security "max-age=31536000"`. HTTPS krypterer all data — uten HTTPS kan alle på nettverket lese passord og personopplysninger.

### English — Practical Exercises

**Exercise 1: Configure a Firewall for the School Network**
Using pfSense VM or iptables:
- Set up NAT rules for LAN internet access
- Create firewall rules for HTTP/HTTPS, SSH, ICMP across LAN/DMZ/WAN zones
- Test allowed and blocked connections
- Document the rule set with justifications

**Exercise 2: Set Up HTTPS on a Web Server**
Using the Apache/Nginx server from KM-03 lab:
- Generate a self-signed SSL certificate
- Configure the web server to use HTTPS
- Force redirect from HTTP to HTTPS
- Bonus: Configure HSTS
- Reflect: Why is HTTPS important for privacy?

**Solution Guidelines:**
- Exercise 1 (iptables): Default policy DROP on WAN inbound. Test with curl from different zones.
- Exercise 2 (Apache): Enable SSL module, configure VirtualHost with certificate paths, redirect HTTP to HTTPS. Without HTTPS, anyone on the network can read passwords and personal data.

## 🔗 Relevante artikler / Related Articles

- [[kryptering]] — Symmetrisk/asymmetrisk kryptering, TLS, PKI
- [[brannmur]] — Brannmurer, IDS/IPS og DMZ
- [[it-losninger-med-sikkerhet]] — Security by Design, Zero Trust, BCDR
- [[personvern]] — GDPR og personvern i IT-drift

## 📚 Kilder / Sources

[^1]: Udir (2020). Læreplan i Vg2 informasjonsteknologi. https://www.udir.no/lk20/itk02-01/
[^2]: NSM. Grunnprinsipper for IKT-sikkerhet. https://nsm.no/
[^3]: Cloudflare. Security Glossary. https://www.cloudflare.com/learning/security/glossary/
[^4]: NDLA. Fagstoff for driftsstøtte VG2. https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/
[^5]: GDPR.eu. Complete guide to GDPR compliance. https://gdpr.eu/
