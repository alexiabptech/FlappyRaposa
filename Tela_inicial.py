import pygame

#Inicialização
pygame.init()

#Gera Tela Principal
raposa_lar = 60
raposa_alt = 40
largura = 600
altura = 500
window = pygame.display.set_mode((largura,altura)) 
pygame.display.set_caption('JumpFox')

imagens = {}
imagens['background'] = pygame.image.load('flappy_fox/img/p_fundo.png').convert()
imagens['cano'] = pygame.image.load('flappy_fox/img/caninho.png').convert_alpha()

#Animação da Raposa
raposas = []
for i in range(1,3):
    filename = 'raposa_text.py/flappy_fox/img/raposa{}.png'.format(i)
    img = pygame.image.load(filename).convert_alpha()
    img = pygame.transform.scale(img,(raposa_lar,raposa_alt))
    raposas.append(img)
imagens["raposas"] = raposas

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