#Convertir euros a dólares y libras

def convertir_euros_a_dolares(cantidad_euros):
    resultado = cantidad_euros * 1.1
    return resultado

def convertir_euros_a_libras(cantidad_euros):
    resultado = cantidad_euros * 0.87
    return resultado

#Pide a la usuaria la cantidad de euros a cambiar

def conversor():
    cantidad_en_euros = float(input("¿Cuántos euros quiere cambiar? "))

    print("Conversión a dólares: ")
    cantidad_en_dolares = convertir_euros_a_dolares(cantidad_en_euros)
    print(cantidad_en_dolares)

    print("Conversión a libras: ")
    cantidad_en_libras = convertir_euros_a_libras(cantidad_en_euros)
    print(cantidad_en_libras)

conversor()