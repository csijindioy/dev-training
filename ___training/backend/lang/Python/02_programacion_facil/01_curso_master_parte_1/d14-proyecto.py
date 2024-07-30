# # Importaciones
# from tkinter import *
# import os # from os import *
# from PIL import ImageTk, ImageColor, Image

# # --- Carga de directorios ---
# # Carpeta principal
# carpeta_principal = os.path.dirname(__file__)

# # Carpeta imágenes
# carpeta_imagenes = os.path.join(carpeta_principal, "imagenes")

# # Carpeta imágenes/paisajes
# carpeta_paisajes = os.path.join(carpeta_imagenes, "paisajes")

# # Creación de la ventana principal
# root = Tk()

# # Titulo de la ventana
# root.title("www.programacionfacil.org")

# # Icono de la ventana
# root.iconbitmap(os.path.join(carpeta_imagenes, "favicon.ico"))

# # Carga de imagen
# bosque = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes, "paisaje-01.jpg")).resize((350, 200)))

# etiqueta = Label(image=bosque)
# etiqueta.pack()

# # Bucle de la ejecución
# root.mainloop()

# # Ejercicio 1
import os
carpeta_principal = os.path.dirname(__file__)
# print(carpeta_principal)

# Ejercicio 2
# Importaciones
from tkinter import *
from PIL import ImageTk, ImageColor, Image

# Carpeta imágenes
carpeta_imagenes = os.path.join(carpeta_principal, "imagenes")
carpeta_paisajes = os.path.join(carpeta_imagenes, "paisajes")

# Creación de la ventana principal
root = Tk()

# Titulo de la ventana
root.title("www.programacionfacil.org")

# Icono de la ventana
root.iconbitmap(os.path.join(carpeta_imagenes, "favicon.ico"))

# Ejercicio 3
paisaje_1 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes, "paisaje-01.jpg")).resize((400, 250)))
etiqueta_paisaje_1 = Label(image=paisaje_1)
etiqueta_paisaje_1.grid(row=0, column=0)

paisaje_2 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes, "paisaje-02.jpg")).resize((400, 250)))
etiqueta_paisaje_2 = Label(image=paisaje_2)
etiqueta_paisaje_2.grid(row=0, column=1)

paisaje_3 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes, "paisaje-03.jpg")).resize((400, 250)))
etiqueta_paisaje_3 = Label(image=paisaje_3)
etiqueta_paisaje_3.grid(row=1, column=0)

paisaje_4 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes, "paisaje-04.jpg")).resize((400, 250)))
etiqueta_paisaje_4 = Label(image=paisaje_4)
etiqueta_paisaje_4.grid(row=1, column=1)

# Bucle de la ejecución
root.mainloop()

