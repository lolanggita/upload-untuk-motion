count = 1
total = 0

while count <= 5:
    num = int(input(f"Masukkan bilangan ke-{count} (2-15): "))

    if 2 <= num <= 15:
        if count == 1:
            min_num = max_num = num
        else:
            if num < min_num:
                min_num = num
            if num > max_num:
                max_num = num

        total += num
        count += 1
    else:
        print("Angka harus berada dalam rentang 2-15. Coba lagi.")

rata_rata = total / 5

print("Nilai Minimum dari 5 bilangan tersebut adalah", min_num)
print("Nilai Maksimum dari 5 bilangan tersebut adalah", max_num)
print("Nilai Rata - Rata dari 5 bilangan tersebut adalah", rata_rata)
