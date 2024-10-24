def input_angka(placeholder):
    try:
        nilai = int(input(placeholder))
        return nilai
    except ValueError:
        print("Input tidak valid. Hanya menerima jenis nilai integer!")


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
    except ZeroDivisionError:
        print("Tidak dapat melakukan pembagian dengan bilangan 0.")
    finally:
        print("Terimakasih telah menggunakan kalkulator pintar!")


while True:
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
