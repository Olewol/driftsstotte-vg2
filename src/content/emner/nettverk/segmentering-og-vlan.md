---
title: "Segmentering og VLAN"
emne: nettverk
kompetansemaal:
  - km-02
kilder:
  - ndla
tags: [vlan, subnetting, cidr, segmentering, nettverk, 802.1q]
flashcards: true
public: true
---

# Segmentering og VLAN

## Introduksjon

Et nettverket der alle enheter snakker med alle andre er enkelt å sette opp — men det er en sikkerhetsmessig og ytelsesmessig katastrofe. Segmentering handler om å dele nettverket inn i logiske soner slik at trafikken styres kontrollert. I praksis gjøres dette med subnetting (lag 3) og VLAN (lag 2). Disse to teknikkene utfyller hverandre og er fundamentale for alle som skal planlegge og drifte et profesjonelt nettverk.

## Teori

### IPv4 og subnetting

#### IPv4-adresser

En IPv4-adresse er 32 bit lang og skrives som fire desimale tall separert av punktum (dotted decimal notation):

```
192  .  168  .   1  .  10
11000000.10101000.00000001.00001010
```

Hvert tall (oktet) kan være fra 0 til 255 (8 bit). Det gir teoretisk ca. **4,29 milliarder** unike adresser — et tall som er oppbrukt, noe som er en av grunnene til IPv6.

#### Nettverksdel og vertsdel

En IP-adresse er delt i to:
- **Nettverksdelen**: identifiserer nettverket
- **Vertsdelen**: identifiserer den spesifikke enheten i nettverket

**Subnettmasken** avgjør grensen mellom delene. Masken er alltid sammenhengende 1-ere etterfulgt av 0-er i binær form.

#### CIDR-notasjon

CIDR (Classless Inter-Domain Routing) er en kompakt måte å skrive subnettmasken på — som et suffiks etter IP-adressen:

| CIDR | Subnettmaske | Antall verter | Typisk bruk |
|------|-------------|---------------|-------------|
| /8 | 255.0.0.0 | 16 777 214 | Svært store nettverk |
| /16 | 255.255.0.0 | 65 534 | Mellomstore nettverk |
| /24 | 255.255.255.0 | 254 | Vanlig LAN |
| /25 | 255.255.255.128 | 126 | Halvdelt /24 |
| /26 | 255.255.255.192 | 62 | Kvartal av /24 |
| /30 | 255.255.255.252 | 2 | Point-to-point-lenker |

Antall verter = 2^(antall vertsbit) − 2 (nettverk- og broadcast-adresse er reservert).

#### Regneeksempel: Del opp 192.168.1.0/24

Scenario: Du har nettverket `192.168.1.0/24` (254 adresser) og trenger fire separate subnett for: Ansatte, Gjest, Servere, Admin.

Hvert subnett kan bruke /26 (62 verter per subnett):

| Subnett | Nettverksadresse | Første host | Siste host | Broadcast |
|---------|-----------------|-------------|------------|-----------|
| Ansatte | 192.168.1.0/26 | 192.168.1.1 | 192.168.1.62 | 192.168.1.63 |
| Gjest | 192.168.1.64/26 | 192.168.1.65 | 192.168.1.126 | 192.168.1.127 |
| Servere | 192.168.1.128/26 | 192.168.1.129 | 192.168.1.190 | 192.168.1.191 |
| Admin | 192.168.1.192/26 | 192.168.1.193 | 192.168.1.254 | 192.168.1.255 |

#### Private adresserom

Disse adressene rutes ikke på internett og brukes til interne nettverk:

| Adresseblokk | CIDR | Antall adresser |
|--------------|------|-----------------|
| 10.0.0.0–10.255.255.255 | 10.0.0.0/8 | ~16,7 mill. |
| 172.16.0.0–172.31.255.255 | 172.16.0.0/12 | ~1,05 mill. |
| 192.168.0.0–192.168.255.255 | 192.168.0.0/16 | 65 536 |

---

