Data_Mahasiswa = {}    # {"Nama", "NIM", "Quiz", "Task", "Exam", "Nilai Akhir"}

def Add_Mahasiswa():
    Name = input("Masukkan Nama: ")
    NIM = int(input("Masukkan NIM: "))
    Quiz = int(input("Masukkan Nilai Kuis: "))
    Task = int(input("Masukkan Nilai Tugas: "))
    Exam = int(input("Masukkan Nilai Ujian: "))
    
    x = NIM % 10**6
    Data_Mahasiswa[x] = {"Nama": Name, "NIM": str(NIM), "Quiz": str(Quiz), "Task": str(Task),  "Exam": str(Exam), "Score": "0"}
    print("==========================================================================================")
    print("|| " + "Nama".center(8) + " || " + "NIM".center(13) +
          " || " + "Nilai Kuis".center(5) + " || " + "Nilai Tugas".center(8) + " || " + "Nilai Ujian".center(8) + " || " + "Nilai Akhir".center(8) + " ||")
    print("==========================================================================================")


    print("|| " + Data_Mahasiswa[x]["Nama"].center(8) + " || " + str(Data_Mahasiswa[x]["NIM"]).center(13) + " || " + str(
            Data_Mahasiswa[x]["Quiz"]).center(10) + " || " + str(Data_Mahasiswa[x]["Task"]).center(11) + " || " + str(Data_Mahasiswa[x]["Exam"]).center(11) + " || " + str(Data_Mahasiswa[x]["Score"]).center(11) + " ||")
    print("==========================================================================================")
    Enter = input("")

def View_Mahasiswa():
    # Data_Mahasiswa[id] = {"Nama": Name, "NIM": NIM, "Quiz": Quiz, "Task": Task, "Exam": Exam, "Score" = "0"} 
    print("==========================================================================================")
    print("|| " + "Nama".center(8) + " || " + "NIM".center(13) +
          " || " + "Nilai Kuis".center(5) + " || " + "Nilai Tugas".center(8) + " || " + "Nilai Ujian".center(8) + " || " + "Nilai Akhir".center(8) + " ||")
    print("==========================================================================================")

    for x in Data_Mahasiswa:
        print("|| " + Data_Mahasiswa[x]["Nama"].center(8) + " || " + str(Data_Mahasiswa[x]["NIM"]).center(13) + " || " + str(
            Data_Mahasiswa[x]["Quiz"]).center(10) + " || " + str(Data_Mahasiswa[x]["Task"]).center(11) + " || " + str(Data_Mahasiswa[x]["Exam"]).center(11) + " || " + str(Data_Mahasiswa[x]["Score"]).center(11) + " ||")
    print("==========================================================================================")
    Enter = input("")

def Count_Score(Data_Mahasiswa):
    found = False
    while found == False: 
        if len(Data_Mahasiswa) == 0:
            print("Belum ada data mahasiswa.")

        else: 
            nim = int(input("Masukkan NIM Mahasiswa: "))
            # print(Data_Mahasiswa)

            for x in Data_Mahasiswa:
                if  nim == Data_Mahasiswa[x]["NIM"]:
                    Quiz_value = Data_Mahasiswa[x]["Quiz"]
                    Task_value = Data_Mahasiswa[x]["Task"]
                    Exam_value = Data_Mahasiswa[x]["Exam"]

                    percentQuiz = Quiz_value * 0.25
                    percentTask = Task_value * 0.25
                    percentExam = Exam_value * 0.5

                    Total = percentQuiz + percentTask + percentExam

                    Data_Mahasiswa[x]["Score"] = Total
                    print("Nilai Akhir " + Data_Mahasiswa[x]["Name"] + ", NIM " + str(Data_Mahasiswa[x]["NIM"]) + " adalah " + str(Total))
                    found = True

                else:
                    print("Mahasiswa dengan NIM tersebut tidak ditemukan.") 
                    found = True

            Enter = input("")      

def Sort_Mahasiswa():
    sortedval = sorted(Data_Mahasiswa("Score"), reverse=True)
    print(sortedval)

# def Delete_Mahasiswa():


def Main():

    while True:
        print("==== PROGRAM MANAJEMEN DATA MAHASISWA UNIVERSITAS DASPRO ====")
        print("|| ".ljust(25) + "Menu".center(11) + " ||".rjust(25))
        print("=============================================================")
        print("|| 1. Menambahkan Data Mahasiswa" )
        print("|| 2. Menampilkan Seluruh Data Mahasiswa" )
        print("|| 3. Menghitung Nilai Akhir") 
        print("|| 4. Mengurutkan Data Nilai Akhir (dari yang terbesar)")
        print("|| 5. Menghapus Data Mahasiswa")
        print("|| 0. Keluar" )
        print("=============================================================")
        menu = int(input("Pilih Menu => "))

        if menu == 1 :
            Add_Mahasiswa()
        elif menu == 2 :
            View_Mahasiswa()
        elif menu == 3 :
            Count_Score(Data_Mahasiswa)
        elif menu == 4 :
            pass
        elif menu == 5 :
            pass
        elif menu == 0 :
            exit()

Main()

# maaf kak codingan saya nomer 3 tidak jalan jadi saya tidak bisa melanjutkannya
# saya juga tidak enak bertanya dengan asprak karena saya mengerjakan h-1 dan sudah malam  