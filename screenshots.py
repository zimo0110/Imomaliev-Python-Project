#imports
import pygame
import sys
from parameters import *


#initialise Pygame 
pygame.init()
screen = pygame.display.set_mode((scr_width,scr_height))
clock = pygame.time.Clock()

#main loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
            #forces program to close by the system as well as pygame itself
			pygame.quit()
			sys.exit()
	
    #basic background filled
	screen.fill('white')

    #refreshes the screen at 60 fps
	pygame.display.update()
	clock.tick(60)

	
   #self.image = pygame.Surface((64,64))
        #self.image.fill((0,255,0))