# ============================================================
# Модуль 4: Навігатор Ресурсів Академії
# IT Академія Hebron (hebron-academy.com)
# ============================================================

import csv
import os

FILENAME = "resources.csv"

DEFAULT_RESOURCES = [
    {
        "id": 1,
        "title": "Адміністрація Академії",
        "category": "контакти",
        "description": "Звертайтеся з організаційними питаннями, документами та загальними справами.",
        "contact": "+380 98 119 17 61 / +380 50 820 23 19",
        "location": "вул. Бірківська, 11, смт Брюховичі (головна будівля)",
        "link": "https://hebron-academy.com/",
        "keywords": "адміністрація директор контакти телефон"
    },
    {
        "id": 2,
        "title": "Електронна пошта Академії",
        "category": "контакти",
        "description": "Офіційна електронна адреса для листів та заявок.",
        "contact": "itacademyfororphans@gmail.com",
        "location": "-",
        "link": "https://hebron-academy.com/",
        "keywords": "email пошта лист"
    },
    {
        "id": 3,
        "title": "Основні правила проживання",
        "category": "правила",
        "description": "Заборонено: палити, вживати алкоголь, солодкі газовані напої та шоколад (крім чорного), фастфуд на території, заводити романтичні стосунки під час навчання.",
        "contact": "-",
        "location": "вся територія Академії",
        "link": "-",
        "keywords": "правила палити алкоголь стосунки харчування"
    },
    {
        "id": 4,
        "title": "Адреса Академії",
        "category": "місця",
        "description": "Фізична адреса навчального закладу та гуртожитку.",
        "contact": "-",
        "location": "79491, Львівська обл., смт Брюховичі, вул. Бірківська, 11",
        "link": "https://hebron-academy.com/",
        "keywords": "адреса де знаходиться як дістатися"
    },
    {
        "id": 5,
        "title": "Навчальні напрямки",
        "category": "навчальні матеріали",
        "description": "Основні напрямки: програмування (HTML, CSS, JS, Python), тестування, дизайн, проєктний менеджмент, англійська мова, математика.",
        "contact": "-",
        "location": "навчальні класи",
        "link": "https://hebron-academy.com/en/study/",
        "keywords": "навчання програмування курси python javascript"
    },
    {
        "id": 6,
        "title": "Офіційний сайт",
        "category": "корисні посилання",
        "description": "Сайт Академії з інформацією про програму, новини та можливість подати заявку.",
        "contact": "-",
        "location": "-",
        "link": "https://hebron-academy.com/",
        "keywords": "сайт hebron academy"
    },
    {
        "id": 7,
        "title": "Facebook сторінка",
        "category": "корисні посилання",
        "description": "Офіційна сторінка в Facebook з новинами та оголошеннями.",
        "contact": "-",
        "location": "-",
        "link": "https://www.facebook.com/IT.Academy.Hebron/",
        "keywords": "facebook соцмережі новини"
    },
    {
        "id": 8,
        "title": "Психологічна / духовна підтримка",
        "category": "допомога",
        "description": "В Академії є ментальна та духовна підтримка, бесіди з менторами, волонтерство та спільнота.",
        "contact": "зверніться до адміністрації або ментора",
        "location": "територія Академії",
        "link": "-",
        "keywords": "психолог допомога ментор підтримка"
    },
    {
        "id": 9,
        "title": "Стажування та працевлаштування",
        "category": "допомога",
        "description": "Академія допомагає з практикою та працевлаштуванням у IT-компаніях (у тому числі через HebronSoft).",
        "contact": "адміністрація / ментори",
        "location": "-",
        "link": "https://hebron-academy.com/",
        "keywords": "стажування робота працевлаштування hebronsoft"
    },
    {
        "id": 10,
        "title": "Спорт та фізичний розвиток",
        "category": "місця",
        "description": "В Академії є спортивний майданчик і спортзал. Також проводяться заняття з Brazilian Jiu-Jitsu та інші фізичні активності.",
        "contact": "зверніться до адміністрації або ментора",
        "location": "спортивний майданчик / спортзал на території Академії",
        "link": "https://hebron-academy.com/en/brazilian-jiu-jitsu-at-hebron-it-academy/",
        "keywords": "спорт спортзал майданчик jiu-jitsu фізичний розвиток тренування"
    },
    {
        "id": 11,
        "title": "Кухня та харчування",
        "category": "місця",
        "description": "В Академії забезпечується харчування студентів. Є кухня та їдальня.",
        "contact": "зверніться до адміністрації",
        "location": "кухня / їдальня на території Академії",
        "link": "-",
        "keywords": "кухня харчування їжа їдальня"
    },
    {
        "id": 12,
        "title": "Медична допомога",
        "category": "допомога",
        "description": "Академія забезпечує студентів медичною підтримкою. При потребі звертайтеся до адміністрації.",
        "contact": "адміністрація Академії",
        "location": "територія Академії",
        "link": "-",
        "keywords": "медицина медпункт лікар здоров'я"
    },
    {
        "id": 13,
        "title": "Технічна підтримка / Wi-Fi",
        "category": "допомога",
        "description": "Питання щодо інтернету, ноутбуків та технічних проблем можна вирішити через адміністрацію або менторів.",
        "contact": "адміністрація / ментори",
        "location": "-",
        "link": "-",
        "keywords": "wifi інтернет техніка ноутбук підтримка"
    }
]


