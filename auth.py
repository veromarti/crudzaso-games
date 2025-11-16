import json
flag_menu = False

def cargar():
    with open("bd.json", "r") as archivo:
        return json.load(archivo)
    
def guardar(users):
    with open("bd.json", "w") as archivo:
        return json.dump(users, archivo, indent=4, ensure_ascii=False)

def register_user():
    users = cargar()
    print("\n====🎮 REGISTER USERS 🎮=====")
    new_user = input("Enter a username: ")
    new_pass = input("Enter a password: ")

    for u in users:
        if u["user"] == new_user:
            print("❌ Username already exists")
            return
        else:
            nuevo_user = {
                "user" :new_user,
                "pass" :new_pass
            }
            
    users.append(nuevo_user)
    guardar(users)
    print("Registration successful ✅")
    print("Users in memory:", users)

def login_user():
    users = cargar()

    print("\n===🔐 LOGIN 🔐===")
    username = input("Username: ")
    password = input("Password: ")

    attempts = 3

    while attempts > 0:

        for u in users:
            if u["user"] == username and u["pass"] == password:
                print("Login successful ✅ - Access granted to MazeQuest!")
                print("Launching game...")
                return True

        print("❌ Invalid username or password")
        attempts -= 1
        print("Attempts left:", attempts)
        return False


    print("Too many failed attempts ❌")
    return False

def menu(flag_menu):
    while not flag_menu:
        print("\n==========🎮 MazeQuest MENU 🎮==========")
        print("1. REGISTER 📄")
        print("2. LOGIN 🔐")
        print("3. EXIT ⛔")

        option = input("Choose an option: ")

        if option == "1":
            register_user()

        elif option == "2":
            success = login_user()
            if success:
                print("Entering MazeQuest... 🚀")
                flag_menu = True
                break  

        elif option == "3":
            print("Exiting program... 👋")
            flag_menu = True
            break

        else:
            print("Invalid option ❗")

menu(flag_menu)
