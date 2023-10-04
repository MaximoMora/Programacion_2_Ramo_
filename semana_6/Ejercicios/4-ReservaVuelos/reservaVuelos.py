

class Reserva():
    def __init__(self,nombre_del_pasajero,número_de_vuelo,fecha):
        self.nombre_del_pasajero = nombre_del_pasajero
        self.número_de_vuelo = número_de_vuelo
        self.fecha = fecha
        
    def mostrar_detalle(self):
        print(f"Reserva:\nNombre:{self.nombre_del_pasajero}\nNumero de vuelo:{self.número_de_vuelo}\nFecha {self.fecha}")
        
class ReservaEconómica(Reserva):
    def __init__(self, nombre_del_pasajero, número_de_vuelo, fecha,comida_basica,espacio_limitado):
        super().__init__(nombre_del_pasajero, número_de_vuelo, fecha)
        self.comida_basica = comida_basica
        self.espacio_limitado = espacio_limitado
        
    def mostrar_detalle(self):
        print(f"Reserva Economica:\nNombre: {self.nombre_del_pasajero}\nNumero de vuelo: {self.número_de_vuelo}\nFecha: {self.fecha}\nTipo de comida: {self.comida_basica}\nTipo de espacio: {self.espacio_limitado}")
    
    
        
class ReservaBusiness(Reserva):
    def __init__(self, nombre_del_pasajero, número_de_vuelo, fecha,comida_gourmet,espacio_amplio,entretenimiento):
        super().__init__(nombre_del_pasajero, número_de_vuelo, fecha)
        self.comida_gourmet = comida_gourmet
        self.espacio_amplio = espacio_amplio
        self.entretenimiento = entretenimiento
        
    def mostrar_detalle(self):
        print(f"Reserva Business:\nNombre: {self.nombre_del_pasajero}\nNumero de vuelo: {self.número_de_vuelo}\nFecha: {self.fecha}\nTipo de comida: {self.comida_gourmet}\nTipo de espacio: {self.espacio_amplio}\nTipo de Entrenimiento: {self.entretenimiento}")


class ReservaPrimeraClase(Reserva):
    def __init__(self, nombre_del_pasajero,número_de_vuelo, fecha,comida_gourmet_exclusiva,espacio_habitacion,entretenimiento_premiun,privacidad,sala_vip):
        super().__init__(nombre_del_pasajero, número_de_vuelo, fecha)
        self.comida_gourmet_exclusiva = comida_gourmet_exclusiva
        self.espacio_habitacion = espacio_habitacion
        self.privacidad = privacidad
        self.entretenimiento_premiun = entretenimiento_premiun
        self.sala_vip = sala_vip
        
    def mostrar_detalle(self):
        print(f"Reserva Primera Clase:\nNombre: {self.nombre_del_pasajero}\nNumero de vuelo: {self.número_de_vuelo}\nFecha: {self.fecha}\nTipo de comida: {self.comida_gourmet_exclusiva}\nTipo de espacio: {self.espacio_habitacion}\nTipo de Entrenimiento: {self.entretenimiento}\nPrivacidad:{self.privacidad}\nSala Vip:{self.sala_vip}")

        

        