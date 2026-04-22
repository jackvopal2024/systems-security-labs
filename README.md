# Systems & Security Labs

This repository contains hands-on projects focused on low-level systems, networking, and security concepts. The goal of these labs is to understand how software behaves under the hood, especially in scenarios involving memory, operating systems, and network communication.

## 🧠 Focus Areas
- Memory management and buffer overflows
- Debugging with tools like GDB and WinDbg
- Network communication and protocol behavior
- Basic exploit development in controlled environments
- Automation and scripting (Python/Bash)

---

## 📁 Projects

### 🔹 Apache / WebLogic Overflow (WinDbg)
Performed exploit development against a vulnerable Apache module using Windows debugging tools.

- Attached WinDbg to live process
- Identified vulnerable module and memory layout
- Used cyclic patterns to determine precise offset
- Located `jmp esp` instruction for control flow redirection
- Verified execution using register analysis
- Executed reverse shell in a controlled lab setup

> Focus: Debugging, memory analysis, and controlled exploitation

---

### 🔹 Cloud-Sentinel: Automated Azure Monitoring & SOC Loop

Engineered a persistent monitoring and intrusion detection solution on an Ubuntu Azure instance to identify and neutralize live brute-force attacks.
- **Provisioned** a hardened Ubuntu 24.04 LTS VM with PKI-based access.
- **Developed** a Python "Heartbeat" daemon using `psutil` for real-time telemetry.
- **Orchestrated** service persistence using **systemd** with automated failure recovery.
- **Automated Threat Mitigation** by parsing `/var/log/auth.log` and dynamically updating **UFW firewall** rules to block malicious IPs.

> Focus: Cloud infrastructure, Linux service management, and active defense automation.
