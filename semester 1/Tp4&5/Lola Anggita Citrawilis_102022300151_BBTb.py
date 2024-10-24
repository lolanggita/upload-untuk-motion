def input_angka(placeholder):
    try:
        nilai = int(input(placeholder))
        if nilai == 0:
            exit(0)
        return nilai
    except ValueError:
        print("Input tidak valid. Hanya bisa memasukkan angka!")
        exit(0)


def jumlah(a, b):
    try:
        hasil = a + b
        print(f"Hasil: {hasil}")
        return hasil
    finally:
        print("Terimakasih telah menggunakan kalkulator pintar!")


def kurang(a, b):
    try:
        hasil = a - b
        print(f"Hasil: {hasil}")
        return hasil
    finally:
        print("Terimakasih telah menggunakan kalkulator pintar!")


def kali(a, b):
    try:
        hasil = a * b
        print(f"Hasil: {hasil}")
        return hasil
    finally:
        print("Terimakasih telah menggunakan kalkulator pintar!")


def bagi(a, b):
    try:
        hasil = a / b
        print(f"Hasil: {hasil}")
        return hasil
        if b == 0:
            raise ZeroDivisionError
    except ZeroDivisionError:
        print("Tidak dapat melakukan pembagian dengan bilangan 0.")
    finally:
        print("Terimakasih telah menggunakan kalkulator pintar!")


data_pasien = []

while True:
    print("========== KALKULATOR BMI ==========")
    print('''\nMenu:
    1. Input Data Pasien
    2. Hitung BMI Pasien
    0. Keluar''')
    menu = input_angka("Masukkan pilihan: ")

    if menu == 1:
        pasien = {}
        pasien['nama'] = input("\nMasukkan nama pasien: ")
        if pasien['nama'] == "0":
            exit(0)
        pasien['bb'] = input_angka("Masukkan berat badan pasien (kg): ")
        pasien['tb'] = input_angka("Masukkan tinggi badan pasien (cm): ")
        data_pasien.append(pasien)
        print("Data telah terinput!")
    elif menu == 2:
        n = 1
        for pasien in data_pasien:
            nama = pasien['nama']
            berat = pasien['bb']
            tinggi = pasien['tb']
            print(f'{n}. {nama}\t | {berat}kg\t | {tinggi}cm')
            n += 1
        pilih = input_angka("Pilih nomor pasien yang ingi di hitung BMI: ")
        if pilih > 0 and pilih <= len(data_pasien):
            pasien = data_pasien[pilih-1]
            nama = pasien['nama']
            berat = pasien['bb']
            tinggi = pasien['tb']
            BMI = berat / (tinggi/100)**2
            kategori = ''
            if BMI < 18.5:
                kategori = "Underweight"
            elif BMI >= 18.5 and BMI < 25:
                kategori = "Normal"
            elif BMI >= 25 and BMI < 30:
                kategori = "Overwweight"
            else:
                kategori = "Obesitas"
            print(f'{nama} memiliki BMI {BMI} dalam kategori {kategori}')
    else:
        print("***Terimakasih Sudah Menggunakan Kalkulator BMI***")

#

    print("=== KALKULATOR PINTAR ===")
    a = input_angka("Masukkan angka pertama: ")
    b = input_angka("Masukkan angka kedua: ")
    print("Pilih Operasi bilangan: ")
    print('''\n1. Penjumlahan
2. Pengurangan
3. Perkalian
4. Pembagian''')

    pilih = input_angka("Masukkan operator: ")
    if pilih == 1:
        jumlah(a, b)
    elif pilih == 2:
        kurang(a, b)
    elif pilih == 3:
        kali(a, b)
    elif pilih == 4:
        try:
            if b == 0:
                raise ZeroDivisionError
            else:
                exit
        except ZeroDivisionError:
            print("Tidak dapat melakukan pembagian dengan bilangan 0.")
        else:
            bagi(a, b)
    else:
        print("Maaf pilihan tidak tersedia!")
        exit(0)
