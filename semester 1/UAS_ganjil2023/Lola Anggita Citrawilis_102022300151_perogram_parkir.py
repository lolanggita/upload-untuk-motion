idx = 

def Time_Count(idx):
    start = datetime.datetime.strptime(
        HISTORY[idx]["entry"], "%Y-%m-%d %H:%M:%S")
    end = datetime.datetime.strptime(HISTORY[idx]["exit"], "%Y-%m-%d %H:%M:%S")

    duration = int((end - start).total_seconds())   # output sudah dalam detik


    if duration >= 86400:
        second = int(duration % 60)
        duration -= second
        minute = int((duration % 3600)/60)
        duration -= minute
        hour = int((duration % 86400)/3600)
        duration -= hour
        day = int(duration/86400)
        time = str(day) + " Day " + str(hour) + " Hour " + \
            str(minute) + " Minute " + str(second) + " Second"
    elif duration >= 3600:
        second = int(duration % 60)
        duration -= second
        minute = int((duration % 3600)/60)
        duration -= minute
        hour = int((duration % 86400)/3600)
        time = str(hour) + " Hour " + str(minute) + \
            " Minute " + str(second) + " Second"
    elif duration >= 60:
        second = int(duration % 60)
        duration -= second
        minute = int(duration/60)
        time = str(minute) + " Minute " + str(second) + " Second"
    else:
        second = duration
        time = str(second) + " Second"
    return time





    















##########################  BACK UP  ##########################

# Libraries
import os
import sys
import datetime

# Dictionaries
USER = {
    "Zeff": {"password": "alesimp123", "role": "admin"},
    "Kin": {"password": "kin123", "role": "worker"}
}

PARKING = {
    "A01": {"type": "car", "status": "idle"},
    "A02": {"type": "car", "status": "idle"},
    "A03": {"type": "car", "status": "idle"},
    "A04": {"type": "car", "status": "idle"},
    "A05": {"type": "car", "status": "idle"},
    "B01": {"type": "car", "status": "idle"},
    "B02": {"type": "car", "status": "idle"},
    "B03": {"type": "car", "status": "idle"},
    "B04": {"type": "car", "status": "idle"},
    "B05": {"type": "car", "status": "idle"},
    "C01": {"type": "car", "status": "idle"},
    "C02": {"type": "car", "status": "idle"},
    "C03": {"type": "car", "status": "idle"},
    "C04": {"type": "car", "status": "idle"},
    "C05": {"type": "car", "status": "idle"},
    "D01": {"type": "motorcycle", "status": "idle"},
    "D02": {"type": "motorcycle", "status": "idle"},
    "D03": {"type": "motorcycle", "status": "idle"},
    "D04": {"type": "motorcycle", "status": "idle"},
    "D05": {"type": "motorcycle", "status": "idle"},
    "E01": {"type": "motorcycle", "status": "idle"},
    "E02": {"type": "motorcycle", "status": "idle"},
    "E03": {"type": "motorcycle", "status": "idle"},
    "E04": {"type": "motorcycle", "status": "idle"},
    "E05": {"type": "motorcycle", "status": "idle"},
    "F01": {"type": "motorcycle", "status": "idle"},
    "F02": {"type": "motorcycle", "status": "idle"},
    "F03": {"type": "motorcycle", "status": "idle"},
    "F04": {"type": "motorcycle", "status": "idle"},
    "F05": {"type": "motorcycle", "status": "idle"},
}

HISTORY = {}    # "Id": {"Plate", "Type", "Park", "Entry", "Exit"}

# Function to handle user login
def Login():
    loop_function = True

    while loop_function == True:
        print("*Type \'9\' if you want to close the app.")
        print("=========================================")
        username = input("|| Enter your username: ")
        if username == '9':
            os.system('cls')
            print("==========================================")
            print("|| Thank you for using the application. ||")
            print("==========================================")
            sys.exit()
        password = input("|| Enter your password: ")

        if username in USER and USER[username]["password"] == password:
            print("Login successful!")
            return USER[username]["role"]
            loop_function = False
        else:
            os.system('cls')
            print("*Invalid username or password.")

