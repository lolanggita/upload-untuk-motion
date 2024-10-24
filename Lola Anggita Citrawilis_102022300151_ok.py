import numpy as np

rooms = {
    1 : {'cost': 1500000, 'arrears': 0},
    2 : {'cost': 1500000, 'arrears': 300000},
    3 : {'cost': 1500000, 'arrears': 150000},
    4 : {'cost': 2000000, 'arrears': 0},
    5 : {'cost': 1800000, 'arrears': 0},
    6 : {'cost': 1800000, 'arrears': 500000},
    7 : {'cost': 2000000, 'arrears': 250000},
    8 : {'cost': 2000000, 'arrears': 0}
}

# Menghitung total pemasukan bulanan
total_income = 0
total_arrears = 0
total_discount = 0

for room_number, room_data in rooms.items():
    cost = room_data['cost']
    arrears = room_data['arrears']

    if arrears > 0 :
        total_arrears += arrears
    
    elif arrears == 0 :
        discount = cost * 0.05
        total_discount += discount
        cost -= discount
    
    total_income += cost

highest_arrears = max(rooms, key=lambda x: rooms[x]['arrears'])     # Mengidentifikasi tunggakan tertinggi

average_cost = np.mean([room_data['cost'] for room_data in rooms.values()])     # Rata - rata tarif bulanan

# Output 
print("================ Data Tagihan Tiap Kamar ================")
print("|| ".ljust(28) + " ||".rjust(29))
for room_number, room_data in rooms.items():
    cost = room_data['cost']
    arrears = room_data['arrears']

    if arrears > 0 :
        print(f"|| Kamar {room_number} : Tarif = {cost}, Tunggakan = {arrears}" + " ||".rjust(9))
    
    else:
        discount = cost * 0.05
        print(f"|| Kamar {room_number} : Tarif = {cost}, Tunggakan = {discount}" + " ||".rjust(7))

print("|| ".ljust(28) + " ||".rjust(29))
print("=========================================================")
print("|| Total pemasukan bulanan\t\t: " + str(total_income) + " ||".rjust(5))
print("|| Kamar dengan tunggakan tertinggi\t: " + str(highest_arrears) + " ||".rjust(14))
print("|| Rata-rata tarif bulanan\t\t: " + str(average_cost) + " ||".rjust(6))
print("|| Jumlah total tunggakan\t\t: " + str(total_arrears) + " ||".rjust(8))
print("|| Jumlah total diskon\t\t\t: " + str(total_discount) + " ||".rjust(7))
print("=========================================================")