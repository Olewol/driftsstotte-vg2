---
title: "Encryption"
emne: sikkerhet
kompetansemaal:
  - km-10
kilder:
  - ndla
  - nsm
  - microsoft
  - https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/informasjonssikkerhet-internkontroll/kryptering/
  - https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/
  - https://www.datatilsynet.no/
  - https://owasp.org/www-project-top-ten/
  - https://www.digdir.no/informasjonssikkerhet/
video: https://www.youtube.com/watch?v=N6Tf1_27n0A
notebooklm: true
tags: []
flashcards: https://notebooklm.google.com/notebook/3e72e53a-b0ca-4f05-a597-a8eea5ea7ea9
public: true
language: en
original: kryptering.md
---

## Introduction

Encryption is the technology that ensures information remains confidential even if it falls into the wrong hands. Without encryption, everything you send over the internet – passwords, banking details, health information, private messages – would be readable by anyone intercepting network traffic.

NSM recommends in its fundamental principles to "protect data at rest and in transit," and encryption is the primary tool for this. For an IT operations professional, it is essential to understand how encryption works, which standards are relevant today, and how to verify that encryption is actually in place.

Encryption is closely tied to [[personvern|privacy]] – GDPR requires that personal data be protected with appropriate technical measures, and encryption is the most central of these. The Norwegian Data Protection Authority (Datatilsynet) provides specific guidance on when and how encryption should be used in Norwegian organizations.

---

## Theory

### Symmetric Encryption

Symmetric encryption uses the **same key** to encrypt and decrypt data.

- Advantage: very fast – suitable for encrypting large amounts of data
- Disadvantage: the **key distribution problem** – the key must be shared securely between sender and receiver, which is challenging over open networks
- Example: **AES-256** (Advanced Encryption Standard with 256-bit key) – considered unbreakable and is the industry standard for encrypting data at rest (file systems, databases, backups)

**Illustration:**
```
Sender: Plaintext → [AES key] → Ciphertext
Receiver: Ciphertext → [AES key] → Plaintext
```

---

### Asymmetric Encryption

Asymmetric encryption uses a **key pair**: a public key and a private key. What is encrypted with one key can only be decrypted with the other.

- **Public key:** can be shared freely with anyone
- **Private key:** kept secret by the owner – must never be shared

Used for two purposes:
1. **Encryption:** Sender encrypts with the receiver's public key → only the receiver can decrypt with their private key
2. **Digital signature:** The sender signs with their private key → anyone can verify the signature using the sender's public key

- Examples: **RSA** (2048 or 4096-bit keys), **ECC** (Elliptic Curve Cryptography – shorter keys, same security)
- Disadvantage: much slower than symmetric encryption – poorly suited for large data volumes

---

### Hybrid Encryption

Hybrid encryption combines the best of both methods:

1. **Asymmetric encryption** is used to securely exchange a temporary symmetric key (session key)
2. **Symmetric encryption** (AES) is used for the actual data communication – efficient and fast

This is the model used by TLS (and therefore HTTPS). Almost all secure communication on the internet is based on hybrid encryption.

---

### TLS 1.3 and HTTPS

**TLS (Transport Layer Security)** is the protocol that secures communication over the internet. TLS 1.3 (2018) is the current standard and has replaced the vulnerable SSL and older TLS versions.

**TLS 1.3 handshake (simplified):**

```
1. Client sends supported cipher suites and a random value
2. Server sends chosen cipher suite, certificate, and a random value
3. Client verifies the server's certificate against a CA (Certificate Authority)
4. Both parties compute a shared session key (via ECDHE)
5. Encrypted communication begins
```

Improvements in TLS 1.3 vs 1.2:
- Faster handshake (1 round trip instead of 2)
- All outdated cipher suites removed (no RC4, DES, 3DES, MD5)
- Forward secrecy is mandatory – old sessions cannot be decrypted even if the long-term key is later compromised

Hashing is a one-way process – unlike encryption, you cannot reverse a hash to recover original data. This distinguishes hashing from encryption: encryption is two-way (reversible with the right key), hashing is one-way.

---

### PKI – Public Key Infrastructure

**PKI** is the infrastructure that makes asymmetric encryption practically usable at scale. The problem PKI solves: How do you know that a public key actually belongs to whom it claims to represent?

**Certificates (X.509):**
A digital certificate binds a public key to an identity (e.g., a domain name). The certificate is signed by a **Certificate Authority (CA)**.

**CA hierarchy (chain of trust):**
```
Root CA (self-signed, built into OS/browser)
    └── Intermediate CA (signed by Root CA)
            └── Server certificate (signed by Intermediate CA)
```

