#imports
import pygame
#imports

#initialise a class
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):

        #initialise pygame using super as its a parent class
        super().__init__()
        
        #new attributes for each tile that will make up my map
        self.image = pygame.Surface((size, size))
        self.image.fill('black')
        self.rect = self.image.get_rect(topleft = pos) #pygame uses top left orientation 

    #public procedure 
    def update(self,x_shift):
        self.rect.x += x_shift