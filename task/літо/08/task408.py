import random

languages = input("Введіть назви мов: ").split()
if languages == sorted(languages):
    random.shuffle(languages)
print("Список до сортування:", " ".join(languages))
languages.sort()
languages.reverse()
print("Результат:")
print(" ".join(languages))
