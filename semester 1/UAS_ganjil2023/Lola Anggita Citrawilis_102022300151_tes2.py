import datetime

# List parkir
tempat_parkir = {}

akun_pengguna = {
    "kunti": "bogel",
    "lumpur": "lapindo"
}

# List Kendaraan
kendaraan_diparkir = {}


def hitung_biaya_parkir(waktu_masuk, waktu_keluar):
    durasi = waktu_keluar - waktu_masuk
    detik_durasi = durasi.total_seconds()
    jam_durasi, sisa = divmod(detik_durasi, 3600)
    menit_durasi, detik_durasi = divmod(sisa, 60)

    if menit_durasi <= 1:
        biaya = 10000
    elif 1 < menit_durasi <= 2:
        biaya = 20000
    elif 2 < menit_durasi <= 3:
        biaya = 30000
    elif 3 < menit_durasi <= 4:
        biaya = 40000
    else:
        biaya = 40000 + 0.1 * 40000 * (1 if 4 < menit_durasi <= 6 else 0.25)

    return round(biaya), int(jam_durasi), int(menit_durasi), int(detik_durasi)


def masuk_kendaraan():
    nomor_plat = input("Masukkan nomor plat kendaraan: ")
    waktu_masuk = datetime.datetime.now()
    kendaraan_diparkir[nomor_plat] = waktu_masuk
    waktu_masuk_formatted = waktu_masuk.strftime("%Y-%m-%d %H:%M:%S")
    print(
        f"Kendaraan dengan nomor plat {nomor_plat} diparkir pada {waktu_masuk_formatted}")


def keluar_kendaraan():
    nomor_plat = input("Masukkan nomor plat kendaraan: ")
    if nomor_plat in kendaraan_diparkir:
        waktu_masuk = kendaraan_diparkir[nomor_plat]
        waktu_keluar = datetime.datetime.now()

        biaya_parkir, jam, menit, detik = hitung_biaya_parkir(
            waktu_masuk, waktu_keluar)
        waktu_keluar_formatted = waktu_keluar.strftime("%Y-%m-%d %H:%M:%S")
        print(
            f"Kendaraan dengan nomor plat {nomor_plat} keluar pada {waktu_keluar_formatted}")
        print(f"Durasi: {jam} jam, {menit} menit, {detik} detik")
        print(f"Total biaya parkir: Rp.{biaya_parkir}")

        del kendaraan_diparkir[nomor_plat]
    else:
        print("Error: Kendaraan tidak ditemukan di tempat parkir.")


def cek_history():
    username = input("Masukkan nama pengguna: ")
    password = input("Masukkan kata sandi: ")

    if username in akun_pengguna and akun_pengguna[username] == password:
        print(f"History kendaraan diparkir untuk pengguna {username}:")
        for kendaraan, waktu_masuk in kendaraan_diparkir.items():
            waktu_masuk_formatted = waktu_masuk.strftime("%Y-%m-%d %H:%:M%S")
            print(
                f"Kendaraan dengan nomor plat {kendaraan} diparkir pada {waktu_masuk_formatted}")
    else:
        print("Kredensial login tidak valid. Akses ditolak.")


def main():
    while True:
        print(
            "\n1. Masuk Kendaraan\n2. Keluar Kendaraan\n3. Cek History\n4. Keluar Program")
        pilihan = input("Masukkan pilihan Anda (1/2/3/4): ")

        if pilihan == "1":
            masuk_kendaraan()
        elif pilihan == "2":
            keluar_kendaraan()
        elif pilihan == "3":
            cek_history()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid. Harap masukkan opsi yang valid.")


if __name__ == "__main__":
    main()
