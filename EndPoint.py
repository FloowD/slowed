import pygame
from pygame.locals import *
from constants import *
from Player import *

class EndPoint(pygame.sprite.Sprite):
    def __init__(self,x,y):

        super().__init__()
        self.image = pygame.image.load("images/sprites/endpoint.png")
        self.image = pygame.transform.scale(self.image, (64,64))
        
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y

