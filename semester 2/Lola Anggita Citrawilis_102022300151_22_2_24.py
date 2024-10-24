import os


def Main():
    cost = 0
    
    print("===========================================================")
    print("|| ".ljust(20) + "Warnet Sinar Abadi".center(12) + " ||".rjust(21))
    print("===========================================================")
    duration = int(input("|| ""Masukkan durasi bermain (jam): "))
    member = input(
        "|| " "Apakah Anda anggota program loyalitas?(ya/tidak): ")
    print("===========================================================")

    if duration >= 12:
        cost = 250000
        if member == "ya":
            total = cost - cost * 0.25
        elif member == "tidak":
            total = cost

    elif duration > 1:
        cost = 20000 * duration
        if member == "ya":
            if duration >= 8:
                disc = cost * 0.20
            elif duration > 1:
                disc = cost * 0.15

            total = cost - disc
        elif member == "tidak":
            total = cost

    elif duration == 1:
        cost = 20000
        if member == "ya":
            total = cost - cost * 0.10
        elif member == "tidak":
            total = cost
        

    loop = True
    while loop:
        print("\n================= Cashier ===================")
        print("|| Cost\t\t\t: Rp. " + str(total).ljust(12))
        payment = int(input("|| Enter payment amount\t: Rp. "))
        exchange = payment - total
        if payment < total:
            print("*Sorry you don't have enough money!")
        else:
            print("=============================================")
            print("\n=============================================")
            print("||                Receipt                  ||")
            print("=============================================")
            print("|| Cost\t\t\t: Rp. " +
                  str(total).ljust(12) + " ||")
            print("|| Payment\t\t: Rp. " + str(payment).ljust(12) + " ||")

            if exchange == 0:
                print("=============================================")
                print("||          Thankyou for playing~          ||")
                print("=============================================")

            else:
                print(f"|| Change\t\t: Rp. " + str(exchange).ljust(12) + " ||")
                print("=============================================")
                print("||          Thankyou for playing~          ||")
                print("=============================================")

            done = input("")
            if done == "":
                Main()
            else:
                print("=============================================")
                print("||          Thankyou for coming~           ||")
                print("=============================================")
                quit()


Main()
