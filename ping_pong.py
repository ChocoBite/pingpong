import pygame
from random import randint

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()
window = pygame.display.set_mode((400, 300))
#background = transform.scale(image.load(''), (700, 500))
#window.feel('blue')
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, image_pl, x_pl, y_pl, speed_pl):
        super().__init__()
        self.image = transform.scale(image.load(image_pl), (80,80))
        self.rect.x = x_pl
        self.rect.y = y_pl
        self.speed = speed_pl
    def reset(self):
        window.blit(self.image, (self.rect.x, self.reset.y))

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    pygame.display.update()
    clock.tick(FPS)
