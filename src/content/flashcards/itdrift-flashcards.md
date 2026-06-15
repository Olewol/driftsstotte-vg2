# IT-drift flashcards

## Card 1

**Q:**Hva er den grunnleggende definisjonen på IT-drift?

**A:**Forvaltning og vedlikehold som sikrer at IT-systemer og infrastruktur fungerer stabilt over tid.

---

## Card 2

**Q:**Hvilken driftsmodell kjennetegnes ved at virksomheten eier og drifter sin egen fysiske maskinvare lokalt?

**A:**On-premise (lokal infrastruktur).

---

## Card 3

**Q:**Hva kalles en modell som kombinerer lokal infrastruktur (on-premise) med offentlige skytjenester?

**A:**Hybrid sky.

---

## Card 4

**Q:**Hva står forkortelsen IaaS for i skysammenheng?

**A:**Infrastructure as a Service (Infrastruktur som tjeneste).

---

## Card 5

**Q:**Hva er kundens hovedansvar i en IaaS-modell?

**A:**Installasjon og vedlikehold av operativsystem, applikasjoner og data.

---

## Card 6

**Q:**Hvilken skymodell lar utviklere fokusere på applikasjonskoding uten å administrere underliggende servere eller operativsystemer?

**A:**PaaS (Platform as a Service).

---

## Card 7

**Q:**Hva kjennetegner SaaS (Software as a Service)?

**A:**Ferdig programvare levert over internett der leverandøren har alt driftsansvar.

---

## Card 8

**Q:**Hvem har alltid ansvaret for egne data i 'Shared Responsibility Model'?

**A:**Kunden (virksomheten).

---

## Card 9

**Q:**Hva er hovedformålet med FinOps i IT-drift?

**A:**Å forstå, kontrollere og optimalisere kostnader ved bruk av skytjenester.

---

## Card 10

**Q:**Nevn de tre kravene i 3-2-1-regelen for backup.

**A:**Minst 3 kopier av data, lagret på 2 ulike medietyper, med 1 kopi lagret offsite.

---

## Card 11

**Q:**I den moderne 3-2-1-1-0 regelen, hva står den ekstra eneren (+1) for?

**A:**Én immutable (uforanderlig) eller air-gapped kopi som beskytter mot ransomware.

---

## Card 12

**Q:**Hva definerer begrepet RPO (Recovery Point Objective)?

**A:**Den maksimale mengden datatap en virksomhet kan akseptere, målt i tid.

---

## Card 13

**Q:**Hva måles med RTO (Recovery Time Objective)?

**A:**Hvor lang tid det maksimalt kan ta å gjenopprette systemene etter en hendelse.

---

## Card 14

**Q:**Hvilken backup-type tar kun kopi av data som er endret siden forrige backup, uansett type?

**A:**Inkrementell backup.

---

## Card 15

**Q:**Hva er forskjellen på en differensiell backup og en inkrementell backup?

**A:**Differensiell tar endringer siden siste fulle backup, mens inkrementell tar endringer siden enhver forrige backup.

---

## Card 16

**Q:**Hva betyr det at en backup er 'immutable'?

**A:**Dataene er låst og kan ikke endres eller slettes i en definert periode.

---

## Card 17

**Q:**Hva kalles en backup som er fysisk isolert fra nettverket?

**A:**Air-gapped backup.

---

## Card 18

**Q:**Hva er den billigste Disaster Recovery-strategien med lengst gjenopprettingstid?

**A:**Cold standby.

---

## Card 19

**Q:**Hvorfor er regelmessig gjenopprettingstesting kritisk for en backup-strategi?

**A:**Det verifiserer at dataene faktisk kan brukes og at systemet fungerer etter gjenoppretting.

---

## Card 20

**Q:**Hva måler indikatoren PUE (Power Usage Effectiveness)?

**A:**Energieffektiviteten i et datasenter ved å sammenligne totalt strømforbruk med strømmen brukt av IT-utstyret.

