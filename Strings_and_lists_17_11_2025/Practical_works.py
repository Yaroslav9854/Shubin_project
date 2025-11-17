# №1

# my_list = input("Введите строку: ")
# reversed_string = my_list[::-1]
# print(reversed_string)

# №2

# Привет, мир! 123

# phrase = input("Введите строку цифрой или буквой: ")
# letter = sum(ou.isalpha() for ou in phrase)
# figure = sum(ou.isdigit() for ou in phrase)
# print(f"Количество букв в строке: {letter}")
# print(f"Количество цифр в строке: {figure}")

# №3

# a = input("Введите строку через пробел ")
# c = input("Введите символ для поиска ")
# counter = 0
# while counter < len(a):
#     val = a[counter]
#     if val == c:
#         print(f"Мы нашли число, которое вы ввели. {c} Не благодарите.")
#         break
#     print(a[counter])
#     counter += 1
# else:
#     print("Боюсь такого числа в строке нет.")
# val2 = a.count(c)
# print(f"Вот сколько раз это число в строке встречается {val2}")

# №4

# string = input('Введите строку: ')
# word = input('Введите слово: ')
# val = string.count(word)
# print(f"Вот сколько раз это число в строке встречается {val}")

# №5

# a = input("Введите строку для замены в нём слова: ")
# b = input("Введите слово для поиска: ")
# c = input("Введите слово для замены: ")
# d = a.replace(b, c)
# print(f"Вот что у нас получилось: {d}")