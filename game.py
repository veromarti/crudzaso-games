import os
import sys
import time
import time_counter

victory = False
game_over = False

if sys.platform == "win32":
    import msvcrt

    def kbhit():
        return msvcrt.kbhit()

    def getch():
        return msvcrt.getch().decode("utf-8")
    
    def set_curses_term():
        pass

    def set_normal_term():
        pass

else:
    import termios, select
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    def set_normal_term():
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    def set_curses_term():
        new_settings = termios.tcgetattr(fd)
        new_settings[3] = new_settings[3] & ~(termios.ICANON | termios.ECHO)
        termios.tcsetattr(fd, termios.TCSADRAIN, new_settings)

    def kbhit():
        dr, _, _ = select.select([sys.stdin], [], [], 0)
        return dr != []

    def getch():
        return sys.stdin.read(1)

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
    elif level == 3:
        file = 'map3.txt'
    return file

def open_file(file_txt, character):
    with open(file_txt,'r+', encoding="utf-8") as map_file:
        structure = map_file.readlines()

    row = list(structure[1])
    row[1] = character
    structure[1] = "".join(row)

    with open(file_txt,'w', encoding="utf-8") as map_file:
        map_file.writelines(structure)

    with open(file_txt,'r+', encoding="utf-8") as map_file:
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

def find_user(map,character):
    cont_row = 0
    cont_col = 0
    for line in map:       
        for pos in line:
            if pos == character:
                return(cont_row, cont_col)
            cont_col += 1
        cont_row += 1 
        cont_col = 0

def find_path(map,dir,character):
    pos_row,pos_col = find_user(map,character)
    match(dir.upper()):
        case 'W':
            if map[pos_row - 1][(pos_col)] == "🔲":
                return True , [pos_row,pos_col]
            elif map[pos_row - 1][(pos_col)] == "⬛" or map[pos_row - 1][(pos_col)] == "🏆":
                new_pos = [-1,0]
                return False, new_pos
            pass
        case 'A':
            if map[pos_row][(pos_col - 1)] == "🔲":
                return True, [pos_row,pos_col]
            elif map[pos_row][(pos_col - 1)] == "⬛" or map[pos_row][(pos_col - 1)] == "🏆":
                new_pos = [0,-1]
                return False, new_pos
            pass
        case 'S':
            if map[pos_row + 1][(pos_col)] == "🔲":
                return True, [pos_row,pos_col]
            elif map[pos_row + 1][(pos_col)] == "⬛" or map[pos_row + 1][(pos_col)] == "🏆":
                new_pos = [1,0]
                return False, new_pos
            pass
        case 'D':
            if map[pos_row][(pos_col + 1)] == "🔲":
                return True, [pos_row,pos_col]
            elif map[pos_row][(pos_col + 1)] == "⬛" or map[pos_row][(pos_col + 1)] == "🏆":
                new_pos = [0,1]
                return False, new_pos
            pass
        case _:
            return True, [pos_row,pos_col]
                        
def move_user(obstacle,map,old_pos_row,old_pos_col,new_pos,character):
    new_map = map
    if not obstacle:
        if map[old_pos_row + new_pos[0]][old_pos_col + new_pos[1]] == '🏆':
            new_map[old_pos_row][old_pos_col] = "⬛"
            new_map[old_pos_row + new_pos[0]][old_pos_col + new_pos[1]] = character
            clear()
            victory = True
            #llamar archivo de finalizacion
        else:
            new_map[old_pos_row][old_pos_col] = "⬛"
            new_map[old_pos_row + new_pos[0]][old_pos_col + new_pos[1]] = character
            victory = False
        return new_map, victory
    if obstacle:
        new_map[old_pos_row][old_pos_col]=character
        victory = False
        return new_map, victory
    pass

def play_game(level, character):
    global game_over, victory
    
    count_thread, display_thread = time_counter.start_timer(60)
    
    clear()
    file = run(level)
    file2map = open_file(file, character)

    map_list = show_map(file2map)
    game_over = False
    victory = False
    
    last_time = time_counter.my_time
    
    while not game_over:
        
        if time_counter.my_time != last_time:
            last_time = time_counter.my_time
            clear()
            map = convert(map_list)
            show_map(map)
            time_counter.print_time()
            print("\nEnter W/A/S/D: ", end="", flush=True)
        
        if time_counter.my_time <= 0:
            time_counter.stop_timer()
            clear()
            print("\n\n⏰ TIME'S UP!")
            print("\n\n- - ☠️ You Lost ☠️- - ")
            print("\n\nRestarting level ")
            set_normal_term()
            game_over = True
            break
        
        if kbhit():
            dir = getch()
            
            row, col = find_user(map_list, character)
            path_blocked, new_pos = find_path(map_list, dir, character)
            new_map_list, victory = move_user(path_blocked, map_list, row, col, new_pos, character)
            
            if not victory:
                clear()
                map = convert(new_map_list)
                map_list = show_map(map)
                time_counter.print_time()
                print("\nEnter W/A/S/D: ", end="", flush=True)
            else:
                time_counter.stop_timer()
                clear()
                print('\n\n🎉 YOU WIN! 🎉')
                set_normal_term()
                level += 1
                game_over = True
        
        time.sleep(0.1) 
    
    count_thread.join()
    display_thread.join()
    return level