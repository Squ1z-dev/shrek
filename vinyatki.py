# Завдання 1
try:
    name = input("Введіть ваше ім'я: ")
    age = int(input("Введіть ваш вік: "))
    if age < 0 or age > 130:
        raise ValueError("Не правильний вік!")
    print(f"Привіт, {name}! Твій вік — {age}")
except ValueError:
    print("Помилка: Не правильний вік!")

# Завдання 2
# Перша версія не обробляє виняток всередині функції. Уся обробка знаходиться зовні;
def obrobka(name, age):
    if age < 0 or age > 130:
        raise ValueError("Не правильний вік!")
    return f"Привіт, {name}! Твій вік — {age}"

try:
    name = input("Введіть ваше ім'я: ")
    age = int(input("Введіть ваш вік: "))
    print(obrobka(name, age))
except ValueError:
    print("Помилка: Не правильний вік!")

# Друга версія обробляє виняток усередині функції.
def obrobka_vseredini(name, age):
    try:
        if age < 0 or age > 130:
            raise ValueError("Некоректний вік!")
        return f"Привіт, {name}! Твій вік — {age}"
    except ValueError:
        return "Помилка: Некоректний вік!"

name = input("Введіть ваше ім'я: ")
age = int(input("Введіть ваш вік: "))
print(obrobka_vseredini(name, age))

# Завдання 3
numbers = []
try:
    while True:
        num = int(input("Введіть число:(ведіть 0 для завершення "))
        if num == 0:
            break
        if num < 0:
            raise ValueError("Виявлено від'ємне число!")
        numbers.append(num)
    print(f"Сума всіх чисел: {sum(numbers)}")
except ValueError:
    print("Помилка: не пиши від'ємне число!")

# Завдання 4
# Перша версія не обробляє виняток всередині функції. Уся обробка знаходиться зовні;
def sum_plus_numbers(numbers):
    for num in numbers:
        if num < 0:
            raise ValueError("Виявлено від'ємне число!")
    return sum(numbers)

try:
    numbers = []
    while True:
        num = int(input("Введіть число: ведіть 0 для завершення "))
        if num == 0:
            break
        numbers.append(num)
    print(f"Сума всіх чисел: {sum_plus_numbers(numbers)}")
except ValueError:
    print("Помилка: Виявлено від'ємне число!")

# Друга версія обробляє виняток усередині функції.
def sum_plus_numbers2(numbers):
    try:
        for num in numbers:
            if num < 0:
                raise ValueError("Виявлено від'ємне число!")
        return sum(numbers)
    except ValueError:
        return "Помилка: Виявлено від'ємне число!"

numbers = []
while True:
    num = int(input("Введіть число:(ведіть 0 для завершення "))
    if num == 0:
        break
    numbers.append(num)
print(sum_plus_numbers2(numbers))