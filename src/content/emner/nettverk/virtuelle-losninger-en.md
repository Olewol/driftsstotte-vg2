---
title: "Virtual Solutions"
emne: nettverk
competence_goals:
  - km-02
language: en
original: virtuelle-losninger.md
kilder:
  - ndla
  - https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/hyper-v-technology-overview
  - https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/
  - https://www.professormesser.com/network-plus/
  - https://www.cloudflare.com/learning/
  - https://learn.microsoft.com/en-us/training/paths/networking-fundamentals/
tags: [virtualization, hyper-v, virtualbox, hypervisor, vm, network]
flashcards: https://notebooklm.google.com/notebook/f7e5ad6c-7082-40cf-abd5-7a41b540f8e1
public: true
video: https://www.youtube.com/watch?v=GidreS70z0U
notebooklm: true
---

# Virtual Solutions

## Introduction

Virtualization is one of the most transformative technologies in modern IT operations. Instead of buying one physical server per service, you can run ten, twenty, or a hundred virtual servers on a single physical machine — with full isolation between them. For IT support technicians, virtualization is fundamental: it's how most corporate servers and network infrastructures are built today.

Virtual solutions are closely connected to [[segmentering-og-vlan|segmentation and VLANs]], since virtual switches support VLAN tagging (IEEE 802.1Q) to integrate VMs into segmented networks. In larger production environments, virtualization is a central element of [[driftsarkitektur|operations architecture]].

## Theory

### What is Virtualization?

Virtualization is the technology that allows a physical computer to run multiple isolated virtual machines (VMs) simultaneously. Each VM runs its own operating system and its own applications, and "thinks" it is an independent physical machine.

A **hypervisor** is the software that manages the virtual machines and distributes physical resources (CPU, RAM, disk, network) among them.

### Type 1 vs. Type 2 Hypervisors

| | Type 1 (Bare Metal) | Type 2 (Hosted) |
|---|---|---|
| **Runs on** | Directly on hardware | On top of a host operating system |
| **Performance** | High (no OS overhead) | Lower (OS layer in the way) |
| **Use case** | Production servers, data centers | Development, testing, education |
| **Examples** | Hyper-V, VMware ESXi, Proxmox | VirtualBox, VMware Workstation |
| **Administration** | Via web interface or mgmt tools | From the host operating system |

#### Type 1: Microsoft Hyper-V

Hyper-V is Microsoft's Type 1 hypervisor and is available as a server role in Windows Server. It can also be enabled as a feature in Windows 10/11 Pro.

Key concepts in Hyper-V:
- **Root partition**: The Windows Server installation with access to actual hardware
- **Child partition (Guest VM)**: The virtual machine that only sees emulated/virtual hardware
- **Generation 1 vs. Generation 2**: Gen 2 supports UEFI and Secure Boot, recommended for modern OS

#### Type 2: Oracle VirtualBox

VirtualBox is free and cross-platform (Windows, macOS, Linux). Well suited for lab exercises where dedicated server hardware is not available.

### Virtual Machines — Characteristics

Each VM has:
- **Virtual CPU** (vCPU) — one or more cores
- **Virtual RAM** — allocated from physical RAM
- **Virtual hard disk** — stored as a file (.vhd, .vhdx, .vmdk) on physical disk
- **Virtual network card** — connected to a virtual switch

Benefits of VMs:
- **Isolation**: a fault or compromise in one VM does not affect others
- **Resource efficiency**: avoids the "one server per service" overconsumption
- **Portability**: a VM can be exported and imported on different hardware
- **Snapshots**: take a point-in-time image of the state — roll back on error
- **Scalability**: easy to clone and scale up
- **Sustainability**: server consolidation reduces power consumption and need for physical hardware

**Isolation** is the principle that a virtual machine is separated from other machines and the host system, so that faults or viruses in one VM do not spread to the rest of the infrastructure.

### Virtual Networks

Hypervisors provide virtual switches (vSwitch) that connect VMs together and to physical networks.

A **virtual switch (vSwitch)** is a software-based network switch that allows virtual machines to communicate with each other and physical networks via VLAN.

#### Hyper-V Virtual Switch — Three Types

| Type | Description | Use Scenario |
|------|-------------|--------------|
| **External** | Connected to physical network card — VMs reach the physical network | Production, lab against real network |
| **Internal** | Communication between host and VMs — not out on physical network | Host manages VMs, shared network |
| **Private** | Only between VMs — host has no access | Isolated test environments |

#### VirtualBox Network Modes

| Mode | VM sees | VM reachable from | Typical Use |
|------|---------|-------------------|-------------|
| **NAT** | Internet via host | Only host (port forwarding) | Simple internet access from VM |
| **Bridged** | Physical network directly | Other machines on the network | VM behaves like physical machine |
| **Host-only** | Only host and other VMs | Only host | Isolated lab network |
| **Internal Network** | Only other VMs | None | Fully isolated VMs |

