def multiplo_de_5 (N):
    for numero in range(int(N)):
        if numero % 5 == 0 and numero % 2 != 0:
            print(numero)


def lista_de_numeros (N):
    lista = []
    while len(lista) < N:
        lista.append (input(f"{len(lista) + 1}° número: "))
    return lista


def numero_de_numeros (lista):
    numero_de_numeros = 0
    for numero in lista:
        if numero > 5:
            numero_de_numeros += 1
    return numero_de_numeros


def menu ():
    print("Envie 'A' para imprimir 'PSG' \nEnvie 'B' para imprimir 'BAYERN' \nRetorne 'D' para encerrar \n")
    opcao = input("Digite sua opção: ")
    while opcao != 'D' or opcao != 'd':
        if opcao == 'A' or opcao == 'a':
            print("PSG")
        elif opcao == 'B' or opcao == 'b':
            print("BAYERN")
        else:
            break
        opcao = input("Digite sua opção: ")
