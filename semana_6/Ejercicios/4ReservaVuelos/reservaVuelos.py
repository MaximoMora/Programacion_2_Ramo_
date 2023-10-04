

class Reserva():
    def __init__(self,nombre_del_pasajero,número_de_vuelo,fecha):
        self.nombre_del_pasajero = nombre_del_pasajero
        self.número_de_vuelo = número_de_vuelo
        self.fecha = fecha
        
    def Mostrar_detalle(self):
        print(f"Reserva:\nNombre:{self.nombre_del_pasajero}\nNumero de vuelo:{self.número_de_vuelo}\nFecha {self.fecha}")
        
class ReservaEconómica(Reserva):
    def __init__(self, nombre_del_pasajero, número_de_vuelo, fecha,comida_basica):
        super().__init__(nombre_del_pasajero, número_de_vuelo, fecha)
        self.comida_basica = comida_basica
        self.equipaje_limitado = []
        
    def Mostrar_detalle(self):
        print(f"Reserva Economica:\nNombre: {self.nombre_del_pasajero}\nNumero de vuelo: {self.número_de_vuelo}\nFecha: {self.fecha}\nTipo de comida: {self.comida_basica}\nTipo de espacio: {self.espacio_limitado}")
    
    def AgregarEquipaje(self,nuevoEquipaje):
        self.espacio_limitado.append(nuevoEquipaje) 
        
    
        
class ReservaBusiness(Reserva):
    def __init__(self, nombre_del_pasajero, número_de_vuelo, fecha,comida_gourmet):
        super().__init__(nombre_del_pasajero, número_de_vuelo, fecha)
        self.comida_gourmet = comida_gourmet
        self.espacio_amplio = []
        self.entretenimiento = []
        self.equipaje = []
        
    def Mostrar_detalle(self):
        print(f"Reserva Business:\nNombre: {self.nombre_del_pasajero}\nNumero de vuelo: {self.número_de_vuelo}\nFecha: {self.fecha}\nTipo de comida: {self.comida_gourmet}\nTipo de espacio: {self.espacio_amplio}\nTipo de Entrenimiento: {self.entretenimiento}")

    def BusPremium(self):
        print(f"El pasajero: {self.nombre_del_pasajero} Sera llevado al aeropuerto por un Bus Premium")
        
    def SetMenuGourmet(self,nuevaComida):
        self.comida_gourmet = nuevaComida
    
    def AgregarEntretenimiento(self,nuevoEntretenimiento):
        self.entretenimiento.append(nuevoEntretenimiento)
        
        

class ReservaPrimeraClase(Reserva):
    def __init__(self, nombre_del_pasajero,número_de_vuelo, fecha,comida_gourmet_exclusiva,espacio_habitacion,privacidad,sala_vip):
        super().__init__(nombre_del_pasajero, número_de_vuelo, fecha)
        self.comida_gourmet_exclusiva = comida_gourmet_exclusiva
        self.espacio_habitacion = espacio_habitacion
        self.privacidad = privacidad
        self.entretenimiento_premiun = []
        self.sala_vip = sala_vip
        self.equipaje_amplio = []
        
    def Mostrar_detalle(self):
        print(f"Reserva Primera Clase:\nNombre: {self.nombre_del_pasajero}\nNumero de vuelo: {self.número_de_vuelo}\nFecha: {self.fecha}\nTipo de comida: {self.comida_gourmet_exclusiva}\nTipo de espacio: {self.espacio_habitacion}\nTipo de Entrenimiento: {self.entretenimiento}\nPrivacidad:{self.privacidad}\nSala Vip:{self.sala_vip}")

    def ConductorPrivado(self):
        print(f"El pasajero: {self.nombre_del_pasajero} Sera llevado al aeropuert por un conductor privado")
    
    def SetcomidaGourmetExclusiva(self,nuevaComida):
        self.comida_gourmet_exclusiva = nuevaComida
      
    def AgregarEntrenimiento(self,nuevoEntrenimiento):
        self.entretenimiento_premiun.append(nuevoEntrenimiento)
        
    def SetSalaVip(self,nuevaSala):
        self.sala_vip = nuevaSala
        