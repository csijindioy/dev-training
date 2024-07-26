#Funciones lambda o anónimas
"""
def multiplicacion(numero1, numero2):
    return numero1 * numero2
"""
"""
multiplicacion = lambda numero1, numero2 : numero1 * numero2

resultado1 = multiplicacion(10, 10)
resultado2 = multiplicacion(5, 5)

print(resultado1)
print(resultado2)
"""

#(lambda numero1, numero2 : print(numero1 * numero2)) (7, 5)

#Ejercicio 1 - Radio de circunferencia
(lambda radio : print(3.14 * radio ** 2)) (2)
