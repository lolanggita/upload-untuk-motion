# Tp 01
print("=== PROGRAM MENGHITUNG RATA-RATA ===")
jumlah = int(input("Masukkan Jumlah Siswa: "))

total_nilai = 0

for i in range(jumlah):
    nilai = float(input(f"Masukkan nilai ke-{i + 1}: "))
    total_nilai += nilai

    if 0 <= nilai <= 100:
        total_nilai += nilai
    else:
        print("Gagal! Mohon Masukkan Nilai dari Rentang 0-100!")
        exit()

rata_rata = total_nilai / jumlah
print(f"Rata-Rata Nilai: {rata_rata}")


# Tp 02
print("\n=== PROGRAM TARGET MENABUNG ===")
target = float(input("Masukkan Nominal yang di inginkan: Rp."))
jangka_waktu = int(input(f"Masukkan Jangka Waktu (bulan): "))
bulan = 0
total = 0

while bulan < jangka_waktu:
    uang = int(input(f"Masukkan uang tabungan di bulan ke-{bulan+1}: "))
    total += uang
    bulan += 1

if total >= target:
    print("Anda Telah Menabung Sesuai Target!")
    print(f"total tabungan Anda : Rp.{total}")
    exit()

else:
    print(f"Tabungan Anda Kurang Rp.{target-total} dari Rp.{target}")
    print(f"total tabungan Anda : Rp.{total}")
    print("Selamat Menabung Lagi!!!")
