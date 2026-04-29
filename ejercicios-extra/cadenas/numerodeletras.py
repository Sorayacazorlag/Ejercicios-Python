#Preguntar nombre al usuario
#Imprimir <NOMBRE> tiene <n> letras (<NOMBRE>: usuario en mayúsculas; <n>: número de letras del nombre)

nombre = input("¿Cómo te llamas?: ")

print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")

