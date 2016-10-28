import pygame
import tiempo
import counter

class Gui(object):
    
    def __init__(self):
        self.clock = tiempo.Tiempo(20,20)
        self.health = counter.Counter("pgui/heart.png", 200, 20)
        self.shurikens = counter.Counter("pgui/shuriken.png", 400, 20)
        
    def draw(self, screen):
        self.clock.mostrar_tiempo(screen)
        self.health.draw(screen)
        self.shurikens.draw(screen)
        
    def update(self, player):
        self.clock.update()
        self.health.update(player.health)
        self.shurikens.update(player.shurikens)