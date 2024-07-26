#for i in range(5):
#    print(F"El valor del bucle es: {i}.")

#for i in range(1, 6):
#    print(F"El valor del bucle es: {i}.")

#for i in range(1, 15, 2):
#    print(F"El valor del bucle es: {i}.")

#for i in range(-5):
#    print(F"El valor del bucle es: {i}.")

#for i in range(1, -6):
#    print(F"El valor del bucle es: {i}.")

#for i in range(1, -15, -2):
#    print(F"El valor del bucle es: {i}.")

#colores = ["rojo", "azul", "verde", "amarillo"]

#print("---LISTADO DE COLORES---")

#for color in colores:
#    if color == "azul" or color == "verde":
#        print("Se ha saltado este valor.")
#        continue
#    print(f"- Color {color}.")

#for color in colores:
#    if color == "azul":
#        print("Se ha roto la ejecución del bucle.")
#        break
#    print(f"- Color {color}.")


#i = 1

#while i <= 5:
#    print(f"El valor del bucle es: {i}.")
#    i+=1

# EJERCICIO 1
#for i in range(7, 15):
#    print(f"El valor del bucle es: {i}.")

# EJERCICIO 2
#top = 14
#counter = 7

#while counter <= top:
#    print(f"El valor del bucle es: {counter}.")
#    counter+=1

# EJERCICIO 3
# FOR
#print("---BUCLE FOR")
#for i in range(0, -5001, -500):
#    print(f"El valor del bucle es: {i}.")

# WHILE
#print("---BUCLE WHILE")
#top = -5000
#counter = 0

#while counter >= top:
#    print(f"El valor del bucle es: {counter}.")
#    counter+=-500

# EJERCICIO 4
#paises = ["Colombia", "Perú", "Ecuador", "Bolivia", "Argentina", "Brasil", "Venezuela", "Chile", "Uruguay", "Paraguay", "El Salvador", "Honduras", "Mexico", "Nicaragua"]
#paises.sort(reverse=False)

#for pais in paises:
#    print(f"-> {pais} <-")
    
# EJERCICIO 5
#numeros = [10, 45, 356, 10, 10, 10, 46, 67, 45, 10, 10, 43, 10, 65, 10, 10]
#numeros.sort(reverse=False)

#for numero in numeros:
#    if numero == 10:
#        continue
#    elif numero == 356:
#        break
#    else:
#        print(f"El valor del elemento es: {numero}")

pizzas = ["Margarita", "Carbonara", "Super Pollo"]
precios_pizzas = [6.50, 9.00, 12.75]

adicionales = ["No añadir extras", "Extra de queso", "Champiñones", "Albahaca"]
precios_adicionales = [0.0, 1.25, 0.85, 0.5]

total_a_pagar = 0.0
total_adicionales = 0.0

print("\n<- Pizzeria PF ->\n")

pote = float(input("Introduzca el monto deseado:\n"))
print("")

for i in range(len(pizzas)):
    print(f"{i + 1} - {pizzas[i]} - {precios_pizzas[i]}$")

pizza_seleccionada = int(input("\nHola, por favor, seleccione su pizza con un  número de opción:\n"))

while pizza_seleccionada > len(pizzas):
    print("\nLa pizza seleccionada no existe. Inténtelo de nuevo.\n")
    pizza_seleccionada = int(input("\nSeleccione su pizza con un  número de opción:"))

total_a_pagar = precios_pizzas[pizza_seleccionada - 1]

print(f"\nHa elegido la pizza {pizzas[pizza_seleccionada - 1]}.")
print(f"Total a pagar {precios_pizzas[pizza_seleccionada - 1]}$.")
print(f"Le quedan {pote - float(precios_pizzas[pizza_seleccionada - 1])}$.\n")

for i in range(len(adicionales)):
    print(f"{i} - {adicionales[i]} - {precios_adicionales[i]}$")
    
adicional = int(input("\nSi desea algún ingrediente extra, seleccionelo.\n"))

while adicional >= len(adicionales):
    print("La opcion seleccionada no existe. Inténtelo de nuevo.\n")
    adicional = int(input("\nSi desea algún ingrediente extra, seleccionelo.\n"))
    
while adicional >  0:
    total_adicionales += precios_adicionales[adicional]
    total_a_pagar += total_adicionales
    
    print(f"\nHa elegido el adicional {adicionales[adicional]}.")
    print(f"\nExtra a pagar {precios_adicionales[adicional]}.")
    print(f"Total a pagar {total_a_pagar}$.")
    print(f"Le quedan {pote - total_a_pagar}$.\n")
    
    adicional = int(input("\nDesea algún ingrediente extra, seleccionelo.\n"))

print("--- SU PEDIDO ---")
print(f"El total de su pedido es {total_a_pagar}$.")
print(f"Su cambio: {pote - total_a_pagar}$.\n")

