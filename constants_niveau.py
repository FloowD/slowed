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
    Platform(480, 520, 20, 200, RED),
    Platform(670, 270, 80, 20, GREY),
    Platform(820,400, 80, 20, GREY),
    Platform(260, 270, 320, 20, GREY),
    Platform(370, 500, 350, 30, GREY),
    Platform(0, 240, 110, 30, RED),
    Platform(110, 270, 30, 110, RED),
    Platform(10, 500, 70, 200, GREEN),
    Platform(100, 80, 550, 30, GREY),
    Platform(10, 200, 120, 30, GREY)
    #Platform(369, 425, 256, 854, BLUE)
]

all_levels = [platformNiv1, platformNiv2]
#--------------- FIN CONSTANTS PLATFORM----------------

#--------------- DEBUT CONSTANTS ENNEMIES----------------
ennemiesNiv1 = [BaseEnnemy(100, 100, 50, 250, True) 
                #Follower(750,600,player)
                ]

ennemiesNiv2 = [
    BaseEnnemy(300, 300, 320, 500, False),
    BaseEnnemy(400, 468, 400, 600, True),
    BaseEnnemy(600, 250, 200, 350, False),
    BaseEnnemy(250, 238, 320, 470, True),
    ]

all_ennemies = [ennemiesNiv1, ennemiesNiv2]
#--------------- FIN CONSTANTS ENNEMIES----------------

#--------------- DEBUT CONSTANTS JOUEUR + FIN----------------
player_spwan = ((50, 1200), (800, 1100), (400, 800))
endpoint_spwan = ((850,150), (15,280), (800,800))
#--------------- FIN CONSTANTS JOUEUR + FIN----------------