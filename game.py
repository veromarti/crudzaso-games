perder = False

def run(level):
    if level == 1:
        file = 'map1.txt'
    elif level == 2:
        file = 'map2.txt'
    return file

def open_file(file_txt):
    with open(file_txt,'r+') as map_file:
        structure = map_file.readlines()
    return structure

def show_map(map):
    new_map = []
    new_path = []
    for i in map:
        print(i[0:-1])
        for j in i:
            new_path.append(j)
        new_map.append(new_path)
        new_path = []  
    return new_map

def convert(map_list):
    organized_path = ''
    organized_map = []
    for line in range(len(map_list)):
        organized_map.append(organized_path.join(map_list[line]))  
    return organized_map

def find_user(map):
    cont_x = 0
    cont_y = 0
    for line in map:       
        for pos in line:
            if pos == 'U':
                return(cont_x, cont_y)
            cont_y += 1
        cont_x += 1 
        cont_y = 0

def find_path(map,dir):
    pos_x,pos_y = find_user(map)
    print(pos_x, pos_y)
    
    match(dir):
        case 'W':
            if map[pos_x-1][(pos_y)] == "|" or map[pos_x-1][(pos_y)] == "+":
                return True , [pos_x,pos_y]
            elif map[pos_x-1][(pos_y)] == " " or map[pos_x-1][(pos_y)] == "_":
                new_pos = [-1,0]
                return False, new_pos
            pass
        case 'A':
            if map[pos_x][(pos_y-1)] == "|" or map[pos_x][(pos_y-1)] == "+":
                return True, [pos_x,pos_y]
            elif map[pos_x][(pos_y-1)] == " " or map[pos_x][(pos_y-1)] == "_":
                new_pos = [0,-1]
                return False, new_pos
            pass
        case 'S':
            if map[pos_x + 1][(pos_y)] == "|" or map[pos_x+1][(pos_y)] == "+":
                return True, [pos_x,pos_y]
            elif map[pos_x+1][(pos_y)] == " " or map[pos_x+1][(pos_y)] == "_":
                new_pos = [1,0]
                return False, new_pos
            pass
        case 'D':
            if map[pos_x][(pos_y+1)] == "|" or map[pos_x][(pos_y+1)] == "+":
                return True, [pos_x,pos_y]
            elif map[pos_x][(pos_y+1)] == " " or map[pos_x][(pos_y+1)] == "_":
                new_pos = [0,1]
                return False, new_pos
            pass
            
def move_user(obstacle,map,old_pos_x,old_pos_y,new_pos):
    new_map = map
    if not obstacle:
        new_map[old_pos_x][old_pos_y]=" "
        new_map[old_pos_x + new_pos[0]][old_pos_y + new_pos[1]]='U'
        return new_map
    if obstacle:
        new_map[old_pos_x][old_pos_y]="U"
        return new_map
    pass

option = int(input("Enter level: "))
file = run(option)
file2map = open_file(file)

map_list = show_map(file2map)
while not perder:
    
    x , y = find_user(map_list)
    dir = input("Enter W/A/S/D: ") 
    path_blocked, new_pos = find_path(map_list,dir)
    new_map_list = move_user(path_blocked,map_list,x,y,new_pos)
    map = convert(new_map_list)
    new_map_list = show_map(map)
    
        