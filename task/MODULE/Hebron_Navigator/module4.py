import csv
import os


FILE_NAME = "resources.csv"


default_resources = [
    {
        "name": "Навчання",
        "category": "Освіта",
        "description": "Інформація про навчальні програми Hebron IT Academy",
        "contact": "Адміністрація академії",
        "link": "https://hebron-academy.com"
    },
    {
        "name": "Програмування",
        "category": "Освіта",
        "description": "Навчання програмуванню та сучасним IT-технологіям",
        "contact": "Викладачі академії",
        "link": "https://hebron-academy.com"
    },
    {
        "name": "Англійська мова",
        "category": "Розвиток",
        "description": "Навчання англійської мови",
        "contact": "Викладач англійської",
        "link": "https://hebron-academy.com"
    },
    {
        "name": "Психологічна підтримка",
        "category": "Підтримка",
        "description": "Психологічна підтримка студентів",
        "contact": "Наставник або відповідальний працівник",
        "link": "https://hebron-academy.com"
    },
    {
        "name": "Проживання",
        "category": "Побут",
        "description": "Забезпечення студентів житлом",
        "contact": "Адміністрація академії",
        "link": "https://hebron-academy.com"
    },
    {
        "name": "Харчування",
        "category": "Побут",
        "description": "Забезпечення студентів харчуванням",
        "contact": "Адміністрація академії",
        "link": "https://hebron-academy.com"
    },
    {
        "name": "Спорт",
        "category": "Фізичний розвиток",
        "description": "Футбол, бразильське джиу-джитсу та інші активності",
        "contact": "Відповідальний за спортивні активності",
        "link": "https://hebron-academy.com"
    },
    {
        "name": "Практика",
        "category": "Кар'єра",
        "description": "Можливість отримати практичний досвід",
        "contact": "Кар'єрний координатор",
        "link": "https://hebron-academy.com"
    },
    {
        "name": "Працевлаштування",
        "category": "Кар'єра",
        "description": "Підтримка студентів у професійному розвитку",
        "contact": "Кар'єрний координатор",
        "link": "https://hebron-academy.com"
    },
    {
        "name": "Офіційний сайт",
        "category": "Інтернет",
        "description": "Офіційний вебсайт Hebron IT Academy",
        "contact": "Hebron IT Academy",
        "link": "https://hebron-academy.com"
    }
]


def load_resources():
    if not os.path.exists(FILE_NAME):
        save_resources(default_resources)
        return default_resources.copy()

    resources = []

    with open(FILE_NAME, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            resources.append(row)

    return resources


def save_resources(resources):
    fields = ["name", "category", "description", "contact", "link"]

    with open(FILE_NAME, "w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)

        writer.writeheader()
        writer.writerows(resources)


def show_all_resources(resources):
    print("\n--- ВСІ РЕСУРСИ ---")

    if not resources:
        print("Ресурсів немає.")
        return

    for i, resource in enumerate(resources, 1):
        print(f"\n{i}. {resource['name']}")
        print(f"   Категорія: {resource['category']}")
        print(f"   Опис: {resource['description']}")
        print(f"   Контакт: {resource['contact']}")
        print(f"   Посилання: {resource['link']}")


def find_resource_by_keyword(resources):
    keyword = input("\nВведіть ключове слово: ").lower().strip()

    if not keyword:
        print("Ключове слово не може бути порожнім.")
        return

    found = []

    for resource in resources:
        text = (
            resource["name"] + " " +
            resource["category"] + " " +
            resource["description"]
        ).lower()

        if keyword in text:
            found.append(resource)

    if found:
        print("\n--- ЗНАЙДЕНІ РЕСУРСИ ---")

        for resource in found:
            print(f"\nНазва: {resource['name']}")
            print(f"Категорія: {resource['category']}")
            print(f"Опис: {resource['description']}")
            print(f"Контакт: {resource['contact']}")
            print(f"Посилання: {resource['link']}")
    else:
        print("\nЗа цим ключовим словом ресурсів не знайдено.")


def show_category(resources):
    category = input("\nВведіть категорію: ").lower().strip()

    found = []

    for resource in resources:
        if resource["category"].lower() == category:
            found.append(resource)

    if found:
        print("\n--- РЕСУРСИ КАТЕГОРІЇ ---")

        for resource in found:
            print(f"\nНазва: {resource['name']}")
            print(f"Опис: {resource['description']}")
            print(f"Контакт: {resource['contact']}")
    else:
        print("\nТакої категорії не знайдено.")


def add_resource(resources):
    print("\n--- ДОДАВАННЯ НОВОГО РЕСУРСУ ---")

    name = input("Назва ресурсу: ").strip()
    category = input("Категорія: ").strip()
    description = input("Опис: ").strip()
    contact = input("Контакт: ").strip()
    link = input("Посилання: ").strip()

    if not name or not category or not description:
        print("\nНазва, категорія та опис є обов'язковими.")
        return

    new_resource = {
        "name": name,
        "category": category,
        "description": description,
        "contact": contact,
        "link": link
    }

    resources.append(new_resource)
    save_resources(resources)

    print("\nРесурс успішно додано та збережено у resources.csv.")


def show_contacts():
    print("\n--- КОНТАКТИ ---")
    print("Email: itacademyfororphans@gmail.com")
    print("Телефон: +380667855460")
    print("Телефон: +380684042276")
    print("Сайт: https://hebron-academy.com")


def show_study():
    print("\n--- НАВЧАННЯ ---")
    print("Hebron IT Academy допомагає студентам")
    print("розвиватися в IT та інших важливих сферах.")

    print("\nОсновні напрями:")
    print("- програмування")
    print("- англійська мова")
    print("- тайм-менеджмент")
    print("- психологічна підтримка")
    print("- фізичний розвиток")
    print("- практична підготовка")

    print("\nОфіційний сайт:")
    print("https://hebron-academy.com")


def show_link():
    print("\n--- КОРИСНЕ ПОСИЛАННЯ ---")
    print("Офіційний сайт Hebron IT Academy:")
    print("https://hebron-academy.com")


def show_menu():
    print("\n" + "=" * 50)
    print("      НАВІГАТОР РЕСУРСІВ HEBRON IT ACADEMY")
    print("=" * 50)
    print("1. Показати всі ресурси")
    print("2. Знайти ресурс за ключовим словом")
    print("3. Показати ресурси за категорією")
    print("4. Додати новий ресурс")
    print("5. Показати контакти")
    print("6. Показати інформацію про навчання")
    print("7. Показати корисне посилання")
    print("8. Вийти")


resources = load_resources()

while True:
    show_menu()

    choice = input("\nВаш вибір: ").strip()

    if choice == "1":
        show_all_resources(resources)

    elif choice == "2":
        find_resource_by_keyword(resources)

    elif choice == "3":
        show_category(resources)

    elif choice == "4":
        add_resource(resources)

    elif choice == "5":
        show_contacts()

    elif choice == "6":
        show_study()

    elif choice == "7":
        show_link()

    elif choice == "8":
        print("\nДякуємо за використання Навігатора!")
        break

    else:
        print("\nПомилка! Виберіть пункт від 1 до 8.")