import pygame
import math
pygame.init()
vec = pygame.math.Vector2
# création de la gravité


# variable à rajouter dans la classe player
self.pos = vec(WIDTH / 2, HEIGHT / 2)
self.vel = vec(0, 0)
self.acc = vec(0, 0)
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
# fonction pour la gravité

def update(self):
    self.acc = vec(0, PLAYER_GRAV)  # la valeur en y du vec acc peut être augmenté pour faire tombé le perso plus vite
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        self.acc.x = -PLAYER_ACC
    if keys[pg.K_RIGHT]:
        self.acc.x = PLAYER_ACC
    # equation gravité
    self.acc.x += self.vel.x * PLAYER_FRICTION
    self.vel += self.acc
    self.pos += self.vel + 0.5 * self.acc
    # gérer les collisions avec le bord de l'écran
    if self.pos.x > WIDTH:
        self.pos.x = 0
    if self.pos.x < 0:
        self.pos.x = WIDTH
    self.rect.midbottom = self.pos

    def jump(self):
        # saute seulement si sur une plateform
        self.rect.x += 1
        hits = player.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20
