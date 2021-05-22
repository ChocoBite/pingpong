import pygame
from random import randint

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()
window_pp = pygame.display.set_mode((400, 300))

FPS = 60

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    pygame.display.update()
    clock.tick(FPS)
