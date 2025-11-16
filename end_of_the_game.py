from auth import login_user
from auth import menu


    
def end(): 
    game_lives=1

    if game_lives > 0:
        print("LEVEL COMPLETE. THANK YOU FOR PLAYING 🎉🎉🎉\n")
    else:
        print("GAME OVER. YOU'RE OUT OF LIVES. ❤️\n")
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
            menu()
            
    elif option =="2":
            print("Returning to menu... 🔄\n")
            menu()
    # 4) Opción: salir
    elif option == "3":
        print("Exiting game... 👋")
        return
    else:
        print("Invalid option. Exiting...")
    
    
        
if __name__ == "__main__":
    end()
    





        
        
   
   
    

    
