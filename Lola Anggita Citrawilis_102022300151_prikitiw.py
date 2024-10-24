import numpy as np

# Array data penjualan
data_penjualan = np.array([
    ["Krisna", 3500000, 2500000, 0],
    ["Marc", 4800000, 0, 2000000],
    ["Chelle", 5200000, 3000000, 0],
    ["Kholaif", 6000000, 0, 3000000],
    ["Bhawa", 3000000, 2500000, 0],
    ["Ali", 4500000, 0, 2500000],
    ["Rizky", 5800000, 4000000, 0],
    ["Andika", 6500000, 0, 3500000]
])

total_pendapatan = sum(int(data[1]) + int(data[2]) + int(data[3]) for data in data_penjualan)       # menghitung total pendapatan toko

max_tunai = max(int(data[2]) for data in data_penjualan)    # mencari bulan dengan jumlah pembayaran tunai tertinggi
bulan_max_tunai = [data[0] for data in data_penjualan if int(data[2]) == max_tunai]

total_diskon = sum(int(data[2]) * 0.05 for data in data_penjualan)      # menghitung total diskon yang diberikan kepada pelanggan yang membayar secara tunai
total_tunggakan = sum(int(data[3]) for data in data_penjualan)      # menghitung total tunggakan yang belum dibayar oleh pelanggan

# Output
print("==============================================================================================================================")   
print("No. Transaksi".ljust(15) + "|".center(12) + "Total Penjualan (Rp)".center(21) + "|".center(12)  + "Pembayaran Tunai (Rp)".center(20) + "|".center(12) + "Sisa Tunggakan (Rp)".center(20))
print("==============================================================================================================================")

for i, data in enumerate(data_penjualan):
    print(f"{i+1}. {data[0]:<13}    |       {data[1]:<21}    |      {data[2]:<22}    |      {data[3]:<18}")

print("==============================================================================================================================")
print(f"|| Total Pendapatan Toko Bahagia selama beberapa bulan terakhir (termasuk pembayaran tunai dan tunggakan) : Rp. {total_pendapatan:,.0f}" + "||".rjust(4))
print(f"|| Bulan dengan jumlah pembayaran tunai tertinggi\t\t\t\t\t\t\t  : {bulan_max_tunai[0]}" + "||".rjust(13))
print(f"|| Total diskon yang diberikan kepada pelanggan yang membayar secara tunai\t\t\t\t  : Rp. {total_diskon:,.0f}" + "||".rjust(7))
print(f"|| Total tunggakan yang belum dibayar oleh pelanggan\t\t\t\t\t\t\t  : Rp. {total_tunggakan:,.0f}" + "||".rjust(4))
print("==============================================================================================================================")
