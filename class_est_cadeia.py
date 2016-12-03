import numpy as np

def c_kolmogorov (mat_prob, n, m, i, j):
    p_ij = 0
    if m == 1:
        return mat_prob[i][j]

    for k in range (n):
        p_ij += mat_prob[i][k] * c_kolmogorov(mat_prob, n, m - 1, k, j )
    return p_ij


def verifica_regular():

	soma = 0
	teste = 0
	g=2
	s=0

	n = input ("Dimensao (n) da matriz: ")
	m = np.zeros((n, n))
	matriz = np.zeros((n,n))
	for i in range (n):
		for j in range (n):
			print "matriz " + str(i) + " " + str(j) + ": "
			m[i][j] = input()
			if matriz[i][j]<=-1:
				teste=1

	for i in range(n):
		soma=0
		for j in range(n):
			soma = soma+matriz[i][j]
		if soma!=1:
			s=1

	if teste==1 or s==1:
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

	    for i in range (n):
	        soma=0
	        for j in range(n):
	            soma = soma+m[i][j]
	        if soma!=1:
	        	s = 1


	    if teste==1 or s==1:
	    	print "GERACAO " + str(g)+ " - NAO REGULAR\n"
	    else:

	        print "GERACAO " + str(g)+ " - REGULAR\n"

	    for i in range (n):
	        for j in range(n):
	            matriz[i][j]=m[i][j]
	    p += 1
	    g += 1

verifica_regular()
