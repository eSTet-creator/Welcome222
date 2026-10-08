#Дано дійсне додатне число a і ціле число n , яке може набувати додатних і відʼємних значень. Напишіть
#функцію для обчислення a в ступені n. Стандартною функцією піднесення до степеня і оператором **
#користуватися не можна.
#Вхідні дані:
#2
#1
#2
#- 1
#Вихідні дані:
#2.0
#0.5
def power(a, n):
    if n == 0:
        return 1

    result = 1

    if n > 0:
        for i in range(n):
            result *= a
    else:
        for i in range(-n):
            result *= a
        result = 1 / result

    return result


while True:
    a = float(input("Введіть число a: "))
    n = int(input("Введіть степінь n: "))

    result = power(a, n)

    print(result)

    answer = input("Продовжити? (так/ні): ")

    if answer.lower() != "так":
        break