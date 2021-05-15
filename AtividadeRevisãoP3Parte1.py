from random import randint

def minimo_de_3():
    # Definir lista
    lista = []

    # Definir menor numero
    less_number = 0

    # Loop para definir o 1°número rejeitando tipo char ou string
    while len(lista) < 1:
        try:
            less_number = float(input("1°Número: "))
            lista.append(0)
        except:
            print("ERROR, SÓ ACEITAMOS NÚMEROS!")

    # Coleta de mais 2 números rejeitando tipo char ou string
    while len(lista) < 3:
        try:
            number = float(input(f"{len(lista) + 1}°Número: "))

            # Se o número for menor que "less_number", atualiza-a
            if number < less_number:
                less_number = number
            lista.append(0)
        except:
            print("ERROR, SÓ ACEITAMOS NÚMEROS!")

    # Menor dos 3 números = less_number


def meu_minimo(lista):

    # Define o número inicial
    less_number = lista[0]

    # Verifica o menor número da lista e guarda no "less_number"
    for i in lista:
        if i < less_number:
            less_number = i

    # Retorna o menor número
    return less_number


def minha_soma(lista):

    # Define a variável soma
    soma = 0

    # Soma a lista e guarda na "soma"
    for i in lista:
        soma += i

    # Retorna a soma
    return soma


def meu_sort(lista):

    # Repete a ordenação até organiza-la completamente
    for i in range(len(lista)):

        # Ordena crescentemente a lista em 1 casa
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp

    # Retorna a lista ordenada
    return lista


def calcula_media():

    # Calcula a media
    media = minha_soma(meu_sort([4, 5, 0, 7, 9, 5])[-2:]) / 2

    # Imprime a media no terminal
    print(media)


def calcula_media_simples():

    # Calcula a media
    media = sum(sorted([4, 5, 0, 7, 9, 5])[-2:]) / 2

    # Imprime a media no terminal
    print(media)


# Mapas, Filtros e Join

def exer1():

    # Imprime a lista de números pares
    print(list(filter(lambda x: x % 2 == 0, [3, 2, 4, 8, 9, 0])))


def exer2():

    # Imprime os números da lista maiores que 3
    print(list(filter(lambda x: x > 3, [3, 2, 4, 8, 9, 0])))


def exer3():

    # Trasforma lista de números tipo string em int
    print(list(map(lambda x: int(x), ['3', '8', '2', '9', '0'])))


def exer4():

    # Separa uma lista de números com ';' entre eles
    print(';'.join(list(map(lambda x: str(x), [3, 2, 4, 8, 9, 0]))))


def exer5():

    # Imprime a média da lista
    print(sum(map(lambda x: int(x), [3, 2, 4, 8, 9, 0])) / len([3, 2, 4, 8, 9, 0]))


def exer6():

    # Imprime a média das notas de João
    print("A média da nota de {} é igual a {:.2f}".format("Joao,3,4,8,5,4,10".split(',')[0], sum(map(lambda x: int(x), "Joao,3,4,8,5,4,10".split(',')[1:])) / 6))


# Lista em uma linha

def exerc1():

    # Cria uma lista de 10 números 1
    lista = list(1 for i in range(10))


def exerc2():

    # Cria uma lista de 4 números aleatórias
    lista = list(randint(0, 10) for i in range(4))


def exerc3():

    # Cria uma lista de 0 (inclusive) a 9 (inclusive)
    lista = list(range(10))


def exerc4():

    # Cria uma lista de 4 números por input do usuário
    lista = list(float(input(f"{i + 1}°Número: ")) for i in range(4))
