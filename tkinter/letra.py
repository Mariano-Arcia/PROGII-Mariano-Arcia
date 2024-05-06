from tkinter import *
from PIL import Image, ImageTk 
import tkinter as tk
main=Tk()

path = Image.open("logo.png")
icono = ImageTk.PhotoImage(path)
main.iconphoto(True, icono)
main.title("Unitecnar")
main.geometry("1024x920")
main.resizable(True, True)
main.config(bg="light grey")

fr1=Frame(main)

fr2=Frame(main)

titulo=Label(fr2,text="Inicio Sesion",font=("Arial",25))
titulo.pack()

nombre=Label(fr2,text="Ingrese Nombre")
nombre.pack()
user=Entry(fr2)
user.pack()

clave = Label(fr2, text = "Ingrese Clave")
clave.pack()
user1 = Entry(fr2)
user1.pack()

n2=Label(fr1,text="Imagen", image=icono)

boton = tk.Button(fr2, text="ingresar")
boton.pack()

n2.pack()



fr1.pack(side="left")
fr2.pack(side="right")


def obtener ():
    nombre = user.get()
    clave = user1.get()
print(nombre,clave)


boton = tk.Button(main, text="ingresar", command=obtener)


mainloop()