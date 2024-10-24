import pandas as pd

while True:
    print("""\nMenu Analisis Data:
    1. 5 Kota dengan Tingkat Penyelesaian Pendidikan Tertinggi
    2. 5 Kota dengan Tingkat Pengangguran Tertinggi
    3. 5 Kota dengan Tingkat Penyelesaian Pendidikan Terendah
    4. 5 Kota dengan Tingkat Pengangguran Terendah 
    5. Tampilkan Keseluruhan Data Frame
    0. Keluar""")
    choose = int(input("Masukkan pilihan Anda: "))

    data = pd.read_csv('c:/Users/anggi/OneDrive/Documents/code/python/semester 2/Praktikum/TP3/DataPendahuluan.csv')
    if choose == 1:
        sorted_a = data.sort_values(by='Tingkat_Penyelesaian_Pendidikan', ascending=False)
        sorted_a_top5 = sorted_a.head(5)
        print(sorted_a_top5[['Provinsi', 'Tingkat_Penyelesaian_Pendidikan']])
        
    elif choose == 2:
        sorted_b = data.sort_values(by='Tingkat_Setengah_Pengangguran', ascending=False)
        sorted_b_top5 = sorted_b.head(5)
        print(sorted_b_top5[['Provinsi', 'Tingkat_Setengah_Pengangguran']])
        
    elif choose == 3:
        sorted_c = data.sort_values(by='Tingkat_Penyelesaian_Pendidikan', ascending=True)
        sorted_c_top5 = sorted_c.head(5)
        print(sorted_c_top5[['Provinsi', 'Tingkat_Penyelesaian_Pendidikan']])

    elif choose == 4:
        sorted_d = data.sort_values(by='Tingkat_Setengah_Pengangguran', ascending=True)
        sorted_d_top5 = sorted_d.head(5)
        print(sorted_d_top5[['Provinsi', 'Tingkat_Setengah_Pengangguran']])

    elif choose == 5:
        print(data)

    elif choose == 0:
        exit()