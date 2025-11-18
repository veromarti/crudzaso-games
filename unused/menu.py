def menu():

    print (" "*30 + "-" * 20) 
    print((" "*30 + "|  \33[96mMenú principal\33[0m"  "  |").center(19))
    print (" "*30 + "-" * 20) 

    print("\n" * 2)

    print (" "*33 + "-" * 14) 
    print((" "*33 + "|  \33[32m1. Jugar\33[0m"  "  |").center(25))
    print (" "*33 + "-" * 14) 

    print("\n" * 2)

    print(" "*4 + "2. Instrucciones"
        +" "*5 + "3. Ajustes sonido"
        +" "*5 + "4. Politicas"
        +" "*5 + "5. Creditos")
    
    import winsound
    winsound.PlaySound('Audio1.wav', winsound.SND_FILENAME)

menu()

opcion=int(input("\nSelecciona una opcion: "))

import winsound
winsound.PlaySound('Audio2.wav', winsound.SND_FILENAME)

match opcion:
    case 1:
        pass

    case 2:
          pass
    
    case 3:
        sonido=input("\nPresiona + para subir el volumen o - para bajar el volumen: ")

        import winsound
        winsound.PlaySound('Audio3.wav', winsound.SND_FILENAME)

        if sonido!="+" and sonido!="-":
            print("\n\033[31mSelección inválida.\033[0m")

            import winsound
            winsound.PlaySound('Audio3.wav', winsound.SND_FILENAME)

        else:
            print("\nVolumen ajustado", "Subir" if sonido=="+" else "Bajar")

            import winsound
            winsound.PlaySound('Audio3.wav', winsound.SND_FILENAME)

    case 4:
        with open("politicas.txt", "r") as archivo:
            print(archivo.read())

        import winsound
        winsound.PlaySound('Audio3.wav', winsound.SND_FILENAME)

    case 5:
        with open("creditos.txt", "r") as archivo:
            print(archivo.read())

        import winsound
        winsound.PlaySound('Audio3.wav', winsound.SND_FILENAME)

    case _:
        print("\n\033[31mnvalido.\033[0m")

        import winsound
        winsound.PlaySound('Audio3.wav', winsound.SND_FILENAME)