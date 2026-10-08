import random
from os.path import join

languages = input("Введіть назви мов: ").split()
if languages == sorted(languages):
    random.shuffle(languages)
print("Список до сортування:", " ".join(languages))
languages.sort()
print("Результат: ")
print(" ".join(languages))