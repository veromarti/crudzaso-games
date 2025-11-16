import os

perder = False
victory = False

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def run(level):
    if level == 1:
        file = 'map1.txt'
    elif level == 2:
        file = 'map2.txt'
    elif level == 4:
        file = 'map4.txt'
    return file

def open_file(file_txt):
    with open(file_txt,'r+') as map_file:
        structure = map_file.readlines()
    return structure

def show_map(map):
    new_map = []
    new_path = []
    for row in map:
        print(row[0:-1])
        for pos in row:
            new_path.append(pos)
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
    cont_row = 0
    cont_col = 0
    for line in map:       
        for pos in line:
            if pos == '🐤':
                return(cont_row, cont_col)
            cont_col += 1
        cont_row += 1 
        cont_col = 0

def find_path(map,dir):
    pos_row,pos_col = find_user(map)
    
    match(dir):
        case 'W':
            if map[pos_row - 1][(pos_col)] == "🔲" or map[pos_row - 1][(pos_col)] == "+":
                return True , [pos_row,pos_col]
            elif map[pos_row - 1][(pos_col)] == "⬛" or map[pos_row - 1][(pos_col)] == "_" or map[pos_row - 1][(pos_col)] == "🏆":
                new_pos = [-1,0]
                return False, new_pos
            pass
        case 'A':
            if map[pos_row][(pos_col - 1)] == "🔲" or map[pos_row][(pos_col - 1)] == "+":
                return True, [pos_row,pos_col]
            elif map[pos_row][(pos_col - 1)] == "⬛" or map[pos_row][(pos_col - 1)] == "_" or map[pos_row][(pos_col - 1)] == "🏆":
                new_pos = [0,-1]
                return False, new_pos
            pass
        case 'S':
            if map[pos_row + 1][(pos_col)] == "🔲" or map[pos_row + 1][(pos_col)] == "+":
                return True, [pos_row,pos_col]
            elif map[pos_row + 1][(pos_col)] == "⬛" or map[pos_row + 1][(pos_col)] == "_" or map[pos_row + 1][(pos_col)] == "🏆":
                new_pos = [1,0]
                return False, new_pos
            pass
        case 'D':
            if map[pos_row][(pos_col + 1)] == "🔲" or map[pos_row][(pos_col + 1)] == "+":
                return True, [pos_row,pos_col]
            elif map[pos_row][(pos_col + 1)] == "⬛" or map[pos_row][(pos_col + 1)] == "_"or map[pos_row][(pos_col + 1)] == "🏆":
                new_pos = [0,1]
                return False, new_pos
            pass
        case _:
            return True, [pos_row,pos_col]
            
            
def move_user(obstacle,map,old_pos_row,old_pos_col,new_pos):
    new_map = map
    if not obstacle:
        if map[old_pos_row + new_pos[0]][old_pos_col + new_pos[1]] == '🏆':
            new_map[old_pos_row][old_pos_col] = "⬛"
            new_map[old_pos_row + new_pos[0]][old_pos_col + new_pos[1]] = '🐤'
            clear()
            victory = True
            #llamar archivo de finalizacion
        else:
            new_map[old_pos_row][old_pos_col] = "⬛"
            new_map[old_pos_row + new_pos[0]][old_pos_col + new_pos[1]] = '🐤'
            victory = False
        return new_map, victory
    if obstacle:
        new_map[old_pos_row][old_pos_col]="🐤"
        victory = False
        return new_map, victory
    pass

option = int(input("Enter level: "))
file = run(option)
file2map = open_file(file)

map_list = show_map(file2map)
while not perder:
    
    while not victory:
        row , col = find_user(map_list)
        dir = input("Enter W/A/S/D: ") 
        path_blocked, new_pos = find_path(map_list,dir)
        new_map_list, victory = move_user(path_blocked,map_list,row,col,new_pos)
        if not victory:
            map = convert(new_map_list)
            new_map_list = show_map(map)
        else:
            clear()
            print('GANASTE')
            #llamar archivo de finalizacion
            perder = True
        break
    
        #baba