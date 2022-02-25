# Palíndromos
def palindromo(contenido):
  a,b = 'áéíóúüñÁÉÍÓÚÜÑ','aeiouunAEIOUUN'
  tilde = str.maketrans(a,b)
  contenido = contenido.lower()
  contenido = contenido.replace(' ', '')
  contenido = contenido.translate(tilde)
  lista = list(contenido)
  listaresultado = list(reversed(contenido))
  if lista == listaresultado:
    print("Esta frase/palabra/número es un palíndromo.")
  else:
    print("No es palíndromo.")
contenido = str(input("Introduzca una frase/palabra/número: "))
palindromo(contenido)