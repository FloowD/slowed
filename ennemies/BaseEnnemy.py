import pygame
from pygame.locals import *
from constants import *
from Player import *

class BaseEnnemy(pygame.sprite.Sprite):
    """
    Classe Ennemy
    """
    def __init__(self,spwan_x,spwan_y,max_left,max_right):
        #max_left : limite a gauche, max_right : limite a droite
        super().__init__()
        
        #self.image = pygame.image.load(image)
        #self.rect = self.image.get_rect()
        widthPerso, heightPerso = 32,32
        self.image = pygame.Surface((widthPerso, heightPerso))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()

        self.x_origin = spwan_x
        self.y_origin = spwan_y

        self.max_left= max_left
        self.max_right = max_right
        
        self.rect.x = self.x_origin
        self.rect.y = self.y_origin

        self.change_x = 5
        
    
        #100, 100, 50, 250
    def update(self):
        #change constament de direction
        
        if self.rect.x > self.max_right:
            self.change_x = -5
        if self.rect.x < self.max_left:
            self.change_x = 5

        self.rect.x += self.change_x