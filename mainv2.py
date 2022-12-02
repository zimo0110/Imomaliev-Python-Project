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

class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((scr_width,scr_height))
        self.clock = pygame.time.Clock()

        #level one
        self.DEAD = pygame.USEREVENT + 1
        self.level_one = Level(levOne_map, self.screen, self.DEAD)
        self.test = pygame.sprite.Group(Tile((100,100),200))

        #Game constants
        self.score = 0

        #Game Pause
        self.game_paused = False
        self.menu_state = "main"
        self.run = True 

        #define colours
        self.TEXT_COL = (255, 255, 255)

        #define fonts
        self.font = pygame.font.SysFont("arialblack", 40)

        #load button images
        self.size_img = (400,200)
        self.resume_img = pygame.image.load("graphics/buttonimages/button_resume.png").convert_alpha()
        self.options_img = pygame.image.load("graphics/buttonimages/button_options.png").convert_alpha()
        self.quit_img = pygame.image.load("graphics/buttonimages/button_quit.png").convert_alpha()
        self.video_img = pygame.image.load('graphics/buttonimages/button_video.png').convert_alpha()
        self.audio_img = pygame.image.load('graphics/buttonimages/button_audio.png').convert_alpha()
        self.keys_img = pygame.image.load('graphics/buttonimages/button_keys.png').convert_alpha()
        self.back_img = pygame.image.load('graphics/buttonimages/button_back.png').convert_alpha()
        self.endgame_img = pygame.transform.scale(pygame.image.load("graphics/buttonimages/endgame.png").convert_alpha(), self.size_img)


        #create button instances
        self.resume_button = button.Button(scr_width//2-90, scr_height//4, self.resume_img, 1)
        self.options_button = button.Button(scr_width//2-90, scr_height//4+150, self.options_img, 1)
        self.quit_button = button.Button(scr_width//2-90, scr_height//4+300, self.quit_img, 1)

        self.video_button = button.Button(scr_width//2-120, scr_height//5, self.video_img, 1)
        self.audio_button = button.Button(scr_width//2-120, scr_height//5+150, self.audio_img, 1)
        self.keys_button = button.Button(scr_width//2-120, scr_height//5+300, self.keys_img, 1)
        self.back_button = button.Button(scr_width//2-120, scr_height//5+450, self.back_img, 1)

        self.endgame_button = button.Button(scr_width//2-180, scr_height//4 + 120, self.endgame_img, 1)

    #menu drawer
    def draw_text(self,text, text_col, x, y):
        img = self.font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    #main loop
    def run_game(self):

        while self.run:

            #basic background filled
            self.screen.fill('white')

            #check if game is paused
            if self.game_paused == True:

                #check menu state
                if self.menu_state == "main":

                    #draw pause self.screen buttons
                    if self.resume_button.draw(self.screen):
                        self.game_paused = False
                    if self.options_button.draw(self.screen):
                        self.menu_state = "options"
                    if self.quit_button.draw(self.screen):
                        self.run = False

                #check if the options menu is open
                if self.menu_state == "options":

                    #draw the different options buttons
                    if self.video_button.draw(self.screen):
                        print("Video Settings")
                    if self.audio_button.draw(self.screen):
                        print("Audio Settings")
                    if self.keys_button.draw(self.screen):
                        print("Change Key Bindings")
                    if self.back_button.draw(self.screen):
                        self.menu_state = "main"
                
                #if player died
                if self.menu_state == "over":

                    #draw different option buttons
                    if self.endgame_button.draw(self.screen):
                        print('Game Over')
                        self.run = False
                    
            else:
                #load level one
                self.level_one.run()
                

            #main event checker
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_paused = True

                if event.type == pygame.QUIT:
                    #forces program to close by the system as well as pygame itself
                    pygame.quit()
                    sys.exit()

                if event.type == self.DEAD:
                
                    self.menu_state = "over"
                    self.game_paused = True
                    print('self.DEAD self.screen')
            
            #refreshes the self.screen at 60 fps
            pygame.display.update()
            self.clock.tick(60)


#main code
x = Game()
x.run_game()