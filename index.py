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

#tela
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Tamagochi<3")
pygame.draw.rect(tela, (white), (0,0,largura,altura))

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


#TELA INICIAL
telainicial=True
while telainicial==True:
    if (button_img.draw(tela)):                             
        pygame.quit()
        exit()
    
    for event in pygame.event.get():
		#quit game
        if event.type == pygame.QUIT:
            telainicial=False

    pygame.draw.rect(tela, (white), (0,0,largura,altura))

    imgbutton = pygame.image.load ("buttonjogo.png")
    tela.blit(imgbutton,(240, 360))

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

    pygame.display.update()

pygame.quit()
