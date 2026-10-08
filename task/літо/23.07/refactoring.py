# Програма для системи перевірки відвідувачів кінотеатру.
# Ціна на квитки залежить від віку відвідувача:
# До 12 років: 80 грн
# Від 12 до 17 років: 120 грн
# Від 18 років і старше: 160 грн
# Додатково відвідувач може обрати попкорн за 70 грн.
# Правила допуску:
# Якщо у відвідувача немає квитка, система має повернути: "Потрібно купити квиток".
# Якщо баланс коштів відвідувача менший за загальну вартість (квиток + попкорн), система повертає:
# "Недостатньо коштів".
# Діти до 6 років не можуть проходити самі, тому для них система повертає:
# "Дитина може пройти тільки з дорослим".
# Якщо всі умови виконано, система повертає повідомлення про успішний вхід із вказанням загальної вартості
# та відміткою про попкорн (якщо його було замовлено).


def get_ticket_price(age):
    if age < 12:
        return 80
    elif age < 18:
        return 120
    else:
        return 160


def get_total_price(ticket_price, wants_popcorn):
    if wants_popcorn:
        return ticket_price + 70
    return ticket_price


def check_ticket(has_ticket):
    if not has_ticket:
        return "Потрібно купити квиток"
    return None


def check_balance(balance, total_price):
    if balance < total_price:
        return "Недостатньо коштів"
    return None


def check_age(age):
    if age < 6:
        return "Дитина може пройти тільки з дорослим"
    return None


def create_message(total_price, wants_popcorn):
    message = f"Вхід дозволено. Вартість: {total_price} грн"

    if wants_popcorn:
        message += ". Попкорн додано"

    return message


def check_movie_session(age, has_ticket, balance, wants_popcorn):
    ticket_price = get_ticket_price(age)
    total_price = get_total_price(ticket_price, wants_popcorn)

    result = check_ticket(has_ticket)
    if result:
        return result

    result = check_balance(balance, total_price)
    if result:
        return result

    result = check_age(age)
    if result:
        return result

    return create_message(total_price, wants_popcorn)


while True:
    age = int(input("Введіть вік: "))

    has_ticket = input("Чи є квиток? (так/ні): ").lower() == "так"

    balance = float(input("Введіть суму грошей: "))

    wants_popcorn = input("Хочете попкорн? (так/ні): ").lower() == "так"

    print(check_movie_session(age, has_ticket, balance, wants_popcorn))

    again = input("Перевірити ще одного відвідувача? (так/ні): ").lower()

    if again != "так":
        print("Програму завершено.")
        break

