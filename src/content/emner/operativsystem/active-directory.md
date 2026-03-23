---
title: "Active Directory"
emne: operativsystem
kompetansemaal:
  - km-04
kilder:
  - ndla
  - https://learn.microsoft.com/nb-no/windows-server/identity/ad-ds/plan/active-directory-domain-services-logical-structure-design-guide
tags: []
flashcards: true
public: true
notebooklm: true
---

## Introduksjon

**Active Directory (AD)** er Microsofts katalogtjeneste og er hjertet i Windows-baserte bedriftsmiljøer. AD sentraliserer administrasjon av brukere, datamaskiner, grupper og policyer for hele organisasjonen. I stedet for å administrere hver maskin separat, styrer du alt fra én plass — domenekontrolleren.

I norske skoler og bedrifter er Active Directory Domain Services (AD DS) den vanligste løsningen for brukeradministrasjon. Denne artikkelen dekker struktur, komponenter og praktisk bruk. AD henger tett sammen med [[dns-og-dhcp]] — uten korrekt DNS fungerer ikke domenepålogging. Se også [[serverroller]] for oversikt over hvilke roller som installeres på en Windows Server, og [[bruker-og-tilgangsstyring]] for detaljer om rettigheter og grupper.

---

## Teori

### AD-hierarkiet

Active Directory er organisert som et hierarki med fire nivåer:

```
Skog (Forest)
└── Tre (Tree)
    └── Domene (Domain)
        └── Organisasjonsenhet (OU)
```

**Skog (Forest)**
Det øverste nivået i AD. En skog kan inneholde ett eller flere trær. Alle domener i samme skog deler et felles skjema (schema) og global katalog. `Enterprise Admins` har kontroll over hele skogen.

**Tre (Tree)**
En samling av domener med sammenhengende DNS-navnerom. Eksempel: `skole.no` med underdomenet `elever.skole.no`.

**Domene (Domain)**
Grunnenheten i AD. Et domene er en logisk gruppe av brukere, datamaskiner og ressurser under felles administrasjon. Identifiseres av DNS-navn, f.eks. `skole.local` eller `firma.no`.

**Organisasjonsenhet (OU)**
Logiske beholdere inni et domene. OU-er brukes til å:
- Gruppere objekter etter funksjon, avdeling eller geografi
- Delegere administrasjonstilgang (f.eks. la IT-avdelingen administrere kun sin OU)
- Knytte gruppepolicyer (GPO-er) til spesifikke brukere eller maskiner

Typisk OU-struktur:
```
skole.local
├── OU=Brukere
│   ├── OU=Lærere
│   └── OU=Elever
├── OU=Datamaskiner
│   ├── OU=Klasserom
│   └── OU=Administrasjon
└── OU=Grupper
```

### Domenekontroller (DC)

En **domenekontroller** er en server med AD DS installert. DC-en:
- Autentiserer alle pålogginger i domenet
- Lagrer og replikerer AD-databasen (`ntds.dit`)
- Kjører DNS (vanligvis) og Kerberos-autentiseringstjenesten

**Beste praksis**: Ha minst to domenekontrollere. Hvis én DC faller ut, overtar den andre uten nedetid.

Den første DC-en i et domene kalles også den første domeneopprettende kontrolleren og holder spesielle FSMO-roller (*Flexible Single Master Operation*).

### LDAP

**LDAP** (Lightweight Directory Access Protocol) er protokollen AD bruker for å gi tilgang til katalogdata. Når du søker etter en bruker i AD eller et program autentiserer seg mot AD, brukes LDAP. Kryptert LDAP kalles LDAPS (LDAP over SSL/TLS, port 636).

### Kerberos-autentisering

AD bruker **Kerberos** som standard autentiseringsprotokoll (i stedet for det eldre NTLM).

