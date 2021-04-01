def converte_entrada (texto_dos_numeros):
  lista = []
  texto = texto_dos_numeros
  y = (texto.split(' '))
  for x in y:
    lista.append (int(x))
  return lista

  
def processar_numeros (lista):
  soma = 0
  for x in lista:
    soma += x
  return (soma, len(lista))


def main (lista_dos_numeros):
  soma = soma_e_contagem [0]
  contagem = soma_e_contagem [1]
  media = soma / contagem
  return media


while input != "a" or "A" or "aloha":
  lista = converte_entrada (input (f"Coloque Sua Entrada Aqui: "))
  soma_e_contagem = processar_numeros (lista)
  media = main (lista)
  print (media)
  input (f"Envie 'A' ou 'aloha' para reiniciar: ")
  print ()
