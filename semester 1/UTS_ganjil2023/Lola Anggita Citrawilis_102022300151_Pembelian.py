# NIM : 102022300151
# Nama : Lola Anggita Citrawilis
daftar_makanan_0151 = {
    '1': {
        'nama': 'Rendang',
        'harga': 20000
    },
    '2': {
        'nama': 'Dendeng',
        'harga': 18000
    },
    '3': {
        'nama': 'Kikil',
        'harga': 15000
    },
    '4': {
        'nama': 'Gulai ikan',
        'harga': 17000
    },
    '5': {
        'nama': 'Gulai Ayam',
        'harga': 15000
    }
}
daftar_minuman_0151 = {
    '1': {
        'nama': 'Lemon Tea',
        'harga': 8000
    },
    '2': {
        'nama': 'Espresso',
        'harga': 12000
    },
    '3': {
        'nama': 'Coffee Latte',
        'harga': 18000
    },
    '4': {
        'nama': 'Matcha Latte',
        'harga': 18000
    },
    '5': {
        'nama': 'MilkChoco',
        'harga': 15000
    }
}
daftar_kategori_0151 = {
    1: 'makanan',
    2: 'minuman'
}

print('''=== Menu ===
1. Makanan
2. Minumuan
      ''')
kategori_0151 = int(input("Pilih 1 atau 2 : "))

if kategori_0151 == 1:  # ketika user memilih makanan_0151
    n = 1
    # key makanan_0151 menggantikan semua key yang ada didalam dict daftar_makanan_0151
    for makanan_0151 in daftar_makanan_0151:
        nama_produk_0151 = daftar_makanan_0151[makanan_0151]['nama']
        harga_0151 = daftar_makanan_0151[makanan_0151]['harga']
        print(f'{n}. {nama_produk_0151}\t Rp. {harga_0151}')
        n += 1

elif kategori_0151 == 2:  # ketika user memilih minuman_0151
    n = 1
    # key minuman_0151 menggantikan semua key yang ada didalam dict daftar_minuman_0151
    for minuman_0151 in daftar_minuman_0151:
        nama_produk_0151 = daftar_minuman_0151[minuman_0151]['nama']
        harga_0151 = daftar_minuman_0151[minuman_0151]['harga']
        print(f'{n}. {nama_produk_0151}\t\t Rp. {harga_0151}')
        n += 1


else:
    print("Maaf, Pilihan tidak tersedia.")
    exit(0)  # menghentikan program

pilihan_produk_0151 = input("Masukkan menu pilihan Anda : ")
kategori_produk_0151 = daftar_kategori_0151[kategori_0151]
jumlah_0151 = int(input(f"Masukkan banyak {kategori_produk_0151} :"))
harga_0151 = 0

nama_produk_0151 = ""
if kategori_0151 == 1:
    harga_0151 = daftar_makanan_0151[pilihan_produk_0151]['harga']
    nama_produk_0151 = daftar_makanan_0151[pilihan_produk_0151]['nama']
elif kategori_0151 == 2:
    harga_0151 = daftar_minuman_0151[pilihan_produk_0151]['harga']
    nama_produk_0151 = daftar_minuman_0151[pilihan_produk_0151]['nama']

total_harga_0151 = harga_0151 * jumlah_0151
total_diskon_0151 = 0
diskon_0151 = 0

if total_harga_0151 > 500_000:
    diskon_0151 = 25/100
elif total_harga_0151 > 250_000:
    diskon_0151 = 15/100
elif total_harga_0151 > 100_000:
    diskon_0151 = 10/100

total_diskon_0151 = total_harga_0151 - total_harga_0151 * diskon_0151

print(f"Total yang harus dibayar adalah {int(total_diskon_0151)}")
nim_0151 = input("Masukkan NIM Anda : ")
nama_0151 = input("Masukkan Nama Anda : ")
bayar_0151 = int(input("Masukkan Nominal Pembayaran : "))
if bayar_0151 < total_diskon_0151:
    print("Maaf uang Anda tidak cukup.")
    exit(0)

kembalian_0151 = bayar_0151 - total_diskon_0151
print(f'''
      ====== Receipt ======
      Jenis \t : {kategori_produk_0151}
      Nama \t : {nama_produk_0151}
      Harga \t : {harga_0151}   
      Jumlah \t : {jumlah_0151}
      Total \t : {total_harga_0151}
      Diskon {int(diskon_0151 * 100)}%
      Total Diskon : {int(total_diskon_0151)}
      
      Uang kembali {int(kembalian_0151)}''')
