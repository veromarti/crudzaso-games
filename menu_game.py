def menu():

    print(" " * 30 + "-" * 20) 
    print(" " * 30 + ("|     \33[96mMazeQuest\33[0m    |").center(20))
    print(" " * 30 + "-" * 20) 

    print("\n" * 2)

    print(" " * 33 + "-" * 14) 
    print((" " * 33 + "|  \33[32m1. Start\33[0m  |").center(25))
    print(" " * 33 + "-" * 14) 

    print("\n" * 2)

    print(" " * 4 + "2. How to play?"
          + " " * 5 + "3. Politicas"
          + " " * 5 + "4. Creditos")
    
def show_instructions():
        try:
            with open("Instructions.txt", "r", encoding="utf-8") as file:
                print("\n=== INSTRUCTIONS ===\n")
                print(file.read())
                print("\n======================\n")
        except FileNotFoundError:
            print("Missing file Instructions.txt")


