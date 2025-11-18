def looser():
    print("|------------------------|")
    print("|       \033[31mYOU LOST ☠️\033[0m       |")
    print("|------------------------|")
     

def winner():
    print("|----------------------------|")
    print("|\033[32mYOU WON\033[0m 🎉🎉🎉              |")
    print("|----------------------------|\n")
    end_menu()

def end_menu(): 
    print("|----------------------------|")
    print("|What do you want to do next?|")    
    print("|----------------------------|")
    print("|1. Play again               |")
    print("|2. Return to main menu      |")
    print("|3. Exit                     |")
    print("|----------------------------|")
    
    flag = False
    while not flag:
        option=input("Choose an option (1/2/3): ").strip()

        if option == "1" or option == "2" or option == "3":
            flag = True
            return option
                
        else:
            print("Wrong Entry. Try again...\n")
            flag = False
