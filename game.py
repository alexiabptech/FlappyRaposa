import pygame
import random
#from inicio import * 
from config import *
from game_screen import *
from init_screen import *
from end_screen import *

pygame.init()
pygame.mixer.init() #para música


#carregando os sons do jogo
pygame.mixer.music.load('raposa_text.py/flappy_fox/sound/backsound.wav')
pygame.mixer.music.set_volume(0.4)

window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Flappy Fox')

state = INIT 
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window)
    elif state == OVER:
        state = end_screen(window)
    else:
        state = QUIT
   

pygame.quit()  