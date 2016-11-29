import numpy as np
aux = 0
m = ((0.08,0.184,0.368,0.368),(0.632,0.368,0.0, 0.0),(0.264,0.368,0.368,0.0),(0.08,0.184,0.368,0.368))



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



# DEFINICAO PARA CALCULAR TEMPO DE RECORRENCIA ESPERADO QUANDO i!=j
def F_ij(matriz, n, i, j, exp):
    if exp == 1:
        return matriz[i][j]
    else:
        soma = 0
        for k in range(n):
            if k!=j:
                soma = soma + matriz[i][k]*F_ij(matriz, n, k, j, exp-1)
        return soma

# calcula a multiplicacao das matrizes
def exp_matriz(exp, matriz):
    p = matriz
    for i in range(int(exp)-1):
        p = np.dot(p,matriz)
    return p


if __name__ == '__main__':

    print 'MATRIZ TRANSICAO\n\n'
    print m

    n = len(m[0])
    verficica_estado = np.zeros((n, n))
    classificacao = np.zeros(n)

    print  'VERIFICAR COMUNICACAO ENTRE ESTADOS\n'
    exp = input ('NUMERO DE ITERACOES DA MATRIZ DE TRANSICAO: ')
    mat_exp = exp_matriz(exp, m)

    # VERIFICAR COMUNICACAO ENTRE ESTADOS
    for i in range (n):
        for j in range (n):
            comunicacao_estados(mat_exp, i, j)

    # passos = input('NUMERO DE PASSOS: ')
