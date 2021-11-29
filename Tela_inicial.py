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
imagens['fundo'] = pygame.image.load('flappy_fox/img/p_fundo.png').convert()

#faz a animação da raposa
raposas = []
for i in range(1,3):
    filename = 'flappy_fox/img/raposa{}.png'.format(i)
    img = pygame.image.load(filename).convert_alpha()
    img = pygame.transform.scale(img,(raposa_lar,raposa_alt))
    raposas.append(img)
imagens["raposas"] = raposas

imagens["obstaculos"] = pygame.image.load('flappy_fox/img/livro1.png').convert_alpha()
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

        if self.rect.top < 0:
            self.rect.y = 0
        if self.rect.bottom > altura - 50:
            self.rect.y = altura - 50

class obstaculo(pygame.sprite.Sprite):
    def __init__(self, imagens):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = imagens
        self.rect = self.image.get_rect()
        self.rect.x = largura
        #self.rect.y = random.randint(-100, - obst_alt)
        self.rect.y = random.randint(0,largura)
        self.speedx = random.randint(0, 4)
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
            self.speedx = random.randint(0, 4)
            #self.speedy = random.randint(2, 9)
            self.speedy = 0

groups = {}
all_sprites = pygame.sprite.Group()
all_livros = pygame.sprite.Group()

groups['all_sprites'] = all_sprites
groups['all_livros'] = all_livros

clock = pygame.time.Clock()
fps = 20

#criando o jogador
player = Fox(imagens['raposas'])
all_sprites.add(player)

game = True

for i in range(5):
    livro = obstaculo(imagens["obstaculos"])
    all_sprites.add(livro)
    all_livros.add(livro)

while game:
    clock.tick(fps)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.speedy -= 80
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.speedy += 80

    
    hits = pygame.sprite.spritecollide(player, all_livros, True)
    if len(hits) > 0:
        game = False


    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(imagens['fundo'], (0, 0))

    all_sprites.draw(window)
    pygame.display.update()

pygame.quit()    