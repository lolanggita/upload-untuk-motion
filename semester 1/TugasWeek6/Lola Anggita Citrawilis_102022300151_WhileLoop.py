a = int(input("Masukkan bilangan ke-1 : "))
b = int(input("Masukkan bilangan ke-2 : "))
c = int(input("Masukkan bilangan ke-3 : "))
d = int(input("Masukkan bilangan ke-4 : "))
e = int(input("Masukkan bilangan ke-5 : "))

Min = a
if (b < Min):
    Min = b
else:
    if (c < Min):
        Min = c
    else:
        if (d < Min):
            Min = d
        else:
            if (e < Min):
                Min = e

Max = a
if (b > Max):
    Max = b
else: 
    if (c > Max):
        Max = c
    else: 
        if (d > Max):
            Max = d
        else: 
            if (e > Max):
                Max = e

jumlah = a + b + c + d + e
rata_rata = jumlah / 5
print("Nilai Minimum dari 5 bilangan tersebut adalah ", Min)
print("Nilai Maximum dari 5 bilangan tersebut adalah ", Max)   
print("Nilai Rata - Rata dari 5 bilangn tersebut adalah ", rata_rata)
