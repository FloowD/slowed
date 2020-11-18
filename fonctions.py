import pygame
from pygame.locals import *
from constants import *
from Player import Player
#from ennemies import Follower

backg = pygame.image.load("images/sprites/background.png")
backg = pygame.transform.scale(backg, [x//RATIO for x in backg.get_size()])

level2 = pygame.image.load("images/levels/level 2.png")
level2 = pygame.transform.scale(level2, [x//RATIO for x in level2.get_size()])
#Fichier qui va être appelé dans le main et lancer les fonctions
#importantes pour le programme
spawn_x = 100
spwan_y = 1200

player = Player(spawn_x,spwan_y,[0,0])

ennemies = []
#ennemies.append(Follower(500,500))

#Mettre tout les objet dans une liste
all_sprite_list = pygame.sprite.Group()
ennemy_list = pygame.sprite.Group()

all_sprite_list.add(player)

for e in ennemies:
    all_sprite_list.add(e)
    ennemy_list.add(e)

def game(screen):
    running = True
    while running:
        ## EVENT
        for event in pygame.event.get():
            keyPressed = pygame.key.get_pressed()

            #FERMER
            if event.type == pygame.QUIT:
                running = False

           #Déplacement du joueur
            if event.type == pygame.KEYDOWN:
                player.isMoving = True
                if keyPressed[K_w]:
                    player.move("UP")
                if keyPressed[K_s]:
                    player.move("DOWN")
                if keyPressed[K_a]:
                    player.move("LEFT")
                if keyPressed[K_d]:
                    player.move("RIGHT")
                if event.key == pygame.K_SPACE:
                    player.move("SAUT")

            if event.type == pygame.KEYUP:
                player.isMoving = False
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player.speed[1] = 0
                elif event.key == pygame.K_a or event.key == pygame.K_d:
                    player.speed[0] = 0
        ## END EVENT

        # TODO: DELETE
#         if player.isMoving:
#             if ennemy.rect.y >= screenHeight-ennemy.rect.height:
#                 ennemy.speed[1] = -5
#             if ennemy.rect.y <= 500:
#                 ennemy.speed[1] = 5
#         else:
#             if ennemy.rect.y >= screenHeight-ennemy.rect.height:
#                 ennemy.speed[1] = -2
#             if ennemy.rect.y <= 500:
#                 ennemy.speed[1] = 2

        ## Modification des coordonnées du joueur
        # Accélération
        player.rect.x += player.speed[0] 
        player.rect.y += player.speed[1]
        #ennemy.rect.y += ennemy.speed[1]

        #On actualise le fond pour voir correctement les affichages
        screen.blit(backg, [0,0])
        screen.blit(level2, [0,0])

        #On actualise le joueur
        player.wallCollision()
        player.gravity()

        all_sprite_list.update()

        #Gère la collision et le respawn
        ennemy_hit_list = pygame.sprite.spritecollide(player, ennemy_list, False)

        for ennemies in ennemy_hit_list:
            player.respawn()

        #Fait le blit de tous les sprites
        all_sprite_list.draw(screen)

        pygame.display.update()
        #On règle les FPS
        pygame.time.Clock().tick(FPS)

    print("Fin du jeu !")
    quit()
