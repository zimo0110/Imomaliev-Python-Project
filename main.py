#imports
import pygame
import sys
import math
from parameters import *
from tile import Tile
from level_one import Level
from menu import Menu
import button
#imports

#initialise Pygame 
pygame.init()
screen = pygame.display.set_mode((scr_width,scr_height))
clock = pygame.time.Clock()

#level one
DEAD = pygame.USEREVENT + 1
level_one = Level(levOne_map, screen, DEAD)
test = pygame.sprite.Group(Tile((100,100),200))

#Game Pause
game_paused = False
menu_state = "main"
run = True 

#define colours
TEXT_COL = (255, 255, 255)

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#load button images
resume_img = pygame.image.load("graphics/buttonimages/button_resume.png").convert_alpha()
options_img = pygame.image.load("graphics/buttonimages/button_options.png").convert_alpha()
quit_img = pygame.image.load("graphics/buttonimages/button_quit.png").convert_alpha()
video_img = pygame.image.load('graphics/buttonimages/button_video.png').convert_alpha()
audio_img = pygame.image.load('graphics/buttonimages/button_audio.png').convert_alpha()
keys_img = pygame.image.load('graphics/buttonimages/button_keys.png').convert_alpha()
back_img = pygame.image.load('graphics/buttonimages/button_back.png').convert_alpha()

#create button instances
resume_button = button.Button(scr_width//2-90, scr_height//4, resume_img, 1)
options_button = button.Button(scr_width//2-90, scr_height//4+150, options_img, 1)
quit_button = button.Button(scr_width//2-90, scr_height//4+300, quit_img, 1)

video_button = button.Button(scr_width//2-120, scr_height//5, video_img, 1)
audio_button = button.Button(scr_width//2-120, scr_height//5+150, audio_img, 1)
keys_button = button.Button(scr_width//2-120, scr_height//5+300, keys_img, 1)
back_button = button.Button(scr_width//2-120, scr_height//5+450, back_img, 1)

#menu drawer
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#main loop
while run:
	
    #basic background filled
	screen.fill('white')

	#check if game is paused
	if game_paused == True:

		#check menu state
		if menu_state == "main":

			#draw pause screen buttons
			if resume_button.draw(screen):
				game_paused = False
			if options_button.draw(screen):
				menu_state = "options"
			if quit_button.draw(screen):
				run = False

		#check if the options menu is open
		if menu_state == "options":

			#draw the different options buttons
			if video_button.draw(screen):
				print("Video Settings")
			if audio_button.draw(screen):
				print("Audio Settings")
			if keys_button.draw(screen):
				print("Change Key Bindings")
			if back_button.draw(screen):
				menu_state = "main"
	else:
		#load level one
		level_one.run()


	#main event checker
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				game_paused = True

		if event.type == pygame.QUIT:
            #forces program to close by the system as well as pygame itself
			pygame.quit()
			sys.exit()

		if event.type == DEAD:
			pygame.quit()
			sys.exit()

	
    #refreshes the screen at 60 fps
	pygame.display.update()
	clock.tick(60)

