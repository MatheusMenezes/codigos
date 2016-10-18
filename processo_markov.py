import numpy as np

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


if __name__ == '__main__':
    n = input('Entre com o tamanho do vetor: ')
    soma = 0

    #while soma != 1.0:
    #    aux = 0
    #    a = vetor_ini(n)
    #    for elem in a:
    #        aux = aux + elem
    #    soma = aux
    #    if soma != 1.0:
    #        print 'probabilidades do vetor diferente de 1.0 (100%)\nrefaca o processo ate soma das prob. igual a 1'

    m = matriz_transacao(n)
    exp = exp_matriz(4, m)
    print exp




#matriz_transicao(3)

