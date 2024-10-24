import array

# Menerima input
N = int(input().strip())
skor_tim_A = array.array('i', map(int, input().strip().split()))
skor_tim_B = array.array('i', map(int, input().strip().split()))

# Menghitung berapa kali skor Tim A lebih tinggi dari Tim B
jumlah_kemenangan_A = sum(a > b for a, b in zip(skor_tim_A, skor_tim_B))

print(jumlah_kemenangan_A)