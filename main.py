import pygame
from pygame.locals import *
from constants import *
from fonctions import *
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Slowed')
#---Main Loop ---
game(screen, True)
#main_menu()


pygame.quit()
