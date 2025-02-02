import pygame
import random

# Inicializa o pygame
pygame.init()

# Configurações da tela
largura, altura = 600, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pac-Man Simples")

# Cores
PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

# Configuração do Pac-Man
tamanho_pacman = 20
x_pacman = largura // 2
y_pacman = altura // 2
velocidade = 5
mov_x, mov_y = 0, 0

# Configuração das comidas
num_comidas = 10
tamanho_comida = 10
comidas = [[random.randint(0, largura - tamanho_comida), random.randint(0, altura - tamanho_comida)] for _ in range(num_comidas)]

# Loop do jogo
rodando = True
clock = pygame.time.Clock()

while rodando:
    tela.fill(PRETO)
    
    # Captura eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mov_x, mov_y = -velocidade, 0
            elif event.key == pygame.K_RIGHT:
                mov_x, mov_y = velocidade, 0
            elif event.key == pygame.K_UP:
                mov_x, mov_y = 0, -velocidade
            elif event.key == pygame.K_DOWN:
                mov_x, mov_y = 0, velocidade
    
    # Movimenta o Pac-Man
    x_pacman += mov_x
    y_pacman += mov_y
    
    # Impede que saia da tela
    x_pacman = max(0, min(largura - tamanho_pacman, x_pacman))
    y_pacman = max(0, min(altura - tamanho_pacman, y_pacman))
    
    # Desenha o Pac-Man
    pygame.draw.circle(tela, AMARELO, (x_pacman + tamanho_pacman // 2, y_pacman + tamanho_pacman // 2), tamanho_pacman // 2)
    
    # Desenha as comidas
    for comida in comidas:
        pygame.draw.rect(tela, BRANCO, (comida[0], comida[1], tamanho_comida, tamanho_comida))
    
    # Verifica colisão com a comida
    novas_comidas = []
    for comida in comidas:
        if not (x_pacman < comida[0] + tamanho_comida and x_pacman + tamanho_pacman > comida[0] and y_pacman < comida[1] + tamanho_comida and y_pacman + tamanho_pacman > comida[1]):
            novas_comidas.append(comida)
    comidas = novas_comidas
    
    # Atualiza a tela
    pygame.display.update()
    clock.tick(30)

pygame.quit()
