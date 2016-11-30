import numpy as np

m = ((1,0),(1,0))
mdc = 0
aux1 = 0
aux2 = 0

def alcancavel(x, y, n):
    global aux1
    c = np.zeros(1000)
    if m[x][y] !=0:
        return 1
    else:
        print aux1
        c[aux1] = x
        aux1 += 1
        for i in range(n):
            if m[x][i]!=0 and i!=y and x!=i:
                res = teste_alcancavel(c,n, y,i);
                if res:
                   for j in range (1000):
                        c[j] = 0;
                   return 1;

        for j in range (1000):
            c[j] = 0
        return 0

def teste_alcancavel(c, n, y, x):
    flag = 0
    global mdc, aux2
    if m[x][y] != 0:
        return 1

    for i in range(n):
        if m[x][i]!=0 and i!=y:
            for j in range (n*n):
                if c[j]==i:
                    flag = 1
                    mdc = mdc + 1
        if flag != 1:
            c[aux2]=i
            aux2 = aux2+1
            r = teste_alcancavel(c,n,y,i)
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
        return 1

    for i in range (n):
        if i!=est:
            if alcancavel(est, i, n):
                if ~alcancavel(i, est, n):
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

    print 'MATRIZ TRANSICAO\n\n'
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

    while passos!=9:
        for i in range (n):
            for j in range (n):
                mat_chap[i][j] = c_kolmogorov(n, passos, i, j);

        m = mat_chap
        for i in range(n):

            m_teste = recorrente(i, n)
            if m_teste == 1:
                print "\nNa geracao "+ str(passos) +" - O estado "+ str(i) + " E RECORRENTE\n"
            else:
                print "\nNa geracao "+ str(passos) +" - O estado "+ str(i) + " E TRANSIENTE\n"
                print "\nMDC = "+str(mdc)+"\n"
        passos += 1

