import pygame
from pygame.locals import *
from constants import *
from Platform import *
from ennemies import Follower
from ennemies import BaseEnnemy

#--------------- DEBUT CONSTANTS PLATFORM----------------
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

platformNiv2 = [
    Platform(670, 270, 80, 20, GREY),
    Platform(820,400, 80, 20, GREY),
    Platform(820, 160, 80, 20, GREY),
    Platform(200, 150, 500, 20, GREY),
    Platform(370, 500, 350, 30, GREY),
    Platform(70, 50, 30, 140, GREY)
    #Platform(369, 425, 256, 854, BLUE)
]

all_levels = [platformNiv1, platformNiv2]
#--------------- FIN CONSTANTS PLATFORM----------------

#--------------- DEBUT CONSTANTS ENNEMIES----------------
ennemiesNiv1 = [BaseEnnemy(100, 100, 50, 250, True) 
                #Follower(750,600,player)
                ]

ennemiesNiv2 = [
    BaseEnnemy(300, 600, 520, 670, False),
    BaseEnnemy(400, 468, 400, 600, True),
    BaseEnnemy(600, 20, 0, 110, False),
    BaseEnnemy(250, 118, 250, 550, True),
    BaseEnnemy(200, 20, 0, 110, False)
    ]

all_ennemies = [ennemiesNiv1, ennemiesNiv2]
#--------------- FIN CONSTANTS ENNEMIES----------------

#--------------- DEBUT CONSTANTS JOUEUR + FIN----------------
player_spwan = ((50, 1200), (800, 1100), (400, 800))
endpoint_spwan = ((850,150), (0,100), (800,800))
#--------------- FIN CONSTANTS JOUEUR + FIN----------------