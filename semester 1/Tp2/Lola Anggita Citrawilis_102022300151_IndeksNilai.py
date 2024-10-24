nilai = float(input("Masukkan nilai anda : "))

if nilai < 0 or nilai > 100:
    indeks = "NILAI DILUAR JANGKAUAN"
else:
    if nilai >= 80:
        indeks = "A"
    elif nilai >= 70:
        indeks = "AB"
    elif nilai >= 60:
        indeks = "B"
    elif nilai >= 50:
        indeks = "BC"
    elif nilai >= 40:
        indeks = "C"
    elif nilai >= 30:
        indeks = "D"
    else:
        indeks = "E"

print(f"Nilai indeks dari {nilai} adalah '{indeks}' ")
