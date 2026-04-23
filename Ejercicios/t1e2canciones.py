#Pide a la usuaria que intrduzca la siguiente información sobre su canción favorita

cancion_favorita = input("¿Cuál es tu canción favorita? ")
artista = input("¿De qué artista es? ")
album = input("¿Pertenece a algún álbum? Si la respuesta es si, ¿a cuál? ")
anyo_lanzamiento = int(input("¿Cuál fue el año de lanzamiento? "))
duracion = float(input("¿Cuánto dura en segundos? "))
videoclip = input("¿Tiene videoclip? ")

print("Mi canción favorita es", cancion_favorita)
print("Pertenece al artista/banda", artista)
print("Pertenece al álbum", album)
print("Salió en el año", anyo_lanzamiento)
print("Tiene una duración de", duracion)
print("¿Tiene videoclip?", videoclip)

#Pide a la usuaria que introduzca la siguiente información sobre la canción que menos le gusta
peor_cancion = input("¿Cuál es la canción que menos te gusta? ")
peor_artista = input("¿De qué artista es? ")
peor_album = input("¿Pertenece a algún álbum? Si la respuesta es si, ¿a cuál? ")
peor_anyo_lanzamiento = int(input("¿Cuál fue el año de lanzamiento? "))
peor_duracion = float(input("¿Cuánto dura en segundos? "))
peor_videoclip = input("¿Tiene videoclip? ")

print("La canción que menos me gusta es", peor_cancion)
print("Pertenece al artista/banda", peor_artista)
print("Pertenece al álbum", peor_album)
print("Salió en el año", peor_anyo_lanzamiento)
print("Tiene una duración de", peor_duracion)
print("¿Tiene videoclip?", peor_videoclip)