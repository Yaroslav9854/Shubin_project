import math


class Circle:
    def __init__(self, radius):
        """Инициализация окружности с заданным радиусом."""
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        self.radius = radius

    def get_length(self):
        """Возвращает длину окружности (C = 2 * pi * r)."""
        return 2 * math.pi * self.radius

    def __str__(self):
        """Строковое представление объекта для удобного вывода."""
        return f"Circle(radius={self.radius}, length={self.get_length():.2f})"

    # 1. Проверка на равенство радиусов (==)
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    # 2. Сравнения длин окружностей (>, <, <=, >=)
    # Так как длина L = 2 * pi * R, сравнение длин эквивалентно сравнению радиусов.

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Circle):
            return self.radius <= other.radius
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.radius >= other.radius
        return NotImplemented

    # 3. Пропорциональное изменение размеров (+, -, +=, -=)
    # Операции + и - должны возвращать НОВЫЙ объект (неизменяемость)
    # Операции += и -= должны изменять ТЕКУЩИЙ объект

    def __add__(self, other):
        """Возвращает новую окружность с увеличенным радиусом."""
        if isinstance(other, (int, float)):
            return Circle(self.radius + other)
        elif isinstance(other, Circle):
            # Если складываем две окружности, суммируем радиусы
            return Circle(self.radius + other.radius)
        return NotImplemented

    def __sub__(self, other):
        """Возвращает новую окружность с уменьшенным радиусом."""
        if isinstance(other, (int, float)):
            return Circle(self.radius - other)
        elif isinstance(other, Circle):
            return Circle(self.radius - other.radius)
        return NotImplemented

    def __iadd__(self, other):
        """Изменяет текущую окружность (увеличение радиуса)."""
        if isinstance(other, (int, float)):
            self.radius += other
        elif isinstance(other, Circle):
            self.radius += other.radius
        else:
            return NotImplemented

        if self.radius < 0:
            raise ValueError("Радиус не может стать отрицательным в результате операции")
        return self

    def __isub__(self, other):
        """Изменяет текущую окружность (уменьшение радиуса)."""
        if isinstance(other, (int, float)):
            self.radius -= other
        elif isinstance(other, Circle):
            self.radius -= other.radius
        else:
            return NotImplemented

        if self.radius < 0:
            raise ValueError("Радиус не может стать отрицательным в результате операции")
        return self


# ==========================================
# Примеры использования
# ==========================================

if __name__ == "__main__":
    c1 = Circle(5)
    c2 = Circle(5)
    c3 = Circle(10)
    c4 = Circle(3)

    print("--- Исходные данные ---")
    print(f"c1: {c1}")
    print(f"c2: {c2}")
    print(f"c3: {c3}")
    print(f"c4: {c4}")

    print("\n--- 1. Проверка на равенство (==) ---")
    print(f"c1 == c2 (радиусы 5 и 5): {c1 == c2}")  # True
    print(f"c1 == c3 (радиусы 5 и 10): {c1 == c3}")  # False

    print("\n--- 2. Сравнение длин (>, <, <=, >=) ---")
    # Так как длина зависит от радиуса, c3 (r=10) больше c1 (r=5)
    print(f"c3 > c1: {c3 > c1}")  # True
    print(f"c1 < c3: {c1 < c3}")  # True
    print(f"c1 >= c2: {c1 >= c2}")  # True
    print(f"c4 <= c1: {c4 <= c1}")  # True

    print("\n--- 3. Изменение размеров (+, -) ---")
    # Операции возвращают новый объект, старые не меняются
    c_new = c1 + 2
    print(f"c1 + 2 -> {c_new}")  # radius=7
    print(f"Исходный c1 остался: {c1}")  # radius=5

    c_diff = c3 - c4
    print(f"c3 - c4 (10 - 3) -> {c_diff}")  # radius=7

    print("\n--- 4. Изменение размеров (+=, -=) ---")
    print(f"Было c4: {c4}")
    c4 += 5
    print(f"c4 += 5 -> {c4}")  # radius=8
    c4 -= 2
    print(f"c4 -= 2 -> {c4}")  # radius=6

    # Пример обработки ошибки (отрицательный радиус)
    try:
        c5 = Circle(5)
        c5 -= 10  # Попытка сделать радиус -5
    except ValueError as e:
        print(f"\nОшибка при вычитании: {e}")