#Напишіть програму для аналізу кошика клієнта в інтернет-магазині:
#Обчислити загальну вартість усіх товарів у кошику.
#Визначити товари, вартість яких (ціна × кількість) перевищує 1000 грн.
#Якщо загальна сума замовлення 3000 грн або більше, надати клієнту знижку 10%.
#Обчислити суму, яку клієнт повинен сплатити після застосування знижки (якщо вона є).
#Сформувати та повернути текстове повідомлення для клієнта.
#Формат повідомлення:
 #Якщо є знижка:
  #Ім’я, ви отримали знижку 10%.
 #Якщо знижки немає:
  #Ім’я, знижка недоступна.
 #Повідомлення також повинно містити:
 #Загальну суму замовлення
 #Сума до сплати
 #Список дорогих товарів (якщо такі є)

# Функція для обчислення загальної вартості замовлення
def calculate_total(cart):
    total = 0
    for item in cart:
        total += item["price"] * item["quantity"]
    return total


# Функція для пошуку дорогих товарів (вартість понад 1000 грн)
def find_expensive_items(cart):
    expensive = []
    for item in cart:
        cost = item["price"] * item["quantity"]
        if cost > 1000:
            expensive.append(item["name"])
    return expensive


# Функція для визначення знижки
def calculate_discount(total):
    if total >= 3000:
        return total * 0.10
    return 0


# Функція для обчислення суми до сплати
def calculate_payment(total, discount):
    return total - discount


# Функція для формування повідомлення
def create_message(name, total, payment, expensive_items, discount):
    message = ""

    if discount > 0:
        message += f"{name}, ви отримали знижку 10%.\n"
    else:
        message += f"{name}, знижка недоступна.\n"

    message += f"Загальна сума замовлення: {total:.2f} грн\n"
    message += f"Сума до сплати: {payment:.2f} грн\n"

    if expensive_items:
        message += "Дорогі товари:\n"
        for item in expensive_items:
            message += f"- {item}\n"
    else:
        message += "Дорогих товарів немає."

    return message


# Головна функція
def main():
    name = input("Введіть ім'я клієнта: ")

    n = int(input("Введіть кількість товарів: "))

    cart = []

    for i in range(n):
        print(f"\nТовар {i + 1}")
        product_name = input("Назва товару: ")
        price = float(input("Ціна: "))
        quantity = int(input("Кількість: "))

        cart.append({
            "name": product_name,
            "price": price,
            "quantity": quantity
        })

    total = calculate_total(cart)
    expensive_items = find_expensive_items(cart)
    discount = calculate_discount(total)
    payment = calculate_payment(total, discount)

    result = create_message(name, total, payment, expensive_items, discount)

    print("\n--- Результат ---")
    print(result)


# Запуск програми
main()