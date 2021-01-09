#On met dans ce fichier toutes les constantes dont on aura besoin dans le jeu
import pygame
from pygame.locals import *


pygame.init()
FPS = 60
RATIO = 2
screenWidth, screenHeight = 1872//RATIO, 1404//RATIO #936 / 702
#screenWidth, screenHeight = 1280, 720
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
GREY = (100,100,100)

score = 0
font = pygame.font.Font(None, 25)

#Variable pour le niveau
Niveau = {
    0 : "menu",
    1 : "Niveau1",
    2 : "Niveau2",
    3 : "Niveau3"
}