Kort forklart:
1. Brukeren logger inn og sender brukernavnet til DC-en
2. DC-en (KDC — Key Distribution Center) sender tilbake en kryptert **TGT** (Ticket Granting Ticket)
3. Når brukeren vil aksessere en ressurs, bruker klienten TGT-en til å be om en **tjenesteticket**
4. Tjenesteticket presenteres for ressursen — uten at passordet sendes over nettverket

Kerberos er sikrere enn NTLM fordi passordet aldri sendes, kun krypterte billetter med begrenset levetid.

### Active Directory Users and Computers (ADUC)

**ADUC** (`dsa.msc`) er det grafiske administrasjonsverktøyet for AD. Her kan du:
- Opprette, redigere og slette brukerkontoer
- Opprette og administrere grupper
- Koble datamaskiner til OU-er
- Tilbakestille passord og låse opp kontoer
- Opprette og flytte OU-er

Standardbeholderen `Users` inneholder de innebygde kontoene: `Administrator`, `Guest` og `KRBTGT`. Det er beste praksis å opprette egne OU-er og flytte kontoer dit.

### Gruppepolicy (GPO)

**Group Policy Objects (GPO)** er en av de kraftigste funksjonene i AD. En GPO er et sett med innstillinger som automatisk distribueres til brukere og maskiner i en OU, et domene eller en site.

GPO-er kan styre:
- Passordpolicyer (lengde, kompleksitet, levetid)
- Sikkerhetsinnstillinger (deaktiver USB, lås skjerm etter X minutter)
- Programvaredistribusjon (installer MSI-pakker automatisk)
- Mappetilordning (koble til nettverksdrev ved pålogging)
- Skrivebordsinnstillinger (bakgrunn, startmeny)

**Eksempel — Nekte pålogging fra Domain Admins på klientmaskiner:**
1. Åpne Group Policy Management Console (GPMC)
2. Opprett ny GPO på OU=Datamaskiner
3. Naviger til: `Computer Configuration → Windows Settings → Security Settings → Local Policies → User Rights Assignment`
4. Rediger `Deny log on locally` — legg til `Domain Admins`

GPO-er arves gjennom hierarkiet (skog → domene → OU). En GPO koblet til en OU overstyrer en GPO på domenivå.

### Global katalog

**Global Catalog (GC)** er en distribuert lagringsplass som inneholder en kopi av alle objekter i hele AD-skogen — ikke bare lokalt domene. Den brukes til:
- Hurtige søk på tvers av domener (f.eks. å finne en bruker i et annet domene)
- Pålogging med UPN-er (User Principal Name, f.eks. `bruker@firma.no`)
- Universelle gruppemedlemskap

Minst én domenekontroller bør ha Global Catalog-rollen aktivert. I et single-domene-miljø (som de fleste skoler) er dette automatisk.

### Planlegging og navnestandard

God planlegging er avgjørende før man setter opp AD. Viktige beslutninger:
- **Domenenavn**: Bruk et internt navn (f.eks. `firma.local`) eller subdomene av et eksternt domene (`intern.firma.no`). Unngå `.local` i nye oppsett — det kan kollidere med mDNS.
- **Navnestandard for brukere**: Konsistent navnekonvensjon (`fornavn.etternavn`, `f.etternavn` e.l.) forenkler administrasjon og scripting med [[powershell-grunnleggende]].
- **OU-struktur**: Design OU-hierarkiet basert på organisasjonsstruktur eller geografisk plassering — ikke etter roller. OU-strukturen bør dokumenteres i [[dokumentasjon-og-planlegging]].

### Domenekobling av klientmaskiner

Når en Windows-klient kobles til domenet:
1. Maskinen opprettes som et objekt i AD (under `Computers` eller angitt OU)
2. Klienten begynner å motta GPO-er fra domenet
3. Domenebrukere kan logge inn på maskinen
4. Brukerens hjemmeprofil opprettes lokalt ved første pålogging

---

## Eksempel / lab

### Windows Server-prosjekt: 7-dagers klasseromslab (Konnekt AS)

