# DICCIONARIOS

microsoft_office = {
    "word": "Suite word",
    "excel": "Suite excel",
    "power": "Suite power point"
}

#print(microsoft_office["excel"])

microsoft_office["outlook"] = "Suite outlook"

#print(microsoft_office["outlook"])

for programa in microsoft_office:
    print(f"-{programa.capitalize()} : {microsoft_office[programa]}")

diccionario = {
    1: "Valor 1",
    2: "Valor 2",
    3: "Valor 3"
}

print(diccionario[3])
