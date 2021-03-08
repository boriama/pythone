list_words = list(input("Введите элементы списка через пробел:").split())
x = 0
y = 1
while x < len(list_words):
    print(y, ".", list_words[x][:10])
    y += 1
    x += 1
