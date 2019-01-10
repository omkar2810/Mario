import time
from board import *

class objects(object):
    """Parent class for all objects in the game"""

    def __init__(self):
        pass

    def place(self, board):
        """Place a particular object on the matrix"""

        if self.y_cor + self.y_siz > board.end:
            return
             
        for i in range(self.x_cor,self.x_cor +self.x_siz):
            for j in range(self.y_cor,self.y_cor+self.y_siz):
                board.mat[i][j]=self.mat[i-self.x_cor][j-self.y_cor]
        return    

    def move(self,delta_x,delta_y,board): 
        """Move objects by specifies x and y movements"""

        if self.x_cor + delta_x <= 0:
            return True 
        
        if self.x_cor + self.x_siz + delta_x  >= board.x_siz:
            if self.type == 1:
                return False    
        
        if self.y_cor + delta_y > board.start and self.y_cor + self.y_siz + delta_y <= board.end:
            self.remove(board)                         
            self.y_cor = self.y_cor + delta_y
            self.x_cor = self.x_cor + delta_x

            for i in range(self.x_cor,self.x_cor + self.x_siz):
                for j in range(self.y_cor, self.y_cor + self.y_siz):
                    if board.obstacle_mat[i][j] == 'X':
                        self.y_cor = self.y_cor - delta_y
                        self.x_cor = self.x_cor - delta_x
                        break            

        return True

    def gravity(self,board):
        """Gravity function that works on all air_borne objects"""

        for i in range(self.y_cor,self.y_cor + self.y_siz):
            if board.obstacle_mat[self.x_cor + self.x_siz][i] == 'X':
                self.in_air = False
                return True
        self.in_air = True        
        
        return self.move(1,0,board)        

    def remove(self,board):
       
        for i in range(self.x_cor,self.x_cor +self.x_siz):
            for j in range(self.y_cor,self.y_cor+self.y_siz):
                board.mat[i][j] = " "     
                board.obstacle_mat[i][j] = " "

class bridge(objects):
    """Moving Bridge"""

    brig_arr = []
    def __init__(self,list):
        self.x_cor = list[0]
        self.y_cor = list[1]
        self.x_siz = list[2]
        self.y_siz = list[3]
        self.choice = list[4]
        self.lim_1 = list[5]
        self.lim_2 = list[6]
        self.char = list[7]
        self.mat = [[self.char for i in range(0,self.y_siz)] for j in range(0,self.x_siz)]
        self.mov_dir = -1
    
    def move_brig(board):
        
        for i in bridge.brig_arr :
            i.remove(board)           
            if i.choice == 'h':         #horizontal bridge
                if i.y_cor <= i.lim_1:
                    i.mov_dir = -i.mov_dir
                elif i.y_cor + i.y_siz - 1 >= i.lim_2:
                    i.mov_dir = -i.mov_dir                        
                i.move(0,i.mov_dir,board)

            else:                       #vertical bridge
                if i.x_cor <= i.lim_1:
                    i.mov_dir = -i.mov_dir
                elif i.x_cor + i.x_siz -1 >= i.lim_2:
                    i.mov_dir = -i.mov_dir
                i.move(i.mov_dir,0,board)
            board.create_obstacle([i.x_cor,i.y_cor,i.x_siz,i.y_siz,i.char,'obs']) 
            i.place(board)            
        return         

class bullet(objects):        
    """Bullets shot by Boss Enemies"""

    bullet_arr = []       #stores all the bullets   

    def __init__(self,x_cor,y_cor,direc):
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.x_siz = 1
        self.y_siz = 1
        if direc > 0:
            self.mat = [['>']]
        else:
            self.mat = [['<']] 
        self.mov_dir = direc

    def move_bullet(board):
        for bul in bullet.bullet_arr:
            bul.remove(board)
            bul.move(0,bul.mov_dir,board)
            bul.place(board)
        return    