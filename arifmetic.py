# Завдання 1
expression = input("Введіть арифметичний вираз (наприклад, 23+12): ")
num1, operator, num2 = int(expression.split()[0]), expression[1], int(expression.split()[1])

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
print("Результат:", result)

# Завдання 2
import random
numbers = [random.randint(-10, 10) for _ in range(20)]
min_value = min(numbers)
max_value = max(numbers)
negative_count = sum(1 for num in numbers if num < 0)
positive_count = sum(1 for num in numbers if num > 0)
zero_count = numbers.count(0)

print("Мінімальне значення:", min_value)
print("Максимальне значення:", max_value)
print("Кількість від'ємних чисел:", negative_count)
print("Кількість додатних чисел:", positive_count)
print("Кількість нулів:", zero_count)