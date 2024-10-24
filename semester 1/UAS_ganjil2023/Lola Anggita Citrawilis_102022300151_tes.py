from datetime import datetime


class Parkir:
    def _init_(self):
        self.data_kendaraan = {}
        self.transaksi_parkir = []
        self.tarif_per_detik = 166.667  # Rp 10.000 per detik
        # Maksimal waktu parkir 4 menit (240 detik)
        self.max_waktu_parkir = 240
        self.denda_4_menit = 0.10  # Denda 10% untuk parkir lebih dari 4 menit
        self.denda_6_menit = 0.25  # Denda 25% untuk parkir lebih dari 6 menit
        self.pin_admin = "1234"  # PIN admin

    def buka_gerbang_masuk(self):
        print("Silahkan masuk")

    def buka_gerbang_keluar(self):
        print("Terima Kasih")

    def hitung_biaya_parkir(self, waktu_parkir):
        # Pembulatan waktu parkir sesuai syarat
        if waktu_parkir <= 60:
            waktu_parkir_bulat = 60
        elif waktu_parkir >= 75:
            waktu_parkir_bulat = 120
        elif waktu_parkir > 60:
            waktu_parkir_bulat = waktu_parkir
        elif waktu_parkir <= 240:
            waktu_parkir_bulat = ((waktu_parkir + 59) // 60) * 60
        else:
            waktu_parkir_bulat = self.max_waktu_parkir

        total_biaya = int(waktu_parkir_bulat * self.tarif_per_detik)

        if waktu_parkir_bulat > self.max_waktu_parkir:
            if waktu_parkir_bulat > 6 * 60:  # Lebih dari 6 menit
                total_biaya += int(total_biaya * self.denda_6_menit)
            else:
                total_biaya += int(total_biaya * self.denda_4_menit)

        return total_biaya

    def catat_transaksi(self, nomor_plat, waktu_masuk, waktu_keluar, biaya_parkir):
        transaksi = {
            "nomor_plat": nomor_plat,
            "waktu_masuk": waktu_masuk,
            "waktu_keluar": waktu_keluar,
            "biaya_parkir": biaya_parkir
        }
        self.transaksi_parkir.append(transaksi)

    def menu_masuk(self):
        nomor_plat = input("Masukkan nomor plat kendaraan: ")
        # Manual input waktu masuk
        waktu_masuk = input("Masukkan waktu masuk (HH:MM:SS): ")
        self.data_kendaraan[nomor_plat] = {"waktu_masuk": waktu_masuk}
        self.buka_gerbang_masuk()

    def menu_keluar(self):
        nomor_plat = input("Masukkan nomor plat kendaraan: ")
        if nomor_plat not in self.data_kendaraan:
            print("Error: Kendaraan tidak terdaftar di area parkir.")
            return

        # Manual input waktu keluar
        waktu_keluar = input("Masukkan waktu keluar (HH:MM:SS): ")
        waktu_masuk = self.data_kendaraan[nomor_plat]["waktu_masuk"]

        # Hitung waktu parkir dalam detik
        waktu_masuk_dt = datetime.strptime(waktu_masuk, "%H:%M:%S")
        waktu_keluar_dt = datetime.strptime(waktu_keluar, "%H:%M:%S")
        waktu_parkir_detik = max(
            60, (waktu_keluar_dt - waktu_masuk_dt).total_seconds())

        # Hitung biaya parkir
        biaya_parkir = self.hitung_biaya_parkir(waktu_parkir_detik)

        print(f"Biaya parkir: Rp {biaya_parkir}")
        nominal_pembayaran = float(input("Masukkan nominal pembayaran: "))

        if nominal_pembayaran < biaya_parkir:
            print("Error: Pembayaran kurang.")
            return

        kembalian = nominal_pembayaran - biaya_parkir
        print(f"Kembalian: Rp {kembalian}")

        self.buka_gerbang_keluar()
        self.catat_transaksi(nomor_plat, waktu_masuk,
                             waktu_keluar, biaya_parkir)
        del self.data_kendaraan[nomor_plat]

    def menu_admin(self):
        pin = input("Masukkan PIN Admin: ")
        if pin == self.pin_admin:
            while True:
                print("\nMenu Admin Parkir:")
                print("1. Cetak Seluruh Transaksi Parkir")
                print("2. Kembali ke Menu Utama")

                admin_pilihan = input("Pilih menu (1-2): ")

                if admin_pilihan == "1":
                    self.cetak_seluruh_transaksi()
                elif admin_pilihan == "2":
                    break
                else:
                    print("Error: Pilihan menu tidak valid. Silakan pilih 1-2.")

    def cetak_seluruh_transaksi(self):
        print("\nSeluruh Transaksi Parkir:")
        for transaksi in self.transaksi_parkir:
            print(f"Nomor Plat: {transaksi['nomor_plat']}")
            print(f"Waktu Masuk: {transaksi['waktu_masuk']}")
            print(f"Waktu Keluar: {transaksi['waktu_keluar']}")
            print(f"Biaya Parkir: Rp {transaksi['biaya_parkir']}\n")


# Contoh penggunaan program
parkir_app = Parkir()

while True:
    print("\nMenu Parkir:")
    print("1. Masuk Area Parkir")
    print("2. Keluar Area Parkir")
    print("3. Admin Parkir")
    print("0. Keluar")

    pilihan = input("Pilih menu (0-3): ")

    if pilihan == "1":
        parkir_app.menu_masuk()
    elif pilihan == "2":
        parkir_app.menu_keluar()
    elif pilihan == "3":
        parkir_app.menu_admin()
    elif pilihan == "0":
        print("Program keluar.")
        break
    else:
        print("Error: Pilihan menu tidak valid. Silakan pilih 0-3.")
