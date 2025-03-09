import random
"""Завдання 1
Користувач вводить із клавіатури арифметичний вираз. Наприклад, 23+12.
Необхідно вивести на екран результат виразу. Для нашого прикладу — це 35. Арифметичний вираз може складатися тільки з трьох частин: число, операція, число.
Можливі операції: +, -, *, /.

Завдання 2
У списку цілих, заповненому випадковими числами, визначити мінімальний і максимальний елементи, порахувати кількість від'ємних елементів,
порахувати кількість додатних елементів, порахувати кількість нулів. Результати вивести на екран.

"""
viraz = input("Введіть арифметичний вираз ")
if '+' in viraz:
    num1, num2 = viraz.split('+')
    result = int(num1) + int(num2)
elif '-' in viraz:
    num1, num2 = viraz.split('-')
    result = int(num1) - int(num2)
elif '*' in viraz:
    num1, num2 = viraz.split('*')
    result = int(num1) * int(num2)
elif '/' in viraz:
    num1, num2 = viraz.split('/')
    result = int(num1) / int(num2)
else:
    print("Not correct enter ")
print(f"Результат: {result}")

"""--------Task2--------"""

numbs = [random.randint(-10, 10) for i in range(10)]
print(numbs)
min_num = min(numbs)
max_num = max(numbs)

minus = 0
positive = 0
zero = 0

for num in numbs:
    if num < 0:
        minus += 1
    elif num > 0:
        positive += 1
    else:
        zero += 1

print(f"Min el: {min_num}")
print(f"MAx el: {max_num}")
print(f"Minus num: {minus}")
print(f"positive numbs: {positive}")
print(f"Zero count: {zero}")