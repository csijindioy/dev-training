# Importaciones
from tkinter import *

# Creación de la ventana principal
root = Tk()

# Título de la ventana
root.title("Curso de Tkinter de Programación Fácil!")

# Entrada de datos
entrada = Entry(root)
entrada.insert(0, "Escriba su nombre ...")
entrada.bind("<Button-1>", lambda e: entrada.delete(0, END))
#entrada.bind("<Key>", lambda e: entrada.delete(0, END))
entrada.pack()

# Evento para el botón
def pulsar_boton():
    #print("Botón pulsado.")
    nombre = entrada.get()
    Label(root, text=f"{nombre}").pack()

# Botón
Button(root, text="Enviar", command=pulsar_boton).pack()

# Bucle de ejecución
root.mainloop()
