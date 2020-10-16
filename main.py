import pygame
from pygame.locals import *

successes, failures = pygame.init()
print("Initializing pygame: {0} successes and {1} failures.".format(successes, failures))

size = width, height = 620, 540
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 60
pourcent_ralenti = 0.7

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.velocity = [0, 0]

    def update(self):
        self.rect.move_ip(*self.velocity)

class Temoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill(RED)
        self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.velocity = [5, 0]
    
    def update(self):
        self.rect.move_ip(*self.velocity)


player = Player()
temoin = Temoin()

running = True
while running:
    dt = clock.tick(FPS) / 1000  # Returns milliseconds between each call to 'tick'. The convert time to seconds.
    screen.fill(BLACK)  # Fill the screen with background color.

    for event in pygame.event.get():
        # FERMER
        if event.type == pygame.QUIT:
            running = False
        # DEPLACEMENTS
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.velocity[1] = -200 * dt  # 200 pixels per second
            if event.key == pygame.K_s:
                player.velocity[1] = 200 * dt
            if event.key == pygame.K_a:
                player.velocity[0] = -200 * dt
            if event.key == pygame.K_d:
                player.velocity[0] = 200 * dt
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player.velocity[1] = 0
            elif event.key == pygame.K_a or event.key == pygame.K_d:
                player.velocity[0] = 0
            temoin.velocity[0] = temoin.velocity[0] * pourcent_ralenti

    player.update()
        
    if temoin.rect.left < 0 or temoin.rect.right > width:
        temoin.velocity[0] = -temoin.velocity[0]
    temoin.update()

    screen.blit(player.image, player.rect)
    screen.blit(temoin.image, temoin.rect)
    pygame.display.update()  # Or pygame.display.flip()

print("Exited the game loop. Game will quit...")
quit()  # Not actually necessary since the script will exit anyway.