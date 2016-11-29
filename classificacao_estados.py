m = ((0.08,0.184,0.368,0.368),(0.632,0.368,0.0, 0.0),(0.264,0.368,0.368,0.0),(0.08,0.184,0.368,0.368))
m1 = ((0.92, -0.632, -0.264, -0.08, 0),(-0.184, 0.632, -0.368, -0.184, 0),(-0.368, 0, 0.632, -0.368, 0),(-0.368, 0, 0, 0.632, 0),(1,1,1,1,1))

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
    
def classificar_estados(n):
    for k in range(0,n):
        rec = 0
        for x in range(0,n):
            rec = rec + F_ij(k, k, x, n)
            if rec >0:
                print 'Recorrente'
            else:
                print 'Transiente'

  
