#imports
import os  #utilising the walk function of os
import pygame

#function to import images for animations
def import_folder(path):
    
    surface_list = []

    #the folder must only contain images, as any other format file will cause an import error
    folder = os.walk(path)

    for a,b, imgs in folder:
        
        #loop through the imgs
        for img in imgs:
            
            full_path = path + '/' + img 
            surface = (pygame.image.load(full_path)).convert_alpha() #to handle png images with transparent background
            surface_list.append(surface) 

    return surface_list