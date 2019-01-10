from objects import *
from board import *
from input import *
from levels import * 
import time
import sys
import os

red = '\x1b[0;31m'
blu = colors['Light Blue']
ENDC = '\x1b[0m' 
mario = [[colors['Red'] + '(','M',')'+ENDC],[blu +'\\','|','/'+ENDC],[blu + '/','.','\\' + ENDC]]
enemy = [[colors['Purple']+'-','N','-'+ENDC],[colors['Purple']+'/','|','\\'+ENDC]]
boss = [['<','B','>'],['|','_','|'],['m',' ','m']]
smart = [[colors['Purple']+'-','S','-'+ENDC],[colors['Purple']+'/','|','\\'+ENDC]]  

class player(objects):
    """Class for players and enemies"""
    enemy_arr = []
    counter = 0
    level = 0
    stage = 0

    def __init__(self,list):
        x_cor = list[0]
        y_cor = list[1]
        choice = list[2]
        x_siz = list[3]
        y_siz = list[4]
        if choice == 1:
            self.mat = mario
        elif choice == 4:
            self.mat = boss    
        elif choice == 2:
            self.mat = enemy
        else: 
            self.mat = smart            
        self.x_siz = x_siz
        self.y_siz = y_siz
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.jump_siz = 2 
        self.in_air = False
        self.type = choice                 # 1-player , 2 normal enemy , 3 smart enemy, 4 Boss Enemy
        self.score = 0
        self.move_dir = -1
        self.pow = 0
        if choice == 1:
            self.life = 3
        elif choice == 4:
            self.life = 5
        else:
            self.life = 1        

    def move_enemies(player,board):
        """ Moves the enemies according to their type"""

        for i in player.enemy_arr: 
            if i.type == 2:
                init_y = i.y_cor
                i.move(0,i.move_dir,board)
                if i.y_cor == init_y:          #normal enemy reverses direction if the path is blocked
                    i.move_dir = -i.move_dir

            elif i.type == 3 or i.type == 4:
                flag=0
                init_y = i.y_cor

                if player.y_cor > i.y_cor + i.y_siz : #smart enemy changes its direction according to the player position 
                    i.move(0,1,board)
                    flag = 1
                elif player.y_cor < i.y_cor :
                    i.move(0,-1,board)
                    flag = 1
                if i.y_cor == init_y and flag == 1 and i.type == 3 :
                    i.jump(board,4)    
            i.place(board)
            
    def check_collision(self,board):
        """Single function for detection of collision between players and various objects/enemies"""    

        front_leg = self.y_cor + self.y_siz - 1 
        kill_enemy = []        # stores all the enemies which are to be killed

        #Check for bullet
        for b in bullet.bullet_arr:
            if b.x_cor >= self.x_cor and b.x_cor < self.x_cor + self.x_siz:
                if b.y_cor >= self.y_cor and b.y_cor < self.y_cor + self.y_siz:
                    self.remove(board)
                    return False

        #Check if enemy kills the player    
        for i in player.enemy_arr:
            if front_leg >= i.y_cor - 1 and front_leg < i.y_cor + i.y_siz :
                if self.x_cor + self.x_siz > i.x_cor and self.x_cor <= i.x_cor + i.x_siz :
                    self.remove(board)
                    return False
                    
            elif self.y_cor <= i.y_cor + i.y_siz and self.y_cor >= i.y_cor :
                if self.x_cor + self.x_siz > i.x_cor and self.x_cor <= i.x_cor + i.x_siz:
                    self.remove(board)
                    return False

        #Check if player kills the enemy    
            if front_leg >= i.y_cor and front_leg < i.y_cor + i.y_siz:
                if self.x_cor + self.x_siz == i.x_cor and self.in_air == True: 
                    i.life = i.life - 1 
                    if i.life == 0:
                        kill_enemy.append(i)
                        continue
                    i.remove(board)    
                    i.y_cor = i.y_cor + 15                    
           
            elif self.y_cor >= i.y_cor and self.y_cor < i.y_cor + i.y_siz:
                if self.x_cor + self.x_siz == i.x_cor and self.in_air == True :
                    i.life = i.life - 1
                    if i.life <= 0:
                        kill_enemy.append(i)
                        continue
                    i.remove(board)    
                    i.y_cor = i.y_cor + 15

            #Checks for mine kills
            for j in range(i.y_cor,i.y_cor+i.y_siz):
            
                if board.obstacle_mat[i.x_cor+i.x_siz][j] == 'm':
                    board.mat[i.x_cor+i.x_siz][j] = ' '
                    board.obstacle_mat[i.x_cor+i.x_siz][j] = ' '
                    i.life = i.life - 1
                    if i.life <= 0:
                        kill_enemy.append(i)
                        
        #Kill all the enemies which are in the list
        for enmy in kill_enemy:
            enmy.remove(board)
            player.enemy_arr.remove(enmy) 
            self.score = self.score + 5   

        for i in range(max(self.x_cor-1,0),self.x_cor + self.x_siz+1):    #check for coin and power ups
            
            for j in range(self.y_cor,self.y_cor + self.y_siz):
                if board.obstacle_mat[i][j] == 'O':
                    board.obstacle_mat[i][j] = ' '
                    board.mat[i][j] = ' '
                    self.score = self.score + 1
                    coin_map[player.level][player.stage].remove([i,j,'c'])
                
                elif board.obstacle_mat[i][j] == 'M':
                    board.obstacle_mat[i][j] = ' '
                    board.mat[i][j] = ' '
                    self.pow = self.pow +  1
                    coin_map[player.level][player.stage].remove([i,j,'m'])                    
               
                elif board.obstacle_mat[i][j] == 'l':
                    board.obstacle_mat[i][j] = ' '
                    board.mat[i][j] = ' '
                    self.life = self.life + 1        
                    coin_map[player.level][player.stage].remove([i,j,'l'])
                    
        return True                    
 
    def jump(self,new_board,jump_no):
        """Jump function for various players/enemies"""

        for i in range(0, jump_no * self.jump_siz ):
            self.move(-1, 0,new_board)
            os.system('tput reset') 
            self.place(new_board)               
            new_board.update_board()
            self.in_air = True
            time.sleep(0.01)  
        return       

    def check_brig(self,board):
        """Checks if the player is on a moving bridge"""

        for i in bridge.brig_arr:
            start = i.y_cor
            end = i.y_cor + i.y_siz -1
            pl_end = self.y_cor + self.y_siz -1
            if (self.y_cor >= start and self.y_cor <=end) or (pl_end >= start and pl_end <=end ):
                if i.x_cor == self.x_cor + self.x_siz:
                    if i.choice == 'h':
                        self.move(0,i.mov_dir,board)     
                    else:
                        if i.x_cor == i.lim_1 or i.x_cor + i.x_siz -1 == i.lim_2: 
                            self.move(-1*i.mov_dir,0,board)
                        else:
                            self.move(i.mov_dir,0,board)                            
        return            

    def place_missile(self,board):  
        """Place a mine at a given location"""

        if self.in_air == False and self.pow > 0:
            board.mat[self.x_cor+self.x_siz][self.y_cor+1] = colors['Red'] + '^' + ENDC
            board.obstacle_mat[self.x_cor+self.x_siz][self.y_cor+1] = 'm' 
            self.pow = self.pow - 1   
        return         

    def boss_level(self,plyr,board):
        """Function for the final boss level"""

        if player.counter == 0:
            player.counter = player.counter + 1     
            enmy = player([17,self.y_cor-20,2,2,3])
            player.enemy_arr.append(enmy)
            return

        if player.counter == 1:
            if len(player.enemy_arr) == 1:
                player.counter = player.counter + 1    
                if plyr.y_cor > 50:
                    enmy = player([17,plyr.y_cor - 20,3,2,3])
                    player.enemy_arr.append(enmy)
                else:
                    enmy = player([17,plyr.y_cor + 20,3,2,3])
                    player.enemy_arr.append(enmy)
            return

        if player.counter == 2:
            if len(player.enemy_arr) == 1:
                player.counter = player.counter + 1
                board.create_obstacle([14,96,5,1,'#','dit'])      
            return

        if player.counter > 2:
            if player.counter % 30 == 0 :
                if self.y_cor + self.y_siz < plyr.y_cor:
                    bul =  bullet(self.x_cor +1 ,self.y_cor + self.y_siz,2)
                    bullet.bullet_arr.append(bul)
                else:    
                    bul =  bullet(self.x_cor +1 ,self.y_cor-1,-2)
                    bullet.bullet_arr.append(bul)

            if player.counter == 20:
                board.create_obstacle([19,45,2,3,' ','dit'])

            if player.counter == 60:
                board.create_obstacle([19,81,2,3,' ','dit'])    

            if player.counter == 85:
                board.create_obstacle([19,15,2,3,' ','dit'])

            player.counter = player.counter + 1        
            return