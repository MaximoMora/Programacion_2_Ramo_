

class Animal():

    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def Sonido(self):
        print(f"{self.nombre} hace un sonido")

class Perro(Animal):

    def __init__(self,nombre,edad):
        super().__init__(nombre,edad)
    
    def Sonido(self):
        print(f"{self.nombre} dice wauuu")

class Gato(Animal):

    def __init__(self,nombre,edad):
        super().__init__(nombre,edad)
    
    def Sonido(self):
        print(f"{self.nombre} dice miau")


class Pajaro(Animal):

    def __init__(self,nombre,edad):
        super().__init__(nombre,edad)
    
    def Sonido(self):
        print(f"{self.nombre} dice pio pio pio")


__