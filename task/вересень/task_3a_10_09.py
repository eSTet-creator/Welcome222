n = int(input("Введіть n: "))

for riadok in range(1, n + 1):
    print(" " * (n - riadok) + "*" * (2 * riadok - 1))