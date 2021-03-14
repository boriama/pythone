from math import factorial
from itertools import count


def fact(n):
    for el in count(n - n):
        if el == n:
            break
        factorial(el)
        yield el


f = fact(int(input('Введите число: ')))
print(f)

for el in f:
    print(el)
