def Input_Nilai():
    global Quiz, Tugas, UTS, UAS
    print("========== INPUT NILAI ==========")
    Quiz = int(input("|| Masukkan nilai Kuis: "))
    Tugas = int(input("|| Masukkan nilai Tugas: "))
    UTS = int(input("|| Masukkan nilai UTS: "))
    UAS = int(input("|| Masukkan nilai UAS: "))
    print("=================================")
    print("Nilai berhasil dimasukkan.")
    Enter = input("")

    return Quiz, Tugas, UTS, UAS  

def Tampil_Nilai():
    global Quiz, Tugas, UTS, UAS
    print("\n======== DATA NILAI ========")
    print("|| Nilai Kuis\t: " + str(Quiz) + " ||".rjust(8))
    print("|| Nilai Tugas\t: " + str(Tugas) + " ||".rjust(8))
    print("|| Nilai UTS\t: " + str(UTS) + " ||".rjust(8))
    print("|| Nilai UAS\t: " + str(UAS) + " ||".rjust(8))
    print("============================")
    Enter = input("")

def Hitung_Nilai():
    global Quiz, Tugas, UTS, UAS, NSM
    percentQuiz = Quiz * 0.2
    percentTugas = Tugas * 0.15
    percentUTS = UTS * 0.3
    percentUAS = UAS * 0.35
    
    NSM = percentQuiz + percentTugas + percentUTS + percentUAS

    print("\n========== NILAI AKHIR ==========")
    print("|| Nilai Akhir\t: " + str(NSM) + " ||".rjust(11))

    if NSM > 80 :    
        print("|| Indeks Nilai\t: A" + " ||".rjust(14))
    
    elif NSM <= 80 and NSM > 70:
        print("|| Indeks Nilai\t: AB" + " ||".rjust(13))
    
    elif NSM <= 70 and NSM > 65:
        print("|| Indeks Nilai\t: B" + " ||".rjust(14))
    
    elif NSM <= 65 and NSM > 60:
        print("|| Indeks Nilai\t: BC" + " ||".rjust(13))
    
    elif NSM <= 60 and NSM > 50:
        print("|| Indeks Nilai\t: C" + " ||".rjust(14))

    elif NSM <= 50 and NSM > 40:
        print("|| Indeks Nilai\t: D" + " ||".rjust(14))

    elif NSM <= 40:
        print("|| Indeks Nilai\t: E" + " ||".rjust(14))
    
    print("=================================")
    Enter = input("")
    return NSM

def Status():
    global NSM
    print("\n========= STATUS KELULUSAN =========")
    if NSM > 40 :
        print("|| Status\t: Lulus" + " ||".rjust(13))
    else:
        print("|| Status\t: Tidak Lulus" + " ||".rjust(7))
    
    print("====================================")
    Enter = input("")

def Main():
    global Quiz, Tugas, UTS, UAS, NSM

    while True:
        print("==== PROGRAM MENGHITUNG NILAI MATA KULIAH ====")
        print("|| ".ljust(20) + "Menu".center(6) + " ||".rjust(20))
        print("==============================================")
        print("|| 1. Input Nilai (Quiz, Tugas, UTS, UAS)" + " ||".rjust(5))
        print("|| 2. Menampilkan Nilai" + " ||".rjust(23))
        print("|| 3. Menghitung Nilai Akhir" + " ||".rjust(18))
        print("|| 4. Menampilkan Status Kelulusan" + " ||".rjust(12))
        print("|| 0. Keluar" + " ||".rjust(34))
        print("==============================================")
        menu = int(input("Pilih Menu => "))

        if menu == 1 :
            Input_Nilai()
        elif menu == 2 :
            Tampil_Nilai()
        elif menu == 3 :
            Hitung_Nilai()
        elif menu == 4 :
            Status()
        elif menu == 0 :
            exit()

Main()