def kalkulasi(a, b, c):
    nilaimax = max(a, b, c)
    nilaimin = min(a, b, c)
    jumlah = a + b + c
    rata_rata = jumlah / 3
    print(f"nilai maksimum: {nilaimax}")
    print(f"nilai minimum: {nilaimin}")
    print(f"rata-rata nilai: {rata_rata}")


a = int(input("masukkan nilai a: "))
b = int(input("masukkan nilai b: "))
c = int(input("masukkan nilai c: "))
kalkulasi(a, b, c)
