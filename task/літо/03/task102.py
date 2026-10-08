# наперед визначений правильний пароль
correct_password = "starlink"
# запитуємо пароль в користувача
user_input = input ("enter password: ")
# перевіряємо чи правильно вказаний пароль
if user_input == correct_password:
    print("Password accepted")
else:
    print("Sorry, that is the wrong password")