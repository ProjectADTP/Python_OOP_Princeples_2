class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
        print("Счёт успешно открыт!")
        self.check_balance()

    def deposit(self, amount):
        self.__balance += amount
        print("Пополнение успешно! Баланс:", self.__balance)

    def try_withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Успешно! Остаток баланса:", self.__balance)
        else:
            print("Ошибка! Недостаточно средств для снятия!")

    def check_balance(self):
        print("Текущий баланс:", self.__balance)


def main():
    bank = BankAccount(100)
    bank.deposit(50)
    bank.try_withdraw(20)
    bank.try_withdraw(200)
    bank.check_balance()
    bank.try_withdraw(130)


if __name__ == "__main__":
    main()
