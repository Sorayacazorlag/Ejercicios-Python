def escoger_color():

    rojo = "Arde con lo que amas y deja que tu energía lo cambie todo"
    verde = "Todo lo que cuidas hoy, florece mañana"
    azul = "Respira, suelta y confía: todo llega en su momento"
    amarillo = "Sonríe, que lo mejor todavía está por venir"
    morado = "Crea, imagina y deja que tu esencia marque el camino"

    color = input("Escoge un color de los siguientes: rojo, verde, azul, amarillo, morado: ").lower()
    print("Ha escogido el siguiente color: ", color)

    if color == "rojo":
        print("Arde con lo que amas y deja que tu energía lo cambie todo")
    elif color == "verde":
        print("Todo lo que cuidas hoy, florece mañana")
    elif color == "azul":
        print("Respira, suelta y confía: todo llega en su momento")
    elif color == "amarillo":
        print("Sonríe, que lo mejor todavía está por venir")
    elif color == "morado":
        print("Crea, imagina y deja que tu esencia marque el camino")
    else:
        print("Escoge un color")

escoger_color()