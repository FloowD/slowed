import pygame
from pygame.locals import *
from constants import *
from fonctions import *
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Slowed')
#---Main Loop ---
game(screen)

pygame.quit()
