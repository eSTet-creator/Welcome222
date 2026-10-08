

n = int(input("Введіть n: "))

for riadok in range(1, n + 1):
    print("")

    for probil in range(n - riadok):
        print(" ", end="")

    for zirochka in range(riadok * 2 - 1):
        print("*", end="")
