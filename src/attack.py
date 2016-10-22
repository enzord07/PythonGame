import pygame
 
import constants

class Attack(pygame.sprite.Sprite):
    
    def __init__(self,posx,posy):
        super(Attack, self).__init__()
        
        self.image = pygame.Surface([20, 58])
        self.image.fill(constants.BLACK) 
        
        # Rectangulo del sprite
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        
        # Tiempo de vida
        self.life_time = 60*0.3
        
    def update(self):
        self.life_time -= 1