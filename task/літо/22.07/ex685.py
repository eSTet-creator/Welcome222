def calculate_cart_total(cart):
    """Підраховує загальну суму кошика"""
    total = 0
    for item in cart:
        total += item["price"] * item["quantity"]
    return total


def find_expensive_items(cart):
    """Знаходить назви дорогих товарів (вартість > 1000 грн)"""
    expensive = []
    for item in cart:
        item_total = item["price"] * item["quantity"]
        if item_total > 1000:
            expensive.append(item["name"])
    return expensive


def calculate_discount(total):
    """Розраховує знижку 10% при сумі від 3000 грн"""
    if total >= 3000:
        return total * 0.1
    return 0


def create_report_message(customer_name, total, final_total, expensive_items, has_discount):
    """Створює текст звіту для клієнта"""
    if has_discount:
        message = f"{customer_name}, ви отримали знижку 10%.\n"
    else:
        message = f"{customer_name}, знижка недоступна.\n"

    message += f"Сума замовлення: {total} грн\n"
    message += f"До сплати: {final_total} грн\n"

    if expensive_items:
        message += "Дорогі товари в кошику: " + ", ".join(expensive_items)

    return message


def analyze_customer_cart(customer_name, cart):
    """Головна функція аналізу кошика (організує роботу)"""
    total = calculate_cart_total(cart)
    expensive_items = find_expensive_items(cart)
    discount = calculate_discount(total)
    final_total = total - discount
    has_discount = discount > 0

    return create_report_message(
        customer_name,
        total,
        final_total,
        expensive_items,
        has_discount
    )
