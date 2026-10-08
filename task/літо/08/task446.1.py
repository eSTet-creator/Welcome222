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
    pair = 0
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] == numbers[j]:
                pair += 1
    print(f"Кількість знайдених пар: {pair}")
    print("-" * 30)
    