# Admin Menu
def Admin_Menu():
    os.system('cls')
    loop_function = True

    while loop_function == True:
        print("======================")
        print("|| " + "Admin Menu:".center(16) + " ||")
        print("======================")
        print("|| 1. Vehicle Entry".ljust(19) + " ||")
        print("|| 2. Vehicle Exit".ljust(19) + " ||")
        print("|| 3. View History".ljust(19) + " ||")
        print("|| 4. Add User".ljust(19) + " ||")
        print("|| 9. Logout".ljust(19) + " ||")
        print("======================")
        choice = input("|| Enter your choice: ")

        if choice == "1":
            Vehicle_Entry()
        elif choice == "2":
            Vehicle_Exit()
        elif choice == "3":
            View_History()
        elif choice == "4":
            Add_User()
        elif choice == "9":
            loop_function = False
            exit
        else:
            os.system('cls')
            print("*Invalid choice")

# Function for the worker menu
def Worker_Menu():
    os.system('cls')
    loop_function = True

    while loop_function == True:
        print("======================")
        print("|| " + "Worker Menu:".center(16) + " ||")
        print("======================")
        print("|| 1. Vehicle Entry".ljust(19) + " ||")
        print("|| 2. Vehicle Exit".ljust(19) + " ||")
        print("|| 9. Logout".ljust(19) + " ||")
        print("======================")
        choice = input("|| Enter your choice: ")

        if choice == "1":
            Vehicle_Entry()
        elif choice == "2":
            Vehicle_Exit()
        elif choice == "9":
            loop_function = False
            exit
        else:
            os.system('cls')
            print("*Invalid choice")

def Vehicle_Entry():
    os.system('cls')
    print("=================================")
    print("||        Vehicle Entry        ||")
    print("=================================")
    plate = input("|| Enter vehicle plate: ")

    loop = True
    while loop == True:
        print("=================================")
        print("|| 1.  Car  || 2.  Motorcycle  ||")
        print("=================================")
        choose = input("|| Enter vehicle type(1/2): ")
        if choose == '1' or choose == '2':
            if choose == '1':
                type = 'car'
            elif choose == '2':
                type = 'motorcycle'
            loop = False
        else:
            os.system('cls')
            print("Invalid vehicle type.")
    os.system('cls')
    loop = True
    while loop == True:
        print("=======================")
        print("||   Vehicle Entry   ||")
        print("=======================")
        print("|| Plate: " + plate.center(10) + " ||")
        print("|| Type : " + type.center(10) + " ||")
        print("=======================")
        if type == 'car':
            for x in PARKING:
                if PARKING[x]["type"] == 'car':
                    print("|| " + x.center(5) + " || " + PARKING[x]["status"].center(8) + " ||")
        elif type == 'motorcycle':
            for x in PARKING:
                if PARKING[x]["type"] == 'motorcycle':
                    print("|| " + x.center(5) + " || " + PARKING[x]["status"].center(8) + " ||")
        print("================================")
        park = input("|| Input parking slot: ")
        if park in PARKING and PARKING[park]["type"] == type:
            if PARKING[park]["status"] == "idle":
                loop = False
                PARKING[park]["status"] = "in use"
            else:
                os.system('cls')
                print("*Parking slot is currently in used.")
        else:
            os.system('cls')
            print("*Parking slot is not in the list")
    x = datetime.datetime.now()
    time = str(x.hour).zfill(2) + str(x.minute).zfill(2) + str(x.second).zfill(2)
    id = plate + time
    HISTORY[id] = {"plate": plate, "type": type,
                   "park": park, "entry": time, "exit": "", "id": id}
    print("=================================")
    print("|| Vehicle added successfully. ||")
    print("||           Welcome~          ||")
    done = input("=================================")
    os.system('cls')

