#imports
import pygame
from pygame.locals import *
from sys import exit
import time
from pygame import mixer

#inits
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

#IMAGES LOAD

#icons
bubbles = pygame.image.load ('images/bolhas.png')
coraçao = pygame.image.load ('images/coraçao.png')
sleepz =  pygame.image.load ('images/sleepz.png')
morango = pygame.image.load ("images/morango.png")
morangomord = pygame.image.load ("images/morangomord.png")
stain = pygame.image.load ('images/stain.png')
framebarra = pygame.image.load ('images/framebar.png')
#cat variations
cat = pygame.image.load ('images/cat.png')
bigcat = pygame.image.load ('images/bigcat.png')
sadcat = pygame.image.load ('images/sadcat.png')
sleepycat =  pygame.image.load ('images/sleepycat.png')
#fundo variations
fundo = pygame.image.load ("images/fundojogo.png")
fundoazul = pygame.image.load ('images/fundoazul.png')
fundobarra = pygame.image.load ('images/fundobarra.png')

#SOUNDS LOAD

#sounds
miausound = mixer.Sound('sounds/miausound.wav')
bubblesound = mixer.Sound('sounds/bubblesound.wav')
sleepsound = mixer.Sound('sounds/sleepsound.wav')
chewsound = mixer.Sound('sounds/chewsound.wav')
clicksound = mixer.Sound('sounds/clicksound.wav')
gameoversound = mixer.Sound('sounds/gameoversound.wav')
#music
mixer.music.load('sounds/backgroundmusic.wav')
mixer.music.play(-1)

#TELA

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("pet.com")

#BUTTON

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

#button cat
cat_img = pygame.image.load("images/bigcat.png").convert_alpha()
cat_img = button(200,140, cat_img, 1)

#TELAS

inicio = True
jogo = False
fim = False
telainicial=True

while telainicial:
    
    #tela inicio
    if inicio == True:
        for event in pygame.event.get():
            #fechar jogo no x
            if event.type == pygame.QUIT:
                telainicial=False
            #fechar tela inicio e abrir tela jogo quando clicar no espaço
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    clicksound.play()
                    inicio = False
                    jogo = True
        
        #fundo branco
        tela.fill(white)
     
        #corações
        if y  >= altura+100:
            y = 0
        y = y + 1
    
        tela.blit(coraçao,(50,y))
    
        tela.blit(coraçao,(440,-100 + y))
    
        tela.blit(coraçao,(550,-40 + y))
    
        #cat
        tela.blit(cat,(245,200))
    
        #TEXTO

        #texto 1
        txt='pet.com'                                                          
        fontetxt=pygame.font.Font('Minecraftia-Regular.ttf', 40)
        txttela = fontetxt.render(txt, 1, (black))      
        tela.blit(txttela,(230,100))    
        #texto 2
        txt2='Aperte espaço para jogar'                      
        fontetxt2=pygame.font.Font('Minecraftia-Regular.ttf', 22)       
        txttela2 = fontetxt2.render(txt2, 1, (black))        
        tela.blit(txttela2,(150,360))               
        pygame.display.update()
    
    #tela jogo
    elif jogo == True:
        
        #papel de parede jogo
        tela.blit(fundo,(0,0))

        #barra de felicide
        pygame.draw.rect(tela, (white), (38,happybar,30,230)) 
        tela.blit(fundobarra,(15, 353))
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

        #enquanto a barra não acaba ela se move
        if happybar<=355:   
            #movmento barra de felicidade
            pygame.draw.rect(tela, (white), (38,happybar,30,230))  
            happybar = happybar + 0.05                #velocidade
            tela.blit(fundobarra,(15, 353))
            tela.blit(framebarra,(25,110))
      
        #barra acaba = jogo acaba
        else:
            #gato triste
            tela.blit(fundo,(0,0))
            tela.blit(sadcat,(190,155))
            #som
            mixer.music.stop()
            gameoversound.play()
            #texto
            txtfim='fim do jogo'                                                          
            fontetxt=pygame.font.Font('Minecraftia-Regular.ttf', 40)
            txtfimtela = fontetxt.render(txtfim, 1, (black))      
            tela.blit(txtfimtela,(200,100))
            #fim do jogo
            pygame.display.update()   
            time.sleep(4)
            pygame.quit()
        
        #funcionalid banho
        if (agua_img.draw(tela)):    
            #images
            tela.blit(framebarra,(25,110))
            tela.blit(bubbles,(210, 80))
            #sounds                        
            bubblesound.play()
            #wait
            pygame.display.update()                                 
            time.sleep(5)
            #+10 felicidade
            if (happybar - 10 < 123):
                happybar = happybar + (123-happybar)
            else:
                happybar = happybar - 10

        #funcionalid comer
        if (morango_img.draw(tela)):
            #images
            tela.blit(stain,(295, 195)) 
            tela.blit(morangomord,(310, 220))
            #sounds
            chewsound.play()
            #wait
            pygame.display.update()  
            time.sleep(3)
            #+10 felicidade
            if (happybar - 10 < 123):
                happybar = happybar + (123-happybar)
            else:
                happybar = happybar - 10
 
        #funcionalid dormir
        if (lua_img.draw(tela)):  
            #images
            tela.blit(framebarra,(25,110))
            tela.blit(fundoazul,(107,0))
            tela.blit(sleepycat,(200,210))
            tela.blit(sleepz,(200,210))
            tela.blit(sleepz,(220,170))
            #sounds
            sleepsound.play()
            #wait
            pygame.display.update()
            time.sleep(5)
            #+10 felicidade
            if (happybar - 10 < 123):
                happybar = happybar + (123-happybar)
            else:
                happybar = happybar - 10

        #funcionalid pet
        if (cat_img.draw(tela)):
            #images
            tela.blit(coraçao,(370,120))
            #sounds
            miausound.play()
            #wait
            pygame.display.update() 
            time.sleep(1) 
            #+5 felicidade
            if (happybar - 10 < 123):
                happybar = happybar + (123-happybar)
            else:
                happybar = happybar - 5
            
        #fechar jogo no x
        for event in pygame.event.get():        
            if event.type == pygame.QUIT:
                telainicial=False

        pygame.display.update()
 
pygame.quit()
 

