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

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Tamagochi<3")

while True:
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
    
    #texto
    txt='pet.com'                                 
    pygame.font.init()                                
    fonte=pygame.font.get_default_font()              ##### fonte padrão
    fontesys=pygame.font.SysFont(fonte, 60)           ##### fonte
    txttela = fontesys.render(txt, 1, (0,0,0))        ##### cor
    tela.blit(txttela,(240,100))                      ##### posição
    pygame.display.update()                        

    

    pygame.display.update()
    