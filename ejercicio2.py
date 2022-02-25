# Palíndromos
def palindromo(contenido):
  contenido = contenido.lower()
  contenido = contenido.replace(' ', '')
  lista = list(contenido)
  listaresultado = list(reversed(contenido))
  if lista == listaresultado:
    print("Esta frase/palabra/número es un palíndromo.")
  else:
    print("No es palíndromo.")
contenido = str(input("Introduzca una frase/palabra/número: "))
palindromo(contenido)