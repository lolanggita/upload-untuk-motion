#masukkan informasi
akun = {
    "NIM": "300442",
    "Nama": "Khalila Aziza Gunawan",
    "No. Rekening": "92857340112",
    "Saldo": 3000000
}

nim = int(input("Masukkan Nim Anda: "))
pin = int(input("Masukkan Pin Anda: "))

if pin == nim:
    print("=== MENU UTAMA ===")
    print("1. Cek Saldo")
    print("2. Tarik uang")
    print("3. Setor Uang")
    pilih = int(input("Pilih Menu: "))

    if pilih == 1:
        print(f"NIM: {akun['NIM']}")
        print(f"Nama: {akun['Nama']}")
        print(f"No. Rekening: {akun['No. Rekening']}")
        print(f"Saldo Anda: {akun['Saldo']}")
    if pilih == 2:
        print(f"NIM: {akun['NIM']}")
        print(f"Nama: {akun['Nama']}")
        print(f"No. Rekening: {akun['No. Rekening']}")
        tarik = float(input("Jumlah Penarikan: "))
        if tarik <= akun ["Saldo"]:
            sisa = akun ["Saldo"] - tarik
            print(f"Sisa saldo anda sekarang adalah: {sisa}")
        else:
            print("SALDO ANDA TIDAK CUKUP UNTUK MELAKUKAN PENARIKAN")
    if pilih == 3:
        print(f"NIM: {akun['NIM']}")
        print(f"Nama: {akun['Nama']}")
        print(f"No. Rekening: {akun['No. Rekening']}")
        tambah = float(input("Jumlah Setoran: "))
        salbar = akun ["Saldo"] + tambah
        print(f"Saldo Anda Sekarang Adalah: {salbar}")
    elif pilih > 3:
        print("COBA LAGI DAN MOHON PILIH MENU")
    else:
        exit()
else:
    print("PIN YANG DIMASUKKAN SALAH. SILAHKAN COBA LAGI")
