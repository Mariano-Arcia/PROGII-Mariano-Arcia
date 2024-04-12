class sub:
    def __init__(self):
        self.notas = {'Nombre':[],
             'ID':[],
             'Nota': []}
        
    def s(self):
        while True:
            print("MENU PRINCIPAL", "\n1) Crear", "\n2) Listar", "\n3) Eliminar", "\n4) regresar")

            x = int(input("Escoja su opcion: "))

            if x == 1:
                self.crear()

            elif x == 2:
                self.mostrar()

            elif x == 3:
                self.eliminar()

            elif x == 4:
                return
            
    def crear(self):
        nombre = input("Ingrese su nombre: ")
        ID = int(input("Ingrese su ID: "))
        Notas = float(input("Ingrese la nota de este corte: "))
        self.notas['Nombre'].append(nombre) 
        self.notas['ID'].append(ID) 
        self.notas['Nota'].append(Notas)
        print("Se registraron sus datos")

    def mostrar(self):
        print(self.notas)

    def eliminar(self):
        del self.notas
        print("Se borraron los datos")
        
#sub=sub()
#sub.s()
