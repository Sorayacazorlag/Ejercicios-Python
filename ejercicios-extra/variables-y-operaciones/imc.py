#Preguntar peso de la usuaria (en kg)
#Preguntar estatura de la usuaria (en m)
#Calcula el imc y almacenalo en una variable
#Imprime "tu imc es <imc> donde <imc> es el imc calculado redondeado con 2 decimales"

peso = float(input("¿Cuánto pesa en kg?: "))

estatura = float(input("¿Cuánto mide en m?: "))

imc = round(peso / (estatura ** 2), 2)

print("Tu imc es: ", imc)
