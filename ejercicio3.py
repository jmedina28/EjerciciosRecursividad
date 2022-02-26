# Bandera:
bandera = ["R","B","G","G","G","B","R","R","B","B","R","G","R","R","B"]
print("A continuación se va a ordenar la siguiente bandera: " + str(bandera))
def ordenrgb(bandera, posicion):
  # Creo las listas que posteriormente fusionaré en una.
  red = []
  green = []
  blue = []
  if bandera[posicion] == "R" and posicion < len(bandera):
    red.append("R")
    print(red)
    ordenrgb(bandera, posicion+1)
  elif bandera[posicion] == "G" and posicion < len(bandera):
    green.append("G")
    ordenrgb(bandera, posicion+1)
    print(green)
  elif bandera[posicion] == "B" and posicion < len(bandera):
    blue.append("B")
    ordenrgb(bandera, posicion+1)
  
ordenrgb(bandera, 0)
  
  
  