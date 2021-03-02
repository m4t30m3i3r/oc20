import pygame
from pygame.locals import *
import math, sys, os
pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
ScreenBackground = BLACK


screen = pygame.display.set_mode([800, 600])

birdPNG = pygame.image.load('help.png')

def Help():
    screen.blit(birdPNG, (0, 0))
    
    
running = True
while running:
    
    screen.fill(ScreenBackground)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
    if pygame.key.get_pressed() [pygame.K_1] == True:
            Help()
    
    
    pygame.display.update()
pygame.quit()