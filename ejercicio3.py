# Bandera:
bandera, red, green, blue = ["R","B","G","G","G","B","R","R","B","B","R","G","R","R","B"], [], [], []   # Creo las listas que posteriormente fusionaré en una.
print("A continuación se va a ordenar la siguiente bandera: " + str(bandera))
def ordenrgb(bandera, posicion):
  if posicion < len(bandera):
    if bandera[posicion] == "R":
      red.append(bandera.pop(posicion))
    elif bandera[posicion] == "B":
      blue.append(bandera.pop(posicion))
    elif bandera[posicion] == "G":
      green.append(bandera.pop(posicion))
    ordenrgb(bandera, posicion)
  else:
    print("La bandera ordenada queda tal que así: "+ str(red + green + blue))
ordenrgb(bandera, 0)