import pygame
import random

pygame.init()
pygame.mixer.init() #para música

# ----- Gera tela principal
largura = 500
altura = 500
raposa_lar = 60
raposa_alt = 40
obst_lar = 40
obst_alt = 30
cerveja_lar = 20
cerveja_alt = 30 

window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Flappy Fox')

#Criando o texto de pontuação
font = pygame.font.SysFont(None, 30)
text = font.render('Pontuação', True, (255, 255, 255))
pontos = 0
conta_pontos = font.render(f'{pontos}', True, (255, 255, 255))
inicial = font.render('Para iniciar clique na tecla espaço', True, (0,255,0))

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

imagens["cerveja"] = pygame.image.load('flappy_fox/img/cerveja.png').convert_alpha()
imagens["cerveja"] = pygame.transform.scale(imagens["cerveja"], (cerveja_lar, cerveja_alt))

imagens['chão'] = pygame.image.load('flappy_fox/img/floor.jpeg').convert_alpha()
imagens["chão"] = pygame.transform.scale(imagens["chão"], (largura, 200))
floor_pos_i = 0

#carregando os sons do jogo
pygame.mixer.music.load('flappy_fox/sound/backsound.wav')
pygame.mixer.music.set_volume(0.4)
imagens['pew_sound'] = pygame.mixer.Sound('flappy_fox/sound/pew_2.wav')

#iniciando a estrutura do jogo

#desenhando o chão
def desenha_chao():
    window.blit(imagens['chão'],(floor_pos_i,440))
    window.blit(imagens['chão'],(floor_pos_i + 500 ,440))# cria uma imagem logo em seguida

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

        if self.rect.top < 0:
            self.rect.y = 0
        if self.rect.bottom > altura - 50:
            self.rect.y = altura - 50

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
        self.speedx = random.randint(6, 25)
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
            self.speedx = random.randint(6, 25)
            #self.speedy = random.randint(2, 9)
            
        if self.rect.bottom > altura - 60:
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
            
groups = {}
all_sprites = pygame.sprite.Group()
all_livros = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()

groups['all_sprites'] = all_sprites
groups['all_livros'] = all_livros
groups['all_bullets'] = all_bullets

clock = pygame.time.Clock()
fps = 10

#criando o jogador
player = Fox(imagens['raposas'], all_sprites, all_bullets, imagens['cerveja'])
all_sprites.add(player)

game = True

for i in range(5):
    livro = obstaculo(imagens["obstaculos"])
    all_sprites.add(livro)
    all_livros.add(livro)

pygame.mixer.music.play(loops=-1)
while game:
    clock.tick(fps)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.speedy -= 11
            if event.key == pygame.K_DOWN:
                player.speedy += 11 
            if event.key == pygame.K_SPACE:
                player.shoot()
                imagens['pew_sound'].play()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.speedy += 11
            if event.key == pygame.K_DOWN:
                player.speedy -= 11
 
       
        


    all_sprites.update()

    hits = pygame.sprite.groupcollide(all_livros, all_bullets, True, True,pygame. sprite.collide_mask)
    for livro in hits: # As chaves são os elementos do primeiro grupo (meteoros) que colidiram com alguma bala
        
        pontos += 1
        conta_pontos = font.render(f'{pontos}', True, (255, 255, 255))

        if pontos == 20:
            imagens['fundo'] =pygame.image.load('jogo_reserva/flappy_fox/img/noite.jpeg').convert()
            
            for i in range(8):
                livro = obstaculo(imagens["obstaculos"])
                livro.speedx = random.randint(15,30)
                all_sprites.add(livro)
                all_livros.add(livro)
            

        if pontos == 40:
            imagens['fundo'] =pygame.image.load('jogo_reserva/flappy_fox/img/fundo.png').convert()

    hits = pygame.sprite.spritecollide(player, all_livros, True, pygame.sprite.collide_mask)
    if len(hits) > 0:
        game = False


    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(imagens['fundo'], (0, 0))
    window.blit(text, (390, 10))
    window.blit(conta_pontos,(436,30))
    all_sprites.draw(window)

    floor_pos_i -= 4 #movimento o chão
    desenha_chao()
    if floor_pos_i <= -500:
        floor_pos_i = 0

    pygame.display.update()

pygame.quit()    