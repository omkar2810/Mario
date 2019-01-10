""" nxm board with x_siz as n and y_siz as m, start and end mark the starting and ending indices of the current scene 
"""
from input import *

class board(object):

    def create_mat(self):

        for i in range (self.x_siz):
            for j in range(self.y_siz):
                if i==self.x_siz-1 or i==0:
                    self.mat[i][j]='_'
                elif j==self.y_siz -1 or j==0:
                    self.mat[i][j]='|'
                else:        
                    self.mat[i][j]=' '

        for i in range((self.x_siz)-1,self.x_siz):
            for j in range(self.y_siz):
                self.mat[i][j]='-'
                self.obstacle_mat[i][j] = ' '        
        return

    def __init__(self,n,m):
     
        self.mat = [[0 for i in range(m)]for j in range(n)]
        self.obstacle_mat = [[0 for i in range(m)]for j in range(n)]
        self.back_mat = [[' ' for i in range(m)]for j in range(n)]        
        self.y_siz = m
        self.x_siz = n
        self.start = 0
        self.end = m-1

    def update_board(self):
        """Print the current scene"""

        for i in range(self.x_siz):
            for j in range(self.y_siz):
                if self.mat[i][j] != ' ':
                    print(self.mat[i][j],end='')
                else:
                    print(self.back_mat[i][j],end='')    
            print('\n',end='')   
            
    def create_obstacle(self,list):
        """Place obstacle at a given position"""

        x_cor = list[0]
        y_cor = list[1]
        x_siz = list[2]
        y_siz = list[3]
        char  = list[4]
        choice = list[5]
        for i in range(x_cor,x_cor+x_siz):
            for j in range(y_cor,y_cor+y_siz):
                self.mat[i][j] = char
                if choice == 'obs':
                    self.obstacle_mat[i][j] = 'X'
                elif choice == 'dit':
                    self.obstacle_mat[i][j] = ' '
    
    def clear(self):
        
        for i in range(0,self.x_siz):
            for j in range(0,self.y_siz):
                self.mat[i][j] = ' '
                self.obstacle_mat[i][j] = ' ' 
                self.back_mat[i][j] = ' '       

    def place_coin(self,list):
        """Place a coin/extra life/Mine"""   
        x_cor = list[0]
        y_cor = list[1]
        choice = list[2]
        
        if choice == 'c':
            self.mat[x_cor][y_cor] = '\x1b[1;33m'+'Ⓒ'+'\x1b[0m'
            self.obstacle_mat[x_cor][y_cor] = 'O'              
        elif choice == 'm':     
            self.mat[x_cor][y_cor] = colors['Cyan'] + '💣' + ENDC
            self.obstacle_mat[x_cor][y_cor] = 'M'                                        
        elif choice == 'l':
            self.mat[x_cor][y_cor] = colors['Red'] + '♥' + ENDC
            self.obstacle_mat[x_cor][y_cor] = 'l'               

    def place_scene(self,list):
        x_cor = list[0]
        y_cor = list[1]
        x_siz = list[2]
        y_siz = list[3]
        mat = list[4]

        for i in range(x_cor,x_cor + x_siz):
            for j in range(y_cor, y_cor + y_siz):
                self.back_mat[i][j] = mat[i-x_cor][j-y_cor]

                  