# En este segundo ejercicio, tendréis que crear un archivo py y 
# dentro crearéis una clase Vehículo, haréis un objeto de ella, 
# lo guardaréis en un archivo y luego lo cargamos.

#serialización de los datos para agregar al fichero
import pickle 

class Vehiculo():
    def __init__(self, modelo, color, ruedas, puertas):
        self.modelo=modelo
        self.color=color
        self.ruedas=ruedas
        self.puertas=puertas
    def getModelo(self):
        return self.modelo

c=Vehiculo(1990,"negro",4,5)
namefile="datos.bin"

fo = open(namefile, "wb")
pickle.dump(c,fo)
fo.close()

fo = open(namefile,'rb')
Vehiculo2=pickle.load(fo)
fo.close()

print(type (Vehiculo2))
print(Vehiculo2.getModelo())


