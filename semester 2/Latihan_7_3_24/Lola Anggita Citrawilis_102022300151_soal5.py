import array

# Menerima input
N = int(input().strip())
penggunaan = array.array('i', map(int, input().strip().split()))
pembelian = array.array('i', map(int, input().strip().split()))

# Menghitung sisa persediaan
sisa_persediaan = array.array('i', (b - a for a, b in zip(penggunaan, pembelian)))

print(*sisa_persediaan)