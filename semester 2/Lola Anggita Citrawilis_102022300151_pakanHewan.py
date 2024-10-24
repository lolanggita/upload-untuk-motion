day = int(input())
ayam, kambing, sapi =  map( int, input().split())

for i in range(day):
    # menginput jumlah penambahan / pengurangan hewan
    a, b, c =  map( int, input().split())

    # menghitung total hewan
    ayam += a
    kambing += b
    sapi += c
    
    # menghitung total pakan
    pakan_ayam = ayam * 0.5
    pakan_kambing = kambing * 3.5
    pakan_sapi = sapi * 5

    total_pakan = pakan_ayam + pakan_kambing + pakan_sapi

print(f"{total_pakan:.2f}kg")