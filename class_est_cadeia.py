import numpy as np

def c_kolmogorov (mat_prob, n, m, i, j):
    p_ij = 0
    if m == 1:
        return mat_prob[i][j]

    for k in range (n):
        p_ij += mat_prob[i][k] * c_kolmogorov(mat_prob, n, m - 1, k, j )
    return p_ij


# retorna se estado x e' alcancavel de y
def est_alcancavel(m,x, y, n):
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
                res = verifica_alcancavel(m,c,n, y,i, pos_verif_estado);
                if res:
                   for j in range (10000):
                        c[j] = 0;
                   return 1;

        for j in range (10000):
            c[j] = 0
        return 0

def verifica_alcancavel(m,c, n, y, x, pos_verif_estado):
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
            r = verifica_alcancavel(m,c,n,y,i, pos_verif_estado)
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

# verifica se estado e' recorrente
def recorrente (m,est, n):
    res = 1
    if m[est][est]==1:
        return 2

    for i in range (n):
        if i!=est:
            if est_alcancavel(m,est, i, n):
                if ~est_alcancavel(m,i, est, n):
                    res = 0
        if ~res :
            return 0;
    return 1;

def redutivel (m, n):
	teste = 0
	for i in range (n):
		if recorrente(m, i, n) != 0:
			teste +=1
		else:
			return 0
	if teste == n:
		return 1
	return 0

# verifica se a cadeia e regular
def verifica_regular():

	soma = 0
	teste = 0
	geracao=2
	s=0

	# leitura da matriz
	n = input ("Dimensao (n) da matriz: ")
	m = np.zeros((n, n))
	matriz = np.zeros((n,n))
	for i in range (n):
		for j in range (n):
			print "matriz " + str(i) + " " + str(j) + ": "
			m[i][j] = input()
			if m[i][j]<=-1:
				teste=1

	print 'MATRIZ DE TRANSICAO\n'
	print m


	if teste==1:
		print "Nao regular na primeira geracao\n"
	else:
		print "Regular na primeira geracao\n"

	passos = input("Numero de passos: ")
	p=2
	while p != passos+1:
	    teste= 0
	    s= 0
	    for i in range(n):
	        for j in range(n):
	            m[i][j] = c_kolmogorov(matriz, n, p, i, j);

	            if m[i][j]<= -1:
	            	teste = 1

	    if teste==1:
	    	print "GERACAO " + str(geracao)+ " - NAO REGULAR\n"
	    else:
	        print "GERACAO " + str(geracao)+ " - REGULAR\n"

	    for i in range (n):
	        for j in range(n):
	            matriz[i][j]=m[i][j]
	    p += 1
	    geracao += 1

	if ~redutivel(m, n):
		print "\nMATRIZ IRREDUTIVEL"
	else:
		print "\nMATRIZ REDUTIVEL"


verifica_regular()