> **Kilde:** Klasseromsnotater (2ITA)
>
> I undervisningen jobber elevene med et realistisk caseprosjekt der de setter opp en komplett Windows Server-løsning for fiktiv bedrift Konnekt AS. Prosjektet er strukturert over 7 arbeidsdager:
>
> **Dag 1 – Installasjon og IP-plan:** Elevene designer en IP-plan for `10.0.10.0/24`-nettverket (DC01 fast adresse, klient W11-KLIENT01, gateway og DHCP-pool). Windows Server 2022/2025 installeres i VirtualBox med to nettverkskort: ett internt (Internal Network) og ett bridged (for Windows Update). Snapshot tas etter ren installasjon — "Ren installasjon - Før AD".
>
> **Dag 2 – Domene og AD DS:** AD DS-rollen installeres og serveren promoteres til domenekontroller for `konnekt.local`. Klientmaskinen meldes inn i domenet etter at DNS pekes mot DC01. OU-struktur opprettes i ADUC etter avdelingsstruktur.
>
> **Dag 3 – Brukere, grupper og filserver:** Testbrukere opprettes med navnestandard `fornavn.etternavn`. Sikkerhetsgrupper per avdeling (`SG_SalgMarked_Medlemmer`, `SG_AlleAnsatte`) opprettes. Filserver med mappe `C:\Data` og undermapper per avdeling settes opp — delings-rettigheter åpne for `Everyone`, NTFS-rettigheter strenge per sikkerhetsgruppe.
>
> **Dag 4 – Group Policy (GPO):** Nettverksdrev kobles automatisk via GPO (F: for felles, avdelings-stasjon per gruppe med sikkerhetsfiltrering). Verifisering med `gpupdate /force` og `gpresult /r`.
>
> **Dag 5 – Sikkerhetsherdning:** Default Domain Policy justeres med passordpolicy (min. 12 tegn, kompleksitetskrav). GPO for automatisk skjermlås etter 600 sekunder. Tilgang til Kontrollpanelet blokkeres for vanlige brukere.

### Opprette en OU i ADUC

1. Åpne **Active Directory Users and Computers** (`dsa.msc`)
2. Høyreklikk på domenenavnet (f.eks. `skole.local`)
3. Velg **New → Organizational Unit**
4. Gi OU-en navn, f.eks. `Elever`
5. La «Protect container from accidental deletion» være avkrysset
6. Klikk **OK**

### Opprette en domenekonto i ADUC

1. Naviger til OU-en der brukeren skal opprettes (f.eks. `Elever`)
2. Høyreklikk → **New → User**
3. Fyll inn: Fornavn, Etternavn, Påloggingsnavn (f.eks. `elev01@skole.local`)
4. Sett passord og velg innstillinger (f.eks. «Bruker må endre passord ved neste pålogging»)
5. Klikk **Finish**

### Opprette bruker med PowerShell (AD-modul)

```powershell
# Importer AD-modulen (krever RSAT)
Import-Module ActiveDirectory

# Opprett domenekonto
New-ADUser `
    -Name "Elev Elevsen" `
    -GivenName "Elev" `
    -Surname "Elevsen" `
    -SamAccountName "elev01" `
    -UserPrincipalName "elev01@skole.local" `
    -Path "OU=Elever,DC=skole,DC=local" `
    -AccountPassword (ConvertTo-SecureString "P@ssw0rd1" -AsPlainText -Force) `
    -Enabled $true `
    -ChangePasswordAtLogon $true
```

### Opprette GPO og koble den til en OU

```powershell
# Opprett ny GPO
New-GPO -Name "Elev-policy"

# Koble GPO til OU
New-GPLink -Name "Elev-policy" -Target "OU=Elever,DC=skole,DC=local"

