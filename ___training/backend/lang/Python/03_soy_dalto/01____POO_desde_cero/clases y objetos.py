class Celular():
    # Constructor de clase celular
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    def llamar(self):
        print("Llamando ...")
        
    def terminar(self):
        print("Llamada terminada")


celualar_1 = Celular("Samsung", "S23", "48MP")
celualar_2 = Celular("Apple", "iPhone 15 Pro", "96MP")
#celualar_3 = Celular("Samsung", "S23", "48MP")


print(celualar_1.marca)
print(celualar_2.marca)

celualar_1.llamar()
celualar_1.terminar()

celualar_2.llamar()
celualar_2.terminar()
