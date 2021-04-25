def exer1():
    numbers_list = []
    while len(numbers_list) < 3:
        numbers_list.append(int(input(f"{len(numbers_list) + 1}° Number: ")))
    print(sorted(numbers_list)[-1:])


def exer2():
    lista_de_palavras = ("Eu sou um aluno feliz".split())
    # imagino eu que não era para imprimir e nem retornar :)


def exer3():
    list_sum = sum([3, 6, 3, 2, 1])
    # aqui também


def exer4():
    converted_list = (" ".join(["seu", "joao", "esta", "aqui"]))
    # esse também


def exer5 (lista_numeros):
    pairs_list = []
    for number in lista_numeros:
        if number % 2 == 0:
            pairs_list.append(number)
    print(pairs_list)


def exer6 (lista_numeros):
    list_min_4 = []
    for number in lista_numeros:
        if number >= 4:
            list_min_4.append(number)
    print(sum(list_min_4))


def exer7 (lista_numeros):
    print(sum(lista_numeros) / len(lista_numeros))


def exer8 (lista_numeros):
    text_list = []
    for number in lista_numeros:
        text_list.append( str ( number))
    print ("|".join(text_list))


def exer9 (lista_numeros):
    ordened_list = sorted( lista_numeros )
    # aqui também


def exer10 (lista_numeros):
    disordened_list = sorted( lista_numeros , reverse = True )
    # preciso nem escrever né :)

lista_numeros = [3, 8, 9, 1, 0, 2]
