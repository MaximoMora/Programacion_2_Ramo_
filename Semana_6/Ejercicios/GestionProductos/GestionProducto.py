

class Producto():
    def __init__(self,nombre,precio,categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria


    def mostrar_detalle(self):
        print(f"Producto = {self.nombre} Precio = {self.precio} Categoria = {self.categoria}")


class Electronico(Producto):

    def __init__(nombre,precio,categoria,consumo):
        super().__init__(nombre,precio,categoria)
        self.consumo = consumo

    def mostrar_detalle(self):
        print(f"Producto = {self.nombre} Precio = {self.precio} Categoria = {self.categoria} Consumo = {self.consumo}")


class Alimenticio(Producto):

    def __init__(nombre,precio,categoria,calorias):
        super().__init__(nombre,precio,categoria)
        self.calorias = calorias

    def mostrar_detalle(self):
        print(f"Producto = {self.nombre} Precio = {self.precio} Categoria = {self.categoria} Calorias = {self.calorias}")


class Vestimenta(Producto):

    def __init__(nombre,precio,categoria,talla):
        super().__init__(nombre,precio,categoria)
        self.talla = talla

    def mostrar_detalle(self):
        print(f"Producto = {self.nombre} Precio = {self.precio} Categoria = {self.categoria} Talla = {self.talla}")
