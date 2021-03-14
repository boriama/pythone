from itertools import count

start = int(input("Введите число: "))
for el in count(start):
    if el > start + 10:
        break
    else:
        print(el)
