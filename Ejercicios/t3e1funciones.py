#Función calcular el precio total aplicando descuento e IVA
def calcular_total_producto(precio, cantidad):
    precio_total = precio * cantidad
    return precio_total

def calcular_descuento(total, porcentaje_descuento):
    total_descuento = total - (total * porcentaje_descuento)/100
    return total_descuento

def calcular_iva(total, iva):
    total_iva = total + (total * iva)/100
    return total_iva

def calcular_operaciones():
    #Solicitud parámetros a la usuaria
    nombre_del_producto = input("¿Cuál es el nombre del artículo? ")
    precio_unidad = float(input("¿Cuál es el precio de 1 unidad? "))
    cantidad_a_comprar = int(input("¿Cuántos artículos llevas? "))
    descuento_en_porcentaje = float(input("¿Qué porcentaje de descuento tiene? "))
    iva_en_porcentaje = float(input("¿Qué porcentaje de IVA tiene? "))

    total_compra = calcular_total_producto(precio_unidad, cantidad_a_comprar)
    total_descuento = calcular_descuento(total_compra, descuento_en_porcentaje)
    total_iva = calcular_iva(total_descuento, iva_en_porcentaje)

    print("El total de la compra del producto " + nombre_del_producto + " es ", + total_iva), "euros"

calcular_operaciones()
