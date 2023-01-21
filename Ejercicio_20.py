# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá 
# los elementos impares de una lista pasada por parámetro con filter y 
# realizará una suma de todos estos elementos obtenidos mediante reduce.

from functools import reduce

lista=[1,2,3,4,8,10,9,2]
listafiltrada=[]
def esImpar(lista):
    i=len(lista)-1
    while i>0:
        if lista[i]%2==0:
            listafiltrada.append(lista[i])
        i-=1
    return listafiltrada

filter(esImpar(lista), lista)

def reduce_array(a, b):
  return a + b

sum = reduce(reduce_array, listafiltrada)


print(sum)