import pygame
from pygame.locals import *
from constants import *


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):

        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #self.image = pygame.image.load("plateforme.png")
        #self.rect.width = width
        #self.rect.height = height
        #self.rect = self.image.get_rect()
        #self.rect.x = self.x 
        #self.rect.y = self.y
        
        #self.s = pygame.Surface((0,0))
        #hit_box = pygame.Rect((x, y), (width, height))
        #self.rect = self.s.get_rect()
        #self.rect = pygame.draw.rect(s, GREY, hit_box)

    