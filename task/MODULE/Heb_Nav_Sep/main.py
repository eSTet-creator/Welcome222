# ============================================================
# MAIN — КОРИСТУВАЦЬКИЙ ІНТЕРФЕЙС
# ============================================================

import storage

from logic import (
    find_resources_by_keyword,
    find_resources_by_category,
    add_resource
)


# ------------------------------------------------------------
# ПЕРЕГЛЯД УСІХ РЕСУРСІВ
# ------------------------------------------------------------

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


# ------------------------------------------------------------
# ПОШУК ЗА КЛЮЧОВИМ СЛОВОМ
# ------------------------------------------------------------

def search_resource(resources):

    keyword = input(
        "\nВведіть ключове слово: "
    ).strip()

    if not keyword:
        print("Ключове слово не може бути порожнім.")
        return

    found = find_resources_by_keyword(
        resources,
        keyword
    )

    if found:

        print("\n--- ЗНАЙДЕНІ РЕСУРСИ ---")

        for resource in found:

            print(f"\nНазва: {resource['name']}")
            print(f"Категорія: {resource['category']}")
            print(f"Опис: {resource['description']}")
            print(f"Контакт: {resource['contact']}")
            print(f"Посилання: {resource['link']}")

    else:

        print(
            "\nЗа цим ключовим словом "
            "ресурсів не знайдено."
        )


# ------------------------------------------------------------
# ПОШУК ЗА КАТЕГОРІЄЮ
# ------------------------------------------------------------

def show_category(resources):

    category = input(
        "\nВведіть категорію: "
    ).strip()

    found = find_resources_by_category(
        resources,
        category
    )

    if found:

        print("\n--- РЕСУРСИ КАТЕГОРІЇ ---")

        for resource in found:

            print(f"\nНазва: {resource['name']}")
            print(f"Опис: {resource['description']}")
            print(f"Контакт: {resource['contact']}")

    else:

        print("\nТакої категорії не знайдено.")


# ------------------------------------------------------------
# ДОДАВАННЯ НОВОГО РЕСУРСУ
# ------------------------------------------------------------

def add_new_resource(resources):

    print("\n--- ДОДАВАННЯ НОВОГО РЕСУРСУ ---")

    name = input("Назва ресурсу: ").strip()
    category = input("Категорія: ").strip()
    description = input("Опис: ").strip()
    contact = input("Контакт: ").strip()
    link = input("Посилання: ").strip()

    result = add_resource(
        resources,
        name,
        category,
        description,
        contact,
        link
    )

    if not result:

        print(
            "\nНазва, категорія та опис "
            "є обов'язковими."
        )

        return

    # Після зміни даних зберігаємо їх.
    storage.save_resources(resources)

    print(
        "\nРесурс успішно додано "
        "та збережено у resources.csv."
    )


# ------------------------------------------------------------
# КОНТАКТИ
# ------------------------------------------------------------

def show_contacts():

    print("\n--- КОНТАКТИ ---")
    print("Email: itacademyfororphans@gmail.com")
    print("Телефон: +380667855460")
    print("Телефон: +380684042276")
    print("Сайт: https://hebron-academy.com")


# ------------------------------------------------------------
# ІНФОРМАЦІЯ ПРО НАВЧАННЯ
# ------------------------------------------------------------

def show_study():

    print("\n--- НАВЧАННЯ ---")

    print(
        "Hebron IT Academy допомагає студентам "
        "розвиватися в IT та інших важливих сферах."
    )

    print("\nОсновні напрями:")
    print("- програмування")
    print("- англійська мова")
    print("- тайм-менеджмент")
    print("- психологічна підтримка")
    print("- фізичний розвиток")
    print("- практична підготовка")

    print("\nОфіційний сайт:")
    print("https://hebron-academy.com")


# ------------------------------------------------------------
# КОРИСНЕ ПОСИЛАННЯ
# ------------------------------------------------------------

def show_link():

    print("\n--- КОРИСНЕ ПОСИЛАННЯ ---")
    print("Офіційний сайт Hebron IT Academy:")
    print("https://hebron-academy.com")


# ------------------------------------------------------------
# ГОЛОВНЕ МЕНЮ
# ------------------------------------------------------------

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


# ------------------------------------------------------------
# ГОЛОВНА ФУНКЦІЯ
# ------------------------------------------------------------

def main():

    # Завантажуємо дані через storage.
    resources = storage.load_resources()

    while True:

        show_menu()

        choice = input(
            "\nВаш вибір: "
        ).strip()

        if choice == "1":

            show_all_resources(resources)

        elif choice == "2":

            search_resource(resources)

        elif choice == "3":

            show_category(resources)

        elif choice == "4":

            add_new_resource(resources)

        elif choice == "5":

            show_contacts()

        elif choice == "6":

            show_study()

        elif choice == "7":

            show_link()

        elif choice == "8":

            print(
                "\nДякуємо за використання Навігатора!"
            )

            break

        else:

            print(
                "\nПомилка! "
                "Виберіть пункт від 1 до 8."
            )


# ------------------------------------------------------------
# ТОЧКА ВХОДУ
# ------------------------------------------------------------

if __name__ == "__main__":
    main()