---

## Card 21

**Q:**Formel: Hvordan beregnes PUE?

**A:**$PUE = \frac{\text{Total tilført energi}}{\text{Energi brukt av IT-utstyr}}$

---

## Card 22

**Q:**Hva betegnes som 'mørke data' (Dark Data)?

**A:**Lagret informasjon som aldri brukes, men som likevel krever strøm til lagring og kjøling.

---

## Card 23

**Q:**Hvor stor andel av en bærbar PCs totale karbonavtrykk skjer vanligvis under produksjonsfasen?

**A:**Omtrent 70 til 80 prosent.

---

## Card 24

**Q:**Hva er det mest effektive tiltaket for å redusere miljøavtrykket til IT-utstyr?

**A:**Å forlenge levetiden på utstyret slik at det brukes i flere år.

---

## Card 25

**Q:**Hva innebærer konseptet 'Sirkulær IT'?

**A:**En driftsmodell som prioriterer gjenbruk, reparasjon og resirkulering fremfor kjøp og kast.

---

## Card 26

**Q:**Hva kalles systemet som gjenvinner varme fra datasentre til for eksempel fjernvarme?

**A:**Varmegjenvinning (overskuddsvarme).

---

## Card 27

**Q:**Hva er hovedformålet med en driftslogg eller endringslogg?

**A:**Å ha en kronologisk oversikt over alle endringer for å forenkle feilsøking og sikre kontinuitet.

---

## Card 28

**Q:**Hva er en CMDB (Configuration Management Database)?

**A:**Et register som inneholder oversikt over all IT-infrastruktur, konfigurasjoner og relasjoner mellom enheter.

---

## Card 29

**Q:**Hvilket rammeverk beskriver beste praksis for IT-drift, inkludert endringstyring?

**A:**ITIL (IT Infrastructure Library).

---

## Card 30

**Q:**Hva er formålet med en ROS-analyse i planleggingsfasen?

**A:**Å kartlegge mulige risikoer og sårbarheter for å vurdere sannsynlighet og konsekvens av feil.

---

## Card 31

**Q:**Hva bør alltid være inkludert i en plan for endringstyring dersom noe går galt?

**A:**En rollback-plan (tilbakerullingsplan).

---

## Card 32

**Q:**Hva kalles lagring som er koblet direkte til én enkelt server via for eksempel USB eller SATA?

**A:**DAS (Direct Attached Storage).

---

## Card 33

**Q:**Hva er forskjellen på NAS og SAN?

**A:**NAS er en fildelingsenhet på nettverket, mens SAN er et dedikert høyhastighetsnettverk for blokklagring.

---

## Card 34

**Q:**Hva brukes en DMZ (Demilitarisert sone) til i et nettverk?

**A:**Å isolere tjenester som skal være tilgjengelige fra internett fra det interne nettverket.

---

## Card 35

**Q:**Hva kalles metoden der IT-infrastruktur styres via maskinlesbare konfigurasjonsfiler i stedet for manuell konfigurering?

**A:**IaC (Infrastruktur som kode).

---

## Card 36

**Q:**Hva betyr 'redundans' i et IT-system?

**A:**At kritiske komponenter er duplisert slik at systemet fungerer selv om én del svikter.

---

## Card 37

**Q:**Hva kalles forsinkelsen i kommunikasjon mellom en klient og en server?

**A:**Latens.

---

## Card 38

**Q:**Hva er en 'Hypervisor'?

**A:**Programvare som lar én fysisk server kjøre flere virtuelle maskiner samtidig.

---

## Card 39

**Q:**Hva er fordelen med en 'Public Cloud' sammenlignet med 'Private Cloud'?

**A:**Den er mer skalerbar og har lavere inngangskostnader (OPEX-modell).

---

## Card 40

**Q:**Hva innebærer prinsippet om 'Digital suverenitet' for Norge?

