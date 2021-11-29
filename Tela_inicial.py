import pygame
import random
import time

pygame.init()
pygame.mixer.init() #para música

# ----- Gera tela principal
largura = 500
altura = 500
raposa_lar = 80
raposa_alt = 60
obst_lar = 50
obst_alt = 30

window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Flappy Fox')

imagens = {}
imagens['fundo'] = pygame.image.load('raposa_text.py/flappy_fox/img/p_fundo.png').convert()

#faz a animação da raposa
raposas = []
for i in range(1,3):
    filename = 'raposa_text.py/flappy_fox/img/raposa{}.png'.format(i)
    img = pygame.image.load(filename).convert_alpha()
    img = pygame.transform.scale(img,(raposa_lar,raposa_alt))
    raposas.append(img)
imagens["raposas"] = raposas

imagens["obstaculos"] = pygame.image.load('jogo_reserva/flappy_fox/img/livro1.png').convert_alpha()
imagens["obstaculos"] = pygame.transform.scale(imagens["obstaculos"], (obst_lar, obst_alt))

#iniciando a estrutura do jogo
class Fox(pygame.sprite.Sprite):
    def __init__(self, imagens):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.raposas = imagens
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.raposas[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 10
        
        
        #self.image = imagens['raposas']
        #self.rect = self.image.get.rect()
        self.rect.y = altura/2
        self.rect.x = 90
        self.speedx = 0
        self.speedy = 14


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