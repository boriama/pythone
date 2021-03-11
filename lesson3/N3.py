def my_func(number_1, number_2, number_3):
    if number_1 <= number_2:
        var_1 = number_2
    else:
        var_1 = number_1
    if number_1 <= number_3:
        var_2 = number_3
    else:
        var_2 = number_1
    return var_1 + var_2


print(my_func(int(input("Число 1 :")), int(input("Число 2 :")), int(input("Число 3 :"))))
