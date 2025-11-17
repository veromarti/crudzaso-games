#🐤🌻🌝
# #Crear
#Eliminar
#Cambiar

def create():
    print("- - - - Available Characters - - - -\n")
    option = input("1. 🐤 \n2. 🌻 \n3. 🌝 \nChoose your character (1-3): ")

    match option:
        case  "1":
            emoji = "🐤"
            pass
        case  "2":
            emoji = "🌻"
            pass
        case  "3":
            emoji = "🌝"
            pass
        case _:
            print("\n Invalid option")
            emoji = None
    return emoji

def show(char):
    print(char)

def edit(char):
    print("\n Current character: "+ char)
    emoji = create()
    return emoji

def remove(char):
    char = None
    return char

def options():
    print("- - - 🌀 MazeQuest 🌀 - - -\n")
    print("1. Play Game 🎮")
    print("2. Show character 👤")
    print("3. Edit character ⚙️")
    print("4. Remove Character 🗑️")
    print("5. Back 🔙") 
    option = input("\nChoose an option: ")
    return option
                