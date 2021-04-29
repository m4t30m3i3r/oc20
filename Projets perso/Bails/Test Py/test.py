import pygame
import random
pygame.init()

#variables couleurs
White = (255, 255, 255)
Red = (255, 0 , 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Black = (0, 0, 0)


#crée l'écran
screenX = 800
screenY = 600
HW = screenX/2
HH = screenY/2
screenY = 600
screen = pygame.display.set_mode([screenX, screenY])

#Titre et icone
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('cosmos.jpg')
pygame.display.set_icon(icon)

#fond
background = pygame.image.load('background.jpg')


#obstacle test
obstacle = pygame.image.load('obstacle.png').convert_alpha()
obstacle_mask = pygame.mask.from_surface(obstacle)
obstacle_rect = obstacle.get_rect()
obstacleX = HW - obstacle_rect.center[0]
obstacleY = HH - obstacle_rect.center[1]



#joueur
playerIMG = pygame.image.load('ally.png').convert_alpha()
playerX =  screenX/2 - 32
playerY = screenY/2
playerX_change = 0
player_mask = pygame.mask.from_surface(playerIMG)

#enemy
enemyIMG = pygame.image.load('enemy.png').convert_alpha()
enemyX = random.randint(0, screenX - 64)
enemyY = random.randint(0, screenY - 300)
enemyX_change = 1
enemyY_change = 40


def player(x, y):
    screen.blit(playerIMG, (x, y))
    
def enemy(x,y):
    screen.blit(enemyIMG, (x, y))

#boucle jeu
running = True
while running:
    
    screen.fill(Black)
    screen.blit(background, (0, 0))
    mx, my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # pressage de touche
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change = +2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    offset = (int(mx - obstacleX), int(my - obstacleX))
    result = player_mask.overlap(obstacle_mask, offset)
    print(playerX, playerY, obstacleX, obstacleY, offset, sep='\t')
    if result:
        print('carré fraté')
        pass
    else:
        print('pas dessus')
        pass
    #player mouvement           
    playerX += playerX_change
    
    if playerX <= 0:
        playerX = 0
    if playerX >= screenX - 64:
        playerX = screenX - 64
    
    #enemy mouvement
    enemyX += enemyX_change
    
    if enemyX <= 0:
        enemyX_change = 1
        enemyY += enemyY_change
    elif enemyX >= screenX-64:
        enemyX_change = -1
        enemyY += enemyY_change
        
    screen.blit(obstacle, (obstacleX, obstacleY))
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

#   pygame.display.flip()

pygame.quit()