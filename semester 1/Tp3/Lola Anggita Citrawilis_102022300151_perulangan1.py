print("=== PROGRAM MENGHITUNG RATA-RATA NILAI ===")

total = 0
jumlah = int(input("Masukkan jumlah siswa: "))
for x in range(jumlah):
    nilai = int(input("Masukkan nilai ke-" + str(x+1) + ":"))

    while nilai < 0 or nilai > 100:
        print("Gagal! Mohon masukkan nilai dari rentang 0-100")
        nilai = int(input("Masukkan nilai ke-" + str(x+1) + ":"))

    total += nilai
# rata_rata = total / jumlah

print("Rata - rata nilai siswa = {:.2f}".format(total/jumlah))
