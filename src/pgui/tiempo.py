import pygame

class Tiempo(object):
    
    def __init__(self,x,y):
        self.fuente = pygame.font.Font(None, 40)
        self.numero_de_fotogramas = 60*90
        self.tasa_fotogramas = 60
        self.segundos_totales=0
        self.minutos=0
        self.segundos=0
        self.pos=(x,y)

                
           
        
    def mostrar_tiempo(self,pantalla):
        
        texto_de_salida = "{0:02}:{1:02}".format(self.minutos, self.segundos)
        texto = self.fuente.render(texto_de_salida, True, (0, 0 ,0))
        pantalla.blit(texto, self.pos)

    def update(self):
        self.numero_de_fotogramas -= 1
        if self.numero_de_fotogramas < 0:
            self.numero_de_fotogramas = 0
        self.segundos_totales = self.numero_de_fotogramas // self.tasa_fotogramas
        
        self.minutos = self.segundos_totales // 60       
        self.segundos = self.segundos_totales % 60        
        
        