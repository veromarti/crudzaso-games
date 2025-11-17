import json
from game import clear
attempts = 3

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
    clear()
    print("Registration successful ✅")

def login_user():
    users = cargar()
    clear()
    print("\n===🔐 LOGIN 🔐===")
    username = input("Username: ")
    password = input("Password: ")

    global attempts

    while attempts > 0:

        for u in users:
            if u["user"] == username and u["pass"] == password:
                clear()
                print("Login successful ✅ - Access granted to MazeQuest!")
                print("Launching game...")
                attempts = 3
                return True
        clear()
        print("❌ Invalid username or password")
        attempts -= 1
        print("Attempts left:", attempts)
        return False
    clear()
    print("Too many failed attempts ❌")
    return False