The browser verifies that the server's certificate is signed by a CA it trusts. If the certificate is invalid, expired, or self-signed, a security warning is displayed.

Well-known CAs: DigiCert, Let's Encrypt (free, automated), Sectigo, GlobalSign.

---

### Hashing

Hashing is a **one-way function** – you can create a hash from data, but you cannot reconstruct the data from the hash. Hashing is not used for encryption, but for **integrity verification**.

| Algorithm | Hash length | Status |
|---|---|---|
| MD5 | 128 bit | **Outdated** – collisions found |
| SHA-1 | 160 bit | **Outdated** – no longer recommended |
| SHA-256 | 256 bit | **Recommended** – used in TLS, certificates, Git |
| bcrypt / Argon2 | variable | **Recommended for passwords** – intentionally slow |

Typical use cases:
- Password storage: never store plaintext passwords – store the hash (with salt)
- File integrity: SHA-256 checksum of a file reveals whether it has been modified
- Digital signatures: you sign the hash of the document, not the document itself

---

### End-to-End Encryption (E2EE)

With end-to-end encryption, messages are encrypted on the sender's device and decrypted only at the receiver's end. The service in the middle (the server) cannot read the content. Examples: Signal, WhatsApp (E2EE for messages, but not backups by default).

E2EE is especially relevant for [[personvern|privacy]] – even if the server is hacked, the content is unreadable. For sensitive communication channels in organizations, E2EE is therefore an important requirement.

---

## Example / Lab

### Check HTTPS Certificate in Browser (Chrome/Edge)

