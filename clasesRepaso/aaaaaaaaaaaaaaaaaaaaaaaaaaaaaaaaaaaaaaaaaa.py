

class Hospital():
    def __init__(self,administracion,salas):
        self.administracion = administracion
        self.salas = salas
        self.medicinas = []
        self.equipos = []
        self.medicos = []
        self.enfermeros = []
        self.pacientes = []
        
    
    def AgregaMedico(self,medico):
        self.medicos.append(medico)
        
    def buscarMedico(self,id):
        
        
        for i in range(len(self.medicos)):
            for j in range(len(self.medicos)-1-i):
                if self.medicos[j+1].id > self.medicos[j].id:
                    
                    self.medicos[j+1],self.medicos[j] = self.medicos[j], self.medicos[j+1]
                    
        high = len(self.medicos)-1
        low = 0
        med = (high+low) //2
        while self.medicos[med].id != id:
            if self.medicos[med].id > id:
                
                high = med
            else:
                low = med
                
        print(self,  self.medicos[med].nombre)
                
class Persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
class Medico(Persona):
    def __init__(self,nombre,edad,id,especialidad,sueldo):
        super().__init__(nombre,edad)
        self.id = id
        self.especialidad = especialidad
        self.sueldo = sueldo
        
class Paciente(Persona):
    def __init__(self,nombre,edad,ingreso,dianostico,tratamiento,alta,gestion,sala):
        super().__init__(nombre,edad)
        self.ingreso = ingreso
        self.dianostico = dianostico
        self.tratamiento = tratamiento
        self.alta = alta
        self.gestio = gestion
        self.sala = sala
        
        
if __name__ == '__main__':
    kevin = Medico("Kevin",20,0,"Medico General",300)
    esteban = Medico("Esteban",18,1,"Podologo",2000)
    
    HospitalEsteban = Hospital([{
        "Director" : "Manuel Robles",
        "Secretaria" : "Camila Diaz"
    }],
    [{
        "Sala_01" : "Sala Directorio",
        "Sala_02" : "Sala Secretaria"
    }])

    HospitalEsteban.AgregaMedico(kevin)
    HospitalEsteban.AgregaMedico(esteban)
    HospitalEsteban.buscarMedico(1)
