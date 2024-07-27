
# Importaciones
from tkinter import *

# Creación de la ventana principal
root = Tk()

# Título de la ventana
root.title("Curso de Tkinter de Programación Fácil!")
'''
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
'''
'''
Button(root, text="Botón 1").pack()
Button(root, text="Botón 2").pack()
Button(root, text="Botón 3").pack()
Button(root, text="Botón 4").pack()

# Evento para el botón
def pulsar_boton(idBoton):
    Label(root, text=f"Botón {idBoton} pulsado").pack()

Button(root, text="Botón 1", command=lambda:pulsar_boton(1)).pack()
Button(root, text="Botón 2", command=lambda:pulsar_boton(2)).pack()
Button(root, text="Botón 3", command=lambda:pulsar_boton(3)).pack()
Button(root, text="Botón 4", command=lambda:pulsar_boton(4)).pack()
'''
Label(root,text="Nombre: ").grid(column=0, row=0)
entrada_nombre = Entry(root)
entrada_nombre.grid(column=1, row=0)

Label(root,text="Edad: ").grid(column=0, row=1)
entrada_edad = Entry(root)
entrada_edad.grid(column=1, row=1)

def pulsar_boton():
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()

    Label(root, text=f"Mi nombre es {nombre}. Tengo {edad} años.").grid(column=1, row=3)

Button(root, text="Enviar", command=pulsar_boton).grid(column=1, row=2)

# Bucle de ejecución
root.mainloop()
