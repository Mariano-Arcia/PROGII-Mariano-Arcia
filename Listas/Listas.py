#punto 1
print("Punto 1")
vacia = []
print("")

#punto 2
print("Punto 2")
cinco= ['a','b','c','d','e','f','g']
print("")

#Punto 3
print("punto3")
print('longitud las listas: ', len(vacia))
print('longitud las listas: ', len(cinco))
print("")

#punto 4
print("punto")
P_L = cinco[0]
print("Primer elemento: ",P_L)
L_M = cinco[4]
print("Elemento central: ",L_M)
U_L =cinco[6]
print("ultimo elemento: ",U_L)
print("")

#punto 5
print("Punto 5")
Datos_personales = ['Nombre','Edad','altura','Estado civil','Direccion']
Datos_personales.append('Fecha de nacimineto')
print(Datos_personales)
print("")

#Punto 6
print("Punto 6")
It_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(It_companies)
print("")

#Punto 7
print("Punto 7")
It_companies.insert(3,'Fedex')
print(It_companies)
print("")

#Punto 8
print("Punto 8")
existe = 'Apple' in It_companies
print("Apple esta en la lista? ",existe)
print("")

#punto 9
print("Punto 9")
print(It_companies)
It_companies.sort()
print(It_companies)
print("")

#Punto 10
print("punto 10")
It_companies.reverse()
print(It_companies)
print("")

#Punto 11a
print("Punto 11a")
It_companies.pop(0)
print(It_companies)
print("")

#Punto 11b
print("Punto 11b")
del It_companies[0]
print(It_companies)
print("")

#Punto 12
print("Punto 12")
It_companies.clear
print(It_companies)
print("")