# Instala la biblioteca noise utilizando: pip install noise
import noise
import numpy as np
import matplotlib.pyplot as plt

def generate_perlin_noise(width, height, scale, octaves, persistence, lacunarity, seed):
    world = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            world[i][j] = noise.pnoise2(i/scale,
                                        j/scale,
                                        octaves=octaves,
                                        persistence=persistence,
                                        lacunarity=lacunarity,
                                        repeatx=1024,
                                        repeaty=1024,
                                        base=seed)
    return world

def generate_biomes(heightmap):
    biomes = np.zeros_like(heightmap, dtype=int)
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            if heightmap[i][j] < -0.1:
                biomes[i][j] = 0  # Water
            elif heightmap[i][j] < 0.2:
                biomes[i][j] = 1  # Plains
            elif heightmap[i][j] < 0.6:
                biomes[i][j] = 2  # Forest
            else:
                biomes[i][j] = 3  # Mountains
    return biomes

def visualize_map(data, title):
    plt.imshow(data, cmap='terrain')
    plt.title(title)
    plt.colorbar()
    plt.show()

# Parámetros del ruido de Perlin
width = 500
height = 500
scale = 100.0
octaves = 6
persistence = 0.5
lacunarity = 2.0
seed = np.random.randint(0, 100)

# Generar el mapa de alturas usando Perlin Noise
heightmap = generate_perlin_noise(width, height, scale, octaves, persistence, lacunarity, seed)
print("height: ",height)

# Generar biomas a partir del mapa de alturas
biomes = generate_biomes(heightmap)

print("biomes: ",biomes)

# Visualizar el mapa de alturas y los biomas
visualize_map(heightmap, 'Perlin Noise Heightmap')
visualize_map(biomes, 'Biomes')

