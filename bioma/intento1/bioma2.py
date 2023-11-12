import noise
import numpy as np
import matplotlib.pyplot as plt

def generate_noise_map(width, height, scale, seed):
    np.random.seed(seed)
    octaves = 6
    persistence = 0.5
    lacunarity = 2.0

    world_map = np.zeros((width, height))

    for i in range(width):
        for j in range(height):
            world_map[i][j] = noise.pnoise2(i/scale,
                                            j/scale,
                                            octaves=octaves,
                                            persistence=persistence,
                                            lacunarity=lacunarity,
                                            repeatx=1024,
                                            repeaty=1024,
                                            base=seed)

    return world_map

def assign_biomes(world_map):
    biomes = np.zeros_like(world_map, dtype=int)

    for i in range(len(world_map)):
        for j in range(len(world_map[i])):
            if world_map[i][j] < -0.2:
                biomes[i][j] = 1  # Desert
            elif world_map[i][j] < 0.5:
                biomes[i][j] = 2  # Grassland
            else:
                biomes[i][j] = 3  # Forest

    return biomes

def visualize_biomes(biomes):
    plt.imshow(biomes, cmap='terrain', interpolation='nearest')
    plt.colorbar(ticks=[1, 2, 3], labels=['Desert', 'Grassland', 'Forest'])
    plt.title("Biome Map")
    plt.show()

def main():
    width = 200
    height = 200
    scale = 20
    seed = np.random.randint(0, 100)

    world_map = generate_noise_map(width, height, scale, seed)
    biomes = assign_biomes(world_map)

    visualize_biomes(biomes)

if __name__ == "__main__":
    main()
