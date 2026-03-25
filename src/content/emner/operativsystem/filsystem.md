---
title: "Filsystemer"
emne: operativsystem
kompetansemaal:
  - km-04
kilder:
  - ndla
  - https://snl.no/filsystem
tags: []
flashcards: https://notebooklm.google.com/notebook/70aa7fff-78f3-4825-aeed-bc879a29770f
public: true
notebooklm: true
---

## Introduksjon

Et **filsystem** bestemmer hvordan data lagres og organiseres på en disk. For IT-driftsteknikere er valg av filsystem direkte knyttet til sikkerhet og tilgangskontroll — kun NTFS støtter for eksempel brukerbaserte tillatelser i Windows. Kunnskap om filsystemer er nødvendig for å administrere rettigheter, sette opp kvoter og forstå begrensningene på ulike lagringsmedier. NTFS-tillatelsene henger tett sammen med [[bruker-og-tilgangsstyring]], og Linux-filsystemet ext4 dekkes i sammenheng med [[linux-grunnleggende]]. Filsystemvalg er også relevant for [[backup-og-gjenoppretting]] siden ikke alle backup-løsninger støtter alle filsystemer.

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

### NTFS vs. delte tillatelser (Share Permissions)

Et vanlig misforståelsespunkt i brukerstøtte er forskjellen mellom **NTFS-tillatelser** og **delte tillatelser**:

- **NTFS-tillatelser** gjelder alltid — uansett om du aksesserer filen lokalt eller over nettverket. De er granulære (7 nivåer) og arves.
- **Delte tillatelser** gjelder kun når du aksesserer en ressurs over nettverk (via `\\server\delt`). De har kun tre nivåer: Les, Endre og Full kontroll.

Når begge er aktive, gjelder den **mest restriktive kombinasjonen**. Best practice er å sette delte tillatelser til «Full kontroll» for `Everyone` og styre all tilgang via NTFS-tillatelser. Dette gir full kontroll og unngår forvirring.

### POSIX ACL i Linux

Standard rwx-modellen i Linux gir tre sett tillatelser (eier, gruppe, andre). For mer granulær kontroll — for eksempel å gi en spesifikk bruker tilgang uten å endre gruppemedlemskap — brukes **POSIX ACL**:

```bash
# Gi brukeren elev02 lesetilgang til en mappe
setfacl -m u:elev02:r-x /felles/klasse2a

# Se gjeldende ACL
getfacl /felles/klasse2a
```

POSIX ACL er tilsvarende NTFS ACL, men brukes sjeldnere i praksis. Støttes av ext4 og de fleste moderne Linux-filsystemer.

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

### Sette NTFS-tillatelser med icacls (kommandolinje)

`icacls` er kommandolinjeverktøyet for NTFS-tillatelser i Windows:

```powershell
# Vis tillatelser for en mappe
icacls C:\Data\Salg

# Gi gruppen SG_Salg endre-tilgang rekursivt
icacls C:\Data\Salg /grant SG_Salg:(OI)(CI)M /T

# Fjern tilgang for en bruker
icacls C:\Data\Salg /remove elev01

# (OI) = object inherit, (CI) = container inherit, M = Modify
```

---

## Study guide

**Filsystemer** bestemmer hvordan data lagres, organiseres og beskyttes på en disk. Valget av filsystem er avgjørende for sikkerhet, ytelse og kompatibilitet.

De fire filsystemene du må kunne:
- **NTFS** — standard for Windows og Windows Server; støtter ACL, journaling, kvoter og kryptering (EFS). Eneste alternativ for Windows-servere med tilgangskontroll.
- **FAT32** — universelt kompatibelt; brukes på USB og minnekort. Ingen tilgangskontroll. Maks filstørrelse 4 GB — en klassisk feilkilde.
- **exFAT** — FAT32 uten 4 GB-begrensningen; brukes på større USB-enheter og SD-kort. Ingen tilgangskontroll.
- **ext4** — standard Linux-filsystem; støtter journaling, inoder, rwx-tillatelser og POSIX ACL.

