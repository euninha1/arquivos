from arquivo.lib.interface import *

def arqExiste(nome):
    try:
        a = open(nome, 'rt') #ler o arquivo do texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #ler o arquivo de texto e se não existir criar
        a.close()
    except:
        print('Houve um erro na criação do arquivo! ')
    else:
        print(f'Arquivo {nome} criado com sucesso! ')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo! ')
    else:
        cabecalho('PESSOAS CADASTRADAS COM SUCESSO! ')
        print(a.read())