time = int(input("Введите количество секунд: "))
min_total = time // 60
hour = min_total // 60
min = min_total % 60
second = time % 60
print(f"Ваше время: {hour}:{min}:{second}")
