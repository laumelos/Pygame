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
black = (0,0,0)
largura = 640
altura = 480
happybar = 123
x = 0
y = 0

#imagens load
bubbles = pygame.image.load ('images/bolhas.png')
coraçao = pygame.image.load ('images/coraçao.png')
cat = pygame.image.load ('images/cat.png')
bigcat = pygame.image.load ('images/bigcat.png')
sleepycat =  pygame.image.load ('images/sleepycat.png')
fundo = pygame.image.load ("images/fundojogo.png")
fundoazul = pygame.image.load ('images/fundoazul.png')
framebarra = pygame.image.load ('images/framebar.png')
fundobarra = pygame.image.load ('images/fundobarra.png')
teste = pygame.image.load ('images/teste.png')

#sounds load
bubblesound = pygame.mixer.Sound('sounds/539823__ristooooo1__bubbles-001.wav')
sleepsound = pygame.mixer.Sound('sounds/gatinhodormindo.wav')

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
# morango_img = pygame.image.load ("images/morango.png").convert_alpha()
# morango_img = button(280, 390, morango_img, 1)

#button lua
lua_img = pygame.image.load("images/lua.png").convert_alpha()
lua_img = button(460, 390,lua_img, 1)

cat_img = pygame.image.load("images/bigcat.png").convert_alpha()
cat_img = button(200,140, cat_img, 1)

#TELA
inicio = True
jogo = False
telainicial=True
while telainicial==True:
    if inicio == True:
        for event in pygame.event.get():
        #quit game
            if event.type == pygame.QUIT:
                telainicial=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    inicio = False
                    jogo = True
        #pygame.time
        
        #atualiz tela
        pygame.draw.rect(tela, (white), (0,0,largura,altura))
        
        #corações
        if y  >= altura:
            y = 0
        y = y + 1
    
        tela.blit(coraçao,(x,y))
    
        tela.blit(coraçao,(320,-80 + y))
    
        tela.blit(coraçao,(440,-40 + y))
    
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
    
    
    if jogo == True:
        #barra
        tela.blit(fundo,(0,0))
        pygame.draw.rect(tela, (white), (38,happybar,30,230)) 
        tela.blit(teste,(15, 353))
        tela.blit(framebarra,(25,110))
  
        #button images
        water = pygame.image.load ("images/agua.png")
        tela.blit(water,(120, 395))

        # morango = pygame.image.load ("images/morango.png")
        # tela.blit(morango,(280, 390))

        lua = pygame.image.load ("images/lua.png")
        tela.blit(lua,(460, 390))

        cat = pygame.image.load ("images/bigcat.png")
        tela.blit(cat,(200,140))

        if happybar<=355:   
            pygame.draw.rect(tela, (white), (38,happybar,30,230))  
            happybar = happybar + 0.008     #velocidade
            tela.blit(teste,(15, 353))
            tela.blit(framebarra,(25,110))           
        else:   #perdeu
            pygame.quit()
        
        #funcionalid banho
        if (agua_img.draw(tela)):    

            tela.blit(framebarra,(25,110))
            tela.blit(bubbles,(210, 80))                           
            pygame.mixer.Sound.play(bubblesound)
            pygame.mixer.music.stop()
            pygame.display.update()                                 
            time.sleep(6)
            tela.blit(bigcat,(200,140))
            tela.blit(fundo,(0,0))

            happybar = happybar - 10
        
        #funcionalid dormir
        if (lua_img.draw(tela)):    

            tela.blit(framebarra,(25,110))
            tela.blit(fundoazul,(107,0))
            tela.blit(sleepycat,(200,210))
            tela.blit(framebarra,(25,110))
            pygame.mixer.Sound.play(sleepsound)
            pygame.mixer.music.stop()
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
 

