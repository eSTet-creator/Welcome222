def maximum(a, b, c):
    return max(a, b, c)
while True:
    a, b, c = map(int, input("Введіть три числа через пробіл: ").split())
    print(maximum(a, b, c))

    answer = input("Продовжити? (так/ні): ")
    if answer == "ні":
        break

