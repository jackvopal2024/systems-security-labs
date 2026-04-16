# Automated Cloud Monitor (Azure VM)

**Author:** Jack Vopal  

This project is a Linux-based monitoring and intrusion detection system deployed on an Azure virtual machine. It simulates real-world systems operations tasks such as service monitoring, failure recovery, and basic security analysis.

---

## Overview

The system runs as a background service using `systemd` and continuously monitors system health and security activity.

**Key features:**
- CPU, RAM, and disk monitoring
- Log-based intrusion detection using `/var/log/auth.log`
- Automated service restart on failure
- Firewall hardening with UFW
- Real-time logging and analysis

---

## Key Features

### Background Monitoring Service
- Deployed using `systemd`
- Automatically restarts on failure
- Runs continuously without user interaction

### System Metrics Tracking
- CPU usage
- Memory usage
- Disk utilization

### Intrusion Detection
- Parses `/var/log/auth.log`
- Detects failed SSH login attempts
- Identifies high-frequency attacker IPs

### Failure Simulation
- Manually killed service process
- Verified automatic restart via systemd
- Tested authentication attack scenarios

### Firewall Hardening
- Configured UFW to allow only SSH (port 22)
- Blocked all other inbound traffic

---

## Example Output


[2026-04-10 12:01:00] CPU: 23% | RAM: 41% | Disk: 62% | Status: HEALTHY


---

## What I Learned

- How systemd manages persistent services
- Importance of retry and recovery in production systems
- How exposed servers receive constant automated attacks
- Practical Linux security (permissions, logs, firewall rules)

---

## Future Improvements

- Alerting system (email or webhook)
- Centralized logging (ELK stack)
- Prometheus + Grafana integration
- Multi-region monitoring
