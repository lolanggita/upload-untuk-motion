import pandas as pd

def muat_data():
    data = pd.read_csv('C:/Users/anggi/OneDrive/Documents/code/python/semester 2/Praktikum/Proporsi Rumah Tangga Yang Memiliki Akses Terhadap Layanan Sanitasi Layak, 2021-2023.csv')
    return data

def tampilkan_data_frame(data):
    # Hint: Isi dengan fungsi untuk menampilkan seluruh dataframe (print data dari csvnya?)
    print(data)


def tampilkan_gambaran_umum(data):
    # Hint: Isi dengan fungsi untuk menampilkan informasi umum tentang data (print ringkasan statistik deskriptif dari data?)
    rincian_1 = data.info()
    rincian_2 = data.describe()
    print(rincian_1, rincian_2)
    

def sepuluh_provinsi_teratas(data):
    # Hint: Isi dengan fungsi untuk menampilkan sepuluh provinsi teratas pada tahun 2023  (pakai sort value)
    sorted_data = data.sort_values(['2023'], ascending=False)
    top_10 = sorted_data[['Provinsi', '2023']].head(10)
    print(top_10)

def provinsi_dengan_peningkatan_terbesar(data):
    # Hint: Isi dengan fungsi untuk menemukan provinsi dengan peningkatan terbesar dari 2021 ke 2023 (pakai data.loc)
    data['Peningkatan'] = data['2023'] - data['2021']
    sorted_data = data.sort_values(['Peningkatan'], ascending=False).head(1)
    print(sorted_data)

def analisis_korelasi(data):
    # Hint: Isi dengan fungsi untuk menganalisis korelasi antara tahun (fungsi buat mencari korelasi?)
    data_numerik = data.select_dtypes(include=['int64', 'float64'])
    korelasi = data_numerik.corr()
    print(korelasi)

def kinerja_provinsi_tertentu(data, nama_provinsi):
    # Hint: Isi dengan fungsi untuk menampilkan kinerja provinsi tertentu (pakai data.loc dan kondisi jika data tidak ada)
    pilihan2 = input("Masukkan nama provinsi: ")
    nama_provinsi = data.loc['Provinsi']
    data['Peningkatan'] = data['2023'] - data['2021']
    if pilihan2 in nama_provinsi:
        print(data[['Provinsi', '2021', '2022', '2023', 'Peningkatan']])
    else:
        print("Provinsi tidak ditemukan")

def utama():
    nama_provinsi = data.loc['Provinsi']
    data = muat_data()
    while True:
        print("\n=====================================")
        print("Menu Analisis Data:")
        print("1. Tampilkan seluruh data frame")
        print("2. Tampilkan gambaran umum data")
        print("3. Tampilkan 10 provinsi terbaik tahun 2023")
        print("4. Tampilkan provinsi dengan peningkatan terbesar 2021-2023")
        print("5. Analisis korelasi antar tahun")
        print("6. Tampilkan performa provinsi tertentu")
        print("7. Keluar")
        print("=====================================")
        pilihan = int(input("Masukkan pilihan Anda: "))
        # Hint: Tambahkan if else untuk setiap pilihan menu sesuai deskripsi soal

        if pilihan == 1 :
            tampilkan_data_frame(data)
        elif pilihan == 2 :
            tampilkan_gambaran_umum(data)
        elif pilihan == 3 :
            sepuluh_provinsi_teratas(data)
        elif pilihan == 4 :
            provinsi_dengan_peningkatan_terbesar(data)
        elif pilihan == 5 :
            analisis_korelasi(data)
        elif pilihan == 6 :
            kinerja_provinsi_tertentu(data, nama_provinsi)
        elif pilihan == 7 :
            print("Keluar dari Program")
            break
        else :
            print("Pilihan tidak tertera.")

if __name__ == "__main__":
    utama()
