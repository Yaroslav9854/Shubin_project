# Вывести на экран фигуры, заполненные звездочками.
# Диалог с пользователем реализовать при помощи меню.

# def print_figure(size):
#     # Выводим верхнюю часть квадрата
#     for i in range(size):
#         # Выводим пробелы
#         for j in range(i):
#             print(" ", end="")
#             # Выводим звездочки
#         for k in range(size - i):
#             print("*", end="")
#         print()  # Переход на новую строку
#
#
# def main():
#     while True:
#         print("\nМеню:")
#         print("1. Нарисовать фигуру")
#         print("2. Выход")
#
#         choice = input("Выберите пункт меню: ")
#
#         if choice == '1':
#             try:
#                 size = int(input("Введите размер фигуры (целое число должно быть больше 0): "))
#                 if size > 0:
#                     print_figure(size)
#                 else:
#                     print("Размер должен быть положительным числом!")
#             except ValueError:
#                 print("Ошибка: введите целое число!")
#
#         elif choice == '2':
#             print("До свидания!")
#             break
#         else:
#             print("Неверный выбор. Попробуйте еще раз.")
#
#
# if __name__ == "__main__":
#     main()


def print_1(height):
    for i in range(height):
        print(' ' * i + '*' * (height - i))
def print_2(height):
    for i in range(height):
        print('*' * (i + 1) + ' ' * (height + i))
def print_3(height):
    for i in range(height // 2):
        print(' ' * i + '*' * (2 * (height // 2 - i) - 1))
def print_4(height):
    for i in range(height // 2):
        print(' ' * (height // 2 - i - 1) + '*' * (2 * i + 1))
def print_5(height):
    print_3(height)
    print_4(height)
# def print_6(height):
#     for i in range(height // 2):
#         print(' ' * i + '*' * (2 * (height // 2 - i) - 1))
#     for i in range(height // 2):
#         print(' ' * (height // 2 - i - 1) + '*' * (2 * i + 1))
def print_7(height):
    for i in range(height):
        # Выводим пробелы для сдвига
        print(' ' * (height - i - 1), end='')
        # Выводим звездочки
        print('*' * (i + 1))
    # def print_8(height):
def print_9(height):
    for i in range(height):
        print('*' * (height - i) + ' ' * (i - 1))
def print_10(height):
    for i in range(height):
        print(' ' * (height - i - 1) + '*' * (i + 1))
while True:
    print("\nМеню:")
    print("1. Треугольник в правом верхнем углу")
    print("2. Треугольник в левом нижнем углу")
    print("3. Равносторонний треугольник с основанием по верхнему краю")
    print("4. Равносторонний треугольник с основанием по нижнему краю")
    print("5. Равносторонние треугольники с основаниями по верхнему и нижнему краям")
    # print("6. Равносторонние треугольники с основаниями по левым и правым краям")
    print("9. Треугольник в верхнем левом углу")
    print("10. Треугольник в нижнем правом углу")
    print("0. Выход")
    choice = int(input("Введите свой выбор: "))
    if choice == 1:
        height = int(input("Введите размер квадрата: "))
        print_1(height)
    elif choice == 2:
        height = int(input("Введите размер квадрата: "))
        print_2(height)
    elif choice == 3:
        height = int(input("Введите размер квадрата: "))
        print_3(height)
    elif choice == 4:
        height = int(input("Введите размер квадрата: "))
        print_4(height)
    elif choice == 5:
        height = int(input("Введите размер квадрата: "))
        print_5(height)
    # elif choice == 6:
    #     height = int(input("Введите размер квадрата: "))
    #     print_6(height)
    elif choice == 7:
        height = int(input("Введите размер квадрата: "))
        print_7(height)
    # elif choice == 8:
    #     height = int(input("Введите размер квадрата: "))
    #     print_8(height)
    elif choice == 9:
        height = int(input("Введите размер квадрата: "))
        print_9(height)
    elif choice == 10:
        height = int(input("Введите размер квадрата: "))
        print_10(height)
    elif choice == 0:
        print("До свидания!")
        break
    else:
        print("Неверный выбор. Пожалуйста, введите число от 0 до 10.")