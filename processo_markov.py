import numpy as np

# verifica se soma vetor igual a 1. Serve tanto para probabilidade quanto porcentagem
def verify(a):
    soma = 0
    for elem in a:
        soma = soma + elem
    if soma != 1.0:
        return False
    else:
        return True

def vetor_ini(n):
    vetor = list()
    print 'Entre com o vetor de inicializacao: '

    for i in range(int(n)):
        porc = input("pos[%d]: " %i) #porcentagem
        vetor.append(porc)

    print 'Vetor de inicialicazao: ',vetor
    return vetor


def matriz_transacao(n):
    matriz = np.zeros((n, n))
    for x in range(int(n)):
        for y in range(int(n)):
            print ('matriz['+str(x)+']['+str(y)+']')
            matriz[x][y] = input()
    return matriz

def exp_matriz(h, m):
    p = m
    for i in range(int(h)-1):
        p = p.dot(m)
    return p

def multi_exp_ini(ini, exp):
    return np.dot(ini, exp)


if __name__ == '__main__':
    n = input('Entre com o tamanho do vetor: ')

    a = vetor_ini(n)
    while verify(a):
        print 'probabilidades do vetor diferente de 1.0 (100%)\nrefaca o processo ate soma das prob. igual a 1'
        a = vetor_ini(n)

    m = matriz_transacao(n)
    exp = exp_matriz(4, m)

    print exp




#matriz_transicao(3)

