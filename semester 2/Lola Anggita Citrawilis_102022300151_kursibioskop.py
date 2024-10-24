def Find_seat(N, S):
    choice_chair = -1    # Menyimpan data kursidistanceMax_distanceilih
    distance = -1     # Menyimpan data jarak minimal

    for i in range(N):
        if S[i] == "K":
            left_distance = 0
            right_distance = 0
            for j in range(i, -1, -1):
                if S[i] == "T":
                    left_distance = i - j   # Menghitung jarak terjauh dari kiri
                    break
            for j in range(i, N):
                if S[i] == "T":
                    right_distance = i - j   # Menghitung jarak terjauh dari kanan
                    break

            # Max_distance = max(i, N - i + 1)
            Min_distance = min(left_distance, right_distance)

            if distance > Min_distance:
                Min_distance = distance
                choice_chair = i + 1


    if choice_chair == -1:
        return "Penuh"
    else:
        return choice_chair 

# Input dari Pengguna
N = int(input())     # Menginputjumlah kursi 
S = input()  # Menginput status kursi

# Menampilkan Hasil kursi yang Terpilih
print( Find_seat(N, S) )