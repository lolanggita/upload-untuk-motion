import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Fungsi untuk menghubungkan dan membuat tabel jika belum ada
def connect():
    conn = sqlite3.connect('gudang1.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS barang_gudang(
                    id_barang INTEGER PRIMARY KEY AUTOINCREMENT,
                    nama_barang TEXT,
                    jumlah_barang INTEGER,
                    harga_barang INTEGER)''')
    conn.commit()
    conn.close()
    st.success("Tabel 'barang_gudang' telah dibuat")

# Fungsi untuk menambahkan barang
def insert_barang():
    conn = sqlite3.connect('gudang1.db')
    cursor = conn.cursor()
    nama_barang = st.text_input('Masukkan nama barang')
    jumlah_barang = st.number_input('Masukkan jumlah barang', min_value=0)
    harga_barang = st.number_input('Masukkan harga barang', min_value=0)

    if st.button('Tambah Barang'):
        cursor.execute("INSERT INTO barang_gudang(nama_barang, jumlah_barang, harga_barang) VALUES (?, ?, ?)", (nama_barang, jumlah_barang, harga_barang))
        conn.commit()
        conn.close()
        st.success(f"Barang '{nama_barang}' telah dimasukkan dalam gudang")

# Fungsi untuk menampilkan daftar barang
def tampilkan_barang():
    conn = sqlite3.connect('gudang1.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM barang_gudang")
    result = cursor.fetchall()
    conn.close()

    table = PrettyTable(['ID Barang', 'Nama Barang', 'Stok', 'Harga Satuan(Rp)'])
    for row in result:
        table.add_row(row)
    
    st.text(table)

# Fungsi untuk memperbarui barang
def update_barang():
    id_pilihan = st.number_input('Masukkan ID barang yang ingin diperbarui', min_value=0)
    nama_barang = st.text_input('Masukkan nama barang baru')
    jumlah_barang = st.number_input('Masukkan jumlah barang baru', min_value=0)
    harga_barang = st.number_input('Masukkan harga barang baru', min_value=0)

    if st.button('Perbarui Barang'):
        conn = sqlite3.connect('gudang1.db')
        cur = conn.cursor()
        cur.execute("UPDATE barang_gudang SET nama_barang = ?, jumlah_barang = ?, harga_barang = ? WHERE id_barang = ?", (nama_barang, jumlah_barang, harga_barang, id_pilihan))
        conn.commit()
        conn.close()
        st.success(f"Barang dengan ID '{id_pilihan}' telah diperbarui")

# Fungsi untuk menghapus barang
def hapus_barang():
    id_barang = st.number_input('Masukkan ID barang yang ingin dihapus', min_value=0)

    if st.button('Hapus Barang'):
        conn = sqlite3.connect('gudang1.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM barang_gudang WHERE id_barang=?", (id_barang,))
        result = cursor.fetchone()
        if result:
            cursor.execute("DELETE FROM barang_gudang WHERE id_barang=?", (id_barang,))
            conn.commit()
            st.success(f"Barang dengan ID '{id_barang}' telah dihapus dari database")
        else:
            st.error("Barang tidak ada")
        conn.close()

# Fungsi untuk mencari barang berdasarkan ID
def search_id():
    id_barang = st.number_input('Masukkan ID barang yang ingin dicari', min_value=0)

    if st.button('Cari Barang'):
        conn = sqlite3.connect("gudang1.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM barang_gudang WHERE id_barang=?", (id_barang,))
        result = cursor.fetchall()
        conn.close()

        table = PrettyTable(['ID Barang', 'Nama Barang', 'Stok', 'Harga Satuan(Rp)'])
        for row in result:
            table.add_row(row)
        st.text(table)

# Fungsi untuk menampilkan bar chart
def bar_chart():
    conn = sqlite3.connect('gudang1.db')
    cursor = conn.cursor()
    cursor.execute('SELECT nama_barang, SUM(jumlah_barang) as jumlah_stok FROM barang_gudang GROUP BY nama_barang')
    result = cursor.fetchall()
    conn.close()

    nama_barang = [barang[0] for barang in result]
    jumlah_barang = [barang[1] for barang in result]

    plt.figure(figsize=(10, 5))
    plt.bar(nama_barang, jumlah_barang, color='skyblue')
    plt.xlabel('Nama Barang')
    plt.ylabel('Jumlah Barang')
    plt.title('Jumlah Barang di Gudang')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

# Fungsi untuk memfilter barang berdasarkan harga
def filter_barang():
    st.subheader("Filter Berdasarkan")
    filter_option = st.selectbox("Pilih Filter", ["Harga Barang (lebih dari)", "Harga Barang (kurang dari)"])
    harga = st.number_input('Masukkan harga', min_value=0)

    if st.button('Filter Barang'):
        if filter_option == "Harga Barang (lebih dari)":
            execute = '''SELECT * FROM barang_gudang WHERE harga_barang > ?'''
        else:
            execute = '''SELECT * FROM barang_gudang WHERE harga_barang < ?'''
        
        conn = sqlite3.connect("gudang1.db")
        cursor = conn.cursor()
        cursor.execute(execute, (harga,))
        result = cursor.fetchall()
        cursor.close()
        conn.close()

        table = PrettyTable(['ID Barang', 'Nama Barang', 'Stok', 'Harga Satuan(Rp)'])
        for row in result:
            table.add_row(row)
        st.text(table)

# Menu utama
def main():
    st.sidebar.title("Menu")
    menu = st.sidebar.selectbox("Pilih Menu", ["Buat Table", "Tambah Barang", "Lihat Daftar Barang", "Update Barang", "Hapus Barang", "Mencari Barang", "Filter Barang", "Visualisasi Data (Bar Chart)", "Keluar"])

    if menu == "Buat Table":
        connect()
    elif menu == "Tambah Barang":
        insert_barang()
    elif menu == "Lihat Daftar Barang":
        tampilkan_barang()
    elif menu == "Update Barang":
        update_barang()
    elif menu == "Hapus Barang":
        hapus_barang()
    elif menu == "Mencari Barang":
        search_id()
    elif menu == "Filter Barang":
        filter_barang()
    elif menu == "Visualisasi Data (Bar Chart)":
        bar_chart()
    elif menu == "Keluar":
        st.write("Terimakasih telah menggunakan aplikasi ini!")

if __name__ == '__main__':
    main()