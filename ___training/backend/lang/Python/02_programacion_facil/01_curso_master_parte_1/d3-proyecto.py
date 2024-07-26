print("\n================================\n")
print("\n          CALCULADORA\n")
print("\n================================\n")

print("[ 1 ] - Suma.\n")
print("[ 2 ] - Resta.\n")
print("[ 3 ] - Multiplicación.\n")
print("[ 4 ] - División.\n")
print("[ 5 ] - Módulo.\n")
print("[ 6 ] - Exponente.\n")

operacion = int(input("Seleccione la operación a realizar:\n"))
error = False

match operacion:
    case 1:
        print(f'Operación "Suma" seleccionada.\n')
    case 2:
        print(f'Operación "Resta" seleccionada.\n')
    case 3:
        print(f'Operación "Multiplicación" seleccionada.\n')
    case 4:
        print(f'Operación "División" seleccionada.\n')
    case 5:
        print(f'Operación "Módulo" seleccionada.\n')
    case 6:
        print(f'Operación "Exponente" seleccionada.\n')
    case _:
        print(f'Operación inválida.\n')
        error = True

if not error:
    operando_1 = float(input("Introduzca el primer operando:\n"))
    operando_2 = float(input("Introduzca el segundo operando:\n"))

    match operacion:
        case 1:
            print(f"Suma: {round(operando_1 + operando_2, 2)}")
        case 2:
            print(f"Resta: {round(round(operando_1 - operando_2, 2))}")
        case 3:
            print(f"Multiplicación: {round(operando_1 * operando_2, 2)}")
        case 4:
            print(f"División: {round(operando_1 / operando_2, 2)}")
        case 5:
            print(f"Módulo: {round(operando_1 % operando_2, 2)}")
        case 6:
            print(f"Exponentes: {round(operando_1 ** operando_2, 2)}")

