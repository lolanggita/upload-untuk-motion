class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga


class Pembelian:
    def __init__(self):
        self.keranjang = {}

    def tambah_barang(self, produk, jumlah):
        if produk.nama in self.keranjang:
            self.keranjang[produk.nama] += jumlah
        else:
            self.keranjang[produk.nama] = jumlah

    def hitung_total(self):
        total = 0
        for nama_produk, jumlah in self.keranjang.items():
            total += produk_dict[nama_produk].harga * jumlah
        return total


# Membuat beberapa produk dan menyimpannya dalam list
daftar_produk = [
    Produk("Laptop", 10000000),
    Produk("Kemeja", 500000),
    Produk("Smartphone", 8000000),
    # Tambahkan produk lain sesuai kebutuhan
]

# Membuat dictionary untuk menyimpan produk
produk_dict = {produk.nama: produk for produk in daftar_produk}

# Membuat objek pembelian
pembelian = Pembelian()

# Menampilkan kategori produk
print("Pilih kategori produk:")
for i, produk in enumerate(daftar_produk, start=1):
    print(f"{i}. {produk.nama}")

# Meminta pengguna memilih kategori
kategori = input("Masukkan nomor kategori: ")

# Memproses pilihan kategori
try:
    index_produk = int(kategori) - 1
    produk_pilihan = daftar_produk[index_produk]
except IndexError:
    print("Pilihan kategori tidak valid.")
    exit()

# Meminta pengguna memasukkan jumlah barang yang akan dibeli
jumlah_barang = int(
    input(f"Masukkan jumlah {produk_pilihan.nama} yang akan dibeli: "))

# Menambahkan barang ke keranjang
pembelian.tambah_barang(produk_pilihan, jumlah_barang)

# Menampilkan total harga pembelian
total_harga = pembelian.hitung_total()
print(f"Total harga pembelian: Rp {total_harga}")
