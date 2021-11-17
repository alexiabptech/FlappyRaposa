import pygame

#Inicialização
pygame.init()


largura = 480
altura = 600
window = pygame.display.set_mode((altura, largura)) 
pygame.display.set_caption('Flappy Fox')

background = pygame.image.load('flappy_fox/img/p_fundo.png').convert()

game = True
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))

    pygame.display.update()

pygame.quit()    