<h1 align="center">Recursividad</h1>

<h3 align="center">Perfil de GitHub del autor de este proyecto:</h3>

1. [@jmedina28](https://github.com/jmedina28)

---
En este [repositorio](https://github.com/jmedina28/EjerciciosRecursividad) quedan resueltos los primeros ejercicios de introducción a la algorítmica. Para llevar a cabo el proyecto me he documentado a través de los ejemplos dados y la teoría que se encuentra en el campus virtual.

## Ejercicio 1: Búsqueda por dicotomía en una tabla ordenada

El código empleado para resolverlo es el siguiente:

```python

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

```
