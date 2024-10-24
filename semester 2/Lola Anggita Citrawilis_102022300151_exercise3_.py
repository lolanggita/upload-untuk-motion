import array as a

# Array bentukan awal 
# var_a = a.array('q', [1, 2, 3, 6, 8, 0, 12]) 
# print(var_a)

# add = int(input())  # Menerima Inputan nilai tambah kedalam array
# var_a.insert(5, add)
# print(var_a)

# eksten = (4, 100, 67)   # Memasukkan nilai untuk dimodifikasi
# var_a.extend(eksten)
# print(var_a)

# Pertanyaan 1
ganjil = a.array('i', [1, 3, 5])
genap = a.array('i', [2, 4, 6])
angka = a.array('i')
angka = ganjil + genap
print(angka)

