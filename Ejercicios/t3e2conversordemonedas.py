cantidad_euros = float(input("Introduzca una cantidad en euros: "))

def calcular_conversiones (conversion_dolares, conversion_libras):
    dolares = conversion_dolares * cantidad_euros
    libras = conversion_libras * cantidad_euros
    return dolares, libras

dolares, libras = calcular_conversiones (1.1, 0.87)
print("Dolares: ", dolares)
print("Libras: ", libras)
