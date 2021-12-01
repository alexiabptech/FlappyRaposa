import pygame
import random
from config import * 

class Fox(pygame.sprite.Sprite):
    def __init__(self, imagens, all_sprites, all_bullets, cerveja_img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.raposas = imagens
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.raposas[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.centerx = altura / 2
        self.rect.bottom = largura - 10
        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 10
        
        
        #self.image = imagens['raposas']
        #self.rect = self.image.get.rect()
        self.rect.y = altura/2
        self.rect.x = 50
        self.speedx = 0
        self.speedy = 0

        self.all_sprites = all_sprites
        self.all_bullets = all_bullets
        self.cerveja_img = cerveja_img
        
         # Só será possível atirar uma vez a cada 400 milissegundos
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 400

    def update (self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        x = self.rect.x
        y = self.rect.y
        now = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update
         # Se já está na hora de mudar de imagem...

        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now
            # Avança um quadro.
            self.frame = (self.frame + 1) % len(self.raposas)
            self.image = self.raposas[self.frame]  # Pega a primeira imagem
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
            self.last_update = pygame.time.get_ticks()  

        #Bottom para aparecer o rodapé
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > altura - 60:
            self.rect.bottom = altura - 60

       
    def shoot(self): 
        # Verifica se pode atirar
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = now - self.last_shot
        
        if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem.
            self.last_shot = now
            new_bullet = Bullet(self.cerveja_img, self.rect.top, self.rect.centerx)
            self.all_sprites.add(new_bullet)
            self.all_bullets.add(new_bullet)
            #self.imagens['pew_sound'].play()

class obstaculo(pygame.sprite.Sprite):
    def __init__(self, imagens):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = imagens
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = largura
        #self.rect.y = random.randint(-100, - obst_alt)
        self.rect.y = random.randint(0,largura)
        self.speedx = random.randint(6, 25) # mexi nas velocidades
        
        #self.speedy = random.randint(2, 9)
        self.speedy = 0
    def update(self):
        # Atualizando a posição 
        self.rect.x -= self.speedx
        self.rect.y += self.speedy

        # Se passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades

        if self.rect.top > largura or self.rect.right < 0 or self.rect.left > altura:
            self.rect.x = largura
            #self.rect.y = random.randint(-100, - obst_alt)
            self.rect.y = random.randint(0,largura)
            self.speedx = random.randint(6, 25) # mexi aqui tbm
        if self.rect.bottom > altura -60:
            self.rect.y = altura - 60
            
            
            
class Bullet(pygame.sprite.Sprite):
    def __init__(self, img, bottom, centerx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedx = +10  # Velocidade fixa para cima

    def update(self):
        # A bala só se move no eixo y
        self.rect.x += self.speedx

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()

