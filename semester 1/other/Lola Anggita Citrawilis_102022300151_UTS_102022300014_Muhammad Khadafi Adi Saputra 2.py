# NIM: 102022300014
# Nama: MUHAMMAD kHADAFI ADI SAPUTRA

nim_0014 = input("Masukkan NIM: ")
nama_0014 = input("Masukkan Nama: ")
no_rek_0014 = input("Masukkan No.Rekening: ")
pin_0014 = input("Masukkan PIN (6 digit dari NIM): ")
saldo_0014 = 500000


def info_user():
    print("===Informasi===")
    print("  NIM: ", nim_0014)
    print("  Nama: ", nama_0014)
    print("  No.Rekening: ", no_rek_0014)


def cek_saldo():
    info_user()
    print("Saldo di Rekening Anda adalah: ", saldo_0014)


def setor_uang():
    global saldo_0014
    info_user()
    nominal_0014 = int(input("Masukkan nominal yang akan di Setorkan: "))
    print("Anda berhasil menyetor sebesar: ", nominal_0014)
    saldo_0014 = saldo_0014 + nominal_0014
    print("Saldo Anda sekarang adalah: ", saldo_0014)


def tarik_uang():
    global saldo_0014
    info_user()
    nominal_0014 = int(input("Masukkan Nominal yang ingin ditarik: "))
    if nominal_0014 > saldo_0014:
        print("Maaf saldo anda tidak mencukupi")
    else:
        saldo_0014 = saldo_0014 - nominal_0014
        print("Anda Berhasil menarik sebesar", nominal_0014)
        print("Saldo Anda sekarang adalah: ", saldo_0014)


if pin_0014 == nim_0014[:6]:
    print("Selamat Datang", nama_0014)

    while True:
        print("Menu ATM")
        print("1. Cek Saldo")
        print("2. Tarik Uang")
        print("3. Setor Uang")
        print("4. Exit")

        menu_0014 = input("PIlih Opsi Menu 1/2/3/4: ")

        if menu_0014 == "1":
            cek_saldo()
        elif menu_0014 == "2":
            tarik_uang()
        elif menu_0014 == "3":
            setor_uang()
        elif menu_0014 == "4":
            exit()
        else:
            print("Pilihan Tidak Valid")


else:
        print("PIN yang anda masukkan salah")
    
