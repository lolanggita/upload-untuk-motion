# NIM : 102022300014
# Nama : MUHAMMAD kHADAFI ADI SAPUTRA
# TUGAS 1 : PROGRAM PEMBELIAN

makanan_1_0014 = "Nasi Uduk"
makanan_2_0014 = "Ayam Katsu"
makanan_3_0014 = "Nasi Goreng"
makanan_4_0014 = "Ayam BBQ"
makanan_5_0014 = "Spageti"

harga_makanan_1_0014 = 10.000
harga_makanan_2_0014 = 15.000
harga_makanan_3_0014 = 18.000
harga_makanan_4_0014 = 20.000
harga_makanan_5_0014 = 25.000

minuman_1_0014 = "Air Mineral"
minuman_2_0014 = "Es Teh Manis"
minuman_3_0014 = "Pop Ice"
minuman_4_0014 = "Sop Buah"
minuman_5_0014 = "Es Mangga Ekslusive"

harga_minuman_1_0014 = 3.000
harga_minuman_2_0014 = 5.000
harga_minuman_3_0014 = 10.000
harga_minuman_4_0014 = 20.000
harga_minuman_5_0014 = 30.000

while True:
    print("=== MENU UTAMA === ")
    print("1. Makanan")
    print("2. Minuman")
    # print("3. Lihat Rincian Pemesanan")
    # print("4. Print truk Pembelian")
    choice_0014 = input("Pilih menu (1-2): ")
    print("")

    if choice_0014 == "1":
        print("=== LIST MAKANAN ===")
        print(f"1. {makanan_1_0014} Harga {harga_makanan_1_0014:.3f}")
        print(f"2. {makanan_2_0014} Harga {harga_makanan_2_0014:.3f}")
        print(f"3. {makanan_3_0014} Harga {harga_makanan_3_0014:.3f}")
        print(f"4. {makanan_4_0014} Harga {harga_makanan_4_0014:.3f}")
        print(f"5. {makanan_5_0014} Harga {harga_makanan_5_0014:.3f}")
        print("")
        print("=== MASUKKAN JUMLAH ITEM MAKANAN ===")
        jumlah_mak_1_0014 = int(
            input(f"jumlah banyaknya {makanan_1_0014} yang ingin dibeli: "))
        jumlah_mak_2_0014 = int(
            input(f"jumlah banyaknya {makanan_2_0014} yang ingin dibeli: "))
        jumlah_mak_3_0014 = int(
            input(f"jumlah banyaknya {makanan_3_0014} yang ingin dibeli: "))
        jumlah_mak_4_0014 = int(
            input(f"jumlah banyaknya {makanan_4_0014} yang ingin dibeli: "))
        jumlah_mak_5_0014 = int(
            input(f"jumlah banyaknya {makanan_5_0014} yang ingin dibeli: "))
        total_harga_mak_0014 = (jumlah_mak_1_0014 * harga_makanan_1_0014) + (jumlah_mak_2_0014 * harga_makanan_2_0014) + (
            jumlah_mak_3_0014 * harga_makanan_3_0014) + (jumlah_mak_4_0014 * harga_makanan_4_0014) + (jumlah_mak_5_0014 * harga_makanan_5_0014)
        print(f"Total Harga Makanan: {total_harga_mak_0014:.3f}")
        print("")

    elif choice_0014 == "2":
        print("=== LIST MINUMAN ===")
        print(f"1. {minuman_1_0014} Harga {harga_minuman_1_0014:.3f}")
        print(f"2. {minuman_2_0014} Harga {harga_minuman_2_0014:.3f}")
        print(f"3. {minuman_3_0014} Harga {harga_minuman_3_0014:.3f}")
        print(f"4. {minuman_4_0014} Harga {harga_minuman_4_0014:.3f}")
        print(f"5. {minuman_5_0014} Harga {harga_minuman_5_0014:.3f}")
        print("")
        print("=== MASUKKAN JUMLAH ITEM MINUMAN ===")
        jumlah_min_1_0014 = int(
            input(f"jumlah banyaknya {minuman_1_0014} yang ingin dibeli: "))
        jumlah_min_2_0014 = int(
            input(f"jumlah banyaknya {minuman_2_0014} yang ingin dibeli: "))
        jumlah_min_3_0014 = int(
            input(f"jumlah banyaknya {minuman_3_0014} yang ingin dibeli: "))
        jumlah_min_4_0014 = int(
            input(f"jumlah banyaknya {minuman_4_0014} yang ingin dibeli: "))
        jumlah_min_5_0014 = int(
            input(f"jumlah banyaknya {minuman_5_0014} yang ingin dibeli: "))
        total_harga_min_0014 = (jumlah_min_1_0014 * harga_minuman_1_0014) + (jumlah_min_2_0014 * harga_minuman_2_0014) + (
            jumlah_min_3_0014 * harga_minuman_3_0014) + (jumlah_min_4_0014 * harga_minuman_4_0014) + (jumlah_min_5_0014 * harga_minuman_5_0014)
        print(f"Total Harga Minuman: {total_harga_min_0014:.3f}")
        print("")

        print("=== RINCIAN PEMBAYARAN ===")
        total_semua_0014 = total_harga_mak_0014 + total_harga_min_0014
        print(f"Total Keseluruhan: {total_semua_0014:.3f}")

        if total_semua_0014 > 500.000:
            diskon_0014 = 25/100
        elif total_semua_0014 >= 250.000:
            diskon_0014 = 15/100
        elif total_semua_0014 >= 100.000:
            diskon_0014 = 10/100
        else:
            diskon_0014 = 0

        harga_diskon_0014 = total_semua_0014 * diskon_0014
        setelah_diskon_0014 = total_semua_0014 - harga_diskon_0014
        print(f"Total Setelah Diskon: {setelah_diskon_0014:.3f}")
        print("")

        print("=== MASUKKAN IDENTITAS PEMBELI ===")
        nama_0014 = input("Masukkan Nama: ")
        nim_0014 = int(input("Masukkan Nim: "))
        print(f"Total Belanja: {setelah_diskon_0014:.3f}")
        nominal_0014 = float(input("Nominal Uang: "))
        kembalian_0014 = nominal_0014 - setelah_diskon_0014
        print()

        print('>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<')
        print('>>> S T R U K   P E M B E L I <<<')
        print('>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<')
        print(f"Nama       : {nama_0014}")
        print(f"NIM        : {nim_0014}")
        print(f"Tagihan    : Rp. {setelah_diskon_0014:.3f}")
        print(f"Uang       : Rp. {nominal_0014:.3f}")
        print(f"Kembalian  : Rp. {kembalian_0014:.3f}")
        print('>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<')
        print('>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<')
        break

    else:
        print("Pilihan tidak Valid")
        break
