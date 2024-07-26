#Importaciones
from tkinter import *

#Creación de la ventana principal
root = Tk()

#Titulo de la ventana
root.title("Curso de Tkinter en Programación Fácil")

#Tamaño de la ventana
root.geometry("800x600+0+0")

#Creación de las etiquetas
#mensaje = Label(root, text="Mi primer programa con Tkinter.")
#mensaje_2 = Label(root, text="Esta es la segunda etiqueta.")
mensaje = Label(root, text="Mi primer programa con Tkinter.").grid(row=0, column=0)
mensaje_2 = Label(root, text="Esta es la segunda etiqueta.").grid(row=0, column=1)

#Se muestran las etiquetas
#mensaje.grid(row=1, column=0)
#mensaje_2.grid(row=0, column=0)

#Bucle de ejecución
root.mainloop()

