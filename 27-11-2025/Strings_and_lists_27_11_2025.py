# №1

# example = input("Введите арифметическое выражение: ")
# if '+' in example:
#     a, b = example.split('+')
#     result = float(a) + float(b)
# elif '-' in example:
#     a, b = example.split('-')
#     result = float(a) - float(b)
# elif '*' in example:
#     a, b = example.split('*')
#     result = float(a) * float(b)
# elif '/' in example:
#     a, b = example.split('/')
#     if float(b) == 0:
#         print("Ошибка: Нельзя делить на ноль!")
#         exit()
#     result = float(a) / float(b)
# else:
#     print("Ошибка: выражение написано направильно")
#     exit()
# print(f"Результат: {result}")

# №2

# import random
#
# random = [random.randint(-50, 50) for _ in range(20)]
# print("Создан случайный список:", random)
# min = max = random[0]
# negative = positive = zero = 0
# for number in random:
#     if number < min:
#         min = number
#     if number > max:
#         max = number
#     if number < 0:
#         negative += 1
#     elif number > 0:
#         positive += 1
#     else:
#         zero += 1
# print(f"Минимальное значение: {min}")
# print(f"Максимальное значение: {max}")
# print(f"Количество отрицательных элементов: {negative}")
# print(f"Количество положительных элементов: {positive}")
# print(f"Количество нулей: {zero}")