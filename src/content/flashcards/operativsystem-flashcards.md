# Systemadministrasjon lærekort

## Card 1

***Q:**Hva er Microsofts sentrale katalogtjeneste som lagrer informasjon om nettverksobjekter som brukerkontoer og
*datamaskiner?

**A:**Active Directory Domain Services (AD DS).

---

## Card 2

**Q:**Hva kalles en server som kjører Active Directory Domain Services og autentiserer pålogginger i et domene?

**A:**Domenekontroller (DC).

---

## Card 3

**Q:**Hvilken logisk beholder i Active Directory brukes for å organisere objekter og knytte til gruppepolicyer (GPO)?

**A:**Organisasjonsenhet (OU).

---

## Card 4

**Q:**Hva er det øverste nivået i Active Directory-hierarkiet som kan inneholde flere trær?

**A:**Skog (Forest).

---

## Card 5

**Q:**I hvilken lokal database lagres brukernavn og passord for lokale brukerkontoer på en Windows-maskin?

**A:**SAM (Security Account Manager).

---

## Card 6

**Q:**Hva oppnår man med mekanismen Single-Sign-On (SSO)?

**A:**At en bruker kun trenger å logge inn én gang for å få tilgang til alle ressurser i domenet.

---

## Card 7

**Q:**Hva er forskjellen på autentisering og autorisasjon?

**A:**Autentisering bekrefter brukerens identitet, mens autorisasjon avgjør hva brukeren har lov til å gjøre.

---

## Card 8

**Q:**Hvilken protokoll bruker Active Directory som standard for sikker autentisering basert på billetter (tickets)?

**A:**Kerberos.

---

## Card 9

**Q:**Hva er standardprotokollen for å gjøre oppslag og spørringer mot katalogdata i Active Directory?

**A:**LDAP (Lightweight Directory Access Protocol).

---

## Card 10

**Q:**Hvilken innebygd Windows-konto har full kontroll over det lokale systemet og kan ikke slettes?

**A:**Administrator.

---

## Card 11

**Q:**Hvilken unik numerisk identifikator tildeler Windows til hver brukerkonto for intern bruk i tilgangslister?

**A:**SID (Security Identifier).

---

## Card 12

**Q:**Hva skjer dersom du sletter en brukerkonto og oppretter en ny med nøyaktig samme navn?

**A:**Den nye kontoen får en ny SID og mister alle tidligere tilganger.

---

## Card 13

**Q:**Hva innebærer prinsippet om 'minste privilegium' (Least Privilege)?

**A:**At brukere kun skal ha de rettighetene som er absolutt nødvendige for å utføre jobben sin.

---

## Card 14

**Q:**Hvilken Windows-mekanisme hindrer programmer i å kjøre med administrative rettigheter uten brukerens godkjenning?

**A:**User Account Control (UAC).

---

## Card 15

**Q:**Hvilken type brukerprofil lagres på en server og lastes ned til enhver maskin brukeren logger på i domenet?

**A:**Vandrende brukerprofil (Roaming Profile).

---

## Card 16

**Q:**Hva kjennetegner en påtvunget brukerprofil (Mandatory Profile)?

**A:**At endringer brukeren gjør i profilen ikke lagres når de logger av.

---

## Card 17

**Q:**Hva er en 'Hjemmekatalog' (Home Folder) i et Windows-nettverk?

**A:**En privat mappe på en filtjener der brukeren har alle rettigheter til egne filer.

---

## Card 18

**Q:**Hvilket grafisk verktøy brukes primært for å administrere brukere, grupper og datamaskiner i Active Directory?

**A:**Active Directory Users and Computers (ADUC).

---

## Card 19

**Q:**Hvilken kommando i Windows kan tvinge frem en umiddelbar oppdatering av gruppepolicyer (GPO)?

**A:**gpupdate /force

---

## Card 20

**Q:**Hva er standard filsystem for moderne Windows-versjoner som støtter tilgangskontroll (ACL)?

**A:**NTFS (New Technology File System).

---

## Card 21

**Q:**Hva er den største begrensningen for filstørrelse på et FAT32-filsystem?

**A:**En enkeltfil kan maksimalt være $4$ GB minus $1$ byte.

---

## Card 22

**Q:**Hvilket filsystem er designet for flash-lagring og fjerner 4 GB-begrensningen uten å ha kompleksiteten til NTFS?

**A:**exFAT.

