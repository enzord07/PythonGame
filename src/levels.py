import pygame
 
import constants
import platforms
 
class Level(object):
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """
 
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
 
        # Lists of sprites used in all levels. Add or remove
        # lists as needed for your game.
        self.platform_list = None
        self.enemy_list = None
 
        # Background image
        self.background = None
 
        # How far this world has been scrolled left/right
        self.world_shift = 0
        self.level_limit = -1000
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
 
    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
 
    def draw(self, screen):
        """ Draw everything on this level. """
 
        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shift // 3,0))
 
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
 
    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """
 
        # Keep track of the shift amount
        self.world_shift += shift_x
 
        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x
 
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
 
# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.background = pygame.image.load("nivel1.jpg").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500
 
        # Array with type of platform, and x, y location of the platform.
        level =   [
                  [platforms.PIEDRA_IZQUIERDA, 0, 530],
                  [platforms.PIEDRA_CENTRO, 70, 530],
                  [platforms.PIEDRA_CENTRO, 140, 530],
                  [platforms.PIEDRA_CENTRO, 210, 530],
                  [platforms.PIEDRA_CENTRO, 280, 530],
                  [platforms.PIEDRA_CENTRO, 350, 530],
                  [platforms.PIEDRA_DERECHA, 420, 530],
                  #1
                  [platforms.PIEDRA_FLOTANTE_IZQUIERDA, 500, 400],
                  [platforms.PIEDRA_FLOTANTE_MEDIO, 570, 400],
                  [platforms.PIEDRA_FLOTANTE_DERECHA, 640, 400], 
                  #2
                  [platforms.PIEDRA_FLOTANTE_IZQUIERDA, 500, 160],
                  [platforms.PIEDRA_FLOTANTE_MEDIO, 570, 160],
                  [platforms.PIEDRA_FLOTANTE_DERECHA, 640, 160], 
                  
                  [platforms.ESTRELLA_NINJA, 640, 5],                  
                  #3
                  [platforms.PIEDRA_FLOTANTE_IZQUIERDA, 200, 280],
                  [platforms.PIEDRA_FLOTANTE_MEDIO, 270, 280],
                  [platforms.PIEDRA_FLOTANTE_DERECHA, 340, 280], 
                  
                  [platforms.PIEDRA_FLOTANTE_IZQUIERDA, 800, 400],
                  [platforms.PIEDRA_FLOTANTE_MEDIO, 870, 400],
                  [platforms.PIEDRA_FLOTANTE_DERECHA, 940, 400],
                  
                  [platforms.PIEDRA_FLOTANTE_IZQUIERDA, 1100, 500],
                  [platforms.PIEDRA_FLOTANTE_MEDIO, 1170, 500],
                  [platforms.PIEDRA_FLOTANTE_DERECHA, 1240, 500],
                  
                  [platforms.INTERROGACION, 1240, 330],
                  
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  
                  [platforms.PIEDRA_IZQUIERDA, 1880, 530],
                  [platforms.PIEDRA_CENTRO, 1950, 530],
                  [platforms.PIEDRA_CENTRO, 2020, 530],
                  [platforms.PIEDRA_CENTRO, 2090, 530],
                  [platforms.PIEDRA_CENTRO, 2160, 530],
                  [platforms.PIEDRA_CENTRO, 2230, 530],
                  [platforms.PIEDRA_DERECHA, 2300, 530],                   
                  ]
 
 
        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
 
        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.PIEDRITA_FOTANTE_CENTRO)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
 
 
# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.background = pygame.image.load("background_02.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1000
 
        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.STONE_PLATFORM_LEFT, 500, 550],
                  [platforms.STONE_PLATFORM_MIDDLE, 570, 550],
                  [platforms.STONE_PLATFORM_RIGHT, 640, 550],
                  [platforms.PIEDRA_FLOTANTE_IZQUIERDA, 800, 400],
                  [platforms.PIEDRA_FLOTANTE_MEDIO, 870, 400],
                  [platforms.PIEDRA_FLOTANTE_DERECHA, 940, 400],
                  [platforms.PIEDRA_FLOTANTE_IZQUIERDA, 1000, 500],
                  [platforms.PIEDRA_FLOTANTE_MEDIO, 1070, 500],
                  [platforms.PIEDRA_FLOTANTE_DERECHA, 1140, 500],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  ]
 
 
        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
 
        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)