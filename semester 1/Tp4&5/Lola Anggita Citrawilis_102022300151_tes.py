def persegi(sisi):
    luas = sisi * sisi
    return luas

def persegi_panjang(p, l):
    luas = p * l
    return luas

def segitiga(a, t):
    luas = 0.5 * a * t
    return luas

def lingkaran(r):
    luas = 3.14 * r**2
    return luas

while True:
    try:
        print('''=== PROGRAM MENGHITUNG LUAS BANGUN DATAR ===
1. Persegi
2. Persegi Panjang
3. Segitiga
4. Lingkaran
0. Exit''')

        pilih = int(input("Masukkan pilihan: "))
        if pilih == 1:
            sisi = int(input("Masukkan nilai sisi:"))
            hasil = persegi(sisi)
            print(f"Luas persegi adalah {hasil}")
        elif pilih == 2:
            p = int(input("Masukkan nilai panjang: "))
            l = int(input("Masukkan nilai lebar: "))
            hasil = persegi_panjang(p, l)
            print(f"Luas persegi panjang adalah {hasil}")
        elif pilih == 3:
            a = int(input("Masukkan nilai alas: "))
            t = int(input("Masukkan nilai tinggi: "))
            hasil = segitiga(a, t)
            print(f"Luas segitiga adalah {hasil}")
        elif pilih == 4:
            r = int(input("Masukkan nilai ruas: "))
            hasil = lingkaran(r)
            print(f"Luas lingkaran adalah {hasil}")
        elif pilih == 0:
            print("Terimakasih telah menggunakan Program Menghitung Luas Bangun Datar!")
            exit(0)
    except ValueError:
        print("Inputan Harus berupa angka!")
    finally:
        print("Terimakasih telah menggunakan Program Menghitung Luas Bangun Datar!")
