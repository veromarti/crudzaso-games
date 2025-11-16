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
          + " " * 5 + "3. Ajustes sonido"
          + " " * 5 + "4. Politicas"
          + " " * 5 + "5. Creditos")
    
    option = input("Select an option: ")

    if option == "2":
        try:
            with open("Instruciones.txt", "r", encoding="utf-8") as file:
                print("\n=== INSTRUCCIONES ===\n")
                print(file.read())
                print("\n======================\n")
        except FileNotFoundError:
            print("No se encontró el archivo Instrucciones.txt")


def sound():
    sonido = input("\nPresiona + para subir el volumen o - para bajar el volumen: ")
    
    if sonido not in ["+", "-"]:
        print("\n\033[31mSelección inválida.\033[0m")
    else:
        print("\nVolumen ajustado", "Subir" if sonido == "+" else "Bajar")
# menu()

# opcion=int(input("\nSelecciona una opcion: "))


# match opcion:
#     case 1:
#         pass
#     case 2:
#           pass
#     case 3:
#         sonido=input("\nPresiona + para subir el volumen o - para bajar el volumen: ")
#         if sonido!="+" and sonido!="-":
#             print("\n\033[31mSelección inválida.\033[0m")
#         else:
#             print("\nVolumen ajustado", "Subir" if sonido=="+" else "Bajar")
#     #case 4:
#         #politicas=" "
#         #pass

#     #case 5:
#         #creditos=" "
#         #pass
        
#     case _:
#         print("\n\033[31mnvalido.\033[0m")


# politicas=" "

# with open("politicas_de_privacidad.txt,"
#        "w") as archivo:
#        archivo.write(politicas)
# print("Leer")

# creditos=" "

# with open("creditos.txt,"
#         "w") as archivo:
#         archivo.write(creditos)
# print("Leer")