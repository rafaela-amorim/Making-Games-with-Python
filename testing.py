import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60    # FPS setting
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption("you know what it is, henny")

WHITE = (255, 255, 255)
xPosition = 10
Y_POS = 10
direction = 'right'
image = pygame.image.load('two_fingers.png')

while True:     # main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        xPosition += 5
        if xPosition == 280:
            direction = 'left'
    elif direction == 'left':
        xPosition -= 5
        if xPosition == 10:
            direction = 'right'

    DISPLAYSURF.blit(image, (xPosition, Y_POS))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)