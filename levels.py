obstacle_map = [[[] for i in range(4)] for j in range(4)]
coin_map = [[[] for i in range(4)] for j in range(4)] 
player_map = [[[] for i in range(4)] for j in range(4)]
brig_map = [[[] for i in range(4)] for j in range(4)]
scene_map = [[[] for i in range(4)] for j in range(4)]

ENDC = '\x1b[0m'

brw = '\x1b[0;33m' + '#' + ENDC 
grn = '\x1b[0;32m' + '#' + ENDC
blu = '\x1b[0;34m' + '#' + ENDC
red = '\x1b[0;31m' + '#' + ENDC

cloud = [ [' ',' ',' ','_','_',' ',' ',' ','_',' ',' ',' '], 
          [' ','_','(',' ',' ',')','_','(',' ',')','_',' '],  
          ['(',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',')'],
          [' ',' ','(','_',')',' ','(','_','_',')',' ',' ']  
        ]

# level 1-1
obstacle_map[0][0].extend([[19,0,2,102,brw,'obs'],[16,51,3,8,grn,'obs']]) 
obstacle_map[0][0].extend([[19,31,2,4,' ','dit'],[19,83,2,4,' ','dit']])
coin_map[0][0].extend([[15,53,'c'],[15,55,'c'],[18,63,'c'],[18,65,'c'],[18,67,'c'],[18,69,'c']])
player_map[0][0].extend([[16,1,1,3,3]])
scene_map[0][0].extend([[2,2,4,12,cloud],[4,15,4,12,cloud],[4,55,4,12,cloud],[3,75,4,12,cloud]])

#level 1-2
obstacle_map[0][1].extend([[19,0,2,101,brw,'obs'],[14,19,2,4,grn,'obs'],[14,28,2,4,grn,'obs']])
obstacle_map[0][1].extend([[17,32,2,3,brw,'obs'],[19,19,2,13,' ','dit']])
coin_map[0][1].extend([[12,20,'c'],[12,30,'c'],[10,25,'c'],[15,10,'m']])
player_map[0][1].extend([[16,1,1,3,3],[17,97,2,2,3]])
scene_map[0][1].extend([[2,2,4,12,cloud],[4,15,4,12,cloud],[4,55,4,12,cloud],[3,75,4,12,cloud]])

#level 1-3
obstacle_map[0][2].extend([[19,0,2,40,brw,'obs'],[15,83,2,18,brw,'obs'],[9,52,1,3,grn,'obs']])
obstacle_map[0][2].extend([[15,25,4,2,brw,'obs'],[15,38,4,2,brw,'obs'],[13,45,1,3,grn,'obs']])
obstacle_map[0][2].extend([[8,59,1,7,grn,'obs'],[11,72,1,3,grn,'obs'],[14,83,1,1,brw,'obs']])
coin_map[0][2].extend([[16,32,'c'],[12,46,'c'],[8,53,'c'],[4,62,'c'],[9,73,'c']])
player_map[0][2].extend([[16,1,1,3,3],[17,32,2,2,3],[13,92,2,2,3]])
scene_map[0][2].extend([[2,2,4,12,cloud],[4,15,4,12,cloud],[3,75,4,12,cloud]])

#level 2-1
obstacle_map[1][0].extend([[19,0,2,27,brw,'obs'],[19,83,2,19,brw,'obs'],[16,25,3,2,brw,'obs'],[18,83,1,2,brw,'obs']])
obstacle_map[1][0].extend([[13,49,1,12,grn,'obs'],[16,44,2,4,grn,'obs'],[16,64,2,4,grn,'obs'],[7,16,1,12,grn,'obs']])
obstacle_map[1][0].extend([[8,32,1,4,grn,'obs'],[9,40,1,4,grn,'obs'],[12,49,1,2,grn,'obs'],[12,59,1,2,grn,'obs']])
coin_map[1][0].extend([[4,17,'c'],[4,19,'c'],[4,21,'c'],[4,23,'c'],[4,25,'c'],[6,34,'c'],[8,42,'c'],[15,65,'l']])
player_map[1][0].extend([[16,1,1,3,3],[17,22,2,2,3],[11,56,2,2,3]])
brig_map[1][0].extend([[16,28,1,4,'h',28,43,blu],[16,69,1,4,'h',69,81,blu]])
player_map[0][2].extend([[16,1,1,3,3],[17,32,2,2,3],[13,92,2,2,3]])
scene_map[1][0].extend([[4,55,4,12,cloud],[3,75,4,12,cloud]])


#level 2-2
obstacle_map[1][1].extend([[1,5,2,96,brw,'obs'],[9,0,2,65,brw,'obs'],[7,24,2,4,brw,'obs'],[9,71,8,2,brw,'obs']])
obstacle_map[1][1].extend([[18,5,2,96,brw,'obs'],[17,71,1,30,brw,'obs'],[24,76,1,24,brw,'obs'],[16,25,2,3,brw,'obs']])
obstacle_map[1][1].extend([[2,99,15,3,brw,'obs'],[9,69,1,2,brw,'obs']])
player_map[1][1].extend([[1,1,1,3,3],[7,41,3,2,3],[15,88,2,2,3],[16,66,2,2,3]])
brig_map[1][1].extend([[24,1,1,5,'h',1,75,blu],[16,75,1,4,'v',8,16,blu]])
coin_map[1][1].extend([[14,86,'m']])

#level 2-3
obstacle_map[1][2].extend([[19,0,2,101,red,'obs'],[14,96,5,1,red,'obs'],[13,96,1,5,red,'obs']])
obstacle_map[1][2].extend([[13,27,1,2,red,'obs'],[11,32,1,2,red,'obs'],[8,38,1,3,red,'obs']])
obstacle_map[1][2].extend([[9,47,1,3,red,'obs'],[13,50,1,10,red,'obs']])
coin_map[1][2].extend([[7,39,'l'],[8,47,'m']])
player_map[1][2].extend([[16,1,1,3,3]])
scene_map[1][2].extend([[2,2,4,12,cloud],[4,15,4,12,cloud],[4,55,4,12,cloud],[3,75,4,12,cloud]])
