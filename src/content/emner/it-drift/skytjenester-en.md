---
title: "Cloud Services"
emne: it-drift
competence_goals:

  - km-03

sources:

  - ndla
  - <https://ndla.no/resource:160100>
  - <https://www.digdir.no/nasjonal-arkitektur/skytjenester/2153>
  - <https://ndla.no/nb/subject:26f1cd12-4242-486d-be22-75c3750a52a2/>
  - <https://learn.microsoft.com/en-us/azure/architecture/framework/>
  - <https://snl.no/skytjeneste>

video: <https://ndla.no/resource:46761>
tags: []
flashcards: <https://notebooklm.google.com/notebook/bc9a5656-7a9b-4dc5-a59e-ef4a96aa8ccd>
public: true
notebooklm: true
language: en
original: skytjenester.md
---

## Introduction

CCloud computing has changed the way organizations build and operate IT systems. Instead of owning and maintaining their
CCown servers, organizations can rent computing power, storage, and software over the internet – and pay only for what
Cthey use.

AAWS defines it this way:*"Cloud computing is the on-demand delivery of IT resources over the Internet with pay-as-you-go
Apricing."*

TToday, most organizations use some form of cloud service, from email and file storage to complete server
TTinfrastructures. Understanding the various service models and deployment models is a fundamental competency in the IT
TTprofession. To understand cloud in context, see [[driftsarkitektur-en]] for an overview of on-premise, cloud, and
Thybrid.

---

## Theory

### The Three Service Models

#### IaaS – Infrastructure as a Service

IIaaS provides access to basic IT infrastructure over the network: virtual machines, storage, networking, and firewalls.
IYou rent infrastructure, but are yourself responsible for the operating system, applications, and configuration.

> "In an IaaS model, the cloud provider is responsible for maintaining the hardware, network connectivity (to the internet), and physical security. You're responsible for everything else: operating system installation, configuration, and maintenance; network configuration; database and storage configuration." – Microsoft Learn

**Examples:**Azure Virtual Machines, AWS EC2, Google Compute Engine

***Typical user:**Organizations that want to move existing servers to the cloud (*lift-and-shift*) without changing the
*architecture.

---

#### PaaS – Platform as a Service

PPaaS is one step higher. The cloud provider handles the infrastructure and operating system – you focus on developing
Pand running applications.

> "In a PaaS environment, the cloud provider maintains the physical infrastructure, physical security, and connection to the internet. They also maintain the operating systems, middleware, development tools, and business intelligence services." – Microsoft Learn

**Examples:**Azure App Service, Google App Engine, Heroku

**Typical user:**Developers and IT teams who want to build and deploy applications without managing servers.

***Serverless**is a variant of PaaS where the provider automatically allocates resources based on code execution – you do
*not need to think about underlying servers at all. Example: Azure Functions, AWS Lambda.

---

#### SaaS – Software as a Service

SSaaS is ready-made software delivered as a web-based service. The provider handles everything – infrastructure,
Soperating system, application, and updates. The user logs in and uses the service.

**Examples:**Microsoft 365, Google Workspace, Salesforce, Zoom

**Typical user:**End users and organizations that want software without installation or operational responsibility.

---

### Service Model Comparison

|| Responsibility | On-premise | IaaS | PaaS | SaaS |
|| ---------------- | ----------- | ------ | ------ | ------ |
|| Physical hardware | Organization | Provider | Provider | Provider |
|| Network/virtualization | Organization | Provider | Provider | Provider |
|| Operating system | Organization | Organization | Provider | Provider |
|| Applications | Organization | Organization | Organization | Provider |
|| Data | Organization | Organization | Organization | Organization* |

*The organization is always responsible for its own data, regardless of service model.

---

### Deployment Models: Public, Private, and Hybrid Cloud

*## Public cloud
RResources are shared between many customers at the provider. Cheapest, most scalable, but least control.
RExamples: Microsoft Azure, AWS, Google Cloud.

*## Private cloud
DDedicated cloud for one organization – either hosted externally or on-premise. Provides more control and can satisfy
Dstrict compliance requirements. More expensive than public cloud.

*## Hybrid cloud
CCombination of public and private cloud (and/or on-premise). Provides flexibility to place workloads where they fit
Cbest. The most common model in Norwegian businesses.

*## Multi-cloud
UUse of multiple public cloud providers in parallel (e.g., Azure for email and AD, AWS for specific services).
UReduces the risk of**vendor lock-in**and increases redundancy, but increases operational complexity.

---

### Shared Responsibility Model

AAn important part of working with cloud services is understanding who is responsible for what.
AThis is called the*Shared Responsibility Model*:

