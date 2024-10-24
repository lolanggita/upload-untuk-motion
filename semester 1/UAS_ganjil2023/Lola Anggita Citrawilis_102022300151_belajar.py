# Libraries
import os
import sys
import datetime
import math

# Dictionaries
USER = {
    "Zeff": {"password": "alesimp123", "role": "admin"},
    "Kin": {"password": "kin123", "role": "worker"}
}

PARKING = {
    "A01": {"type": "car", "status": "idle", "plate": " "},
    "A02": {"type": "car", "status": "idle", "plate": " "},
    "A03": {"type": "car", "status": "idle", "plate": " "},
    "A04": {"type": "car", "status": "idle", "plate": " "},
    "A05": {"type": "car", "status": "idle", "plate": " "},
    "B01": {"type": "car", "status": "idle", "plate": " "},
    "B02": {"type": "car", "status": "idle", "plate": " "},
    "B03": {"type": "car", "status": "idle", "plate": " "},
    "B04": {"type": "car", "status": "idle", "plate": " "},
    "B05": {"type": "car", "status": "idle", "plate": " "},
    "C01": {"type": "motorcycle", "status": "idle", "plate": " "},
    "C02": {"type": "motorcycle", "status": "idle", "plate": " "},
    "C03": {"type": "motorcycle", "status": "idle", "plate": " "},
    "C04": {"type": "motorcycle", "status": "idle", "plate": " "},
    "C05": {"type": "motorcycle", "status": "idle", "plate": " "},
    "D01": {"type": "motorcycle", "status": "idle", "plate": " "},
    "D02": {"type": "motorcycle", "status": "idle", "plate": " "},
    "D03": {"type": "motorcycle", "status": "idle", "plate": " "},
    "D04": {"type": "motorcycle", "status": "idle", "plate": " "},
    "D05": {"type": "motorcycle", "status": "idle", "plate": " "}
}
HISTORY = {}    # "Id": {"Plate", "Type", "Park", "Entry", "Exit", "Payment"}
# Function to handle user login


def Login():
    loop_function = True

    while loop_function:
        print("*Type '9' if you want to close the app.")
        print("=========================================")

        try:
            username = input("|| Enter your username: ")

            if username == '9':
                raise SystemExit(
                    "==========================================\n|| Thank you for using the application. ||\n==========================================")

            password = input("|| Enter your password: ")

            if username in USER and USER[username]["password"] == password:
                print("Login successful!")
                loop_function = False
                return USER[username]["role"]
                break

            else:
                raise ValueError("Invalid username or password.")

        except SystemExit as se:
            print(se)
            sys.exit()

        except ValueError as ve:
            print(ve)


def Admin_Menu():
    # os.system('cls')
    loop_function = True

    while loop_function == True:
        print("======================")
        print("|| " + "Admin Menu:".center(16) + " ||")
        print("======================")
        print("|| 1. Vehicle Entry".ljust(19) + " ||")
        print("|| 2. Vehicle Exit".ljust(19) + " ||")
        print("|| 3. View History".ljust(19) + " ||")
        print("|| 0. Logout".ljust(19) + " ||")
        print("======================")

        try:
            choice = input("Enter your choice: ")

            if choice == "1":
                Vehicle_Entry("admin")
            elif choice == "2":
                Vehicle_Exit("admin")
            elif choice == "3":
                View_History()
            elif choice == "0":
                loop_function = False
                exit
            else:
                raise ValueError("Invalid choice")

        except ValueError as e:
            print(e)

        finally:
            if choice == "9":
                print("==========================================")
                print("|| Thank you for using the application. ||")
                print("==========================================")
                left_ = input("Press Enter to exit.")
                sys.exit()


