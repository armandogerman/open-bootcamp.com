# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, 
# lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.

namefile="archivo.txt"
print("Create file")
# Open a file
fo = open(namefile, "wb")
print ("Name of the file: ", fo.name)

# Close opened file
fo.close()

print("Write file") 

# Open a file
fo = open(namefile, "w")
fo.write( "Python is a great language.\nYeah its great!!\n")

# Close opend file
fo.close()

print("Done")