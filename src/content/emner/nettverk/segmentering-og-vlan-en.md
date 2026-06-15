---
title: "Segmentation and VLAN"
emne: nettverk
competence_goals:

  - km-02

language: en
original: segmentering-og-vlan.md
kilder:

  - ndla
  - <https://ndla.no/nb/subject:1:f5471415-32e6-4299-813c-0466099b0577/topic:1:43d57d77-628d-4a12-8857-4b77f884693a/resource:1:66547>
  - <https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/>
  - <https://www.professormesser.com/network-plus/>
  - <https://www.cloudflare.com/learning/>
  - <https://learn.microsoft.com/en-us/training/paths/networking-fundamentals/>

tags: [vlan, subnetting, cidr, segmentation, network, 802.1q]
flashcards: <https://notebooklm.google.com/notebook/f7e5ad6c-7082-40cf-abd5-7a41b540f8e1>
public: true
video: <https://www.youtube.com/watch?v=MzwV67L_6f8>
notebooklm: true
---

# Segmentation and VLAN

## Introduction

AA network where all devices can talk to everyone else is easy to set up — but it's a security and performance disaster.
AASegmentation is about dividing the network into logical zones so that traffic is controlled.
AAIn practice, this is done with subnetting (layer 3) and VLANs (layer 2). These two techniques complement each other and
Aare fundamental for anyone planning and operating a professional network.

TTo understand segmentation, it's useful to see it in the context of the [[osi-modellen-en|OSI model]] and the
TTstandardized protocols described in [[nettverksprotokoller-en|network protocols]].
TTVLANs are especially central in virtual infrastructures where virtual switches use IEEE 802.1Q tagging to logically
Tseparate traffic.

## Theory

### IPv4 and Subnetting

#### IPv4 Addresses

An IPv4 address is 32 bits long and is written as four decimal numbers separated by periods (dotted decimal notation):

```text
192  .  168  .   1  .  10
11000000.10101000.00000001.00001010
```

EEach number (octet) can range from 0 to 255 (8 bits). This gives theoretically about**4.29 billion**unique addresses — a
Enumber that has been exhausted, which is one of the reasons for IPv6.

#### Network Part and Host Part

An IP address is divided into two parts:
-**Network part**: identifies the network
-**Host part**: identifies the specific device in the network

TThe**subnet mask**determines the boundary between the parts. The mask is always contiguous 1s followed by 0s in binary
Tform.

#### CIDR Notation

CIDR (Classless Inter-Domain Routing) is a compact way to write the subnet mask — as a suffix after the IP address:

|| CIDR | Subnet Mask | Number of Hosts | Typical Use |
|| ------ | ------------ | ----------------- | ------------- |
|| /8 | 255.0.0.0 | 16,777,214 | Very large networks |
|| /16 | 255.255.0.0 | 65,534 | Medium-sized networks |
|| /24 | 255.255.255.0 | 254 | Typical LAN |
|| /25 | 255.255.255.128 | 126 | Half a /24 |
|| /26 | 255.255.255.192 | 62 | Quarter of a /24 |
|| /30 | 255.255.255.252 | 2 | Point-to-point links |

Number of hosts = 2^(number of host bits) − 2 (network and broadcast addresses are reserved).

#### Calculation Example: Subdivide 192.168.1.0/24

SScenario: You have the network `192.168.1.0/24` (254 addresses) and need four separate subnets for: Employees, Guest,
SServers, Admin.

Each subnet can use /26 (62 hosts per subnet):

|| Subnet | Network Address | First Host | Last Host | Broadcast |
|| -------- | ---------------- | ------------ | ----------- | ----------- |
|| Employees | 192.168.1.0/26 | 192.168.1.1 | 192.168.1.62 | 192.168.1.63 |
|| Guest | 192.168.1.64/26 | 192.168.1.65 | 192.168.1.126 | 192.168.1.127 |
|| Servers | 192.168.1.128/26 | 192.168.1.129 | 192.168.1.190 | 192.168.1.191 |
|| Admin | 192.168.1.192/26 | 192.168.1.193 | 192.168.1.254 | 192.168.1.255 |

#### Private Address Ranges

These addresses are not routed on the internet and are used for internal networks:

|| Address Block | CIDR | Number of Addresses |
|| -------------- | ------ | ------------------- |
|| 10.0.0.0–10.255.255.255 | 10.0.0.0/8 | ~16.7 million |
|| 172.16.0.0–172.31.255.255 | 172.16.0.0/12 | ~1.05 million |
|| 192.168.0.0–192.168.255.255 | 192.168.0.0/16 | 65,536 |

