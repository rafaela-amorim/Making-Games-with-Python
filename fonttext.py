import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello World, but pretty")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

fontObj = pygame.font.Font("freesansbold.ttf", 42)
txtSurface = fontObj.render("Hello World", True, BLUE, GREEN)
txtRect = txtSurface.get_rect()
txtRect.center = (200, 150)

while True:     # main game loop
    DISPLAYSURF.fill(WHITE)

    DISPLAYSURF.blit(txtSurface, txtRect)   # blitting the text onto the surface

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.exit()
            sys.exit()
    
    pygame.display.update()