print("=== PROGRAM TARGET MENABUNG ===")

total = 0
x = 0
jumlah = int(input("Masukkan jumlah Target yang diinginkan : Rp."))
jangka = int(input("Masukkan jangka waktu (Bulan) : "))

while x < jangka:
    nominal = int(input("Masukkan uang tabungan di bulan ke-"+str(x+1)+" : "))
    total += nominal
    x += 1

if total >= jumlah:
    print("Anda telah berhasil menabung sesuai target🙌😊")

else:
    print(f"Tabungan Anda kurang Rp.{jumlah-total} dari Rp.{jumlah}😓")

print(f"Total tabungan anda sekarang Rp.{total}")