### VLAN in Virtual Networks

Virtual switches support VLAN tagging. A VM can be assigned a specific VLAN ID, meaning it logically resides in the same VLAN as physical machines in the same segment. This is the key to competence goal km-02: virtual solutions are integrated into the segmented networks.

Example: A Windows Server VM with AD DS is assigned VLAN 30 (Servers), while client VMs are assigned VLAN 10 (Employees) — exactly as physical machines would be placed.

### Practical Use in VG2

**Creating a VM in Hyper-V (simplified):**
1. Hyper-V Manager → Action → New → Virtual Machine
2. Give the VM a name (e.g. `WinServer01`)
3. Choose Generation (Gen 2 for Windows Server 2019/2022)
4. Allocate RAM (minimum 2 GB, recommended 4 GB)
5. Connect to a virtual switch
6. Create virtual hard disk (e.g. 60 GB dynamic)
7. Select installation ISO
8. Complete and start the VM

**Snapshots/checkpoints:**
- Right-click VM → Checkpoint (takes a snapshot)
- Rollback: right-click checkpoint → Apply
- Delete obsolete checkpoints to free up disk space

## Example / Lab

### Lab: Two-Tier Service Architecture with Linux (WebServer + DBServer)

> **Source:** Classroom notes (2ITA)
>
> In class, students set up a two-tier service architecture with two Ubuntu Server VMs in VirtualBox. The goal is to get the osTicket ticketing system running with web server and database on separate machines.
>
> **VM Setup:** Both VMs (WebServer and DBServer) are configured with min. 4 GB RAM, 2 CPUs, and 25 GB disk. Network mode is set to **Bridged Adapter** so the VMs get their own IP addresses on the school network.
>
> **Static IP with Netplan (Ubuntu Server):**
> ```yaml
> network:
>   ethernets:
>     enp0s3:
>       dhcp4: no
>       addresses:
>         - 192.168.52.100/24
>       routes:
>         - to: default
>           via: 192.168.52.5
>       nameservers:
>         addresses: [192.168.52.5, 8.8.8.8]
>   version: 2
> ```
> Activate with `sudo netplan apply`.
>
> **WebServer:** Apache is installed (`sudo apt install apache2 -y`) along with PHP modules required by osTicket. osTicket is downloaded and placed in `/var/www/html/`.
>
> **DBServer:** MariaDB is installed (`sudo apt install mariadb-server -y`). For WebServer to reach the database, `bind-address` in `/etc/mysql/mariadb.conf.d/50-server.cnf` must be changed from `127.0.0.1` to `0.0.0.0`, followed by `sudo systemctl restart mariadb`.

### Lab Scenario: Two VMs on an Isolated Network

Goal: Set up a Windows Server VM and a Windows client VM that communicate only with each other (isolated from the internet).

1. In VirtualBox: create two VMs
2. Both VMs: network mode = "Internal Network", same network name (e.g. "labnet")
3. Windows Server: set static IP `192.168.10.1/24`
4. Windows client: set static IP `192.168.10.2/24`, gateway `192.168.10.1`
5. Test: `ping 192.168.10.1` from the client
6. Install the DHCP role on the server and change the client to dynamic IP

This simulates a production environment without risk to the physical network.

## Study Guide

**Core Understanding: Hypervisors**
Type 1 (bare metal) runs directly on hardware — high performance, used in production (Hyper-V, ESXi, Proxmox). Type 2 runs on top of an OS — simpler, used in labs and development (VirtualBox, VMware Workstation).

**Network Modes in VirtualBox**
NAT: VM shares the host's IP, not visible from outside. Bridged: VM gets its own IP, behaves like a physical machine. Host-only: only between host and VMs. Internal Network: only between VMs.

**VLAN in Virtual Environments**
Virtual switches support VLAN tagging. A VM can belong to a VLAN just like a physical machine. This is central for integrating virtual servers into segmented network architectures.

**Common Exam Points**
- The difference between Type 1 and Type 2 hypervisors
- What a snapshot is and when to use it
- The difference between NAT and Bridged in VirtualBox
- Benefits of virtualization (isolation, efficiency, portability, sustainability)

## FAQ

**What is the difference between a Type 1 and Type 2 hypervisor?**
A Type 1 hypervisor (bare metal) runs directly on hardware without an underlying OS, providing better performance. It is used in production (Hyper-V, VMware ESXi). A Type 2 hypervisor runs as a program on top of a host operating system (VirtualBox, VMware Workstation) — easier to set up, but with somewhat lower performance.

**What is a snapshot/checkpoint in a VM, and why is it useful?**
A snapshot (checkpoint) is a point-in-time image of a VM's state. It allows you to roll back the VM to that state if something goes wrong — e.g. after a failed update or misconfiguration. Indispensable in lab environments.

