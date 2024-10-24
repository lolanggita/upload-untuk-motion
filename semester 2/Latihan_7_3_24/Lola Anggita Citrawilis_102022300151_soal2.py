import array

def rotateArray(arr, N, k):
    # Karena rotasi sirkuler, kita perlu menghitung rotasi efektif
    k = k % N  # Menghitung rotasi efektif
    return arr[-k:] + arr[:-k]

# Input
N, k = map(int, input().strip().split())
arr = array.array('i', map(int, input().strip().split()))

# Melakukan rotasi dan mencetak hasil
rotated_arr = rotateArray(arr, N, k)
print(*rotated_arr)