### VLAN — Virtuelt lokalnettverk

#### Hva er et VLAN?

Et VLAN (Virtual Local Area Network) er en logisk inndeling av et fysisk nettverk. Med VLAN kan du ha tre separate nettverk på én fysisk svitsj — enhetene i hvert VLAN ser hverandre, men ikke enheter i andre VLAN (med mindre du eksplisitt tillater det via en ruter).

#### IEEE 802.1Q — VLAN-tagging

Standarden for VLAN er **IEEE 802.1Q**. Den definerer hvordan en VLAN-tag legges til i Ethernet-rammen:

```
[Dest MAC][Src MAC][802.1Q tag][EtherType][Data][FCS]
                  |          |
                  4 bytes: inkluderer 12-bits VLAN ID (0–4094)
```

VLAN ID 0 og 4095 er reservert; brukbare VLAN-ID-er er 1–4094.

#### Access-porter vs. trunk-porter

| Port-type | Funksjon | Tagging | Brukes til |
|-----------|----------|---------|------------|
| **Access-port** | Tilhører ett VLAN | Untagged (taggen fjernes) | Sluttenheter (PC, printer) |
| **Trunk-port** | Bærer trafikk for flere VLAN | Tagged (taggen beholdes) | Forbindelser mellom svitsjer og til ruter |

En PC på en access-port "vet" ikke at den er i et VLAN — den ser bare et vanlig nettverk. Taggen legges til av svitsjen og fjernes på mottakersiden.

**Native VLAN** er VLAN-et som mottar *untagget* trafikk på en trunk-port (standard er VLAN 1). Det anbefales å endre native VLAN fra 1 av sikkerhetshensyn.

#### Hvorfor segmentere med VLAN?

**Sikkerhet**: En trussel i gjeste-VLAN-et kan ikke nå servere i server-VLAN-et uten å passere en ruter/brannmur med eksplisitte tillatelses-regler.

**Ytelse**: Hvert VLAN er sitt eget broadcast-domene. Broadcast-trafikk (ARP, DHCP Discover) sendes bare innenfor VLAN-et — ikke til alle enheter i hele nettverket.

**Fleksibilitet**: En ansatt som flytter til et annet rom trenger bare å endre port-VLAN-tilordningen i svitsjen — ingen ny kabling.

**Typisk VLAN-struktur i en skole/bedrift**:

| VLAN | Navn | Adresserom | Formål |
|------|------|-----------|--------|
| 10 | Ansatte | 192.168.10.0/24 | Arbeidsmaskiner |
| 20 | Gjest | 192.168.20.0/24 | Besøkende, IoT |
| 30 | Servere | 192.168.30.0/24 | Interne servere |
| 40 | Admin | 192.168.40.0/24 | IT-avdelingen |
| 99 | Mgmt | 192.168.99.0/24 | Nettverksutstyr |

## Eksempel / lab

### Konfigurasjon i UniFi

**Opprette et VLAN:**
1. UniFi Network → Settings → Networks
2. Klikk "Create New Network"
3. Velg "Virtual Network (VLAN)"
4. Gi nettverket et navn (f.eks. "Gjest")
5. Sett VLAN ID (f.eks. 20)
6. Konfigurer subnett (f.eks. `192.168.20.1/24`) og aktiver DHCP
7. Lagre

**Tilordne VLAN til svitsjeport:**
1. UniFi Network → Devices → velg svitsjen
2. Gå til Ports-fanen
3. Klikk på ønsket port
4. Velg "Switch Port Profile" eller sett manuelt:
   - Native VLAN: VLAN-et for utagget trafikk (access-port: velg VLAN 20)
   - Tagged VLANs: VLAN-ene som skal tagges gjennom porten (trunk-port)

**Trådløst VLAN (SSID):**
1. Settings → WiFi → opprett nytt WiFi-nettverk
2. Knytt SSID til ønsket VLAN (f.eks. "Gjest-WiFi" → VLAN 20)

## Quiz

