#key value
#aerolineas : avianca
#origen : Ctg
#Destino : MDE
#Tipo_maleta : ['cabina','mano','bodega']
#imprimir valores del diccionario
#imprimir los valores tipo maleta

Datos = {
    'Aerolinea': 'Avianca',
    'Origen':'CTG',
    'Destino': 'MDE',
    'Tipo':['Cabina','Mano','Bodega']
}
for key, value in Datos.items():
    print(value)
print("Valor de el tipo de maleta: ")

for maleta in Datos ['Tipo']:
    print(maleta)