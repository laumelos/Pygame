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
largura = 640
altura = 480
x = 0
y = 0
happybar = 230
#happybarlar = 50

#imagens load
bubbles = pygame.image.load ('images/bolhas.png')
coraçao = pygame.image.load ('images/coraçao.png')
gatinho = pygame.image.load ('images/gatinho.png')
gatinhomaior = pygame.image.load ('images/gatinhomaior.png')
gatinhodormindo =  pygame.image.load ('images/gatinhodormindo.png')
fundo = pygame.image.load ("images/fundojogo.png")
fundoazul = pygame.image.load ('images/fundoazul.png')
framebarra = pygame.image.load ('images/framebar.png')
fundobarra = pygame.image.load ('images/fundobarra.png')



#sounds load
bubblesound = pygame.mixer.Sound('sounds/539823__ristooooo1__bubbles-001.wav')
sleepsound = pygame.mixer.Sound('sounds/gatinhodormindo.wav')

#tela
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("pet.com")
tela.blit(fundo,(0,0))

# class barra():
#     def __init__(self, time):


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
 
#button agua
agua_img = pygame.image.load("images/agua.png").convert_alpha()
agua_img = button(120, 395, agua_img, 1)

#button morango
morango_img = pygame.image.load ("images/morango.png").convert_alpha()
morango_img = button(280, 390, morango_img, 1)

#button lua
lua_img = pygame.image.load("images/lua.png").convert_alpha()
lua_img = button(460, 390,lua_img, 1)

#TELA
telainicial=True
while telainicial==True:

    tela.blit(fundobarra,(0, 0))
    
    if happybar>=0:
        pygame.draw.rect(tela, (white), (38,123,30,happybar))
        happybar = happybar - 0.01
        
    else:
        telainicial==False
    
    #funcionalid banho
    if (agua_img.draw(tela)):    

        tela.blit(framebarra,(25,110))
        tela.blit(bubbles,(210, 80))                           
        pygame.mixer.Sound.play(bubblesound)
        pygame.mixer.music.stop()
        pygame.display.update()                                 
        time.sleep(6)
        tela.blit(gatinhomaior,(200,140))
        tela.blit(fundo,(0,0))

        happybar = happybar + 10
    
    #funcionalid dormir
    if (lua_img.draw(tela)):    

        tela.blit(framebarra,(25,110))
        tela.blit(fundoazul,(0,0))
        tela.blit(gatinhodormindo,(200,210))
        tela.blit(framebarra,(25,110))
        pygame.mixer.Sound.play(sleepsound)
        pygame.mixer.music.stop()
        pygame.display.update()
        time.sleep(4)
        tela.blit(fundo,(0,0))
        
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            telainicial=False

    # tela.blit(fundobarra,(0, 0))
    # pygame.draw.rect(tela, (white), (38,123,30,happybar))
    # time.sleep(3)

#button images
    water = pygame.image.load ("images/agua.png")
    tela.blit(water,(120, 395))

    morango = pygame.image.load ("images/morango.png")
    tela.blit(morango,(280, 390))

    lua = pygame.image.load ("images/lua.png")
    tela.blit(lua,(460, 390))
    
    #gatinho
    tela.blit(gatinhomaior,(200,140))

    #frame barra
    tela.blit(framebarra,(25,110))


    pygame.display.update()
 
pygame.quit()
 

