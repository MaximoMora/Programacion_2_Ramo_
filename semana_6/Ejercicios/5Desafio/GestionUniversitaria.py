

class Persona():
    
    def __init__(self,nombre,apellido,fecha_de_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_de_nacimiento = fecha_de_nacimiento
        
    def Presentacion(self):
        print(f"Nombre:{self.nombre}\nApellido:{self.apellido}\nFecha:{self.fecha_de_nacimiento}")
        
        
class Estudiante(Persona):
    
    def __init__(self,nombre,apellido,fecha_de_nacimiento,matricula,carrera,semestre):
        super().__init__(nombre,apellido,fecha_de_nacimiento)
        self.matricula = matricula
        self.carrera = carrera
        self.semestre = semestre
        
    def Estudiar(self,materia,horas):
        print(f"El estudiante:{self.nombre}\nestudio {horas}\nla materia {materia}")
        
    def Presentacion(self):
        print(f"Estudiante:{self.nombre}\nApellido:{self.apellido}\nFecha:{self.fecha_de_nacimiento}\nEstudia:{self.carrera}\nSemestre:{self.semestre}")
        

class Profesor(Persona):
    
    def __init__(self,nombre,apellido,fecha_de_nacimiento,número_empleado,departamento):
        super().__init__(nombre,apellido,fecha_de_nacimiento)
        self.número_empleado = número_empleado
        self.departamento = departamento
        
    def Enseñar(self,materia ):
        
    def Presentacion(self):
        print(f"Estudiante:{self.nombre}\nApellido:{self.apellido}\nFecha:{self.fecha_de_nacimiento}\nEstudia:{self.carrera}\nSemestre:{self.semestre}")
        
        
class Asignatura
        
        
        
