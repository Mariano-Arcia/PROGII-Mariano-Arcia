from tkinter import *
from PIL import Image, ImageTk 
import tkinter as tk
ventana=Tk()

ventana = Image.open("logo.png")
icono = ImageTk.PhotoImage(path)
ventana.iconphoto(True, icono)
ventana.title("Ejercicio #3")
ventana.geometry("800x800")
ventana.resizable(True, True)
ventana.config(bg="grey")

fr1=Frame(main)

fr2=Frame(main)

titulo=Label(fr2,text="Inicio Sesion",font=("Arial",25))
titulo.pack()

nombre=Label(fr2,text="Ingrese Nombre")
nombre.pack()
no=Entry(fr2)
no.pack()

clave = Label(fr2, text = "Ingrese Clave")
clave.pack()
cl = Entry(fr2)
cl.pack()

n2=Label(fr1,text="Imagen", image=icono)

boton = tk.Button(fr2, text="ingresar")
boton.pack()

n2.pack()



fr1.pack(side="left")
fr2.pack(side="right")


def obtener ():
    nombre = no.get()
    clave = cl.get()
print(nombre,clave)


boton = tk.Button(main, text="ingresar", command=obtener)


mainloop()
