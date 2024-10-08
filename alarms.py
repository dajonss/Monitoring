# Menyval 3
cpu_alarm_set = []
ram_alarm_set = []
hdd_alarm_set = []

# Set CPU alarm and add to cpu_alarm_set list
def cpu_alarm():
    input_str = input("Enter alarm level for CPU, 1-100%: ")
    if input_str.isdigit():
        user_input = int(input_str)
        if user_input >= 1 and user_input <= 100:
            cpu_alarm_set.append(user_input)
            print(f"CPU Alarm set to: {user_input}%")
        else:
            print("ERROR!\nPlease enter a valid integer between 1-100 and try again.")
    else:
        print("ERROR!\nPlease enter a valid integer between 1-100 and try again.")

# Set RAM alarm and add to ram_alarm_set list
def ram_alarm():
    input_str = input("Enter alarm level for RAM, 1-100%: ")
    if input_str.isdigit():
        user_input = int(input_str)
        if user_input >= 1 and user_input <= 100:
            ram_alarm_set.append(user_input)
            print(f"RAM Alarm set to: {user_input}%")
        else:
            print("ERROR!\nPlease enter a valid integer between 1-100 and try again.")
    else:
        print("ERROR!\nPlease enter a valid integer between 1-100 and try again.")

# Set HDD alarm and add to ram_alarm_set list
def hdd_alarm():
    input_str = input("Enter alarm level for HDD, 1-100%: ")
    if input_str.isdigit():
        user_input = int(input_str)
        if user_input >= 1 and user_input <= 100:
            hdd_alarm_set.append(user_input)
            print(f"HDD Alarm set to: {user_input}%")
        else:
            print("ERROR!\nPlease enter a valid integer between 1-100 and try again.")
    else:
        print("ERROR!\nPlease enter a valid integer between 1-100 and try again.")


def show_alarms():
    for i in range(len(cpu_alarm_set)):
        print(f"CPU Alarm set to: {cpu_alarm_set[i]}%")

    for i in range(len(ram_alarm_set)):
        print(f"RAM Alarm set to: {ram_alarm_set[i]}%")
        
    for i in range(len(hdd_alarm_set)):
        print(f"HDD Alarm set to: {hdd_alarm_set[i]}%")