1. Go to a website, e.g., [https://www.nav.no](https://www.nav.no)
2. Click the padlock icon (or info icon) to the left in the address bar
3. Select **"Connection is secure"** → **"Certificate is valid"**

Check the following in the certificate:
- **Issued to:** confirms the domain matches
- **Issued by:** which CA signed the certificate
- **Valid from / to:** certificates expire (typically 1 year for commercial, 90 days for Let's Encrypt)
- **SHA-256 fingerprint:** unique identifier for the certificate

**Bonus:** Open the browser's developer tools (F12) → Security tab to see which TLS version and cipher suite is in use.

---

## Study Guide

### Encryption – Core Content

**Two basic types:**
Symmetric encryption uses the same key both ways – fast, but key distribution is challenging. Asymmetric encryption uses key pairs (public/private) – solves the key distribution problem, but is slower. In practice, they are combined in hybrid encryption.

**Hybrid encryption and TLS:**
TLS (and HTTPS) uses asymmetric encryption only for key exchange, then symmetric AES for the actual data transfer. TLS 1.3 is the current standard with mandatory forward secrecy.

**PKI and certificates:**
PKI solves the trust problem: a Certificate Authority (CA) signs certificates and confirms that a public key belongs to the correct identity. Browsers trust pre-installed CAs. Let's Encrypt has made free, automated certificates the standard.

**Hashing vs. encryption:**
Hashing is a one-way process used for integrity verification and password storage – not for hiding data. Encryption is two-way. SHA-256 is recommended for integrity, bcrypt/Argon2 for passwords. MD5 and SHA-1 are outdated and should not be used.

**E2EE:**
End-to-end encryption ensures that only the sender and receiver can read the content – not the service provider. Critical for privacy in communication services.

**Practical checklist:**
- Always use HTTPS on websites (TLS 1.3 preferred)
- AES-256 for data at rest (files, databases, backups)
- Never store passwords in plaintext – use bcrypt/Argon2 with salt
- Check certificate status in the browser to verify HTTPS

---

## FAQ

**What is the difference between encryption and hashing?**
Encryption is a two-way operation: data is encrypted and can be decrypted again with the right key. Hashing is a one-way process: you create a fingerprint of the data but cannot reconstruct the original data from the fingerprint. Encryption is used to hide content, hashing to verify integrity.

**Why is MD5 no longer considered secure?**
The MD5 algorithm has a known weakness: it is possible to find two different inputs that produce the same hash (collision). This makes it possible to forge digital signatures and files. Use SHA-256 or newer.

**What happens if a website's certificate is expired?**
The browser displays a security warning. This does not necessarily mean the site is dangerous, but that the TLS connection cannot be verified. For users, it's a red flag. For operations staff, it's a sign of poor maintenance – certificates should be renewed automatically (e.g., with Let's Encrypt and certbot).

**What is forward secrecy and why is it important?**
Forward secrecy means session keys are deleted after use and cannot be derived from the long-term key. Even if an attacker records all encrypted traffic now and later steals the server's private key, they cannot decrypt the old traffic. TLS 1.3 requires this by default.

**Can quantum computers break the encryption we use today?**
Quantum computers are a future threat to RSA and ECC (asymmetric encryption). Symmetric AES-256 is far more resistant. NIST is working on standardizing post-quantum encryption algorithms. At the VG2 level, it's important to know that future-proof encryption is an active research field.

**What is a CA, and who can become one?**
A Certificate Authority (CA) is a trusted third party that issues digital certificates. Becoming a root CA requires strict audit requirements and approval from browser vendors (Apple, Google, Mozilla, Microsoft). Let's Encrypt is a non-profit CA that offers free, automated certificates and has revolutionized HTTPS adoption.

**Why do passwords need "salt"?**
Salt is a random value added to the password before hashing. Without salt, two users with the same password would get identical hashes – and an attacker with a precomputed "rainbow table" could crack them quickly. With salt, each hash is unique, and rainbow tables become useless.

---

## Quiz

<details><summary>Question 1: What is the key distribution problem in symmetric encryption?</summary>

**Answer:** The key distribution problem is that the sender and receiver must share the key securely in advance. Over open networks, this is difficult – if the key is intercepted during exchange, the encryption is compromised.

</details>

<details><summary>Question 2: What is the private key used for in asymmetric encryption?</summary>

**Answer:** The private key is used for two things: (1) to decrypt messages that have been encrypted with your public key, and (2) to digitally sign messages so others can verify they came from you.

</details>

<details><summary>Question 3: Why does TLS use hybrid encryption instead of only asymmetric?</summary>

**Answer:** Asymmetric encryption is very slow and poorly suited for large data volumes. TLS uses asymmetric encryption only for key exchange (to share a session key securely), then uses fast symmetric AES encryption for the actual data traffic.

</details>

<details><summary>Question 4: What is the purpose of hashing passwords?</summary>

**Answer:** Passwords are never stored in plaintext. Instead, a hash of the password is stored (preferably with salt). When the user logs in, the entered password is hashed and compared to the stored hash. Even if the database is stolen, the passwords cannot be read directly.

</details>

<details><summary>Question 5: What is a Certificate Authority (CA)?</summary>

**Answer:** A CA is a trusted third party that issues and signs digital certificates. The CA confirms that a public key actually belongs to the identity (e.g., the domain) it claims to represent. Browsers trust CAs that are pre-installed in the operating system.

</details>

---

## Flashcards

Symmetric encryption :: Encryption where the same key is used for both encryption and decryption. Fast, but key distribution is challenging. E.g., AES-256
Asymmetric encryption :: Encryption with a key pair: public key (shared freely) and private key (kept secret). E.g., RSA, ECC
Hybrid encryption :: Combines asymmetric key exchange with symmetric data encryption – the model used by TLS and HTTPS
TLS :: Transport Layer Security – protocol that secures communication over the internet. TLS 1.3 is the current standard
PKI :: Public Key Infrastructure – system of certificates and CAs that makes asymmetric encryption practical at scale
Certificate Authority (CA) :: Trusted third party that issues and signs digital certificates, confirms ownership of public keys
SHA-256 :: Cryptographic hash function that produces a 256-bit fingerprint. Recommended standard (replaces MD5 and SHA-1)
Hashing :: One-way function that creates a unique fingerprint of data. Used for integrity verification and password storage
End-to-end encryption :: Encryption where only the sender and receiver can read the content – not the server or third parties
Forward secrecy :: Property of TLS 1.3: even if the long-term key is compromised, previous sessions cannot be decrypted
Salt :: Random value added to a password before hashing to prevent rainbow table attacks and make identical passwords unique
AES-256 :: Advanced Encryption Standard with 256-bit key – the industry standard for symmetric encryption of data at rest

---

## Resources

- [NDLA – Encryption](https://ndla.no)
- [NSM Fundamental Principles – Protect data at rest and in transit](https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/)
- [Mozilla – TLS 1.3 Explained](https://hacks.mozilla.org/2018/03/introducing-the-new-firefox-63/)
- [Azure Encryption and Key Management](https://learn.microsoft.com/en-us/azure/security/fundamentals/encryption-overview)
- [Datatilsynet – Encryption of Personal Data (Norwegian)](https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/informasjonssikkerhet-internkontroll/kryptering/)
- [YouTube: Encryption (NDLA, 6 min)](https://www.youtube.com/watch?v=N6Tf1_27n0A)
