#№1

# a = int(input("Введите начальное число: "))
# b = int(input("Введите конечное число: "))
# if a > b:
#     print("Ошибка: начало диапазона должно быть меньше конца")
# else:
#     for number in range(a, b + 1):
#         print(number)

#№2

# a = int(input("Введите начальное число: "))
# b = int(input("Введите конечное число: "))
# if a > b:
#     print("Ошибка: начало диапазона должно быть меньше конца")
# else:
#     for number in range(a, b + 1):
#         if number % 2 != 0:
#             print(number)

#№3

# a = int(input("Введите начальное число: "))
# b = int(input("Введите конечное число: "))
# if a > b:
#     print("Ошибка: начало диапазона должно быть меньше конца")
# else:
#     for number in range(a, b + 1):
#         if number % 2 == 0:
#             print(number)

#№4

# a = int(input("Введите конечное число: "))
# b = int(input("Введите начальное число: "))
# if a < b:
#     a, b = b, a
#     print("Ошибка: начало диапазона должно быть меньше конца")
# else:
#     for number in range(a, b - 1, -1):
#         print(number)

#№5

# a = int(input("Введите начальное число: "))
# b = int(input("Введите конечное число: "))
# if a > b:
#     a, b = b, a
#     print(f"Ошибка: нужно нормализовать от начала ({a}) до конца ({b})")
# else:
#     for number in range(a, b + 1):
#         if number % 2 != 0:
#             print(number)



# a = int(input("Введите начальное число: "))
# b = int(input("Введите конечное число: "))
# if a > b:
#     print("Ошибка: начало диапазона должно быть меньше конца")
# else:
#     numbers = list(range(a, b + 1))
#     total_sum = sum(numbers)
#     count = len(numbers)
#     average = total_sum / count
#     print(f"Числа в диапазоне: {numbers}")
#     print(f"Сумма чисел: {total_sum}")
#     print(f"Среднее арифметическое: {average:.2f}")



# a = int(input("Введите число: "))
# if a < 0:
#     print("Факториал не определяют для отрицательных чисел")
# else:
#     factorial = 1
#     for i in range(1, a + 1):
#         factorial *= i
#     print(f"Факториал числа {a} равен {factorial}")



# a = int(input("Введите длину линии: "))
# b = ""
# for i in range(a):
#     b += "*"
# print(b)



# a = int(input("Введите длину линии: "))
# b = input("Введите символ для заполнения: ")
# c = a * b
# print(c)



# a = int(input("Введите число для таблицы умножения: "))
# print(f"Таблица умножения для числа {a}:")
# for b in range(1, 11):
#     c = a * b
#     print(f"{a} * {b} = {c}")



# a = int(input("Введите нижнюю границу диапазона: "))
# b = int(input("Введите верхнюю границу диапазона: "))
# if a > b:
#     print("Ошибка: вы ввели неправильно!")
#     exit()
# while True:
#     try:
#         с = int(input(f"Введите число в диапазоне от {a} до {b}: "))
#         if a <= с <= b:
#             break
#         else:
#             print(f"Число должно быть в диапазоне от {a} до {b}. Попробуйте еще раз.")
# for d in range(a, b + 1):
#     if d == с:
#         print(f"!{d}!", end=' ')
#     else:
#         print(d, end=' ')


import random
import time
def guess_number():
    number_to_guess = random.randint(1, 500)
    attempts = 0
    start_time = time.time()
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 500. Попробуйте его угадать.")
    print("Введите 0, если хотите выйти из игры.")''