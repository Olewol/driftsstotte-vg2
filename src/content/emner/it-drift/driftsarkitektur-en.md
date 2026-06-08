---
title: "Operations Architecture"
emne: it-drift
competence_goals:
  - km-01
  - km-03
sources:
  - ndla
  - https://ndla.no/nb/subject:1:34375b6a-9a99-4d64-884d-2a3164a27521/topic:2:183915/resource:1:160358
  - https://snl.no/skytjeneste
  - https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/
  - https://www.digdir.no/nasjonal-arkitektur/skytjenester/2153
  - https://learn.microsoft.com/en-us/azure/architecture/framework/
video: https://www.youtube.com/watch?v=mxT23V-pS0I
tags: []
flashcards: https://notebooklm.google.com/notebook/bc9a5656-7a9b-4dc5-a59e-ef4a96aa8ccd
public: true
notebooklm: true
language: en
original: driftsarkitektur.md
---

## Introduction

An operations architecture describes how an organization's IT infrastructure is built – which components exist, how they connect, and where they are located. A well-thought-out architecture makes the system stable, secure, and scalable.

Today, there are three main models: on-premise infrastructure, cloud-based infrastructure, and a combination of both (hybrid). The choice depends on requirements for control, cost, flexibility, and legal obligations. A good operations architecture always considers who is responsible for what – which is especially important when services are moved to the cloud (see [[skytjenester-en]] for the Shared Responsibility Model).

---

## Theory

### On-premise, Cloud, and Hybrid

**On-premise** means all infrastructure is located locally – in the organization's own rooms or rented server rooms. The organization owns and operates everything itself: servers, network, storage, and software.

- Advantages: full control, predictable costs over time, no dependence on internet connection
- Disadvantages: high capital costs (CAPEX), requires in-house expertise, scaling takes time

**Cloud-based infrastructure (public cloud)** means resources are rented from an external cloud provider (Microsoft Azure, Amazon Web Services, Google Cloud). The organization pays for what it uses (OPEX model).

- Advantages: elastic scaling, pay only for usage, low maintenance responsibility
- Disadvantages: ongoing costs, dependence on provider and internet, concerns about data storage and GDPR

**Hybrid cloud** combines on-premise and cloud. Critical data and services can remain local, while variable workloads run in the cloud. This is the most common model for medium-sized and large Norwegian enterprises today.

> Connection to km-03: Cloud services are an integrated part of modern operations architecture. IaaS (Infrastructure as a Service) is effectively an extension of on-premise – you rent virtual machines and networks instead of owning physical equipment. See [[skytjenester-en]] for a complete overview.

---

### Servers: Physical and Virtual

A **physical server** is dedicated hardware that runs one or more operating systems. In a data center, servers are placed in **racks** (metal cabinets), and many racks are collected in a server hall.

**Virtualization** makes it possible to run multiple virtual machines (VMs) on one physical server. A **hypervisor** is the software that manages the VMs. The most common hypervisors are:

- **VMware ESXi** – industry standard, widely used in enterprises
- **Microsoft Hyper-V** – built into Windows Server
- **KVM** – open source, used in Linux environments

Virtualization provides better resource utilization, easier administration, and faster deployment of new servers. See [[virtuelle-losninger-en]] for a deeper look at virtualization technology.

**Containers** (e.g., Docker) are a lighter form of virtualization that share the operating system kernel between applications. Kubernetes is used to orchestrate containers at scale.

---

### Network Components

A local network (LAN) consists of several key components:

| Component | Function |
|-----------|----------|
| **Switch** | Connects devices in a local network. Operates at layer 2 (MAC addresses). |
| **Router** | Connects different networks. Operates at layer 3 (IP addresses). Routes traffic between LAN and WAN. |
| **Firewall** | Controls and filters network traffic based on rules. First line of defense against attacks. |
| **DMZ** | Demilitarized zone – an isolated network segment for services accessible from the internet (e.g., web server). |
| **VLAN** | Logical network segmentation without physical separation. Used for security and performance. |
| **Wireless Access Point (AP)** | Provides Wi-Fi access to the network. |

See [[brannmur-en]] and [[segmentering-og-vlan-en]] for more on these components.

---

### Storage Types

Storage is a critical part of the operations architecture. The three main types are:

