import pygame
from pygame.locals import *
from constants import *
from Player import *
import math

class Follower(pygame.sprite.Sprite):
    """
    Class de l'ennemi qui chase en permanance le joueur
    """
    def __init__(self,spwan_x,spwan_y,target):
        
        super().__init__()
        #Les coordonnées du joueur
        
        #self.image = pygame.image.load(image)
        #self.rect = self.image.get_rect()
        widthPerso, heightPerso = 32,32
        self.image = pygame.Surface((widthPerso, heightPerso))
        self.image.fill(RED)
        self.rect = self.image.get_rect()

        self.target = target
        self.x_origin = spwan_x
        self.y_origin = spwan_y
        
        self.rect.x = self.x_origin
        self.rect.y = self.y_origin
        
        self.speed = [7,7]

        self.floating_point_x = self.rect.centerx
        self.floating_point_y = self.rect.centery
    

    def calcul_angle(self):
        dest_x = self.target.rect.centerx
        dest_y = self.target.rect.centery

        x_diff = dest_x - self.rect.centerx
        y_diff = dest_y - self.rect.centery
        angle = math.atan2(y_diff, x_diff)

        return angle


    def update(self):
        angle = self.calcul_angle()

        self.change_x = math.cos(angle) * self.speed[0]
        self.change_y = math.sin(angle) * self.speed[1]

        # Les points flotant x et y donne une position plus precise.
        self.floating_point_y += self.change_y
        self.floating_point_x += self.change_x
 
        # On convertit ces valeur en entier pour rect.x
        # et rect.y pour déplacer le monstre
        self.rect.y = int(self.floating_point_y)
        self.rect.x = int(self.floating_point_x)

    def respwan(self):
        self.rect.x = self.x_origin
        self.rect.y = self.y_origin