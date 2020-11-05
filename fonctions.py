import pygame
from pygame.locals import *
from constants import *
from Player import *

#Fichier qui va être appelé dans le main et lancer les fonctions
#importantes pour le programme


def game(screen):
    running = True
    while running:
        for event in pygame.event.get():
            #FERMER
            if event.type == pygame.QUIT:
                running = False
