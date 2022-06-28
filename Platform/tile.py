#imports
import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        #new attributes for each tile that will make up my map
        self.image = pygame.Surface((size, size))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = pos) #pygame uses top left orientation 

    #public procedure 
    def update(self,x_shift):
        self.rect.x += x_shift