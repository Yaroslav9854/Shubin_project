class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        """Инициализация банковского счета с владельцем и начальным балансом."""
        self.__owner = owner
        self.__balance = max(initial_balance, 0.0)  # Гарантируем неотрицательный начальный баланс

    def deposit(self, amount: float) -> None:
        """
        Пополнение счета на указанную сумму.

        Args:
            amount: Сумма для пополнения

        Raises:
            ValueError: Если сумма отрицательная
        """
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Снятие средств со счета.

        Args:
            amount: Сумма для снятия

        Raises:
            ValueError: Если сумма отрицательная или недостаточно средств
        """
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self.__balance:
            raise ValueError("Недостаточно средств на счете")
        self.__balance -= amount

    def get_balance(self) -> float:
        """
        Возвращает текущий баланс счета.

        Returns:
            Текущий баланс
        """
        return self.__balance

    def get_owner(self) -> str:
        """
        Возвращает имя владельца счета.

        Returns:
            Имя владельца
        """
        return self.__owner

    def __str__(self) -> str:
        """
        Строковое представление счета.

        Returns:
            Строка с информацией о счете
        """
        return f"BankAccount(Владелец: '{self.__owner}', Баланс: {self.__balance:.2f})"

if __name__ == "__main__":
# Пример 5: Несколько счетов
    print("\n=== Пример 5: Работа с несколькими счетами ===")
    account1 = BankAccount("Иван Сидоров", 2000.0)
    account2 = BankAccount("Мария Иванова", 1500.0)
    print(f"Счет 1: {account1.get_owner()} - {account1.get_balance():.2f}")
    print(f"Счет 2: {account2.get_owner()} - {account2.get_balance():.2f}")