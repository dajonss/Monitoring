from monitoring import get_cpu_usage, get_ram_usage, get_disk_usage
from alarms import cpu_alarm, ram_alarm, hdd_alarm
from alarms import cpu_alarm_set, ram_alarm_set, hdd_alarm_set


starta_overvakning = False
# Main menu Options
def main_menu():
    print("1. Start monitoring")
    print("2. Show current monitoring")
    print("3. Create Alarm")
    print("4. Show Alarms")
    print("5. Start monitoring-mode")
    print("6. Exit")

# Menyval 1
def start_monitoring():
    global starta_overvakning
    starta_overvakning = True
    print("Starting monitoring..")

# Menyval 2
def current_monitoring():
    if starta_overvakning is True:
        get_cpu_usage()
        get_ram_usage()
        get_disk_usage()
        input("Press any key to return to main menu...")
        main_menu_loop()
    else:
        input("Start the monitoring to see current usages, press any key to continue..")
        main_menu_loop()


# Menyval 3
def create_alarms():
    print("1. CPU Usage")
    print("2. RAM Usage")
    print("3. HDD Usage")
    print("4. Return to Main Menu..")
    while True:
        create_alarm = input("Choose an option: ")
        if create_alarm == "1":
            cpu_alarm()
            break
        elif create_alarm == "2":
            ram_alarm()
            break
        elif create_alarm == "3":
            hdd_alarm()
            break
        elif create_alarm == "4":
            main_menu_loop()
        else:
            print("ERROR: Choose a valid option in the menu..")

# Menyval 4
def show_alarms():
    #print(f"CPU Alarm set to: {cpu_alarm_set}%")
    for i in range(len(cpu_alarm_set)):
        print(f"CPU Alarm set to: {cpu_alarm_set[i]}%")

    for i in range(len(ram_alarm_set)):
        print(f"RAM Alarm set to: {ram_alarm_set[i]}%")
        
    for i in range(len(hdd_alarm_set)):
        print(f"HDD Alarm set to: {hdd_alarm_set[i]}%")
    
# Menyval 5
def start_monitoring_mode():
    print("Starting monitoring-mode... ")
# Main Menu Loop
def main_menu_loop():
    while True:
        main_menu()
        option = input("Choose an option: ")
        if option == "1":
            start_monitoring()
            input("Press any key to return to main menu...")
        elif option == "2":
            current_monitoring()
            input("Press any key to return to main menu...")
        elif option == "3":
            create_alarms()
            input("Press any key to return to main menu...")
        elif option == "4":
            show_alarms()
            input("Press any key to return to main menu...")
        elif option == "5":
            start_monitoring_mode()
            input("Press any key to return to main menu...")
        elif option == "6":
            exit()
        else:
            print("Error: Choose a valid option")
print()
print()
print()
print()
print("Welcome to the monitoring program")
main_menu_loop()
