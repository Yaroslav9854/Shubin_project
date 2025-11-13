#№1

start = int(input("Введите первое число: "))
end = int(input("Введите второе число: "))
for number in range(start, end + 1):
    if number % 7 == 0:
        print(number)

#№2
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a > b:
    a, b = b, a
# 1. Все числа диапазона
print("\n1. Все числа диапазона:")
for i in range(a, b + 1):
    print(i, end=' ')
print()
# 2. Все числа в убывающем порядке
print("\n2. Числа в убывающем порядке:")
for i in range(b, a - 1, -1):
    print(i, end=' ')
print()
# 3. Числа, кратные 7
print("\n3. Числа, кратные 7:")
for i in range(a, b + 1):
    if i % 7 == 0:
        print(i)
# 4. Количество чисел, кратных 5.
print("\n4. Количество чисел, кратных 5:")
count = 0
for i in range(a, b + 1):
    if i % 5 == 0:
        count += 1
        print(f"Это: {i}")

#№3

First = int(input("Введите первое число для диапазона: "))
Second = int(input("Введите последнее число для диапазона: "))
for i in range(First, Second + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)