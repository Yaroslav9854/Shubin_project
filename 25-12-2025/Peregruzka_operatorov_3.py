class Airplane:
    def __init__(self, model, current_passengers, max_passengers):
        """
        Инициализация самолета.
        :param model: Модель/тип самолета (строка)
        :param current_passengers: Текущее количество пассажиров
        :param max_passengers: Максимальная вместимость пассажиров
        """
        self.model = model
        self.max_passengers = max_passengers

        # Валидация при создании
        if current_passengers < 0:
            raise ValueError("Количество пассажиров не может быть отрицательным")
        if current_passengers > max_passengers:
            raise ValueError("Текущее количество пассажиров не может превышать максимальное")

        self.current_passengers = current_passengers

    def __str__(self):
        """Строковое представление самолета."""
        return (f"Airplane(model='{self.model}', "
                f"passengers={self.current_passengers}/{self.max_passengers})")

    def __repr__(self):
        """Официальное представление для отладки."""
        return f"Airplane('{self.model}', {self.current_passengers}, {self.max_passengers})"

    # ==========================================
    # 1. Проверка на равенство типов самолетов (==)
    # ==========================================
    def __eq__(self, other):
        """
        Сравнивает типы (модели) самолетов.
        Два самолета равны, если у них одинаковая модель.
        """
        if isinstance(other, Airplane):
            return self.model == other.model
        return NotImplemented

    # ==========================================
    # 2. Увеличение и уменьшение пассажиров (+, -, +=, -=)
    # ==========================================

    def __add__(self, other):
        """
        Возвращает НОВЫЙ самолет с увеличенным количеством пассажиров.
        Исходный объект не изменяется.
        :param other: Число (пассажиры) или объект Airplane (пассажиры другого самолета)
        """
        if isinstance(other, (int, float)):
            new_passengers = self.current_passengers + int(other)
        elif isinstance(other, Airplane):
            new_passengers = self.current_passengers + other.current_passengers
        else:
            return NotImplemented

        # Создаем новый объект с тем же типом и макс. вместимостью
        return Airplane(self.model, new_passengers, self.max_passengers)

    def __sub__(self, other):
        """
        Возвращает НОВЫЙ самолет с уменьшенным количеством пассажиров.
        Исходный объект не изменяется.
        """
        if isinstance(other, (int, float)):
            new_passengers = self.current_passengers - int(other)
        elif isinstance(other, Airplane):
            new_passengers = self.current_passengers - other.current_passengers
        else:
            return NotImplemented

        return Airplane(self.model, new_passengers, self.max_passengers)

    def __iadd__(self, other):
        """
        Увеличивает количество пассажиров в ТЕКУЩЕМ самолете (+=).
        """
        if isinstance(other, (int, float)):
            self.current_passengers += int(other)
        elif isinstance(other, Airplane):
            self.current_passengers += other.current_passengers
        else:
            return NotImplemented

        self._validate_passengers()
        return self

    def __isub__(self, other):
        """
        Уменьшает количество пассажиров в ТЕКУЩЕМ самолете (-=).
        """
        if isinstance(other, (int, float)):
            self.current_passengers -= int(other)
        elif isinstance(other, Airplane):
            self.current_passengers -= other.current_passengers
        else:
            return NotImplemented

        self._validate_passengers()
        return self

    def _validate_passengers(self):
        """Внутренний метод проверки корректности количества пассажиров."""
        if self.current_passengers < 0:
            raise ValueError("Количество пассажиров не может быть отрицательным")
        if self.current_passengers > self.max_passengers:
            raise ValueError(f"Количество пассажиров не может превышать максимальное ({self.max_passengers})")

    # ==========================================
    # 3. Сравнение по максимальной вместимости (>, <, <=, >=)
    # ==========================================

    def __lt__(self, other):
        """Меньше ли максимальная вместимость текущего самолета."""
        if isinstance(other, Airplane):
            return self.max_passengers < other.max_passengers
        return NotImplemented

    def __le__(self, other):
        """Меньше или равно."""
        if isinstance(other, Airplane):
            return self.max_passengers <= other.max_passengers
        return NotImplemented

    def __gt__(self, other):
        """Больше ли максимальная вместимость текущего самолета."""
        if isinstance(other, Airplane):
            return self.max_passengers > other.max_passengers
        return NotImplemented

    def __ge__(self, other):
        """Больше или равно."""
        if isinstance(other, Airplane):
            return self.max_passengers >= other.max_passengers
        return NotImplemented


# ==========================================
# Примеры использования
# ==========================================

if __name__ == "__main__":
    print("=== Создание самолетов ===")
    a1 = Airplane("Boeing 737", 100, 180)
    a2 = Airplane("Boeing 737", 150, 180)  # Та же модель
    a3 = Airplane("Airbus A320", 120, 200)  # Другая модель, больше вместимость
    a4 = Airplane("Boeing 777", 200, 400)  # Большая вместимость

    print(a1)
    print(a2)
    print(a3)
    print(a4)

    print("\n=== 1. Проверка на равенство типов (==) ===")
    print(f"a1 == a2 (одинаковая модель Boeing 737): {a1 == a2}")  # True
    print(f"a1 == a3 (разные модели): {a1 == a3}")  # False

    print("\n=== 2. Увеличение/уменьшение пассажиров (+, -) ===")
    # Операции возвращают новый объект
    a_new = a1 + 50
    print(f"{a1} + 50 пассажиров = {a_new}")
    print(f"Исходный a1 не изменился: {a1}")

    a_new2 = a1 + a3  # Сумма пассажиров двух самолетов
    print(f"{a1} + {a3} (пассажиры) = {a_new2}")

    a_new3 = a1 - 30
    print(f"{a1} - 30 пассажиров = {a_new3}")

    print("\n=== 2.1. Изменение текущего объекта (+=, -=) ===")
    print(f"Было a1: {a1}")
    a1 += 40
    print(f"a1 += 40: {a1}")  # 140/180
    a1 -= 20
    print(f"a1 -= 20: {a1}")  # 120/180

    print("\n=== 2.2. Обработка ошибок (превышение вместимости) ===")
    try:
        a5 = Airplane("Boeing 737", 100, 180)
        a5 += 100  # Попытка сделать 200 пассажиров при макс 180
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n=== 2.3. Обработка ошибок (отрицательные пассажиры) ===")
    try:
        a6 = Airplane("Boeing 737", 50, 180)
        a6 -= 100  # Попытка сделать -50 пассажиров
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n=== 3. Сравнение по максимальной вместимости (>, <, <=, >=) ===")
    print(f"a3.max ({a3.max_passengers}) > a1.max ({a1.max_passengers}): {a3 > a1}")  # True (200 > 180)
    print(f"a1.max ({a1.max_passengers}) < a4.max ({a4.max_passengers}): {a1 < a4}")  # True (180 < 400)
    print(f"a1.max ({a1.max_passengers}) >= a2.max ({a2.max_passengers}): {a1 >= a2}")  # True (180 >= 180)
    print(f"a3.max ({a3.max_passengers}) <= a4.max ({a4.max_passengers}): {a3 <= a4}")  # True (200 <= 400)

    # Поиск самолета с максимальной вместимостью
    airplanes = [a1, a3, a4]
    biggest = max(airplanes)
    print(f"\nСамолет с наибольшей вместимостью: {biggest}")