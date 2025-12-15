# Напишите функцию, которая отображает на экран форматированный текст, указанный ниже:
# “Don't let the noise of others' opinions drown out your own inner voice.”
# Steve Jobs

# def display():
#     a = "Don't let the noise of others' opinions drown out your own inner voice."
#     b = "Steve Jobs"
#     c = "*" * 50
#     formatted_quote = f"\n{c}\n\n\t{a}\n\n\t\t— {b}\n{c}"
#     print(formatted_quote)
# display()

# Напишите функцию, которая принимает два числа в качестве параметра и отображает все нечетные числа между ними.

# def print_numbers(start, end):
#     if start > end:
#         start, end = end, start
#     for number in range(start, end + 1):
#         if number % 2 != 0:
#             print(number)
# print_numbers(3, 10)  # Выведет: 3, 5, 7, 9

# Напишите функцию, которая отображает горизонтальную или вертикальную линию из некоторого символа.
# Функция принимает в качестве параметра: длину линии, направление, символ.

# def draw
def draw_line(length, direction, symbol):
    """
    Рисует горизонтальную или вертикальную линию
    Параметры:
    length (int) - длина линии
    direction (str) - направление ('horizontal' или 'vertical')
    symbol (str) - символ для рисования.
    """
    if direction.lower() == 'horizontal':
        # Для горизонтальной линии просто соединяем символы
        return symbol * length
    elif direction.lower() == 'vertical':
        # Для вертикальной линии выводим символ на новой строке
        return '\n'.join([symbol for _ in range(length)])
    else:
        raise ValueError("Направление должно быть 'horizontal' или 'vertical'")
    # Примеры использования:
# Горизонтальная линия
print(draw_line(5, 'horizontal', '*'))  # *****
# Вертикальная линия
print(draw_line(3, 'vertical', '#'))

# Напишите функцию, которая возвращает максимальное из четырёх чисел.
# Числа передаются в качестве параметров.

# def find_max(a, b, c, d):
#     return max(a, b, c, d)
# result = find_max(5, 12, 8, 3)
# print(result)  # Выведет: 12

# Напишите функцию, которая возвращает сумму чисел в указанном диапазоне.
# Границы диапазона передаются в качестве параметров. Alpha and Omega

# def summa_range(Alpha, Omega):
#     """
#     Возвращает сумму чисел в диапазоне от Alpha до Omega включительно.
#     Параметры:
#     Alpha (int) - начало диапазона
#     Omega (int) - конец диапазона
#
#     Возвращает:
#     int - сумму чисел в диапазоне
#     """
#     # Проверяем, что Alpha не больше Omega
#     if Alpha > Omega:
#         return "Ошибка: начало диапазона должно быть меньше конца"
#         # Вычисляем сумму с помощью встроенной функции sum()
#     return sum(range(Alpha, Omega + 1))
# # Пример использования:
# print(summa_range(1, 5))  # Выведет 15 (1+2+3+4+5)
# print(summa_range(3, 7))  # Выведет 25 (3+4+5+6+7)

# Напишите функцию, которая проверяет является ли число простым.
# Число передаётся в качестве параметра.
# Если число простое нужно вернуть из метода true, иначе false.

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
        # Исключаем четные числа и кратные 3
    if number % 2 == 0 or number % 3 == 0:
        return False
        # Проверяем делители от 5 до корня из числа
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


# Напишите функцию, которая проверяет является ли шестизначное число «счастливым».
# Число передаёт вернуть из функции true, иначе false.
# «Счастливое шестизначное число» — это число у которого сумма первых трёх цифр равна сумме трёх вторых цифр.
# Например, 123420 – счастливое 1+2+3 = 4+2+0, а 723422 - несчастливое 7+2+3 != 4+2+2.

def lucky_number(number):
    # Проверяем, что число шестизначное
    if not (100000 <= number <= 999999):
        return False
    # Преобразуем число в строку
    num_str = str(number)
     # Получаем первые и вторые три цифры
    first = num_str[:3]
    second = num_str[3:]
    # Считаем суммы
    sum1 = sum(int(i) for i in first)
    sum2 = sum(int(i) for i in second)
    # Сравниваем суммы
    return sum1 == sum2
# Примеры использования:
print(lucky_number(123420))  # True
print(lucky_number(723422))  # False
number = int(input("Введите шестизначное число: "))
if lucky_number(number):
    print(f"Число {number} является счастливым")
else:
    print(f"Число {number} не является счастливым")