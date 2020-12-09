
import pygame
import SlowedImages
import math
pygame.init()

# création fond d'écran

pygame.display.set_caption("slowed")
screen = pygame.display.set_mode((1024, 768))

running = True
background = pygame.image.load('SlowedImages/level1.png')

# création de flipper
import pygame
pygame.init()

# création de la classe flipper
class Flipper(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load('SlowedImages/flipper.png')
        self.rect = self.image.get_rect(center= (500, 300))
        self.rect.x = 500
        self.rect.y = 300

Flipper = Flipper()
angle = 0


# boucle tant que cette condition est vraie
while running:
    # appliquer l'arrière plan de notre jeu
    screen.blit(background, (0,0))
    pygame.display.flip()

    # appliquer l'image de flipper
    screen.blit(flipper_rotated, flipper_rotated_rect)
    # On va rajouter un degré à l'angle à chaque tour
    angle += 1
    flipper_rotated,flipper_rotated_rect =rotate(flipper, angle)

    # si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print ("Fermeture du jeu")