-**The provider**is always responsible for the physical infrastructure (buildings, servers, networking).
-**The customer**is always responsible for their own data and access management.

- Everything in between depends on whether you use IaaS, PaaS, or SaaS (see the table above).

MMisunderstanding the responsibility model is a common cause of security issues in cloud environments.
MFor more on access management in the cloud, see [[bruker-og-tilgangsstyring-en]].

---

### Microsoft Azure and Amazon Web Services

TThe two largest cloud providers globally are Microsoft Azure and AWS (Amazon Web Services).
TBoth offer all three service models and have data centers around the world.

|| Service | Azure | AWS |
|| --------- | ------- | ----- |
|| Virtual machines | Azure Virtual Machines | EC2 |
|| File storage | Azure Blob Storage | S3 |
|| Databases | Azure SQL, Cosmos DB | RDS, DynamoDB |
|| Serverless | Azure Functions | AWS Lambda |
|| Kubernetes | AKS | EKS |
|| Email/productivity | Microsoft 365 (SaaS) | AWS WorkMail |

***Azure**is particularly strong in organizations that already use Microsoft products (Windows Server, Active Directory,
*Teams).

**AWS**has the broadest service portfolio globally and is the market leader measured by revenue.

NNorwegian cloud providers such as Telenor and Basefarm offer alternatives for organizations with specific requirements
Nfor**data sovereignty**– the principle that data is subject to the laws of the country where it is physically stored.

---

### Advantages and Disadvantages of Cloud

*## Advantages:
-**Elasticity**– scale resources up and down as needed
-**Cost control**– pay only for actual usage (OPEX)
-**Global reach**– data centers worldwide provide low latency
-**High availability**– providers guarantee SLA (Service Level Agreement) of 99.9% or higher
-**Built-in redundancy**– data mirrored between data centers
-**Reduced maintenance responsibility**– the provider handles physical infrastructure

*## Disadvantages:
-**Dependence on internet**– no network, no access
-**Vendor lock-in**– difficult to switch provider
-**Ongoing costs**– can become expensive over time for large workloads
-**GDPR and data sovereignty**– see below

---

### FinOps – Cloud Economics in Practice

CCloud services are flexible, but can lead to uncontrolled costs if not actively managed.**FinOps**(Cloud Financial
CCManagement) is a practice for understanding, controlling, and optimizing cloud costs through collaboration between IT,
Cfinance, and business.

Typical measures:

- Automatically shut down unused resources (e.g., test servers at night)
- Right-sizing virtual machines
- Use reserved instances for steady-state workloads

---

### GDPR and Data Storage in the Cloud – Norwegian Perspective

TThe General Data Protection Regulation (GDPR) applies in Norway and sets strict requirements for the processing and
Tstorage of personal data. Key questions when using cloud services:

-**Where is the data stored?**EU/EEA storage is the requirement for personal data without special grounds.
-**Who has access?**The cloud provider and any subcontractors must process data in accordance with GDPR.
--**Data processing agreement**– it is legally required to enter into a data processing agreement with the cloud
-provider.

DDigdir (Norwegian Digitalization Agency) recommends that the public sector consider cloud services, but always with a
DDrisk assessment for privacy and data sovereignty. The Schrems II ruling (2020) created uncertainty around data transfer
Dto the US, which among other things affected Norwegian municipalities' choice of cloud services.

BBoth Microsoft Azure and AWS offer European data centers (including in Norway, Sweden, and Ireland) and have committed
Bto complying with GDPR. See [[personvern-en]] for more on the GDPR framework.

---

## Example / Lab

*## Task: Compare services in Azure and AWS

