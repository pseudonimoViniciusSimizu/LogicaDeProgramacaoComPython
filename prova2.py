def exercicio1 ():
    list = []
    soma = 0
    while len(list) < 3:
        list.append (int(input(f"{len(list) + 1}° número: ")))
    for number in list:
        soma += number
    media = soma / len(list)
    return (f"Média do aluno é: {media}")

def exercicio2 (N):
    lista = []
    while len(lista) < N:
        lista.append (input(f"{len(lista) + 1}° número: "))
    return lista


def exercicio3 ():
    print("Envie 'A' para imprimir 'globo' \nEnvie 'B' para imprimir 'sbt' \nRetorne 'Z' para encerrar \n")
    opcao = input("Digite sua opção: ")
    while opcao != 'z' or opcao != 'Z':
        if opcao == 'A' or opcao == 'a':
            print("globo")
        elif opcao == 'B' or opcao == 'b':
            print("sbt")
        elif opcao == 'z' or opcao == 'Z':
            break
        else:
            print("Inválido")
        opcao = input("Digite sua opção: ")


def exercicio4 (media_dos_alunos):
    medias_inferiores = 0
    for media in media_dos_alunos:
        if media < 7:
            medias_inferiores += 1
    if medias_inferiores / len (media_dos_alunos) < 0.25:
        return ("Professor Coxa")  #Ou professor mano, não sei se coxa é bom ou ruim, entao coloquei assim mesmo
    else:
        return ("Professor Padrão")

