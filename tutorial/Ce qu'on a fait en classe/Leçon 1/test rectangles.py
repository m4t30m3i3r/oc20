import pygame
from pygame.locals import*

#size = 640, 320
#width, heigh = size

width = 640
height = 320

size = (width, height)
GREEN = (150, 225, 225)
RED = (225, 0, 0)
GRAY = (127,127, 127)
background = GREY

pygame.init()
screen = pygame.display.set_mode(size)
screen.fill(background)

pygame.draw.rect(screen, RED,(50, 20, 220, 100))
                 
pygame.display.update()

running = True
while running:
    for event in pygame.event.get()
    if event.type == QUIT:
        running = False
        
pygame.quit()