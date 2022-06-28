import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self,pos) -> None:
        super().__init__()
        self.image = pygame.Surface((32,64))
        self.image.fill('blue')
        self.rect = self.image.get_rect(topleft = pos)

        #mechanics
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.jump_h = -16 # how much player jumps up
        self.gravity = 0.8  # the gravity on the player 


    def animations(self):
        self.folder_path = '../graphics/player/' #folder path for all animations

        self.animations = {'idle':[], 'run':[],'jump':[],'fall':[]} # name of the folders for each action

        for animation in self.animations.keys():
            path = self.folder_path + animation



    def get_input(self):
        keys_pressed = pygame.key.get_pressed()

        #x-axis input
        if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:     
            self.direction.x = -1
        else:
            self.direction.x = 0

        #y-axis input
        if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
            self.player_jump()


    def player_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y


    def player_jump(self):
        self.direction.y = self.jump_h


    def update(self):
        self.get_input() 
        