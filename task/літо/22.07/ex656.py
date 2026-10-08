
def culc_accumulation(sum_deposit: float, rate: float, years: int) -> float:
    return sum_deposit + sum_deposit * rate / 100 * years

n = float(input("Введіть суму вкладу: "))
p = float(input("Введіть процентну ставку: "))
m = int(input("Введіть кількість років: "))
accumulation = n + n * p / 100 * m
print(f"{accumulation: .2f}")
