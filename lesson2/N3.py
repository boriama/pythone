seasons = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8],
           'осень': [9, 10, 11]}
userInput = int(input("Введите номер месяца :"))
for month in seasons:
    if userInput in seasons[month]:
        print(month.capitalize())

seasons = ['зима', 'весна', 'лето', 'осень']
userInput = int(input("Введите номер месяца: "))
if 3 <= userInput <= 5:
    print(seasons[1])
if 6 <= userInput <= 8:
    print(seasons[2])
if 9 <= userInput <= 11:
    print(seasons[3])
if userInput == 12:
    print(seasons[0])
if 1 <= userInput <= 2:
    print(seasons[0])
# не уверен что это правильное решение, но ничего больше не придумал
