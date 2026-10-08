# ============================================================
# LOGIC — БІЗНЕС-ЛОГІКА
# ============================================================

# ------------------------------------------------------------
# ПОШУК ЗА КЛЮЧОВИМ СЛОВОМ
# ------------------------------------------------------------

def find_resources_by_keyword(resources, keyword):

    keyword = keyword.lower().strip()

    if not keyword:
        return []

    found = []

    for resource in resources:

        text = (
            resource["name"] + " " +
            resource["category"] + " " +
            resource["description"]
        ).lower()

        if keyword in text:
            found.append(resource)

    return found


# ------------------------------------------------------------
# ПОШУК ЗА КАТЕГОРІЄЮ
# ------------------------------------------------------------

def find_resources_by_category(resources, category):

    category = category.lower().strip()

    if not category:
        return []

    found = []

    for resource in resources:

        if resource["category"].lower() == category:
            found.append(resource)

    return found


# ------------------------------------------------------------
# ДОДАВАННЯ НОВОГО РЕСУРСУ
# ------------------------------------------------------------

def add_resource(
    resources,
    name,
    category,
    description,
    contact,
    link
):

    # Перевіряємо обов'язкові поля.
    if not name or not category or not description:
        return False

    new_resource = {
        "name": name.strip(),
        "category": category.strip(),
        "description": description.strip(),
        "contact": contact.strip(),
        "link": link.strip()
    }

    resources.append(new_resource)

    return True