---

## Card 23

**Q:**Hva skjer når en bruker aksesserer en fil over nettverk og det er konflikt mellom Share- og NTFS-tillatelser?

**A:**Den mest restriktive tillatelsen blir gjeldende.

---

## Card 24

**Q:**Hvilken NTFS-funksjon gjør at undermapper automatisk får de samme tillatelsene som foreldremappen?

**A:**Tillatelsesarv (Inheritance).

---

## Card 25

**Q:**Hva er hensikten med 'Journaling' i et filsystem som NTFS eller ext4?

**A:**Å logge filoperasjoner for å sikre konsistens og rask gjenoppretting etter et systemkrasj.

---

## Card 26

**Q:**Hva er navnet på superbrukeren i Linux som har ubegrensede rettigheter til systemet?

**A:**root.

---

## Card 27

**Q:**Hvilken numerisk UID har root-brukeren i Linux?

**A:**UID $0$.

---

## Card 28

**Q:**Hvilken Linux-kommando lar en vanlig bruker utføre administrative oppgaver med root-rettigheter?

**A:**sudo.

---

## Card 29

**Q:**Hva representerer bokstavene 'rwx' i Linux-tillatelsessystemet?

**A:**Read (lese), Write (skrive) og Execute (kjøre).

---

## Card 30

**Q:**I Linux-tillatelser, hvilken tallverdi tilsvarer 'Read' ($r$)?

**A:**Tallet $4$.

---

## Card 31

**Q:**I Linux-tillatelser, hvilken tallverdi tilsvarer 'Write' ($w$)?

**A:**Tallet $2$.

---

## Card 32

**Q:**I Linux-tillatelser, hvilken tallverdi tilsvarer 'Execute' ($x$)?

**A:**Tallet $1$.

---

## Card 33

**Q:**Hvilke tillatelser gir oktaltallet $755$ på en Linux-fil?

**A:**Eier har full tilgang (rwx), mens gruppe og andre kan lese og kjøre (r-x).

---

## Card 34

**Q:**Hvilken Linux-kommando brukes for å endre rettigheter på filer og mapper?

**A:**chmod.

---

## Card 35

**Q:**Hvilken Linux-kommando brukes for å endre eier av en fil?

**A:**chown.

---

## Card 36

**Q:**I hvilken Linux-katalog finner man systemets konfigurasjonsfiler?

**A:**/etc.

---

## Card 37

**Q:**Hvilken Linux-fil inneholder oversikt over brukerkontoer, men ikke de krypterte passordene?

**A:**/etc/passwd.

---

## Card 38

**Q:**Hvilken Linux-fil er kun lesbar for root og lagrer brukernes krypterte passord?

**A:**/etc/shadow.

---

## Card 39

**Q:**Hva er hensikten med 'Sticky Bit' på en delt Linux-mappe som /tmp?

**A:**Den hindrer brukere i å slette eller gi nytt navn til filer de ikke eier selv.

---

## Card 40

**Q:**Hva kalles de tre kategoriene tillatelser settes for i Linux?

**A:**User (u), Group (g) og Others (o).

---

## Card 41

**Q:**Hvilken Linux-katalog inneholder brukernes personlige hjemmemapper?

**A:**/home.

---

## Card 42

**Q:**Hva er standard filsystem for de fleste moderne Linux-distribusjoner?

**A:**ext4.

---

## Card 43

***Q:**Hvilken Windows-tjeneste brukes for å knytte domenenavn til IP-adresser, noe som er kritisk for at Active
*Directory skal fungere?

**A:**DNS (Domain Name System).

---

## Card 44

**Q:**Hva er en 'Global Katalog' (Global Catalog) i et Active Directory-nettverk?

**A:**En database som inneholder en delmengde av informasjonen om alle objekter i hele skogen.

---

## Card 45

**Q:**Hvilken parameter må brukes med useradd i Linux for å automatisk opprette en hjemmemappe for den nye brukeren?

**A:**-m.

---

## Card 46

**Q:**Hvilken Linux-kommando brukes for å sette eller endre passordet til en bruker?

**A:**passwd.

---

## Card 47

**Q:**Hva skjer dersom man bruker usermod -G uten flagget -a når man legger en bruker til i en ny gruppe i Linux?

**A:**Brukeren fjernes fra alle andre grupper de var medlem av.

---

## Card 48

**Q:**Hvilken Linux-katalog lagrer systemlogger som auth.log og syslog?

