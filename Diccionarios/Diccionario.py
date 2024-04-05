#Punto 1.
print("Punto 1")
perro = {}
print(perro)

#Punto 2.
print("\nPunto 2")
perro = {'nombre': 'Lucas', 
         'color':'blanco y negro',
         'raza': 'Pastor Aleman', 
         'pata':'4', 
         'edad': '2 años' }
print(perro)

#Punto 3
print("\nPunto 3")
estudiante = {'nombre':'Mariano',
              'apellido': 'Arcia',
              'sexo': 'Masculino',
              'edad': '19',
              'estado_civil':'soltero',
              'habilidades':['Tocar guitarra', 'Tocar bajo'],
              'pais': 'Colombia',
              'ciudad': 'Cartagena',
              'direccion': 'San Jose de los campanos'
              }
print(estudiante)

#Punto 4
print("\nPunto 4")
print(len(estudiante))

#Punto 5
print("\nPunto 5")
print(estudiante['habilidades'][0])

#Punto 6
print("\nPunto 6")
estudiante['habilidades'].append('saber sumar')
print(estudiante)

#Punto 7
print("\nPunto 7")
claves = estudiante.keys()
print(claves)

#Punto 8
print("\nPunto 8")
valores = estudiante.values()
print(valores)

#Punto 9
print("\nPunto 9")
print(estudiante.items())

#Punto 10
print("\nPunto 10")
estudiante.pop('direccion')
print(estudiante)

#Punto 11
print("\nPunto 11")
del estudiante