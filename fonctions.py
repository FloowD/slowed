import pygame
from pygame.locals import *
from constants import *
from Player import *
from Ennemy import *
from ChasingEnnemy import *

#Fichier qui va être appelé dans le main et lancer les fonctions
#importantes pour le programme
spawn_x = 100
spwan_y = 1200
player = Player(spawn_x,spwan_y,[0,0])
ennemy = Ennemy(screenWidth/2,screenHeight-40,[0,5])
chasingEnnemy = ChasingEnnemy(500,500)

#Mettre tout les objet dans une liste
all_sprite_list = pygame.sprite.Group()
all_sprite_list.add(player)
all_sprite_list.add(ennemy)
all_sprite_list.add(chasingEnnemy)

ennemy_list = pygame.sprite.Group()
ennemy_list.add(ennemy)
ennemy_list.add(chasingEnnemy)

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
            
            
            elif event.type == pygame.KEYUP:
                player.isMoving = False
                if event.key == pygame.K_w or event.key == pygame.K_s:
                 player.speed[1] = 0
                elif event.key == pygame.K_a or event.key == pygame.K_d:
                    player.speed[0] = 0
            
        if player.isMoving:
            if ennemy.rect.y >= screenHeight-ennemy.rect.height:
                ennemy.speed[1] = -5
            if ennemy.rect.y <= 500:
                ennemy.speed[1] = 5
        else:
            if ennemy.rect.y >= screenHeight-ennemy.rect.height:
                ennemy.speed[1] = -2
            if ennemy.rect.y <= 500:
                ennemy.speed[1] = 2
                
        #---Modification des coordonnées du joueur
        player.rect.x += player.speed[0]
        player.rect.y += player.speed[1]
        ennemy.rect.y += ennemy.speed[1]
        #On actualise le fond pour voir correctement les affichages
        screen.fill(BLACK)
        #On actualise le joueur
        player.wallCollision()
        player.gravity()
        
        all_sprite_list.update()

        #Gère la collision et le respawn
        ennemy_hit_list = pygame.sprite.spritecollide(player, ennemy_list, False)
                
        for ennemys in ennemy_hit_list:
            player.rect.x = spawn_x
            player.rect.y = spwan_y

        #Fait le blit de tous les sprites
        all_sprite_list.draw(screen)
        
        pygame.display.update()
        #On règle les FPS
        pygame.time.Clock().tick(FPS)
        
    print("Fin du jeu !")
    quit()