#imports
import pygame
import sys
import math
from parameters import *
from tile import Tile
from level_one import Level

#initialise Pygame 
pygame.init()
screen = pygame.display.set_mode((scr_width,scr_height))
clock = pygame.time.Clock()
level_one = Level(levOne_map, screen)
test = pygame.sprite.Group(Tile((100,100),200))

#main loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	screen.fill('white')
	level_one.run()

	pygame.display.update()
	clock.tick(60)
