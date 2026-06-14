class BankAccount:
    def __init__(self, initial: int):
        self.__balance = initial

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount: int) -> None:
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount: int) -> bool:
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            return True
        return False