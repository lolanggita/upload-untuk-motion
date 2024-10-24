def input_angka(placeholder):
    try:
        nilai = int(input(placeholder))
        return nilai
    except ValueError:
        print("Input tidak valid. Hanya menerima jenis nilai integer!")
        
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
        print(f"Hasil: {a+b}")
    elif pilih == 2:
        print(f"Hasil: {a-b}")
    elif pilih == 3:
        print(f"Hasil: {a*b}")
    elif pilih == 4:
        try:
            if b == 0:
                raise ZeroDivisionError
            print(f"Hasil: {a/b}")
        except ZeroDivisionError:
            print("Tidak dapat melakukan pembagian dengan bilangan 0.")
        finally:
            print("Terimakasih telah menggunakan kalkulator pintar!")
    else:
        print("Maaf pilihan tidak tersedia!")
        exit(0)
