def triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


while True:
    a, b, c = map(int, input("Введіть три числа через пробіл: ").split())
    print(triangle(a, b, c))

    answer = input("Продовжити? (так/ні): ")
    if answer == "ні":
        break


