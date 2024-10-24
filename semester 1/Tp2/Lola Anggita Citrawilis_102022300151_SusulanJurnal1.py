belanja = int(input("Masukkan total belanjaan Anda: Rp "))
member = input("Apakah Anda anggota program loyalitas?(ya/tidak): ")

if belanja >= 500000:
    diskon = belanja * 0.20
    total_diskon = belanja - diskon
    if member == "ya":
        total_loyalitas = total_diskon - belanja * 0.05
        print(f"Total belanjaan setelah diskon: Rp{total_loyalitas}")
    elif member == "tidak":
        print(f"Total belanjaan anda : Rp{total_diskon}")
elif belanja >= 300000:
    diskon = belanja * 0.15
    total_diskon = belanja - diskon
    if member == "ya":
        total_loyalitas = total_diskon - belanja * 0.05
        print(f"Total belanjaan setelah diskon: Rp{total_loyalitas}")
    elif member == "tidak":
        print(f"Total belanjaan anda : Rp{total_diskon}")
elif belanja >= 200000:
    diskon = belanja * 0.10
    total_diskon = belanja - diskon
    if member == "ya":
        total_loyalitas = total_diskon - belanja * 0.05
        print(f"Total belanjaan setelah diskon: Rp{total_loyalitas}")
    elif member == "tidak":
        print(f"Total belanjaan anda : Rp{total_diskon}")
else:
    if member == "ya":
        total_loyalitas = belanja - belanja * 0.05
        print(f"Total belanjaan setelah diskon: Rp{total_loyalitas}")
    elif member == "tidak":
        print(f"Total belanjaan anda : Rp{belanja}")
