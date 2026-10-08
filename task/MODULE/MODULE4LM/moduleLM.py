import csv
import os

# Назва файла для зберігання бази знань
DATA_FILE = "hebron_resources.csv"

# Початкові дані Hebron IT Academy (якщо файл ще не створено)
INITIAL_RESOURCES = [
    {
        "id": "1",
        "category": "Контакти",
        "title": "Академічний відділ / Куратори",
        "description": "Питання розкладу, відвідуваності, навчального прогресу та менторів.",
        "location_or_link": "Кабінет 201 / Telegram: @hebron_study",
        "tags": "куратор, навчання, розклад, довідка, ментор"
    },
    {
        "id": "2",
        "category": "Побут",
        "title": "Правила проживання в кампусі",
        "description": "Регламент чергування, тихий час, правила користування кухнею та пральнею.",
        "location_or_link": "Інфо-дошка в холі / hebron-academy.com/rules",
        "tags": "побут, гуртожиток, чергування, правила, тиша"
    },
    {
        "id": "3",
        "category": "Навчання",
        "title": "Локальний сервер матеріалів та GitLab",
        "description": "Доступ до репозиторіїв з домашніми завданнями, ЛМС та конспектами.",
        "location_or_link": "https://gitlab.hebron-academy.com",
        "tags": "код, git, lms, матеріали, домашка, python"
    },
    {
        "id": "4",
        "category": "Техніка",
        "title": "Мережевий принтер та IT-підтримка",
        "description": "Друк навчальних матеріалів. Звернення при поломці ноутбуків.",
        "location_or_link": "IP: 192.168.1.100 / Telegram: @hebron_it_support",
        "tags": "принтер, друк, ноутбук, wifi, техніка, ремонт"
    },
    {
        "id": "5",
        "category": "Допомога",
        "title": "Психологічна служба та соціальний ментор",
        "description": "Особисті консультації, підтримка в адаптації, вирішення конфліктів.",
        "location_or_link": "Кабінет психолога (2 поверх) / Telegram: @hebron_support",
        "tags": "допомога, адаптація, психолог, розмова, соціальний"
    }
]

FIELDNAMES = ["id", "category", "title", "description", "location_or_link", "tags"]


def init_storage():
    """Створює CSV файл із базовими даними, якщо він відсутній."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode="w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(INITIAL_RESOURCES)


def load_resources():
    """Завантажує ресурси з CSV файла."""
    resources = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                resources.append(row)
    return resources


def save_resources(resources):
    """Зберігає список ресурсів у CSV файл."""
    with open(DATA_FILE, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(resources)


def print_resource_card(res):
    """Красиво форматує картку одного ресурсу."""
    print("─" * 60)
    print(f"📌 [{res['id']}] {res['title'].upper()} ({res['category']})")
    print(f"ℹ️  Опис: {res['description']}")
    print(f"📍 Локація / Контакт: {res['location_or_link']}")
    print(f"🏷️  Теги: {res['tags']}")
    print("─" * 60)


def display_all(resources):
    """Виводить всі наявні ресурси."""
    if not resources:
        print("\n[!] База даних порожня.")
        return
    print(f"\n=== СПИСОК ВСІХ РЕСУРСІВ HEBRON ACADEMY ({len(resources)}) ===")
    for res in resources:
        print_resource_card(res)


def search_resources(resources):
    """Пошук за ключовим словом у назві, описі або тегах."""
    query = input("\nВведіть пошуковий запит (наприклад: 'принтер', 'git', 'правила'): ").strip().lower()
    if not query:
        print("[!] Порожній запит.")
        return

    results = [
        r for r in resources
        if query in r['title'].lower()
           or query in r['description'].lower()
           or query in r['tags'].lower()
    ]

    print(f"\n=== ЗНАЙДЕНО РЕСУРСІВ ЗА ЗАПИТОМ '{query}': {len(results)} ===")
    if results:
        for res in results:
            print_resource_card(res)
    else:
        print("За вашим запитом нічого не знайдено. Зверніться до адміністратора Hebron Academy.")


def filter_by_category(resources):
    """Фільтрація ресурсів за обраною категорією."""
    categories = sorted(list(set(r['category'] for r in resources)))
    print("\nДоступні категорії:")
    for idx, cat in enumerate(categories, 1):
        print(f" {idx}. {cat}")

    choice = input("Оберіть номер категорії: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(categories):
        selected_cat = categories[int(choice) - 1]
        results = [r for r in resources if r['category'] == selected_cat]
        print(f"\n=== КАТЕГОРІЯ: {selected_cat} ({len(results)}) ===")
        for res in results:
            print_resource_card(res)
    else:
        print("[!] Некоректна категорія.")


def add_new_resource(resources):
    """Додавання нового ресурсу з автозбереженням."""
    print("\n=== ДОДАВАННЯ НОВОГО РЕСУРСУ HEBRON ===")
    title = input("Назва ресурсу / посади: ").strip()
    category = input("Категорія (Навчання/Побут/Контакти/Техніка/Допомога): ").strip().capitalize()
    description = input("Короткий опис: ").strip()
    location_or_link = input("Локація, посилання або контакний Telegram: ").strip()
    tags = input("Теги через кому (наприклад: python, домашка, ментор): ").strip().lower()

    if not title or not category or not location_or_link:
        print("\n[ПОМИЛКА] Назва, категорія та локація є обов'язковими полями!")
        return

    # Генерація унікального ID
    new_id = str(max([int(r['id']) for r in resources], default=0) + 1)

    new_res = {
        "id": new_id,
        "category": category,
        "title": title,
        "description": description,
        "location_or_link": location_or_link,
        "tags": tags
    }

    resources.append(new_res)
    save_resources(resources)
    print(f"\n[УСПІХ] Ресурс '{title}' додано та збережено!")


def main():
    init_storage()
    resources = load_resources()

    while True:
        print("\n" + "=" * 50)
        print(" 🏛️  НАВІГАТОР РЕСУРСІВ IT АКАДЕМІЇ HEBRON  🏛️ ")
        print("=" * 50)
        print("1. Переглянути всі ресурси")
        print("2. Швидкий пошук за тегом або словом")
        print("3. Показати ресурси за категорією")
        print("4. Додати новий ресурс (Адмін/Ментор)")
        print("0. Вийти з системи")
        print("=" * 50)

        choice = input("Оберіть дію (0-4): ").strip()

        if choice == "1":
            display_all(resources)
        elif choice == "2":
            search_resources(resources)
        elif choice == "3":
            filter_by_category(resources)
        elif choice == "4":
            add_new_resource(resources)
        elif choice == "0":
            print("\nДякуємо за користування Навігатором Hebron Academy! Успіхів у навчанні! 🚀")
            break
        else:
            print("\n[!] Невірний вибір. Введіть цифру від 0 до 4.")


if __name__ == "__main__":
    main()