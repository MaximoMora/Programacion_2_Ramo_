
class Person():
    
    def __init__(self,name,inventory):
        self.name = name
        self.inventory = inventory
        
        
class Inventory():
    
    def __init__(self,name,amount):
        self.name = name
        self.amount = amount
        
    def Increase(self):
        self.amount += 1
        
    def Decrease(self):
        self.amount -= 1
        
        
class Food(Inventory):
    def __init__(self, name, amount,taste):
        super().__init__(name, amount)
        self.taste = taste
        

