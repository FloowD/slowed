import os
import sys
import pygame
from pygame.locals import *
from constants import *
from constants_niveau import *
from Player import Player
from ennemies import Follower
from ennemies import BaseEnnemy
from Platform import *
from EndPoint import *
import math

backg = pygame.image.load("images/sprites/background.png")
backg = pygame.transform.scale(backg, [x//RATIO for x in backg.get_size()])

#level2 = pygame.image.load("images/levels/level 2.png")
#level2 = pygame.transform.scale(level2, [x//RATIO for x in level2.get_size()])

#Fichier qui va être appelé dans le main et lancer les fonctions
#importantes pour le programme


#follower = Follower(750,600,player)
#follower2 = Follower(100,0,player)


#baseEnnemy = BaseEnnemy(100, 100, 50, 250)

#ennemies = []
#ennemies.append(follower)
#ennemies.append(follower2)
#ennemies.append(baseEnnemy)

#ennemies = [ennemiesNiv1, ennemiesNiv2]

#Mettre tout les objet dans une liste
all_sprite_list = pygame.sprite.Group()
ennemy_list = pygame.sprite.Group()
endPoint_Collision = pygame.sprite.Group()
joueur_tout_seul = pygame.sprite.Group()
all_platform_list = pygame.sprite.Group()
#-------Platform(x, y, width, height, color)-----------

#all_sprite_list.add(follower)
#all_sprite_list.add(follower2)

#all_sprite_list.add(baseEnnemy)




#------------------INIT_SPRITE-------------------
def initSprite():
    # Spwan Player
    player = Player(player_spwan[1][0],player_spwan[1][1],11)
    joueur_tout_seul.add(player)

    # Platform
    for p in platformNiv2:
        all_platform_list.add(p)

    # Ennemi
    for e in ennemiesNiv2:
        all_sprite_list.add(e)
        ennemy_list.add(e)

    # EndPoint
    endPoint = EndPoint(endpoint_spwan[1][0],endpoint_spwan[1][1])
    all_sprite_list.add(endPoint)
    endPoint_Collision.add(endPoint)

    return player, endPoint



def game(screen):
    running = True
    #Pour l'affichage du texte
    player, endPoint = initSprite() 
    #Pour le chrono
    frame_count = 0
    frame_rate = 60
    start_time = 90
    while running:

    #Déplacement du joueur
        keys = pygame.key.get_pressed() 
            
        if (keys[K_RIGHT]):
            player.moveRight()
 
        if (keys[K_LEFT]):
            player.moveLeft()
 
        if (keys[K_UP] and not(player.isjump)):
            player.jump()
 
        if (keys[K_ESCAPE]):
            running = False    

        ## EVENT
        for event in pygame.event.get():

            #FERMER
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Test si le joueur bouge
            if event.type == pygame.KEYDOWN:
                player.isMoving = True

            if event.type == pygame.KEYUP:
                player.isMoving = False
        
        ## END EVENT

        #-----Ralentissement pour tout les ennemies si le joueur bouge
        for e in ennemy_list:
            if player.isMoving:
                e.speed = [5,5]
            else:
                e.speed = [2,2]
            
        #On actualise le fond pour voir correctement les affichages
        screen.blit(backg, [0,0])
        #screen.fill(WHITE)
        #screen.blit(level2, [0,0])
        
        
        #frame_count = 0
        #frame_rate = 60
        #start_time = 90
        #CHRONO
        # --- Timer going up ---
        # Calculate total seconds
        total_seconds = frame_count // frame_rate
 
        # Divide by 60 to get total minutes
        minutes = total_seconds // 60
 
        # Use modulus (remainder) to get seconds
        seconds = total_seconds % 60
 
        # Use python string formatting to format in leading zeros
        output_string = "Time :{0:02}:{1:02}".format(minutes, seconds)
        chrono = "{0:02}:{1:02}".format(minutes, seconds)
 
        # Blit to the screen
        text = font.render(output_string, True, BLACK)
        screen.blit(text, [20, 20])
        
        

       
        

        #Gère la collision et le respawn
        ennemy_hit_list = pygame.sprite.spritecollide(player, ennemy_list, False)
        for ennemies in ennemy_hit_list:
            player.respawn()
            #follower.respwan()
            #follower2.respwan()
            frame_count = 0
        
            #print(follower.rect.x, follower.rect.y)
        
        platform_collision_list = pygame.sprite.spritecollide(player, all_platform_list, False)
        collision_player_fin = pygame.sprite.spritecollide(player, endPoint_Collision, False)

        #-------------------------------------------------------------------------
        #--------------------------------FIN--------------------------------------
        #-------------------------------------------------------------------------
        for c in collision_player_fin:
            #----------TES UPDATENIVEAU
            UpdateNiveau(1, all_platform_list, all_sprite_list, player, endPoint)
            #fin(screen, chrono)



        all_sprite_list.update()
        player.update(all_platform_list)
        

        all_platform_list.draw(screen)
        #Fait le blit de tous les sprites
        all_sprite_list.draw(screen)
        joueur_tout_seul.draw(screen)
        
        pygame.display.update()
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        frame_count += 1
        #On règle les FPS
        pygame.time.Clock().tick(FPS)


    
    print("Fin du jeu !")
    #quit()

def fin(screen, chrono):
    running = True
    while running:
        for event in pygame.event.get():

            #FERMER
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #Affichage à la fin
        screen.fill(WHITE)
        font = pygame.font.Font(None, 36)
        text = font.render("Bravo ! Tu as fini le jeu en "+chrono+"s", 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = screenWidth /2
        textpos.centery = screenHeight /2
        screen.blit(text, textpos)

        pygame.display.update()
        pygame.time.Clock().tick(FPS)


def chronometre(screen):
    """Chronomètre pour le speedrun
    """
    start_ticks=pygame.time.get_ticks() #starter tick
    seconds= (pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
    minute = 0
    point =":"
    if seconds>60: # if more than 10 seconds close the game
        minute += 1
        seconds = 0
    temps = (str(minute)+point+str(seconds))
    
    font = pygame.font.Font(None, 36)
    text = font.render(temps, 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = 50
    textpos.centery = 50
    screen.blit(text, textpos)



def UpdateNiveau(indiceNiveau, all_platform_list, all_sprite_list, player, endPoint):
    """Variables
            -indiceNiveau : int qui indique le niveau : 0 -> menu, 1 -> niv1, ...
            -all_platform_list : la liste des platform du niveau
            -player : le sprite joueur
            -endPoint : la fin du niveau
    """
    all_platform_list.empty()
    all_sprite_list.empty()
    
    #--Gere les platformes---
    for p in all_levels[indiceNiveau]:
        all_platform_list.add(p)

    
    #--Gere les ennemies
    for e in all_ennemies[indiceNiveau]:
        all_sprite_list.add(e)
        ennemy_list.add(e)

    #--Gere player---
    player.x_origin = player_spwan[indiceNiveau][0]
    player.y_origin = player_spwan[indiceNiveau][1]

    #--Gere endPoint---
    endPoint.rect.x = endpoint_spwan[indiceNiveau][0]
    endPoint.rect.y = endpoint_spwan[indiceNiveau][1]
    all_sprite_list.add(endPoint)
    


    player.respawn()

    #---------------FAIRE TOUT LE CODE AVANT CETTE LIGNE-------------
    indiceNiveau +=1

    def incrementationNiveau(indiceNiveau):
        switcher={
                0:'Menu',
                1:'Niv1',
                2:'Niv2',
                3:'Niv3',
             }
        return switcher.get(indiceNiveau + 1)

    
    