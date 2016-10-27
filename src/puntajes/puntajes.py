
import pygame
 
def main(screen):
 
    done = False
    clock = pygame.time.Clock()
    file = open("puntajes/puntajes.txt")
    fuente = pygame.font.Font(None, 40)
    puntajes = []
    cont=0
    for line in file:
        cont +=1
        line = str(cont) + ".- " + line.strip()
        puntajes.append(fuente.render(line, True, (0, 0 ,0)))
    pos = [360,40]
    cont = 0
    screen.blit(pygame.image.load("game/nivel1.jpg").convert(), (-550, 0))
    for p in puntajes:
        cont +=1
        screen.blit(p,[pos[0],pos[1]+40*cont])
    pygame.display.flip()
    file.close()
    
    while not done:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                return "Salir"
 
            if event.type == pygame.KEYDOWN:
                return "Menu"
 
        
 
        clock.tick(60)
        
    pygame.quit()
 
if __name__ == "__main__":
    main()