---

### VLAN — Virtual Local Area Network

#### What is a VLAN?

AA VLAN (Virtual Local Area Network) is a logical division of a physical network. With VLANs, you can have three separate
AAnetworks on one physical switch — devices in each VLAN can see each other, but not devices in other VLANs (unless you
Aexplicitly allow it through a router).

#### IEEE 802.1Q — VLAN Tagging

The standard for VLANs is**IEEE 802.1Q**. It defines how a VLAN tag is added to the Ethernet frame:

```text
[Dest MAC][Src MAC][802.1Q tag][EtherType][Data][FCS]
                  ||  |
                  4 bytes: includes 12-bit VLAN ID (0–4094)
```

VVLAN IDs 0 and 4095 are reserved; usable VLAN IDs are 1–4094.**IEEE 802.1Q**is the international standard for VLAN
Vtagging in Ethernet frames — it enables multiple logical networks on a single physical connection.

#### Access Ports vs. Trunk Ports

|| Port Type | Function | Tagging | Used for |
|| ----------- | ---------- | --------- | ---------- |
|| **Access port** | Belongs to one VLAN | Untagged (tag is removed) | End devices (PC, printer) |
|| **Trunk port** | Carries traffic for multiple VLANs | Tagged (tag is kept) | Connections between switches and to router |

AA PC on an access port doesn't "know" it's on a VLAN — it just sees a regular network.
AThe tag is added by the switch and removed on the receiving end.

AA**trunk port**is a switch port configured to carry traffic from multiple VLANs simultaneously by keeping the VLAN tags
Ain the data packet.

***Native VLAN**is the VLAN that receives*untagged*traffic on a trunk port (default is VLAN 1).
*It is recommended to change the native VLAN from 1 for security reasons.

#### Why Segment with VLANs?

***Security**: A threat in the guest VLAN cannot reach servers in the server VLAN without passing through a
*router/firewall with explicit allow rules.

***Performance**: Each VLAN is its own broadcast domain. Broadcast traffic (ARP, DHCP Discover) is only sent within the
*VLAN — not to all devices in the entire network.

***Flexibility**: An employee who moves to another room only needs the port VLAN assignment changed on the switch — no
*new cabling.

**Typical VLAN structure in a school/business**:

|| VLAN | Name | Address Space | Purpose |
|| ------ | ------ | ------------- | --------- |
|| 10 | Employees | 192.168.10.0/24 | Work machines |
|| 20 | Guest | 192.168.20.0/24 | Visitors, IoT |
|| 30 | Servers | 192.168.30.0/24 | Internal servers |
|| 40 | Admin | 192.168.40.0/24 | IT department |
|| 99 | Mgmt | 192.168.99.0/24 | Network equipment |

## Example / Lab

### Configuration in UniFi

*## Creating a VLAN:

1. UniFi Network → Settings → Networks
2. Click "Create New Network"
3. Select "Virtual Network (VLAN)"
4. Give the network a name (e.g. "Guest")
5. Set VLAN ID (e.g. 20)
6. Configure subnet (e.g. `192.168.20.1/24`) and enable DHCP
7. Save

*## Assigning VLAN to Switch Port:

1. UniFi Network → Devices → select the switch
2. Go to the Ports tab
3. Click the desired port
4. Select "Switch Port Profile" or set manually:
   - Native VLAN: VLAN for untagged traffic (access port: select VLAN 20)
   - Tagged VLANs: VLANs to be tagged through the port (trunk port)

*## Wireless VLAN (SSID):

1. Settings → WiFi → create new WiFi network
2. Bind SSID to desired VLAN (e.g. "Guest-WiFi" → VLAN 20)

## Study Guide

*## Core Understanding: Subnetting
SSubnetting divides an IP address space into smaller, isolated networks. /24 is the most common LAN size (254 hosts).
SSUnderstand the difference between network address, broadcast address, and usable host addresses.
SRemember the formula: 2^(host bits) − 2.

*## Core Understanding: VLAN
VVLAN is logical network segmentation at layer 2 (data link). The IEEE 802.1Q tag (4 bytes) is inserted into the Ethernet
Vframe with a VLAN ID. Access ports remove the tag for end devices; trunk ports keep it to carry multiple VLANs.

*## Common Exam Points

- Calculate network address, broadcast, and usable addresses from CIDR notation
- The difference between access port and trunk port
- What native VLAN is and why VLAN 1 as native VLAN is a security risk
- Benefits of VLANs: security, performance (fewer broadcasts), flexibility

## FAQ

