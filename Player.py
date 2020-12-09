import pygame
from pygame.locals import *
from constants import *


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,speed):

        super().__init__()
        #Les coordonnées de spawn du joueur
        self.x_origin = x
        self.y_origin = y
        self.speed = speed

        # Stores if player is jumping or not.
        self.isjump = 0     
    
        # Force (v) up and mass m.
        self.v = 8
        self.m = 6

        self.isMoving = False

        #widthPerso, heightPerso = 32,32
        #self.image = pygame.Surface((widthPerso, heightPerso))
        self.image = pygame.image.load("images/sprites/player.png")
        self.image = pygame.transform.scale(self.image, (64,64))
        #self.image.fill(BLACK)
        self.rect = self.image.get_rect()

        self.rect.x = self.x_origin
        self.rect.y = self.y_origin


    def moveRight(self):
        self.rect.x = self.rect.x + self.speed
 
    def moveLeft(self):
        self.rect.x = self.rect.x - self.speed
 
    def jump(self):
        self.isjump = 1

    def update(self):
        if self.isjump:
            # Calculate force (F). F = mass * velocity
            
            F = (self.m * self.v)
            # Change position
            self.rect.y = self.rect.y - F

            # Change velocity
            self.v = self.v - 1

            # If ground is reached, reset variables.
            if self.rect.y >= 638:
                self.rect.y = 638
                self.isjump = 0
                self.v = 8 



    def wallCollision(self):
        #Gère la collision avec les murs
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= screenWidth-self.rect.height:
            self.rect.x = screenWidth-self.rect.height
            self.isJumping = False
        if self.rect.y <=0:
            self.rect.y = 0
        if self.rect.y >= screenHeight-self.rect.height:
            self.rect.y = screenHeight-self.rect.height


    def respawn(self):
        self.rect.x = self.x_origin
        self.rect.y = self.y_origin
