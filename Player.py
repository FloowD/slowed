import pygame
from pygame.locals import *
from constants import *


class Player(pygame.sprite.Sprite):
    def __init__(self,x=0,y=0,speed=[0,0]):
        
        super().__init__()
        #Les coordonnées du joueur
        self.x = x
        self.y = y
        
        #self.image = pygame.image.load(image)
        #self.rect = self.image.get_rect()
        widthPerso, heightPerso = 32,32
        self.image = pygame.Surface((widthPerso, heightPerso))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = speed
        self.isJumping = False
        self.jumpCount = 10

        #Variable pour tester si le joueur bouge
        self.isMoving = False
        
        

    def move(self,direction):
        #direction -> paramètre a rentrer en fonction sur quel touche 
        #du clavier on appuie pour se déplacer
        if not(self.isJumping):
            if direction == "UP":
                self.speed[1] = -5
            if direction == "DOWN":
                self.speed[1] = 5
            if direction == "LEFT":
                self.speed[0] = -5
            if direction == "RIGHT":
                self.speed[0] = 5
            if direction == "SAUT" and self.rect.y+self.rect.height >= screenHeight:
                self.isJumping = True
        
        

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
    
    def gravity(self):
        #Fonction qui gère la gravité
        self.rect.y += 3.5
    
    #def jump(self):
        #Faut un saut
     #   isJumping = True
        
        
        
    def update(self):
        self.rect.move_ip(*self.speed)

        if self.isJumping:
            if self.jumpCount >= 0:
                self.rect.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                self.jumpCount -= 1
            else: 
                self.jumpCount = 10
                self.isJumping = False
        