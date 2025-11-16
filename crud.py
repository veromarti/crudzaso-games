#🐤🌻🌝
# #Crear👨‍💼
#Eliminar
#Cambiar

personajes = []  

def create():
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

# character = create() 
# show(character)  
# character = edit(character)
# character = remove(character) 
# show(character)
                