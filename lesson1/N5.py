gain = int(input("Введите количество выручки: "))
exp = int(input("Введите количество затрат: "))
if gain > exp:
    print("Фирма работает прибыльно")
    profit = gain - exp
    ratio = profit / gain
    count = int(input("Введите количество сотрудников:"))
    salary = profit / count
    print(f"Количество прибыли на одного сотрудника: {salary}")
else:
    print("Фирма работает не прибыльно")


