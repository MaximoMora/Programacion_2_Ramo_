import pygame
import sys

# Dimensiones de la ventana y de la matriz
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
MATRIX_ROWS = 5
MATRIX_COLS = 5
CELL_SIZE = WINDOW_WIDTH // MATRIX_COLS

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Matriz de ejemplo (puedes reemplazarla con tus propios datos)
matrix_data = [
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1]
]

def draw_matrix(surface, matrix):
    for row in range(MATRIX_ROWS):
        for col in range(MATRIX_COLS):
            color = WHITE if matrix[row][col] == 0 else BLACK
            pygame.draw.rect(surface, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def main():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Matriz con Pygame')

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill(WHITE)
        draw_matrix(window, matrix_data)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
