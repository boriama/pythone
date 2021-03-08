rating = [7, 5, 3, 3, 1]
x = 0
number = int(input("Введите любое число:"))
while x < len(rating):
    if rating[x] <= number:
        rating.insert(x, number)
        break
    else:
        rating.append(number)
        break
    x += 1
print(rating)
