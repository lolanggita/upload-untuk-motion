while True:
    print("    Eksplorasi 1    ")
    print("=====================")
    N = list(map(int, input().strip().split()))     # Menginput nilai ke dalam list dengan jeda spasi

    def sorted():
        N.sort()
        print("Hasil Sort: " + str(N) + "\n")

    def copy():
        copy = N.copy()
        print("Hasil Copy: ", copy)

    def joins():
        separator = "% ".join(map(str, N))
        print("Hasil Join: " + str(separator) + "\n")

    def reversed():
        N.reverse()
        print("Hasil Reverse: " + str(N) + "\n")

    def counting():
        S = int(input("Frekuensi angka yang ingin dihitung: "))
        Result = N.count(S)
        print("Hasil Count: " + str(Result) + "\n")

    def extendind():
        S = ["jagung, apel, pisang"]
        N.extend(S)
        print("Hasil Extend: ", N )
        print("Hasil Index: "+ str(N[2:6]) + "\n")


    print("=====================")
    print("|| 1. sort" + " ||".rjust(11))
    print("|| 2. copy" + " ||".rjust(11))
    print("|| 3. join" + " ||".rjust(11))
    print("|| 4. reverse" + " ||".rjust(8))
    print("|| 5. count" + " ||".rjust(10))
    print("|| 6. Extend" + " ||".rjust(9))
    print("=====================")
    i = input("=> ")

    if i == "1" :
        sorted()

    elif i == "2" :
        copy()

    elif i == "3" :
        joins()

    elif i == "4" :
        reversed()

    elif i == "5" :
        counting()

    elif i == "6" :
        extendind()