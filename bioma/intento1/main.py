import pygame
import random
import sys

pygame.init()

width = 200
height = 200

screem = pygame.display.set_mode((height, width))

bg = 25, 25, 25
screem.fill(bg)

ncX, ncY = 50, 50

#dimCW = width / ncX
#dimCH = height / ncY

dimCW = 20
dimCH = 20

while True:

    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    for y in range(0, ncX):
        for x in range(0, ncY):

            # Creamos el polígono de cada celda a dibujar
            poly = [((x) * dimCW, y * dimCH),
                    ((x + 1) * dimCW, y * dimCH),
                    ((x + 1) * dimCW, (y + 1) * dimCH),
                    ((x) * dimCW, (y + 1) * dimCH)]

            # Si estamos en la posición (1, 1), colorear toda la celda de rojo
            if x == 1 and y == 1:
                pygame.draw.polygon(screem, (255, 0, 0), poly, 0)
            else:
                pygame.draw.polygon(screem, (255,255,255), poly, 1)

    pygame.display.flip()





    