import auth
import menu_game
import crud
import game
import time
import time_counter
import sys

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
    import tty, termios, select, atexit
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

finish = False
game_over = False
flag_login = False
flag_menu = False
flag_crud = False
flag_game = False
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
    
    count_thread, display_thread = time_counter.start_timer(60)
    
    game.clear()
    file = game.run(level)
    file2map = game.open_file(file, character)

    map_list = game.show_map(file2map)
    game_over = False
    victory = False
    
    last_time = time_counter.my_time
    
    while not game_over:
        
        if time_counter.my_time != last_time:
            last_time = time_counter.my_time
            game.clear()
            map = game.convert(map_list)
            game.show_map(map)
            time_counter.print_time()
            print("\nEnter W/A/S/D: ", end="", flush=True)
        
        if time_counter.my_time <= 0:
            time_counter.stop_timer()
            game.clear()
            print("\n\n⏰ TIME'S UP!")
            print("\n\n- - ☠️ You Lost ☠️- - ")
            print("\n\nRestarting level ")
            set_normal_term()
            game_over = True
            break
        
        if kbhit():
            dir = getch()
            
            row, col = game.find_user(map_list, character)
            path_blocked, new_pos = game.find_path(map_list, dir, character)
            new_map_list, victory = game.move_user(path_blocked, map_list, row, col, new_pos, character)
            
            if not victory:
                game.clear()
                map = game.convert(new_map_list)
                map_list = game.show_map(map)
                time_counter.print_time()
                print("\nEnter W/A/S/D: ", end="", flush=True)
            else:
                time_counter.stop_timer()
                game.clear()
                print('\n\n🎉 YOU WIN! 🎉')
                set_normal_term()
                level += 1
                game_over = True
        
        time.sleep(0.1) 
    
    count_thread.join()
    display_thread.join()
    return level

while not finish: 
    set_normal_term()
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
            game.clear()
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

                    while not flag_game:
                        game.clear()
                        option_crud = crud.options()

                        match option_crud:
                            case '1':
                                for _ in range(3):
                                    set_curses_term()
                                    level = play_game(level, character)
                                    set_normal_term()

                                input("\n🏁 All levels completed Succesfully🥇! Press Enter to continue...")
                                break   
                            case '2':
                                crud.show(character)
                                input("\nPress Enter to continue...")
                            case '3':
                                character = crud.edit(character)
                                input("\nPress Enter to continue...")
                            case '4':
                                crud.remove()
                                input("\nPress Enter to continue...")
                                break
                            case '5':
                                break
                                
                            case _:
                                print("\n ❌Invalid option")
                                time.sleep(1)
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



