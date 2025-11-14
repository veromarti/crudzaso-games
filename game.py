def levelI():
    with open('map1.txt','r+') as map:
        structure = map.readlines()
        new_map = []
        new_path = []
        cont = 0

        for i in structure:
            print(i)
            for j in i:
                if j != '\n':
                    new_path.append(j)
                else:
                    pass
            new_map.append(new_path)
            new_path = []
    return new_map

def find_user(map):
    cont_x = 0
    cont_y = 0
    for line in map:
        print(line)        
        for pos in line:
            if pos == 'U':
                x = line.index('U')
                y = line.index(pos)
                return(cont_x, cont_y)
            cont_y += 1
        cont_x += 1 
        cont_y = 0
            
    

# def levelII():
#     with open('map2.txt','r+') as map:
#         structure = map.readlines()
#         new_map = []
#         for i in structure:
#             print(i)
#             new_map.append(i)
#     return new_map


def move_cursor(map,dir):
    pos_x,pos_y = find_user(map)
    new_map = map
    i = 0
    j = 0
    if new_map[pos_x][(pos_y - 1)] == "|" or new_map[pos_x][(pos_y -1)] == "+":
        print("errorA")
    elif new_map[pos_x][(pos_y + 1)] == "|" or new_map[pos_x][(pos_y +1)] == "+":
        print("errorD")
    elif new_map[pos_x - 1][(pos_y)] == "|" or new_map[pos_x -1 ][(pos_y)] == "+":
        print("errorW")
    # for line in map:
    #     #print(line)
    #     for pos in line:
    #         j += 1
    #         if dir == "A":
    #             if new_map[pos_x][(pos_y -1)] == "|":
    #                 print("error")
            

levelI()

dir = 'W'
#print(find_user(levelI()))

move_cursor(levelI(),dir)