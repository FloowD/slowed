import os
import sys
import pygame
from pygame.locals import *
from constants import *
from Player import Player
from ennemies import Follower
from Platform import *
from EndPoint import *
import math

#backg = pygame.image.load("images/sprites/background.png")
#backg = pygame.transform.scale(backg, [x//RATIO for x in backg.get_size()])

#level2 = pygame.image.load("images/levels/level 2.png")
#level2 = pygame.transform.scale(level2, [x//RATIO for x in level2.get_size()])

#Fichier qui va être appelé dans le main et lancer les fonctions
#importantes pour le programme

spawn_x = 50
spwan_y = 1200

player = Player(spawn_x,spwan_y,11)
follower = Follower(750,600,player)
follower2 = Follower(100,0,player)
endPoint = EndPoint(850, 100)


ennemies = []
ennemies.append(follower)
ennemies.append(follower2)

#Mettre tout les objet dans une liste
all_sprite_list = pygame.sprite.Group()
ennemy_list = pygame.sprite.Group()
endPoint_Collision = pygame.sprite.Group()

joueur_tout_seul = pygame.sprite.Group()
joueur_tout_seul.add(player)
all_sprite_list.add(follower)
all_sprite_list.add(follower2)
all_sprite_list.add(endPoint)
endPoint_Collision.add(endPoint)

for e in ennemies:
    all_sprite_list.add(e)
    ennemy_list.add(e)

#-------Platform(x, y, width, height, color)-----------

platform1 = Platform(150, 620, 50, 20, GREY)
platform2 = Platform(300, 520, 100, 20, GREY)
platform3 = Platform(560, 300, 120, 20, GREY)
platform4 = Platform(320, 100, 100, 150, GREY)
platform5 = Platform(870, 550, 66, 152, GREEN)
platform6 = Platform(600, 120, 45, 20, GREY)
platform7 = Platform(100, 250, 73, 94, GREY)
platform8 = Platform(720, 470, 45, 45, GREY)
all_platform_list = pygame.sprite.Group()

platforms = []
platforms.append(platform1)
platforms.append(platform2)
platforms.append(platform3)
platforms.append(platform4)
platforms.append(platform5)
platforms.append(platform6)
platforms.append(platform7)
platforms.append(platform8)

for p in platforms:
    all_platform_list.add(p)



def game(screen):
    running = True
    #Pour l'affichage du texte
    font = pygame.font.Font(None, 25)
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

        # TODO: DELETE
        if player.isMoving:
            follower.speed = [8,8]
            follower2.speed = [8,8]
        else:
            follower.speed = [3,3]
            follower2.speed = [3,3]
            
        #On actualise le fond pour voir correctement les affichages
        #screen.blit(backg, [0,0])
        screen.fill(WHITE)
        #screen.blit(level2, [0,0])
        
        

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
            follower.respwan()
            follower2.respwan()
            frame_count = 0
        
            #print(follower.rect.x, follower.rect.y)
        
        platform_collision_list = pygame.sprite.spritecollide(player, all_platform_list, False)
        collision_player_fin = pygame.sprite.spritecollide(player, endPoint_Collision, False)

        for c in collision_player_fin:
            fin(screen, chrono)

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
        text = font.render("Bravo tu as gagné, tu as fini le jeu en "+chrono+"s", 1, (10, 10, 10))
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
    