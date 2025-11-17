from auth import login_user
from main import principal_menu 


    
def end(): 
    game_lives=1

    if game_lives > 0:
        print("|----------------------------|")
        print("|\033[32mYOU WON\033[0m 🎉🎉🎉              |")
        print("|----------------------------|\n") 
    else:
        print("|------------------------|")
        print("|\033[31mYOU HAS LOST. ❤️\033[0m         |")
        print("|------------------------|\n")
       #mostrar opciones 
    print("|----------------------------|")
    print("|what do you want to do next?|")    
    print("|----------------------------|")
    print("|1. Play again               |")
    print("|2. Return to the menu       |")
    print("|3. Exit                     |")
    print("|----------------------------|")
    
    option=input("Choose an option (1/2/3): ").strip()
    if option == "1":
        if login_user():
            print("PLAY AGAIN... 🎮\n")
            principal_menu(True)
            
    elif option =="2":
            print("Returning to menu... 🔄\n")
            principal_menu(False)
    # 4) Opción: salir
    elif option == "3":
        print("Exiting game... 👋")
        return
    else:
        print("Invalid option. Exiting...")
        
if __name__ == "__main__":
    end()
    





        
        
   
   
    

    
