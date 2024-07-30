# p = "Programacion"
# f = "Facil"

# print(" ".join([p,f]))

# colores = ["azul", "rojo", "verde", "amarillo", "blanco"]
# separador = "*"

# concatena = separador.join(colores)

# print(concatena)

# p = "Programacion"
# f = "Facil"

# # Formateo de Strings
# print("%s %s" % (p,f))

# # Formateo de Float
# # print("%f %s" % (p,f))

# # Formateo de Int
# # print("%i %s" % (p,f))
# # print("%d %s" % (p,f))

# # Se puede agregar tantas llaves '{}' como valores se desea formatear
# print("{} {}".format(p,f))

# print(f"{p} {f}")

# texto = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
# "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
# "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
# "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
# "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
# "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia "
# "deserunt mollit anim id est laborum")

# texto = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
# sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
# Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
# nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
# reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
# Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia 
# deserunt mollit anim id est laborum"""

# print(texto)
# print(texto*3)
# print((texto + " ") * 3)

# # print(len(texto))

# # for letra in texto:
# #     print(letra)

# for letra in range(len(texto)):
#     print(texto[letra])

# print("cion" in "Programacion Facil")

# busca = "cion"
# pf = "Programacion Facil"

# print(busca in pf)
# print(busca not in pf)

# lista = dict(enumerate(texto))
# print(lista)

# lista = list(enumerate(texto))
# print(lista)

# lista = tuple(enumerate(texto))
# print(lista)

# lista = set(enumerate(texto))
# print(lista)

# comillas = """Texto de prueba para "comillas" dobles"""
# print(comillas)

# Ejercicio # 1
frase = [ "Estoy", "aprendiendo", "Python", "con", "el", "curso", "de", "100", "dias", "de", "Programacion", "Facil"]
print(" ".join(frase))

# Ejercicio 2
colores = [ "rojo", "azul", "verde", "amarillo" ]
GUION = "-"
PUNTO = "."

for color in colores:
    print("{} {}{}".format(GUION, color.capitalize(), PUNTO))
    #print(f"{GUION} {color.capitalize()} {PUNTO}")

# Ejercicio 3
numero_1 = 10
numero_2 = 34.50
resultado = numero_1 * numero_2

print("La multiplicacion de %i * %f da como resultado: %f" % (numero_1, numero_2, resultado))

# Ejercicio 4
texto = "Muy lejos, más allá de las montañas de palabras, alejados de los países de las vocales y las consonantes, viven los tecto simulados. Vicen aislados en casas de letras, en la costa de la semántica, un gran océano de lenguas"
coincidencias = 0

busqueda = str(input("Que letra deseas buscar?\n"))

for letra in texto:
    if letra == busqueda:
        coincidencias+=1

print(f"Se encontró {coincidencias} coincidencias de la letra {busqueda}.")

# Ejercicio 5
print("La multiplicacion de %i * %.3f da como resultado: %.3f" % (numero_1, numero_2, resultado))