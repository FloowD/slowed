import os
import pygame
from pygame.locals import *
from constants import *
from Player import Player
from ennemies import Follower
import math

backg = pygame.image.load("images/sprites/background.png")
backg = pygame.transform.scale(backg, [x//RATIO for x in backg.get_size()])

level2 = pygame.image.load("images/levels/level 2.png")
level2 = pygame.transform.scale(level2, [x//RATIO for x in level2.get_size()])

end_point = pygame.image.load("images/sprites/endpoint.png")
end_point = pygame.transform.scale(end_point, (64,64))
#Fichier qui va être appelé dans le main et lancer les fonctions
#importantes pour le programme

spawn_x = 200
spwan_y = 1200

player = Player(spawn_x,spwan_y,15)
follower = Follower(700,600,player)

ennemies = []
ennemies.append(follower)

#Mettre tout les objet dans une liste
all_sprite_list = pygame.sprite.Group()
ennemy_list = pygame.sprite.Group()

all_sprite_list.add(player)
all_sprite_list.add(follower)

for e in ennemies:
    all_sprite_list.add(e)
    ennemy_list.add(e)


def game(screen):
    running = True
    while running:

    #Déplacement du joueur
        keys = pygame.key.get_pressed() 
            
        if (keys[K_RIGHT]):
            player.moveRight()
 
        if (keys[K_LEFT]):
            player.moveLeft()
 
        if (keys[K_UP]):
            player.jump()
 
        if (keys[K_ESCAPE]):
            running = False    

        ## EVENT
        for event in pygame.event.get():

            #FERMER
            if event.type == pygame.QUIT:
                running = False

            #Test si le joueur bouge
            if event.type == pygame.KEYDOWN:
                player.isMoving = True

            if event.type == pygame.KEYUP:
                player.isMoving = False
        
        ## END EVENT

        # TODO: DELETE
        if player.isMoving:
            follower.speed = [7,7]
        else:
            follower.speed = [2,2]

        ## Modification des coordonnées du joueur
        # Accélération

        #On actualise le fond pour voir correctement les affichages
        screen.blit(backg, [0,0])
        screen.blit(level2, [0,0])
        screen.blit(end_point,(860,20))

        #On actualise le joueur
        player.wallCollision()

        all_sprite_list.update()

        #Gère la collision et le respawn
        ennemy_hit_list = pygame.sprite.spritecollide(player, ennemy_list, False)

        for ennemies in ennemy_hit_list:
            player.respawn()
            follower.respwan()

        #Fait le blit de tous les sprites
        all_sprite_list.draw(screen)
        
        pygame.display.update()
        #On règle les FPS
        pygame.time.Clock().tick(FPS)

    print("Fin du jeu !")
    quit()


def chronometre():
    """Chronomètre pour le speedrun
    """
    