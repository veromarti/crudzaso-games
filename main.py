import auth
import menu_game
import crud
import game
import time

finish = False
game_over = False
flag_login = False
flag_menu = False
flag_crud = False
character = None
victory = False
level = 1

def principal_menu():
    print("\n==========🎮 MazeQuest MENU 🎮==========")
    print("1. REGISTER 📄")
    print("2. LOGIN 🔐")
    print("3. EXIT ⛔")

    option = input("Choose an option: ")
    return option

def play_game(level, character):
    global game_over, victory
    game.clear()
    file = game.run(level)
    file2map = game.open_file(file,character)

    map_list = game.show_map(file2map)
    while not game_over:
        
        while not victory:
            row , col = game.find_user(map_list,character)
            dir = input("Enter W/A/S/D: ") 
            path_blocked, new_pos = game.find_path(map_list,dir,character)
            new_map_list, victory = game.move_user(path_blocked,map_list,row,col,new_pos,character)
            if not victory:
                map = game.convert(new_map_list)
                new_map_list = game.show_map(map)
            else:
                game.clear()
                print('GANASTE')
                #llamar archivo de finalizacion
                game_over = True
            break
    print("jugando")
    pass

while not finish: 
    while not flag_login:
        option_login = principal_menu()

        if option_login == "1":
            auth.register_user()
            flag_login = False

        elif option_login == "2":
            success = auth.login_user()
            if success:
                print("Entering MazeQuest... 🚀")
                time.sleep(3)
                game.clear()
                flag_login = True
                break  
            else: flag_login = False

        elif option_login == "3":
            print("Exiting program... 👋")
            flag_login = True
            break

        else:
            print("Invalid option ❗")
            flag_login = False
    
    while not flag_menu:
        game.clear()
        menu_game.menu()
        option_menu = (input("\nChoose an option: "))

        match option_menu:
            case '1':
                game.clear()
                character = crud.create()
                if character != None:
                    option_crud = crud.options()

                    match option_crud:
                        case '1':
                            play_game(level,character)
                            pass
                        case '2':
                            crud.show(character)
                            pass
                        case '3':
                            pass
                        case '4':
                            pass
                        case '5':
                            pass
                        case _:
                            pass
                pass
            case '2':
                flag_menu = True
                pass
            case '3':
                crud.sound()
                pass
            #case 4:
                #politicas=" "
                #pass

            #case 5:
                #creditos=" "
                #pass
                
            case _:
                print("\n\033[31mInvalido.\033[0m")

        #menu() definir el archivo menu con funciones
        pass



