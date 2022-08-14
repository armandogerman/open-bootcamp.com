# En este segundo ejercicio, tendréis que crear un programa que tenga una clase 
# llamada Alumno que tenga como atributos su nombre y su nota. Deberéis de definir
# los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con
# el resultado de la nota y si ha aprobado o no.

class Alumno():

    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def imprimealumno(self):
        print("Nombre:",self.nombre,"Nota:",self.nota)

    def aprueba(self):
        if self.nota>=7:
            print("aprueba")
        else:
            print("no aprueba")

a=Alumno()
b=Alumno()

a.inicializar("Juan",3)
b.inicializar("jorge",8)
a.imprimealumno()
a.aprueba()
b.imprimealumno()
b.aprueba()

