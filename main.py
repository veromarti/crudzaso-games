import auth
import menu_game
import crud
import game
import time


finish = False
flag_login = False
flag_menu = False
flag_crud = False
flag_game = False
character = None
level = 1
winner = False
user_info = []

def principal_menu():
    print("\n==========🎮 MazeQuest MENU 🎮==========")
    print("1. REGISTER 📄")
    print("2. LOGIN 🔐")
    print("3. EXIT ⛔")

    option = input("Choose an option: ")
    return option

while not finish: 
    game.set_normal_term()
    while not flag_login:
        option_login = principal_menu()

        if option_login == "1":
            game.clear()
            username = auth.register_user()
            flag_login = False

        elif option_login == "2":
            game.clear()
            success = auth.login_user()
            if success:
                print("Entering MazeQuest... 🚀")
                time.sleep(3)
                game.clear()
                flag_login = True
                flag_menu = False
                flag_crud = False
                flag_game = False
                break  
            else: flag_login = False

        elif option_login == "3":
            game.clear()
            flag_login = True
            flag_menu = True
            finish = True
            flag_game = True
            break

        else:
            print("Invalid option ❗")
            flag_login = False
    
    while not flag_menu:
        game.clear()
        menu_game.menu()
        option_menu = (input("\nChoose an option: "))
        flag_crud = False

        while not flag_crud:
            match option_menu:
                case '1':
                    game.clear()
                    character = crud.create()
                    flag_game = False
                    if character is not None:

                        while not flag_game:
                            game.clear()
                            option_crud = crud.options()

                            match option_crud:
                                case '1':
                                    while level<4:
                                        game.set_curses_term()
                                        level = game.play_game(level, character)
                                        game.set_normal_term()

                                    #input("\n🏁 All levels completed Succesfully🥇! Press Enter to continue...")
                                
                                case '2':
                                    game.clear()
                                    crud.show(character)
                                    input("\nPress Enter to continue...")
                                case '3':
                                    game.clear()
                                    character = crud.edit(character)
                                case '4':
                                    game.clear()
                                    character = crud.remove(character)
                                    input("\nPress Enter to continue...")
                                    flag_crud = True
                                    flag_game = True
                                    flag_menu = False

                                case '5':
                                    flag_game = True
                                    flag_menu = False
                                    flag_crud = True
                                    game.clear()
                                    break
                                    
                                case _:
                                    print("\n ❌Invalid option")
                                    time.sleep(1)
                                    game.clear
                                    flag_game = False

                    else:
                        game.clear()
                        print("\nPlease create a character\n")
                        flag_crud = False
                case '2':
                    game.clear()
                    menu_game.show_instructions()
                    flag_crud = True
                    flag_menu = False
                    print(input("\nPress enter to continue\n"))

                case '3':
                    game.clear()
                    menu_game.show_politics()
                    flag_crud = True
                    flag_menu = False
                    print(input("\nPress enter to continue\n"))

                case '4':
                    game.clear()
                    menu_game.show_credits()
                    flag_crud = True
                    flag_menu = False
                    print(input("\nPress enter to continue\n"))
                case '5':
                    flag_game = False
                    flag_menu = True
                    flag_login = False
                    flag_crud = True
                    finish = False
                    game.clear()
                    break
                    
                case _:
                    print("\n\033[31mInvalido.\033[0m")
                    pass

print("\n\nExiting program... 👋")
time.sleep(2)
game.clear()

