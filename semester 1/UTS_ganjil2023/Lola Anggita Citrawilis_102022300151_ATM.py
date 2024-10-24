# NIM : 102022300151
# Nama : Lola Anggita Citrawilis
nama_0151 = ""
norek_0151 = 0
nim_0151 = 0
pin_0151 = 0
saldo_0151 = 0
nominal_0151 = 0
pilihan_0151 = 0
inputPin_0151 = 0


def cekSaldo():
    print(
        f"NIM \t\t : {nim_0151} \nNama \t\t : {nama_0151} \nNo. Rekening \t : {norek_0151}")
    print(f"Saldo saat ini Rp.{saldo_0151}")


def tarikUang():
    global saldo_0151
    print(
        f"NIM \t\t : {nim_0151} \nNama \t\t : {nama_0151} \nNo. Rekening \t : {norek_0151}")
    nominal_0151 = int(input("Masukkan nominal yang ingin di tarik : Rp."))
    if nominal_0151 <= saldo_0151:
        saldo_0151 = saldo_0151 - nominal_0151
        print(f"Sisa saldo Anda saat ini : Rp.{saldo_0151}")

    elif nominal_0151 > saldo_0151:
        print("Maaf, saldo anda tidak cukup.")


def setorUang():
    global saldo_0151
    print(
        f"NIM \t\t : {nim_0151} \nNama \t\t : {nama_0151} \nNo. Rekening \t : {norek_0151}")
    nominal_0151 = int(input("Masukkan nominal yang ingin di setor : Rp."))
    saldo_0151 = saldo_0151 + nominal_0151
    print(f"Saldo Akhir : Rp.{saldo_0151}")


def tampilMenu():
    print("""
    ==== Bank ====
    Pilih Layanan :
    1. Cek Saldo
    2. Tarik Uang
    3. Setor Uang 
    0. Selesai 
    """)
    pilihan_0151 = int(input("Masukkan pilihan Anda : "))
    return pilihan_0151


nim_0151 = int(input("Masukkan NIM : "))
nama_0151 = input("Masukkan Nama Anda : ")
norek_0151 = int(input("Masukkan No. Rekaning Anda : "))
while int(nim_0151 / 10**5) <= 0:
    print("Maaf 🙏🏻, NIM Anda kurang dari 6 angka")
    nim_0151 = int(input("Masukkan NIM : "))
    nama_0151 = input("Masukkan Nama Anda : ")
    norek_0151 = int(input("Masukkan No. Rekaning Anda : "))

while int(nim_0151 / 10**17) > 0:
    print("Maaf 🙏🏻, NIM Anda terlalu panjang.")
    nim_0151 = int(input("Masukkan NIM : "))
    nama_0151 = input("Masukkan Nama Anda : ")
    norek_0151 = int(input("Masukkan No. Rekaning Anda : "))

pin_0151 = nim_0151 % 10**6
inputPin_0151 = int(input("Masukkan PIN : "))
if pin_0151 != inputPin_0151:
    print("Maaf 🙏🏻, PIN Anda salah.")
    exit(0)

pilihan_0151 = tampilMenu()
while pilihan_0151 >= 0 and pilihan_0151 < 4:
    if pilihan_0151 == 1:
        cekSaldo()
    elif pilihan_0151 == 2:
        tarikUang()
    elif pilihan_0151 == 3:
        setorUang()
    elif pilihan_0151 == 0:
        print("Terimakasih sudah menggunakan Layanan.🙌😊")
        break
    else:
        print("Layanan tidak tersedia")

    pilihan_0151 = tampilMenu()
