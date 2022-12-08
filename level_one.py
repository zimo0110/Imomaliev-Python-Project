#imports
import pygame
from tile import Tile
from parameters import tileDim, scr_width, scr_height
from player import Player
#imports


class Level:
    def __init__(self,lev_data, surface, dd) -> None:

        #level attributes  
        self.display_surf = surface
        self.setup(lev_data)
        self.world_shift = 0
        self.tempx = 0
        self.dead = dd
        self.score = 0

    #draw the map arrangement
    def setup(self, layout):

        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.target = pygame.sprite.GroupSingle()

        for row_index,row in enumerate(layout):
            for col_index, cell in enumerate(row):
                #print(f'{row_index},{col_index} : {cell}')

                x = col_index * tileDim
                y = row_index * tileDim

                if cell == 'X':
        
                    tile = Tile((x,y),tileDim)
                    self.tiles.add(tile)

                elif cell == 'P':

                    player = Player((x,y))
                    self.player.add(player)

                elif cell == 'T':
                    target = Target((x,y),tileDim)
                    self.target.add(target)
                    

    #camera of the game
    def scroll_x(self):

        #initialise player
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        #makes camera follow the player, by moving all the sprites and stopping the player itself
        if player_x < (scr_width/4) and direction_x < 0:
            self.world_shift = 8 #player moves left
            player.speed = 0
        elif player_x > scr_width * 3/4 and direction_x > 0:
            self.world_shift = -8 #player moves right
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8 #player moves within the screen bounds


    def horizontal_collision(self):

        #mechanics
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        #target = self.target.sprite
    
        #collision
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect): #use 'rect' instead of 'sprite' to get hold of rectangle info of tiles and the player
                if player.direction.x < 0: # moving left
                    player.rect.left = sprite.rect.right 
                    player.lwall = True
                    self.tempx = player.rect.left
                elif player.direction.x > 0: #move right
                    player.rect.right = sprite.rect.left
                    player.rwall = True
                    self.tempx = player.rect.right

        #wall collision
        if player.lwall and (player.rect.left < self.tempx or player.direction.x >= 0): #if player is moving left and is not colliding with the left wall
            player.lwall = False
        if player.rwall and (player.rect.right > self.tempx or player.direction.x <= 0):
            player.rwall = False

        #target collision
        for target in self.target.sprites():
            if target.rect.colliderect(player.rect): #player vs target
                self.score += 1
                print(self.score)
                                                 
        
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
                    player.floor = True

                elif player.direction.y < 0: #move up
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.ceiling = True

        if player.floor and (player.direction.y < 0 or player.direction.y >1):
            player.floor = False

        if player.ceiling and player.direction.y > 0 :
            player.ceiling = False

        
    def player_death(self):
        player = self.player.sprite
        y = player.rect.bottom

        if y >= scr_height:
            #print('player dead')
            pygame.event.post(pygame.event.Event(self.dead))


    def show_score(self):

        black = (0,0,0)

        #define fonts
        self.font = pygame.font.SysFont("arialblack", 35)
        score_text = self.font.render("Score: "+str(self.score), True, black)
        scoreRect = score_text.get_rect()
        self.display_surf.blit(score_text, scoreRect)
        


    #public procedure
    def run(self):
        
        #all tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surf)

        #target
        self.target.update(self.world_shift)
        self.target.draw(self.display_surf)

        #scroll
        self.scroll_x()

        #player
        self.player.update()
        self.horizontal_collision()
        self.vertical_collision()
        self.player_death()
        self.player.draw(self.display_surf)

        #score
        self.show_score()

    
        