# Bandera:
bandera = ["R","B","G","G","G","B","R","R","B","B","R","G","R","R","B"]
print("A continuación se va a ordenar la siguiente bandera: " + str(bandera))
red, green, blue  = [], [], []

def ordenrgb(bandera, posicion):
  # Creo las listas que posteriormente fusionaré en una.

  if bandera[posicion] == "R" and posicion+1 < len(bandera):
    red.append(bandera.pop(posicion))
    print(red)
    ordenrgb(bandera, posicion)
  elif bandera[posicion] == "B" and posicion+1 < len(bandera):
    blue.append(bandera.pop(posicion))
    print(blue)
    ordenrgb(bandera, posicion)
  elif bandera[posicion] == "G" and posicion+1 < len(bandera):
    green.append(bandera.pop(posicion))
    print(green)
    ordenrgb(bandera, posicion)
  else:
    total = red + green + blue
    print(total)
  
ordenrgb(bandera, 0)
  
  
  