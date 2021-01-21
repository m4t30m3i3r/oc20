import pygame
from pygame, locals import

#size = 640, 320
#width, heigh = size

size = (width, height)
GREEN = (150, 225, 225)
RED = (225, 0, 0)

pygame.init()
screen = pygmae.display.set_mode(size)
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
pygame.quit()