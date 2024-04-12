from parcial_2 import *

def menu_principal():
    while True:
        print("\n1) Periodo 1", "\n2) Periodo 2", "\n3) Periodo 3", "\n4) periodo 4","\n5) Salir") 

        x = int(input("Escoja una opcion: "))

        if x == 1 or x < 5:
            su = sub()
            print(su.s())

        elif x == 5:
            print("cesion cerrada")
            break

        else:
            print("Opcion invalida")

menu_principal()