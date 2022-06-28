#imports
import pygame
import os 

#initilisers
pygame.font.init()
pygame.font.init()
pygame.init()

#globals
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodgy Star Game by ZOIR")


#main loop
def main():

    clock = pygame.time.Clock()
    run = True
    FPS = 70

    while run:
        clock.tick(FPS)

        for event in pygame.event.get()
        
