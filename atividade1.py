def converte_entrada (texto_dos_numeros):
  lista = []
  texto = texto_dos_numeros
  y = (texto.split(' '))
  for x in y:
    x = int(x)
    lista.append (x)
  return lista
  
def processar_numeros (lista):
  i = 0
  soma = 0
  while len(lista) > i:
    soma += lista [i]
    i += 1
  return (soma, i)

def main (lista_dos_numeros):
  soma = soma_e_contagem [0]
  contagem = soma_e_contagem [1]
  media = soma / contagem
  return media

while input != "a" or "A":
  lista = converte_entrada (input (f"Coloque Sua Entrada Aqui "))
  soma_e_contagem = processar_numeros (lista)
  media = main (lista)
  print (media)
  input (f"Envie 'A' para reiniciar ")
  print ()
