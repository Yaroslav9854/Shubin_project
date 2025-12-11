# №1
# Реализуйте класс «Человек».
# Необходимо хранить в полях класса: ФИО, дату рождения, контактный телефон, город, страну, домашний адрес.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

class Human:
    def __init__(self):
        self._full_name = ""
        self._date_of_birth = 0
        self._contact_phone_number = ""
        self._city = ""
        self._country = ""
        self._home_address = 0

    # Методы для установки значений

    def set_full_name(self, full_name):
        self._full_name = full_name

    def set_date_of_birth(self, date_of_birth):
        self._date_of_birth = date_of_birth

    def set_contact_phone_number(self, contact_phone_number):
        self._contact_phone_number = contact_phone_number

    def set_city(self, city):
        self._city = city

    def set_country(self, country):
        self._country = country

    def set_home_address(self, home_address):
        self._home_address = home_address

    # Методы для получения значений

    def get_full_name(self):
        return self._full_name

    def get_date_of_birth(self):
        return self._date_of_birth

    def get_contact_phone_number(self):
        return self._contact_phone_number

    def get_city(self):
        return self._city

    def get_country(self):
        return self._country

    def get_home_address(self):
        return self._home_address

    # Метод для ввода всех данных

    def input_data(self):
        self._full_name = input("Введите ФИО: ")
        self._date_of_birth = int(input("Введите дату рождения: "))
        self._contact_phone_number = input("Введите номер телефона: ")
        self._city = float(input("Введите город: "))
        self._country = input("Введите страну: ")
        self._home_address = float(input("Введите домашний адрес: "))
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