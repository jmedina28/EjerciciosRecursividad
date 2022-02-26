lista = ["perro","gato","hamster","koala","tigre","ciervo","jabalí","conejo","cabra"]
print(lista)
def dicotomia(palabra, longitud):
  if palabra == lista[round(longitud/2)]:
    print("La palabra es " + str(lista[round(longitud/2)]))
    if longitud >= 0:
      print("Se encuentra en el punto " + str(round(longitud/2)))
    else:
      print("Se encuentra en el punto " + str(round(longitud/2)+len(lista)))
  else:
    dicotomia(palabra, longitud-1)
dicotomia(str(input("Introduzca una palabra que desee localizar de la lista dada: ")), len(lista))