import pygame
import time
import random

pygame.init()

blanc = (255, 255,255)
noir = (0, 0, 0)
rouge = (255, 0, 0)
bleu = (0, 0, 255)

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Jeu du sepent')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 30
font_style = pygame.font.SysFont(None, 30)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/3, dis_height/3])

def gameloop(): #création d'une fonction
    game_over = False
    game_close = False

x1 = dis_width/2
y1 = dis_height/2

x1_change = 0
y1_change = 0
foodx = round(random.randrange(0, dis_width - snake_block)/10.00) * 10.0
foody = round(random,randrange(0, dis_width - snake_block)/10.00) * 10.0

while not game_over:
    while game_close == True:
        dis.fill(white)
        message('vous avez perdu Q-Quitter ou C-Continuer',red)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K.q:
                                            game_over = True
                                            game_close = False
                if event.key == pygame.K_c:
                                            gameloop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_GAUCHE:
                    x1_change = -snake_block
                    y1_change = 0 
                elif event.key == pygame.K_DROITE:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_HAUT:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K.BAS:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
snake_block=10

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
snake_speed=30
font_style = pygame.font.SysFont(None, 50)

def message(msg,color):
    mesg = font_style.render(msg,True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over =True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_GAUCHE:
                                            x1_change = -snake_block
                                            y1_change = 0
        elif event.key == pygame.K_DROITE:
            x1_change = snake_block
            y1_change = 0
        elif event.key == pygame.K_HAUT:
            y1_change = -snake_block
            x1_change = 0
        elif event.key == pygame.K_BAS:
            y1_change = snake_block
            x1_change = 0
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_close = True  

    x1 += x1_change
    y1 += y1_change
    dis.fill(white) 
    pygame.draw.rect(dis, blue,[foodx, foody, snake_block, snake_block])
    pygame.draw.rect(dis,black,[x1, y1, snake_block, snake_block])
    pygame.display.update()

    if x1 == foodx and y1 == foody:
        print ('miam')

        clock.tick(snake_speed)
pygame.quit()
quit()