def load_resources():
    """Завантажує ресурси з CSV-файлу. Якщо файлу немає — створює його з початковими даними."""
    if not os.path.exists(FILENAME):
        save_resources(DEFAULT_RESOURCES)
        return [r.copy() for r in DEFAULT_RESOURCES]

    resources = []
    with open(FILENAME, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["id"] = int(row["id"])
            resources.append(row)
    return resources


def save_resources(resources):
    """Зберігає весь список ресурсів у CSV-файл"""
    fieldnames = ["id", "title", "category", "description", "contact", "location", "link", "keywords"]
    with open(FILENAME, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(resources)


def show_menu():
    print("\n" + "=" * 50)
    print("  НАВІГАТОР РЕСУРСІВ АКАДЕМІЇ HEBRON")
    print("=" * 50)
    print("1. Показати всі ресурси")
    print("2. Пошук за ключовим словом")
    print("3. Фільтр за категорією")
    print("4. Показати деталі ресурсу")
    print("5. Додати новий ресурс")
    print("0. Вийти")
    print("=" * 50)


def show_all(resources):
    print("\n--- Усі ресурси ---")
    for r in resources:
        print(f"{r['id']}. [{r['category']}] {r['title']}")


def search(resources):
    keyword = input("Введіть ключове слово: ").strip().lower()
    if not keyword:
        print("Ключове слово не може бути порожнім.")
        return

    found = []
    for r in resources:
        text = f"{r['title']} {r['description']} {r['category']} {r['keywords']}".lower()
        if keyword in text:
            found.append(r)

    if not found:
        print("Нічого не знайдено.")
    else:
        print(f"\nЗнайдено {len(found)} ресурс(ів):")
        for r in found:
            print(f"{r['id']}. [{r['category']}] {r['title']}")


def filter_by_category(resources):
    categories = sorted(set(r["category"] for r in resources))
    print("\nДоступні категорії:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")

    try:
        choice = int(input("Виберіть номер категорії: "))
        if 1 <= choice <= len(categories):
            selected = categories[choice - 1]
            print(f"\n--- Категорія: {selected} ---")
            for r in resources:
                if r["category"] == selected:
                    print(f"{r['id']}. {r['title']}")
        else:
            print("Невірний номер.")
    except ValueError:
        print("Введіть число.")


def show_details(resources):
    try:
        num = int(input("Введіть номер ресурсу: "))
        for r in resources:
            if r["id"] == num:
                print("\n" + "-" * 40)
                print(f"Назва:        {r['title']}")
                print(f"Категорія:    {r['category']}")
                print(f"Опис:         {r['description']}")
                print(f"Контакт:      {r['contact']}")
                print(f"Локація:      {r['location']}")
                print(f"Посилання:    {r['link']}")
                print("-" * 40)
                return
        print("Ресурс з таким номером не знайдено.")
    except ValueError:
        print("Введіть число.")


def add_resource(resources):
    print("\n--- Додавання нового ресурсу ---")
    title = input("Назва: ").strip()
    category = input("Категорія: ").strip()
    description = input("Опис: ").strip()
    contact = input("Контакт (або -): ").strip() or "-"
    location = input("Локація (або -): ").strip() or "-"
    link = input("Посилання (або -): ").strip() or "-"
    keywords = input("Ключові слова: ").strip()

    if not title or not category or not description:
        print("Назва, категорія та опис обов’язкові!")
        return

    new_id = max((r["id"] for r in resources), default=0) + 1
    resources.append({
        "id": new_id,
        "title": title,
        "category": category,
        "description": description,
        "contact": contact,
        "location": location,
        "link": link,
        "keywords": keywords
    })
    save_resources(resources)
    print(f"Ресурс «{title}» додано і збережено (id={new_id}).")


def main():
    resources = load_resources()
    print(f"Завантажено {len(resources)} ресурсів з файлу «{FILENAME}»")

    while True:
        show_menu()
        choice = input("Ваш вибір: ").strip()

        if choice == "1":
            show_all(resources)
        elif choice == "2":
            search(resources)
        elif choice == "3":
            filter_by_category(resources)
        elif choice == "4":
            show_details(resources)
        elif choice == "5":
            add_resource(resources)
        elif choice == "0":
            save_resources(resources)
            print("Дані збережено. До побачення! Успіхів у навчанні в Hebron Academy.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()