# Дано список чисел, підрахуйте, скільки пар елементів мають однакове значення (рівні).
# Будь-які два елементи, що дорівнюють один одному, слід вважати рівно один раз.
# Вхідні дані:
# 1 2 2 2 3 3 4
# 4 5 5 8 10 12 3 3
# 1 5 2 8 9 5
# Вихідні дані:
# 4
# 2
# 1

import random
import time
from collections import Counter

counts = [7, 8, 6]

min_number = 1
max_number = 9

data = []

for count in counts:
    nums = []

    for i in range(count):
        nums.append(random.randint(min_number, max_number))

    data.append(nums)
# Блок підрахунку пар
for numbers in data:
    print(f"Згенерований список: {numbers}")

    # 1. Рахуємо, скільки разів зустрічається кожне число
    # Наприклад, для [5, 5, 5, 2] отримаємо: {5: 3, 2: 1}
    elements_frequency = Counter(numbers)

    total_pairs = 0

    # 2. Застосовуємо формулу до кожного унікального числа
    for count in elements_frequency.values():
        if count > 1:
            # Формула: (k * (k - 1)) // 2
            total_pairs += (count * (count - 1)) // 2

    print(f"Кількість пар: {total_pairs}")
    print("-" * 30)
    