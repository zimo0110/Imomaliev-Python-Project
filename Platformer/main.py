#imports
import pygame, sys


class Game:
    def __init__(self):

        #Game attributes
        self.hp = 100
        self.cur_hp = 100
        
        pass




#main loop
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('grey')
    #initialise game game.run()

    pygame.display.update()
    clock.tick(60)
