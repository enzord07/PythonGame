import pygame
import game
import menu
import puntajes

def main():
    pygame.init()
    size = [game.constants.SCREEN_WIDTH, game.constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)   
    pygame.display.set_caption("NinjaHero")
    opc = "Menu"
    while opc != "Salir":
        if opc=="Menu":
            opc = menu.menu.main(screen)
        elif opc=="Jugar":
            opc = game.NinjaHero.main(screen)
        elif opc=="Puntajes":
            opc = puntajes.puntajes.main(screen)
    pygame.quit()
main()