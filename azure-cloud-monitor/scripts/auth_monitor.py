### Based on my The SOC Script findings, this script parses the authentication logs to identify automated brute-force attempts.

import os
import subprocess

# Path to system auth logs as identified in the project report
LOG_FILE = "/var/log/auth.log"

def analyze_logs():
    if not os.path.exists(LOG_FILE):
        print(f"Error: {LOG_FILE} not found. Ensure script has proper permissions.")
        return

    # Utilizing grep-style logic to find failed password attempts
    with open(LOG_FILE, 'r') as f:
        failed_attempts = [line for line in f if "Failed password" in line]
    
    print(f"Forensic Analysis: Found {len(failed_attempts)} failed login attempts.")
    
    # Logic to extract unique attacker IPs
    attacker_ips = set()
    for line in failed_attempts:
        parts = line.split()
        if "from" in parts:
            ip_index = parts.index("from") + 1
            attacker_ips.add(parts[ip_index])
            
    for ip in attacker_ips:
        print(f"SECURITY ALERT: Identified brute-force origin - {ip}")
        # Note: In a live SOC environment, this triggers a 'ufw deny' command

if __name__ == "__main__":
    analyze_logs()
