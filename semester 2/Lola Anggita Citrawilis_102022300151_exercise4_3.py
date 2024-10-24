import array as a

N = int(input())
Frequence = a.array('d', [0]*101)
for i in range(N):
    S = float(input())
    Frequence.append(S)

print(Frequence)
