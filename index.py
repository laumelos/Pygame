from typing import List
import pygame
from pygame.locals import *
from sys import exit
import time
import pygame.sprite
from pygame import mixer
 
pygame.init()
pygame.font.init()
pygame.mixer.init()

#variáveis
white = (255,255,255)
black = (0,0,0)
largura = 640
altura = 480
happybar = 123
y = 0

#imagens load
bubbles = pygame.image.load ('images/bolhas.png')
coraçao = pygame.image.load ('images/coraçao.png')
cat = pygame.image.load ('images/cat.png')
bigcat = pygame.image.load ('images/bigcat.png')
sadcat = pygame.image.load ('images/sadcat.png')
sleepycat =  pygame.image.load ('images/sleepycat.png')
sleepz =  pygame.image.load ('images/sleepz.png')
fundo = pygame.image.load ("images/fundojogo.png")
fundoazul = pygame.image.load ('images/fundoazul.png')
framebarra = pygame.image.load ('images/framebar.png')
fundobarra = pygame.image.load ('images/fundobarra.png')
teste = pygame.image.load ('images/teste.png')
morango = pygame.image.load ("images/morango.png")
morangomord = pygame.image.load ("images/morangomord.png")
stain = pygame.image.load ('images/stain.png')

#sounds load
bubblesound = mixer.Sound('sounds/539823__ristooooo1__bubbles-001.wav')
sleepsound = mixer.Sound('sounds/gatinhodormindo.wav')
mixer.music.load('sounds/backgroundmusic.wav')
mixer.music.play(-1)

#tela
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("pet.com")

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

cat_img = pygame.image.load("images/bigcat.png").convert_alpha()
cat_img = button(200,140, cat_img, 1)

#TELA
inicio = True
jogo = False
fim = False
telainicial=True

while telainicial:
    
    if inicio == True:
        for event in pygame.event.get():
        #quit game
            if event.type == pygame.QUIT:
                telainicial=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    inicio = False
                    jogo = True
        
        #atualiz tela
        tela.fill(white)
     
        #corações
        if y  >= altura+100:
            y = 0
        y = y + 1
    
        tela.blit(coraçao,(50,y))
    
        tela.blit(coraçao,(440,-100 + y))
    
        tela.blit(coraçao,(550,-40 + y))
    
        #gatinho
        tela.blit(cat,(245,200))
    
        #texto
        txt='pet.com'                                                          
        fonte=pygame.font.Font('Minecraftia-Regular.ttf', 40)
        txttela = fonte.render(txt, 1, (black))      
        tela.blit(txttela,(230,100))    

        txt2='Aperte espaço para jogar'                      
        fonte=pygame.font.Font('Minecraftia-Regular.ttf', 22)       
        txttela = fonte.render(txt2, 1, (black))        
        tela.blit(txttela,(150,360))               
        pygame.display.update()
    
    elif jogo == True:
        
        #barra
        tela.blit(fundo,(0,0))
        pygame.draw.rect(tela, (white), (38,happybar,30,230)) 
        tela.blit(teste,(15, 353))
        tela.blit(framebarra,(25,110))
  
        #button images
        water = pygame.image.load ("images/agua.png")
        tela.blit(water,(120, 395))

        morango = pygame.image.load ("images/morango.png")
        tela.blit(morango,(280, 390))

        lua = pygame.image.load ("images/lua.png")
        tela.blit(lua,(460, 390))

        cat = pygame.image.load ("images/bigcat.png")
        tela.blit(cat,(200,140))

        if happybar<=355:   
            pygame.draw.rect(tela, (white), (38,happybar,30,230))  
            happybar = happybar + 0.04     #velocidade
            tela.blit(teste,(15, 353))
            tela.blit(framebarra,(25,110))
      
        else:
            tela.blit(fundo,(0,0))
            tela.blit(sadcat,(190,155))
        
            txtfim='fim do jogo'                                                          
            fonte=pygame.font.Font('Minecraftia-Regular.ttf', 40)
            txttela = fonte.render(txtfim, 1, (black))      
            tela.blit(txttela,(200,100))
            pygame.display.update()   
            time.sleep(6) 
            pygame.quit()
        
        #funcionalid banho
        if (agua_img.draw(tela)):    

            tela.blit(framebarra,(25,110))
            tela.blit(bubbles,(210, 80))                           
            bubblesound.play()
            pygame.display.update()                                 
            time.sleep(6)
            tela.blit(bigcat,(200,140))
            tela.blit(fundoazul,(0,0))

            happybar = happybar - 10

        if (morango_img.draw(tela)):
            tela.blit(stain,(295, 195)) 
            tela.blit(morangomord,(310, 220)) 
            pygame.display.update()  
            time.sleep(4)
            
            
            
        #funcionalid dormir
        if (lua_img.draw(tela)):  

            tela.blit(framebarra,(25,110))
            tela.blit(fundoazul,(107,0))
            tela.blit(sleepycat,(200,210))
            tela.blit(sleepz,(200,210))
            tela.blit(sleepz,(220,170))
            sleepsound.play()
            pygame.display.update()
            time.sleep(4)
            tela.blit(fundo,(0,0))

            happybar = happybar - 10
            
        #quit game x
        for event in pygame.event.get():        
            if event.type == pygame.QUIT:
                telainicial=False

        pygame.display.update()
 
pygame.quit()
 

