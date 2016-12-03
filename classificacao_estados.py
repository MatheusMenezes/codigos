'''
    ALGORITMO PARA VERIFICAR CORRESPONDECIA ENTRE ESTADOS E
    CLASSIFICA-LOS SE RECORRENTES OU TRANSIENTE
    ALUNOS: MATHEUS CHAVES E DANILO NOGUEIRA
'''

import numpy as np

m = ((0.2,0.8,0),(0,0.3,0.7),(0,0,1))


def est_alcancavel(x, y, n):
    pos = 0
    pos_verif_estado = 0
    c = np.zeros(10000)
    if m[x][y] !=0:
        return 1
    else:
        c[pos] = x
        pos += 1
        for i in range(n):
            if m[x][i]!=0 and i!=y and x!=i:
                res = verifica_alcancavel(c,n, y,i, pos_verif_estado);
                if res:
                   for j in range (10000):
                        c[j] = 0;
                   return 1;

        for j in range (10000):
            c[j] = 0
        return 0

def verifica_alcancavel(c, n, y, x, pos_verif_estado):
    teste_estado = 0
    if m[x][y] != 0:
        return 1

    for i in range(n):
        if m[x][i]!=0.0 and i!=y:
            for j in range (10000):
                if c[j]==i:
                    teste_estado = 1
        if teste_estado != 1:
            c[pos_verif_estado]=i
            pos_verif_estado = pos_verif_estado+1
            r = verifica_alcancavel(c,n,y,i, pos_verif_estado)
            if r:
                j=0
                while True :
                    if c[j]==0:
                        c[j-1] == 0
                        break
                    j = j+1
                return 1
    j = 0
    while True:
        if c[j]==0:
            c[j-1]==0
            break
        j = j+1
    return 0


def recorrente (est, n):
    res = 1
    if m[est][est]==1:
        return 2

    for i in range (n):
        if i!=est:
            if est_alcancavel(est, i, n):
                if ~est_alcancavel(i, est, n):
                    res = 0
        if ~res :
            return 0;
    return 1;



def comunicacao_estados(p, i, j):
    if p[i][j] > 0.0:
        print str(i) + ' -> ' + str(j)
        verficica_estado[i][j] = 1.0
    elif p[j][i] > 0.0:
        print str(j) + ' -> ' + str(i)
        verficica_estado[j][i] = 1.0
    if verficica_estado[i][j] == 1 and verficica_estado[i][j] == verficica_estado[j][i]:
        print str(i) + ' <--> ' + str(j)
    elif verficica_estado[i][j] == 0 and verficica_estado[j][i] == 0:
        print str(i) + ' <-/-> ' + str(j)






# calcula a multiplicacao das matrizes
def exp_matriz(exp, matriz):
    p = matriz
    for i in range(int(exp)-1):
        p = np.dot(p,matriz)
    return p

def c_kolmogorov (n, passos, i, j):
    p_ij = 0
    if passos == 1:
        return m[i][j]

    for k in range (n):
        p_ij += m[i][k] * c_kolmogorov(n, passos - 1, k, j )
    return p_ij


if __name__ == '__main__':

    passos = 1

    print 'MATRIZ TRANSICAO\n'
    print m

    n = len(m[0])
    verficica_estado = np.zeros((n, n))
    classificacao = np.zeros(n)
    mat_chap = np.zeros((n, n))

    print  'VERIFICAR COMUNICACAO ENTRE ESTADOS\n'
    exp = input ('NUMERO DE ITERACOES DA MATRIZ DE TRANSICAO: ')
    mat_exp = exp_matriz(exp, m)

    # VERIFICAR COMUNICACAO ENTRE ESTADOS
    for i in range (n):
        for j in range (n):
            comunicacao_estados(mat_exp, i, j)

    print "\n\nCLASSIFICACAO DOS ESTADOS DA MATRIZ m: \n\n"


    print m
    for i in range(n):

        m_teste = recorrente(i, n)
        if m_teste == 1:
            print "O estado "+ str(i) + " E RECORRENTE\n"
        elif m_teste == 2:
            print "O estado "+ str(i) + " E ABSORVENTE\n"
        else:
            print "O estado "+ str(i) + " E TRANSIENTE\n"

    passos += 1

