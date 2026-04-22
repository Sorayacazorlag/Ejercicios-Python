nombre_producto = input("Introduzca el nombre del producto: ")
precio_unidad = input("Introduzca el precio de la unidad: ")
cantidad = input("Introduzca la cantidad de productos: ")
descuento_porcentaje = int(input("Introduzca el descuento en porcentaje: "))
iva_porcentaje = int(input("Introduzca el IVA en porcentaje: "))

def calcular_descuento(descuento_porcentaje, cienporcien):
    descuento = cantidad * precio_unidad * (descuento_porcentaje / cienporcien)
    return descuento

descuento_total = descuento (20, 100)

print("Descuento total: ", descuento)