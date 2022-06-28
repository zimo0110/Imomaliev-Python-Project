#all imports
import pygame
import os
import random
from improve_space import BORDER, SPACE_BG
import sys

#game class, the base of the game
class Game():

    #initialise the Game's attributes
    def __init__(self):

        #parameters of the screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.FPS = 60

        #mechanics of the game
        self.player_VEL = 5
        self.player_Lives = 5

        #colours that will be used in my game
        self.end = False
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.BLUE = (50,50,255)
        self.YELLOW = (255,255,0)
        self.RED = (255,0,0)

        #fonts and sounds
        self.HEALTH_FONT = pygame.font.SysFont('Aharoni', 40)
        self.WINNER_FONT = pygame.font.SysFont('Biome', 80)

        self.BULLET_HSOUND = pygame.mixer.Sound(os.path.join('resourcesExtra', 'Grenade+1.mp3'))
        self.BULLET_FSOUND = pygame.mixer.Sound(os.path.join('resourcesExtra', 'Gun+Silencer.mp3'))

        #parameters for the player and enemy
        self.SPACESHIP_WIDTH = 60
        self.SPACESHIP_HEIGHT = 60

        self.YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('resourcesExtra', 'spaceship_yellow.png'))
        self.ENEMY_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(self.YELLOW_SPACESHIP_IMAGE, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT)), 90)

        self.RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('resourcesExtra', 'spaceship_red.png'))
        self.PLAYER_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(self.RED_SPACESHIP_IMAGE, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT)), -90)
        
        #collision events
        self.PLAYER_HIT = pygame.USEREVENT + 1
        self.ENEMY_HIT = pygame.USEREVENT + 2

        #player and enemy


        #background
        self.Background = pygame.transform.scale(pygame.image.load(os.path.join('resourcesExtra','space.png')),(self.WIDTH, self.HEIGHT))
        self.Border = pygame.Rect(10, 0, 10, HEIGHT)

        #bullet parameters
        self.BULL_VEL = 7
        self.MAX_BULL = 3

    #end constructor

    #get the image of the player spaceship
    def get_player_img(self):

        return self.PLAYER_SPACESHIP
        
    #get the image of the enemy spaceship
    def get_enemy_img(self):
            
        return self.ENEMY_SPACESHIP

    #get players speed
    def get_player_vel(self):

        return self.player_vel
        
    #get number of player lives
    def get_player_lives(self):

        return self.player_lives

    #get the screen width 
    def get_screen_wid(self):
            
        return  self.WIDTH 
        
    #get the screen height
    def get_screen_hei(self):

        return self.HEIGHT
    
    #return the type of the font
    def get_healthFont(self):

        return self.HEALTH_FONT
        
    #main function
    def game1(self):

        #game loop
        clock = pygame.time.Clock()
        run = True

        bullets = []
        #lives = self.player_Lives

        while run :
            clock.tick(self.FPS)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False
                    sys.exit()
                    
            self.draw()

    def draw(self):
        #bg and border
        global WIN
        WIN.blit(self.Background,(0,0))
        pygame.draw.rect(WIN, self.BLACK, self.Border)


#class of the user
class Player(pygame.sprite.Sprite):

    def __init__(self, width,height,x,y):

        super().__init__()
        self.image = Game.get_player_img()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.height = height
        self.width = width
        self.speed = 5
        self.lives  = 5

        #colours that will be used in my game
        self.end = False
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.BLUE = (50,50,255)
        self.YELLOW = (255,255,0)
        self.RED = (255,0,0)
    
    def movement(self, keys_pressed):
        if keys_pressed[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= Game.get_player_vel()

        if keys_pressed[pygame.K_d] and self.rect.x + self.width < Game.get_screen_wid():
            self.rect.x += Game.get_player_vel()
    
    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def collision(self, inv_group, my_inv, lives):
        for my_inv in inv_group:
            col2 = pygame.sprite.collide_rect(self,my_inv)
            if col2 == True:
                inv_group.remove(my_inv)
                self.lives -= 1    

    def scoreP(self):
        #update the score of the player
        draw_text = (Game.get_healthFont()).render("Health :" + str(self.lives), 1, self.WHITE)
        winner_text = (Game.get_healthFont()).render("YOU LOST", 1, self.WHITE)
        WIN.blit(draw_text ,(draw_text.get_width()//2 - 20, 0 + draw_text.get_height()//2))
        if self.lives == 0:
            WIN.blit(winner_text ,(winner_text.get_width()//2 - 20, 30 + winner_text.get_height()//2))
            pygame.display.update()
        else:
            pygame.display.update()
            pygame.time.delay(5000)

if __name__ == '__main__':

    #initialise pygame 
    pygame.mixer.init()
    pygame.font.init()
    pygame.init()
    pygame.display.set_caption('Space Shooters by Zoir')
    WIDTH, HEIGHT = 710, 500
    SIZE = (WIDTH, HEIGHT)
    WIN = pygame.display.set_mode(SIZE)
    main_game = Game()
    main_game.game1()