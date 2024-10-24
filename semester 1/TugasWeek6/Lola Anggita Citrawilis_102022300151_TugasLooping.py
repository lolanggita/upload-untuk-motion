angka = 2
total = 0
nilai_maksimum = angka
nilai_minimum = angka

while angka <= 15:
    total += angka
    
    if angka > nilai_maksimum:
        nilai_maksimum = angka
    
    if angka < nilai_minimum:
        nilai_minimum = angka
    
    angka += 1

rata_rata = total / 14 

# Menampilkan hasil
print("Nilai Maksimum:", nilai_maksimum)
print("Nilai Minimum:", nilai_minimum)
print("Rata-rata:", rata_rata)
