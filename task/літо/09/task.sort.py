import random

# Створення списку випадкових чисел
numbers = [random.randint(1, 100) for _ in range(10)]

print("Початковий список:")
print(numbers)


# 1. Сортування перестановками
def exchange_sort(arr):
    a = arr.copy()
    n = len(a)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

    return a

# 2. Бульбашкове сортування
def bubble_sort(arr):
    a = arr.copy()
    n = len(a)

    for i in range(n):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a


# 3. Сортування вибором
def selection_sort(arr):
    a = arr.copy()
    n = len(a)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j

        a[i], a[min_index] = a[min_index], a[i]

    return a
# 4. Сортування вставками
def insertion_sort(arr):
    a = arr.copy()

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a
print("\nСортування перестановками:")
print(exchange_sort(numbers))

print("\nБульбашкове сортування:")
print(bubble_sort(numbers))

print("\nСортування вибором:")
print(selection_sort(numbers))

print("\nСортування вставками:")
print(insertion_sort(numbers))

print("\nПеревірка за допомогою sorted():")
print(sorted(numbers))