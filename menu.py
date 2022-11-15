#imports
import pygame
from tile import Tile
from parameters import tileDim, scr_width
import sys
#imports

class Menu:
    def __init__(self) -> None:

        #screen
        pygame.init()
        self.colours = {'Blue': (170,170,170)}
        self.res = (800,800)
        self.screen = pygame.display.set_mode(self.res)
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.smallfont = pygame.font.SysFont('Corbel',35)
        self.run()
    

    #public procedure to run the menu screen loop
    def run(self):
        
        # screen into a variable 
       
        # light shade of the button 
        color_light = (170,170,170) 
        color = (255,255,255)

        # dark shade of the button 
        color_dark = (100,100,100)
        text = self.smallfont.render('quit' , True , color) 

        run = True
        while run: 
            for e in pygame.event.get(): 
                if e.type == pygame.QUIT: 
                    run = False

                #checks if a mouse is clicked 
                if e.type == pygame.MOUSEBUTTONDOWN: 
                    
                    #if the mouse is clicked on the 
                    # button the game is terminated 
                    if self.width/2 <= mouse[0] <= self.width/2+200 and self.height/2 <= mouse[1] <= self.height/2+100: 
                        run = False
               
            # fills the screen with a color 
            self.screen.fill((60,25,60)) 
            
            # stores the (x,y) coordinates into 
            # the variable as a tuple 
            mouse = pygame.mouse.get_pos() 
            
            # if mouse is hovered on a button it 
            # changes to lighter shade 
            if self.width/2 <= mouse[0] <= self.width/2+200 and self.height/2 <= mouse[1] <= self.height/2+100: 
                pygame.draw.rect(self.screen,color_light,[self.width/2,self.height/2,200,100]) 
                
            else: 
                pygame.draw.rect(self.screen,color_dark,[self.width/2,self.height/2,200,100]) 
            
            # superimposing the text onto our button 
            self.screen.blit(text, (self.width/2+100,self.height/2)) 
            
            
            # updates the frames of the game 
            pygame.display.update()  

        #unintialize pygame
        pygame.quit()
            
                    

