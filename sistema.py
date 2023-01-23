from arquivo.lib.arquivo import *
from arquivo.lib.interface import *
from time import sleep

arq = 'cadastro.txt'

if not arqExiste(arq):
    criarArquivo(arq)
else:
    print('Arquivo não encontrado! ')
    criarArquivo(arq)

while True:
    resp = menu(['Listar pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resp == 1:
        #Opção de listar o contúdo de um arquivo!
        lerArquivo(arq)
    elif resp == 2:
        cabecalho('Opção 2')
    elif resp == 3:
        cabecalho('Saindo do sistema... Tchau!')
        break
    else:
        print('ERRO! Digite uma opção válida!')
    sleep(1)
