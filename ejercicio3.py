# Bandera:
bandera = ["R","B","G","G","G","B","R","R","B","B","R","G","R","R","B"]
print("A continuación se va a ordenar la siguiente bandera: " + str(bandera))
def ordenrgb(bandera, posicion):
  # Creo las listas que posteriormente fusionaré en una.
  red = []
  green = []
  blue = []
  total = [red,green,blue]
  if bandera[posicion] == "R":
    red.append("R")
    ordenrgb(bandera, posicion+1)

  print(total)
  
  
  
ordenrgb(bandera, 0)
  
  
  