import psutil
from alarms import cpu_alarm, ram_alarm, hdd_alarm, show_alarms

def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_percent}%")

def get_ram_usage():
    ram_percent = psutil.virtual_memory()[2]
    print(f"RAM Usage: {ram_percent}%")

def get_disk_usage():
    disk_usage = psutil.disk_usage("C:/").percent
    print(f"HDD Usage: {disk_usage}%")



#def monitoring_mode():

