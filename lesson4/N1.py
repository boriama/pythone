from sys import argv

name, hour, money, prize = argv

print("Ожидаемая заработная плата: ", int(hour) * int(money) + int(prize))
