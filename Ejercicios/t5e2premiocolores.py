#Pide a la usuaria 5 veces que introduzca un color
#Si la usuaria introduce el color azul, muestra el premio conseguido.
#Si no, dile que pruebe otro color

for i in range(5):
    color = input("Introduce un color: ").lower()

    if color == "azul":
        print("¡HA CONSEGUIDO EL PREMIO!")
        break;
    else:
        print("Prueba otro color")


