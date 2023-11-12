import simpy
import random

class Cliente(simpy.Process):
    def __init__(self, env, tiempo_servicio):
        super().__init__(env=env)
        self.tiempo_servicio = tiempo_servicio

    def run(self):
        # Llega al sistema
        print("Cliente llega al sistema")

        # Espera a ser atendido
        with self.env.resource(caja):
            print("Cliente es atendido")
            # Se atiende durante un tiempo aleatorio
            yield self.env.timeout(self.tiempo_servicio)

        # Se retira del sistema
        print("Cliente se retira del sistema tras {} segundos".format(self.tiempo_servicio))


env = simpy.Environment()

# Crea una caja con una sola posición
caja = simpy.Resource(env, capacity=1)

# Crea 10 clientes
for i in range(10):
    env.process(Cliente(env, random.uniform(1, 5)))

# Ejecuta la simulación
env.run()
