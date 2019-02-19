import pygame, sys
from pygame.locals import *
import time

pygame.init()
pygame.mixer.init(22050, -16, 2, 4096)

# setting the display
DISP = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("it sounds gay")

# images and colors
closedChest = pygame.image.load("sprites/closed.gif")
openChest = pygame.image.load("sprites/open.gif")
heartPiece1 = pygame.image.load("sprites/heart1.gif")
heartPiece2 = pygame.image.load("sprites/heart2.gif")
BKG_COLOR = (90, 170, 185)

# positions settings
chestCenter1 = (180, 140)
chestCenter2 = (183, 142)
heartCenter = (193, 125)

while True:     # main game loop
    DISP.fill(BKG_COLOR) 
    DISP.blit(closedChest, chestCenter1)
    pygame.display.update()

    pygame.mixer.music.load("sounds/beginning.mp3")
    pygame.mixer.music.play(1, 0.0)  
    time.sleep(8)
    pygame.mixer.music.stop()

    pygame.mixer.music.load("sounds/ending.mp3")
    pygame.mixer.music.play(1, 0.0)
    DISP.blit(openChest, chestCenter2)
    pygame.display.update()
    time.sleep(1)
    for x in xrange(3):
        DISP.blit(heartPiece1, heartCenter)
        pygame.display.update()
        time.sleep(0.5)
        DISP.blit(heartPiece2, heartCenter)
        pygame.display.update()
    time.sleep(1)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()