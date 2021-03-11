"""def my_func(x, y):
    return x**y


print(my_func(int(input("Введите целое положительное число: ")),
              int(input("Введите целое отрицательное число: "))))"""


def my_func(x, y):
    i = y
    while i != -1:
        x *= x
        i += 1
    return 1/x


print(my_func(float(input("Введите целое положительное число: ")),
              float(input("Введите целое отрицательное число: "))))
