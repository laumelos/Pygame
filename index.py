import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#variáveis
white = (255,255,255)
coraçao = pygame.image.load ("coraçao.png")
gatinho = pygame.image.load ("gatinho.png")
largura = 640
altura = 480
x = 0
y = 0
telainicial=True

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Tamagochi<3")

class Botao(pygame.sprite.Sprite):
    def __init__(self,*groups):
        self.rect = pygame.draw.rect(tela,(235,103,155,90),(xbut,ybut,largbut,altbut)).convert_alpha()
        self.touche = False

        if self.rect.collidepoit (self.MousePos):
            if self.self.mouse[0]:
                self.touche = True
                pygame.mouse.get_rel()
            else: 
                self.touche = False

        pass

while telainicial==True:
    for event in pygame.event.get():
        if event.type== QUIT:
            pygame.quit()
            exit()
    fundo = pygame.draw.rect(tela, (white), (0,0,largura,altura))
    
    #TELA INICIAL

    #gatinho
    tela.blit(gatinho,(245,200))

    #corações
    tela.blit(coraçao,(x,y,0,0))
    if y  >= altura:
        y = 0
    y = y + 1

    tela.blit(coraçao,(320,30))

    tela.blit(coraçao,(440,70))

    #button
    xbut = 240
    ybut = 360
    largbut = 150
    altbut = 60

    '''

    pygame.draw.rect(tela,(235,103,155,90),(xbut,ybut,largbut,altbut))

    self.mouse = pygame.mouse.get_pressed()
    self.MousePos = pygame.mouse.get_pos()


    
    if(mouse[0] > x and mouse[0] < x+largura and mouse[1] > y and mouse[1] < y+altura):
        telainicial==False
        pygame.draw.rect(tela,(0,0,0),(xbut,ybut,largbut,altbut))
  '''
     


    
    #texto
    txt='pet.com'                                 
    pygame.font.init()                                
    fonte=pygame.font.get_default_font()              ##### fonte padrão
    fontesys=pygame.font.SysFont(fonte, 60)           ##### fonte
    txttela = fontesys.render(txt, 1, (0,0,0))        ##### cor
    tela.blit(txttela,(240,100))                      ##### posição
    pygame.display.update()                        

    

    pygame.display.update()
    