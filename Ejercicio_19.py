# Crea un script que le pida al usuario una lista de países (separados por comas). 
# Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). 
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

from cmath import sin

def setLista(lista):
    listas = lista.split(',')
    return (",".join(sorted(list(set(listas)))))

print("Ingresa lista de países (separados por comas)")
lista= input()
print(setLista(lista))