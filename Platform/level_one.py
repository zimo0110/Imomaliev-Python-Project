import pygame
from tile import Tile
from parameters import tileDim, scr_width
from player import Player

class Level:
    def __init__(self,lev_data, surface) -> None:
        #level attributes  
        self.display_surf = surface
        self.setup(lev_data)
        self.world_shift = 0

    #draw the map arrangement
    def setup(self, layout):

        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index,row in enumerate(layout):
            for col_index, cell in enumerate(row):
                print(f'{row_index},{col_index} : {cell}')

                x = col_index * tileDim
                y = row_index * tileDim

                if cell == 'X':
        
                    tile = Tile((x,y),tileDim)
                    self.tiles.add(tile)

                elif cell == 'P':

                    player = Player((x,y))
                    self.player.add(player)


    #camera of the game
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < (scr_width/4) and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > scr_width * 3/4 and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8


    def horizontal_collision(self):
        #mechanics
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        #collision
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect): #use 'rect' instead of 'sprite' to get hold of rectangle info of tiles and the player
                if player.direction.x < 0: # moving left
                    player.rect.left = sprite.rect.right 
                elif player.direction.x > 0: #move right
                    player.rect.right = sprite.rect.left
            
    def vertical_collision(self):
        #mechanics
        player = self.player.sprite
        player.player_gravity()

        #collision
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect): #use 'rect' instead of 'sprite' to get hold of rectangle info of tiles and the player
                if player.direction.y > 0: # moving down
                    player.rect.bottom = sprite.rect.top 
                    player.direction.y = 0
                elif player.direction.y < 0: #move up
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0


    #public procedure
    def run(self):

        #all tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surf)
        self.scroll_x()

        #player
        self.player.update()
        self.horizontal_collision()
        self.vertical_collision()
        self.player.draw(self.display_surf)
        