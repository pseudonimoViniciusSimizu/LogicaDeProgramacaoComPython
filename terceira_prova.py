from random import randint

def calcula_max(elem1, elem2):
    if elem1 > elem2:
        return elem1
    else:
        return elem2
      

def calcula_media(lista):
  soma = 0
  for i in lista:
    soma += i
  media = soma / len(lista)
  return media


def maior_media(lista):
  media1 = calcula_media(lista[:3])
  media2 = calcula_media(lista[-3:])
  return calcula_max(media1, media2)
  
  
def saida_txt():
  with open("./input.txt", 'r') as file:
    lista = list(map(lambda x: int(x), file.readlines()))
    minimo = min(lista)
    maximo = calcula_max(lista)
    media = calcula_media(lista)
    file.close()
  with open("saida.txt", 'w') as file:
    file.write("Minimo\t\t{}\n".format(minimo))
    file.write("Maximo\t\t{}\n".format(maximo))
    file.write("Media\t\t{}".format(media))
    file.close()
    
    
def cria_matriz(num_linhas, num_colunas):
  matriz = []
  for i in range(num_linhas):
      linha = []
      for j in range(num_colunas):
          linha.append(randint(0, 10))
      matriz.append(linha)
  return matriz
      
