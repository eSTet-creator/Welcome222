n = int(input("Введіть n: "))
sum = 0.00
for i in range(1, n + 1):
    sum = sum + i / (i + 1)
print(f"{sum =:.2f}")
