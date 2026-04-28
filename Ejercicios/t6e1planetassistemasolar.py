#Crea una lista con 8 planetas del sistema solar

planetas = ["mercurio", "venus", "tierra", "marte", "jupiter", "saturno", "urano", "neptuno"]

#Pide a la usuaria un número del 1 al 8

numero = int(input("Introduzca un número del 1 al 8: "))

#Si el número es inválido, muestra mensaje de error

if numero >= 1 and numero <= 8:
    print("El planeta es: ", planetas[numero - 1])
else:
    print("Número no válido")



