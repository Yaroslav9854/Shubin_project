# №1
# Реализуйте класс «Человек».
# Необходимо хранить в полях класса: ФИО, дату рождения, контактный телефон, город, страну, домашний адрес.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
# from datetime import datetime
# class Person:
#     def __init__(self):
#         self._full_name = ""
#         self._birth_date = None
#         self._phone = ""
#         self._city = ""
#         self._country = ""
#         self._address = ""
#
#         # Методы для установки значений
#
#     def set_full_name(self, full_name):
#         self._full_name = full_name
#
#     def set_birth_date(self, birth_date):
#         try:
#             self._birth_date = datetime.strptime(birth_date, "%d.%m.%Y")
#         except ValueError:
#             print("Неверный формат даты. Используйте ДД.ММ.ГГГГ")
#
#     def set_phone(self, phone):
#         self._phone = phone
#
#     def set_city(self, city):
#         self._city = city
#
#     def set_country(self, country):
#         self._country = country
#
#     def set_address(self, address):
#         self._address = address
#
#         # Методы для получения значений
#
#     def get_full_name(self):
#         return self._full_name
#
#     def get_birth_date(self):
#         if self._birth_date:
#             return self._birth_date.strftime("%d.%m.%Y")
#         return None
#
#     def get_phone(self):
#         return self._phone
#
#     def get_city(self):
#         return self._city
#
#     def get_country(self):
#         return self._country
#
#     def get_address(self):
#         return self._address
#
#         # Метод для ввода всех данных
#
#     def input_data(self):
#         self.set_full_name(input("Введите ФИО: "))
#         self.set_birth_date(input("Введите дату рождения (ДД.ММ.ГГГГ): "))
#         self.set_phone(input("Введите телефон: "))
#         self.set_city(input("Введите город: "))
#         self.set_country(input("Введите страну: "))
#         self.set_address(input("Введите домашний адрес: "))
#
#         # Метод для вывода всех данных
#
#     def display_data(self):
#         print(f"ФИО: {self.get_full_name()}")
#         print(f"Дата рождения: {self.get_birth_date()}")
#         print(f"Телефон: {self.get_phone()}")
#         print(f"Город: {self.get_city()}")
#         print(f"Страна: {self.get_country()}")
#         print(f"Адрес: {self.get_address()}")
#
#     # Пример использования:
# person = Person()
# person.input_data()
# person.display_data()

# №2
# Создайте класс «Город».
# Необходимо хранить в полях класса: название города, название региона, название страны, количество жителей в городе,
# почтовый индекс города, телефонный код города.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
# class City:
#     def __init__(self):
#         self._name = ""
#         self._region = ""
#         self._country = ""
#         self._population = 0
#         self._postal_code = ""
#         self._phone_code = ""
#
#     # Методы установки значений
#     def set_name(self, name):
#         self._name = name
#
#     def set_region(self, region):
#         self._region = region
#
#     def set_country(self, country):
#         self._country = country
#
#     def set_population(self, population):
#         if population >= 0:
#             self._population = population
#         else:
#             raise ValueError("Население не может быть отрицательным")
#
#     def set_postal_code(self, postal_code):
#         self._postal_code = postal_code
#
#     def set_phone_code(self, phone_code):
#         self._phone_code = phone_code
#
#     # Методы получения значений
#     def get_name(self):
#         return self._name
#
#     def get_region(self):
#         return self._region
#
#     def get_country(self):
#         return self._country
#
#     def get_population(self):
#         return self._population
#
#     def get_postal_code(self):
#         return self._postal_code
#
#     def get_phone_code(self):
#         return self._phone_code
#
#     # Метод для ввода всех данных
#     def input_data(self):
#         self._name = input("Введите название города: ")
#         self._region = input("Введите название региона: ")
#         self._country = input("Введите название страны: ")
#         self._population = int(input("Введите количество жителей: "))
#         self._postal_code = input("Введите почтовый индекс: ")
#         self._phone_code = input("Введите телефонный код: ")
#
#     # Метод для вывода всех данных
#     def display_data(self):
#         print(f"Название города: {self._name}")
#         print(f"Регион: {self._region}")
#         print(f"Страна: {self._country}")
#         print(f"Население: {self._population}")
#         print(f"Почтовый индекс: {self._postal_code}")
#         print(f"Телефонный код: {self._phone_code}")
#
#     # Пример использования класса
#
#
# if __name__ == "__main__":
#     city = City()
#     city.input_data()
#     city.display_data()


