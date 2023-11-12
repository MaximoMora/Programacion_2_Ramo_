import random
import matplotlib.pyplot as plt
import numpy as np

# Tamaño del mapa
width = 50
height = 50

# Crear un mapa vacío
biome_map = np.zeros((width, height))

# Definir tipos de biomas
BIOME_GRASS = 1
BIOME_FOREST = 2
BIOME_DESERT = 3

# Generar biomas aleatorios
for x in range(width):
    for y in range(height):
        rand_value = random.uniform(0, 1)
        
        if rand_value < 0.4:
            biome_map[x, y] = BIOME_GRASS
        elif rand_value < 0.8:
            biome_map[x, y] = BIOME_FOREST
        else:
            biome_map[x, y] = BIOME_DESERT

# Visualizar el mapa de biomas
print(biome_map)
plt.imshow(biome_map, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.title("Biome Map")
plt.show()
