import tkinter as tk 
from PIL import ImageTk

ventana = tk.Tk()

path = "c:/Users/MARIANO/Dropbox/Mi PC (MarianOPC)/Downloads/al.jpeg"  
icono = ImageTk.PhotoImage(file=path)
ventana.iconphoto(True, icono)
ventana.title("Ejercicio #2") 

ancho_pantalla = ventana.winfo_screenwidth() 
alto_pantalla = ventana.winfo_screenheight() 

ventana.geometry(f"{800}x{800}")
ventana.config(bg="grey")

def mostrar_datos():
    nombre = cd_1.get()
    apellido = cd_2.get()
    edad = cd_3.get()
    direccion = cd_4.get()
    telefono = cd_5.get()
    sexo = var_genero.get()
    ciudad = cd_7.get(cd_7.curselection())
    datos_formateados = f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nDirección: {direccion}\nTeléfono: {telefono}\nGénero: {sexo}\nCiudad: {ciudad}"
    etiqueta_datos.config(text=datos_formateados)

etiqueta = tk.Label(ventana, text="Hola", bg="grey", fg="white", font=("Arial", 40))
etiqueta.grid(row=0, column=0, columnspan=2, pady=10)

cd_1 = tk.Entry(ventana, width=10, font=("Arial",15))
cd_1.grid(row=1, column=1, sticky="w", pady=2)
bd_1 = tk.Button(ventana, text="Ingresar nombre", command=mostrar_datos, font=("Arial",15))
bd_1.grid(row=1, column=0, sticky="w", pady=2)

cd_2 = tk.Entry(ventana, width=10, font=("Arial",15))
cd_2.grid(row=2, column=1, sticky="w", pady=2)
bd_2 = tk.Button(ventana, text="Ingresar apellido", command=mostrar_datos, font=("Arial",15))
bd_2.grid(row=2, column=0, sticky="w", pady=2)

cd_3 = tk.Entry(ventana, width=10, font=("Arial",15))
cd_3.grid(row=3, column=1, sticky="w", pady=2)
bd_3 = tk.Button(ventana, text="Ingresar edad", command=mostrar_datos, font=("Arial",15))
bd_3.grid(row=3, column=0, sticky="w", pady=2)

cd_4 = tk.Entry(ventana, width=10, font=("Arial",15))
cd_4.grid(row=4, column=1, sticky="w", pady=2)
bd_4 = tk.Button(ventana, text="Ingresar dirección", command=mostrar_datos, font=("Arial",15))
bd_4.grid(row=4, column=0, sticky="w", pady=2)

cd_5 = tk.Entry(ventana, width=10, font=("Arial",15))
cd_5.grid(row=5, column=1, sticky="w", pady=2)
bd_5 = tk.Button(ventana, text="Ingresar teléfono", command=mostrar_datos, font=("Arial",15))
bd_5.grid(row=5, column=0, sticky="w", pady=2)

cd_6 = tk.Label(ventana,text="Género", font=("Arial",15))
cd_6.grid(row=6, column=0, sticky="w", pady=2)

var_genero = tk.StringVar()
var_genero.set("Masculino")

rb_hombre = tk.Radiobutton(ventana, text="Masculino", variable=var_genero, value="Masculino")
rb_mujer = tk.Radiobutton(ventana, text="Femenino", variable=var_genero, value="Femenino")
rb_hombre.grid(row=7, column=0, sticky="w", pady=2)
rb_mujer.grid(row=8, column=0, sticky="w", pady=2)

bd_ciudad = tk.Button(ventana, text="Seleccionar ciudad", command=mostrar_datos, font=("Arial",15))
bd_ciudad.grid(row=9, column=0, pady=10)

cd_7 = tk.Listbox(ventana, width=10, selectmode="single", font=("Arial",15))
ciudades = ["Bogota", "Cartagena", "Barranquilla", "Cali", "Medellin"]

for ciudad in ciudades:
    cd_7.insert(tk.END, ciudad)

cd_7.grid(row=10, column=0, sticky="w", pady=2)

etiqueta_datos = tk.Label(ventana, text="", bg="grey", fg="white", font=("Arial", 20), width=10, height=4, anchor="center")
etiqueta_datos.grid(row=11, column=0, sticky="w", pady=10)

ventana.mainloop()
