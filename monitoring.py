import psutil
from alarms import cpu_alarm, ram_alarm, hdd_alarm, show_alarms

def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_percent}%")

def get_ram_usage():
    ram = psutil.virtual_memory()
    ram_available = ram.available / (1024**3)
    ram_total = ram.total / (1024**3)
    #print(f"{ram_available} of {ram_total} used")
    print(f"RAM Usage: {ram.percent}% | {round(ram_available, 2)} GB out of {round(ram_total, 2)} GB used." )
    


def get_disk_usage():
    hdd = psutil.disk_usage("C:/")#.percent
    hdd_percent = psutil.disk_usage("C:/").percent
    hdd_free = hdd.free / (1024**3)
    hdd_used = hdd.used / (1024**3)
    print(f"HDD Usage: {hdd_percent}% | {round(hdd_used)} GB out of {round(hdd_free)} GB used.")



#def monitoring_mode():