# Tvinge oppdatering av policyer på klienten
gpupdate /force
```

---

## Study guide

**Active Directory** er Microsofts sentraliserte katalogtjeneste for Windows-domener. Den er organisert i et hierarki: **Skog → Tre → Domene → OU**. En **domenekontroller (DC)** er serveren som kjører AD DS-rollen og autentiserer alle pålogginger.

Kjernekomponenter du må kjenne:
- **ADUC** (`dsa.msc`) — det grafiske verktøyet for å opprette og administrere brukere, grupper, datamaskiner og OU-er
- **GPO (Group Policy Object)** — automatiske innstillinger som distribueres til brukere og maskiner i en OU; arver hierarkisk, nærmeste OU vinner
- **Kerberos** — autentiseringsprotokollen AD bruker; passordet sendes aldri over nettverket, kun krypterte billetter (TGT)
- **LDAP** — protokollen programmer bruker til å søke i og oppdatere AD-katalogen
- **Global katalog** — tverr-domene søketjeneste; nødvendig for UPN-pålogging

Viktige sammenhenger:
- AD er avhengig av **DNS** — klienten må kunne slå opp domenekontrolleren via DNS for å logge inn
- **FSMO-roller** er spesialiserte DC-oppgaver som kun én DC kan ha om gangen (f.eks. PDC Emulator, RID Master)
- Tilgangsstyring gjøres via **sikkerhetsgrupper** koblet til NTFS-rettigheter — aldri tildel tilgang direkte til enkeltbrukere

Beste praksis:
- Ha alltid minst to domenekontrollere (redundans)
- Gi administratorer to kontoer: en daglig brukerkonto og en separat adminkonto
- Bruk GPO til å håndheve passordpolicyer og sikkerhetskrav automatisk

---

## FAQ

**Hva er forskjellen mellom AD DS og Azure AD?**
AD DS er den klassiske on-premises katalogtjenesten som krever en Windows Server og domenekontroller i eget nettverk. Azure AD (nå kalt Microsoft Entra ID) er Microsofts skybaserte katalogtjeneste for Microsoft 365 og skytjenester. De kan synkroniseres via Azure AD Connect.

**Kan en bruker logge inn på hvilken som helst maskin i domenet?**
Ja — det er hele poenget med et domene. Domenebrukeren eksisterer i AD, ikke på den enkelte maskinen. GPO-er kan likevel begrense hvilke brukere som kan logge inn på bestemte maskiner.

**Hva skjer hvis domenekontrolleren er nede?**
Med én enkelt DC vil ingen kunne logge inn med domenekontoer. Allerede innloggede brukere kan fortsette å jobbe lokalt en stund (cachen). Derfor bør man alltid ha minst to DC-er.

**Hva er forskjellen mellom Domain Admins og Enterprise Admins?**
Domain Admins har full kontroll innenfor ett domene. Enterprise Admins har kontroll over hele AD-skogen (alle domener). Enterprise Admins bør kun brukes ved skog-nivå-operasjoner.

**Hvorfor bør jeg bruke grupper i stedet for å tildele tilgang direkte til brukere?**
Med grupper trenger du bare å endre gruppemedlemskap når en bruker bytter rolle — ikke gå gjennom alle ressurser manuelt. Det er enklere å revidere (hvem har tilgang til hva) og reduserer feilrisiko.

**Hva er FSMO-roller og hvorfor er de viktige?**
Flexible Single Master Operation-roller er spesialiserte AD-oppgaver som bare én DC kan utføre om gangen (f.eks. å utstede nye SID-er). Hvis DC-en med en FSMO-rolle faller ut, kan visse operasjoner stoppe inntil rollen overføres til en annen DC.

**Kan jeg endre domenenavn etter installasjon?**
Teknisk sett ja, men det er komplisert og risikabelt. Alle GPO-er, profiler og tjenestekoblinger er knyttet til domenenavnet. Det anbefales å planlegge domenenavn grundig før installasjon.

---

## Quiz

<details><summary>Spørsmål 1: Hva er en domenekontroller?</summary>

**Svar:** En domenekontroller er en server med Active Directory Domain Services (AD DS) installert. Den autentiserer alle pålogginger i domenet, lagrer AD-databasen og distribuerer gruppepolicyer.

</details>

<details><summary>Spørsmål 2: Hva er forskjellen mellom en OU og en sikkerhetsgruppe?</summary>

**Svar:** En OU (organisasjonsenhet) er en logisk beholder for å organisere objekter i AD og knytte GPO-er til. En sikkerhetsgruppe samler brukere for å tildele dem felles tilganger og rettigheter. OU-er brukes til administrasjon; grupper brukes til tilgangskontroll.

</details>

<details><summary>Spørsmål 3: Hva er en GPO og hva kan den brukes til?</summary>

**Svar:** En Group Policy Object er et sett med innstillinger som automatisk distribueres til brukere og maskiner i AD. Den kan styre passordpolicyer, sikkerhetsinnstillinger, programvaredistribusjon, nettverksdrev og mye mer.

</details>

<details><summary>Spørsmål 4: Hvorfor bør man ha minst to domenekontrollere?</summary>

**Svar:** For redundans. Hvis én domenekontroller faller ut, kan den andre fortsette å autentisere brukere uten nedetid. Med kun én DC vil hele domenet slutte å fungere ved et havari.

</details>

<details><summary>Spørsmål 5: Hva er LDAP?</summary>

**Svar:** Lightweight Directory Access Protocol — protokollen som brukes for å spørre mot og oppdatere katalogdata i Active Directory.

</details>

---

## Flashcards

Active Directory (AD) :: Microsofts katalogtjeneste for sentralisert administrasjon av brukere, maskiner og policyer
Domenekontroller (DC) :: Server med AD DS installert som autentiserer alle pålogginger i domenet
Organisasjonsenhet (OU) :: Logisk beholder i AD for å organisere objekter og knytte GPO-er til
GPO :: Group Policy Object — sett med innstillinger som distribueres automatisk til brukere og maskiner i AD
ADUC :: Active Directory Users and Computers — grafisk verktøy for å administrere AD-objekter
Skog (Forest) :: Øverste nivå i AD-hierarkiet; samling av trær med felles skjema og global katalog
Domene :: Grunnenheten i AD — logisk gruppe av brukere og maskiner under felles administrasjon
LDAP :: Lightweight Directory Access Protocol — protokoll for å søke i og oppdatere AD-katalogen
Kerberos :: Autentiseringsprotokoll AD bruker; basert på krypterte billetter, passordet sendes aldri over nettverket
TGT :: Ticket Granting Ticket — Kerberos-billett brukt til å be om tilgang til tjenester uten nytt passord
FSMO :: Flexible Single Master Operation — spesielle AD-roller som kun én DC kan inneha om gangen
gpupdate /force :: Kommando for å tvinge umiddelbar oppdatering av gruppepolicyer på en klient
Global katalog (GC) :: Distribuert lagring med kopi av alle objekter i AD-skogen; muliggjør tverr-domene søk og UPN-pålogging
RBAC :: Rollebasert tilgangsstyring — rettigheter tildeles basert på brukerens rolle, ikke som enkeltpersonstillatelser
Navnestandard :: Konsistent konvensjon for brukernavn i AD (f.eks. fornavn.etternavn) som forenkler administrasjon og scripting

---

## Ressurser

- [Microsoft Learn: AD-standardkontoer](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-default-user-accounts)
- [Microsoft Learn: AD-sikkerhetsgrupper](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups)
- [Microsoft Learn: Active Directory Users and Computers](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc754217(v=ws.11))
- [NDLA: Datalab med Windows Server og generisk nettverk](https://ndla.no/nb/r/driftsstotte-im-itk-vg2/datalab-med-windows-server-og-generisk-nettverk/6fbbe0f727)
- [Microsoft Learn: Logisk strukturdesign for AD DS](https://learn.microsoft.com/nb-no/windows-server/identity/ad-ds/plan/active-directory-domain-services-logical-structure-design-guide)
