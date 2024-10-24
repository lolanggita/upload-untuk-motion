class pegawai:
    '''Class Para Pegawai Universitas Telkom'''

    def __init__(self, NIP, nama, jabatan, umur, jenkel, notelp):
        self.nip = NIP
        self.nama = nama
        self.jabatan = jabatan
        self.umur = umur
        self.jenkel = jenkel
        self.notelp = notelp

    def tampilkan_profil(self):
        print("\n==========================================")
        print("|| NIP\t\t\t: ", self.nip)
        print("|| Nama\t\t\t: ", self.nama)
        print("|| Jabatan\t\t: ", self.jabatan)
        print("|| Umur\t\t\t: ", self.umur)
        print("|| Jenis Kelamin\t: ", self.jenkel)
        print("|| No Telepon\t\t: ", self.notelp)

    def tampilkan_gaji(self, total_gaji):
        gaji = 2500000
        sks_kehadiran = int(input("|| Total sks/kehadiran\t:  "))

        if self.jabatan == "dosen":
            total_gaji = gaji + (sks_kehadiran * 250000)
        elif self.jabatan == "staff":
            total_gaji = gaji + (sks_kehadiran * 150000)

        self.gaji = total_gaji
        print("|| Gaji\t\t\t: ", self.gaji)
        print("==========================================")

# Data pegawai (tanpa inputan)     
karyawan1 = pegawai(1020123, "Abdi", "dosen", 30, "laki-laki", "081200001234")
karyawan2 = pegawai(1020124, "Anisa", "dosen", 33, "perempuan", "081200001235")
karyawan3 = pegawai(1020125, "Cinta", "dosen", 27, "perempuan", "081200001236")
karyawan4 = pegawai(1020126, "Cahyo", "dosen", 42, "laki-laki", "081200001237")
karyawan5 = pegawai(1020127, "Budi", "dosen", 35, "laki-laki", "0812000012348")
karyawan6 = pegawai(1020128, "Kinan", "staff", 25, "perempuan", "081200001239")
karyawan7 = pegawai(1020129, "Nanda", "staff", 26, "laki-laki", "081200001240")
karyawan8 = pegawai(1020130, "Tati", "staff", 40, "perempuan", "081200001245")
karyawan9 = pegawai(1020131, "Judi", "staff", 32, "laki-laki", "081200001280")
karyawan10 = pegawai(1020132, "Yayan", "staff", 27, "laki-laki", "081200001200")

# menampilkan data pegawai dan total gaji
karyawan1.tampilkan_profil()
karyawan1.tampilkan_gaji(0)

karyawan2.tampilkan_profil()
karyawan2.tampilkan_gaji(0)

karyawan3.tampilkan_profil()
karyawan3.tampilkan_gaji(0)

karyawan4.tampilkan_profil()
karyawan4.tampilkan_gaji(0)

karyawan5.tampilkan_profil()
karyawan5.tampilkan_gaji(0)

karyawan6.tampilkan_profil()
karyawan6.tampilkan_gaji(0)

karyawan7.tampilkan_profil()
karyawan7.tampilkan_gaji(0)

karyawan8.tampilkan_profil()
karyawan8.tampilkan_gaji(0)

karyawan9.tampilkan_profil()
karyawan9.tampilkan_gaji(0)

karyawan10.tampilkan_profil()
karyawan10.tampilkan_gaji(0)
