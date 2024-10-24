import numpy as np 

no_kamar = np.array(range(1,9))
tarif_bulanan = np.array(1500000, 1500000, 1500000, 2000000, 1800000, 1800000, 2000000, 2000000)
Tunggakan = np.array([0, 300000, 150000, 0, 0, 500000, 250000, 0])

# Menghitung total tagihan
tagihan = dict(zip(no_kamar, tarif_bulanan + Tunggakan))
diskon = dict(zip(no_kamar[Tunggakan == 0], tarif_bulanan[Tunggakan == 0] * 0.05))

tagihan = {k:v - diskon.get(k, v) for k, v in tagihan.items()}

# Menghitung total pemasukan bulanan
min = np.min(Tunggakan, tarif_bulanan * 0.05)
total_pemasukan = np.sum(tarif_bulanan)