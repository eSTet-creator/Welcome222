# Написати скрипт-лічильник слів у реченні: словник {слово: кількість повторень},
# виведений через цикл по .items().

text = "реве реве та стогне Дніпр широкий сердитий вітер завива"
text_lower = text.lower() # зробили всі літери маленькими
counts = {}
for word in text_lower.split():
    counts[word] = counts.get(word, 0) + 1
for word, count in counts.items():
    print(f"Слово '{word}' зустрічається {count} р.")


