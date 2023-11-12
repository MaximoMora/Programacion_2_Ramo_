import simpy

# Define un entorno de simulación
env = simpy.Environment()

# Define un proceso que simule la llegada de un cliente cada 2 unidades de tiempo
def llegada_cliente(env):
    while True:
        print(f"Llega un cliente en el tiempo {env.now}")
        yield env.timeout(2)

# Agrega el proceso al entorno de simulación
env.process(llegada_cliente(env))

# Ejecuta la simulación durante 5 unidades de tiempo
env.run(until=5)
