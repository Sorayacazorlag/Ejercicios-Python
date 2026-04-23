#Precio artículos
camiseta = 10
sudadera = 20.5
gorra = 5.5

cantidad_camisetas = int(input("¿Cuántas camisetas llevas? "))
cantidad_sudaderas = int(input("¿Cuántas sudaderas llevas? "))
cantidad_gorras = int(input("¿Cuántas gorras llevas? "))

precio_total_camisetas = cantidad_camisetas * camiseta
precio_total_sudaderas = cantidad_sudaderas * sudadera
precio_total_gorras = cantidad_gorras * gorra

total_compra = precio_total_camisetas + precio_total_sudaderas + precio_total_gorras
total_mas_21iva = total_compra + (total_compra * 0.21)

print("Precio camiseta" , camiseta)
print("Precio sudadera" , sudadera)
print("Precio gorra" , gorra)


print("Precio total sin IVA" , total_compra)
print("Precio total con 21%IVA" , total_mas_21iva)

