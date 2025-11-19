# Сегодня температура воздуха +25 градусов, а давление составляет 760 мм ртутного столба. это грустно.

# №1

text = input("Введите строку: ")
figure = sum(char.isdigit() for char in text)
punctuation = ['.', ',', ':', ';', '?']
count_punctuations = sum(text.count(punc) for punc in punctuation)
exclamation = ['!']
count_exclamation = sum(text.count(ex) for ex in exclamation)
print(text)
print(f"В тексте найдено {figure} цифр.")
print(f"В вашем предложении нашли вот сколько знаков препинания {count_punctuations}.")
print(f"Из них восклицательных знаков: {count_exclamation}")

# №2

# В 2022 году 2 февраля в 2 часа ночи произошло редкое событие: одновременно встретились две двойки — число месяца, год и часы показывали цифру два.

# a = input('Введите информацию в строку с цифрами через пробел: ')
# b = input('Введите число, количество которого в списке, хотите узнать: ')
# counter = 0
# while counter < len(a):
#     val = a[counter]
#     if val == b:
#         print(f"Мы нашли число, которое вы ввели. {b}")
#         break
#     print(a[counter])
#     counter += 1
# else:
#     print("Боюсь такого числа в строке нет или вы ввели символ, который не является цифрой.")
# c = a.count(b)
# print(f"Вот сколько раз это число в строке встречается {c}")

# №3

# numbers = input('Введите элементные числа из категории целых. Через пробел и только положительные числа: ')
# figure = list(map(int, numbers.split()))
# if len(figure) > 0:
#     total_sum = sum(figure)
#     average_value = total_sum / len(figure)
#     print(f"Сумма цифр в этой строке будет: {total_sum}")
#     print(f"Среднее арифметическое будет равна: {average_value:.2f}")
# else:
#     print("Ошибка: введена пустая строка. Надо ввести числа.")