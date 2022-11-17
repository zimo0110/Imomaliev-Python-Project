#imports
import pygame
from helperGame import import_folder as lol
import os
#imports


class Player(pygame.sprite.Sprite):

    def __init__(self,pos):
        super().__init__() #inherited from a sprite superclass

        #init functions
        self.import_animations()

        #player animations
        self.animation_indx = 0     #indicates which action the player is perfoming
        self.animation_vel = 0.15   #how quickly the images change
        self.image = self.animations['idle'][self.animation_indx] #initial image
        

        #player structure attributes
        self.rect = self.image.get_rect(topleft = pos)  #blits the self.img to my player sprite

        #mechanics
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.jump_h = -16 # how much player jumps up
        self.gravity = 0.8  # the gravity on the player 

        #player directions
        self.movement = 'idle'     #initial movement
        self.right = True          #initial direction player is facing
        self.floor = False
        self.ceiling = False
        self.rwall = False
        self.lwall = False


    def import_animations(self):
        folder_path = './graphics/playerx/' #folder path for all animations

        self.animations = {'idle':[],'run':[],'jump':[],'fall':[]} # name of the folders for each action

        for animation in self.animations.keys():
            f_path = folder_path + animation #combine the path for each action and overall animations
            self.animations[animation] = lol(f_path)


    def animate(self):
        current_pic = self.animations[self.movement]

        #loop over the images
        self.animation_indx += self.animation_vel
        if self.animation_indx >= len(current_pic):
            self.animation_indx = 0
        
        #update the image 
        temp = current_pic[int(self.animation_indx)]
        if self.right:
            self.image = temp
        else:
            self.image = pygame.transform.flip(temp,True,False) #item, x, y

        #redefine the self.rect
        if self.floor and self.rwall:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.floor and self.lwall:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.floor:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.ceiling and self.rwall:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.ceiling and self.lwall:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)


    def get_input(self):

        keys_pressed = pygame.key.get_pressed()

        #x-axis input
        if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
            self.direction.x = 1
            self.right = True
        elif keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:     
            self.direction.x = -1
            self.right = False
        else:
            self.direction.x = 0

        #y-axis input
        if (keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]) and self.floor:
            self.player_jump()


    def player_gravity(self):
        #y-direction indicates the current vertical vector direction 
        self.direction.y += self.gravity
        self.rect.y += self.direction.y


    def get_movement(self):

        #player going up
        if self.direction.y < 0: 
            self.movement = 'jump'
        elif self.direction.y > 1: #bigger than self.gravity, as player sprites y-direction is almost never actually 0
            self.movement = 'fall'
        else:
            if self.direction.x == 0:
                self.movement = 'idle'
            else:
                self.movement = 'run'


    def player_jump(self):
        #simple jump where direction is vertically up, but y-value decreases as pygame is reversed coordinate system
        self.direction.y = self.jump_h


    def update(self):
        #call internal function to make coordinate changes based on the current input
        self.get_input()
        self.get_movement()
        self.animate()