# # №3
# Создайте класс «Страна».
# Необходимо хранить в полях класса: название страны, название континента, количество жителей в стране,
# телефонный код страны, название столицы, название городов страны.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класс.

# class Country:
#     def __init__(self):
#         self._name = ""
#         self._continent = ""
#         self._population = 0
#         self._phone_code = ""
#         self._capital = ""
#         self._cities =
#
#     # Методы установки значений полей
#     def set_name(self, name):
#         self._name = name
#
#     def set_continent(self, continent):
#         self._continent = continent
#
#     def set_population(self, population):
#         self._population = population
#
#     def set_phone_code(self, phone_code):
#         self._phone_code = phone_code
#
#     def set_capital(self, capital):
#         self._capital = capital
#
#     def set_cities(self, cities):
#         self._cities = cities
#
#     # Методы доступа к полям
#     def get_name(self):
#         return self._name
#
#     def get_continent(self):
#         return self._continent
#
#     def get_population(self):
#         return self._population
#
#     def get_phone_code(self):
#         return self._phone_code
#
#     def get_capital(self):
#         return self._capital
#
#     def get_cities(self):
#         return self._cities
#
#     # Метод для ввода данных
#     def set_data(self, name, continent, population, phone_code, capital, cities):
#         self._name = name
#         self._continent = continent
#         self._population = population
#         self._phone_code = phone_code
#         self._capital = capital
#         self._cities = cities
#
#     # Метод для вывода всех данных
#
#     def display_info(self):
#         print(f"Название страны: {self._name}")
#         print(f"Континент: {self._continent}")
#         print(f"Население: {self._population} человек")
#         print(f"Телефонный код: {self._phone_code}")
#         print(f"Столица: {self._capital}")
#         print(f"Города: {', '.join(self._cities)}")
#
# # Пример использования класса
# if __name__ == "__main__":
#     russia = Country()
#     russia.set_data(
#         name="Россия",
#         continent="Евразия",
#         population=144_000_000,
#         phone_code="+7",
#         capital="Москва",
#         cities=["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург"]
#     )
#
#     russia.display_info()
#     print("\nСтолица страны:", russia.get_capital())
#     print("Телефонный код:", russia.get_phone_code())

# №4
# Создайте класс «Дробь».
# Необходимо хранить в полях класса: числитель и знаменатель.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
# Также создайте методы класса для выполнения арифметических операций (сложение, вычитание, умножение, деление, и т.д.).
from math import gcd
class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    # Методы доступа к полям
    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    # Метод для ввода данных
    def set_fraction(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    # Метод для вывода данных
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    # Метод сокращения дроби
    def simplify(self):
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor
        # Приведение к стандартному виду
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

            # Арифметические операции
    def __add__(self, other):
        new_numerator = (self.numerator * other.denominator +
                         other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = (self.numerator * other.denominator -
                         other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError("Деление на ноль")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

        # Перегрузка оператора равенства

    def __eq__(self, other):
        return (self.numerator == other.numerator and
                self.denominator == other.denominator)

    # Пример использования:


if __name__ == "__main__":
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)

    print("f1:", f1)  # Вывод: 1/2
    print("f2:", f2)  # Вывод: 1/3

    print("f1 + f2:", f1 + f2)  # Вывод: 5/6
    print("f1 - f2:", f1 - f2)  # Вывод: 1/6
    print("f1 * f2:", f1 * f2)  # Вывод: 1/6
    print("f1 / f2:", f1 / f2)  # Вывод: 3/2