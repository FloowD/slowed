import pygame

# Création fonction rotation que l'on va ensuite appliquer à flipper

def rotate (surface, angle):
    rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
    rotated_rect = rotated_surface.get_rect(center=(500, 300))
    return rotated_surface, rotated_rect

