import pygame
from pygame.locals import *
from constants import *
from fonctions import *
from menu import *
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Slowed')
#---Main Loop ---
main_menu(screen)
#main_menu()


pygame.quit()
