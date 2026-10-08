# Дано список словників із даними про учнів (ім'я, три оцінки).
# Потрібно порахувати середній бал кожного.
# Вивести відсортований за спаданням середнього балу список і зберегти результат у файл results.txt.

def calculate_average(grades):
     return sum(grades) / len(grades)


students = [
    {"name": "Ганна", "grades": [90, 85, 92]},
    {"name": "Іван", "grades": [70, 65, 80]},
    {"name": "Марко", "grades": [95, 98, 100]},
]

for student in students:
    student["average"] = calculate_average(student["grades"])

sorted_students = sorted(
    students, key=lambda student_dick: student_dick["average"], reverse=True)

print("Ім'я — Середній бал")
print("-" * 20)

with open("results.txt", "w", encoding="utf-8") as file:
    
    for student in sorted_students:
        name = student["name"]
        average_round = round(student["average"], 1)
        ryadok = f'{name} - {average_round}'

        print(ryadok)
        file.write(ryadok + "\n")




