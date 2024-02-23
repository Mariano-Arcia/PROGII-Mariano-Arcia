class persona:
    def __init__(self, nombre, apellido):
        self.nombre= nombre
        self.apellido= apellido
    def imprimirnombre(self): 
        return f'mi nombre es {self.nombre}{self.apellido}'
    #instanciamos la clase
    
p = persona("Mariano"," Arcia")
print(p.imprimirnombre())#llamamos al metodo
    