*## What is the difference between subnetting and VLAN?
SSubnetting (layer 3) divides the IP address space and is a routable separation. VLAN (layer 2) creates logical networks
SSon a single physical infrastructure without requiring separate physical cables. The two are commonly used together:
Seach VLAN gets its own subnet.

*## Can devices in different VLANs communicate?
YYes, but only via a router or layer 3 switch with explicit allow rules. This gives controlled traffic between segments —
Ye.g., servers are accessible from the employee VLAN but not from the guest VLAN.

*## What happens to broadcast traffic in a VLAN?
BBroadcasts (e.g. DHCP Discover, ARP) are only sent within the same VLAN. This means a large company with 10 VLANs has
Bmuch lower broadcast load than if all devices were in one large flat network.

*## What is the native VLAN and why should you change it from VLAN 1?
TThe native VLAN is the VLAN that handles untagged traffic on a trunk port. VLAN 1 is the default, but it is known as a
Tsecurity risk (VLAN hopping attacks). Best practice is to choose an unused VLAN number as the native VLAN.

*## How do you configure VLANs on a Cisco switch (basic)?

```bash
Switch(config)# vlan 10
Switch(config-vlan)# name Employees
Switch(config)# interface fa0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10
```

*## What is IEEE 802.1Q?
IIEEE 802.1Q is the international standard for VLAN tagging in Ethernet frames. The tag is 4 bytes and contains, among
Iother things, a 12-bit VLAN ID enabling 4094 different VLANs.

*## What is CIDR and why is it better than classic subnetting?
CCIDR (Classless Inter-Domain Routing) allows you to use subnet masks that don't follow the old class A/B/C boundaries.
CThis gives much more flexible addressing and is the foundation of all modern IP planning.

*## Can you have VLANs on wireless networks?
YYes. Modern access points support SSID-to-VLAN mapping. The guest WiFi network can be connected to VLAN 20, while
Yemployee WiFi connects to VLAN 10 — the traffic is kept separate even though both use the same physical access point.

## Quiz

<details>
<summary>Question 1: What is the network address, first usable IP, and broadcast for 192.168.5.0/26?</summary>

**Answer:**/26 gives subnet mask 255.255.255.192 (64 addresses per block).

- Network address: `192.168.5.0`
- First usable host: `192.168.5.1`
- Last usable host: `192.168.5.62`
- Broadcast: `192.168.5.63`

</details>

<details>
<summary>Question 2: What is the difference between an access port and a trunk port?</summary>

***Answer:**An access port belongs to one VLAN and sends untagged traffic to end devices.
*A trunk port carries tagged traffic for multiple VLANs and is used between switches and to routers.
</details>

<details>
<summary>Question 3: Which IEEE standard defines VLAN tagging?</summary>

***Answer:**IEEE 802.1Q defines VLAN tagging in Ethernet frames. The tag is 4 bytes and contains, among other things, a
*12-bit VLAN ID (1–4094).
</details>

<details>
<summary>Question 4: Why is VLAN useful for network security?</summary>

***Answer:**VLANs create separate broadcast domains. A device in one VLAN cannot communicate directly with devices in
**another VLAN without passing through a router or firewall with explicit allow rules.
*This limits the spread of threats and prevents unauthorized access between networks.
</details>

<details>
<summary>Question 5: What is a private address range, and why is it used?</summary>

***Answer:**Private address ranges (10.x.x.x, 172.16-31.x.x, 192.168.x.x) are IP addresses that are not routed on the
**internet. They are used for internal networks and are translated to a public IP via NAT when traffic goes to the
*internet. This saves address space and provides an extra layer of concealment from the internet.
</details>

## Resources

- [Virtual Local Area Network VLAN — NDLA](<https://ndla.no/nb/r/driftsstotte-im-itk-vg2/virtuelt-lokalnettverk-vlan/9d865afa88>)
- [IPv4 — NDLA](<https://ndla.no/en/r/operational-support-im-itk-vg2/ipv4/987eefec02>)
- [Creating Virtual Networks (VLANs) — Ubiquiti UniFi](<https://help.ui.com/hc/en-us/articles/9761080275607-Creating-Virtual-Networks-VLANs>)
- [Switch Port VLAN Assignment — Ubiquiti UniFi](<https://help.ui.com/hc/en-us/articles/26136855808919-Switch-Port-VLAN-Assignment-Trunk-Access-Ports>)
- [Switch — NDLA](<https://ndla.no/nb/r/driftsstotte-im-itk-vg2/svitsj/a33b4b015c>)
- [VLAN — SNL](<https://snl.no/VLAN>)
