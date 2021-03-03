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

#rect
start = (0, 0)
size = (0, 0)
drawing = False
rect_list = []
RECT_COLOR = RED
key_dict_RECT_COLOR = {K_r:'RED', K_g:'GREEN', K_b:'BLUE', K_w:'WHITE'}
key_dict_RECT_WIDTH = {K_0:0, K_1:1, K_2:2, K_3:3, K_4:4, K_5:5, K_6:6, K_7:7, K_8:8, K_9:9}
RECT_WIDTH = 1

class Rectangle:
    def __init__(self, rect, color=RECT_COLOR, width=RECT_WIDTH):
        self.rect = rect
        self.color = color
        self.width = width
        
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect, self.width)

#polygone
points = []
key_dict_POLYGON_COLOR = {K_r:'RED', K_g:'GREEN', K_b:'BLUE', K_w:'WHITE'}
key_dict_POLYGON_WIDTH = {K_0:0, K_1:1, K_2:2, K_3:3, K_4:4, K_5:5, K_6:6, K_7:7, K_8:8, K_9:9}
POLYGON_COLOR = RED
POLYGON_WIDTH = 2

#image
# module = sys.modules['__main__']
# path, name = os.path.split(module.__file__)
# path = os.path.join(path, 'bird.png')
# img0 = pygame.image.load('bird.png')
# img0.convert()
# rect0 = img0.get_rect()
# center = 800//2, 600//2
# img = img0
# rect = img.get_rect()
# rect.center = center
# angle = 0
# scale = 1




#testIMG
movingIMG = pygame.image.load('bird.png')
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

######################################################################################################

        if forme == 'rectangle':
            if event.type == MOUSEBUTTONDOWN:
                start = event.pos
                size = 0, 0
                drawing = True
                
            elif event.type == MOUSEBUTTONUP:
                end = event.pos
                size = end[0] - start[0], end[1] - start[1]
                rect = Rectangle(Rect(start, size), RECT_COLOR, RECT_WIDTH)
                rect_list.append(rect)
                drawing = False
                
            elif event.type == MOUSEMOTION and drawing:
                end = event.pos
                size = end[0] - start[0], end[1] - start[1]
                
            if event.type == KEYDOWN:
                if event.key in key_dict_RECT_WIDTH:
                    rect_list[-1].width = key_dict_RECT_WIDTH[event.key]
                
            if event.type == KEYDOWN:
                if event.key in key_dict_RECT_COLOR:
                    rect_list[-1].color = key_dict_RECT_COLOR[event.key]
                     
                     
                     
        
                
     #####################################################################################################
     
        if forme == 'ellipse':
            if event.type == KEYDOWN:
                if event.key == K_1:
                    print('hello')
    ######################################################################################################

        if forme == 'polygone':
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    if len(points) > 0:
                        points.pop()

            elif event.type == MOUSEBUTTONDOWN:
                points.append(event.pos)
                drawing = True

            elif event.type == MOUSEBUTTONUP:
                drawing = False

            elif event.type == MOUSEMOTION and drawing:
                points[-1] = event.pos

            if event.type == KEYDOWN:
                if event.key in key_dict_POLYGON_WIDTH:
                    RECT_WIDTH = key_dict_POLYGON_WIDTH[event.key]
            
            if event.type == KEYDOWN:
                if event.key in key_dict_POLYGON_COLOR:
                    POLYGON_COLOR = key_dict_POLYGON_COLOR[event.key]



    #####################################################################################################
#         if forme == 'image':
#             
#             mouse = pygame.mouse.get_pos()
#             pygame.draw.line(screen, GREEN, center, mouse, 1)
#             if event.type == KEYDOWN:
#                 if event.key == K_r:
#                     if event.mod & KMOD_SHIFT:
#                         angle -= 10
#                     else:
#                         angle += 10
#                     img = pygame.transform.rotozoom(img0, angle, scale)
# 
#                 elif event.key == K_s:
#                     if event.mod & KMOD_SHIFT:
#                         scale /= 1.1
#                     else:
#                         scale *= 1.1
#                     img = pygame.transform.rotozoom(img0, angle, scale)
# 
#                 elif event.key == K_o:
#                     img = img0
#                     angle = 0
#                     scale = 1
# 
#                 elif event.key == K_h:
#                     img = pygame.transform.flip(img, True, False)
#             
#                 elif event.key == K_v:
#                     img = pygame.transform.flip(img, False, True)
# 
#                 elif event.key == K_l:
#                     img = pygame.transform.laplacian(img)
# 
#                 elif event.key == K_2:
#                     img = pygame.transform.scale2x(img)
# 
#                 rect = img.get_rect()
#                 rect.center = center
# 
#             elif event.type == MOUSEMOTION:
#                 mouse = event.pos
#                 x = mouse[0] - center[0]
#                 y = mouse[1] - center[1]
#                 d = math.sqrt(x ** 2 + y ** 2)
# 
#                 angle = math.degrees(-math.atan2(y, x))
#                 scale = abs(5 * d / 800)
#                 img = pygame.transform.rotozoom(img0, angle, scale)
#                 rect = img.get_rect()
#                 rect.center = center
#             pygame.draw.rect(img0, GREEN, rect0, 1)
#             screen.blit(img, rect)
#             pygame.draw.rect(screen, RED, rect, 1)
#             pygame.draw.circle(screen, RED, center, 6, 1)
#             pygame.draw.circle(screen, RED, mouse, 6, 1)
#             pygame.display.update()
   
###############################################################################################################################   
   
   
        if forme == 'testIMG':
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movingIMG_X_change = -1
                if event.key == pygame.K_RIGHT:
                    movingIMG_X_change = +1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    movingIMG_X_change = 0
     
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    movingIMG_Y_change = -1
                if event.key == pygame.K_DOWN:
                    movingIMG_Y_change = +1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    movingIMG_Y_change = 0
    
    movingIMG_X += movingIMG_X_change
    movingIMG_Y += movingIMG_Y_change   

#############################################################################################################################
    for rect in rect_list:
        rect.draw()
    
    if len(points)>1:
        rect = pygame.draw.lines(screen, POLYGON_COLOR, True, points, POLYGON_WIDTH)
        pygame.draw.rect(screen, GREEN, rect, POLYGON_WIDTH)
        pygame.display.update()
    movingIMG_f(0, 0)
    pygame.display.update()
    
pygame.quit()