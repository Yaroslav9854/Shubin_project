# Вывести на экран фигуры, заполненные звездочками.
# Диалог с пользователем реализовать при помощи меню.

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
def print_6(height):
    for i in range(height):
        if i < 5:
            print("*" * (height // 2 - i - 1) + '*' * (2 * i + 1))

# Вывести на экран фигуры, заполненные звездочками.
# Диалог с пользователем реализовать при помощи меню.
# Надо вывести два равносторонних треугольника в квадрате которые находятся один на левой, второй на правой стороне квадрата.
# При этом одна вершина одного треугольника должна быть направлена на другую вершину второго треугольника.
# Эти вершины соединяются в центре квадрата с левой и правой стороны.
# Выполнить в виде одной функции.
# def print_7(height):

def print_8(height):
    for i in range(height):
        print(' ' * (height - i - 1), end='')
        print('*' * (i + 1))
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
    print("6. Равносторонние треугольники с основаниями по левым и правым краям")
    print("7. Равносторонний треугольник с основанием по левому краю")
    print("8. Равносторонний треугольник с основанием по правому краю")
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
    elif choice == 6:
        height = int(input("Введите размер квадрата: "))
        print_6(height)
    elif choice == 7:
        height = int(input("Введите размер квадрата: "))
        print_7(height)
    elif choice == 8:
        height = int(input("Введите размер квадрата: "))
        print_8(height)
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