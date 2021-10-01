list_change = list(input("Введите элементы списка через пробел:").split())
print(list_change)
x = 0
number_1 = 0
number_2 = 1
while x < len(list_change):
    y = list_change[number_1]
    list_change[number_1] = list_change[number_2]
    list_change[number_2] = y
    number_1 += 2
    number_2 += 2
    x += 2
    if number_2 == len(list_change):
        break
print(list_change)
