# Задача: Аналіз витрат за тиждень
# Учень отримує список витрат за тиждень. Кожна витрата має категорію і суму. Потрібно написати програму, яка:
# 1. Рахує загальну суму витрат.
# 2. Знаходить категорію, на яку витрачено найбільше.
# 3. Формує короткий текстовий звіт.


# Вхідні дані (можна змінювати):
expenses = [
    {"category": "їжа", "amount": 250},
    {"category": "транспорт", "amount": 80},
    {"category": "їжа", "amount": 170},
    {"category": "розваги", "amount": 300},
    {"category": "транспорт", "amount": 120},
    {"category": "навчання", "amount": 500}
]
# Підраховуємо загальну суму всіх витрат
def calculate_total_expenses(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total

# Групуємо витрати за категоріями
def group_expenses_by_category(expenses):
    from collections import defaultdict
    categories = defaultdict(int)
    for expense in expenses:
        categories[expense["category"]] += expense["amount"]
    return dict(categories)

# Шукаємо категорію з найбільшою сумою
def find_max_category(categories):
    if not categories: # Захист
        return None, 0
    max_category = max(categories, key=categories.get)
    max_amount = categories[max_category]
    return max_category, max_amount

# Головна функція - генеруємо повний текстовий звіт
def generate_report(expenses):
    if not expenses: # Захист
        return "Немає даних про витрати."
    # Викликаємо інші функції для отриимання даних
    total = calculate_total_expenses(expenses)
    categories = group_expenses_by_category(expenses)
    max_category, max_amount = find_max_category(categories)
    # Формуємо тиекстовий звіт
    report = f"Загальні витрати: {total} грн\n"
    report += f"Найбільше витрачено на категорію: {max_category} ({max_amount})\n\n"
    report += f"Витрати по категоріях:\n"

    # Сортуємо категорії за сумою (від більшої до меншої)
    for category, amount in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        report += f" - {category}: {amount} грн\n"

    return report

# Виклик головної функції
result = generate_report(expenses)
print(result)





    