**What is the difference between NAT and Bridged network mode in VirtualBox?**
In NAT mode, the VM shares the host machine's IP address and reaches the internet through it — but is not directly visible from other machines on the network. In Bridged mode, the VM connects directly to the physical network and gets its own IP address, as if it were a physical machine.

**What three types of virtual switches exist in Hyper-V?**
External (connects VMs to the physical network via the host's network card), Internal (communication between host and VMs, not out on physical network), and Private (only between VMs, host has no access).

**Name three benefits of virtualization in IT operations.**
(Choose three of): Resource efficiency (fewer physical servers), isolation between services, portability (export/import of VMs), snapshots for easy rollback, easy scaling, faster deployment of new servers.

**What is a virtual switch (vSwitch)?**
A software-based network switch that allows virtual machines to communicate with each other and with physical networks. Virtual switches support VLAN tagging so VMs can be placed in logical network segments just like physical machines.

**How does virtualization contribute to sustainability?**
Server consolidation allows one physical server to replace many separate machines. This reduces power consumption, cooling needs, and the amount of physical hardware that must be produced and disposed of — a direct contribution to reduced environmental impact in IT operations.

**What does isolation mean in virtualization?**
Isolation means a VM is separated from other VMs and from the host system. If a VM is compromised by malware, it does not automatically spread to other VMs. This is one of the most important security advantages of virtualization.

## Quiz

<details>
<summary>Question 1: What is the difference between a Type 1 and Type 2 hypervisor?</summary>

**Answer:** A Type 1 hypervisor (bare metal) runs directly on hardware without an underlying OS, providing better performance. It is used in production (Hyper-V, VMware ESXi). A Type 2 hypervisor runs as a program on top of a host operating system (VirtualBox, VMware Workstation) — easier to set up, but with somewhat lower performance.
</details>

<details>
<summary>Question 2: What is a snapshot/checkpoint in a VM, and why is it useful?</summary>

**Answer:** A snapshot (checkpoint) is a point-in-time image of a VM's state. It allows you to roll back the VM to that state if something goes wrong — e.g. after a failed update or misconfiguration. Indispensable in lab environments.
</details>

<details>
<summary>Question 3: What is the difference between NAT and Bridged network mode in VirtualBox?</summary>

**Answer:** In NAT mode, the VM shares the host machine's IP address and reaches the internet through it — but is not directly visible from other machines on the network. In Bridged mode, the VM connects directly to the physical network and gets its own IP address, as if it were a physical machine.
</details>

<details>
<summary>Question 4: What three types of virtual switches exist in Hyper-V?</summary>

**Answer:** External (connects VMs to the physical network via the host's network card), Internal (communication between host and VMs, not out on physical network), and Private (only between VMs, host has no access).
</details>

<details>
<summary>Question 5: Name three benefits of virtualization in IT operations.</summary>

**Answer:** (Choose three of): Resource efficiency (fewer physical servers), isolation between services, portability (export/import of VMs), snapshots for easy rollback, easy scaling, faster deployment of new servers.
</details>

## Flashcards

Hypervisor :: Software that manages virtual machines and distributes physical resources among them
Type 1 hypervisor :: Hypervisor that runs directly on hardware (bare metal): Hyper-V, VMware ESXi, Proxmox
Type 2 hypervisor :: Hypervisor that runs on top of a host operating system: VirtualBox, VMware Workstation
VM (virtual machine) :: Isolated software-simulated computer that runs its own OS on a hypervisor
Snapshot :: Point-in-time image of a VM's state that can be used to roll back changes
Hyper-V external switch :: Virtual switch connected to a physical network card — gives VMs access to the physical network
NAT (VM networking) :: VM shares the host's IP and reaches the internet, but is not directly visible from outside
Bridged (VM networking) :: VM connects directly to the physical network and gets its own IP address
Root partition :: Hyper-V terminology for the Windows Server installation with access to physical hardware
Child partition :: Hyper-V terminology for a guest VM that only sees virtual/emulated hardware
Virtual Switch (vSwitch) :: A software-based network switch that allows virtual machines to communicate with each other and physical networks via VLAN
Isolation :: The principle that a virtual machine is separated from other machines and the host system, so that faults or viruses in one VM do not spread

## Resources

- [Virtualization in Windows Server — NDLA](https://ndla.no/nb/r/teknologiforstaelse-im-ikm-vg1/virtualisering-i-windows-server/5f000530eb)
- [Create Virtual Machine in Hyper-V — NDLA](https://ndla.no/nb/r/yrkesfaglig-fordypning-im-ikm-vg1/opprett-virtuell-maskin-i-hyper-v/23c398aac8)
- [windowsnett.no — lesson 1: virtualization and Windows Server](https://www.windowsnett.no/)
- [Hyper-V Technology Overview — Microsoft Learn](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/hyper-v-technology-overview)
