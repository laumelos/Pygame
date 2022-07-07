from typing import List
import pygame
from pygame.locals import *
from sys import exit
import time
import pygame.sprite
 
pygame.init()
pygame.font.init()
pygame.mixer.init()

 
#variáveis
white = (255,255,255)
bubbles = pygame.image.load ("c92a44f1dbab187.png")
coraçao = pygame.image.load ("coraçao.png")
gatinho = pygame.image.load ("gatinho.png")
gatinhomaior = pygame.image.load ("gatinhomaior.png")
fundo = pygame.image.load ("fundojogo.png")
bubblesound = pygame.mixer.Sound('539823__ristooooo1__bubbles-001.wav')

largura = 640
altura = 480
x = 0
y = 0
 
#tela
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("pet.com")
tela.blit(fundo,(0,0))

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
 
#button water
water_img = pygame.image.load("sabonete.png").convert_alpha()
water_img = button(120, 395, water_img, 1)

 
#TELA
telainicial=True
while telainicial==True:
    if (water_img.draw(tela)):                           
        tela.blit(bubbles,(210, 80))
        pygame.mixer.Sound.play(bubblesound)
        pygame.mixer.music.stop()
        pygame.display.update()
        time.sleep(4)
        tela.blit(gatinhomaior,(200,140))
    
    

        
        

        

    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            telainicial=False
    
   #button images
    water = pygame.image.load ("sabonete.png")
    tela.blit(water,(120, 395))
    #time.sleep(5)

    morango_img = pygame.image.load ("morango.png")
    tela.blit(morango_img,(280, 390))

    lua_img = pygame.image.load ("lua.png")
    tela.blit(lua_img,(460, 390))
     
    #gatinho
    tela.blit(gatinhomaior,(200,140))

    pygame.display.update()
 
pygame.quit()
 

