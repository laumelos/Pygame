import pygame
from pygame.locals import *
from sys import exit
 
pygame.init()
 
#variáveis
white = (255,255,255)
coraçao = pygame.image.load ("coraçao.png")
gatinho = pygame.image.load ("gatinho.png")
gatinhomaior = pygame.image.load ("gatinhomaior.png")
fundo = pygame.image.load ("fundojogo.png")
largura = 640
altura = 480
x = 0
y = 0
 
#tela
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("pet.com")
tela.blit(fundo,(0,0))
 
'''
#button class
class button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
 
    def draw(self, surface):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
 
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
 
        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))
 
        return action
 
#button
button_img = pygame.image.load("buttonjogo.png").convert_alpha()
button_img = button(240, 360, button_img, 1)
'''
 
#TELA
telainicial=True
while telainicial==True:
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            telainicial=False
    pygame.time
    
    sabao_img = pygame.image.load ("Removal-77.png")
    tela.blit(sabao_img,(120, 395))
    
    morango_img = pygame.image.load ("morango.png")
    tela.blit(morango_img,(280, 390))

    lua_img = pygame.image.load ("lua.png")
    tela.blit(lua_img,(460, 390))

     
    #gatinho
    tela.blit(gatinhomaior,(200,140))

    pygame.display.update()
 
pygame.quit()
 