def Worker_Menu():
    # os.system('cls')
    loop_function = True

    while loop_function == True:
        print("======================")
        print("|| " + "Worker Menu:".center(16) + " ||")
        print("======================")
        print("|| 1. Vehicle Entry".ljust(19) + " ||")
        print("|| 2. Vehicle Exit".ljust(19) + " ||")
        print("|| 0. Logout".ljust(19) + " ||")
        print("======================")

        try:
            choice = input("Enter your choice: ")

            if choice == "1":
                Vehicle_Entry("worker")

            elif choice == "2":
                Vehicle_Exit("worker")

            elif choice == "0":
                loop_function = False
                exit

            else:
                raise ValueError("Invalid choice")

        except ValueError as e:
            print(e)

        finally:
            if choice == "9":
                print("==========================================")
                print("|| Thank you for using the application. ||")
                print("==========================================")
                left_ = input("Press Enter to exit.")
                sys.exit()


def Menu(role):
    if role == "admin":
        Admin_Menu()

    elif role == "worker":
        Worker_Menu()


def Vehicle_Entry(role):
    loop_ = True
    while loop_ == True:
        print("=================================")
        print("||        Vehicle Entry        ||")
        print("=================================")
        plate = str(input("|| Enter vehicle plate: "))

        if len(HISTORY) != 0:

            for x in reversed(HISTORY):

                if plate == HISTORY[x]["plate"] and HISTORY[x]["fee"] == "0":
                    done = input("*This vehicle is already parked")
                    Menu(role)

                else:
                    loop_ = False
                    break

        else:
            loop_ = False

    loop = True
    while loop == True:
        print("=================================")
        print("|| 1.  Car  || 2.  Motorcycle  ||")
        print("=================================")
        choose = input("|| Enter vehicle type(1/2): ")

        if choose == '1':
            type = 'car'
            loop = False

        elif choose == '2':
            type = 'motorcycle'
            loop = False

        elif choose == '9':
            print("==========================================")
            print("|| Thank you for using the application. ||")
            print("==========================================")
            left_ = input("")
            sys.exit()

        else:
            # os.system('cls')
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
                    print("|| " + x.center(5) + " || " +
                          PARKING[x]["status"].center(8) + " ||")

        elif type == 'motorcycle':

            for x in PARKING:
                if PARKING[x]["type"] == 'motorcycle':
                    print("|| " + x.center(5) + " || " +
                          PARKING[x]["status"].center(8) + " ||")

        print("================================")
        park = input("|| Input parking slot: ")

        if park in PARKING and PARKING[park]["type"] == type:

            if PARKING[park]["status"] == "idle":
                loop = False
                PARKING[park]["status"] = "in use"
                PARKING[park]["plate"] = plate

            else:
                # os.system('cls')
                print("*Parking slot is currently in used.")

        else:
            # os.system('cls')
            print("*Parking slot is not in the list")

    x = datetime.datetime.now()
    time = x.strftime('%Y-%m-%d %H:%M:%S')
    id = plate + x.strftime('%Y%m%d%H%M%S')
    HISTORY[id] = {"plate": str(plate), "type": str(type),
                   "park": str(park), "entry": str(time), "exit": " ", "fee": "0", "id": id}
    print("=================================")
    print("|| Vehicle added successfully. ||")
    print("||           Welcome~          ||")
    done = input("=================================")
    os.system('cls')


