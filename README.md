<h1 align="center">Recursividad</h1>

<h3 align="center">Perfil de GitHub del autor de este proyecto:</h3>

1. [@jmedina28](https://github.com/jmedina28)

---
En este [repositorio](https://github.com/jmedina28/EjerciciosRecursividad) quedan resueltos los ejercicios de recursividad. Para llevar a cabo el proyecto me he documentado a través de los ejemplos dados y la teoría que se encuentra en el campus virtual.

## Ejercicio 1: Búsqueda por dicotomía en una tabla ordenada

El código empleado para resolverlo es el siguiente:

```python
# Búsqueda por dicotomía en una tabla ordenada
listainicial = ["perro","gato","hamster","koala","tigre","ciervo","jabalí","conejo","cabra","ratón","rata","serpiente","hormiga","lobo","lince"]
lista = sorted(listainicial) # Ordeno la lista
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
```

## Ejercicio 2: Palíndromos

El código empleado para resolverlo es el siguiente:
 
 ```python
 # Palíndromos
def palindromo(contenido):
  a,b = 'áéíóúüñÁÉÍÓÚÜ','aeiouunAEIOUU'
  tilde = str.maketrans(a,b)
  contenido = contenido.lower() # Convierto el texto en minúsculas.
  contenido = contenido.replace(' ', '') # Quito los espacios.
  contenido = contenido.translate(tilde) # Elimino las tildes.
  lista = list(contenido) # Convierto en el contenido en una lista.
  listaresultado = list(reversed(contenido)) # Invierto la lista.
  if lista == listaresultado: # Comparo el contenido original con el inverso.
    print("Esta frase/palabra/número es un palíndromo.")
  else:
    print("No es palíndromo.")
contenido = str(input("Introduzca una frase/palabra/número: "))
palindromo(contenido)

```
## Ejercicio 3: La bandera de Dijkstra

El código empleado para resolverlo es el siguiente:
 
 ```python
# La bandera de Dijkstra:
bandera, red, green, blue = ["R","B","G","G","G","B","R","R","B","B","R","G","R","R","B","R","B","G","G","G","R","B"], [], [], []   # Creo las listas que posteriormente fusionaré en una.
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
```
