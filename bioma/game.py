import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
window_size = (400, 300)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Juego con Pygame")

# Configuración del rectángulo
player_size = 50
player_color = (0, 128, 255)  # Azul
player_pos = [window_size[0] // 2 - player_size // 2, window_size[1] - player_size - 10]

# Configuración de los obstáculos
obstacle_size = 50
obstacle_color = (255, 0, 0)  # Rojo
obstacle_speed = 5
obstacle_frequency = 25  # Cada cuántos frames se genera un nuevo obstáculo
obstacles = []

# Configuración de la consola
console_font = pygame.font.Font(None, 36)
console_pos = (10, window_size[1] - 40)

# Puntaje inicial
score = 0

# Bucle principal del juego
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Manejo de la entrada del usuario
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT] and player_pos[0] < window_size[0] - player_size:
        player_pos[0] += 5

    # Generar obstáculos
    if random.randint(1, obstacle_frequency) == 1:
        obstacle_x = random.randint(0, window_size[0] - obstacle_size)
        obstacle_y = 0
        obstacles.append([obstacle_x, obstacle_y])

    # Mover obstáculos y verificar colisiones
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed
        if (
            player_pos[0] < obstacle[0] + obstacle_size
            and player_pos[0] + player_size > obstacle[0]
            and player_pos[1] < obstacle[1] + obstacle_size
            and player_pos[1] + player_size > obstacle[1]
        ):
            # Colisión con un obstáculo
            pygame.quit()
            sys.exit()

    # Eliminar obstáculos fuera de la pantalla
    obstacles = [obstacle for obstacle in obstacles if obstacle[1] < window_size[1]]

    # Actualizar puntaje
    score += 1

    # Actualizar la pantalla
    screen.fill((255, 255, 255))  # Fondo blanco
    pygame.draw.rect(screen, player_color, (player_pos[0], player_pos[1], player_size, player_size))

    for obstacle in obstacles:
        pygame.draw.rect(screen, obstacle_color, (obstacle[0], obstacle[1], obstacle_size, obstacle_size))

    # Dibujar la consola
    console_text = f"Puntaje: {score}"
    console_surface = console_font.render(console_text, True, (0, 0, 0))  # Texto negro
    screen.blit(console_surface, console_pos)

    pygame.display.flip()

    # Establecer el número de frames por segundo
    clock.tick(60)
