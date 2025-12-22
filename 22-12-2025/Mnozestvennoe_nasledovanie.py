# №2

# class Колёса:
#     def __init__(self):
#         self.kolichestvo_koles = 4
#
#     def info(self):
#         return f'Количество колёс: {self.kolichestvo_koles}'
#
#
# class Двигатель:
#     def __init__(self):
#         self.tip_dvigatelya = 'бензиновый'
#
#     def info(self):
#         return f'Тип двигателя: {self.tip_dvigatelya}'
#
#
# class Двери:
#     def __init__(self):
#         self.kolichestvo_dverey = 5
#
#     def info(self):
#         return f'Количество дверей: {self.kolichestvo_dverey}'
#
#
# class Автомобиль(Колёса, Двигатель, Двери):
#     def __init__(self):
#         # Инициализация родительских классов
#         Колёса.__init__(self)
#         Двигатель.__init__(self)
#         Двери.__init__(self)
#
#     def vse_info(self):
#         result = []
#         for cls in type(self).__mro__[:-1]:  # перебираем цепочку наследования кроме самого объекта
#             if hasattr(cls, 'info'):
#                 result.append(cls.info(self))
#         return '\n'.join(result)
#
#
# # Пример использования
# avto = Автомобиль()
# print(avto.vse_info())

# №3

# # Базовый класс
# class Pet:
#     def __init__(self, name, species, characteristics):
#         self.name = name
#         self.species = species
#         self.characteristics = characteristics
#
#     def sound(self):
#         raise NotImplementedError("Метод должен быть переопределен в подклассе")
#
#     def show(self):
#         print(f"Имя: {self.name}")
#
#     def type(self):
#         print(f"Вид: {self.species}")
#
#     # Класс Собака
#
#
# class Dog(Pet):
#     def __init__(self, name, breed, size):
#         characteristics = f"Порода: {breed}, Размер: {size}"
#         super().__init__(name, "Собака", characteristics)
#
#     def sound(self):
#         print("Гав-гав!")
#
#     # Класс Кошка
#
#
# class Cat(Pet):
#     def __init__(self, name, breed, fur_color):
#         characteristics = f"Порода: {breed}, Окрас: {fur_color}"
#         super().__init__(name, "Кошка", characteristics)
#
#     def sound(self):
#         print("Мяу-мяу!")
#
#     # Класс Попугай
#
#
# class Parrot(Pet):
#     def __init__(self, name, species, can_speak):
#         characteristics = f"Вид: {species}, Умеет говорить: {can_speak}"
#         super().__init__(name, "Попугай", characteristics)
#
#     def sound(self):
#         print("Кар-кар! (или повторяет человеческие слова)")
#
#     # Класс Хомяк
#
#
# class Hamster(Pet):
#     def __init__(self, name, fur_color, size):
#         characteristics = f"Окрас: {fur_color}, Размер: {size}"
#         super().__init__(name, "Хомяк", characteristics)
#
#     def sound(self):
#         print("Пи-пи-пи!")
#
#     # Пример использования
#
#
# dog = Dog("Рекс", "Немецкая овчарка", "Большой")
# cat = Cat("Мурка", "Сиамская", "Рыжий")
# parrot = Parrot("Кеша", "Волнистый", "Да")
# hamster = Hamster("Пушистик", "Белый", "Маленький")
#
# # Демонстрация методов
# dog.show()  # Имя: Рекс
# dog.type()  # Вид: Собака
# dog.sound()  # Гав-гав!
#
# cat.show()  # Имя: Мурка
# cat.type()  # Вид: Кошка
# cat.sound()  # Мяу-мяу!
#
# parrot.show()  # Имя: Кеша
# parrot.type()  # Вид: Попугай
# parrot.sound()  # Кар-кар!
#
# hamster.show()  # Имя: Пушистик
# hamster.type()  # Вид: Хомяк
# hamster.sound()  # Пи-пи-пи!

# №4

# Базовый класс
class Employer:
    def __init__(self):
        pass

    def print(self):
        print("This is Employer class")

    # Производный класс для президента


class President(Employer):
    def __init__(self, name, company):
        super().__init__()
        self.name = name
        self.company = company

    def print(self):
        print(f"President: {self.name}")
        print(f"Company: {self.company}")
        print("Responsible for strategic management")

    # Производный класс для менеджера


class Manager(Employer):
    def __init__(self, name, department):
        super().__init__()
        self.name = name
        self.department = department

    def print(self):
        print(f"Manager: {self.name}")
        print(f"Department: {self.department}")
        print("Responsible for team management")

    # Производный класс для работника


class Worker(Employer):
    def __init__(self, name, position):
        super().__init__()
        self.name = name
        self.position = position

    def print(self):
        print(f"Worker: {self.name}")
        print(f"Position: {self.position}")
        print("Performs daily tasks")

    # Пример использования


if __name__ == "__main__":
    # Создаём объекты
    employer = Employer()
    president = President("John Doe", "TechCorp")
    manager = Manager("Alice Smith", "Sales")
    worker = Worker("Bob Johnson", "Software Developer")

    # Выводим информацию
    print("Базовый класс:")
    employer.print()
    print("\nПрезидент:")
    president.print()
    print("\nМенеджер:")
    manager.print()
    print("\nРаботник:")
    worker.print()
