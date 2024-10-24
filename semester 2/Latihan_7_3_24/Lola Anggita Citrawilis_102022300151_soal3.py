import array

# Input
N = int(input().strip())
hasil_ujian = array.array('i', map(int, input().strip().split()))

# Inisialisasi array frekuensi dengan ukuran 101 (0-100) dan nilai awal 0
frekuensi = array.array('i', [0]*101)
print(*frekuensi)
# Mengisi frekuensi
for skor in hasil_ujian:
    frekuensi[skor] += 1

# Mencari angka dengan frekuensi maksimal
frekuensi_maks = max(frekuensi)
angka_terbanyak = frekuensi.index(frekuensi_maks)

# Mencetak hasil
print(angka_terbanyak)