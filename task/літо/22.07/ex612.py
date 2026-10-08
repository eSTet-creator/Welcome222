def maximum(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "equal"

while True:
    a, b = map(int, input("Введіть два числа через пробіл: ").split())
    print(maximum(a, b))

    answer = input("Продовжити? (так/ні): ")
    if answer == "ні":
        break
