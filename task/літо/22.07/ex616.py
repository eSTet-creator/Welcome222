def calc(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        return "Unknown operation"


a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
operation = input("Введіть операцію: ")

result = calc(a, b, operation)

if isinstance(result, float) or isinstance(result, int):
    print(f"{result:.2f}")
else:
    print(result)
