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
screen = pygame.display.set_mode([screenX, screenY])

#Titre et icone
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('cosmos.jpg')
pygame.display.set_icon(icon)

#fond
background = pygame.image.load('background.jpg')


#joueur
playerIMG = pygame.image.load('ally.png')
playerX =  screenX/2 - 32
playerY = screenY/1.25
playerX_change = 0


#enemy
enemyIMG = pygame.image.load('enemy.png')
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
        
    
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

#   pygame.display.flip()

pygame.quit()