import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Fungsi untuk membuat tabel di database jika belum ada
def create_table():
    conn = sqlite3.connect('gudangbektel.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS barang_gudang(
                id_barang INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_barang TEXT,
                jumlah_barang INTEGER,
                harga_barang INTEGER,
                gambar BLOB)''')
    conn.commit()
    conn.close()

# Inisialisasi tabel di database
create_table()

def insert_barang():
    st.title("Tambah Barang")
    nama_barang = st.text_input('Masukkan nama barang')
    jumlah_barang = st.number_input('Masukkan jumlah barang', min_value=0)
    harga_barang = st.number_input('Masukkan harga barang', min_value=0)
    gambar_barang = st.file_uploader("Unggah gambar barang", type=["jpg", "png", "jpeg"])

    if st.button('Tambah Barang'):
        if gambar_barang is not None:
            gambar_bytes = gambar_barang.read()
            conn = sqlite3.connect('gudangbektel.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO barang_gudang (nama_barang, jumlah_barang, harga_barang, gambar) VALUES (?, ?, ?, ?)",
                           (nama_barang, jumlah_barang, harga_barang, gambar_bytes))
            conn.commit()
            conn.close()
            st.success(f"Barang '{nama_barang}' telah dimasukkan dalam gudang")
        else:
            st.error("Harap unggah gambar barang.")

def tampilkan_barang():
    st.title("Daftar Barang")
    conn = sqlite3.connect('gudangbektel.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM barang_gudang")
    data = cursor.fetchall()
    conn.close()
    
    if data:
        df = pd.DataFrame(data, columns=['ID Barang', 'Nama Barang', 'Jumlah Barang', 'Harga Barang', 'Gambar'])
        for _, row in df.iterrows():
            if row['Gambar']:
                st.image(row['Gambar'])
            st.write(f"ID Barang: {row['ID Barang']}")
            st.write(f"Nama Barang: {row['Nama Barang']}")
            st.write(f"Jumlah Barang: {row['Jumlah Barang']}")
            st.write(f"Harga Barang: {row['Harga Barang']}")
            st.write("---")
    else:
        st.write("Tidak ada barang dalam gudang.")

def update_barang():
    st.title("Update Barang")
    id_pilihan = st.number_input('Masukkan ID barang yang ingin diperbarui', min_value=1)
    nama_barang = st.text_input('Masukkan nama barang baru')
    jumlah_barang = st.number_input('Masukkan jumlah barang baru', min_value=0)
    harga_barang = st.number_input('Masukkan harga barang baru', min_value=0)
    gambar_barang = st.file_uploader("Unggah gambar barang baru", type=["jpg", "png", "jpeg"])

    if st.button('Perbarui Barang'):
        conn = sqlite3.connect('gudangbektel.db')
        cursor = conn.cursor()
        if gambar_barang is not None:
            gambar_bytes = gambar_barang.read()
            cursor.execute("UPDATE barang_gudang SET nama_barang = ?, jumlah_barang = ?, harga_barang = ?, gambar = ? WHERE id_barang = ?",
                           (nama_barang, jumlah_barang, harga_barang, gambar_bytes, id_pilihan))
        else:
            cursor.execute("UPDATE barang_gudang SET nama_barang = ?, jumlah_barang = ?, harga_barang = ? WHERE id_barang = ?",
                           (nama_barang, jumlah_barang, harga_barang, id_pilihan))
        conn.commit()
        conn.close()
        st.success(f"Barang dengan ID '{id_pilihan}' telah diperbarui")

def hapus_barang():
    st.title("Hapus Barang")
    id_barang = st.number_input('Masukkan ID barang yang ingin dihapus', min_value=1)
    if st.button('Hapus Barang'):
        conn = sqlite3.connect('gudangbektel.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM barang_gudang WHERE id_barang = ?", (id_barang,))
        conn.commit()
        conn.close()
        st.success(f"Barang dengan ID '{id_barang}' telah dihapus dari database")

def search_id():
    st.title("Cari Barang")
    id_barang = st.number_input('Masukkan ID barang yang ingin dicari', min_value=1)
    if st.button('Cari Barang'):
        conn = sqlite3.connect('gudangbektel.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM barang_gudang WHERE id_barang = ?", (id_barang,))
        data = cursor.fetchall()
        conn.close()
        
        if data:
            df = pd.DataFrame(data, columns=['ID Barang', 'Nama Barang', 'Jumlah Barang', 'Harga Barang', 'Gambar'])
            for _, row in df.iterrows():
                if row['Gambar']:
                    st.image(row['Gambar'])
                st.write(f"ID Barang: {row['ID Barang']}")
                st.write(f"Nama Barang: {row['Nama Barang']}")
                st.write(f"Jumlah Barang: {row['Jumlah Barang']}")
                st.write(f"Harga Barang: {row['Harga Barang']}")
                st.write("---")
        else:
            st.error("Barang tidak ditemukan")

def bar_chart():
    st.title("Visualisasi Data (Bar Chart)")
    conn = sqlite3.connect('gudangbektel.db')
    cursor = conn.cursor()
    cursor.execute('SELECT nama_barang, SUM(jumlah_barang) as jumlah_stok FROM barang_gudang GROUP BY nama_barang')
    data = cursor.fetchall()
    conn.close()

    if data:
        df = pd.DataFrame(data, columns=['Nama Barang', 'Jumlah Barang'])
        plt.figure(figsize=(10, 5))
        plt.bar(df['Nama Barang'], df['Jumlah Barang'], color='skyblue')
        plt.xlabel('Nama Barang')
        plt.ylabel('Jumlah Barang')
        plt.title('Jumlah Barang di Gudang')
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(plt)
    else:
        st.write("Tidak ada barang dalam gudang untuk divisualisasikan.")

def filter_barang():
    st.title("Filter Barang")
    filter_option = st.selectbox("Pilih Filter", ["Harga Barang (lebih dari)", "Harga Barang (kurang dari)"])
    harga = st.number_input('Masukkan harga', min_value=0)

    if st.button('Filter Barang'):
        conn = sqlite3.connect('gudangbektel.db')
        cursor = conn.cursor()
        if filter_option == "Harga Barang (lebih dari)":
            cursor.execute("SELECT * FROM barang_gudang WHERE harga_barang > ?", (harga,))
        else:
            cursor.execute("SELECT * FROM barang_gudang WHERE harga_barang < ?", (harga,))
        data = cursor.fetchall()
        conn.close()

        if data:
            df = pd.DataFrame(data, columns=['ID Barang', 'Nama Barang', 'Jumlah Barang', 'Harga Barang', 'Gambar'])
            for _, row in df.iterrows():
                if row['Gambar']:
                    st.image(row['Gambar'])
                st.write(f"ID Barang: {row['ID Barang']}")
                st.write(f"Nama Barang: {row['Nama Barang']}")
                st.write(f"Jumlah Barang: {row['Jumlah Barang']}")
                st.write(f"Harga Barang: {row['Harga Barang']}")
                st.write("---")
        else:
            st.write("Tidak ada barang yang memenuhi kriteria.")

page_bg_img = """
<style>
    [data-testid="stAppViewContainer"] > .main {
        background-image: linear-gradient(#538392, #26355D);
        color: white;
    }
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


# Menu utama
def main():
    st.sidebar.title("Menu")
    menu = st.sidebar.selectbox("Pilih Menu", ["Tambah Barang", "Lihat Daftar Barang", "Update Barang", "Hapus Barang", "Mencari Barang", "Filter Barang", "Visualisasi Data (Bar Chart)"])

    if menu == "Tambah Barang":
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

if __name__ == '__main__':
    main()