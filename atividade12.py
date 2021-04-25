from random import randint


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
    print( list ( filter ( lambda x: x % 2 == 0, lista_numeros )))


def exer6 (lista_numeros):
    print( sum ( list ( filter ( lambda x: x >= 4, lista_numeros))))


def exer7 (lista_numeros):
    print( sum ( lista_numeros ) / len ( lista_numeros ))


def exer8 (lista_numeros):
    print( "|".join ( list ( map ( lambda x: str (x), lista_numeros ))))


def exer9 (lista_numeros):
    ordened_list = sorted( lista_numeros )
    # aqui também


def exer10 (lista_numeros):
    disordened_list = sorted( lista_numeros , reverse = True )
    # preciso nem escrever né :)


def exer11 (segunda_lista_numeros):
    print( segunda_lista_numeros [:] )


def exer12 (segunda_lista_numeros):
    print( segunda_lista_numeros [ :3 ])


def exer13 (segunda_lista_numeros):
    print( sorted (segunda_lista_numeros) [ :2 ])


def exer14 (segunda_lista_numeros):
    print( sorted ( segunda_lista_numeros, reverse = True )[ :2 ])


def exer15 ():
    print ( list ( x+1 for x in range(10) ))


def exer16 ():
    print ( list ( x * 2 for x in range(11) ))


def exer17 ():
    print( list ( randint( 0, 100) for x in range(19) ))

lista_numeros = [ 3, 8, 9, 1, 0, 2 ]
segunda_lista_numeros = [ 4, 5, 2, 0, 9 ]
