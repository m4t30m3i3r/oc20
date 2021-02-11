import pygame
pygame.init()

#variables couleurs
White = (255, 255, 255)
Red = (255, 0 , 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Black = (0, 0, 0)

#crée l'écran
screen = pygame.display.set_mode([800, 600])

#Titre et icone
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('cosmos.jpg')
pygame.display.set_icon(icon)

#joueur
playerIMG = pygame.image.load('ally.png')
playerX =  370
playerY = 480
playerX_change = 0


#enemy
enemyIMG = pygame.image.load('enemy.png')
enemyX = 370
enemyY = 30
enemyX_change = 0


def player(x, y):
    screen.blit(playerIMG, (x, y))
    
def enemy(x,y):
    screen.blit(enemyIMG, (x, y))

#boucle jeu
running = True
while running:
    
    screen.fill(Black)
    
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
                
                
    playerX += playerX_change
    
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

#   pygame.display.flip()

pygame.quit()