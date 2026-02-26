# №1


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


# №2


# Получаем текст от пользователя
text = input("Введите текст: ")

# Получаем зарезервированные слова
reserved_words = input("Введите зарезервированные слова через пробел: ").split()

# Разбиваем текст на слова
words = text.split()

# Проходим по каждому слову в тексте
for i in range(len(words)):
    # Проверяем, есть ли слово в списке зарезервированных
    if words[i].lower() in [word.lower() for word in reserved_words]:
        # Если есть, меняем регистр на верхний
        words[i] = words[i].upper()

# Собираем текст обратно
result = ' '.join(words)

# Выводим результат
print("Измененный текст:")
print(result)


# №3


def count_sentences(text):
    # Разбиваем текст на предложения по точке
    sentences = text.split('.')

    # Удаляем пустые строки, которые могут появиться
    sentences = [s.strip() for s in sentences if s.strip()]

    return len(sentences)


# Пример использования
text = input("Введите текст: ")
sentence_count = count_sentences(text)
print(f"Количество предложений: {sentence_count}")