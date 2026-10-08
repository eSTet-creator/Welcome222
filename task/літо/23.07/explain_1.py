# =============================================
# Задача: Аналіз витрат за тиждень
# =============================================

# Вхідні дані - список витрат
# Кожен елемент - це словник з категорією та сумою
expenses = [
    {"category": "їжа", "amount": 250},
    {"category": "транспорт", "amount": 80},
    {"category": "їжа", "amount": 170},
    {"category": "розваги", "amount": 300},
    {"category": "транспорт", "amount": 120},
    {"category": "навчання", "amount": 500}
]


def calculate_total_expenses(expenses):
    """Підраховує загальну суму всіх витрат"""

    # Ініціалізуємо змінну для накопичення суми
    total = 0

    # Перебираємо кожну витрату в списку
    for expense in expenses:
        # Додаємо суму поточної витрати до загальної
        # += означає: total = total + expense["amount"]
        total += expense["amount"]

    # Повертаємо результат
    return total


def group_expenses_by_category(expenses):
    """Групує витрати за категоріями"""

    # Імпортуємо defaultdict - спеціальний словник,
    # який автоматично створює значення 0 для нового ключа
    from collections import defaultdict

    # Створюємо порожній "розумний" словник
    categories = defaultdict(int)

    # Перебираємо всі витрати
    for expense in expenses:
        # Додаємо суму до відповідної категорії
        # Якщо категорії ще немає - defaultdict автоматично поставить 0
        categories[expense["category"]] += expense["amount"]

    # Перетворюємо defaultdict у звичайний dict і повертаємо
    return dict(categories)


def find_max_category(categories):
    """Знаходить категорію з найбільшою сумою витрат"""

    # Якщо словник порожній - повертаємо None і 0
    if not categories:
        return None, 0

    # Знаходимо категорію з максимальною сумою
    # key=categories.get означає: порівнювати не ключі, а їх значення
    max_category = max(categories, key=categories.get)

    # Отримуємо суму для цієї категорії
    max_amount = categories[max_category]

    # Повертаємо дві речі: назву категорії та її суму
    return max_category, max_amount


def generate_report(expenses):
    """Генерує повний текстовий звіт"""

    # Захист: якщо список витрат порожній
    if not expenses:
        return "Немає даних про витрати."

    # Викликаємо інші функції для отримання даних
    total = calculate_total_expenses(expenses)
    categories = group_expenses_by_category(expenses)
    max_category, max_amount = find_max_category(categories)

    # Починаємо формувати текстовий звіт
    report = f"Загальні витрати: {total} грн\n"
    report += f"Найбільше витрачено на категорію: {max_category} ({max_amount} грн)\n\n"
    report += "Витрати по категоріях:\n"

    # Сортуємо категорії за сумою (від більшої до меншої)
    # sorted() з reverse=True = за спаданням
    # key=lambda x: x[1] - сортуємо за другим елементом пари (сума)
    for category, amount in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        # Додаємо кожен рядок до звіту
        # • - це маркер (bullet point) для краси
        report += f"  • {category}: {amount} грн\n"

    # Повертаємо готовий текстовий звіт
    return report


# ======================
# Запуск програми
# ======================

# Викликаємо головну функцію і зберігаємо результат
result = generate_report(expenses)

# Виводимо результат на екран
print(result)