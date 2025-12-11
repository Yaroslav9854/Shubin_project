# №1
# Реализуйте класс «Автомобиль».
# Необходимо хранить в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

# class Car:
#     def __init__(self):
#         self._model = ""
#         self._year = 0
#         self._manufacturer = ""
#         self._engine_volume = 0.0
#         self._color = ""
#         self._price = 0.0
#
#     # Методы для установки значений
#
#     def set_model(self, model):
#         self._model = model
#
#     def set_year(self, year):
#         self._year = year
#
#     def set_manufacturer(self, manufacturer):
#         self._manufacturer = manufacturer
#
#     def set_engine_volume(self, volume):
#         self._engine_volume = volume
#
#     def set_color(self, color):
#         self._color = color
#
#     def set_price(self, price):
#         self._price = price
#
#     # Методы для получения значений
#
#     def get_model(self):
#         return self._model
#
#     def get_year(self):
#         return self._year
#
#     def get_manufacturer(self):
#         return self._manufacturer
#
#     def get_engine_volume(self):
#         return self._engine_volume
#
#     def get_color(self):
#         return self._color
#
#     def get_price(self):
#         return self._price
#
#     # Метод для ввода всех данных
#
#     def input_data(self):
#         self._model = input("Введите модель автомобиля: ")
#         self._year = int(input("Введите год выпуска: "))
#         self._manufacturer = input("Введите производителя: ")
#         self._engine_volume = float(input("Введите объем двигателя (л): "))
#         self._color = input("Введите цвет: ")
#         self._price = float(input("Введите цену: "))
#
#     # Метод для вывода всех данных
#
#     def display_data(self):
#         print(f"Модель: {self._model}")
#         print(f"Год выпуска: {self._year}")
#         print(f"Производитель: {self._manufacturer}")
#         print(f"Объем двигателя: {self._engine_volume} л")
#         print(f"Цвет: {self._color}")
#         print(f"Цена: {self._price} руб.")
#
#     # Пример использования класса
#
#
# if __name__ == "__main__":
#     car = Car()
#     car.input_data()
#     car.display_data()
#
#     # Пример доступа к отдельным полям
#     print(f"\nДоступ к отдельным полям:")
#     print(f"Модель: {car.get_model()}")
#     print(f"Цена: {car.get_price()} руб.")

# №2
# Реализуйте класс «Книга».
# Необходимо хранить в полях класса: название книги, год выпуска, издателя, жанр, автора, цену.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

# class Book:
#     def __init__(self):
#         self._title = ""
#         self._year = 0
#         self._publisher = ""
#         self._genre = ""
#         self._author = ""
#         self._price = 0.0
#
#     # Методы для установки значений
#
#     def set_title(self, title):
#         self._title = title
#
#     def set_year(self, year):
#         self._year = year
#
#     def set_publisher(self, publisher):
#         self._publisher = publisher
#
#     def set_genre(self, genre):
#         self._genre = genre
#
#     def set_author(self, author):
#         self._author = author
#
#     def set_price(self, price):
#         self._price = price
#
#     # Методы для получения значений
#
#     def get_title(self):
#         return self._title
#
#     def get_year(self):
#         return self._year
#
#     def get_publisher(self):
#         return self._publisher
#
#     def get_genre(self):
#         return self._genre
#
#     def get_author(self):
#         return self._author
#
#     def get_price(self):
#         return self._price
#
#     # Метод для ввода всех данных
#
#     def input_data(self):
#         self._title = input("Введите название книги: ")
#         self._year = int(input("Введите год выпуска: "))
#         self._publisher = input("Введите издателя: ")
#         self._genre = input("Введите жанр: ")
#         self._author = input("Введите автора: ")
#         self._price = float(input("Введите цену: "))
#
#     # Метод для вывода всех данных
#
#     def display_info(self):
#         print(f"Название: {self._title}")
#         print(f"Год выпуска: {self._year}")
#         print(f"Издатель: {self._publisher}")
#         print(f"Жанр: {self._genre}")
#         print(f"Автор: {self._author}")
#         print(f"Цена: {self._price} руб.")
#
#     # Пример использования класса
#
#
# if __name__ == "__main__":
#     book = Book()
#     book.input_data()
#     print("\nИнформация о книге:")
#     book.display_info()
#
#     # Пример доступа к отдельным полям
#     print("\nДоступ к отдельным полям:")
#     print(f"Автор: {book.get_author()}")
#     print(f"Цена: {book.get_price()} руб.")


# №3
# Реализуйте класс «Стадион».
# Необходимо хранить в полях класса: название стадиона, дату открытия, страну, город, вместимость.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
# class Stadium:
#     def __init__(self):
#         self._name = ""
#         self._opening_date = ""
#         self._country = ""
#         self._city = ""
#         self._capacity = 0
#
#     # Методы для установки значений
#
#     def set_name(self, name):
#         self._name = name
#
#     def set_opening_date(self, date):
#         self._opening_date = date
#
#     def set_country(self, country):
#         self._country = country
#
#     def set_city(self, city):
#         self._city = city
#
#     def set_capacity(self, capacity):
#         if capacity > 0:
#             self._capacity = capacity
#         else:
#             raise ValueError("Вместимость должна быть положительным числом")
#
#     # Методы для получения значений
#
#     def get_name(self):
#         return self._name
#
#     def get_opening_date(self):
#         return self._opening_date
#
#     def get_country(self):
#         return self._country
#
#     def get_city(self):
#         return self._city
#
#     def get_capacity(self):
#         return self._capacity
#
#     # Метод для ввода всех данных
#
#     def input_data(self):
#         self._name = input("Введите название стадиона: ")
#         self._opening_date = input("Введите дату открытия: ")
#         self._country = input("Введите страну: ")
#         self._city = input("Введите город: ")
#         try:
#             self._capacity = int(input("Введите вместимость: "))
#         except ValueError:
#             print("Ошибка! Вместимость должна быть числом")
#             self._capacity = 0
#
#     # Метод для вывода всех данных
#
#     def display_info(self):
#         print(f"Название стадиона: {self._name}")
#         print(f"Дата открытия: {self._opening_date}")
#         print(f"Страна: {self._country}")
#         print(f"Город: {self._city}")
#         print(f"Вместимость: {self._capacity} мест")
#
#     # Пример использования класса
#
#
# if __name__ == "__main__":
#     stadium = Stadium()
#     stadium.input_data()
#     stadium.display_info()
#
#     # Пример доступа к отдельным полям
#     print("\nДоступ к отдельным полям:")
#     print(f"Название стадиона: {stadium.get_name()}")
#     print(f"Вместимость: {stadium.get_capacity()} мест")