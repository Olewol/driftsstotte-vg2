# Nettverk lynkort

## Card 1

**Q:**Which layer of the OSI model is responsible for the physical transmission of bits over a medium?

**A:**Layer 1 (Physical Layer)

---

## Card 2

**Q:**The_____layer of the OSI model handles MAC addresses and organizes bits into frames.

**A:**Data Link (Layer 2)

---

## Card 3

**Q:**Which OSI layer is responsible for logical addressing (IP) and routing packets between different networks?

**A:**Layer 3 (Network Layer)

---

## Card 4

***Q:**The_____layer of the OSI model ensures end-to-end communication, flow control, and error recovery using protocols
*like TCP.

**A:**Transport (Layer 4)

---

## Card 5

***Q:**Which OSI layer manages the establishment, maintenance, and termination of communication sessions between
*applications?

**A:**Layer 5 (Session Layer)

---

## Card 6

***Q:**The_____layer handles data formatting, encryption, and compression to make data presentable for the application
*layer.

**A:**Presentation (Layer 6)

---

## Card 7

**Q:**Which layer is the only one that directly interacts with data from end-user software like web browsers?

**A:**Layer 7 (Application Layer)

---

## Card 8

**Q:**In the OSI model, what is the Protocol Data Unit (PDU) at Layer 2?

**A:**Frame

---

## Card 9

**Q:**In the OSI model, what is the Protocol Data Unit (PDU) at Layer 3?

**A:**Packet

---

## Card 10

**Q:**In the OSI model, what is the Protocol Data Unit (PDU) at Layer 4?

**A:**Segment (for TCP) or Datagram (for UDP)

---

## Card 11

**Q:**The process of adding a header to data as it moves down the OSI layers is called_____.

**A:**Encapsulation

---

## Card 12

**Q:**How does the TCP/IP model differ from the OSI model regarding the top three layers?

**A:**TCP/IP combines the Session, Presentation, and Application layers into a single Application layer.

---

## Card 13

**Q:**Which transport protocol is connection-oriented and guarantees that data arrives in the correct order?

**A:**TCP (Transmission Control Protocol)

---

## Card 14

**Q:**Which transport protocol is connectionless and prioritized for speed over reliability?

**A:**UDP (User Datagram Protocol)

---

## Card 15

**Q:**What are the three steps of the TCP connection establishment process?

**A:**SYN, SYN-ACK, and ACK (Three-way handshake)

---

## Card 16

**Q:**Standard port for HTTP

**A:**80

---

## Card 17

**Q:**Standard port for HTTPS

**A:**443

---

## Card 18

**Q:**Standard port for SSH and SFTP

**A:**22

---

## Card 19

**Q:**Standard port for DNS queries

**A:**53

---

## Card 20

**Q:**Standard port for RDP (Remote Desktop)

**A:**3389

---

## Card 21

**Q:**Which UDP ports are used by DHCP?

**A:**67 (Server) and 68 (Client)

---

## Card 22

**Q:**What is the primary function of the Domain Name System (DNS)?

**A:**Translating human-readable domain names into machine-friendly IP addresses.

---

## Card 23

**Q:**DNS Record Type: A

**A:**Maps a hostname to an IPv4 address.

---

## Card 24

**Q:**DNS Record Type: AAAA

**A:**Maps a hostname to an IPv6 address.

---

## Card 25

**Q:**DNS Record Type: MX

**A:**Specifies the mail server responsible for receiving email for a domain.

---

## Card 26

**Q:**DNS Record Type: CNAME

**A:**Creates an alias that points one domain name to another canonical domain name.

---

## Card 27

**Q:**DNS Record Type: PTR

**A:**Used for reverse lookups, mapping an IP address back to a hostname.

---

## Card 28

**Q:**What is a DNS 'Forwarder'?

**A:**A configuration where a DNS server sends queries it cannot resolve to an external DNS server.

---

## Card 29

**Q:**In the DNS hierarchy, which servers manage the suffixes like .no, .com, or .org?

**A:**TLD (Top-Level Domain) nameservers

---

## Card 30

**Q:**What does the 'D' stand for in the DHCP DORA process?

**A:**Discover (Client broadcasts to find a server)

---

## Card 31

**Q:**What does the 'O' stand for in the DHCP DORA process?

**A:**Offer (Server sends proposed configuration to the client)

---

## Card 32

**Q:**What does the 'R' stand for in the DHCP DORA process?

**A:**Request (Client accepts the offer from a specific server)

---

## Card 33

**Q:**What does the 'A' stand for in the DHCP DORA process?

**A:**Acknowledge (Server finalizes the lease and confirms settings)

---

## Card 34

**Q:**In DHCP, what is a 'Scope'?

