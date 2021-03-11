def division(number_1, number_2):
    if number_2 == 0:
        print("Не получается выполнить деление на 0")
    else:
        return number_1 / number_2


print("Резульат:", division(int(input("Введите число которое хотите разделить:")),
                            int(input("Введите число на которое хотите разделить:"))))
