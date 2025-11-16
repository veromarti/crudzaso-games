users = []
passwords = []

def register_user():
    print("\n====🎮 REGISTER USERS 🎮=====")
    new_user = input("Enter a username: ")
    new_pass = input("Enter a password: ")

    if new_user in users:
        print("This username is already taken. ❎")
    else:
        users.append(new_user)
        passwords.append(new_pass)
        print("Registration successful. ✅")
        print("Users in memory:", users)

def login_user():
    print("\n===🔐 LOGIN 🔐===")
    username = input("Username: ")
    password = input("Password: ")

    attempts = 3

    while attempts > 0:
        if username in users:
            pos = users.index(username)

            if password == passwords[pos]:
                print("Login successful  Access granted to MazeQuest!")
                print("Launching game...")
                return True 
            else:
                attempts -= 1
                print("Wrong password ❌")
                print("Attempts left:", attempts)

                if attempts > 0:
                    password = input("Try again: ")
        else:
            print("User does not exist ❌")
            return False

    print("Too many failed attempts ❌")
    return False

def menu():
    while True:
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
                break  

        elif option == "3":
            print("Exiting program... 👋")
            break

        else:
            print("Invalid option ❗")

menu()