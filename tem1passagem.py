'''
    Atividade Desenvolvida compor segunda nota
        da Disciplina de Processos Estocasticos
    Topico da aula: Tempo de primeira passagem
'''

import numpy as np

'''
P = |0.08   0.184   0.368   0.368|
    |0.632  0.368   0.0     0.0  |
    |0.264  0.368   0.368   0.0  |
    |0.08   0.184   0.368   0.368|


P1 = MATRIZ DOS ESTADOS ESTAVEIS
P1= |0.92   -0.632  -0.264  -0.08   0|
    |-0.184  0.632  -0.368  -0.184  0|
    |-0.368  0       0.632  -0.368  0|
    |-0.368  0       0       0.632  0|
    |1       1       1       1      1|

'''

# SOLUCAO DE SISTEMA DE EQUACOES LINEARES
def solve_eq(v):

    A = []
    b = []
    nrows = len(v)
    ncols = len(v[0])
    if(nrows == ncols):
        for linha in v:
            A.append(linha[0:len(v)-1])
            b.append(linha[len(v)-1])
    else:
        for linha in v:
            A.append(linha[0:len(v)])
            b.append(linha[len(v)])

    print 'MATRIX = \n'+str(v)
    print 'A = \n'+str(A)
    print 'b = \n'+str(b)


    res = np.linalg.lstsq(A, b)
    print '\nresposta (em ordem de entrada) = \n'+str(res[0])
    return res


# DEFINICAO PARA CALCULAR TEMPO DE RECORRENCIA ESPERADO QUANDO i!=j
def F_ij(n, i, j, exp):
    if exp == 1:
        return P[i][j]
    else:
        soma = 0
        for k in range(n):
            if k!=j:
                soma = soma + P[i][k]*F_ij(n, k, j, exp-1)
        return soma


# DEFINICAO PARA CALCULAR TEMPO DE RECORRENCIA ESPERADO QUANDO i=j
def F_jj(j):
    vaj_j = 0
    res = solve_eq(P1)
    sol = 1/res[0][j]
    print "\nRESPOSTA: " + str(sol)

# TEMPO DA PRIMEIRA PASSAGEM ESPERADO
# GERA UM SISTEMA DE EQUACOES LINEARES NO FORMATO MATRICIAL PARA SER RESOLVIDA
# AS VARIAVEIS SAO COLOCADAS DE FORMA DECRESCENTE NA MATRIZ EX:
#
#   |aM30 bM20 cM10| = |1|
#   |dM30 eM20 fM10| = |1|
#   |gM30 hM20 iM10| = |1|
#
#   ONDE M30 EH O TEMPO DA PRIMEIRA PASSAGEM ESPERADO Mij

def _U(n,i,j):
    print "\nTEMPO DA PRIMEIRA PASSAGEM ESPERADO\n"
    posx = 0
    for x in range(n-1,-1,-1): #preciso descobrir n-1 variaveis (i!=j)
        posy = 0
        if(x!=j):
            for y in range(n-1,-1,-1): # y = n .. 0
                if (y != j):
                    if x - y == 0:
                        v[posx][posy] = 1 - P[x][y]
                    else:
                        v[posx][posy] = -P[x][y]
                    posy = posy+1
            posx = posx + 1
    for k in range (n-1):
        v[k][len(P)-1] = 1
    solve_eq(v)



if __name__ == '__main__':
    P = ((0.08,0.184,0.368,0.368),(0.632,0.368,0.0, 0.0),(0.264,0.368,0.368,0.0),(0.08,0.184,0.368,0.368))
    P1 = ((0.92, -0.632, -0.264, -0.08, 0),(-0.184, 0.632, -0.368, -0.184, 0),(-0.368, 0, 0.632, -0.368, 0),(-0.368, 0, 0, 0.632, 0),(1,1,1,1,1))
    print "MATRIZ P:\n"
    print P
    print "\nTEMPO DE RECORRENCIA ESPERADO QUANDO i!=j\n"
    print F_ij(len(P), 3, 0, 3)
    print "\nTEMPO DE RECORRENCIA ESPERADO QUANDO i=j\n"
    F_jj(1)
    v = np.zeros((len(P)-1,len(P)))
    _U(len(P), 1, 0)

