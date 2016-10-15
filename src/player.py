"""
This module is used to hold the Player class. The Player represents the user-
controlled sprite on the screen.
"""
import pygame
 
import constants
 
from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet
 
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """
 
 
    # -- Methods
    def __init__(self):
        """ Constructor function """
 
        # Call the parent's constructor
        super(Player, self).__init__()
 
        # -- Attributes
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0
 
        # Listas de las animaciones del protagonista
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.stopped_frames_l = []
        self.stopped_frames_r = []
        self.stoppedjumping_frames_l = []
        self.stoppedjumping_frames_r = []
        self.falling_frames_l = []
        self.falling_frames_r = []
        self.fall_frames_r = []
        self.fall_frames_l = []
        self.running_frames_r = []
        self.running_frames_l = []
        
        #Numero de Frame a mostrar
        self.frame=0
        
        # Direccion del personaje
        self.direction = "R"
        
        # Accion del personaje
        
        self.action = "S"
 
        # List of sprites we can bump against
        self.level = None
 
        sprite_sheet = SpriteSheet("ninja.png")
        
        # Cargar la cara derecha de la accion WALKING
        image = sprite_sheet.get_image(1, 76, 37, 58)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(45, 76, 33, 58)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(84, 76, 46, 58)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(132, 76, 41, 58)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(176, 76, 39, 58)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(220, 76, 35, 58)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(260, 76, 42, 58)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(308, 76, 44, 58)
        self.walking_frames_r.append(image)        
 
        # Cargar la cara izquierda de la accion WALKING
        image = sprite_sheet.get_image(1, 76, 37, 58)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(45, 76, 33, 58)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(84, 76, 46, 58)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(132, 76, 41, 58)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(176, 76, 39, 58)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)        
        image = sprite_sheet.get_image(220, 76, 35, 58)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(260, 76, 42, 58)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(308, 76, 44, 58)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        
        # Cargar ambas caras de la accion STOPPED
        image = sprite_sheet.get_image(3, 3, 29, 61)
        self.stopped_frames_r.append(image)
        
        image = sprite_sheet.get_image(3, 3, 29, 61)
        image = pygame.transform.flip(image, True, False)
        self.stopped_frames_l.append(image)        
 
        # Cargar ambas caras de STOPPED JUMPING
        image = sprite_sheet.get_image(252,301,39,40)
        self.stoppedjumping_frames_r.append(image)
        image = sprite_sheet.get_image(300,281,32,60)
        self.stoppedjumping_frames_r.append(image)
        image = sprite_sheet.get_image(337,281,31,52)
        self.stoppedjumping_frames_r.append(image)
        image = sprite_sheet.get_image(374,283,31,39)
        self.stoppedjumping_frames_r.append(image)
        
        image = sprite_sheet.get_image(252,301,39,40)
        image = pygame.transform.flip(image, True, False)
        self.stoppedjumping_frames_l.append(image)
        image = sprite_sheet.get_image(300,281,32,60)
        image = pygame.transform.flip(image, True, False)
        self.stoppedjumping_frames_l.append(image)      
        image = sprite_sheet.get_image(337,281,31,52)
        image = pygame.transform.flip(image, True, False)
        self.stoppedjumping_frames_l.append(image)
        image = sprite_sheet.get_image(374,283,31,39)
        image = pygame.transform.flip(image, True, False)
        self.stoppedjumping_frames_l.append(image)
        
        # Cargar ambas caras de FALLING
        image = sprite_sheet.get_image(3,355,39,40)
        self.falling_frames_r.append(image)
        image = sprite_sheet.get_image(49,355,40,44)
        self.falling_frames_r.append(image)
        image = sprite_sheet.get_image(92,357,40,43)
        self.falling_frames_r.append(image)
        image = sprite_sheet.get_image(135,356,39,47)
        self.falling_frames_r.append(image)
        image = sprite_sheet.get_image(178,356,39,47)
        self.falling_frames_r.append(image)
        
        image = sprite_sheet.get_image(3,355,39,40)
        image = pygame.transform.flip(image, True, False)
        self.falling_frames_l.append(image)
        image = sprite_sheet.get_image(49,355,40,44)
        image = pygame.transform.flip(image, True, False)
        self.falling_frames_l.append(image)
        image = sprite_sheet.get_image(92,357,40,43)
        image = pygame.transform.flip(image, True, False)
        self.falling_frames_l.append(image)
        image = sprite_sheet.get_image(135,356,39,47)
        image = pygame.transform.flip(image, True, False)
        self.falling_frames_l.append(image)
        image = sprite_sheet.get_image(178,356,39,47)
        image = pygame.transform.flip(image, True, False)
        self.falling_frames_l.append(image)        
        
        # Cargar ambas caras de FALL
        image = sprite_sheet.get_image(248,353,35,61)
        self.fall_frames_r.append(image)
        image = sprite_sheet.get_image(288,363,37,51)
        self.fall_frames_r.append(image)
        image = sprite_sheet.get_image(328,380,32,33)
        self.fall_frames_r.append(image)        
        image = sprite_sheet.get_image(367,376,35,37)
        self.fall_frames_r.append(image)
        
        image = sprite_sheet.get_image(248,353,35,61)
        image = pygame.transform.flip(image, True, False)
        self.fall_frames_l.append(image)
        image = sprite_sheet.get_image(288,363,37,51)
        image = pygame.transform.flip(image, True, False)
        self.fall_frames_l.append(image)
        image = sprite_sheet.get_image(328,380,32,33)
        image = pygame.transform.flip(image, True, False)
        self.fall_frames_l.append(image)        
        image = sprite_sheet.get_image(367,376,35,37)
        image = pygame.transform.flip(image, True, False)
        self.fall_frames_l.append(image)
        
        # Cargar ambas caras de RUNNING
        image = sprite_sheet.get_image(3,225,60,44)
        self.running_frames_r.append(image)
        image = sprite_sheet.get_image(69,226,57,45)
        self.running_frames_r.append(image)
        image = sprite_sheet.get_image(130,226,49,45)
        self.running_frames_r.append(image)        
        image = sprite_sheet.get_image(182,226,61,42)
        self.running_frames_r.append(image)
        image = sprite_sheet.get_image(247,225,53,45)
        self.running_frames_r.append(image)
        image = sprite_sheet.get_image(304,226,51,45)
        self.running_frames_r.append(image)
        
        image = sprite_sheet.get_image(3,225,60,44)
        image = pygame.transform.flip(image, True, False)
        self.running_frames_l.append(image)
        image = sprite_sheet.get_image(69,226,57,45)
        image = pygame.transform.flip(image, True, False)
        self.running_frames_l.append(image)
        image = sprite_sheet.get_image(130,226,49,45)
        image = pygame.transform.flip(image, True, False)
        self.running_frames_l.append(image)        
        image = sprite_sheet.get_image(182,226,61,42)
        image = pygame.transform.flip(image, True, False)
        self.running_frames_l.append(image)
        image = sprite_sheet.get_image(247,225,53,45)
        image = pygame.transform.flip(image, True, False)
        self.running_frames_l.append(image)
        image = sprite_sheet.get_image(304,226,51,45)
        image = pygame.transform.flip(image, True, False)
        self.running_frames_l.append(image)        
        
        
        
        # Set a reference to the image rect.
        self.image = pygame.Surface([29,58])
             
        self.rect = self.image.get_rect()
        self.image.fill(constants.BLUE)
        
        # Set the image the player starts with
        self.draw_image = self.walking_frames_r[0]
        self.draw_rect = self.rect.copy()
        
        # Reloj para la hoja de sprites
        self.reloj = 0
        
        # Estado del Personaje
        self.status = 0
 
    def update(self):
        """ Move the player. """       

        # Gravity
        self.calc_grav()
        
        #Seleccionar imagen
        self.select_image()         
 
        # Move izquierda/derecha
        if self.action!= "F":
            self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift

        
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        
        if (self.action == "J")and(self.reloj==5):
            self.change_y = -10
        self.rect.y += self.change_y
        if self.change_y>8:
            if self.action!="f":
                self.action = "f"
                self.frame = 0
                reloj = 0
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                if self.action == "f":
                    self.action="F"
                    self.frame=0
                    self.reloj=0
                elif self.action == "J" and self.reloj>5:
                    if self.change_x==0:
                        self.action="S"                       
                    elif self.change_x==-2 or self.change_x==2:
                        self.action="W"
                    else:
                        self.action="R"
                    self.frame=0
                    self.reloj=0                    
                        
                    
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
 
            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x
                
        # Incrementar reloj
        self.reloj+=1
        
        #Centar la imagen en el sprite
        self.draw_rect= self.draw_image.get_rect()
        self.draw_rect.midbottom = self.rect.midbottom
 
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .4
 
        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
 
    def jump(self):
        """ Called when user hits 'jump' button. """
 
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
        
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            if self.action != "F":
                self.action= "J"
                self.frame= 0
                self.reloj=0
            
 
    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -2
        self.direction = "L"
        if self.action =="S":
            self.action = "W"
            self.reloj = 0
            
    def run_left(self):
        self.change_x= -4
        if self.action =="S":
            self.action = "R"
            self.reloj = 0
            self.frame = 0
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 2
        self.direction = "R"
        if self.action =="S":
            self.action = "W"
            self.reloj = 0
            self.frame = 0
            
    def run_right(self):
        self.change_x = 4
        if self.action =="S":
            self.action = "R"
            self.reloj = 0        
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        if self.action == "W" or self.action == "R":
            self.action = "S"
            self.frame = 0
        
    def select_image(self):
        if self.action == "W":
            if (self.reloj % 7)==0:
                self.frame+=1
                if self.frame>len(self.walking_frames_r)-1:
                    self.frame=0
                if self.direction=="R":
                    self.draw_image = self.walking_frames_r[self.frame]
                else:
                    self.draw_image = self.walking_frames_l[self.frame]
        elif self.action == "S":
            if self.direction=="R":
                self.draw_image = self.stopped_frames_r[self.frame]
            else:
                self.draw_image = self.stopped_frames_l[self.frame]
        elif self.action == "J":
            if self.reloj==0:
                self.frame=0
            elif self.reloj==5:
                self.frame=1
            elif self.reloj==15:
                self.frame=2
            elif self.reloj==30:
                self.frame=3
            if self.direction=="R":
                self.draw_image = self.stoppedjumping_frames_r[self.frame]
            else:
                self.draw_image = self.stoppedjumping_frames_l[self.frame]
        elif self.action == "f":
            if (self.reloj % 7)==0:
                self.frame+=1
                if self.frame>len(self.falling_frames_r)-1:
                    self.frame=0
                if self.direction=="R":
                    self.draw_image = self.falling_frames_r[self.frame]
                else:
                    self.draw_image = self.falling_frames_l[self.frame]
        elif self.action == "F":
            if (self.reloj % 7)==0:
                self.frame+=1
                if self.frame>len(self.fall_frames_r)-1:
                    if self.change_x!=0:
                        self.action="W"
                    else:
                        self.action="S"
                    self.frame=0
                else:
                    if self.direction=="R":
                        self.draw_image = self.fall_frames_r[self.frame]
                    else:
                        self.draw_image = self.fall_frames_l[self.frame]
        elif self.action == "R":
            if (self.reloj % 7)==0:
                self.frame+=1
                if self.frame>len(self.running_frames_r)-1:
                    self.frame=0
                if self.direction=="R":
                    self.draw_image = self.running_frames_r[self.frame]
                else:
                    self.draw_image = self.running_frames_l[self.frame]        