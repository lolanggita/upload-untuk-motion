import array as a
from collections import deque

# Input Nilai
N, k = map(int, input().split())    # N = jumlah nilai, k = jumlah rotasi
box = a.array('i')     # Array kosong untuk menyimpan jumlah permen, dengan tipe data int

for i in range(N):
    # c = map(int, input().split())
    c = int(input())    # Menginput nilai
    box.append(c)

def rotate_list(box):
    rotated_C = deque(box)  # Merotasikan nilai yang ada didalam array 'box'
    rotated_C.rotate(k)     # Menggunakan nilai k yang telah diinput untuk menentukan jumlah rotasi

    return list(rotated_C)

rotated_list = rotate_list(box)

print("Nilai awal:\t", box)
print("Nilai setelah rotasi:\t", rotated_list)
