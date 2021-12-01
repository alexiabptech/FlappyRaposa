import pygame
from config import *

def load_assets():
    

    # fazendo todas as imagens
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

    imagens["obstaculos"] = pygame.image.load('raposa_text.py/flappy_fox/img/livro1.png').convert_alpha()
    imagens["obstaculos"] = pygame.transform.scale(imagens["obstaculos"], (obst_lar, obst_alt))

    imagens["cerveja"] = pygame.image.load('raposa_text.py/flappy_fox/img/cerveja.png').convert_alpha()
    imagens["cerveja"] = pygame.transform.scale(imagens["cerveja"], (cerveja_lar, cerveja_alt))

    #imagens['vidas'] = pygame.image.load('raposa_text.py/flappy_fox/img/vida.png').convert_alpha()
    #imagens['vidas'] = pygame.transform.scale(imagens["vidas"], (30, 50))

    imagens['chão'] = pygame.image.load('raposa_text.py/flappy_fox/img/floor.jpeg').convert_alpha()
    imagens["chão"] = pygame.transform.scale(imagens["chão"], (largura, 200))


    #carregando os sons
    imagens['pew_sound'] = pygame.mixer.Sound('raposa_text.py/flappy_fox/sound/pew_2.wav')
    
    return imagens