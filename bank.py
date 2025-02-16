class Account():

    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Вы пополнили счет. Сумма на счете -  {self.balance}")


    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств")
        elif amount <=self.balance:
            self.balance -= amount
            print(f"Вы сняли деньги. Сумма на счете - {self.balance}")

    def get_balance(self):
        print(f"Сумма на счете - {self.balance}")

man = Account("Ivan", 0)


man.deposit(100)
man.withdraw(50)
man.withdraw(100)
man.deposit(10000)
man.get_balance()
