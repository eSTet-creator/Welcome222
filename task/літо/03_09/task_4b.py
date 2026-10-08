
def analize_grades(grades):
    for grade in grades:
        if grade >= 4:
            print(f"Оцінка {grade} - Чудово!")
        elif grade == 3:
            print(f"Оцінка {grade} - Задовільно!")
        else:
            print(f"Оцінка {grade} - Борг!")




def analize_gpa(grades):
    for grade in grades:
        gpa = sum(grades) / len(grades)
    if gpa >= 4:
        print(f"Стипендію призначено!\n")
    else:
        print(f"Стипендії немає! Треба підтягнути навчання.")

def total_result(grades):
    analize_grades(grades)
    analize_gpa(grades)


total_result([5, 4, 5, 5, 4])
total_result([3, 2, 4, 3, 4])