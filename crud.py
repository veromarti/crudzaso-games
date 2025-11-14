#🐤🌻🌝
# #Crear👨‍💼
#Eliminar
#Cambiar

personajes = []  

while True:

    print("1. Crear personaje")
    print("2. Mostrar personajes")
    print("3. Actualizar personaje")
    print("4. Eliminar personaje")
    print("5. Salir") 
    opcion = input("Elige una opción: ")

    match opcion:
        
        case  "1":
            emoji = input("Ingresa el emoji del personaje:(🐤/🌻/🌝) ")
            
            if emoji not in ["🐤", "🌻", "🌝"]:
             print("Personaje no disponible")
            
        case "2":
            print(emoji)
            
        case "3":
            emoji = input("Ingresa el emoji del personaje:(🐤/🌻/🌝) ")
            
            if emoji not in ["🐤", "🌻", "🌝"]:
                print("Personaje no disponible")
            
        case "4":
            emoji = ""
            print(f"Emoji eliminsdo{emoji}")
        case "5":
            print("Saliendo")
        case _:
            print("Opcion invalida")
                