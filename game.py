def levelI():
    with open('map1.txt','r+') as map:
        structure = map.readlines()
        new_map = []
        for i in structure:
            print(i)
            for j in i:
                new_map.append(i).append(j)
    return new_map

def levelII():
    with open('map2.txt','r+') as map:
        structure = map.readlines()
        new_map = []
        for i in structure:
            print(i)
            new_map.append(i)
    return new_map


def move_cursor(map,dir):
    new_map = map
    print(new_map)
    print(type(new_map))
    i = 0
    j = 0
    for line in map:
        print(line)
        i += 1
        for pos in line:
            j += 1
            print(new_map.size())
            if dir == "A":
                if new_map[line.index()][(pos.index())-1] == "|":
                    print("error")
                pass

levelI()

dir = 'A'

move_cursor(levelI(),dir)