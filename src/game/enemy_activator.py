import pygame
 
import constants

class Enemy_Activator(pygame.sprite.Sprite):
    
    def __init__(self):
        super(Enemy_Activator, self).__init__()
        
        self.image = pygame.Surface([700, 58])
        self.image.fill(constants.BLACK)
        
        # Rectangulo del sprite
        self.rect = self.image.get_rect()
        