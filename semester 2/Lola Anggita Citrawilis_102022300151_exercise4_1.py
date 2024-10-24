import array as a

N = int(input())
queue = a.array('d')

for i in range(N):
    # Height = map( int, input().split())
    Height = float(input())
    queue.append(Height)

sorted_queue = sorted(queue)
queue_length = len(sorted_queue)

if N % 2 == 1:
    mid = sorted_queue[queue_length // 2]

else:
    left = sorted_queue[queue_length // 2 - 1]
    right = sorted_queue[queue_length // 2]
    mid = min(left, right) 

print("Antrian:\t", queue[:], end=" ")
print("Nilai tengah:\t", mid)