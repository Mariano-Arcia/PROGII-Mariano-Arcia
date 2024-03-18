def menu():
    
    print("personas = 1")
    print("vehiculos = 2")
    print("universiades = 3")
    print("notas = 4")
    print("salir = 5")
    
    x = int(input("Escoja un numero: "))

    while x :
        if x == 1: 
            print("Hola has presionado la opcion personas.")
            menu()

        elif x == 2:     
                print("Hola has presionado la opcion vehiculos.")
                menu()

        elif x == 3:
             print("Hola has presionado la opcion universidades.")
             menu()

        elif x == 4:
             print("Hola has presionado la opcion notas.")
             menu()

        elif x == 5:
             print("Hola has presionado la opcion salir.")
             exit()

        else:
             print("Numero no disponible.")
             menu()
menu()

