#Pide a la usuaria cuántas notas desea introducir

numero_notas = int(input("¿Cuántas notas desea introducir?: "))

#Solicita cada nota

for i in range(numero_notas):
    nota = float(input("Introduce una nota: "))

#Suma todas las notas

suma = 0
suma = suma + nota

#Calcula y muestra la media

media = suma / numero_notas

print("La media es: ", media)




