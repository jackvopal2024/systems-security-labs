### This script follows the second-edition logic you established using the psutil library to monitor system health in 60-second intervals.

import psutil
import time
import datetime

def monitor_system():
    # Logging the start of the service for journalctl visibility
    print(f"[{datetime.datetime.now()}] Heartbeat Service Started")
    
    while True:
        # Gathering metrics as documented in Phase 2
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        
        # Formatting output for Standard Output (stdout) capture
        print(f"[{datetime.datetime.now()}] STATUS: OK | CPU: {cpu_usage}% | RAM: {ram_usage}% | Disk: {disk_usage}%")
        
        # 60-second sleep interval to manage cloud resource consumption
        time.sleep(60)

if __name__ == "__main__":
    try:
        monitor_system()
    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
