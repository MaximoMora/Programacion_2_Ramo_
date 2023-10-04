

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
        
    def Enseñar(self,materia):
        print(f"Profesor enseña la materia:{materia}")
        
    def Presentacion(self):
        print(f"Estudiante:{self.nombre}\nApellido:{self.apellido}\nFecha:{self.fecha_de_nacimiento}\nEstudia:{self.carrera}\nSemestre:{self.semestre}")
        
        
class Asignatura:
    def __init__(self,nombre,codigo,creditos):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}Codigo: {self.codigo} Creditos: {self.creditos}")
        
class Grupo:
    def __init__(self,número_grupo,asignatura ,profesor,estudiantes):
        self.número_grupo = número_grupo
        self.asignatura = asignatura
        self.profesor = profesor
        self.estudiantes = []
        
    def agregar_estudiante(self,estudiante):
        self.estudiantes.append(estudiante)
    
    def eliminar_estudiante(self,estudiante):
        self.estudiantes.remove(estudiante)
        
    def mostrar_grupo(self):
        print(f"Profesor:{self.profesor}")
        for i in range(len(self.estudiantes)):
            print(i)

        

class ProgramaAcademico:
    def __init__(self,nombre,codigo,grupos):
        self.nombre = nombre
        self.codigo = codigo
        self.grupos = []
        
    def agregar_grupo(self,grupo):
        self.grupos.append(grupo)
    
    def eliminar_grupo(self,grupo):
        self.grupos.remove(grupo)
        
    def mostrar_programa(self):
        for i in range(len(self.grupos)):
            print(i)