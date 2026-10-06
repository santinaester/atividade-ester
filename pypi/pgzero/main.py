import sys
import pygame

# 1. Inicialização
pygame.init()

# Configurações da Janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Rebatedor - Pygame 2.6.1")

# Controle de taxa de quadros (FPS)
clock = pygame.time.Clock()
FPS = 60

# Cores (RGB)
BLACK = (20, 20, 20)
WHITE = (240, 240, 240)
BLUE = (50, 150, 250)
RED = (230, 60, 60)

# 2. Objetos do Jogo
# Bloco do Jogador (x, y, largura, altura)
paddle = pygame.Rect(WIDTH // 2 - 60, HEIGHT - 30, 120, 15)
paddle_speed = 7

# Bola
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)
ball_speed_x = 5
ball_speed_y = -5

# Pontuação
score = 0
font = pygame.font.SysFont("Arial", 28)

# 3. Game Loop Principal
running = True
while running:
    # --- A. Tratamento de Eventos ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
            pygame.quit()
            sys.exit()

    # Movimentação do jogador (Teclas contínuas)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed

    # --- B. Atualização da Física/Lógica ---
    # Mover a bola
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Colisão da bola com as paredes laterais
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1

    # Colisão da bola com o topo
    if ball.top <= 0:
        ball_speed_y *= -1

    # Colisão da bola com o jogador
    if ball.colliderect(paddle) and ball_speed_y > 0:
        ball_speed_y *= -1
        score += 1

    # Resetar bola se passar do fundo (Game Over/Ponto Perdido)
    if ball.bottom >= HEIGHT:
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_y = -5
        score = 0

    # --- C. Desenho na Tela ---
    screen.fill(BLACK)

    # Desenhar o jogador e a bola
    pygame.draw.rect(screen, BLUE, paddle, border_radius=5)
    pygame.draw.ellipse(screen, RED, ball)

    # Desenhar a pontuação
    score_text = font.render(f"Pontos: {score}", True, WHITE)
    screen.blit(score_text, (20, 20))

    # Atualizar tela e controlar o framerate
    pygame.display.flip()
    clock.tick(FPS)