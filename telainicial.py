import pygame
from sys import exit

#variáveis
white = (255,255,255)
coraçao = pygame.image.load ("coraçao.png")
gatinho = pygame.image.load ("gatinho.png")
largura = 640
altura = 480
x = 0
y = 0
 
#tela
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("pet.com")
pygame.draw.rect(tela, (white), (0,0,largura,altura))

telainicial=True
while telainicial==True:
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            telainicial=False
    pygame.time
    
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
    tela.blit(gatinho,(245,200))
 
    #texto
    txt='pet.com'                                
    pygame.font.init()                                
    fonte=pygame.font.get_default_font()              ##### fonte padrão
    fontesys=pygame.font.SysFont(fonte, 60)           ##### fonte
    txttela = fontesys.render(txt, 1, (0,0,0))        ##### cor
    tela.blit(txttela,(240,100))                      ##### posição
    pygame.display.update()                   