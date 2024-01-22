class Account:
    def __init__(self, number, cpf, holderName, balance):
        self.balance = balance
        self.cpf = cpf
        self.number = number
        self.holderName = holderName

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        self.balance -= value

    def statement(self):
        print(f"number: {self.number} \ncpf: {self.cpf} \nbalance: {self.balance}")