def Vehicle_Exit(role):
    exist = False
    while exist == False:
        print("=================================")
        print("||         Vehicle Exit        ||")
        print("=================================")
        plate = input("|| Enter vehicle plate: ")

        y = ''
        for i in HISTORY:  # looping history
            y = i

            if HISTORY[i]["plate"] == plate and PARKING[HISTORY[i]["park"]]["plate"] == plate:
                exist = True
                PARKING[HISTORY[i]["park"]]["status"] = "idle"
                PARKING[HISTORY[i]["park"]]["plate"] = " "
                break

        if HISTORY[y]["plate"] != plate:
            # os.system('cls')
            done = input("*Plate doesnt exist!")
            Menu(role)

    exit_time = datetime.datetime.now()
    time = exit_time.strftime('%Y-%m-%d %H:%M:%S')
    HISTORY[y]["exit"] = time

    os.system('cls')
    print("========================================================")
    print("||" + "Vehicle Exit".center(52) + "||")
    print("========================================================")
    print("|| Plate\t: " + plate.ljust(8) + "||".rjust(30))
    print("|| Entry\t: " + HISTORY[y]["entry"] + "||".rjust(19))
    print("|| Exit\t\t: " + HISTORY[y]["exit"] + "||".rjust(19))
    print("|| Total time\t: " + str(Time_Count(y)).ljust(35) + " ||")
    print("|| Cost\t\t: Rp. " + str(Calculate_Cost(y)).ljust(31) + " ||")
    print("========================================================")
    test = input("Press Enter")

    loop = True
    while loop == True:
        print("\n================= Cashier ===================")
        print("|| Cost\t\t\t: Rp. " + str(Calculate_Cost(y)).ljust(12))
        payment = int(input("|| Enter payment amount\t: Rp. "))

        if payment < Calculate_Cost(y):
            print("*Sorry you don't have enough money!")
            exit

        else:
            print("=============================================")
            print("||                Receipt                  ||")
            print("=============================================")
            print("|| Cost\t\t\t: Rp. " +
                  str(Calculate_Cost(y)).ljust(12) + " ||")
            print("|| Payment\t\t: Rp. " + str(payment).ljust(12) + " ||")
            loop = False
            exchange = payment - Calculate_Cost(y)
            HISTORY[y]["fee"] = str(Calculate_Cost(y))

            if exchange == 0:
                print("=============================================")
                print("||        Data updated successfully.       ||")
                print("||          Thankyou for coming~           ||")
                done = input("=============================================")

            else:
                print(f"|| Change\t\t: Rp. " + str(exchange).ljust(12) + " ||")
                print("=============================================")
                print("||        Data updated successfully.       ||")
                print("||          Thankyou for coming~           ||")
                done = input("=============================================")
            # os.system('cls')


def View_History():
    # HISTORY[id] = {"plate": plate, "type": type, "park": park, "entry": time, "exit": "-", "fee" = fee}
    print("==============================================================================================================================")
    print("|| " + "Parking Id".center(22) + " || " + "Plate".center(8) + " || " + "Type".center(10) +
          " || " + "Park".center(5) + " || " + "Entry".center(19) + " || " + "Exit".center(19) + " || " + "Fee".center(13) + " ||")
    print("==============================================================================================================================")

    for x in HISTORY:
        print("|| " + str(x).center(22) + " || " + str(HISTORY[x]["plate"]).center(8) + " || " + str(HISTORY[x]["type"]).center(10) + " || " + str(
            HISTORY[x]["park"]).center(5) + " || " + HISTORY[x]["entry"].center(19) + " || " + HISTORY[x]["exit"].center(19) + " || " + ("Rp. " + HISTORY[x]["fee"]).ljust(13) + " ||")
    print("==============================================================================================================================")
    test = input("!!Out?!")


# parameter idx itu sama dengan parameter y pada function Vehicle_Exit()
def Time_Count(idx):
    start = datetime.datetime.strptime(
        HISTORY[idx]["entry"], "%Y-%m-%d %H:%M:%S")
    end = datetime.datetime.strptime(HISTORY[idx]["exit"], "%Y-%m-%d %H:%M:%S")

    duration = int((end - start).total_seconds())

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
        hour = int(duration/3600)
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


def Calculate_Cost(idx):
    start = datetime.datetime.strptime(
        HISTORY[idx]["entry"], "%Y-%m-%d %H:%M:%S")
    end = datetime.datetime.strptime(HISTORY[idx]["exit"], "%Y-%m-%d %H:%M:%S")

    duration = int((end - start).total_seconds())

    if duration > 240:
        cost = 40000 + Calculate_Fines(duration)

    else:
        cost = 10000 * math.ceil(duration/60)

    return cost


def Calculate_Fines(duration):
    cost = 40000

    if duration > 360:
        fines = cost * 0.25

    elif duration > 240:
        fines = cost * 0.10

    return fines

# Main function to orchestrate the program


def Main():
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
