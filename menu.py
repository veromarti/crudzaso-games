def menu():

    print(("Menú principal\n").upper().center(30))

    print("1. jugar")
    print("2. Instrucciones")
    print("3. Ajustes sonido")

menu()

opcion=int(input("Selecciona una opcion "))


match opcion:
    case 1:
        pass
    case 2:
          pass
    case 3:
        sonido=input("Presiona + para subir el volumen o - para bajar el volumen: ")
        if sonido!="+" and sonido!="-":
            print("Selección inválida")
        else:
            print("Volumen ajustado", "Subir" if sonido=="+" else "Bajar")
        
    case _:
        print("Invalido")



# while opcion2 !=2:
#     print("Selecciona\n 1. Sonido\n2. Tipo de control")

#     if opcionajustes!=1 and opcionajustes!=2:
#             print("Error")
#             continue
            
#     elif opcionajustes==1:
#             sonido=input("Presiona + para subir el volumen o - para bajar el volumen: ")
#             if sonido!="+" and sonido!="-":
#                 print("Selección inválida")
#             else:
#                 print("Volumen ajustado", "Subir" if sonido=="+" else "Bajar")
#     elif opcionajustes==2:
#             pass
#     break