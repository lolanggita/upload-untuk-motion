print("=== Tebak Kata Kunci ===")
key = "dasprokece"
i = 0
while i < 3:
    print(f"\nPercobaan ke-{i+1}")
    password = input("Masukkan kata Kunci: ")
    i += 1
    if password == key:
        print("Anda Berhasil!")
        break
    elif password != key and i == 3:
        print("Anda Gagal!")
    else:
        print("Coba lagi...")