<details>
<summary>Spørsmål 1: Hva er nettverksadressen, første brukbare IP og broadcast for 192.168.5.0/26?</summary>

**Svar:** /26 gir subnettmaske 255.255.255.192 (64 adresser per blokk).
- Nettverksadresse: `192.168.5.0`
- Første brukbare host: `192.168.5.1`
- Siste brukbare host: `192.168.5.62`
- Broadcast: `192.168.5.63`
</details>

<details>
<summary>Spørsmål 2: Hva er forskjellen mellom en access-port og en trunk-port?</summary>

**Svar:** En access-port tilhører ett VLAN og sender utagget trafikk til sluttenheter. En trunk-port bærer tagget trafikk for flere VLAN og brukes mellom svitsjer og til rutere.
</details>

<details>
<summary>Spørsmål 3: Hvilken IEEE-standard definerer VLAN-tagging?</summary>

**Svar:** IEEE 802.1Q definerer VLAN-tagging i Ethernet-rammer. Taggen er 4 bytes og inneholder bl.a. et 12-bits VLAN ID (1–4094).
</details>

<details>
<summary>Spørsmål 4: Hvorfor er VLAN nyttig for nettverkssikkerhet?</summary>

**Svar:** VLAN skaper separate broadcast-domener. En enhet i ett VLAN kan ikke kommunisere direkte med enheter i et annet VLAN uten å passere en ruter eller brannmur med eksplisitte tillatelsesregler. Dette begrenser spredning av trusler og hindrer uautorisert tilgang mellom nettverk.
</details>

<details>
<summary>Spørsmål 5: Hva er et privat adresserom, og hvorfor brukes det?</summary>

**Svar:** Private adresserom (10.x.x.x, 172.16-31.x.x, 192.168.x.x) er IP-adresser som ikke rutes på internett. De brukes til interne nettverk og oversettes til en offentlig IP via NAT når trafikk går ut på internett. Dette gir adressebesparelse og et ekstra lag med skjul mot internett.
</details>

## Flashcards

VLAN :: Virtual Local Area Network — logisk inndeling av et fysisk nettverk med IEEE 802.1Q
CIDR :: Classless Inter-Domain Routing — skriving av subnettmaske som suffiks: f.eks. /24 = 255.255.255.0
Subnettmaske :: Angir grensen mellom nettverksdel og vertsdel i en IP-adresse
Access-port :: Svitsjeport som tilhører ett VLAN og sender utagget trafikk til sluttenheter
Trunk-port :: Svitsjeport som bærer tagget trafikk for flere VLAN (svitsj-til-svitsj, svitsj-til-ruter)
Native VLAN :: VLAN-et som mottar utagget trafikk på en trunk-port (standard VLAN 1)
IEEE 802.1Q :: Standarden for VLAN-tagging i Ethernet-rammer
Broadcast-domene :: Området der broadcast-trafikk spres; hvert VLAN er et eget broadcast-domene
/24-nettverk :: Subnett med 256 adresser (254 brukbare), subnettmaske 255.255.255.0
Private adresser :: IP-adresser (10.x.x.x, 172.16-31.x.x, 192.168.x.x) som ikke rutes på internett

## Ressurser

- [Virtuelt lokalnettverk VLAN — NDLA](https://ndla.no/nb/r/driftsstotte-im-itk-vg2/virtuelt-lokalnettverk-vlan/9d865afa88)
- [IPv4 — NDLA](https://ndla.no/en/r/operational-support-im-itk-vg2/ipv4/987eefec02)
- [Creating Virtual Networks (VLANs) — Ubiquiti UniFi](https://help.ui.com/hc/en-us/articles/9761080275607-Creating-Virtual-Networks-VLANs)
- [Switch Port VLAN Assignment — Ubiquiti UniFi](https://help.ui.com/hc/en-us/articles/26136855808919-Switch-Port-VLAN-Assignment-Trunk-Access-Ports)
- [Svitsj — NDLA](https://ndla.no/nb/r/driftsstotte-im-itk-vg2/svitsj/a33b4b015c)
