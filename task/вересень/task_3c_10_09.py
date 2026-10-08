
n = int(input("Введіть n: "))

for riadok in range(1, n + 1):
    print("")
    i = n - riadok
    for probil in range(i):
        print(" ", end="")
    j = riadok * 2 - 1
    for zirochka in range(j):
        print("*", end="")