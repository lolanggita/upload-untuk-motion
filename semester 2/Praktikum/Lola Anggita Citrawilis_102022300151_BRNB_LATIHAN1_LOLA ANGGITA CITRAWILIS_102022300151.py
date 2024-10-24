#import library sqlite 3 dan maplotlib
import sqlite3
import matplotlib.pyplot as plt
from prettytable import PrettyTable

#buatlah database yang dapat diakses secara keseluruhan

#Buatlah fungsi untuk membuat tabel
def buattabel(): 
    conn = sqlite3.connect("Apotek.db")
    cur = conn.cursor()
    cur.execute(""" CREATE TABLE IF NOT EXISTS obat (id_obat INTEGER primary key, nama TEXT not null, harga INTEGER not null, jenis_obat TEXT not null)
                """)
    conn.commit()
    cur.close()

#Buatlah fungsi untuk menambahkan obat
def tambah_obat(id_obat, nama, harga, stok, jenis_obat):
    conn = sqlite3.connect("Apotek.db")
    cur = conn.cursor()
    id_obat = int(input("Masukkan ID Obat: "))
    nama = input("Masukkan Nama Obat: ")
    harga = int(input("Masukkan Harga Obat: "))
    stok = int(input("Masukkan stok Obat: "))
    jenis_obat = input("Masukkan Jenis Obat: ")
    cur.execute("INSERT INTO obat (?,?,?,?,?)", (id_obat, nama, harga, stok, jenis_obat))
    conn.commit()
    cur.close()

    
#Buatlah fungsi untuk hapus obat berdasarkan id obat
def hapus_obat(id_obat):
    conn = sqlite3.connect("Apotek.db")
    cur = conn.cursor()
    id_obat = int(input("Masukkan ID Obat yang ingin di hapus: "))
    cur.execute("DELETE FROM obat WHERE ID=?", (id_obat))
    conn.commit()
    conn.close()
    
    
#Buatlah fungsi untuk mencari obat berdasarkan id
def cari_obat(id_obat : int):
    conn = sqlite3.connect("Apotek.db")
    cur = conn.commit()
    id_obat = int(input("Masukkan ID Obat yang dicari: "))
    cur.execute(f"""
                SELECT * FROM obat
                WHERE id_obat LIKE "{id_obat}%“
                """)
    result = cur.fetchall()
    cur.close()
    conn.close()
    for row in result:
        print(row)
    

#Buatlah fungsi untuk menampilkan seluruh obat yang ada pada tabel
def tampilkan_obat():
    conn = sqlite3.connect("Apotek.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM obat")
    result = conn.fetchall()
    conn.close()
    return (result)
    
        
#Buatlah fungsi untuk visualisasi data dalam bentuk bar chart
def vis_data():
    conn = sqlite3.connect("Apotek.db")
    cur = conn.commit()
    cur.execute("SELECT * FROM obat")
    data = cur.fetchall()
    cur.close()
    conn.close()
    stok = [obat[3] for obat in data]
    nama = [obat[1] for obat in data]
    plt.boxplot(figsize=(10,7))
    plt.bar(stok, nama, color='#87cdeb')
    plt.xlabel("nama")
    plt.ylabel("stok")
    plt.title("Stok Keseluruhan Obat")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    

#buatlah perulangan untuk menampilkan pilihan menu dan menjalankan program
while True:
    print("Selamat Datang di APOTEK DASPRO!!")
    print("Pilihan Menu:")
    print("1. Membuat Tabel")
    print("2. Menambahkan Obat")
    print("3. Menghapus Obat")
    print("4. Mencari Obat")
    print("5. Menampilkan Data")
    print("6. Visualisasi Data")
    print("7. Keluar")
    pilihan = int(input("Masukan pilihan menu: "))
    if pilihan == 1:
        buattabel()
        print("Tabel berhasil dibuat")
    elif pilihan == 2:
        tambah_obat()
        print("Data Obat berhaisl ditambahkan!")
    elif pilihan == 3:
        hapus_obat()
        print("Data Obat berhasil di hapus")
    elif pilihan == 4:
        cari_obat()
    elif pilihan == 5:
        tampilkan_obat()
    elif pilihan == 6:
        vis_data()
    elif pilihan == 7:
        print("Terimakasih telah menggunakan layanan APOTEK DASPRO!!")
        break
    else :
        print("Pilihan tidak tersedia, Silahkan pilih sesuai dengan Menu yang tersedia!")