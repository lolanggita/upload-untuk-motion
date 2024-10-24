import sqlite3
from prettytable import PrettyTable
import matplotlib.pyplot as plt

def Create_table():
    conn = sqlite3.connect("perpustakaan.db")
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS tabel_buku (
                id_buku INTEGER  PRIMARY KEY AUTOINCREMENT,
                judul TEXT NOT NULL,
                penulis TEXT NOT NULL,
                tahun_terbit INTEGER,
                genre TEXT,
                stok INTEGER NOT NULL
                )
                """)
    conn.commit()
    print("Tabel 'tabel_buku' telah dibuat\n")
    conn.close()
    

def insert_book(id_buku, judul, penulis, tahun_terbit, genre, stok):
    conn = sqlite3.connect("perpustakaan.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO tabel_buku (id_buku, judul, penulis, tahun_terbit, genre, stok) VALUES (?, ?, ?, ?, ?, ?)", (id_buku, judul, penulis, tahun_terbit, genre, stok))
    conn.commit()
    print(f"Buku '{judul}' telah ditambahkan ke dalam database.\n")
    conn.close()

def Input_book():
    jumlah = int(input("Masukkan Jumlah Buku: "))

    i = 0
    while i < jumlah:
        judul = input("Masukan Judul Buku: ")
        if not judul:
            break
        else:
            penulis = input("Masukan penulis Buku: ")
            tahun_terbit = input("Masukan tahun terbit: ")
            genre = input("Masukan genre Buku: ")
            stok = input("Masukan Jumlah stok: ")
            id_buku = None
        i += 1
        insert_book(id_buku, judul, penulis, tahun_terbit, genre, stok)

def Show_book():
    conn = sqlite3.connect("perpustakaan.db")
    cur = conn.cursor()
    cur.execute("SELECT id_buku, judul, penulis, tahun_terbit, genre, stok FROM tabel_buku")
    res = cur.fetchall()
    if len(res) == 0:
        print("Data tidak ditemukan")
    else:
        table = PrettyTable()
        table.field_names = ["id_buku", "Judul", "Penulis", "Tahun Terbit", "Genre", "Stok"]
            
        for row in res:
            table.add_row(row)
            
        print(table)
    conn.close()

def Delete_book():
    id_buku = input("Masukkan ID buku yang ingin dihapus: ")
    conn = sqlite3.connect("perpustakaan.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM tabel_buku WHERE id_buku = ?", (id_buku,))
    conn.commit()
    print(f"Buku dengan ID {id_buku} telah dihapus dari database.")
    conn.close()

def Show_data():
    conn = sqlite3.connect("perpustakaan.db")
    cur = conn.cursor()
    cur.execute("SELECT genre, stok FROM tabel_buku")
    data = cur.fetchall()
    conn.close()
    genre = [buku[0] for buku in data]
    stok = [buku[1] for buku in data]
    plt.figure(figsize=(10, 5))
    plt.bar(genre, stok, color='#87cdeb')
    plt.xlabel('Genre')
    plt.ylabel('Jumlah buku')
    plt.title('Jumlah buku per genre')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

while True:
    print("\nMenu: ")
    print("1. Buat Tabel")
    print("2. Masukan Buku")
    print("3. Tampilkan buku ")
    print("4. Hapus Buku")
    print("5. Tampilkan data")
    print("6. Keluar")
    
    choose = int(input("Pilih Menu: "))

    if choose == 1 :
        Create_table() 
    elif choose == 2 :
        Input_book() 
    elif choose == 3 :
        Show_book() 
    elif choose == 4 :
        Delete_book() 
    elif choose == 5 :
        Show_data() 
    elif choose == 6 :
        print("Terima kasih! Program berakhir.")
        break 
    else:
        print("Masukkan angka yang sesuai pada menu!")

