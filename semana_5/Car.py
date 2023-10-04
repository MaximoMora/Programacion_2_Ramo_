
class Car:
    
    def __init__(self):
        self.__brand = ""
        self.__model = ""
        self.__year = ""
        
    def setBrand(self,brand):
        self.__brand = brand
        
    def getBrand(self):
        return self.__brand
    
    def Status(self):
        print(f"brand: {self.__brand}")
        
Toyota = Car()
Toyota.setBrand("Toyota")

Toyota.Status()

        