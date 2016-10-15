import pygame

class Edited_Sprite_Group(pygame.sprite.Group):
    """ Esta clase redefine un metodo para poder dibujar bien los sprites"""
    def __init__(self):
        
        super(Edited_Sprite_Group, self).__init__()
    
    def draw(self, surface):
            """draw all sprites onto the surface
    
            Group.draw(surface): return None
    
            Draws all of the member sprites onto the given surface.
    
            """
            sprites = self.sprites()
            surface_blit = surface.blit
            for spr in sprites:
                self.spritedict[spr] = surface_blit(spr.draw_image, spr.draw_rect)
            self.lostsprites = []