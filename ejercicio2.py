# Palíndromos
def palindromo(contenido):
  contenido = contenido.lower()
  lista = list(contenido)
  listaresultado = list(reversed(contenido))
  if lista == listaresultado:
    print(lista, listaresultado)
    print("Esta palabra es un palíndromo.")
  else:
    print(lista, listaresultado)
    print("No es palíndromo.")
contenido = str(input("Introduzca una palabra: "))
palindromo(contenido)