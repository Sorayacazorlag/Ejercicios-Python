#Pide a la usuaria un número entre el 1 y el 10
def elegir_numero():

    numero_elegido = int(input("Elige un número del 1 al 10: "))

    if numero_elegido == 4:
        print("¡ENHORABUENA!")
    else:
        print("LO SIENTO, OTRA VEZ SERÁ")

elegir_numero()
