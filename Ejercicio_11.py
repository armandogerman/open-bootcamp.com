# Escribe una función que pueda decirte si un número (número entero) es primo o no.
def primo(numero):
    i=2
    while i<numero:
        if numero%i==0:
            print("el numero:",numero,"no es primo")
            break
        i+=1
    if i==numero: 
        print("el numero",numero,"es primo!!!")
primo(3)
primo(7)
primo(10)
primo(8)
primo(11)