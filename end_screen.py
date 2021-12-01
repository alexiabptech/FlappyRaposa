import pygame
import random
from assets import * 
from os import path
#from inicio import *
from config import BLACK, FPS, GAME, QUIT, OVER

# Define algumas variáveis com as cores básicas

def end_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load('flappy_fox/img/f_screen.jpeg').convert()
    background = pygame.transform.scale(background,(500,500))
    background_rect = background.get_rect()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False

            if event.type == pygame.KEYUP:
                state = INIT
                running = False


        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state