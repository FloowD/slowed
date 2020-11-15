import pygame
from pygame.locals import *
from constants import *
from Player import *

#Fichier qui va être appelé dans le main et lancer les fonctions
#importantes pour le programme

player = Player(100,100,[0,0])

def game(screen):
    running = True
    while running:
        for event in pygame.event.get():
            keyPressed = pygame.key.get_pressed()
            #FERMER
            if event.type == pygame.QUIT:
                running = False
               #Déplacement du joueur
            elif event.type == pygame.KEYDOWN:
                if keyPressed[K_w]:
                    player.move("UP")
                if keyPressed[K_s]:
                    player.move("DOWN")
                if keyPressed[K_a]:
                    player.move("LEFT")
                if keyPressed[K_d]:
                    player.move("RIGHT")
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player.speed[1] = 0
                elif event.key == pygame.K_a or event.key == pygame.K_d:
                    player.speed[0] = 0
        #---Modification des coordonnées du joueur
        player.rect.x += player.speed[0]
        player.rect.y += player.speed[1]
        screen.fill(BLACK)
        player.update()
        screen.blit(player.image, player.rect)
        pygame.display.update()
        pygame.time.Clock().tick(FPS)
        
    print("Fin du jeu !")
    quit()