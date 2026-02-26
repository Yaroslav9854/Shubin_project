class Flat:
    def __init__(self, address, area, price):
        """
        Инициализация квартиры.
        :param address: Адрес квартиры (строка)
        :param area: Площадь квартиры в квадратных метрах (число)
        :param price: Цена квартиры (число)
        """
        self.address = address

        # Валидация данных
        if area <= 0:
            raise ValueError("Площадь квартиры должна быть положительным числом")
        if price <= 0:
            raise ValueError("Цена квартиры должна быть положительным числом")

        self.area = area
        self.price = price

    def __str__(self):
        """Строковое представление квартиры для вывода."""
        return (f"Flat(address='{self.address}', "
                f"area={self.area} м², price={self.price:,.0f} руб.)")

    def __repr__(self):
        """Официальное представление для отладки."""
        return f"Flat('{self.address}', {self.area}, {self.price})"

    # ==========================================
    # 1. Проверка на равенство площадей (==)
    # ==========================================
    def __eq__(self, other):
        """
        Сравнивает площади двух квартир.
        Квартиры равны, если их площади одинаковы.
        """
        if isinstance(other, Flat):
            return self.area == other.area
        return NotImplemented

    # ==========================================
    # 2. Проверка на неравенство площадей (!=)
    # ==========================================
    def __ne__(self, other):
        """
        Сравнивает площади двух квартир на неравенство.
        Квартиры не равны, если их площади различаются.
        """
        if isinstance(other, Flat):
            return self.area != other.area
        return NotImplemented

    # ==========================================
    # 3. Сравнение по цене (>, <, <=, >=)
    # ==========================================

    def __lt__(self, other):
        """Меньше ли цена текущей квартиры."""
        if isinstance(other, Flat):
            return self.price < other.price
        return NotImplemented

    def __le__(self, other):
        """Меньше или равна ли цена текущей квартиры."""
        if isinstance(other, Flat):
            return self.price <= other.price
        return NotImplemented

    def __gt__(self, other):
        """Больше ли цена текущей квартиры."""
        if isinstance(other, Flat):
            return self.price > other.price
        return NotImplemented

    def __ge__(self, other):
        """Больше или равна ли цена текущей квартиры."""
        if isinstance(other, Flat):
            return self.price >= other.price
        return NotImplemented

    # ==========================================
    # Дополнительные полезные методы
    # ==========================================

    def price_per_meter(self):
        """Возвращает цену за квадратный метр."""
        return self.price / self.area


# ==========================================
# Примеры использования
# ==========================================

if __name__ == "__main__":
    print("=== Создание квартир ===")
    f1 = Flat("ул. Ленина, 10, кв. 5", 45.5, 5500000)
    f2 = Flat("ул. Пушкина, 25, кв. 12", 45.5, 6200000)  # Такая же площадь
    f3 = Flat("ул. Гагарина, 8, кв. 3", 60.0, 7500000)  # Больше площадь и цена
    f4 = Flat("ул. Чехова, 15, кв. 8", 38.0, 4800000)  # Меньше площадь и цена

    print(f1)
    print(f2)
    print(f3)
    print(f4)

    print("\n=== 1. Проверка на равенство площадей (==) ===")
    print(f"f1.area ({f1.area} м²) == f2.area ({f2.area} м²): {f1 == f2}")  # True
    print(f"f1.area ({f1.area} м²) == f3.area ({f3.area} м²): {f1 == f3}")  # False
    print(f"f3.area ({f3.area} м²) == f4.area ({f4.area} м²): {f3 == f4}")  # False

    print("\n=== 2. Проверка на неравенство площадей (!=) ===")
    print(f"f1.area ({f1.area} м²) != f2.area ({f2.area} м²): {f1 != f2}")  # False
    print(f"f1.area ({f1.area} м²) != f3.area ({f3.area} м²): {f1 != f3}")  # True
    print(f"f3.area ({f3.area} м²) != f4.area ({f4.area} м²): {f3 != f4}")  # True

    print("\n=== 3. Сравнение по цене (>, <, <=, >=) ===")
    print(f"f2.price ({f2.price:,.0f}) > f1.price ({f1.price:,.0f}): {f2 > f1}")  # True
    print(f"f4.price ({f4.price:,.0f}) < f1.price ({f1.price:,.0f}): {f4 < f1}")  # True
    print(f"f1.price ({f1.price:,.0f}) <= f2.price ({f2.price:,.0f}): {f1 <= f2}")  # True
    print(f"f3.price ({f3.price:,.0f}) >= f2.price ({f2.price:,.0f}): {f3 >= f2}")  # True
    print(f"f1.price ({f1.price:,.0f}) >= f2.price ({f2.price:,.0f}): {f1 >= f2}")  # False

    print("\n=== Дополнительные возможности ===")
    print(f"Цена за м² для f1: {f1.price_per_meter():,.2f} руб./м²")
    print(f"Цена за м² для f2: {f2.price_per_meter():,.2f} руб./м²")
    print(f"Цена за м² для f3: {f3.price_per_meter():,.2f} руб./м²")

    print("\n=== Поиск самой дорогой и дешевой квартиры ===")
    flats = [f1, f2, f3, f4]
    most_expensive = max(flats)
    cheapest = min(flats)
    print(f"Самая дорогая: {most_expensive}")
    print(f"Самая дешевая: {cheapest}")

    print("\n=== Сортировка квартир по цене ===")
    sorted_flats = sorted(flats)
    print("Квартиры от дешевой к дорогой:")
    for i, flat in enumerate(sorted_flats, 1):
        print(f"{i}. {flat}")

    print("\n=== Обработка ошибок ===")
    try:
        f_error = Flat("ул. Ошибочная, 1", -50, 5000000)
    except ValueError as e:
        print(f"Ошибка при создании: {e}")

    try:
        f_error2 = Flat("ул. Ошибочная, 2", 50, -1000000)
    except ValueError as e:
        print(f"Ошибка при создании: {e}")