**DAS – Direct Attached Storage**
Storage connected directly to one server (e.g., internal hard drive or external disk over USB/SAS). Simple and fast, but cannot be shared between servers.

**NAS – Network Attached Storage**
A dedicated storage unit connected to the network. All servers and clients on the network can access files via protocols such as SMB (Windows) or NFS (Linux). Typically used for file sharing and backup.

**SAN – Storage Area Network**
A dedicated high-speed network for storage, separate from the regular data network. Uses protocols such as Fibre Channel or iSCSI. Provides very fast access and is used in organizations with high performance requirements (e.g., databases).

**Cloud object storage**
Cloud storage (e.g., Azure Blob Storage, AWS S3) is suitable for large amounts of unstructured data such as images, videos, and backups. Highly scalable and cost-effective.

---

### Client Equipment

End-user equipment is called client equipment and includes:
- PCs and laptops
- Tablets and mobile phones (BYOD – Bring Your Own Device)
- Thin clients – inexpensive devices that connect to a terminal server

---

### UPS and Redundancy

**UPS (Uninterruptible Power Supply)** is a battery system that provides power during outages. It ensures that servers and network equipment can shut down gracefully – or continue running – when the power goes out.

**Redundancy** means that critical components exist in duplicate, so the system continues to function if one component fails:
- Redundant power supplies in servers
- Redundant network connections (bonding/failover)
- RAID (Redundant Array of Independent Disks) for storage
- Redundant internet connections from different providers

---

### Infrastructure as Code (IaC)

Modern operations architecture is not only about which components exist – it is also about how they are configured and maintained. **Infrastructure as Code (IaC)** is a method where IT infrastructure is described and managed via machine-readable configuration files instead of manual configuration.

Advantages of IaC:
- Reproducible infrastructure – the same configuration always produces the same result
- Version control – changes are tracked as code
- Automated deployment – faster and more reliable than manual work

Tools: Terraform (infrastructure), Ansible (configuration), Azure ARM templates. See [[automatisering-en]] for more.

---

### Typical Architecture for an SMB

A small to medium-sized business (SMB) might have an architecture like this:

```
[Internet]
     |
[Firewall/Router]
     |
[Core Switch]
  /       \
[Server VLAN]   [Client VLAN]
  |               |
[Virtual         [PCs, laptops,
 servers,        printers]
 NAS, UPS]
```

In addition, some services may reside in the cloud (e.g., email via Microsoft 365, backup to Azure), resulting in a hybrid architecture. Good [[dokumentasjon-og-planlegging-en]] ensures that all components are mapped and that changes are tracked.

---

## Example / Lab

**Task: Map the architecture at your school**

1. Find out which network components exist at the school (switch, router, firewall).
2. Are there any services that run in the cloud? (e.g., Microsoft 365, Google Workspace)
3. Draw a simplified architecture diagram in draw.io or on paper.
4. Identify which type of storage is used for the file server (DAS, NAS, or SAN).

**Additional task: Evaluate IaC**

Look at an example of an Azure ARM template or Terraform configuration (many open examples exist on GitHub). Discuss: What is the advantage of describing infrastructure as code versus configuring manually in a web interface?

---

## Study Guide

### Core Content

Operations architecture is about how IT systems are built and what choices are made for the placement, scaling, and security of infrastructure.

**The three models:**
- **On-premise** – full control, high CAPEX, no dependence on internet
- **Public cloud** – elastic, OPEX model, dependent on provider
- **Hybrid** – combination, most common in Norwegian enterprises

**Servers and virtualization:**
- Hypervisor enables multiple VMs on one physical server (VMware, Hyper-V, KVM)
- Containers (Docker/Kubernetes) are lighter than VMs and share the OS kernel
- IaC automates and version-controls infrastructure setup

**Network components:**
- Switch (layer 2), router (layer 3), firewall (filtering), VLAN (segmentation), DMZ (public services)
- Redundancy and UPS ensure continuity during failures

**Storage:**
- DAS (directly attached, one server only), NAS (network sharing, SMB/NFS), SAN (high-speed block storage, Fibre Channel/iSCSI)
- Cloud object storage for unstructured data and backups

**Remember:** CAPEX vs. OPEX is not just a cost decision – it is a strategic decision about control, flexibility, and risk. Hybrid cloud is a deliberate combination, not a compromise.

