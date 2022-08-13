class Vehiculo:
    _encendido=False #si ponemos _ significa que no deberiamos modificarlo directamente (seria como los atributos privados, pero python no los tiene)

    def enciende(self):
        self._encendido=True

d=Vehiculo()
d.encendido=False
d.enciende()
print(d._encendido)

