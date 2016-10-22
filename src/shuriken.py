import pygame
 
import constants
from spritesheet_functions import SpriteSheet

class Shuriken(pygame.sprite.Sprite):
    
    def __init__(self,posx,posy,dir, img):
        
        super(Shuriken, self).__init__()
        
        self.change_x=4
        self.direction=dir
        
        
        sprite_sheet = img
        # Lista de las animaciones del Shuriken
        self.shuriken_frames = []
        
        image = sprite_sheet.get_image(312, 2452, 13, 13)
        self.shuriken_frames.append(image)
        image = sprite_sheet.get_image(328, 2452, 13, 13)
        self.shuriken_frames.append(image)
        image = sprite_sheet.get_image(344, 2452, 13, 13)
        self.shuriken_frames.append(image)
        
        # Numero de Frame a mostrar
        self.frame=0
        
        self.image = self.shuriken_frames[self.frame]
        
        # Rectangulo del sprite
        self.rect = self.image.get_rect()
        
        self.rect.x = posx
        self.rect.y = posy        
        
        # Direccion del shuriken
        self.direction = dir    
        
        # Reloj para la hoja de sprites
        self.reloj = 0
        
        # Tiempo de vida
        self.life_time = 60*2.5
        
        
    def update(self):
        if self.direction=="R":
            self.rect.x += self.change_x
        else:
            self.rect.x += self.change_x * (-1)
        self.select_image()
        self.reloj += 1
        self.life_time -= 1
        
    def select_image(self):
        if (self.reloj % 2)==0:
            self.frame +=1
            if self.frame>len(self.shuriken_frames)-1:
                self.frame=0
            self.image = self.shuriken_frames[self.frame]      
            
        
        
        