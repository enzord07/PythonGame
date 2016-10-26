
import pygame
 
import constants
import levels
from Edited_Sprite_Group import Edited_Sprite_Group
 
from player import Player
 
def registrar_puntaje(puntaje):
    file = open("puntajes/puntajes.txt")
    puntajes = []
    for line in file:
        puntajes.append(int(line))
    file.close()
    if puntaje > puntajes[9]:
        puntajes[9] = puntaje
        cursor = 9
        listo = False
        while cursor !=0 and listo != True:
            if puntajes[cursor] > puntajes[cursor-1]:
                aux=puntajes[cursor-1]
                puntajes[cursor-1]=puntajes[cursor]
                puntajes[cursor]=aux
            else:
                listo = True
            cursor-=1
        file = open("puntajes/puntajes.txt", "w")
        cursor = 0
        for p in puntajes:
            file.write(str(p))
            if cursor!=9:
                file.write(str("\n"))
            cursor += 1
        file.close()
        
        

def main(s):
 
    pygame.mixer.music.load("game/music.mp3")
    pygame.mixer.music.play(2)    
    # Set the height and width of the screen
    screen = s
 
    # Create the player
    player = Player()
 
    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01(player))
 
    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = Edited_Sprite_Group()
    player.level = current_level
 
    player.rect.x = 340
    player.rect.y = constants.SCREEN_HEIGHT-70 - player.rect.height
    active_sprite_list.add(player)
 
    #Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    #usado para detectar si fue presionado la flecha dos veces seguidas
    contl=0
    contr=0
    
    # Usado para poner un delay para volver al menu
    tiemposalir=60*7
    
    # Flag si termino el juego
    terminado = False
    
    # Puntaje
    puntaje = 0
    imgpuntaje = None
    fuente = pygame.font.Font(None, 80)
    
    # -------- Main Program Loop -----------
    while not done:
        contl+=1
        contr+=1
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                return "Salir"
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if contl<15:
                        player.run_left()
                    else:
                        player.go_left()
                    contl=0
                if event.key == pygame.K_RIGHT:
                    if contr<15:
                        player.run_right()
                    else:
                        player.go_right()
                    contr=0
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_DOWN:
                    player.crouch()
                if event.key == pygame.K_z:
                    player.attack()
                if event.key == pygame.K_x:
                    player.attackshuriken()
                if event.key == pygame.K_h:
                    player.hurt()
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
                if event.key == pygame.K_DOWN:
                    player.go_up()
 
        # Update the player.
        active_sprite_list.update()
 
        # Update items in the level
        current_level.update()
 
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)
  
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)
 
        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift*-1
        if current_position > current_level.level_limit*-1:
            if current_level_no < len(level_list)-1:
                player.rect.x = 120
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
            else:
                if terminado == False:
                    terminado = True
                    puntaje = player.shurikens * 20 + player.health * 30 + current_level.enemies_death * 40 + current_level.gui.clock.segundos_totales * 5
                    imgpuntaje = fuente.render("Puntaje: " + str(puntaje), True, (0, 0 ,0))
                    registrar_puntaje(puntaje)
        # Iniciar contador para volver al menu principal si muere.
        if player.health == 0:
            tiemposalir -=1
            if tiemposalir==0:
                return "Menu"
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        player.shuriken_list.draw(screen)
        if terminado:
            screen.blit(imgpuntaje, (230,80))
            tiemposalir -=1
            if tiemposalir == 0:
                return "Puntajes"
        
 
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
 
if __name__ == "__main__":
    main()