**A:**The administrative range of IP addresses on a subnet that a server is allowed to lease.

---

## Card 35

**Q:**In DHCP, what is the 'Lease Time'?

**A:**The duration for which a client is permitted to use a dynamically assigned IP address.

---

## Card 36

**Q:**What DHCP feature ensures a specific device always receives the same IP address based on its MAC address?

**A:**Reservation

---

## Card 37

**Q:**What mechanism allows a DHCP server to provide IP addresses to a subnet where it is not physically present?

**A:**DHCP Relay Agent (or IP Helper Address)

---

## Card 38

**Q:**What is the name of the IEEE standard for VLAN tagging?

**A:**IEEE 802.1Q (Dot1q)

---

## Card 39

**Q:**VLANs operate at Layer_____of the OSI model.

**A:**2 (Data Link Layer)

---

## Card 40

**Q:**Term: Access Port

**A:**Definition: A switch port that belongs to only one VLAN and carries untagged traffic.

---

## Card 41

**Q:**Term: Trunk Port

**A:**Definition: A switch port that carries traffic for multiple VLANs using tagging.

---

## Card 42

**Q:**What is a 'Native VLAN' on a trunk port?

**A:**The VLAN that receives all untagged traffic arriving on the trunk.

---

## Card 43

**Q:**How can devices in different VLANs communicate with each other?

**A:**Through a Layer 3 device (router or L3 switch) using Inter-VLAN routing.

---

## Card 44

**Q:**What is 'Router-on-a-stick'?

***A:**A configuration where a single physical router interface is divided into sub-interfaces to route between multiple
*VLANs.

---

## Card 45

**Q:**Name two major benefits of network segmentation using VLANs.

**A:**Improved security (isolation) and better performance (reduced broadcast domains).

---

## Card 46

***Q:**Which software layer sits between physical hardware and virtual machines, allowing multiple OSs to share the same
*hardware?

**A:**Hypervisor

---

## Card 47

**Q:**What is the purpose of the Address Resolution Protocol (ARP)?

**A:**Mapping a known IP address to a physical MAC address on a local network.

---

## Card 48

**Q:**Which diagnostic protocol is used by the 'ping' command to test connectivity?

**A:**ICMP (Internet Control Message Protocol)

---

## Card 49

**Q:**In an Active Directory environment, where are DNS records typically stored and replicated?

**A:**In Active Directory-integrated zones on Domain Controllers.

---

## Card 50

**Q:**What is the purpose of DNSSEC?

**A:**To validate DNS responses and ensure data integrity and authenticity.

---

## Card 51

**Q:**What happens if a DHCP client receives a 'NACK' (Negative Acknowledge) message?

**A:**The requested IP address is invalid, and the client must restart the DHCP process.

---

## Card 52

**Q:**Standard ports for FTP

**A:**20 (Data) and 21 (Control)

---

## Card 53

**Q:**Which command-line tool is used to query DNS records manually?

**A:**nslookup

---

## Card 54

**Q:**What is the CIDR notation for the subnet mask 255.255.255.0?

**A:**/24

---

## Card 55

**Q:**Which network device uses MAC addresses to forward frames within a single LAN?

**A:**Switch (Layer 2)

---

## Card 56

**Q:**What is the valid range for VLAN IDs under the 802.1Q standard?

**A:**1 to 4,094

---

## Card 57

**Q:**In OSI troubleshooting, which layer should be checked first if 'ping' to the gateway fails but the cable is fine?

**A:**Layer 3 (Network Layer) for IP configuration issues.

---

## Card 58

**Q:**A_____is a portion of a larger network that has been isolated to improve security or performance.

**A:**Subnet (or segment)

---

## Card 59

**Q:**What is the primary role of a Domain Controller (DC) in Windows Server?

**A:**Managing authentication and authorization via Active Directory Domain Services.

---

## Card 60

**Q:**Which protocol is used for synchronizing email between a server and a client while keeping messages on the server?

**A:**IMAP (Internet Message Access Protocol)

---

## Card 61

**Q:**Which protocol is used for sending emails from a client to a server?

**A:**SMTP (Simple Mail Transfer Protocol)

---

## Card 62

**Q:**What defines the boundary between the network portion and the host portion of an IP address?

**A:**Subnet Mask

---

## Card 63

**Q:**Which network address is used by a client to send data to a different network?

**A:**Default Gateway

---

## Card 64

**Q:**Example of a Private IPv4 range

**A:**192.168.0.0 to 192.168.255.255 (also 10.x.x.x and 172.16-31.x.x)

---

## Card 65

**Q:**Which protocol is used to monitor and manage network devices like switches and routers?

**A:**SNMP (Simple Network Management Protocol)

---
