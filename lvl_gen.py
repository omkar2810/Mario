from player import *
from objects import *
from board import *
from levels import *

def generate_level(plyr,board,level,stage):
    """generates the frame for a given level and stage,each level consists of 3 stages  """
    
    board.create_mat()
    player.enemy_arr = []
    bridge.brig_arr = []
  
    for i in obstacle_map[level][stage]:
        board.create_obstacle(i)
    
    for i in coin_map[level][stage]:
        board.place_coin(i)     
    
    for i in player_map[level][stage]:
        if i[2] == 1:
            plyr.x_cor = i[0]
            plyr.y_cor = i[1]
        else:
            enemy = player(i) 
            player.enemy_arr.append(enemy)   
            del(enemy)
    
    for i in brig_map[level][stage]:
        brig = bridge(i)
        bridge.brig_arr.append(brig)

    for i in scene_map[level][stage]:
        board.place_scene(i)

