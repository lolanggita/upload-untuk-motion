berat = int(input("Masukkan berat muatan (ton): "))
penumpang = int(input("Masukkan jumlah penumpang: "))

if penumpang <= 40:
    if berat > 5 and berat <= 20:
        print("Kendaraan yang sesuai adalah Truk")
    elif berat > 1 and berat <= 5:
        print("Kendaraan yang sesuai adalah Bus")
    elif berat == 0 or berat <= 1:
        print("Kendaraan yang sesuai adalah Mobil")
elif penumpang <= 5:
    if berat > 5 and berat <= 20:
        print("Kendaraan yang sesuai adalah Truk")
    elif berat > 1 and berat <= 5:
        print("Kendaraan yang sesuai adalah Bus")
    elif berat == 0 or berat <= 1:
        print("Kendaraan yang sesuai adalah Mobil")
elif penumpang == 0:
    if berat > 5 and berat <= 20:
        print("Kendaraan yang sesuai adalah Truk")
    elif berat > 1 and berat <= 5:
        print("Kendaraan yang sesuai adalah Bus")
    elif berat == 0 or berat <= 1:
        print("Kendaraan yang sesuai adalah Mobil")
