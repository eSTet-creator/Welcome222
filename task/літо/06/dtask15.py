h_in_feets = int(input("Введіть висоту в футах: "))
h_in_inches = int(input("Введіть висоту в дюймах: "))
h_in_cm = h_in_feets * 30.48 + h_in_inches * 2.54
result_height = round(h_in_cm)
print(f"Your height is: {result_height} cm.")
