# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
# Color
# Ruedas
# Puertas
# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
# Velocidad
# Cilindrada
# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

class Vehiculo():
    def __init__(self, color, ruedas, puertas):
        self.color=color
        self.ruedas=ruedas
        self.puertas=puertas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color=color
        self.ruedas=ruedas
        self.puertas=puertas
        self.velocidad=velocidad
        self.cilindrada=cilindrada

c=Coche("negro",4,5,200,1600)
print("Coche color:",c.color, "ruedas:",c.ruedas,"puertas:",c.puertas,"velocidad",c.velocidad,"cilindrada",c.cilindrada)
