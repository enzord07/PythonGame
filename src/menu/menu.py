import random
import pygame
from pygame.locals import *
import sys

#/////////////////CLASE OPCIONES/////////////////////////////////////////////
class Opcion:
    def __init__(self, fuente, titulo, x, y, paridad, funcion_asignada):
        self.imagen_normal = fuente.render(titulo, 1, (0, 0, 0))
        self.imagen_destacada = fuente.render(titulo, 1, (200, 0, 0))
        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = 500 * paridad
        self.rect.y = y
        self.funcion_asignada = funcion_asignada
        self.x = float(self.rect.x)

    def actualizar(self):
        destino_x = 50
        self.x += (destino_x - self.x) / 5.0
        self.rect.x = int(self.x)

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)

    def destacar(self, estado):
        if estado:
            self.image = self.imagen_destacada
        else:
            self.image = self.imagen_normal
    def activar(self):
        self.funcion_asignada()

#/////////////////////CLASE CURSOR///////////////////////////////////
class Cursor:

    def __init__(self, x, y, dy):
        self.image = pygame.image.load('menu/cursor.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_inicial = y
        self.dy = dy
        self.y = 0
        self.seleccionar(0)

    def actualizar(self):
        self.y += (self.to_y - self.y) / 10.0
        self.rect.y = int(self.y)

    def seleccionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)

#///////////////////Clase menu////////////////////////////////////
class Menu:
    "Representa un menu con opciones para un juego"
  #-------------------------------------------------------------  
    def __init__(self, opciones):
        self.opciones = []
        fuente = pygame.font.Font('menu/dejavu.ttf', 20)
        x = 50  #posicion del menu
        y = 480    #posicion del menu
        paridad = 1

        self.cursor = Cursor(x - 30, y, 30)

        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente, titulo, x, y, paridad, funcion))
            y += 30
            if paridad == 1:
                paridad = -1
            else:
                paridad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False
    #------------------------------------------------------------------
    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""
        
        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:
                # Invoca a la funcion asociada a la opcion.
                self.opciones[self.seleccionado].activar()
                return self.seleccionado

        # procura que el cursor este entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1
        
        self.cursor.seleccionar(self.seleccionado)

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]
        
        self.cursor.actualizar()
     
        for o in self.opciones:
            o.actualizar()
 #--------------------------------------------------------------
    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opcion del menu."""

        self.cursor.imprimir(screen)

        for opcion in self.opciones:
            opcion.imprimir(screen)

#//////////////////FUNCIONES//////////////////////////////////////////
def comenzar_nuevo_juego():
    pygame.mixer.music.stop()
#---------------------------------------------------------
def mostrar_opciones():
    pygame.mixer.music.play(2) #Cuando voy a opciones la musica vuelve a empezar
    print " Funcion que muestra otro menu de opciones."
#---------------------------------------------------------
def salir_del_programa():
    pygame.mixer.music.stop()
    #import sys
    #sys.exit(0)

#---------------------------------------------------------
# ////////////////OPCIONES EN TUPLA///////////////////////////////

def main(s):
    
    salir = False

    pygame.mixer.music.load("menu/NinjaMenu.mp3")
    pygame.mixer.music.play(2)
    
    opciones = [
        ("Jugar", comenzar_nuevo_juego),
        ("Opciones", mostrar_opciones),
        ("Salir", salir_del_programa)
        ]
    screen = s
    fondo = pygame.image.load("menu/ninja heroe.png").convert()
    menu = Menu(opciones)

    while not salir:

        for e in pygame.event.get():
            if e.type == pygame.QUIT: #agrege pygame
                salir = True
                pygame.mixer.music.stop()
                return "Salir"
        
        screen.blit(fondo, (0, 0))
        opc = menu.actualizar()
        if opc == 0 or opc == 2:
            salir=True
        menu.imprimir(screen)

        pygame.display.flip()
        pygame.time.delay(10)
    if opc == 0:
        return "Jugar"
    else:
        return "Salir"
    
    
if __name__ == "__main__":
    main()




















        
