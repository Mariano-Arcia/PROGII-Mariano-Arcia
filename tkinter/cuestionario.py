import tkinter as tk 
from PIL import  ImageTk 

ventana = tk.Tk()

path = "c:/Users/MARIANO/Dropbox/Mi PC (MarianOPC)/Downloads/al.jpeg"  
icono = ImageTk.PhotoImage(file=path)
ventana.iconphoto(True, icono)
ventana.title("Ejercicio #2") 

ancho_pantalla = ventana.winfo_screenwidth() 
alto_pantalla = ventana.winfo_screenheight() 

ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")
ventana.config(bg="grey")

def mostrar_datos():
    nombre = cd_1.get()
    apellido = cd_2.get()
    edad = cd_3.get()
    direccion = cd_4.get()
    telefono = cd_5.get
    sexo = cd_6.get
    ciudad = cd_7.get
    datos_formateados = f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad} \nDireccion: {direccion} \nTelefono: {telefono} \nSexo : {sexo} \nCiudad: {ciudad}"
    etiqueta_datos.config(text=datos_formateados)

etiqueta = tk.Label(ventana, text="Hola", bg="grey", fg="white", font=("Arial", 40), width=40, height=2, anchor="center")
etiqueta.grid(row=0, column=0, sticky="w", pady=2)

cd_1 = tk.Entry(ventana, width=30, font=("Arial",15))
cd_1.grid(row=1, column=0, sticky="w", pady=2)
bd_1 = tk.Button(ventana, text="Ingresar nombre", command=mostrar_datos, font=("Arial",15))
bd_1.grid(row=1, column=0, sticky="w", pady=2)

cd_2 = tk.Entry(ventana, width=30, font=("Arial",15))
cd_2.grid(row=2, column=0, sticky="w", pady=2)
bd_2 = tk.Button(ventana, text="Ingresar apellido", command=mostrar_datos, font=("Arial",15))
bd_2.grid(row=2, column=0, sticky="w", pady=2)

cd_3 = tk.Entry(ventana, width=30, font=("Arial",15))
cd_3.grid(row=3, column=0, sticky="w", pady=2)
bd_3 = tk.Button(ventana, text="Ingresar edad", command=mostrar_datos, font=("Arial",15))
bd_3.grid(row=3, column=0, sticky="w", pady=2)

cd_4 = tk.Entry(ventana, width=30, font=("Arial",15))
cd_4.grid(row=4, column=0, sticky="w", pady=2)
bd_4 = tk.Button(ventana, text="Ingresar direccion", command=mostrar_datos, font=("Arial",15))
bd_4.grid(row=4, column=0, sticky="w", pady=2)


cd_5 = tk.Entry(ventana, width=30, font=("Arial",15))
cd_5.grid(row=5, column=0, sticky="w", pady=2)
bd_5 = tk.Button(ventana, text="Ingresar telefono", command=mostrar_datos, font=("Arial",15))
bd_5.grid(row=5, column=0, sticky="w", pady=2)


cd_6 = tk.Entry(ventana, width=30, font=("Arial",15))
cd_6.grid(row=6, column=0, sticky="w", pady=2)
bd_6 = tk.Button(ventana, text="Ingresar sexo", command=mostrar_datos, font=("Arial",15))
bd_6.grid(row=6, column=0, sticky="w", pady=2)


cd_7 = tk.Entry(ventana, width=30, font=("Arial",15))
cd_7.grid(row=7, column=0, sticky="w", pady=2)
bd_7 = tk.Button(ventana, text="Ingresar ciudad", command=mostrar_datos, font=("Arial",15))
bd_7.grid(row=7, column=0, sticky="w", pady=2)

etiqueta_datos = tk.Label(ventana, text="", bg="grey", fg="white", font=("Arial", 20), width=50, height=4, anchor="center")
etiqueta_datos.grid(row=5, column=0, sticky="w", pady=2)

ventana.mainloop()
