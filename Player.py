import pygame
from pygame.locals import *
from constants import *

#dt = clock.tick(FPS) / 1000

class Player(pygame.sprite.Sprite):
    def __init__(self,x=0,y=0,speed=[0,0]):
        
        super().__init__()
        #Les coordonnées du joueur
        self.x = x
        self.y = y
        
        #La vitesse de déplacement
        

        #self.image = pygame.image.load(image)
        #self.rect = self.image.get_rect()
        widthPerso, heightPerso = 32,32
        self.image = pygame.Surface((widthPerso, heightPerso))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = speed
        

    def move(self,direction):
        #direction -> paramètre a rentrer en fonction sur quel touche 
        #du clavier on appuie pour se déplacer
        if direction == "UP":
            self.speed[1] = -5
        if direction == "DOWN":
            self.speed[1] = 5
        if direction == "LEFT":
            self.speed[0] = -5
        if direction == "RIGHT":
            self.speed[0] = 5
        
    def update(self):
        self.rect.move_ip(*self.speed)
        