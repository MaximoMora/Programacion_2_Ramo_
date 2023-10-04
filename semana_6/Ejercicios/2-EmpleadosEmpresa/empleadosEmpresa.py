

class Empleado():

    def __init__(self,nombre,edad,salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

class Gerente(Empleado):
    def __init__(self,nombre,edad,salario,liderazgo,grupos):
        super().__init__(nombre,edad,salario)
        self.liderazgo = liderazgo
        self.grupos = grupos

    def describir_rol(self):
        print(f"Gerente\nNombre:{self.nombre}\nSalario:{self.salario}\nLiderazgo:{self.liderazgo}\nGrupos:{self.grupos}")
        
    def MostrarManejoDeGrupos(self):
        print(f"grupos: {self.grupos}")
        
    def SetLiderazgo(self,nuevoLiderazgo):
        self.liderazgo = nuevoLiderazgo


class Ingeniero(Empleado):
    def __init__(self,nombre,edad,salario,tecnicatura):
        super().__init__(nombre,edad,salario)
        self.tecnicatura = tecnicatura
        self.habilidades = []
    
    def describir_rol(self):
        print(f"Ingeniero\nNombre:{self.nombre}\nSalario:{self.salario}\nTecnicatura:{self.tecnicatura}\nHabilidades:{self.habilidades}")
        
    
    def AgregarHabilidar(self,nuevaHabilidad):
        self.habilidades.append(nuevaHabilidad)
               


class Asistente(Empleado):
    def __init__(self,nombre,edad,salario):
        super().__init__(nombre,edad,salario)
        self.tareas = []
        self.citas = []
        
    def describir_rol(self):
        print(f"Asistente\nNombre:{self.nombre}\nSalario:{self.salario}\nTareas:{self.tareas}\nCitas:{self.citas}")
        
    
    def MostrarTareas(self):
        print(f"Tareas:\n{self.tareas}")
        
    def AgregarTarea(self,nuevaTarea):
        self.tareas.append(nuevaTarea)
    
    def EliminarTarea(self,tarea):
        self.tareas.remove(tarea)
        
    def AgregarCita(self,nuevaCita):
        self.citas.append(nuevaCita)
    
    


    

