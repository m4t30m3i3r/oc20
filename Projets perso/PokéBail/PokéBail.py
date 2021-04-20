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
screenX = 750
screenY = 350
screen = pygame.display.set_mode([screenX, screenY])
background = pygame.image.load('background.jpg')

#Titre et icone
pygame.display.set_caption("pokemon")
icon = pygame.image.load('pokeball.png')
pygame.display.set_icon(icon)

#joueur
playerIMG = pygame.image.load('pokemon_trainer1.png')
playerX =  screenX/2 - 32
playerY = screenY/1.25
playerX_change = 0
playerY_change = 0




def player(x, y):
    screen.blit(playerIMG, (x, y))
    
#boucle jeu
running = True
while running:
    
    screen.blit(background, (0, 0))
    #screen.fill(Black)    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # pressage de touche
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = +1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change = -1
            if event.key == pygame.K_DOWN:
                playerY_change = +1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
 
 
    #player mouvement           
    playerX += playerX_change
    playerY += playerY_change
    
    
    if playerX <= 0:
        playerX = 0
    if playerX >= screenX - 64:
        playerX = screenX - 64
    
    if playerY <= 0:
        playerY = 0
    if playerY >= screenY - 64:
        playerY = screenY - 64
    
    player(playerX, playerY)
    pygame.display.update()

#   pygame.display.flip()

pygame.quit()