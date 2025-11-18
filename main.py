import auth
import menu_game
import crud
import game
import time

finish = False
flag_login = False
flag_menu = False
flag_game = False
character = None
level = 1
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
                                    game.set_curses_term()
                                    level = game.play_game(level, character)
                                    game.set_normal_term()

                                input("\n🏁 All levels completed Succesfully🥇! Press Enter to continue...")
                                break   
                            case '2':
                                game.clear()
                                crud.show(character)
                                input("\nPress Enter to continue...")
                            case '3':
                                character = crud.edit(character)
                            case '4':
                                crud.remove(character)
                                input("\nPress Enter to continue...")
                                game.clear()
                                break
                            case '5':
                                break
                                
                            case _:
                                print("\n ❌Invalid option")
                                time.sleep(1)
            case '2':
                menu_game.show_instructions()
                flag_menu = False
                print(input("\nPress enter to continue\n"))
            case '3':
                crud.sound()
                pass
            case 4:
                menu_game.show_politics()
                flag_menu = False
                print(input("\nPress enter to continue\n"))

            case 5:
                creditos=" "
                menu_game.show_credits()
                flag_menu = False
                print(input("\nPress enter to continue\n"))
                
            case _:
                print("\n\033[31mInvalido.\033[0m")
        pass

print("\n\nExiting program... 👋")
time.sleep(2)
game.clear()