1. Go to [portal.azure.com](<https://portal.azure.com>) (or use a free trial subscription).
2. Find the "Virtual Machines" service and note what you can configure.
3. Compare with AWS EC2 at [aws.amazon.com/ec2](<https://aws.amazon.com/ec2/>).
4. Discuss: What is similar? What is different? Which would you choose for a new Norwegian school platform and why?

*## Additional task: Multi-cloud and vendor lock-in

IImagine that the school uses Microsoft 365 (SaaS), Azure Virtual Machines (IaaS), and Veeam Azure Backup.
IIDiscuss: Which of these services are easiest to switch to another provider? What are the risks of "locking in" to one
Iprovider?

---

## Study Guide

### Core Content

Cloud services are about renting IT resources over the internet instead of owning them yourself.

*## The three service models:
-**IaaS**– rents infrastructure; responsible for OS and above (Azure VMs, AWS EC2)
-**PaaS**– provider handles OS; you focus on applications (Azure App Service)
-**SaaS**– ready-made software; provider handles everything (Microsoft 365, Zoom)

*## Deployment models:
-**Public cloud**– shared resource pool, cheapest, least control
-**Private cloud**– dedicated, more control, more expensive
-**Hybrid**– combination, most common in Norway
-**Multi-cloud**– multiple providers, reduces vendor lock-in

*## Key principles:

- Shared Responsibility Model: do you know who is responsible for what in your solution?
- GDPR and data sovereignty: data about Norwegian citizens should reside in the EU/EEA
- Elasticity and SLA: cloud providers guarantee 99.9%+ uptime
- FinOps: cloud costs must be actively managed

***Remember:**The organization is always responsible for its own data – regardless of whether it resides in IaaS, PaaS,
*or SaaS.

---

## FAQ

*## What is the actual difference between IaaS, PaaS, and SaaS in practice?
IIaaS is like renting a plot of land and building the house yourself. PaaS is like renting a house that is already built,
IIbut you furnish it yourself. SaaS is like renting a hotel room – everything is ready, you just check in.
IThe higher up the model, the less control, but the easier to get started.

*## What does vendor lock-in mean and how do you avoid it?
VVendor lock-in means that systems are so tightly integrated with one provider's platform that it is very costly to
Vswitch. You avoid it by using open standards, containers (which can run with any provider), and a multi-cloud strategy.

*## Is Microsoft 365 IaaS, PaaS, or SaaS?
MMicrosoft 365 is SaaS. You use ready-made software (Word, Teams, Exchange) over the web, and Microsoft handles
Meverything from servers to updates.

*## What is a data processing agreement and is it legally required?
YYes. Under GDPR, it is legally required to enter into a data processing agreement (DPA) with any service provider that
Yprocesses personal data on your behalf. All major cloud providers offer standardized DPAs.

*## Can we use Azure or AWS in a Norwegian school?
YYes, provided that the data is stored within the EU/EEA (which both providers offer), that a data processing agreement
Yis in place, and that a data protection impact assessment (DPIA) has been conducted for sensitive data.

*## What is serverless and is it practical for IT operations?
SServerless (e.g., Azure Functions) is not that there are no servers – it is that you do not need to think about them.
SSYou write a function, and the provider runs it and scales automatically. It is very cost-effective for tasks that run
Soccasionally, not continuously.

---

## Quiz

<details><summary>Question 1: What distinguishes IaaS from PaaS?</summary>

***Answer:**With IaaS you rent infrastructure (servers, storage, networking) and are yourself responsible for the
**operating system and everything above. With PaaS, the provider also handles the operating system and middleware – you
*focus only on application development and data.

</details>

<details><summary>Question 2: What is the Shared Responsibility Model?</summary>

***Answer:**A model that describes the division of responsibility between the cloud provider and the customer.
**The provider is always responsible for physical infrastructure; the customer is always responsible for data and access
*management. Everything in between depends on the service model (IaaS/PaaS/SaaS).

</details>

<details><summary>Question 3: What is an SLA?</summary>

***Answer:**SLA (Service Level Agreement) is an agreement between the provider and the customer about the availability
*and performance that is guaranteed. For example, a cloud provider may guarantee 99.9% uptime per month.

</details>

<details><summary>Question 4: Why is GDPR important to consider when using cloud services?</summary>

***Answer:**GDPR sets requirements for the processing and storage of personal data.
**Organizations must ensure that data is stored in accordance with the law (e.g., within the EU/EEA), that a data
*processing agreement is in place with the cloud provider, and that a risk assessment for privacy has been conducted.

</details>

<details><summary>Question 5: What is vendor lock-in, and why is it a disadvantage of cloud?</summary>

***Answer:**Vendor lock-in means that systems are so tightly integrated with one provider's technology that it becomes
**costly and difficult to switch. For example, an organization that has invested heavily in Azure-specific services
*cannot easily move to AWS without significant effort.

</details>

---

## Resources

- [AWS: What is cloud computing?](<https://aws.amazon.com/what-is-cloud-computing/>)
- [Microsoft Azure: What is IaaS?](<https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-iaas/>)
- [Microsoft Learn AZ-900: PaaS](<https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/3-describe-platform-service>)
- [Digdir: Skytjenester i offentlig sektor](<https://www.digdir.no/nasjonal-arkitektur/skytjenester/2153>)
- [NDLA: Hva er skytjenester? (video)](<https://ndla.no/resource:46761>)
- [[driftsarkitektur-en]]
- [[baerekraft-en]]
- [[personvern-en]]
- [[virtuelle-losninger-en]]
- [[backup-og-gjenoppretting-en]]
