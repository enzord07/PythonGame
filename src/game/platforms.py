import pygame
 
from spritesheet_functions import SpriteSheet
 
# Tipos de plataformas
#  (x, y, ancho, alto)

 
GRASS_LEFT            = (576, 720, 70, 70)
GRASS_RIGHT           = (576, 576, 70, 70)
GRASS_MIDDLE          = (504, 576, 70, 70)
STONE_PLATFORM_LEFT   = (432, 720, 70, 40)
STONE_PLATFORM_MIDDLE = (648, 648, 70, 40)
STONE_PLATFORM_RIGHT  = (792, 648, 70, 40)
PIEDRA_IZQUIERDA      = (792,216,70,70)
PIEDRA_CENTRO      = (792,144,70,70)
PIEDRA_DERECHA      = (792,72,70,70)
PIEDRA_FLOTANTE_IZQUIERDA=(144,432,70,70)
PIEDRA_FLOTANTE_MEDIO=(72,432,70,70)
PIEDRA_FLOTANTE_DERECHA=(144,288,70,70)
PIEDRITA_FOTANTE_CENTRO=(144,144,70,70)
INTERROGACION=(0,0,70,70)
ESTRELLA_NINJA=(0,576,70,70)
EXIT=(288,360,70,70)
 
class Platform(pygame.sprite.Sprite):
 
    def __init__(self, sprite_sheet_data):
        super(Platform, self).__init__()
 
        sprite_sheet = SpriteSheet("game/tiles_spritesheet.png")
        # Imagen de la plataforma
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
 
        self.rect = self.image.get_rect()
 
class MovingPlatform(Platform):
    """ Plataforma Movil """
 
    def __init__(self, sprite_sheet_data):
 
        super(MovingPlatform, self).__init__(sprite_sheet_data)
 
        self.change_x = 0
        self.change_y = 0
 
        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0
 
        self.level = None
        self.player = None
 
    def update(self):
 
 
        # Mover izq/der
        self.rect.x += self.change_x
 
        # Desplazar jugador si esta en la plataforma
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                self.player.rect.left = self.rect.right
 
        # Mover arriba/abajo
        self.rect.y += self.change_y
 
        # Desplazar jugador si esta en la plataforma
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom
 
        # Rebote de la plataforma
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1
 
        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1