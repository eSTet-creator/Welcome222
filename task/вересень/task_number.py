# Дано список чисел із повторами — вивести унікальні значення через set()
# і порахувати, скільки дублікатів було видалено.


numbers = [1, 5, 3.14, 5, 7, 1, 2, 5, 4]

def duplicates_count(num):

    unic = sorted(set(num))
    duplicates = len(num) - len(unic)

    return unic, duplicates
unic, duplicates = duplicates_count(numbers)

print(f"Початковий список: {numbers}")
print(f"Унікальні значення: {unic}")
print(f"Видалено дублікатів: {duplicates}")