**A:**/var/log.

---

## Card 49

***Q:**Hva kalles programvaren som lar deg kjøre flere virtuelle operativsystemer på én fysisk maskin (f.eks.
*VirtualBox)?

**A:**Hypervisor.

---

## Card 50

**Q:**Hva er den viktigste forskjellen på NTFS-tillatelser og Share-tillatelser?

**A:**NTFS-tillatelser gjelder både lokalt og over nettverk, mens Share-tillatelser kun gjelder over nettverk.

---

## Card 51

***Q:**Hvilken Linux-funksjon gjør at et program kjøres med rettighetene til fileieren i stedet for brukeren som starter
*det?

**A:**SUID (Set User ID).

---

## Card 52

**Q:**Hva er fordelen med å bruke sikkerhetsgrupper i Active Directory fremfor å tildele rettigheter til enkeltbrukere?

**A:**Det forenkler administrasjonen og reduserer risikoen for feil ved endring av personell.

---

## Card 53

**Q:**Hva lagres i en 'Inode' i et Linux-filsystem?

**A:**Metadata om en fil, som eier, rettigheter og pekere til selve dataen på disken.

---

## Card 54

**Q:**Hvorfor bør man deaktivere fremfor å slette en brukerkonto når en ansatt slutter i en bedrift?

**A:**For å bevare tilganger og eierskap til data dersom kontoen må gjenåpnes senere.

---

## Card 55

**Q:**Hva kreves for at en Windows-klient skal kunne logge på med en domenekonto?

**A:**Klientmaskinen må være meldt inn i (være medlem av) domenet.

---

## Card 56

**Q:**Hva er hensikten med en 'Logon Script'?

**A:**En kommandofil som kjøres automatisk ved pålogging for å sette opp f.eks. nettverksstasjoner.

---

## Card 57

**Q:**Hvilket filsystem har ingen innebygd støtte for tilgangskontroll og brukes ofte på USB-pinner?

**A:**FAT32.

---

## Card 58

**Q:**Hva er den anbefalte maksimale lengden for et NetBIOS-brukernavn (pre-Windows 2000)?

**A:**$20$ tegn.

---

## Card 59

**Q:**Hva betyr flagget -R når man bruker chmod-kommandoen i Linux?

**A:**At rettighetsendringen gjøres rekursivt for alle filer og undermapper.

---

## Card 60

**Q:**Hvilket Linux-verktøy bør alltid brukes for å redigere /etc/sudoers-filen for å unngå syntaksfeil?

**A:**visudo.

---

## Card 61

**Q:**Hva er forskjellen mellom et 'Tre' (Tree) og en 'Skog' (Forest) i Active Directory?

**A:**Et tre er domener med sammenhengende navnerom, mens en skog er en samling av ett eller flere trær.

---

## Card 62

**Q:**Hva er de tre standard tillatelsesnivåene for Share-tillatelser i Windows?

**A:**Les (Read), Endre (Change) og Full kontroll (Full Control).

---

## Card 63

**Q:**Hvorfor er det 'Beste praksis' å ha minst to domenekontrollere i et nettverk?

**A:**For å sikre redundans og unngå at hele domenet stopper opp dersom én server svikter.

---

## Card 64

**Q:**Hvilken Linux-kommando viser hvilke grupper en spesifikk bruker er medlem av?

**A:**groups eller id.

---

## Card 65

**Q:**I NTFS, hva innebærer tillatelsen 'Endre' (Modify) sammenlignet med 'Skriv' (Write)?

**A:**'Endre' gir i tillegg rettighet til å slette filer og mapper.

---

## Card 66

***Q:**Hvilket verktøy brukes i Windows for å administrere lokale brukere og grupper på en maskin som ikke er en
*domenekontroller?

**A:**Computer Management (lusrmgr.msc).

---

## Card 67

***Q:**Hva skjer dersom en bruker er medlem av to grupper der den ene har NTFS 'Allow' og den andre har 'Deny' til samme
*mappe?

**A:**'Deny' overstyrer alltid 'Allow'.

---

## Card 68

**Q:**Hvilken Linux-kommando brukes for å slette en brukerkonto?

**A:**userdel.

---

## Card 69

**Q:**Hvilken type gruppe i Active Directory brukes primært for å tildele tilgang til ressurser?

**A:**Sikkerhetsgruppe (Security Group).

---
