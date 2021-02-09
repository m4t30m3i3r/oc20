import pygame
pygame.init()


White = (255, 255, 255)
Red = (255, 0 , 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Snoop Dogg")
icon = pygame.image.load('joint.png')
pygame.display.set_icon(icon)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    screen.fill(Blue)

pygame.quit()