import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Umbrales para la aparición de nuevos tipos de enemigos
vertical_enemy_threshold = 200
diagonal_enemy_threshold = 1000

# Configuración de la pantalla
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego de Enemigos")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)
indigo = (75,0,130)
red = (255,204,204)

# Jugador
player_size = 30
player_x = width // 2 - player_size // 2
player_y = height - 2 * player_size
player_speed = 5

# Enemigos
enemy_size = 20
enemy_speed = 5
enemies = []

# Puntaje
score = 0
font = pygame.font.SysFont(None, 36)

# Reloj y FPS (Frames Per Second)
clock = pygame.time.Clock()
FPS = 60

# Función para mostrar texto en la pantalla
def draw_text(text, x, y):
    text_surface = font.render(text, True, white)
    screen.blit(text_surface, (x, y))

# Función para mostrar el menú principal
def show_menu():
    screen.fill(black)
    draw_text("¡Bienvenido al Juego de Enemigos!", 200, height // 2 - 50)
    draw_text("Presiona 'S' para empezar", 250, height // 2)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    waiting = False

# Función para mostrar el menú de pausa
def show_pause_menu():
    screen.fill(black)
    draw_text("¡Juego en pausa!", 300, height // 2 - 50)
    draw_text("Presiona 'P' para continuar", 250, height // 2)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    waiting = False

def reset_game():
    global player_x, player_y, enemies, score
    player_x = width // 2 - player_size // 2
    player_y = height - 2 * player_size
    enemies = []
    score = 0
def create_object(objects, object_size, object_type):
    x = random.randint(0, width - object_size)
    y = -object_size

    if object_type == "vertical":
        speed = random.randint(2, 5)  # Se puede ajustar la velocidad
        objects.append([x, y, object_type, speed])    
    elif object_type == "diagonal":
        speed_x = random.randint(2, 5)
        speed_y = random.randint(2, 5)
        objects.append([x, y, object_type, speed_x, speed_y])


# Función principal del juego
def game():
    global player_x, enemies, score

    show_menu()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    show_pause_menu()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < width - player_size:
            player_x += player_speed

        screen.fill(black)

        # Dibujar jugador y enemigos
        pygame.draw.rect(screen, white, [player_x, player_y, player_size, player_size])
        for enemy in enemies:
            if enemy[2] == "vertical":
                pygame.draw.rect(screen, indigo, [enemy[0], enemy[1], enemy_size, enemy_size])
                enemy[1] += enemy[3]  # Movimiento vertical diferente
            elif enemy[2] == "diagonal":
                # Dibujar triángulo para enemigo diagonal
                triangle_points = [
                    (enemy[0], enemy[1]),
                    (enemy[0] + enemy_size, enemy[1]),
                    (enemy[0] + enemy_size / 2, enemy[1] + enemy_size)
                ]
                pygame.draw.polygon(screen, red, triangle_points)

                enemy[0] += enemy[3]  # Movimiento diagonal en X
                enemy[1] += enemy[4]  # Movimiento diagonal en Y
                 # Rebote en las paredes laterales
                if enemy[0] < 0 or enemy[0] > width - enemy_size:
                    enemy[3] = -enemy[3]

                # Desaparecer al tocar la parte inferior de la ventana
                if enemy[1] > height:
                    enemies.remove(enemy)
        # Crear nuevos enemigos aleatorios después de ciertos umbrales de puntaje
        if score >= vertical_enemy_threshold and random.randint(0, 100) < 5:
            create_object(enemies, enemy_size, "vertical")


        if score >= diagonal_enemy_threshold and random.randint(0, 100) < 5:
            create_object(enemies, enemy_size, "diagonal")

        # Verificar colisiones con enemigos
        for enemy in enemies:
            if (
                player_x < enemy[0] < player_x + player_size
                and player_y < enemy[1] < player_y + player_size
            ):
                show_game_over()

        # Actualizar y mostrar puntaje
        score += 1
        draw_text(f"Puntaje: {score}", 10, 10)

        pygame.display.flip()
        clock.tick(FPS)

# Función para mostrar la ventana emergente de derrota
def show_game_over():
    global player_x, player_y, enemies, score

    screen.fill(black)
    draw_text("¡Perdiste!", 350, height // 2 - 50)
    draw_text(f"Puntaje: {score}", 350, height // 2)
    draw_text("Presiona 'R' para reiniciar", 300, height // 2 + 50)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game()
                    waiting = False


if __name__ == "__main__":
    game()
