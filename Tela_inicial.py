import pygame

#Inicialização
pygame.init()


largura = 480
altura = 600
window = pygame.display.set_mode((altura, largura)) 
pygame.display.set_caption('Flappy Fox')

imagens = {}
imagens['background'] = pygame.image.load('flappy_fox/img/p_fundo.png').convert()
imagens['cano'] = pygame.image.load('flappy_fox/img/caninho.png').convert_alpha()
imagens['raposa f'] = pygame.image.load('flappy_fox/img/raposa1.jpeg').convert_alpha()
imagens['raposa a'] = pygame.image.load('flappy_fox/img/raposa2.jpeg').convert_alpha()

game = True
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(imagens['background'], (0, 0))


    pygame.display.update()

pygame.quit()    