**A:**Å styrke nasjonal kontroll over kritisk digital infrastruktur og IT-systemer.

---

## Card 41

**Q:**I skysammenheng, hva menes med 'Vendor lock-in'?

**A:**At en virksomhet blir så avhengig av én leverandør at det er vanskelig og dyrt å bytte.

---

## Card 42

**Q:**Hvilken lovgivning stiller krav til behandling og lagring av personopplysninger i skytjenester?

**A:**GDPR (Personvernforordningen).

---

## Card 43

**Q:**Hva kalles avtalen som regulerer hvordan en skyleverandør behandler personopplysninger på vegne av en kunde?

**A:**Databehandleravtale.

---

## Card 44

**Q:**Hva er 'eOppslag' ifølge Digitaliseringsdirektoratet?

**A:**Beskrivelse av synkrone API-kall mot en datatilbyder med tilgangsstyring.

---

## Card 45

**Q:**Hvilken standardserie setter krav til bygging og infrastruktur i norske datasentre?

**A:**NEK 703.

---

## Card 46

**Q:**Hva måles med en 'bærekraftsindeks' for digital infrastruktur?

**A:**En transparent status på miljøpåvirkningen fra digital infrastruktur for befolkning og bedrifter.

---

## Card 47

**Q:**Hva kalles prosessen med å ta utrangert IT-utstyr tilbake for sikker sletting og gjenbruk?

**A:**Takeback-tjeneste.

---

## Card 48

**Q:**Hva er 'fri-kjøling' i et datasenter?

**A:**Bruk av kald uteluft eller vann til kjøling for å redusere behovet for aircondition.

---

## Card 49

**Q:**Hvorfor er Norge et attraktivt land for grønne datasentre?

**A:**Tilgang på fornybar vannkraft, lav energipris og kaldt klima for naturlig kjøling.

---

## Card 50

**Q:**Hva er forskjellen på CAPEX og OPEX i IT-budsjettering?

**A:**CAPEX er investeringskostnader i forkant, mens OPEX er løpende driftsutgifter.

---

## Card 51

**Q:**Hva kalles en samling disker som fungerer sammen for å gi redundans eller økt ytelse?

**A:**RAID (Redundant Array of Independent Disks).

---

## Card 52

**Q:**Hva er formålet med en UPS (Uninterruptible Power Supply) i et serverrom?

**A:**Å sikre kontinuerlig strømforsyning ved strømbrudd frem til nødstrøm starter.

---

## Card 53

**Q:**Hva betyr 'elastisitet' i skyberegning?

**A:**Evnen til å raskt skalere ressurser opp eller ned basert på det faktiske behovet.

---

## Card 54

**Q:**Hva er en IP-adresseplan?

**A:**En oversikt over bruken av IP-adresser, VLAN, subnett og gateway i en virksomhet.

---

## Card 55

**Q:**Hvilken nettverkstopologi er vanligst i moderne lokalnettverk?

**A:**Stjernetopologi.

---

## Card 56

**Q:**Hva står forkortelsen EE-avfall for?

**A:**Elektrisk og elektronisk avfall.

---

## Card 57

**Q:**Hvilket organ i Norge gir råd og veiledning om informasjonssikkerhet og personellsikkerhet?

**A:**NSM (Nasjonal sikkerhetsmyndighet).

---

## Card 58

**Q:**Hva kalles et fullstendig parallelt IT-miljø som alltid er klart for umiddelbar overtagelse ved feil?

**A:**Hot standby.

---

## Card 59

**Q:**Hva er hovedforskjellen på backup og arkivering?

**A:**Backup er for rask gjenoppretting av aktive data, mens arkivering er langtidslagring av historiske data.

---

## Card 60

**Q:**Hva er formålet med 'Schrems II'-dommen i forhold til skytjenester?

**A:**Den begrenset lovligheten ved å overføre personopplysninger til land utenfor EU/EØS, som USA.

---
