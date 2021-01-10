import pygame
from pygame.locals import *
from constants import *
from Player import *
from time import time

class EndPoint(pygame.sprite.Sprite):
    def __init__(self,x,y,tabPosition):
        #tabPosition -> tab de tuple pour les coordonnées 
        #intervalle -> temps sépratant chaque tp
        super().__init__()
        self.tempsPred = int(time())
        self.image = pygame.image.load("images/sprites/endpoint.png")
        self.image = pygame.transform.scale(self.image, (64,64))
        
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
        self.indice = 0

        self.tabPosition = tabPosition

    def nextPosition(self):
        try:
            self.rect.x = self.tabPosition[self.indice + 1 ][0]
            self.rect.y = self.tabPosition[self.indice + 1 ][1]
            self.indice += 1
        except IndexError:
            self.rect.x = self.tabPosition[0][0]
            self.rect.y = self.tabPosition[0][1]
            self.indice = 0

    def update(self):
        if len(self.tabPosition) != 0 :
            if (int(time()) - self.tempsPred) > 1:
                if int(time()) % 4== 0:
                    self.nextPosition()
                    self.tempsPred = int(time())

        

    
        
        
        