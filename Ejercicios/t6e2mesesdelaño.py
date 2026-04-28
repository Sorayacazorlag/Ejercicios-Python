#Crea una lista con los 12 meses del año

meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

#Pide a la usuaria un número del 1 al 12

numero = int(input("Elige un número del 1 al 12: "))

#Muestra el mes correspondiente
#Si el mes es junio, muestra el mensaje 'EL MEJOR MES'

if numero >= 1 and numero <= 12:
    mes = meses[numero - 1]
    print("El mes es: ", mes)

    if mes == "junio":
        print("EL MEJOR MES")

else:
    print("Número no valido")