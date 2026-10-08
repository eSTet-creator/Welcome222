def analize_grades(grades):
    for grade in grades:
        if grade >= 4:
            print(f"Оцінка {grade} - Чудово!")
        elif grade == 3:
            print(f"Оцінка {grade} - Задовільно!")
        else:
            print(f"Оцінка {grade} - Борг!")

analize_grades([5, 4, 5, 5, 4])
analize_grades([3, 2, 4, 3, 4])


def analize_gpa(grades):
    for grade in grades:
        gpa = sum(grades) / len(grades)
    if gpa >= 4:
        print(f"Стипендію призначено!")
    else:
        print(f"Стипендії немає! Треба підтягнути навчання.")

analize_gpa([5, 4, 5, 5, 4])
analize_gpa([3, 2, 4, 3, 4])
