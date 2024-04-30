import tkinter as tk 
from PIL import Image, ImageTk # Requiere instalar Pillow 
import tkinter as tk

ventana = tk.Tk()
#Agregando icono a la ventana
path = Image.open("c:/Users/MARIANO/Dropbox/Mi PC (MarianOPC)/Downloads/al.jpeg")
icono = ImageTk.PhotoImage(path)
ventana.iconphoto(True, icono)
# Establecemos el nombre del titulo de la ventana.
ventana.title("Ejercicio #1") 
# Establecemos el tamaño de la ventana. ventana.geometry("<ancho>x<alto>+<posición_x>+<posición_y>")

# Obtener las dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth() #método para obtener Ancho
alto_pantalla = ventana.winfo_screenheight() #método para obtener Alto

# Establecer el tamaño completo de la ventana
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")
# Definimos si la ventana puede ser modificada en su tamaño.
ventana.resizable(True, True) 
# Podemos añadir configuraciones adicionales a la ventana con la funcion config
ventana.config(bg="black")
# Inicializamos la aplicacion

def cambiar_texto():
    etiqueta.config(text="Bienvenido")
etiqueta = tk.Label(ventana, text = "Hola", bg = "black", fg = "white", font = ("Ariel",40), width = 20, height = 2, anchor = "center")
etiqueta.pack()
# Crear un botón con texto y función de comando
boton1 = tk.Button(ventana, text="Iniciar Cesion", command=cambiar_texto, bg = "black", fg = "white", font = ("Ariel",25), width = 20, height = 2, anchor = "center")
boton1.pack()

# Crear un botón con colores de fondo y texto personalizados
boton2 = tk.Button(ventana, text="Crear una cuenta", bg="black", fg="green", font=("Arial", 20))
boton2.pack()

# Crear un botón deshabilitado
boton3 = tk.Button(ventana, text="atras", state="disabled", bg="black", fg="red", font=("Arial", 20))
boton3.pack()
ventana.mainloop()