def Vehicle_Exit():
    os.system('cls')
    exist = False
    while exist == False:
        print("=================================")
        print("||         Vehicle Exit        ||")
        print("=================================")
        plate = input("|| Enter vehicle plate: ")
        y = ''
        x = datetime.datetime.now()
        time = str(x.hour).zfill(2) + str(x.minute).zfill(2) + str(x.second).zfill(2)
        for x in HISTORY:
            y = x
            if HISTORY[x]["plate"] == plate:
                exist = True
                exit
        if HISTORY[y]["plate"] != plate:
            os.system('cls')
            print("*Plate doesnt exist!")
    HISTORY[y]["exit"] = time
    duration = Duration(HISTORY[y]["entry"], HISTORY[y]["exit"])
    os.system('cls')
    print("========================================================")
    print("||" + "Vehicle Exit".center(52) + "||")
    print("========================================================")
    print("|| Plate\t: " + plate.center(8) + "||".rjust(30))
    print("|| Entry\t: " + HISTORY[y]["entry"][:2] + ":" + HISTORY[y]["entry"][2:4] + ":" + HISTORY[y]["entry"][4:6] + "||".rjust(30))
    print("|| Exit\t\t: " + HISTORY[y]["exit"][:2] + ":" + HISTORY[y]["exit"][2:4] + ":" + HISTORY[y]["exit"][4:6] + "||".rjust(30))
    print("|| Total time\t: " + Time_Count(duration).ljust(35) + " ||")
    print("========================================================")
    test = input("keliatan?")
    os.system('cls')

# Duration Function
def Duration(entry, exit):
    entry_hour = int(entry[:2]) * 3600
    entry_minute = int(entry[2:4])  * 60
    entry_second = int(entry[4:6])
    exit_hour = int(exit[:2]) * 3600
    exit_minute = int(exit[2:4]) * 60   
    exit_second = int(exit[4:6])

    entry_ = entry_hour + entry_minute + entry_second
    exit_ = exit_hour + exit_minute + exit_second

    return exit_ - entry_

# Time Counting function 
def Time_Count(duration):
    if duration >= 86400:
        second = int(duration%60)
        duration -= second
        minute = int((duration%3600)/60)
        duration -= minute
        hour = int((duration%86400)/3600)
        duration -= hour
        day = int(duration/86400)
        time = str(day) + " Day " + str(hour) + " Hour " + str(minute) + " Minute " + str(second) + " Second"
    elif duration >= 3600:
        second = int(duration%60)
        duration -= second
        minute = int((duration%3600)/60)
        duration -= minute
        hour = int((duration%86400)/3600)
        time = str(hour) + " Hour " + str(minute) + " Minute " + str(second) + " Second"
    elif duration >= 60:
        second = int(duration%60)
        duration -= second
        minute = int((duration%3600)/60)
        time = str(minute) + " Minute " + str(second) + " Second"
    else:
        second = duration
        time = str(second) + " Second"
    return time
    
def View_History():
    # HISTORY[id] = {"plate": plate, "type": type, "park": park, "entry": time, "exit": "-"}
    print("===============================================================================")
    print("|| " + "Parking Id".center(14) + " || " + "Plate".center(8) + " || " + "Type".center(10) + " || " + "Park".center(5) + " || " + "Entry".center(8) + " || " + "Exit".center(8)  + " ||")
    print("===============================================================================")
    for x in HISTORY:
        print("|| " + str(x).center(14) + " || " + str(HISTORY[x]["plate"]).center(8) + " || " + str(HISTORY[x]["type"]).center(10) + " || " + str(HISTORY[x]["park"]).center(5) + " || " + str(HISTORY[x]["entry"])[:2].center(2) + ":" + str(HISTORY[x]["entry"])[2:4].center(2) + ":" + str(HISTORY[x]["entry"])[4:6].center(2) + " || " + str(HISTORY[x]["exit"])[:2].center(2) + ":" + str(HISTORY[x]["exit"])[2:4].center(2) + ":" + str(HISTORY[x]["exit"])[4:6].center(2) + " ||")
    print("===============================================================================")
    test = input("!!keliatan?!")


def Add_User():
    username = input("Enter new username: ")
    if username in USER:
        print("Username already exist.")
    else:
        password = input("Enter new password: ")
        role = input("Enter role (admin/worker): ")
        USER[username] = {"password": password, "role": role}
        print("User added successfully.")


# Main function to orchestrate the program
def Main():
    # x = datetime.datetime.now()
    # print(x.hour)
    # print(x.minute)
    # print(x.second)
    loop_main = True

    # Main Program
    while loop_main == True:
        os.system('cls')
        role = Login()

        if role == "admin":
            Admin_Menu()
        elif role == "worker":
            Worker_Menu()
        else:
            print("Exiting program.")

# Run the program
Main()