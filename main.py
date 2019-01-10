import time
import sys
import os
import time
import termios
import tty

from input import *
from board import board
from player import *
from lvl_gen import *
from objects import *

def main():

    new_board = board(27,102)
    plyr = player([20,2,1,3,3]) # (y,x) "mario"
    level = 0
    stage = 0

    while plyr.life >0:

        player.level = (int)(level/3)
        player.stage = stage%3
        
        new_board.clear()
        player.enemy_arr.clear()
        bridge.brig_arr.clear()
        bullet.bullet_arr.clear()
        player.counter = 0
        
        generate_level(plyr, new_board, int(level/3), stage%3)
        
        if level == 5 and stage == 5:
            boss1 = player([16,97,4,3,3])
            player.enemy_arr.append(boss1)
        
        running = True    
        
        while running:

            time.sleep(0.01)
            os.system('tput reset')
            plyr.place(new_board)
           
            if level == 5 and stage == 5:
                if boss1.life == 0:
                    print("Congrats!!You win. Your score is-",plyr.score)
                    plyr.life = 0
                    break                
                boss1.boss_level(plyr,new_board)
                bullet.move_bullet(new_board) 
         
            player.move_enemies(plyr,new_board)
            bridge.move_brig(new_board)        
            running = plyr.check_collision(new_board)           
            os.system('tput reset')
            
            new_board.update_board()
            print("SCORE-",plyr.score,colors['Red'] + " ♥ " + ENDC,plyr.life," 💣", plyr.pow,)   
            if level==5 and stage ==5 :
                print("Boss Level Boss life-",boss1.life)
            else:    
                print("Level- ",player.level," Stage- ",player.stage)                 
            
            key_pressed = get_input()      
            running = running & plyr.gravity(new_board)
            for i in player.enemy_arr:
                if i.type == 3:
                    i.gravity(new_board)
                 
            if key_pressed == 'd':            
                plyr.move(0,1,new_board)
                time.sleep(0.01)

            elif key_pressed == 'a':
                plyr.move(0,-1,new_board)
                time.sleep(0.01)

            elif key_pressed == 'w' and plyr.in_air == False:
                jump_no = 4
                plyr.jump(new_board,jump_no)

            elif key_pressed == 'q':
                plyr.life = 0   
                break
            
            elif key_pressed == 'e':
                plyr.place_missile(new_board)
        
            plyr.check_brig(new_board)
            if plyr.y_cor == 97 and plyr.in_air == False and ( level != 5 and stage != 5):
                break                                                                   
            time.sleep(0.01)

        if running == False:
            plyr.life = plyr.life - 1
        else:
            level = level + 1
            stage = stage + 1 
            
    if level < 5 :
        print(colors['Red'] + "Game Over!!!" + ENDC)
        print(colors['Red'] + "Final Score:", plyr.score)                           
        
if __name__ == '__main__':
    main()              