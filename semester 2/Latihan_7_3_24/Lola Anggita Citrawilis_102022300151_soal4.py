import array

N = int(input().strip())
set_pertama = array.array('i', map(int, input().strip().split()))
set_kedua = array.array('i', map(int, input().strip().split()))

# Mengurutkan kedua array
set_pertama = array.array('i', sorted(set_pertama))
set_kedua = array.array('i', sorted(set_kedua))

# Membandingkan kedua array untuk menentukan permutasi
if set_pertama == set_kedua:
    print("Ya")
else:
    print("Tidak")