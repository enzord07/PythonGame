from player import Player
from spritesheet_functions import SpriteSheet

class Enemy(Player):
    def __init__(self,level,posx,posy):
        super(Enemy, self).__init__()
        self.health = 1
        self.level = level
        self.rect.midbottom = [posx,posy]
        self.direction = "L"
        # Shurikens infinitos
        self.shurikens = -1
        self.reloj_ai = 0
        self.enemy_type = 0
        self.activated = False
        self.deactivate = False
        
        # Reloj que mantiene el enemigo activo por unos segundos mas
        self.reloj_delay=0
        
    def ai(self,player):
        self.reloj_ai +=1
        if (self.reloj_ai - self.reloj_delay) == 60*3:
            self.activated = False
        if self.activated:
            if self.rect.x < player.rect.x:
                self.direction = "R"
            else:
                self.direction = "L"
            if self.enemy_type == 0 and (self.reloj_ai % 60*3) ==0:
                self.attackshuriken()
        if self.action=="D" and self.death == False:
            self.death= True
            self.reloj_ai=0
    
    def active(self, b):
        if b==True:
            self.deactivate=False
            self.activated=True
        else:
            if self.activated == True and self.deactivate == False:
                self.deactivate=True
                self.reloj_delay=self.reloj_ai
         
            