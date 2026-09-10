# Nettverk quiz

## Question 1

Hvilket lag i OSI-modellen er ansvarlig for å videresende data basert på MAC-adresser?

- [ ] Nettverkslaget (Lag 3)
- [x] Datalinklaget (Lag 2)
- [ ] Transportlaget (Lag 4)
- [ ] Fysisk lag (Lag 1)

**Hint:** Tenk på hvilket lag en vanlig svitsj opererer på for å koble sammen enheter i et LAN.

## Question 2

Hva skjer i det første steget av DORA-prosessen i DHCP?

- [ ] Serveren sender et tilbud om en IP-adresse til klienten.
- [x] Klienten sender en broadcast-melding for å finne tilgjengelige servere.
- [ ] Klienten bekrefter at den ønsker å bruke den foreslåtte adressen.
- [ ] Serveren registrerer adressen som utleid i sin database.

**Hint:** Vurder hva bokstaven D står for i forkortelsen DORA.

## Question 3

Hvilken DNS-posttype (record) brukes for å koble et domenenavn til en IPv4-adresse?

- [ ] MX
- [ ] CNAME
- [ ] PTR
- [x] A

**Hint:** Dette er den vanligste posttypen som brukes når du taster inn en nettadresse i nettleseren.

## Question 4

Hvorfor foretrekkes UDP fremfor TCP for tjenester som videostreaming og nettspill?

- [ ] UDP garanterer at alle pakker kommer frem i riktig rekkefølge.
- [x] UDP har mindre overhead og er raskere fordi den ikke krever bekreftelser.
- [ ] UDP krypterer data automatisk på transportlaget.
- [ ] UDP kan bare brukes i lokale nettverk uten rutere.

**Hint:** Tenk på forskjellen mellom pålitelighet og hastighet i sanntidskommunikasjon.

## Question 5

Hva er hovedformålet med å konfigurere en 'Trunk-port' på en svitsj?

- [ ] Å koble til en enkelt PC som bare skal ha tilgang til ett VLAN.
- [x] Å bære trafikk fra flere VLAN samtidig over én fysisk forbindelse.
- [ ] Å øke den fysiske hastigheten på kabelen fra 1 Gbps til 10 Gbps.
- [ ] Å fungere som en brannmur som blokkerer all innkommende trafikk.

**Hint:** Vurder hvordan to svitsjer kan utveksle informasjon om flere adskilte nettverk over samme kabel.

## Question 6

Hvilken serverrolle er nødvendig for at Windows-klienter skal kunne finne domenekontrolleren under innlogging?

- [ ] Webserver (IIS)
- [ ] Filserver
- [x] DNS-server
- [ ] Printserver

**Hint:** Tenk på hvilken tjeneste som oversetter navn til adresser slik at klienter vet hvem de skal snakke med.

## Question 7

Hvilket portnummer og transportprotokoll benyttes som standard for HTTPS-trafikk?

- [ ] Port 80 over TCP
- [x] Port 443 over TCP
- [ ] Port 53 over UDP
- [ ] Port 22 over TCP

**Hint:** Dette er porten som aktiveres når du ser hengelåsikonet i nettleseren.

## Question 8

Hva er en 'Native VLAN' på en trunk-forbindelse?

- [ ] VLAN-et som brukes til å kryptere all trafikk på trunken.
- [ ] Det eneste VLAN-et som har lov til å kommunisere med internett.
- [x] VLAN-et som håndterer trafikk som kommer inn på trunken uten en 802.1Q-tag.
- [ ] VLAN-et som automatisk deaktiverer alle andre porter ved et angrep.

**Hint:** Vurder hva som skjer med pakker som mangler en spesifikk ID-etikett når de sendes over en trunk.

## Question 9

I VirtualBox, hva skjer når en virtuell maskin er satt til 'NAT'-modus?

- [ ] Den virtuelle maskinen får en unik IP direkte fra det fysiske nettverket.
- [ ] Den virtuelle maskinen kan bare snakke med andre virtuelle maskiner på samme host.
- [x] Den virtuelle maskinen deler hostens IP og når internett via en intern oversettelse.
- [ ] Den virtuelle maskinen deaktiverer alt nettverk for å beskytte hosten.

**Hint:** Tenk på hvordan rutere i hjemmenettverk vanligvis kobler mange enheter til internett ved bruk av bare én offentlig adresse.

## Question 10

Hva er den viktigste fordelen med nettverkssegmentering ved hjelp av VLAN?

- [ ] Det gjør at man slipper å bruke fysiske rutere i nettverket.
- [x] Det øker sikkerheten ved å begrense trafikkflyt mellom ulike deler av nettverket.
- [ ] Det tvinger alle maskiner til å bruke samme IP-adresse.
- [ ] Det fjerner behovet for å ha en DHCP-server i nettverket.

**Hint:** Vurder hvordan det å dele opp et stort rom i mindre celler kan påvirke sikkerheten og spredning av problemer.
