import numpy as np

pendapatan = {
    "A": 1000000,
    "B": 800000,
    "C": 1200000,
    "D": 900000,
    "E": 1100000, 
}

pengeluaran = {
    "A": 600000,
    "B": 500000,
    "C": 700000,
    "D": 400000,
    "E": 600000,   
}

total_pendapatan = sum(pendapatan.values())
total_pengeluaran = sum(pengeluaran.values())
laba_kotor = total_pendapatan - total_pengeluaran

pengurangan_pajak = 0.1 * laba_kotor
tarif_pajak = {
    "A": 0.2, 
    "B": 0.25, 
    "C": 0.15, 
    "D": 0.3, 
    "E": 0.18
}

total_pajak_per_negara = {negara: (tarif_pajak[negara] * laba_kotor) - pengurangan_pajak for negara in tarif_pajak}

memenuhi_persyaratan_perpajakan = all(pajak > 50000 for pajak in total_pajak_per_negara.values())

print("Total pendapatan perusahaan:", total_pendapatan)
print("Total pengeluaran perusahaan:", total_pengeluaran)
print("Total laba kotor perusahaan:", laba_kotor)
print("Total pengurangan pajak:", pengurangan_pajak)
print("Total pajak yang harus dibayar per negara:", total_pajak_per_negara)
print("Apakah perusahaan memenuhi persyaratan perpajakan?", "Ya" if memenuhi_persyaratan_perpajakan else "Tidak")
