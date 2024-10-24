import array
# Mengambil input jumlah orang
N = int(input().strip())

# Mengambil input tinggi setiap orang dan mengubahnya menjadi list integers

#tinggi_orang = list(map(int, input().strip().split()))
tinggi_orang = array.array('i', map(int, input().strip().split()))

# Mengurutkan  tinggi orang
#tinggi_orang.sort() #jikalist
tinggi_orang = sorted(tinggi_orang)
# Mencari nilai tengah
if N % 2 == 1:
    # Jika jumlah orang ganjil, ambil nilai tengah langsung
    nilai_tengah = tinggi_orang[N // 2]
else:
    # Jika jumlah orang genap, ambil nilai tengah yang lebih kecil
    nilai_tengah = tinggi_orang[(N // 2) - 1]

# Mencetak nilai tengah
print(nilai_tengah)