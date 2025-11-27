#Bank account
class Bankacc:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance+amt
b=Bankacc(1000)
b.deposit(500)
print(b.balance)