Kritisk å forstå for NTFS:
- **ACL (Access Control List)** er listen over hvem som har tilgang til en fil/mappe og hva de kan gjøre
- **Tillatelsesarv** — undermapper arver tillatelser automatisk fra overordnet; kan deaktiveres per objekt
- **NTFS vs. Share Permissions**: begge gjelder ved nettverkstilgang — den mest restriktive vinner. Best practice: sett Share til «Full kontroll»/«Everyone» og styr via NTFS.
- Tillatelsesnivåene fra minst til mest: Les → List mappeinnhold → Les og kjør → Skriv → Endre → Full kontroll

For Linux: rwx-modellen gir tre tillatelsessett (eier, gruppe, andre). POSIX ACL gir mer granulær kontroll der standard rwx ikke er tilstrekkelig.

---

## FAQ

**Kan jeg flytte en disk med NTFS-tillatelser til en annen Windows-maskin og beholde tillatelsene?**
Tillatelsene flyttes med disken, men de er lagret som SID-er. Hvis du kobler disken til en maskin i et annet domene eller med andre lokale brukere, vil SID-ene ikke lenger matche noen bruker — og du vil typisk ikke ha tilgang. Du kan ta eierskap med `takeown` og `icacls` for å gjenopprette tilgang.

**Hva er forskjellen mellom journaling og backup?**
Journaling beskytter mot korrupsjon ved systemkrasj midt i en skriveoperasjon — det er ikke en backup. Journalen logger hva som var planlagt, slik at filsystemet kan fullføre eller rulle tilbake operasjonen ved neste oppstart. Journaling erstatter ikke [[backup-og-gjenoppretting]].

**Hvorfor kan jeg ikke kopiere en ISO-fil på 5 GB til en USB-pinne formatert som FAT32?**
FAT32 har en absolutt grense på 4 GB − 1 byte per fil. En fil på 5 GB overskrider denne grensen. Løsning: formater USB-pinnen som exFAT (behold kompatibilitet) eller NTFS (kun Windows uten ekstra drivere på Mac/Linux).

**Hva er en inode i Linux?**
En inode er en datastruktur som lagrer metadata om en fil: eier, gruppe, tillatelser, størrelse, tidsstempler og pekere til diskblokkene som inneholder selve dataene. Filnavnet er ikke lagret i inoden — det er en peker fra katalogen til inoden. To filer kan dele samme inode (hardlenke).

**Hva skjer med tillatelsene på en fil når jeg kopierer den vs. flytter den i NTFS?**
Kopiering til en annen mappe: filen arver tillatelsene til destinasjonsmappen. Flytting innenfor samme volum: filen beholder sine eksplisitte tillatelser. Flytting til et annet volum fungerer som kopiering — filen arver destinasjonsmappens tillatelser.

**Hva betyr «den mest restriktive kombinasjonen» av NTFS og Share Permissions?**
Eksempel: NTFS sier «Les», Share sier «Full kontroll». Brukeren får kun lesetilgang fordi NTFS-tillatelsen er mest restriktiv. Et annet eksempel: NTFS sier «Full kontroll», Share sier «Les» — brukeren får kun lesetilgang. Systemet tar laveste felles nevner.

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
POSIX ACL :: Utvidet tilgangskontroll i Linux utover standard rwx; gir per-bruker- og per-gruppe-tillatelser med `setfacl`/`getfacl`
icacls :: Windows kommandolinjeverktøy for å vise og endre NTFS-tillatelser
Share Permissions :: Tillatelser som kun gjelder ved nettverkstilgang til en delt ressurs; kombineres med NTFS-tillatelser (mest restriktive gjelder)
EFS :: Encrypting File System — NTFS-funksjonen for transparent filkryptering knyttet til brukerens sertifikat

---

## Ressurser

- [Microsoft Learn: NTFS-oversikt](https://learn.microsoft.com/en-us/windows-server/storage/file-server/ntfs-overview)
- [Microsoft Learn: Konfigurere delte tillatelser og NTFS-tillatelser](https://learn.microsoft.com/en-us/iis/web-hosting/configuring-servers-in-the-windows-web-platform/configuring-share-and-ntfs-permissions)
- [Ubuntu Community Wiki: Filrettigheter](https://help.ubuntu.com/community/FilePermissions)
- [Store Norske Leksikon: Filsystem](https://snl.no/filsystem)
