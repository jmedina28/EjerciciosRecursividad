# Palíndromos
def palindromo(contenido):
  contenido = contenido.lower()
  contenido = contenido.replace(' ', '')
  lista = list(contenido)
  listaresultado = list(reversed(contenido))
  if lista == listaresultado:
    print(lista, listaresultado)
    print("Esta frase/palabra es un palíndromo.")
  else:
    print(lista, listaresultado)
    print("No es palíndromo.")
contenido = str(input("Introduzca una frase/palabra: "))
palindromo(contenido)