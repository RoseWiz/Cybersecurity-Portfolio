# Muhammad Farhan Budiman

**Cybersecurity Portfolio**

Created as part of WQE7001 Cyber Security.
Documenting my technical skills, hands-on lab projects, and ongoing professional development.

---

## 1. About Me

I am pursuing a Master of Cybersecurity at the University of Malaya and have a background in Information Technology. My interest in cybersecurity began when I realised how everyday digital infrastructure depends on proactive defence and resilient system architecture.

Through hands-on lab work, I have been building practical foundations in network reconnaissance, virtualised lab administration, and vulnerability assessment. This portfolio documents my technical progression, course projects, and ongoing skill development. My goal is to bridge theoretical security principles with verifiable, real-world defensive practices as I prepare to transition into a dedicated security role.

---

## 2. Technical Skills

Levels are my honest self-assessment: **Beginner**, **Working knowledge**, or **Confident**.
 
| Skill | Level | Evidence |
|---|---|---|
| Virtualisation (VMware Workstation) | Working knowledge | [Virtual lab setup](projects/virtual-lab-setup/) |
| Linux command line (Kali) | Working knowledge | [Virtual lab setup](projects/virtual-lab-setup/) |
| TCP/IP and basic network design | Working knowledge | [Virtual lab setup](projects/virtual-lab-setup/) |
| Network scanning with Nmap | Working knowledge | [Virtual lab setup](projects/virtual-lab-setup/) |
| Vulnerability identification and risk rating | Working knowledge | [Virtual lab setup](projects/virtual-lab-setup/) |
| Network reconnaissance tool using scapy | Beginner | [Network Reconnaissance Tool](projects/network-reconnaissance-tool/) |
| Git and GitHub | Working knowledge | This repository's commit history and pull requests |
| Technical writing and documentation | Working knowledge | Project write-ups on this site |

---

## 3. Certifications and Training

**Earned**
 
| Credential | Issuer | Date | Verification |
|---|---|---|---|
| CCNA v.7: Introduction to Networks | Cisco | June 2022 | [Credly Link](https://www.credly.com/badges/b33c0704-f456-46da-9c8b-0c2270ec188c/public_url) |
 
**In progress**
 
| Credential | Issuer | Target completion |
|---|---|---|
| CyberOps Associate v.2 | Cisco | Jan 2027 |
| Network Security | Cisco | Jan 2027 |
| CCNA v.8: Enterprise Networking, Security, and Automation | Cisco | Jan 2027 |
| CCNA v.8: Switching, Routing, and Wireless Essentials | Cisco | Jan 2027 |
| CCNA v.8: Introduction to Networks | Cisco | Jan 2027 |
 
**Practice Platforms**

 TryHackMe | [Profile Link](https://tryhackme.com/p/mfarhanb7)
- TryHackMe room, Cyber Kill Chain: In Progress Dec 2026
- TryHackMe Geolocating Images: Completed Nov 2026

---

## 4. Projects

| Project | Summary |
|---|---|
| [Virtual Lab Setup](projects/virtual-lab-setup/) | Built an isolated Kali Linux and Metasploitable2 lab on VMware Workstation using a host-only network and run a Nmap scan against the lab target and rated the findings. |
| [Network Reconnaissance Tool](projects/network-reconnaissance-tool/) | The objective of this project was to design, build, and empirically validate a scope-enforced **Layer 2 ARP Device Mapper** in Python using **Scapy**, and cross-validate its host discovery results against **Nmap** (`nmap -sn -PR`). Rather than wrapping Nmap inside Python, the tool constructs raw Ethernet/ARP probes directly, enforces strict rate and subnet boundaries before transmitting any packets, deduplicates replies with microsecond UTC timestamps, and exports deterministic JSON results. |
 
*All projects use my own lab. No client or employer data appears anywhere on this site.*

---

## 5. Learning Journey

This semester I studied five cybersecurity courses: WQE7001 Cyber Security, WQE7002 Advanced Network Security Programming, WQE7005 Advance Digital Forensics, WQE7007 Network Technology and Security, and WQE70011 Advanced Computer Penetration and Defence. Together, they moved me from knowing security concepts to applying them in labs.
 
**Lab 1: Building a penetration testing lab (WQE70011).** I built an isolated lab on VMware Workstation, with Kali Linux as the attacker and Metasploitable2 as the target on a host-only network. What I took from it is that safe, authorised practice starts with isolation and scope. The host-only network let me test freely without risk to anyone else's systems, and it gave me an environment I could reuse for other work. In addition, I did a network scan with Nmap to identify vulnerabilities and rate risks.
 
**Lab 2: writing a scan with Scapy (WQE7002).** I used Python's Scapy library to create a simple Nmap-style scan. Building the probes myself, instead of only running a tool, showed me what a scan does on the wire and how the replies reveal whether a port is open or closed. It made tools like Nmap feel less like black boxes.
 
I also gained a framework for thinking about attacks. In WQE7001, TryHackMe's Cyber Kill Chain showed me how an attack unfolds in stages, and where a defender can detect or stop it. In WQE7007, the Cisco Networking Academy courses (ITN, SRWE, ENSA, and Network Security) built the networking foundation this all depends on.
 
**Something that went wrong.** While building a network in Cisco Packet Tracer, I accidentally pasted an IP address into the default gateway field instead of the device's own IP address field. Pings failed even though the devices and cables looked correct. I diagnosed it by checking each device's configuration against my addressing table and testing connectivity step by step, which showed that one device had the wrong value in that field. I corrected it, re-ran the ping tests to confirm, and now verify the address, subnet mask and gateway of every device before testing.
 
**What I still find challenging.** There are two things. The first is absorbing the material from several demanding courses in limited time. The second is turning cybersecurity practice into a programmable setup, because I do not have a strong programming background. Scapy showed me how valuable this skill is, and how much more practice I need.
 
**Improvement goal.** I will complete the TryHackMe Cyber Kill Chain by December 2026, then complete all my university courses and all Cisco Networking Academy certifications by January 2027. I will measure progress by the TryHackMe completion badge, the certificates in my Cisco NetAcad account, and my final course results.

---

## 6. Career Objective

My target role is a junior Security Operations Centre (SOC) analyst, monitoring alerts, investigating suspicious activity and supporting incident response. I am also interested in becoming a governance, risk and compliance (GRC) analyst, which would let me apply the same foundations to policy, risk and compliance work. I want a role where technical understanding and clear communication both matter.
 
My next steps are:
1. Complete the TryHackMe Cyber Kill Chain by December 2026, then complete all my university courses and all Cisco Networking Academy certifications by January 2027.
2. Finish my master's degree by September 2027.
3. Apply for internships and entry-level cybersecurity roles, using this portfolio and my LinkedIn profile as evidence of my skills.

---

## 7. Contact Information

* **Email:** [mfarhanb7@gmail.com]
* **GitHub:** [github.com/RoseWiz](https://github.com/RoseWiz)
* **LinkedIn:** [linkedin.com/in/farhanbudiman](https://www.linkedin.com/in/farhanbudiman)
