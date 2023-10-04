
class BankAccount():

    def __init__(self,name,money):
        self.name = name
        self.money = money

    def Status(self):
        print(f"name: {self.name} money: {self.money}")

    def Deposit(self,amount):
        self.money += amount

    def Withdraval(self,amount):
        if self.money - amount < 0:
            print("insufficient funds")
        else:
            self.money -= amount



kevin = BankAccount("kevin",100)
kevin.Status()
kevin.Withdraval(150)
kevin.Status()


