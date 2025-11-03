#a = 123456 // 10
#b = a % 10
#b = 123400 + 56
#print(a)
#print(b)

#1

#number = input("Введите шестизначное число: ")
#if len(number) != 6:
#    print("Ошибка: число должно содержать 6 символов")
#else:
#    first_half = int(number) + int(number) + int(number)
#    second_half = int(number) + int(number) + int(number)
#if first_half == second_half:
#    print("Введённое число счастливое")
#else:
#    print("Введённое число несчастливое")

#2

a = int(input("Введите число: "))
if a != 6:
    print("Ошибка: число должно содержать 6 символов")
else:
    b = a // 1000
    one = b // 100
    two = b % 11
    three = b % 10
    c = a % 1000
    four = c // 100
    five = c % 11
    six = c % 10
    if (one + two + three) == (four + five + six):
        print("Введённое число счастливое")
    else:
        print("Введённое число несчастливое")
#3

#if len(a) != 6:
#    print("Ошибка: число должно содержать 6 символов")
#else: