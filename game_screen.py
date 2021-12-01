import pygame
import random
from assets import * 
from config import *
from sprites import * 


def game_screen(window):
    imagens = load_assets()

    floor_pos_i = 0
    #criando o texto de pontuação
    font = pygame.font.SysFont(None, 30)
    text = font.render('Pontuação', True, (255, 255, 255))
    pontos = 0
    conta_pontos = font.render(f'{pontos}', True, (255, 255, 255))
    inicial = font.render('Para iniciar clique na tecla espaço', True, (0,255,0))

        
                

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




    # tela_inicio(window,imagens['fundo'])

    pygame.mixer.music.play(loops=-1)
    while game:
        clock.tick(fps)
        
        #inicia_jogo() 
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
                    imagens['pew_sound'].play() #toca o som de tiro (Isa falando)
            if event.type == pygame.KEYUP:
                
                # if event.key == pygame.K_KP_ENTER:
                #     jogo_iniciado()

                if event.key == pygame.K_UP:
                    player.speedy += 11
                if event.key == pygame.K_DOWN:
                    player.speedy -= 11
    

        all_sprites.update()

        hits = pygame.sprite.groupcollide(all_livros, all_bullets, True, True, pygame.sprite.collide_mask)
        for livro in hits: # As chaves são os elementos do primeiro grupo (meteoros) que colidiram com alguma bala
            
            pontos += 1
            conta_pontos = font.render(f'{pontos}', True, (255, 255, 255))

            if pontos == 20:
                imagens['fundo'] =pygame.image.load('flappy_fox/img/noite.jpeg').convert()

                for i in range(8):
                    livro = obstaculo(imagens['obstaculos'])
                    livro.speedx = random.randint(15,30)
                    all_sprites.add(livro)
                    all_livros.add(livro)
            if pontos == 40:
                imagens['fundo'] =pygame.image.load('flappy_fox/img/fundo.png').convert()    
                for i in range(8):
                    livro = obstaculo(imagens['obstaculos'])
                    livro.speedx = random.randint(20,40)
                    all_sprites.add(livro)
                    all_livros.add(livro)

            #O livro e destruido e precisa ser recriado
            m = obstaculo(imagens['obstaculos'])
            all_sprites.add(m)
            all_livros.add(m)


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
        #Chão
        window.blit(imagens['chão'],(floor_pos_i,440))
        window.blit(imagens['chão'],(floor_pos_i + 500 ,440))# cria uma imagem logo em seguida

        if floor_pos_i <= -500:
            floor_pos_i = 0
        
    
        
        pygame.display.update()

    return OVER