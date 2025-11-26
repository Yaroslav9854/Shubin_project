def process_text(text):
    # 1.1: Приведение предложений к нужному формату
    # Разбиваем текст на предложения
    a = text.split('. ')
    # Приводим каждое предложение к нужному формату
    b = [i.strip().capitalize() for i in a]
    # Собираем обратно в единый текст
    c = '. '.join(b)
    # 1.2: Подсчет цифр
    d = sum(c.isdigit() for c in text)
    # 1.3: Подсчет знаков препинания
    e = sum(c in '.,!?;:' for c in text)
    # 1.4: Подсчет восклицательных знаков
    f = text.count('!')
    return {
        'formatted_text': c,
        'digits_count': d,
        'punctuation_count': e,
        'exclamation_marks': f
    }
text = "привет! как дела? у меня все хорошо. сегодня 25 число. а у вас?"
result = process_text(text)
print("Отформатированный текст:")
print(result['formatted_text'])
print("\nКоличество цифр:", result['digits_count'])
print("Количество знаков препинания:", result['punctuation_count'])
print("Количество восклицательных знаков:", result['exclamation_marks'])

# №2

# input_string = input("Введите элементы списка целых чисел через пробел: ")
# number_to_count = int(input("Введите число, которое хотите посчитать: "))
# elements = list(map(int, input_string.split()))
# result = elements.count(number_to_count)
# print(f"Ваше введенное число {number_to_count} встречается в списке {result} раз.")

# №3

# Lists = input("Введите нужные элементы в виде списка через пробел: ")
# numbers = list(map(int, Lists.split()))
# total_sum = sum(numbers)
# average_value = total_sum / len(numbers)
# print(f"Сумма всех элементов равна: {total_sum}")
# print(f"Среднее арифметическое число равно: {average_value:.2f}")