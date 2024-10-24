def display_menu(menu):
    print("====== Menu ======")
    for item_0151, harga_0151 in menu.items():
        print(f"{item_0151}: Rp.{harga_0151:.2f}")


def place_food_order_0151(food_menu):
    food_order_0151 = {}
    while True:
        display_menu(food_menu)
        food_item_0151 = input("Pilih Makanan yang di inginkan : ")

        if food_item_0151 in food_menu:
            jumlah_0151 = int(
                input(f"Masukkan jumlah {food_item_0151} yang di pesan :  "))
            food_order_0151[food_item_0151] = food_order_0151.get(
                food_item_0151, 0) + jumlah_0151
        else:
            print("Maaf, Pilihan tidak tersedia")

    return food_order_0151


def place_drink_order_0151(drink_menu):
    drink_order_0151 = {}
    while True:
        display_menu(drink_menu)
        drink_item_0151 = input("Pilih Minuman yang di inginkan : ")

        if drink_item_0151 in drink_menu:
            jumlah_0151 = int(
                input(f"Masukkan jumlah {drink_item_0151} yang di pesan : "))
            drink_order_0151[drink_item_0151] = drink_order_0151.get(
                drink_item_0151, 0) + jumlah_0151
        else:
            print("Maaf, Pilihan tidak tersedia")

    return drink_order_0151


def hitung_total(order, menu):
    total_0151 = sum(menu[item_0151] * order[item_0151] for item_0151 in order)
    return total_0151


def hitung_diskon(total_0151):
    if total_0151 >= 500000:
        diskon_rate_0151 = 0.25
    elif total_0151 >= 250000:
        diskon_rate_0151 = 0.15
    elif total_0151 >= 100000:
        diskon_rate_0151 = 0.10

    return total_0151 * diskon_rate_0151


def menu():
    food_menu_0151 = {
        'Rendang': 18000,
        'Kikil': 15000,
        'Dendeng': 18000,
        'Gulai Ikan': 17000,
        'Gulai Ayam': 14000
    }
    drink_menu_0151 = {
        'Lemon Tea': 8000,
        'Espresso': 12000,
        'Coffee Latte': 18000,
        'Matcha Latte': 18000,
        'Milkchoco': 15000
    }

    food_order_0151 = place_food_order_0151(food_order_0151)
    drink_order_0151 = place_drink_order_0151(drink_menu_0151)

    print("\nMakanan :")
    for item_0151, jumlah_0151 in food_order_0151.items():
        print(f"{item_0151.capitalize()}: {jumlah_0151}")

    print("\nMinuman :")
    for item_0151, jumlah_0151 in drink_order_0151.items():
        print(f"{item_0151.capitalize()}: {jumlah_0151}")

    total_food_0151 = hitung_total(food_order_0151, food_menu_0151)
    total_drink_0151 = hitung_total(drink_order_0151, drink_menu_0151)
    total_0151 = total_food_0151 + total_drink_0151
    diskon_0151 = hitung_diskon(total_0151)
    print(f"\nTotal : Rp. {total_0151:.2f}")

    if diskon_0151 > 0:
        print(
            f"Diskon ({diskon_0151/total_0151 *100}%) : Rp. {diskon_0151:.2f}")
    else:
        print("Tidak ada diskon.")

    total_diskon_0151 = total_0151 - diskon_0151
    print(f"Total Akhir : Rp. {total_diskon_0151:.2f}")


menu()
