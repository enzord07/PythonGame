import pygame
 
import constants
 
from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet
from shuriken import Shuriken
from attack import Attack
import enemy
from enemy_activator import Enemy_Activator
 
class Player(pygame.sprite.Sprite):
 
    def __init__(self):
 
        super(Player, self).__init__()
        
        self.sword_sound = pygame.mixer.Sound("game/EspadaSonido.wav")
        self.shuriken_sound = pygame.mixer.Sound("game/shuriken.wav")
        
        # Salud del personaje
        self.health = 5
        
        # Cantidad de Shurikens
        self.shurikens = 10
        
        # Velocidad del personaje
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
        self.crouched_frames_r = []
        self.crouched_frames_l = []
        self.crouchedwalking_frames_l = []
        self.crouchedwalking_frames_r = []
        self.attack_frames_l = []
        self.attack_frames_r = []
        self.attackshuriken_frames_l = []
        self.attackshuriken_frames_r = []
        self.hurt_frames_r = []
        self.hurt_frames_l = []
        self.die_frames_l = []
        self.die_frames_r = []
        
        # Numero de Frame a mostrar
        self.frame=0
        
        # Direccion del personaje
        self.direction = "R"
        
        # Accion del personaje
        self.action = "S"
 
        # Lista de sprites que podemos impactar
        self.level = None
        
        # Lista de shurikens arrojados
        self.shuriken_list = pygame.sprite.Group()
        
        # Sprite de ataque
        self.attack_list = pygame.sprite.Group()
        
        if isinstance(self, enemy.Enemy):
            self.image_file = "game/enemy.png"
        else:
            self.image_file = "game/ninja.png"
        
        # Cargar hoja de sprites
        sprite_sheet = SpriteSheet(self.image_file)
        self.spritesheet = sprite_sheet
        
        # Esta muerto?
        self.death=False
        
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
        image = sprite_sheet.get_image(134,286,39,49)
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
        image = sprite_sheet.get_image(134,286,39,49)
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
        
        # Cargar ambas caras de CROUCHED
        image = sprite_sheet.get_image(4,146,26,55)
        self.crouched_frames_r.append(image)
        image = sprite_sheet.get_image(79,163,34,39)
        self.crouched_frames_r.append(image)        
        image = sprite_sheet.get_image(173,165,29,36)
        self.crouched_frames_r.append(image)       
        
        image = sprite_sheet.get_image(4,146,26,55)
        image = pygame.transform.flip(image, True, False)
        self.crouched_frames_l.append(image)
        image = sprite_sheet.get_image(79,163,34,39)
        image = pygame.transform.flip(image, True, False)
        self.crouched_frames_l.append(image)        
        image = sprite_sheet.get_image(173,165,29,36)
        image = pygame.transform.flip(image, True, False)
        self.crouched_frames_l.append(image)         
        
        # Cargar ambas caras de CROUCHED WALKING
        image = sprite_sheet.get_image(269,165,39,37)
        self.crouchedwalking_frames_r.append(image)
        image = sprite_sheet.get_image(315,166,39,35)
        self.crouchedwalking_frames_r.append(image)        
        image = sprite_sheet.get_image(355,167,35,34)
        self.crouchedwalking_frames_r.append(image)
        image = sprite_sheet.get_image(392,167,34,34)
        self.crouchedwalking_frames_r.append(image)
        image = sprite_sheet.get_image(427,168,35,33)
        self.crouchedwalking_frames_r.append(image)
        image = sprite_sheet.get_image(355,167,35,34)
        self.crouchedwalking_frames_r.append(image) 
        image = sprite_sheet.get_image(315,166,39,35)
        self.crouchedwalking_frames_r.append(image) 
        
        image = sprite_sheet.get_image(269,165,39,37)
        image = pygame.transform.flip(image, True, False)
        self.crouchedwalking_frames_l.append(image)
        image = sprite_sheet.get_image(315,166,39,35)
        image = pygame.transform.flip(image, True, False)
        self.crouchedwalking_frames_l.append(image)        
        image = sprite_sheet.get_image(355,167,35,34)
        image = pygame.transform.flip(image, True, False)
        self.crouchedwalking_frames_l.append(image)
        image = sprite_sheet.get_image(392,167,34,34)
        image = pygame.transform.flip(image, True, False)
        self.crouchedwalking_frames_l.append(image)
        image = sprite_sheet.get_image(427,168,35,33)
        image = pygame.transform.flip(image, True, False)
        self.crouchedwalking_frames_l.append(image)
        image = sprite_sheet.get_image(355,167,35,34)
        image = pygame.transform.flip(image, True, False)
        self.crouchedwalking_frames_l.append(image) 
        image = sprite_sheet.get_image(315,166,39,35)
        image = pygame.transform.flip(image, True, False)
        self.crouchedwalking_frames_l.append(image)
        
        # Cargar ambas caras de ATTACK
        image = sprite_sheet.get_image(5,425,58,67)
        self.attack_frames_r.append(image)
        image = sprite_sheet.get_image(66,426,48,66)
        self.attack_frames_r.append(image)
        image = sprite_sheet.get_image(114,427,71,65)
        self.attack_frames_r.append(image)
        image = sprite_sheet.get_image(191,427,68,67)
        self.attack_frames_r.append(image)
        image = sprite_sheet.get_image(265,451,44,41)
        self.attack_frames_r.append(image)        
        
        image = sprite_sheet.get_image(5,425,58,67)
        image = pygame.transform.flip(image, True, False)
        self.attack_frames_l.append(image)
        image = sprite_sheet.get_image(66,426,48,66)
        image = pygame.transform.flip(image, True, False)
        self.attack_frames_l.append(image)
        image = sprite_sheet.get_image(114,427,71,65)
        image = pygame.transform.flip(image, True, False)
        self.attack_frames_l.append(image)
        image = sprite_sheet.get_image(191,427,68,67)
        image = pygame.transform.flip(image, True, False)
        self.attack_frames_l.append(image)
        image = sprite_sheet.get_image(265,451,44,41)
        image = pygame.transform.flip(image, True, False)
        self.attack_frames_l.append(image)
        
        # Cargar ambas caras de ATTACKSHURIKEN
        image = sprite_sheet.get_image(8,2437,41,46)
        self.attackshuriken_frames_r.append(image)
        image = sprite_sheet.get_image(57,2443,61,40)
        self.attackshuriken_frames_r.append(image)
        image = sprite_sheet.get_image(124,2443,66,40)
        self.attackshuriken_frames_r.append(image)
        image = sprite_sheet.get_image(214,2443,65,40)
        self.attackshuriken_frames_r.append(image)
        
        image = sprite_sheet.get_image(8,2437,41,46)
        image = pygame.transform.flip(image, True, False)
        self.attackshuriken_frames_l.append(image)
        image = sprite_sheet.get_image(57,2443,61,40)
        image = pygame.transform.flip(image, True, False)
        self.attackshuriken_frames_l.append(image)
        image = sprite_sheet.get_image(124,2443,66,40)
        image = pygame.transform.flip(image, True, False)
        self.attackshuriken_frames_l.append(image)
        image = sprite_sheet.get_image(214,2443,65,40)
        image = pygame.transform.flip(image, True, False)
        self.attackshuriken_frames_l.append(image)         
        
        
        # Cargar ambas caras de HURT
        
        image = sprite_sheet.get_image(134,1062,53,53)
        self.hurt_frames_r.append(image)
        image = sprite_sheet.get_image(193,1061,43,54)
        self.hurt_frames_r.append(image)           
        image = sprite_sheet.get_image(247,1065,41,50)
        self.hurt_frames_r.append(image)           

        image = sprite_sheet.get_image(134,1062,53,53)
        image = pygame.transform.flip(image, True, False)
        self.hurt_frames_l.append(image)
        image = sprite_sheet.get_image(193,1061,43,54)
        image = pygame.transform.flip(image, True, False)
        self.hurt_frames_l.append(image)           
        image = sprite_sheet.get_image(247,1065,41,50)
        image = pygame.transform.flip(image, True, False)
        self.hurt_frames_l.append(image)          
        
        # Cargar ambas caras de DIE
        image = sprite_sheet.get_image(266,221,32,55)
        self.die_frames_r.append(image)     
        image = sprite_sheet.get_image(306,1220,30,56)
        self.die_frames_r.append(image)
        image = sprite_sheet.get_image(344,1233,33,43)
        self.die_frames_r.append(image)
        image = sprite_sheet.get_image(382,1234,33,42)
        self.die_frames_r.append(image)
        image = sprite_sheet.get_image(419,1236,27,40)
        self.die_frames_r.append(image)
        image = sprite_sheet.get_image(493,1238,27,38)
        self.die_frames_r.append(image)
        image = sprite_sheet.get_image(530,1243,30,33)
        self.die_frames_r.append(image)   
        image = sprite_sheet.get_image(567,1250,38,27)
        self.die_frames_r.append(image)  
        image = sprite_sheet.get_image(609,1260,49,18)
        self.die_frames_r.append(image)  
        image = sprite_sheet.get_image(660,1258,51,20)
        self.die_frames_r.append(image)  
        image = sprite_sheet.get_image(716,1258,50,20)
        self.die_frames_r.append(image)  
        image = sprite_sheet.get_image(771,1261,48,19)
        self.die_frames_r.append(image)  
        
        image = sprite_sheet.get_image(266,221,32,55)
        image = pygame.transform.flip(image, True, False)
        self.die_frames_l.append(image)     
        image = sprite_sheet.get_image(306,1220,30,56)
        image = pygame.transform.flip(image, True, False)
        self.die_frames_l.append(image)
        image = sprite_sheet.get_image(344,1233,33,43)
        image = pygame.transform.flip(image, True, False)
        self.die_frames_l.append(image)
        image = sprite_sheet.get_image(382,1234,33,42)
        image = pygame.transform.flip(image, True, False)
        self.die_frames_l.append(image)
        image = sprite_sheet.get_image(419,1236,27,40)
        image = pygame.transform.flip(image, True, False)
        self.die_frames_l.append(image)
        image = sprite_sheet.get_image(493,1238,27,38)
        image = pygame.transform.flip(image, True, False)
        self.die_frames_l.append(image)
        image = sprite_sheet.get_image(530,1243,30,33)
        image = pygame.transform.flip(image, True, False)
        self.die_frames_l.append(image)   
        image = sprite_sheet.get_image(567,1250,38,27)
        image = pygame.transform.flip(image, True, False)
        self.die_frames_l.append(image)  
        image = sprite_sheet.get_image(609,1260,49,18)
        image = pygame.transform.flip(image, True, False)
        self.die_frames_l.append(image)  
        image = sprite_sheet.get_image(660,1258,51,20)
        image = pygame.transform.flip(image, True, False)
        self.die_frames_l.append(image)  
        image = sprite_sheet.get_image(716,1258,50,20)
        image = pygame.transform.flip(image, True, False)
        self.die_frames_l.append(image)  
        image = sprite_sheet.get_image(771,1261,48,19)
        image = pygame.transform.flip(image, True, False)
        self.die_frames_l.append(image)        
        
        # Rectangulo del sprite
        self.image = pygame.Surface([25,58])
             
        self.rect = self.image.get_rect()
        self.image.fill(constants.BLUE)
        
        # Sprite usado para activar a los enemigos
        self.enemy_activator = pygame.sprite.Group()
        self.enemy_activator.add(Enemy_Activator())
        
        # Seleccionar con que imagen va a comenzar
        self.draw_image = self.walking_frames_r[0]
        self.draw_rect = self.rect.copy()
        
        # Reloj para la hoja de sprites
        self.reloj = 0
 
    def update(self):
        """ Actualizar al jugador """
        
        self.shuriken_update()
        self.attack_update()
        for e in self.enemy_activator:
            e.rect.midbottom = self.rect.midbottom

        
        # Gravedad
        self.calc_grav()
        
        # Seleccionar imagen del personaje
        self.select_image()
        
        # Ajustar el tamanio del sprite de acuerdo a la imagen
        self.sprite_config()
        
        # Centrar la imagen en el sprite
        self.draw_rect= self.draw_image.get_rect()
        self.draw_rect.midbottom = self.rect.midbottom
        
        # Incrementar reloj
        self.reloj+=1        
 
        # Move izquierda/derecha
        if self.action != "F" and self.action != "A" and self.action != "D" and self.action != "a": 
            self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift

        
        # Acomodar si impacta con una plataforma
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right
 
 
        # Mover arriba/abajo
        
        if (self.action == "J")and(self.reloj==5):
            self.change_y = -10
        self.rect.y += self.change_y
        if self.change_y>1:
            if self.action!="f":
                self.action = "f"
                self.reset_anim()
 
        # Chequear si impacta con alguna plataforma
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # Resetar la posicion basado en la parte superior/inferior del objeto.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                if self.change_y > 9:
                    if self.health==0:
                        self.action = "D"
                        self.reset_anim()
                    else:
                        self.action="F"
                        self.reset_anim()
                elif (self.action == "J" and self.reloj>5) or self.action == "f":
                    if self.health==0:
                        self.action = "D"
                        self.reset_anim()
                    elif self.change_x==0:
                        self.action="S"
                    elif self.change_x==-2 or self.change_x==2:
                        self.action="W"
                    else:
                        self.action="R"
                    self.reset_anim()                  
                    
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Detener el movimiento vertical
            self.change_y = 0
 
            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .4
 
        # Ver si sale de la pantalla por abajo
        if self.rect.y >= constants.SCREEN_HEIGHT and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT + 50
            self.action= "D"
            self.health = 0
 
    def jump(self):
 
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
        
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            if self.action != "F" and self.action != "H" and self.action != "D":
                self.action= "J"
                self.reset_anim()
            
    def go_left(self):
        self.change_x = -2
        if self.action != "D":
            self.direction = "L"
        if self.action =="S":
            self.action = "W"
            self.reset_anim()
        if self.action == "C" or self.action == "w":
            self.change_x = -1
            self.action = "w"
            self.reset_anim()
            
    def run_left(self):
        if self.action =="S":
            self.change_x= -4
            self.action = "R"
            self.reset_anim()
        else:
            self.go_left()
 
    def go_right(self):
        self.change_x = 2
        if self.action != "D":
            self.direction = "R"
        if self.action =="S":
            self.action = "W"
            self.reset_anim()
        if self.action == "C" or self.action == "w":
            self.change_x = 1
            self.action = "w"
            self.reset_anim()        
            
    def run_right(self):
        if self.action =="S":
            self.change_x = 4
            self.action = "R"
            self.reset_anim()
        else:
            self.go_right()
            
    def crouch(self):
        if self.action == "S" or self.action == "A" or self.action == "W" or self.action == "R" or self.action == "F" or self.action == "a":
            self.change_x=0
            self.action = "C"
            self.reset_anim()
    
    def stop(self):
        self.change_x = 0
        if self.action == "W" or self.action == "R" or self.action == "C" or self.action=="A" or self.action=="a":
            self.action = "S"
            self.frame = 0
        if self.action == "w":
            self.action = "C"
        
    def go_up(self):
        if self.action == "w":
            self.action = "W"
            self.change_x += self.change_x
            self.reset_anim()
        elif self.action == "C":
            self.action = "S"
            self.reset_anim()
    
    def attack(self):
        if self.action == "S" or self.action == "W" or self.action== "R":
            self.sword_sound.play()
            if self.direction=="R":
                self.attack_list.add(Attack(self.rect.right,self.rect.y))
            else:
                self.attack_list.add(Attack(self.rect.left - 20,self.rect.y))
            self.action = "A"
            self.change_x = 0
            self.reset_anim()
        
    def attackshuriken(self):
        if (self.action == "S" or self.action == "W" or self.action== "R") and self.shurikens != 0:
            self.shuriken_sound.play()
            self.shurikens -= 1
            if self.direction=="R":
                self.shuriken_list.add(Shuriken(self.rect.right,self.rect.y + 8, self.direction,self.spritesheet))
            else:
                self.shuriken_list.add(Shuriken(self.rect.left,self.rect.y + 8, self.direction, self.spritesheet))
            self.action = "a"
            self.change_x = 0
            self.reset_anim()        
            
    def hurt(self):
        self.health-=1
        if self.direction=="R":
            self.change_x = -3
        else:
            self.change_x = 3
        if self.action != "J" and self.action != "f" and self.action != "D":
            self.action = "H"
            self.reset_anim()
        else:
            self.change_x=0
        if self.health <= 0 and self.action != "D":
            self.health=0
            self.die()
            
    def heal(self):
        self.health += 1
        
    def die(self):
        if self.action != "J" and self.action != "f":
            self.action = "D"
            self.reset_anim()
        else:
            self.change_x=0
            
    def reset_anim(self):
        self.reloj = 0
        self.frame = 0
        
    def sprite_config(self):
        if self.action == "C" or self.action == "w" or self.action == "F":
            dif = self.rect.height - 36
            self.rect.height = 36
            self.rect.y += dif
        elif self.action == "D":
            dif = self.rect.height - 6
            self.rect.height = 6
            self.rect.y += dif            
        else:
            dif = self.rect.height - 58
            self.rect.height = 58
            self.rect.y += dif
        
    def select_image(self):
        if self.action == "W":
            if (self.reloj % 7)==0:
                self.frame = self.reloj // 7
                if self.frame>len(self.walking_frames_r)-1:
                    self.reset_anim()
                if self.direction=="R":
                    self.draw_image = self.walking_frames_r[self.frame]
                else:
                    self.draw_image = self.walking_frames_l[self.frame]
        elif self.action == "S":
            if (self.reloj % 7)==0:
                self.frame = self.reloj // 7
                if self.frame>len(self.stopped_frames_r)-1:
                    self.reset_anim()            
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
            elif self.reloj==25:
                self.frame=3
            elif self.reloj==35:
                self.frame=4
            if self.direction=="R":
                self.draw_image = self.stoppedjumping_frames_r[self.frame]
            else:
                self.draw_image = self.stoppedjumping_frames_l[self.frame]
        elif self.action == "f":
            if (self.reloj % 7)==0:
                self.frame = self.reloj // 7
                if self.frame>len(self.falling_frames_r)-1:
                    self.reset_anim()
                if self.direction=="R":
                    self.draw_image = self.falling_frames_r[self.frame]
                else:
                    self.draw_image = self.falling_frames_l[self.frame]
        elif self.action == "F":
            if (self.reloj % 7)==0:
                self.frame = self.reloj // 7
                if self.frame>len(self.fall_frames_r)-1:
                    if self.change_x!=0:
                        self.action="W"
                        if self.direction=="R":
                            self.change_x=2
                        else:
                            self.change_x=-2
                    else:
                        self.action="S"
                    self.reset_anim()
                else:
                    if self.direction=="R":
                        self.draw_image = self.fall_frames_r[self.frame]
                    else:
                        self.draw_image = self.fall_frames_l[self.frame]
        elif self.action == "R":
            if (self.reloj % 7)==0:
                self.frame = self.reloj // 7
                if self.frame>len(self.running_frames_r)-1:
                    self.reset_anim()
                if self.direction=="R":
                    self.draw_image = self.running_frames_r[self.frame]
                else:
                    self.draw_image = self.running_frames_l[self.frame]
        elif self.action == "C":
            if (self.reloj % 3)==0:
                self.frame = self.reloj // 3
                if self.frame>len(self.crouched_frames_r)-1:
                    self.frame = len(self.crouched_frames_r)-1
                else:
                    if self.direction=="R":
                        self.draw_image = self.crouched_frames_r[self.frame]
                    else:
                        self.draw_image = self.crouched_frames_l[self.frame]
        elif self.action == "w":
            if (self.reloj % 7)==0:
                self.frame = self.reloj // 7
                if self.frame>len(self.crouchedwalking_frames_r)-1:
                    self.reset_anim()
                if self.direction=="R":
                    self.draw_image = self.crouchedwalking_frames_r[self.frame]
                else:
                    self.draw_image = self.crouchedwalking_frames_l[self.frame]
        elif self.action == "A":
            if (self.reloj % 3)==0:
                self.frame = self.reloj // 3
                if self.frame>len(self.attack_frames_r)-1:
                    if self.change_x==0:
                        self.action="S"
                    else:
                        self.action="W"
                else:
                    if self.direction=="R":
                        self.draw_image = self.attack_frames_r[self.frame]
                    else:
                        self.draw_image = self.attack_frames_l[self.frame]
        elif self.action == "H":
            if (self.reloj % 4)==0:
                self.frame = self.reloj // 4
                if self.frame>len(self.hurt_frames_r)-1:
                        self.action="S"
                        self.change_x=0;
                else:
                    if self.direction=="R":
                        self.draw_image = self.hurt_frames_r[self.frame]
                    else:
                        self.draw_image = self.hurt_frames_l[self.frame]
        elif self.action == "D":
            self.death = True
            if (self.reloj % 7)==0:
                self.frame = self.reloj // 7
                if self.frame>len(self.die_frames_r)-1:
                        pass
                else:
                    if self.direction=="R":
                        self.draw_image = self.die_frames_r[self.frame]
                    else:
                        self.draw_image = self.die_frames_l[self.frame]
        elif self.action == "a":
            if (self.reloj % 3)==0:
                self.frame = self.reloj // 3
                if self.frame>len(self.attackshuriken_frames_r)-1:
                    if self.change_x==0:
                        self.action="S"
                    else:
                        self.action="W"
                else:
                    if self.direction=="R":
                        self.draw_image = self.attackshuriken_frames_r[self.frame]
                    else:
                        self.draw_image = self.attackshuriken_frames_l[self.frame]        
    
    def shuriken_update(self):
        for s in self.shuriken_list:
            # Si se acaba el tiempo de vida del shuriken, eliminarlo.
            if s.life_time==0:
                self.shuriken_list.remove(s)
            else:
                # Chequear si impacta con alguna plataforma
                block_hit_list = pygame.sprite.spritecollide(s, self.level.platform_list, False)
                for block in block_hit_list:
                    self.shuriken_list.remove(s)
        self.shuriken_list.update()
    
    def attack_update(self):
        for a in self.attack_list:
            if a.life_time==0:
                self.attack_list.remove(a)
        self.attack_list.update()
    