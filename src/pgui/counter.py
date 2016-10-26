import pygame

class Counter(object):
    
    def __init__(self, imagen, x, y): #x,y de la imagen, el texto va a la izquierda de la imagen.
        
        self.num = 0
        self.fuente = pygame.font.Font(None, 40)
        self.pos=[x,y]
        self.image = pygame.image.load(imagen).convert()
        self.image.set_colorkey((0,255,0))
        
    def update(self,num):
        self.num = num
    
    def draw(self, screen):
        screen.blit(self.image,self.pos)
        screen.blit(self.fuente.render(str(self.num), True, (0, 0 ,0)), (self.pos[0] - 20, self.pos[1]))
        
        
        