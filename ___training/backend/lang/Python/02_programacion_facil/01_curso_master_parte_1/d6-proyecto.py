"""

def saludar():
    nombre = input("Introduzca su nombre, por favor\n")
    print(f"Muy buenas, {nombre}!")

saludar()

"""

""""
def suma(numero1, numero2):
    print(numero1 + numero2)
"""

"""
def suma(numero1, numero2):
    return numero1 + numero2
    
resulado = suma(10, 50)

print(resulado)
"""

def sumar(operando_1, operando_2):
    return round(operando_1 + operando_2, 2)

def restar(operando_1, operando_2):
    return round(round(operando_1 - operando_2, 2))

def multiplicar(operando_1, operando_2):
    return round(operando_1 * operando_2, 2)
    
def dividir(operando_1, operando_2):
    return round(operando_1 / operando_2, 2)

def modulo(operando_1, operando_2):
    return round(operando_1 % operando_2, 2)

def exponente(operando_1, operando_2):
    return round(operando_1 ** operando_2, 2)

def validarContinuar(inputValue):
    continuar = ""
    
    match inputValue:
        case "s":
            continuar = "s"
        case "n":
            continuar = "n"
        case _:
            continuar = "Error"
    
    return continuar

error = False

def printContinuar():
    return "Desea realizar una operación? [ S ] / [ N ]: "

print("\n================================\n")
print("          CALCULADORA")
print("\n================================\n")

continuar = validarContinuar(input(printContinuar()).lower())

while continuar == "Error":
    print(f"\nOperación inválida.")
    continuar = validarContinuar(input(printContinuar()).lower())

while continuar == "s":
    print()
    print("[ 1 ] - Suma")
    print("[ 2 ] - Resta")
    print("[ 3 ] - Multiplicación")
    print("[ 4 ] - División")
    print("[ 5 ] - Módulo")
    print("[ 6 ] - Exponente")

    operacion = input("\nSeleccione la operación a realizar:\n")

    if operacion == "1" or operacion == "2" or operacion == "3" or operacion == "4" or operacion == "5" or operacion == "6":
        error = False
    else:
        print(f'\nOperación inválida.')
        error = True

    if not error:
        print()
        operando_1 = float(input("Introduzca el primer operando: "))
        operando_2 = float(input("\nIntroduzca el segundo operando: "))

        match int(operacion):
            case 1:
                print(f"\nSuma: {sumar(operando_1, operando_2)}")
            case 2:
                print(f"\nResta: {restar(operando_1, operando_2)}")
            case 3:
                print(f"\nMultiplicación: {multiplicar(operando_1, operando_2)}")
            case 4:
                print(f"\nDivisión: {dividir(operando_1, operando_2)}")
            case 5:
                print(f"\nMódulo: {modulo(operando_1, operando_2)}")
            case 6:
                print(f"\nExponentes: {exponente(operando_1, operando_2)}")
    
    print()
    continuar = validarContinuar(input(printContinuar()).lower())

    while continuar == "Error":
        print(f"\nOperación inválida.")
        continuar = validarContinuar(input(printContinuar()).lower())

