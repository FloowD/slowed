import pygame
from pygame.locals import *
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self,x=0,y=0,velocity=10,image="images/player.png"):
        super().__init__()
        #Les coordonnées du joueur
        self.x = x
        self.y = y
        #La vitesse de déplacement
        self.velocity = velocity

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

    def move(self,direction):
        #direction -> paramètre a rentrer en fonction sur quel touche 
        #du clavier on appuie pour se déplacer
        if direction == "UP":
            self.rect.x -= velocity
        if direction == "DOWN":
            self.rect.x += velocity
        if direction == "RIGHT":
            self.rect.y += velocity
        if direction == "RIGHT":
            self.rect.y -= velocity
        

        #collision avec le mur
        if self.rect.left <0 or self.rect.right > screenWidth:
            self.velocity = self.velocity

    def update(self):
        self.rect.move_ip(*self.velocity)
