

class Empleado():

    def __init__(self,nombre,edad,salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

class Gerente(Empleado):
    def __init__(self,nombre,edad,salario,liderazgo,grupos):
        super().__init__(nombre,edad,salario)
        self.liderazgo = liderazgo
        self.grupos = []

    def MostrarManejoDeGrupos(self):
        print(f"grupos: {self.grupos}")


class Ingeniero(Empleado):
    def __init__(self,nombre,edad,salario,tecnicatura,creatividad):
        super().__init__(nombre,edad,salario)
        self.tecnicatura = tecnicatura
        self.creatividad = creatividad


class Asistente(Empleado):
    def __init__(self,nombre,edad,salario,tareas,citas):
        super().__init__(nombre,edad,salario)
        self.tareas = tareas
        self.citas = citas

