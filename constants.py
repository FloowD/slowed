#On met dans ce fichier toutes les constantes dont on aura besoin dans le jeu
import pygame
from pygame.locals import *
from Platform import *
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

#Tableau de platform par niveau
platformNiv1 = [
    Platform(150, 620, 50, 20, GREY),
    Platform(300, 520, 100, 20, GREY),
    Platform(560, 300, 120, 20, GREY),
    Platform(320, 100, 100, 150, GREY),
    Platform(870, 550, 66, 152, GREEN),
    Platform(600, 120, 45, 20, GREY),
    Platform(100, 250, 73, 94, GREY),
    Platform(720, 470, 45, 45, GREY),
    Platform(440, 380, 45, 60, GREEN)
]