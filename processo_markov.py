import numpy as np

# verifica se soma vetor igual a 1. Serve para probabilidade dos vetores.
def verify(a):
    soma = 0
    for elem in a:
        soma = soma + elem
    if soma != 1.0:
        return False
    else:
        return True
# define o vetor de inicializacao
def vetor_ini(n):
    vetor = np.zeros(n)
    while not verify(vetor):
        print 'Entre com o vetor de inicializacao: '
        for i in range(int(n)):
            valor_ini = input("pos[%d]: " %i) #porcentagem
            vetor[i] = valor_ini

    print 'VETOR DE INICIALIZACAo: ',vetor
    return vetor
# define a matriz de transicao
def matriz_transicao(n):
    matriz = np.zeros((n, n))
    print 'Entre com a matriz de transicao: '
    for x in range(int(n)):
        while not verify(matriz[x]):
            for y in range(int(n)):
                matriz[x][y] = input('pos['+str(x)+']['+str(y)+']: ')
    print 'MATRIZ DE TRANSICAO: \n',matriz
    return matriz
# calcula a multiplicacao das matrizes
def exp_matriz(h, m):
    p = m
    for i in range(int(h)-1):
        p = p.dot(m)
    return p
# multiplica vetor de inialicazao com a matriz exponencial
def multi_exp_ini(ini, exp):
    return np.dot(ini, exp)


if __name__ == '__main__':
    print '\n\t\t\t--CADEIA DE MARKOV--\nVALORES DOS VETORES E MATRIZES DEVEM ESTAR NORMALIZADOS ENTRE 0 E 1'
    print 'O VETOR DE INIALIZACAO E MATRIZ DE TRANSICAO ESTAO ZERADOS POR PADRAO\n\n'
    n = int(input('Entre com o tamanho do vetor de inicializacao (n > 0): ')) #tamanho do vetor
    a = np.zeros(n) #vetor de inicialicacao
    m = np.zeros((n,n)) #matriz de transicao
    h = 0 #numero de passos
    exp = np.zeros # (a * m^h)
    flag_a = flag_m = flag_h = False #flags de controle de alteracao das variaveis
    #opt = 1 #opcao dentro do loop
    opt = int(input('1-Definir Vetor de Incialicazao\n2-Definir Matriz de Transicao\n3-Definir numero de passos\n4-Definir qual observar\n0-Sair\nopcao: '))
    while opt:
        if(n <= 0):
            n = input('Entre com o tamanho do vetor de inicializacao (n > 0): ') #tamanho do vetor
        else:
            if opt == 1: #definir vetor de inicialicacao
                a = vetor_ini(n)
                flag_a = True
            if opt == 2: #definir matriz de transicao
                m = matriz_transicao(n)
                flag_m = True
            if opt == 3: #definir numero de passos
                h = input ('Entre com o numero de passos: ')
                flag_h = True
            if opt == 4: #definir qual elemento observar
                exp = 0
                #if flag_a and flag_m and flag_h:
                exp = multi_exp_ini(a, exp_matriz(h, m))
                print 'Probabilidade dos estados: ', exp
            opt = int(input('1-Definir Vetor de Incialicazao\n2-Definir Matriz de Transicao\n3-Definir numero de passos\n4-Definir qual observar\n0-Sair\nopcao: '))


