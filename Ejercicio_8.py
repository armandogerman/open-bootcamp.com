# Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
# Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]
print("ingresa numero inicial")
numero_inicial=float(input())
print("ingresa numero final")
numero_final=float(input())
i=numero_inicial
impares=[]
while i <= numero_final:
    if i%2==0:
        i+=1
    else:
        impares.append(i)
        i+=2
print("los numeros impares son:",impares)