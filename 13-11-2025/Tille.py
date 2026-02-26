# val_str = "Привет"
# val_int = 10
# val_list = [1, 2, 3]
#
# print(id(val_list))
# val_list.append(4)
# print(id(val_list))

# counter = 0
# for i in range(1, 10):
#     counter += 1
#     print(id(counter))

"""
Hello World
"""

# строка[начало:конец]
# строка[начало:конец:шаг] [start:stop:step]
# val_int = "1234567890"
# print(val_int[::-1])

# val_str = "Hello World"
# print("Python" in val_str)

# s = "AB"
# s = s * 2 + "CD"
# print(s)

# age = input()
# print(type(age))

# Написать код, который запрашивает имя пользователя и  затем выводит его в рамочку в виде символа *
# Подсказка: длинна рамки = длинна имени + 4 символа, длинна имени вычисляется функцией len(name)
# Например:

"""
******
* Петр *
******
"""

# iun = input("Введите ваше имя: ")
# len_name = len(iun) + 4
# border = '*' * len_name
# middle = f'*{iun}*'
# print(border)
# print(middle)
# print(border)

# Создать список из нескольких чисел и: добавьте число в конец списка, в начало
# удалите первое число, последнее число, проверьте что некое число находится в списке

# numbers = [1, 2, 3, 4, 5]
# print("Что мы сейчас вписали:", numbers)
# numbers.append(6)
# print("Добавляем конец:", numbers)
# numbers.insert(0, 0)
# print("Добавляем начало:", numbers)
# numbers = numbers[1:]
# print("После удаления первого числа:", numbers)
# numbers = numbers[:-1]
# print("После удаления последнего числа:", numbers)
# n = 2
# if n in numbers:
#     print(f"Число {n} есть в списке")
# else:
#     print(f"Числа {n} нет в списке")
