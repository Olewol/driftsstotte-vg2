---
title: "Filsystemer"
emne: operativsystem
kompetansemaal:
  - km-04
kilder:
  - ndla
tags: []
flashcards: true
public: true
---

## Introduksjon

Et **filsystem** bestemmer hvordan data lagres og organiseres på en disk. For IT-driftsteknikere er valg av filsystem direkte knyttet til sikkerhet og tilgangskontroll — kun NTFS støtter for eksempel brukerbaserte tillatelser i Windows. Kunnskap om filsystemer er nødvendig for å administrere rettigheter, sette opp kvoter og forstå begrensningene på ulike lagringsmedier.

---

## Teori

### NTFS (New Technology File System)

NTFS er standard filsystem for Windows og Windows Server. Det er det eneste alternativet når du trenger tilgangskontroll på filnivå i Windows.

**Nøkkelfunksjoner:**

- **Access Control Lists (ACL)**: Hver fil og mappe har en ACL som lister opp hvilke brukere og grupper som har hvilke tillatelser. Dette er selve motoren bak Windows-tilgangskontroll.
- **Tillatelsesarv**: Tillatelser arves som standard fra overordnet mappe. Hvis du gir gruppe `Elever` lesetilgang til `C:\Felles`, arver alle undermapper denne tillatelsen automatisk. Arv kan deaktiveres per objekt.
- **Diskkvoter**: Administratorer kan sette grenser for hvor mye lagringsplass enkeltbrukere kan bruke på et volum.
- **Journaling (transaksjonslogg)**: NTFS logger alle filoperasjoner til en journal. Hvis systemet krasjer midt i en skriveoperasjon, kan journalen brukes til å gjenopprette konsistens ved neste oppstart.
- **Kryptering og komprimering**: Støtter EFS (Encrypting File System) og transparent komprimering.
- **Maks volum**: Opptil 8 petabyte med 2 MB klyngestørrelse (Windows Server 2019).

**NTFS-tillatelsesnivåer:**

| Tillatelse | Hva brukeren kan gjøre |
|---|---|
| Full kontroll | Alt — inkludert endre tillatelser og ta eierskap |
| Endre | Les, skriv, slett filer og undermapper |
| Les og kjør | Se innhold og kjøre programmer |
| List mappeinnhold | Se filnavn i mappen (ikke åpne filene) |
| Les | Åpne og lese filer |
| Skriv | Opprette nye filer og mapper, skrive til eksisterende |

> **Merk**: NTFS-tillatelser gjelder både lokalt og over nettverk. Når en bruker aksesserer en delt mappe, kombineres NTFS-tillatelser med delte tillatelser (Share Permissions) — den mest restriktive kombinasjonen gjelder.

### FAT32 (File Allocation Table 32)

FAT32 er et eldre filsystem som støttes av praktisk talt alle operativsystemer og enheter. Det brukes primært på USB-pinner og minnekort.

**Kjennetegn:**
- **Ingen tilgangskontroll** — alle som kan lese disken kan lese alle filer
- **Maks filstørrelse: 4 GB − 1 byte** (4 294 967 295 bytes) — kan ikke lagre enkeltfiler på 4 GB eller mer (f.eks. store ISO-filer eller videofiler)
- **Maks volumstørrelse: 2 TB**
- Støttes av Windows, macOS og Linux uten ekstra drivere
- Brukes **ikke** til Windows Server-volumer

### exFAT (Extended FAT)

exFAT er en etterfølger til FAT32 designet for flash-lagring. Fjerner 4 GB-begrensningen, støtter filer opp til 16 eksabyte og fungerer på tvers av plattformer. Ingen tilgangskontroll. Vanlig på SD-kort og USB-pinner som skal deles mellom Windows og macOS.

### ext4 (Fourth Extended Filesystem)

ext4 er standard filsystem i moderne Linux-distribusjoner som Ubuntu, Debian og RHEL.

**Kjennetegn:**
- **Journaling**: Tilsvarende NTFS — logger operasjoner for å sikre konsistens ved strømbrudd.
- **Inoder**: Hver fil har en inode som lagrer metadata (eier, gruppe, tillatelser, tidsstempler). Selve filnavnet er en peker til inoden.
- **Tillatelsesmodell**: rwx for eier, gruppe og andre (se [[linux-grunnleggende]]).
- **POSIX ACL**: For mer granulær kontroll, likt NTFS ACL.
- Støtter volumstørrelser opp til 1 eksabyte og filer opp til 16 TB.

### Sammenligning

