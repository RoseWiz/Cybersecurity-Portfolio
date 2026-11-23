# Muhammad Farhan Budiman | Cybersecurity Portfolio

Created as part of **WQE7001 Cyber Security**.
This site documents my technical skills, hands-on lab projects, and ongoing professional development.

---

## 1. About Me

I am pursuing a Master of Cybersecurity at the University of Malaya and have a background in Information Technology. My interest in cybersecurity began when I realised how everyday digital infrastructure depends on proactive defence and resilient system architecture.

Through hands-on lab work, I have been building practical foundations in network reconnaissance, virtualised lab administration, and vulnerability assessment. This portfolio documents my technical progression, course projects, and ongoing skill development. My goal is to bridge theoretical security principles with verifiable, real-world defensive practices as I prepare to transition into a dedicated security role.

---

## 2. Technical Skills

| Skill / Domain | Proficiency Level | Demonstrating Project |
| :--- | :--- | :--- |
| Virtualisation & Lab Networking (VirtualBox / VMware) | Working Knowledge | [Virtual Lab Setup](./projects/virtual-lab-setup/) |
| Linux Command Line & System Administration | Working Knowledge | [Virtual Lab Setup](./projects/virtual-lab-setup/) |
| Network Reconnaissance & Service Enumeration (Nmap) | Working Knowledge | [Nmap Service Scan](./projects/nmap-service-scan/) |
| Packet Capture & Traffic Inspection (Wireshark) | Beginner | [Nmap Service Scan](./projects/nmap-service-scan/) |
| Version Control & Technical Documentation (Git / GitHub) | Confident | [Portfolio Repository](https://github.com/[your-username]/cybersecurity-portfolio) |

Levels are my honest self-assessment: **Beginner**, **Working knowledge**, or **Confident**.
 
| Skill | Level | Evidence |
|---|---|---|
| Virtualisation (VMware Workstation) | Working knowledge | [Virtual lab setup](projects/virtual-lab-setup/) |
| Linux command line (Kali) | Working knowledge | [Virtual lab setup](projects/virtual-lab-setup/) |
| TCP/IP and basic network design | Working knowledge | [Virtual lab setup](projects/virtual-lab-setup/) |
| Network scanning with Nmap | Working knowledge | [Nmap service scan](projects/nmap-service-scan/) |
| Vulnerability identification and risk rating | Beginner | [Nmap service scan](projects/nmap-service-scan/) |
| Git and GitHub | Beginner | This repository's commit history and pull requests |
| Technical writing and documentation | Working knowledge | Project write-ups on this site |
| Cybersecurity law and ethics (Malaysia, ISC2 Code of Ethics) | Beginner | [Learning journey](#learning-journey) |

---

## 3. Certifications and Training

**Earned**
 
| Credential | Issuer | Date | Verification |
|---|---|---|---|
| CCNA v.7: Introduction to Networks | [Cisco] | [June 2022] | [Credly Link](https://www.credly.com/badges/b33c0704-f456-46da-9c8b-0c2270ec188c/public_url) |
 
**In progress**
 
| Credential | Issuer | Target completion |
|---|---|---|
| CyberOps Associate v.2 | Cisco | [Jan 2027] |
| Network Security | Cisco | [Jan 2027] |
| CCNA v.8: Enterprise Networking, Security, and Automation | Cisco | [Jan 2027] |
| CCNA v.8: Switching, Routing, and Wireless Essentials | Cisco | [Jan 2027] |
| CCNA v.8: Introduction to Networks | Cisco | [Jan 2027] |
 
**Practice Platforms**

 TryHackMe | [Profile Link](https://tryhackme.com/p/mfarhanb7)
- [TryHackMe room, Cyber Kill Chain: In Progress Dec 2026]
- [TryHackMe Geolocating Images: Completed Nov 2026]

---

## 4. Projects

| Project | Summary |
|---|---|
| [Virtual Lab Setup](projects/virtual-lab-setup/) | Built an isolated Kali Linux and Metasploitable2 lab on VMware Workstation using a host-only network. |
| [Nmap Service Scan](projects/nmap-service-scan/) | Ran an authorised Nmap service and version scan against the lab target and rated the findings. |
 
*All projects use my own lab. No client or employer data appears anywhere on this site.*

---

## 5. Learning Journey

Participating in WQE7001 Cyber Security has shifted my approach from passive reading to structured, evidence-based technical practice. Two course topics in particular shaped my understanding: virtualised lab architecture and network reconnaissance. Building an isolated virtual lab environment taught me how network segmentation, host-only adapters, and firewall rules prevent unintended traffic leakage while creating a controlled sandbox for security testing. Similarly, conducting structured service enumeration with Nmap reinforced that effective defence begins with visibility—understanding exactly which ports, services, and software versions are exposed on a host allows administrators to harden configurations and reduce the attack surface before an adversary can exploit outdated daemons.

Not everything went smoothly during my practical lab work. While configuring my virtual network, my Kali Linux testing VM could not communicate with the target machine even though both virtual machines were powered on and running properly. Instead of guessing at settings, I diagnosed the issue systematically from the network layer upward. I inspected interface IP assignments using `ip a`, verified subnet masks, and ran `ping` and `arp-scan` to test local reachability. Through this process, I discovered that one VM was attached to a NAT interface while the other sat on an isolated host-only network, placing them on completely separate subnets. Reconfiguring both virtual adapters onto the same host-only subnet and verifying static IP allocations resolved the connectivity failure immediately.

Despite steady progress across the course labs, packet-level traffic analysis using Wireshark remains an area I still find challenging. While capturing live packets on an interface is straightforward, filtering high-volume traffic streams to isolate subtle anomalies—such as malformed TCP handshakes, suspicious DNS queries, or unencrypted credential transmissions—requires deeper fluency in protocol headers and display filter syntax. Reading raw hex dumps and reliably distinguishing benign background network noise from genuine indicators of compromise still takes me considerable time and manual cross-referencing.

To address this gap, my concrete improvement goal is to achieve intermediate proficiency in network traffic analysis and packet inspection by [Target Date, e.g., January 31, 2027]. I will measure my progress by completing the Wireshark and Network Traffic Analysis modules on TryHackMe, solving at least ten standalone PCAP investigation exercises without relying on walkthroughs, and publishing a documented PCAP analysis write-up to this portfolio. Tracking my accuracy in identifying embedded indicators of compromise across those ten challenges will give me an objective benchmark of my technical growth.

---

## 6. Career Objective

My short-to-medium-term career aspiration is to secure an entry-level role as a Junior Security Operations Centre (SOC) Analyst, Information Security Analyst or GRC (governance, risk and compliance) analyst in a Malaysian organisation, helping teams understand their risks, meet requirements such as the Cyber Security Act 2024, and show evidence that controls work. I chose this path because I enjoy structured problem-solving and clear writing, and because good security decisions depend on both technical understanding and sound policy.

To achieve this target role, I am taking three concrete steps over the next twelve months. First, I will complete the [ISC2 Certified in Cybersecurity (CC) / CompTIA Security+] certification to validate my foundational governance and technical knowledge. Second, I will expand this GitHub portfolio with at least two additional hands-on projects focused on log analysis and SIEM alerting. Third, I will actively participate in local cybersecurity community events and apply for analyst internships and graduate security positions.

---

## 7. Contact Information

* **Email:** [mfarhanb7@gmail.com]
* **GitHub:** [github.com/RoseWiz](https://github.com/RoseWiz)
* **LinkedIn:** [linkedin.com/in/farhanbudiman](https://www.linkedin.com/in/farhanbudiman)
