camiseta = 10
sudadera = 20.5
gorra = 5.5

cantidad_camisetas = int(input("¿Cuántas camisetas llevas?"))
cantidad_sudaderas = int(input("¿Cuántas sudaderas llevas?"))
cantidad_gorras = int(input("¿Cuántas gorras llevas?"))

total_compra = (cantidad_camisetas * camiseta) + (cantidad_sudaderas * sudadera) + (cantidad_gorras * gorra)
total_mas_21iva = total_compra * 1.21

print("Precio camiseta" , camiseta)
print("Precio sudadera" , sudadera)
print("Precio gorra" , gorra)


print("Precio total sin IVA" , total_compra)
print("Precio total con 21%IVA" , total_mas_21iva)

