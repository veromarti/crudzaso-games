def nivel_basico():
    with open('map1.txt','r+') as map:
        structure = map.readlines()
        for i in structure:
            #structure.append(int(x) for x in i.strip('\n'))
            # print(map.readlines())
            # print('\n')
            print(i)

nivel_basico()