| Egenskap | NTFS | FAT32 | exFAT | ext4 |
|---|---|---|---|---|
| OS | Windows | Alle | Windows/macOS | Linux |
| Maks filstørrelse | 8 PB (volum) | 4 GB | 16 EB | 16 TB |
| Tilgangskontroll | Ja (ACL) | Nei | Nei | Ja (rwx + POSIX ACL) |
| Journaling | Ja | Nei | Nei | Ja |
| Kryptering | Ja (EFS) | Nei | Nei | Via dm-crypt/LUKS |
| Kvoter | Ja | Nei | Nei | Ja |
| Bruksområde | Windows-systemer | USB/minnekort | USB/minnekort | Linux-systemer |

---

## Eksempel / lab

### Sette NTFS-tillatelser i Windows

1. Høyreklikk på mappen → **Egenskaper** → fanen **Sikkerhet**
2. Klikk **Rediger** → **Legg til** → skriv inn bruker- eller gruppenavn
3. Velg ønsket tillatelsesnivå og klikk **OK**

### Kontrollere arv

1. Egenskaper → Sikkerhet → **Avansert**
2. Under «Arvede fra» ser du hvilke tillatelser som er arvet
3. For å bryte arven: klikk **Deaktiver arv** — velg om eksisterende arvede tillatelser skal konverteres til eksplisitte eller fjernes

### Se filsystemtype i PowerShell

```powershell
Get-Volume
```

Eksempel på output:
```
DriveLetter FriendlyName FileSystemType SizeRemaining    Size
----------- ------------ -------------- -------------    ----
C           Windows      NTFS            45.2 GB   237.4 GB
D           Data         NTFS           120.0 GB   500.0 GB
```

---

## Quiz

<details><summary>Spørsmål 1: Hva er den største begrensningen med FAT32?</summary>

**Svar:** Maks filstørrelse er 4 GB − 1 byte (4 294 967 295 bytes). Filer på 4 GB eller større kan ikke lagres på et FAT32-volum.

</details>

<details><summary>Spørsmål 2: Hva er en ACL?</summary>

**Svar:** En Access Control List er en liste knyttet til en fil eller mappe som angir hvilke brukere og grupper som har hvilke tillatelser. NTFS bruker ACL for all tilgangskontroll.

</details>

<details><summary>Spørsmål 3: Hva skjer hvis NTFS-tillatelsene sier "Les" men delte tillatelser sier "Full kontroll"?</summary>

**Svar:** Brukeren får kun lesetilgang. Når NTFS og delte tillatelser kombineres, gjelder alltid den mest restriktive tillatelsen.

</details>

<details><summary>Spørsmål 4: Hva er journaling og hvorfor er det viktig?</summary>

**Svar:** Journaling er en mekanisme der filsystemet logger alle planlagte operasjoner før de utføres. Hvis systemet krasjer midt i en operasjon, kan journalen brukes til å gjenopprette filsystemets konsistens uten datatap.

</details>

<details><summary>Spørsmål 5: Hvilket filsystem er standard i Ubuntu Linux?</summary>

**Svar:** ext4 (Fourth Extended Filesystem).

</details>

---

## Flashcards

NTFS :: Standard Windows-filsystem med støtte for ACL, kvoter, journaling og kryptering
ACL :: Access Control List — liste over brukere/grupper og deres tillatelser på en fil eller mappe
Tillatelsesarv :: Mekanisme i NTFS der undermapper automatisk overtar tillatelsene til overordnet mappe
FAT32 :: Eldre filsystem uten tilgangskontroll; maks filstørrelse 4 GB − 1 byte (4 294 967 295 bytes)
exFAT :: Moderne FAT-basert filsystem uten 4 GB-begrensning; brukes på USB/SD
ext4 :: Standard Linux-filsystem med journaling, inoder og rwx-tillatelsesmodell
Inode :: Datastruktur i Linux-filsystemer som lagrer metadata om en fil (eier, tillatelser, tidsstempel)
Journaling :: Filsystemets transaksjonslogg som sikrer konsistens etter systemkrasj
Diskkvote :: Grense for hvor mye lagringsplass en bruker kan bruke på et volum
Full kontroll :: Høyeste NTFS-tillatelsesnivå — inkluderer rettigheten til å endre tillatelser og ta eierskap

---

## Ressurser

- [Microsoft Learn: NTFS-oversikt](https://learn.microsoft.com/en-us/windows-server/storage/file-server/ntfs-overview)
- [Microsoft Learn: Konfigurere delte tillatelser og NTFS-tillatelser](https://learn.microsoft.com/en-us/iis/web-hosting/configuring-servers-in-the-windows-web-platform/configuring-share-and-ntfs-permissions)
- [Ubuntu Community Wiki: Filrettigheter](https://help.ubuntu.com/community/FilePermissions)