---

## FAQ

**What is the actual difference between a switch and a router?**
A switch connects devices within the same network using MAC addresses (layer 2). A router connects different networks and routes traffic based on IP addresses (layer 3). In practice: the switch connects PCs in the classroom, the router sends traffic from the classroom out to the internet.

**Why do many organizations choose hybrid cloud instead of only cloud or only on-premise?**
Hybrid cloud provides flexibility: sensitive data and systems with strict GDPR requirements can remain local, while scalable and variable services can run in the cloud. It is also easier to migrate gradually than to move everything at once.

**What is RAID and what does it protect against?**
RAID (Redundant Array of Independent Disks) is a technology that spreads data across multiple hard drives for redundancy and/or performance. RAID 1 mirrors data (one disk can fail without data loss). RAID 5/6 combines performance and fault tolerance. RAID is not a backup – it protects against disk failure, not against accidental deletion or ransomware.

**What is meant by "latency" and why is it important in architecture choices?**
Latency is the delay in communication between client and server. An application that requires fast response (e.g., a real-time inventory system) should have low latency – which may favor local hosting over cloud. Choosing a cloud region (close to users) reduces latency.

**What is IaC and is it relevant at VG2 level?**
Infrastructure as Code (IaC) is describing server setup and network configuration in text files that can be version-controlled and run automatically. It is relevant because it is the standard in modern IT operations – even if you do not code yourself, it is important to understand the principle and see that "manual clicking" is becoming obsolete.

**What is a DMZ and why is it important?**
A DMZ (Demilitarized Zone) is an isolated network between the internet and the internal network. Services such as web servers and email servers, which should be accessible from the internet, are placed here. This means a compromise of a DMZ server is not automatically an entry ticket to the internal network.

---

## Quiz

<details><summary>Question 1: What is the difference between CAPEX and OPEX in relation to IT operations?</summary>

**Answer:** CAPEX (Capital Expenditure) is large one-time expenses for purchasing equipment and infrastructure, typically for on-premise. OPEX (Operational Expenditure) is ongoing operating expenses, typically for cloud services where you pay monthly for what you use.

</details>

<details><summary>Question 2: What does a hypervisor do?</summary>

**Answer:** A hypervisor is software that allows one physical server to run multiple virtual machines (VMs) simultaneously. It allocates resources (CPU, memory, storage) between the VMs and isolates them from each other.

</details>

<details><summary>Question 3: What is the difference between NAS and SAN?</summary>

**Answer:** NAS (Network Attached Storage) is a file server connected to the regular network and offers file sharing via SMB/NFS. SAN (Storage Area Network) is a dedicated high-speed network for storage that provides block-based access to servers – as if the disk were locally attached. SAN is faster and used for performance-intensive applications.

</details>

<details><summary>Question 4: What is a DMZ in network architecture?</summary>

**Answer:** A DMZ (Demilitarized Zone) is an isolated network segment between the internet and the internal network. Services that need to be accessible from the internet (e.g., web servers) are placed here, so that an attack against these does not provide direct access to the internal network.

</details>

<details><summary>Question 5: What is hybrid cloud and why is it common in Norwegian organizations?</summary>

**Answer:** Hybrid cloud combines local on-premise infrastructure with public cloud services. It is common because it provides flexibility: sensitive data and systems with strict GDPR requirements can remain local, while scalable services and backups can reside in the cloud. It also enables cost optimization.

</details>

---

## Resources

- [Microsoft Azure: What is IaaS?](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-iaas/)
- [Microsoft Learn AZ-900: IaaS](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/2-describe-infrastructure-service)
- [AWS: What is cloud computing?](https://aws.amazon.com/what-is-cloud-computing/)
- [NDLA: Driftsarkitektur](https://ndla.no/nb/subject:1:34375b6a-9a99-4d64-884d-2a3164a27521/topic:2:183915/resource:1:160358)
- [SNL: Skytjeneste](https://snl.no/skytjeneste)
- [YouTube: What is Cloud Computing? – Amazon Web Services](https://www.youtube.com/watch?v=mxT23V-pS0I)
- [[skytjenester-en]]
- [[backup-og-gjenoppretting-en]]
- [[dokumentasjon-og-planlegging-en]]
