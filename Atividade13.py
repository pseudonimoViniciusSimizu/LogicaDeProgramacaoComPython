import os
import json
import requests

def exer1 ():
    with open( os.environ ["HOMEPATH"] + "/Downloads" + "/teste.txt", "r") as file:
        print ( file.read())
        file.close()


def exer2 ():
    with open( "./precos.txt", "r" ) as file:
        precos = list ( map ( lambda preco: float (preco.strip("\n")), file.readlines()))
        print( sum ( precos ) / len ( precos ))
        file.close()


def exer3 ():
    with open( os.environ ["HOMEPATH"] + "/arquivo.txt", "w" ) as file:
        for elemento in "Vinicius Simizu".split():
            file.write ( elemento + "\n" )
        file.close()


def exer4 ():
    print ( requests.get ("https://jsonplaceholder.typicode.com/todos/1").text )


def exer5 ():
    dicionario = json.loads ( requests.get ("https://jsonplaceholder.typicode.com/todos/1").text )
    print ( dicionario ["title"] )


def exer6 ():
    dicionarios = json.loads ( requests.get ("https://jsonplaceholder.typicode.com/posts").text )
    for discionario in dicionarios:
        print ( discionario ["body"] + "\n" )
