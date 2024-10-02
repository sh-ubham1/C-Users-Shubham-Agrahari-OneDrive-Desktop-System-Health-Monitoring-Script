import psutil
import time

# Define threshold values
CPU_THRESHOLD = 80  # 80%
MEMORY_THRESHOLD = 80  # 80%
DISK_THRESHOLD = 80  # 80%

def monitor_system_health():
    # Check CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        print(f"ALERT! CPU usage is high: {cpu_usage}%")

    # Check Memory usage
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        print(f"ALERT! Memory usage is high: {memory_usage}%")

    # Check Disk usage
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        print(f"ALERT! Disk usage is high: {disk_usage}%")

if __name__ == "__main__":
    while True:
        monitor_system_health()
        time.sleep(5)  # Monitor every 5 seconds
