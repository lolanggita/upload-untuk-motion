# Menginput data mahasiswa
Mahasiswa = input("Masukkan Nama Mahasiswa: ")
NIM = input("Masukkan NIM Mahasiswa: ")
Kelas = input("Masukkan Kelas Mahasiswa: ")

# Menginput dan menghitung nilai mahasiswa
tugas = float(input("Masukkan nilai tugas: "))
quiz = float(input("Masukkan nilai quiz: "))
UTS = float(input("Masukkan nilai UTS: "))
UAS = float(input("Masukkan nilai UAS: "))

rata_rata = (tugas + quiz + UTS + UAS) / 4

# Menampilkan hasil
print(
    f"Rata-rata Nilai MK Pengantar & Pemrograman Logika milik {Mahasiswa} dengan NIM {NIM} dari kelas {Kelas} adalah {rata_rata}")
