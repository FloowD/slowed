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
        self.isdroping = False
        self.isGoingUp = False
        self.isGoingLeft = False
        self.isGoingRight = False

        self.image = pygame.image.load("images/sprites/player.png")
        self.image = pygame.transform.scale(self.image, (64,64))
        #self.image.fill(BLACK)
        self.rect = self.image.get_rect()

        self.rect.x = self.x_origin
        self.rect.y = self.y_origin

        


    def moveRight(self):
        self.rect.x = self.rect.x + self.speed
        self.isGoingRight = True
 
    def moveLeft(self):
        self.rect.x = self.rect.x - self.speed
        self.isGoingLeft = True
 
    def jump(self):
        self.v = 8
        self.isjump = 1

    

    def update(self, all_platform_list):
        #saute
        #v = 8
        #si v<0 on descend
        self.verification_vitesse()
        if not(self.isjump):
            self.drop()

        else :
            F = (self.m * self.v)
            self.rect.y = self.rect.y - F
            self.v = self.v - 1
        #Collision avec le mur
        platform_hit_list = pygame.sprite.spritecollide(self, all_platform_list, False)

        for p in platform_hit_list:
            if p.color != (255,0,0):
                #si la platform est rouge -> dead
                if self.isGoingUp:
                    self.rect.top = p.rect.bottom
                
                elif self.isdroping:
                    self.rect.bottom = p.rect.top
                    if p.color == (0,0,255):
                        self.jump()
                    else:
                        self.isjump = 0
                        self.v = 0
                
                elif self.isGoingLeft:
                    self.rect.left = p.rect.right
                
                elif self.isGoingRight:
                    self.rect.right = p.rect.left
            
            else:
                self.respawn()
        #Gestion de la collision avec les bords de l'écran
        self.wallCollision()

        #On remet le mouvement gauche et droite a False
        self.isGoingLeft, self.isGoingRight = False, False



    def verification_vitesse(self):
        if self.v > 0:
            self.isdroping = False
            self.isGoingUp = True
        else:
            self.isdroping = True
            self.isGoingUp = False


    def drop(self):
        self.rect.y += 6
        
    def collide(self, all_platform_list):
        collision = False
        y_platform = 0
        y_width_platform = 0
        platform_collision_list = pygame.sprite.spritecollide(self, all_platform_list, False)
        for platform in platform_collision_list:
            collision = True
            y_platform = platform.rect.y
            y_width_platform = platform.rect.y + platform.rect.width

        return collision,y_platform,y_width_platform




    def wallCollision(self):
        #Gère la collision avec les murs
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= screenWidth-self.rect.height:
            self.rect.x = screenWidth-self.rect.height
        if self.rect.y <=0:
            self.rect.y = 0
        if self.rect.y >= screenHeight-self.rect.height:
            self.rect.y = screenHeight-self.rect.height
            self.isjump = False
            self.v = 0


    def respawn(self):
        self.rect.x = self.x_origin
        self.rect.y = self.y_origin
