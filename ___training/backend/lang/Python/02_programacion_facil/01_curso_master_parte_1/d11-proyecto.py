"""
class Taza():
    color = "blanco"
    mensaje = None
    material = "Porcelana"
    limpia = True

taza_1 = Taza()
taza_2 = Taza()
taza_2.color = "blanco y azul"

print(taza_1.color)
print(taza_2.color)
"""

""""
class Vehiculo():
    # Atributos
    pais_origen = "Alemania"
    
    def __init__(self, color, longitud_metros, ruedas):
        self.color = color
        self.longitud_metros = longitud_metros
        self.ruedas = ruedas
    
    # Métodos
    def arrancar(self):
        print("El vehículo ha arrancado.")
    
    def detener(self):
        print("El vehículo esta detenido.")
    
    def mostrar_info():
        print(f"Vehículo de color {self.color}. Con una longitud de {self.longitud_metros}. Tiene {self.ruedas}.")

# Instancia de los objetos
vehiculo_1 = Vehiculo("rojo", 4, 4)
vehiculo_2 = Vehiculo("negro", 8.25, 8)

vehiculo_2.material_aleron = "Fibra de carbono"
"""

"""
# Llamadas a métodos
vehiculo_1.arrancar()
vehiculo_1.detener()
"""
#print(vehiculo_2.material_aleron)

#print(vehiculo_2.pais_origen)

class Motocicleta():
    # Atributos de clase
    estado = "Nueva"
    motor = False
    precio = None

    # Métodos
    def __init__(self, color, matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_fabricacion, velocidad_punta, peso, capacidad_total_combustible):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        self.capacidad_total_combustible = capacidad_total_combustible

    def arrancar(self):
        if(self.motor):
            print("El motor ya esta en marcha.")
        else:
            self.motor = True
            print("El motor ha arrancado.")
    
    def detener(self):
        if(self.motor):
            self.motor = False
            print("El motor se ha detenido.")
        else:
            print("El motor ya esta detenido.")
    
    def consultar_precio(self):
        print(f"El precio de la motocicleta {self.marca} {self.modelo} es de {self.precio}")
    
    def consultar_combustible(self):
        # Imprimir reporte combustible disponible
        print(f"\n*** Reporte de depósito de {self.marca} {self.modelo} ***\n")
        print(f"Capacidad total de combustible: {self.capacidad_total_combustible} litros.")
        print(f"Combustible disponible: {self.combustible_litros}  litros.")
        print(f"Combustible faltante: {self.capacidad_total_combustible - self.combustible_litros} litros.\n")
        print(f"*** Fin reporte de depósito de {self.marca} {self.modelo} ***\n")
    
    def tanquear(self):
        while True:
            self.litros_repostaje = float(input("Cuantos litros desea respostar?:\n"))

            if(self.litros_repostaje + self.combustible_litros > self.capacidad_total_combustible):
                print(f"Sólo puede repostar {self.capacidad_total_combustible - self.combustible_litros} litros.\n")
            else:
                self.combustible_litros += self.litros_repostaje
                print(f"Se repostó exitosamente {self.litros_repostaje} litros de combustible.")
                print(f"Total combustible en tanque: {self.combustible_litros} litros.")
                break

mi_primera_moto = Motocicleta("Negro", "QWA04F", 10, 2, "AKT", 2023, "SEP 2022", "180 Kms/h", "98 Kgs", 13)
mi_primera_moto.precio = "7'000.000,00 COP"

# Ejercicio 8
moto_imaginaria = Motocicleta(
    capacidad_total_combustible=30,
    matricula="WER87Y",
    combustible_litros=0,
    numero_ruedas=2,
    velocidad_punta="245 Kms/h",
    peso="115 Kgs",
    color="Azul Indigo",
    fecha_fabricacion="Ene 2024",
    modelo=2024,
    marca="Honda"
    )

# Ejercicio 9
#print("*** Mi primera moto ***\n")
#mi_primera_moto.detener()
#mi_primera_moto.arrancar()
#mi_primera_moto.arrancar()
#mi_primera_moto.detener()
#mi_primera_moto.consultar_precio()
mi_primera_moto.consultar_combustible()
mi_primera_moto.tanquear()
mi_primera_moto.consultar_combustible()
print()

#print("*** Moto imaginaria ***\n")
#moto_imaginaria.detener()
#moto_imaginaria.arrancar()
#moto_imaginaria.arrancar()
#moto_imaginaria.detener()
#moto_imaginaria.consultar_precio()
moto_imaginaria.consultar_combustible()
moto_imaginaria.tanquear()
moto_imaginaria.consultar_combustible()
#new test comment