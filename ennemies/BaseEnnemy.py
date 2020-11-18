import pygame
from pygame.locals import *
from constants import *
from Player import *

class Ennemy(pygame.sprite.Sprite):
    """
    Classe Ennemy
    """
    def __init__(self,x=0,y=0,speed=[0,0]):
        
        super().__init__()
        #Les coordonnées du joueur
        self.x = x
        self.y = y
        
        #self.image = pygame.image.load(image)
        #self.rect = self.image.get_rect()
        widthPerso, heightPerso = 32,32
        self.image = pygame.Surface((widthPerso, heightPerso))
        self.image.fill(RED)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = speed
        
    
            
    def update(self):
        self.rect.move_ip(*self.speed)