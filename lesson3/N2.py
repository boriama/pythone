def data(name, surname, age, city, email, phone):
    print(f"фио: {name} {surname}, Возраст: {age}, Город проживания: {city}, email: {email}, Номер телефона: {phone}")


print(data(name=input("Ваше имя: "), surname=input("Ваша фамилия: "), age=input("Возраст: "),
           city=input("Город проживания: "), email=input("email: "), phone=input("Контактный номер: ")))
