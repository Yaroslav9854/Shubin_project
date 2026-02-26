class Complex:
    def __init__(self, real, imag):
        """
        Инициализация комплексного числа.
        :param real: Вещественная часть (a)
        :param imag: Мнимая часть (b)
        Формат: a + bi
        """
        self.real = real
        self.imag = imag

    def __str__(self):
        """
        Красивое строковое представление числа.
        Обрабатывает знаки для мнимой части (например, 5 - 3i вместо 5 + -3i).
        """
        if self.imag == 0:
            return f"{self.real}"
        if self.real == 0:
            return f"{self.imag}i"

        if self.imag > 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"

    def __repr__(self):
        """Официальное представление для отладки."""
        return f"Complex({self.real}, {self.imag})"

    # Вспомогательный метод для приведения другого операнда к типу Complex
    # Это позволяет складывать/умножать с обычными числами (int, float)
    def _to_complex(self, other):
        if isinstance(other, Complex):
            return other
        elif isinstance(other, (int, float)):
            return Complex(other, 0)
        else:
            raise TypeError("Операнд должен быть числом или объектом Complex")

    # 1. Сложение (+)
    # (a + bi) + (c + di) = (a + c) + (b + d)i
    def __add__(self, other):
        other = self._to_complex(other)
        return Complex(self.real + other.real, self.imag + other.imag)

    # Обратное сложение (чтобы работало 5 + complex_obj)
    def __radd__(self, other):
        return self.__add__(other)

    # 2. Вычитание (-)
    # (a + bi) - (c + di) = (a - c) + (b - d)i
    def __sub__(self, other):
        other = self._to_complex(other)
        return Complex(self.real - other.real, self.imag - other.imag)

    # Обратное вычитание (чтобы работало 5 - complex_obj)
    def __rsub__(self, other):
        other = self._to_complex(other)
        # other - self
        return Complex(other.real - self.real, other.imag - self.imag)

    # 3. Умножение (*)
    # (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
    def __mul__(self, other):
        other = self._to_complex(other)
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)

    def __rmul__(self, other):
        return self.__mul__(other)

    # 4. Деление (/)
    # (a + bi) / (c + di) = [(ac + bd) + (bc - ad)i] / (c^2 + d^2)
    def __truediv__(self, other):
        other = self._to_complex(other)
        denominator = other.real ** 2 + other.imag ** 2

        if denominator == 0:
            raise ZeroDivisionError("Деление на ноль (комплексное число равно 0)")

        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real_part, imag_part)

    # Обратное деление (чтобы работало 5 / complex_obj)
    def __rtruediv__(self, other):
        other = self._to_complex(other)
        return other.__truediv__(self)

    # Проверка на равенство (для удобства тестирования)
    def __eq__(self, other):
        if isinstance(other, Complex):
            return self.real == other.real and self.imag == other.imag
        return False


# ==========================================
# Примеры использования
# ==========================================

if __name__ == "__main__":
    print("--- Создание комплексных чисел ---")
    c1 = Complex(3, 4)  # 3 + 4i
    c2 = Complex(1, -2)  # 1 - 2i
    c3 = Complex(2, 0)  # 2 (вещественное)

    print(f"c1 = {c1}")
    print(f"c2 = {c2}")
    print(f"c3 = {c3}")

    print("\n--- 1. Сложение (+) ---")
    res_add = c1 + c2
    print(f"{c1} + {c2} = {res_add}")
    # (3+1) + (4-2)i = 4 + 2i

    print("\n--- 2. Вычитание (-) ---")
    res_sub = c1 - c2
    print(f"{c1} - {c2} = {res_sub}")
    # (3-1) + (4 - (-2))i = 2 + 6i

    print("\n--- 3. Умножение (*) ---")
    res_mul = c1 * c2
    print(f"{c1} * {c2} = {res_mul}")
    # Real: 3*1 - 4*(-2) = 3 + 8 = 11
    # Imag: 3*(-2) + 4*1 = -6 + 4 = -2
    # Результат: 11 - 2i

    print("\n--- 4. Деление (/) ---")
    res_div = c1 / c2
    print(f"{c1} / {c2} = {res_div}")
    # Знаменатель: 1^2 + (-2)^2 = 5
    # Real: (3*1 + 4*(-2)) / 5 = (3 - 8) / 5 = -1.0
    # Imag: (4*1 - 3*(-2)) / 5 = (4 + 6) / 5 = 2.0
    # Результат: -1.0 + 2.0i

    print("\n--- 5. Операции с обычными числами ---")
    print(f"{c1} + 5 = {c1 + 5}")  # 8 + 4i
    print(f"10 - {c1} = {10 - c1}")  # 7 - 4i
    print(f"{c1} * 2 = {c1 * 2}")  # 6 + 8i

    print("\n--- 6. Обработка ошибки деления на ноль ---")
    c_zero = Complex(0, 0)
    try:
        res_err = c1 / c_zero
    except ZeroDivisionError as e:
        print(f"Ошибка: {e}")