# ============================================================
# STORAGE — ЗБЕРЕЖЕННЯ ДАНИХ
# ============================================================

import csv
import os


# Назва CSV-файлу
FILE_NAME = "resources.csv"


# ------------------------------------------------------------
# ПОЧАТКОВІ ДАНІ
# ------------------------------------------------------------

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


# ------------------------------------------------------------
# ЗАВАНТАЖЕННЯ РЕСУРСІВ
# ------------------------------------------------------------

def load_resources():

    # Якщо файлу немає, створюємо його
    # з початковими даними.
    if not os.path.exists(FILE_NAME):
        save_resources(default_resources)
        return default_resources.copy()

    resources = []

    with open(
        FILE_NAME,
        "r",
        encoding="utf-8-sig",
        newline=""
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            resources.append(row)

    return resources


# ------------------------------------------------------------
# ЗБЕРЕЖЕННЯ РЕСУРСІВ
# ------------------------------------------------------------

def save_resources(resources):

    fields = [
        "name",
        "category",
        "description",
        "contact",
        "link"
    ]

    with open(
        FILE_NAME,
        "w",
        encoding="utf-8-sig",
        newline=""
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fields
        )

        writer.writeheader()
        writer.writerows(resources)