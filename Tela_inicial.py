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