import pygame
 
import constants
import platforms
from enemy import Enemy
from Edited_Sprite_Group import Edited_Sprite_Group
 
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
        self.enemy_list = Edited_Sprite_Group()
        self.player = player
 
    # Update everythign on this level
    def update(self):
        """ Actualizar todo de este nivel"""
        self.platform_list.update()
        self.enemy_list.update()
        for enemy in self.enemy_list:
            enemy.ai(self.player)
            if enemy.death == True and enemy.reloj_ai==60*4:
                self.enemy_list.remove(enemy)
            # El enemigo fue golpeado por la espada?
            contacto = pygame.sprite.spritecollide(enemy, self.player.attack_list, False)
            for c in contacto:
                enemy.hurt()
            
            # El enemigo fue golpeado por un shuriken?
            contacto = pygame.sprite.spritecollide(enemy, self.player.shuriken_list, True)
            for c in contacto:
                enemy.hurt()
                
            # El enemigo esta en contacto con el activador?
            contacto = pygame.sprite.spritecollide(enemy, self.player.enemy_activator, False)
            cont = False
            for c in contacto:
                cont = True
                enemy.active(True)
            if cont == False:
                enemy.active(False)
            
            
            # El player impacto con algun shuriken del enemigo?
            contacto = pygame.sprite.spritecollide(self.player, enemy.shuriken_list, True)
            for c in contacto:
                self.player.hurt()
    
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
        for e in self.enemy_list:
            e.shuriken_list.draw(screen)
 
    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """
 
        # Keep track of the shift amount
        self.world_shift += shift_x
 
        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x
 
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
            for s in enemy.shuriken_list:
                s.rect.x += shift_x
        
        for shuriken in self.player.shuriken_list:
            shuriken.rect.x += shift_x
        
 
# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.background = pygame.image.load("game/nivel1.jpg").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -4000
 
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
                  [platforms.STONE_PLATFORM_LEFT, 500, 150],
                  [platforms.STONE_PLATFORM_MIDDLE, 570, 150],
                  [platforms.STONE_PLATFORM_RIGHT, 640, 150], 
                  
                  [platforms.ESTRELLA_NINJA, 640, 5],                  
                  #3
                  [platforms.PIEDRA_FLOTANTE_IZQUIERDA, 200, 280],
                  [platforms.PIEDRA_FLOTANTE_MEDIO, 270, 280],
                  [platforms.PIEDRA_FLOTANTE_DERECHA, 340, 280], 
                  #4
                  [platforms.PIEDRA_FLOTANTE_IZQUIERDA, 800, 400],
                  [platforms.PIEDRA_FLOTANTE_MEDIO, 870, 400],
                  [platforms.PIEDRA_FLOTANTE_DERECHA, 940, 400],
                  #5
                 # [platforms.PIEDRA_FLOTANTE_IZQUIERDA, 1100, 500],
                  #[platforms.PIEDRA_FLOTANTE_MEDIO, 1170, 500],
                  #[platforms.PIEDRA_FLOTANTE_DERECHA, 1240, 500],
                  
                  #6
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  
                  [platforms.PIEDRA_IZQUIERDA, 2090, 530],
                  [platforms.PIEDRA_CENTRO, 2160, 530],
                  [platforms.PIEDRA_CENTRO, 2230, 530],
                  [platforms.PIEDRA_CENTRO, 2300, 530],
                  [platforms.PIEDRA_CENTRO, 2370, 530],
                  [platforms.PIEDRA_CENTRO, 2440, 530],
                  [platforms.PIEDRA_DERECHA, 2510, 530],  
                  
                  [platforms.INTERROGACION, 2230, 330],                 
                  
                  #7
                  [platforms.PIEDRA_FLOTANTE_IZQUIERDA, 2600, 400],
                  [platforms.PIEDRA_FLOTANTE_MEDIO, 2670, 400],
                  [platforms.PIEDRA_FLOTANTE_DERECHA, 2740, 400],
                  #8
                  [platforms.PIEDRA_FLOTANTE_IZQUIERDA, 2900, 300],
                  [platforms.PIEDRA_FLOTANTE_MEDIO, 2970, 300],
                  [platforms.PIEDRA_FLOTANTE_DERECHA, 3040, 300],  
                  
                  [platforms.PIEDRA_IZQUIERDA, 3200, 160],
                  [platforms.PIEDRA_CENTRO, 3270, 160],
                  [platforms.PIEDRA_CENTRO, 3340, 160],
                  [platforms.PIEDRA_CENTRO, 3410, 160],
                  [platforms.PIEDRA_CENTRO, 3480, 160],
                  [platforms.PIEDRA_CENTRO, 3550, 160],
                  [platforms.PIEDRA_DERECHA, 3620, 160],      
                  
                  [platforms.PIEDRA_IZQUIERDA, 3200, 360],
                  [platforms.PIEDRA_CENTRO, 3270, 360],
                  [platforms.PIEDRA_CENTRO, 3340, 360],
                  [platforms.PIEDRA_CENTRO, 3410, 360],
                  [platforms.PIEDRA_CENTRO, 3480, 360],
                  [platforms.PIEDRA_CENTRO, 3550, 360],
                  [platforms.PIEDRA_DERECHA, 3620, 360],   
                  
                  [platforms.PIEDRA_IZQUIERDA, 3200, 530],
                  [platforms.PIEDRA_CENTRO, 3270, 530],
                  [platforms.PIEDRA_CENTRO, 3340, 530],
                  [platforms.PIEDRA_CENTRO, 3410, 530],
                  [platforms.PIEDRA_CENTRO, 3480, 530],
                  [platforms.PIEDRA_CENTRO, 3550, 530],
                  [platforms.PIEDRA_CENTRO, 3620, 530],
                  [platforms.PIEDRA_CENTRO, 3690, 530],
                  [platforms.PIEDRA_CENTRO, 3760, 530],
                  [platforms.PIEDRA_CENTRO, 3830, 530], 
                  [platforms.PIEDRA_DERECHA, 3900, 530],
                  
                  [platforms.EXIT, 3830, 460],
                  ]
        # Agregar enemigo [x,y]
        # Eje X pertenece a la mitad del personaje
        # Eje Y pertenece a la planta de los pies
        enemies = [[690,400],
                   [690,150],
                   [220,280],
                   [990,400],
                   [1320,280],
                   [2100,530],
                   [2265,330],
                   [2560,530],
                   [2790,400],
                   [3090,300],
                   [3210,160],
                   [3680,160],
                   [3210,360],
                   [3680,360],
                   [3210,590],
                   [3680,590]                   
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

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.PIEDRITA_FOTANTE_CENTRO)
        block.rect.x = 1700
        block.rect.y = 280
        block.boundary_left = 1700
        block.boundary_right = 1900
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block) 
        
        
        for enemy in enemies:
            self.enemy_list.add(Enemy(self,enemy[0],enemy[1]))
 
# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.background = pygame.image.load("game/background_02.png").convert()
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