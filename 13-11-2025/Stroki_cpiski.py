def is_palindrome(text):
    # Приводим текст к нижнему регистру и убираем пробелы
    cleaned_text = text.lower().replace(" ", "")

    # Сравниваем строку с её реверсом
    return cleaned_text == cleaned_text[::-1]


# Получаем ввод от пользователя
user_input = input("Введите строку: ")

# Проверяем и выводим результат
if is_palindrome(user_input):
    print("Введённая строка является палиндромом!")
else:
    print("Введённая строка не является палиндромом.")