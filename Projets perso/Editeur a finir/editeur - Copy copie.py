import pygame
from pygame.locals import *
import math, sys, os
pygame.init()

#variables couleurs
WHITE = (255, 255, 255)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
ScreenBackground = BLACK


#key dict pour savoir quelle forme faire
key_dict1 = {K_p:'rectangle', K_l:'ellipse', K_m:'polygone', K_n:'image', K_f:'testIMG'}
forme = 'début'

#crée l'écran
screen = pygame.display.set_mode([800, 600])

#Titre et icone
pygame.display.set_caption("Editeur")
icon = pygame.image.load('Icone.png')
pygame.display.set_icon(icon)



#testIMG
movingIMG = pygame.image.load('bird.png').convert_alpha()
movingIMG_mask = pygame.mask.from_surface(movingIMG)
movingIMG_rect = movingIMG.get_rect()
movingIMG_x = 400 - movingIMG_rect.center[0]
movingIMG_Y =  300 - movingIMG_rect.center[1]





movingIMG_X_change = 0
movingIMG_Y_change = 0
movingIMG_X =  0
movingIMG_Y = 0
def movingIMG_f(x, y):
    screen.blit(movingIMG, (movingIMG_X, movingIMG_Y))



#boucle editeur
running = True
while running:
     
    screen.fill(ScreenBackground)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == KEYDOWN:
            if event.key in key_dict1:
                forme = key_dict1[event.key]


   
###############################################################################################################################   
   
   
        if forme == 'testIMG':
        
            mx, my = pygame.mouse.get_pos()
    
    movingIMG_X += movingIMG_X_change
    movingIMG_Y += movingIMG_Y_change
#############################################################################################################################

    pygame.display.update()
    
pygame.quit()