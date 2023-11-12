# Importamos las librerías necesarias:
import pygame
import numpy as np

# Para comenzar vamos a crear la pantalla de nuestro juego
pygame.init()

width = 600
height = 600
screen = pygame.display.set_mode((height, width))  # Corregido el nombre de la variable

bg = 25, 25, 25
screen.fill(bg)  # Corregido el nombre de la variable

# Número de celdas
ncX, ncY = 25, 25

# Dimensiones de las celdas
dimCW = width / ncX
dimCH = height / ncY

while True:
    for y in range(0, ncX):
        for x in range(0, ncY):

            # Creamos el polígono de cada celda a dibujar
            poly = [((x)     * dimCW,  y      * dimCH),
                    ((x + 1) * dimCW,  y      * dimCH),
                    ((x + 1) * dimCW, (y + 1) * dimCH) ,
                    ((x)     * dimCW, (y + 1) * dimCH)]

            # Y dibujamos la celda para cada par de X e Y.
            pygame.draw.polygon(screen, (128, 12, 128), poly, 1)  # Corregido el nombre de la variable

    # Actualizamos la pantalla
    pygame.display.flip()
