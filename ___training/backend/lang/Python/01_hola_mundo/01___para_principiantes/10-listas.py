lenguajes = ["Python", "Ruby", "PHP", "Javascript", "Java"]
print(lenguajes)
print(lenguajes[1])
lenguajes[1] = "Go"
print(lenguajes)

# El índice positivo, o sin índice, hace referencia a la posicioón en la lista de izquierda a derecha
# El índice negativo hace referencia a la posicioón en la lista de derecha a izquierda
print(lenguajes[-1])

# Sólo incluye los elementos de las posisciones 1 y 2
# El elemento en la posisción 3 no lo toma pues se esta señalando que esa es la posición para terminar la selección
print(lenguajes[1:3])

# Selecciona desde la posición cero hasta la posición 2
print(lenguajes[:3])

# Selecciona desde la posición 1 hasta la última posición
print(lenguajes[1:])