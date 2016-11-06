'''
    Desenvolvido por Matheus Chaves Menezes para compor segunda nota
        da Disciplina de Processos Estocasticos
    Resolucao de Sistema de Equacoes Lineares de varias variaveis utilizando numpy
    Matriz A representa a matriz dos coeficientes
    Vetor B representa as igualdades das operacoes com os coeficientes
'''

import numpy as np

print '\n\tAlgoritmo para resolver sistemas de equacoes lineares com muitas variaveis.'
print '\tA matriz deve ser lida de um arquivo'
print '\tNecessario entrar com o nome do arquivo para continuar\n'
print 'Entrada do tipo \nax -by z d1\n-ex fy -gz d2'
print 'Solucao no formato \n[x y z]'

def load_file(file):
    return [[float(x) for x in (line.split())] for line in file]
name = raw_input("INFORME O LOCAL E NOME DO ARQUIVO (EX: ./dados/matrix.txt): ")
f = open(str(name),'r')
C = load_file(f)
A = []
b = []
nrows = len(C)
ncols = len(C[0])
if(nrows == ncols):
    for linha in C:
        A.append(linha[0:len(C)-1])
        b.append(linha[len(C)-1])
else:
    for linha in C:
        A.append(linha[0:len(C)])
        b.append(linha[len(C)])

print 'MATRIX C = \n'+str(C)
print 'A = \n'+str(A)
print 'b = \n'+str(b)


res = np.linalg.lstsq(A, b)
print '\nresposta (em ordem de entrada) = \n'+str(res[0])


